#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import sqlite3
import subprocess
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


SCHEMA_VERSION = "project_continuity.v1"
CONFIG_SCHEMA = "project_continuity_config.v1"
REGISTRY_SCHEMA = "project_continuity_registry.v1"
SEVERITY_ORDER = {"healthy": 0, "warning": 1, "rotate_required": 2, "error": 3}
LAYERS = {"raw", "normalized", "curated", "analysis", "result"}
HIGH_CONFIDENCE_PRIVATE_KEY_PATTERNS = {
    "open_ssh_private_key": re.compile(
        r"-----BEGIN OPENSSH PRIVATE KEY-----[^\n]*\n(?:[^\n]*\n){1,80}?[^\n]*-----END OPENSSH PRIVATE KEY-----"
    ),
    "rsa_private_key": re.compile(
        r"-----BEGIN RSA PRIVATE KEY-----[^\n]*\n(?:[^\n]*\n){1,200}?[^\n]*-----END RSA PRIVATE KEY-----"
    ),
    "ec_private_key": re.compile(
        r"-----BEGIN EC PRIVATE KEY-----[^\n]*\n(?:[^\n]*\n){1,80}?[^\n]*-----END EC PRIVATE KEY-----"
    ),
    "generic_private_key": re.compile(
        r"-----BEGIN PRIVATE KEY-----[^\n]*\n(?:[^\n]*\n){1,200}?[^\n]*-----END PRIVATE KEY-----"
    ),
}
CREDENTIAL_ASSIGNMENT_PATTERN = re.compile(
    r"(?m)(?:^|:)"
    r"[A-Z][A-Z0-9_]*(?:API_KEY|TOKEN|SECRET|PASSWORD|SESSION)="
    r"(?P<value>[^\s\"']{16,})$"
)


def flatten_tool_output(value: Any) -> str:
    if isinstance(value, str):
        return value
    if isinstance(value, list):
        return "\n".join(flatten_tool_output(item) for item in value)
    if isinstance(value, dict):
        return "\n".join(flatten_tool_output(item) for item in value.values())
    return str(value)


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def parse_time(value: Any) -> datetime | None:
    try:
        return datetime.fromisoformat(str(value).replace("Z", "+00:00")).astimezone(timezone.utc)
    except (TypeError, ValueError):
        return None


def expanded_path(value: Any, base: Path | None = None) -> Path:
    text = os.path.expandvars(os.path.expanduser(str(value or "")))
    path = Path(text)
    if not path.is_absolute() and base is not None:
        path = base / path
    return path.resolve()


def read_json(path: Path, default: Any = None) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        return default


def write_text_atomic(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.{uuid.uuid4().hex}.tmp")
    temporary.write_text(text, encoding="utf-8")
    temporary.replace(path)


def write_json_atomic(path: Path, payload: Any) -> None:
    write_text_atomic(path, json.dumps(payload, ensure_ascii=False, indent=2) + "\n")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def content_hash(payload: Any) -> str:
    encoded = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def high_confidence_secret_markers(path: Path) -> list[str]:
    if not path.is_file():
        return []
    found: set[str] = set()
    with path.open("r", encoding="utf-8", errors="replace") as handle:
        for line in handle:
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                continue
            payload = row.get("payload") or {}
            if row.get("type") != "response_item" or payload.get("type") not in {
                "custom_tool_call_output",
                "function_call_output",
            }:
                continue
            text = flatten_tool_output(payload.get("output", ""))
            for name, pattern in HIGH_CONFIDENCE_PRIVATE_KEY_PATTERNS.items():
                if pattern.search(text):
                    found.add(name)
            for match in CREDENTIAL_ASSIGNMENT_PATTERN.finditer(text):
                value = match.group("value")
                if not value.startswith(("$", "<", "{", "[")) and value.lower() not in {
                    "replace_me",
                    "changeme",
                    "placeholder",
                }:
                    found.add("credential_assignment")
    return sorted(found)


def validate_config(payload: Any, path: Path) -> dict[str, Any]:
    if not isinstance(payload, dict):
        raise ValueError(f"config is not an object: {path}")
    if payload.get("schema") != CONFIG_SCHEMA:
        raise ValueError(f"unsupported config schema: {payload.get('schema')}")
    for key in ("project_id", "name", "project_root"):
        if not str(payload.get(key) or "").strip():
            raise ValueError(f"missing config field: {key}")
    project_id = str(payload["project_id"])
    if not all(character.isalnum() or character in "-_" for character in project_id):
        raise ValueError("project_id may contain only letters, digits, hyphen, and underscore")
    thresholds = payload.get("thresholds")
    if not isinstance(thresholds, dict):
        raise ValueError("thresholds must be an object")
    for metric in ("log_bytes", "tokens_used", "compaction_count", "turn_count"):
        warning = int(thresholds.get(f"{metric}_warning", 0))
        rotate = int(thresholds.get(f"{metric}_rotate", 0))
        if warning <= 0 or rotate <= warning:
            raise ValueError(f"invalid thresholds for {metric}: warning={warning}, rotate={rotate}")
    return payload


def load_config(path_value: str | Path) -> tuple[dict[str, Any], Path]:
    path = expanded_path(path_value)
    payload = validate_config(read_json(path), path)
    payload = dict(payload)
    payload["project_root"] = str(expanded_path(payload["project_root"], path.parent))
    payload["state_db_path"] = str(
        expanded_path(payload.get("state_db_path", "~/.codex/state_5.sqlite"), path.parent)
    )
    payload["runtime_root"] = str(
        expanded_path(
            payload.get("runtime_root", "~/Documents/Codex/runtime/project-continuity"),
            path.parent,
        )
    )
    if payload.get("registry_path"):
        payload["registry_path"] = str(expanded_path(payload["registry_path"], path.parent))
    payload["config_path"] = str(path)
    return payload, path


def runtime_dir(config: dict[str, Any]) -> Path:
    return expanded_path(config["runtime_root"]) / str(config["project_id"])


def database_path(config: dict[str, Any]) -> Path:
    return runtime_dir(config) / "continuity.sqlite3"


SCHEMA_SQL = """
PRAGMA foreign_keys = ON;
CREATE TABLE IF NOT EXISTS projects (
    project_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    root_path TEXT NOT NULL,
    config_path TEXT NOT NULL,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS conversations (
    conversation_id TEXT PRIMARY KEY,
    project_id TEXT NOT NULL REFERENCES projects(project_id) ON DELETE CASCADE,
    title TEXT NOT NULL DEFAULT '',
    rollout_path TEXT NOT NULL,
    archived INTEGER NOT NULL DEFAULT 0,
    log_bytes INTEGER NOT NULL DEFAULT 0,
    tokens_used INTEGER NOT NULL DEFAULT 0,
    turn_count INTEGER NOT NULL DEFAULT 0,
    compaction_count INTEGER NOT NULL DEFAULT 0,
    severity TEXT NOT NULL DEFAULT 'healthy',
    checked_at TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_conversations_project_checked
    ON conversations(project_id, checked_at DESC);
CREATE TABLE IF NOT EXISTS rollout_scan_state (
    rollout_path TEXT PRIMARY KEY,
    project_id TEXT NOT NULL REFERENCES projects(project_id) ON DELETE CASCADE,
    scanned_bytes INTEGER NOT NULL DEFAULT 0,
    turn_count INTEGER NOT NULL DEFAULT 0,
    compaction_count INTEGER NOT NULL DEFAULT 0,
    parse_errors INTEGER NOT NULL DEFAULT 0,
    updated_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS thread_checks (
    check_id TEXT PRIMARY KEY,
    project_id TEXT NOT NULL REFERENCES projects(project_id) ON DELETE CASCADE,
    conversation_id TEXT NOT NULL REFERENCES conversations(conversation_id) ON DELETE CASCADE,
    created_at TEXT NOT NULL,
    severity TEXT NOT NULL,
    fingerprint TEXT NOT NULL,
    metrics_json TEXT NOT NULL,
    reasons_json TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_thread_checks_conversation_created
    ON thread_checks(conversation_id, created_at DESC);
CREATE TABLE IF NOT EXISTS checkpoints (
    checkpoint_id TEXT PRIMARY KEY,
    project_id TEXT NOT NULL REFERENCES projects(project_id) ON DELETE CASCADE,
    conversation_id TEXT REFERENCES conversations(conversation_id) ON DELETE SET NULL,
    created_at TEXT NOT NULL,
    reason TEXT NOT NULL,
    severity TEXT NOT NULL,
    json_path TEXT NOT NULL,
    markdown_path TEXT NOT NULL,
    content_sha256 TEXT NOT NULL,
    git_sha TEXT NOT NULL DEFAULT '',
    snapshot_json TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_checkpoints_project_created
    ON checkpoints(project_id, created_at DESC);
CREATE TABLE IF NOT EXISTS lineage_nodes (
    node_id TEXT PRIMARY KEY,
    project_id TEXT NOT NULL REFERENCES projects(project_id) ON DELETE CASCADE,
    conversation_id TEXT REFERENCES conversations(conversation_id) ON DELETE SET NULL,
    run_id TEXT NOT NULL,
    layer TEXT NOT NULL CHECK(layer IN ('raw','normalized','curated','analysis','result')),
    kind TEXT NOT NULL,
    uri TEXT NOT NULL DEFAULT '',
    content_sha256 TEXT NOT NULL DEFAULT '',
    payload_json TEXT NOT NULL DEFAULT '{}',
    created_at TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_lineage_nodes_project_run
    ON lineage_nodes(project_id, run_id, layer);
CREATE TABLE IF NOT EXISTS lineage_edges (
    parent_node_id TEXT NOT NULL REFERENCES lineage_nodes(node_id) ON DELETE CASCADE,
    child_node_id TEXT NOT NULL REFERENCES lineage_nodes(node_id) ON DELETE CASCADE,
    relation TEXT NOT NULL,
    created_at TEXT NOT NULL,
    PRIMARY KEY(parent_node_id, child_node_id, relation)
);
CREATE TABLE IF NOT EXISTS quality_checks (
    quality_id TEXT PRIMARY KEY,
    project_id TEXT NOT NULL REFERENCES projects(project_id) ON DELETE CASCADE,
    run_id TEXT NOT NULL,
    check_name TEXT NOT NULL,
    ok INTEGER NOT NULL,
    detail TEXT NOT NULL DEFAULT '',
    created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS notifications (
    notification_id TEXT PRIMARY KEY,
    project_id TEXT NOT NULL REFERENCES projects(project_id) ON DELETE CASCADE,
    conversation_id TEXT,
    severity TEXT NOT NULL,
    fingerprint TEXT NOT NULL,
    channel TEXT NOT NULL,
    delivered INTEGER NOT NULL,
    created_at TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_notifications_project_created
    ON notifications(project_id, created_at DESC);
"""


def open_store(config: dict[str, Any]) -> sqlite3.Connection:
    path = database_path(config)
    path.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(path)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    connection.execute("PRAGMA journal_mode = WAL")
    connection.execute("PRAGMA busy_timeout = 5000")
    connection.executescript(SCHEMA_SQL)
    now = utc_now()
    connection.execute(
        """
        INSERT INTO projects(project_id, name, root_path, config_path, created_at, updated_at)
        VALUES(?, ?, ?, ?, ?, ?)
        ON CONFLICT(project_id) DO UPDATE SET
            name=excluded.name,
            root_path=excluded.root_path,
            config_path=excluded.config_path,
            updated_at=excluded.updated_at
        """,
        (
            config["project_id"],
            config["name"],
            config["project_root"],
            config["config_path"],
            now,
            now,
        ),
    )
    connection.commit()
    return connection


def rollout_counts(
    path: Path,
    connection: sqlite3.Connection,
    project_id: str,
) -> dict[str, int]:
    counts = {"turn_count": 0, "compaction_count": 0, "parse_errors": 0}
    if not path.exists():
        return counts
    size = path.stat().st_size
    cached = connection.execute(
        "SELECT * FROM rollout_scan_state WHERE rollout_path=?",
        (str(path),),
    ).fetchone()
    start = 0
    if cached and 0 <= int(cached["scanned_bytes"]) <= size:
        start = int(cached["scanned_bytes"])
        counts = {
            "turn_count": int(cached["turn_count"]),
            "compaction_count": int(cached["compaction_count"]),
            "parse_errors": int(cached["parse_errors"]),
        }
    with path.open("rb") as handle:
        handle.seek(start)
        chunk = handle.read()
    complete_length = len(chunk)
    if chunk and not chunk.endswith(b"\n"):
        last_newline = chunk.rfind(b"\n")
        complete_length = last_newline + 1 if last_newline >= 0 else 0
    for line in chunk[:complete_length].splitlines():
        try:
            row = json.loads(line.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError):
            counts["parse_errors"] += 1
            continue
        row_type = row.get("type")
        if row_type == "turn_context":
            counts["turn_count"] += 1
        elif row_type == "compacted":
            counts["compaction_count"] += 1
    scanned_bytes = start + complete_length
    connection.execute(
        """
        INSERT INTO rollout_scan_state(
            rollout_path, project_id, scanned_bytes, turn_count,
            compaction_count, parse_errors, updated_at
        ) VALUES(?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(rollout_path) DO UPDATE SET
            project_id=excluded.project_id,
            scanned_bytes=excluded.scanned_bytes,
            turn_count=excluded.turn_count,
            compaction_count=excluded.compaction_count,
            parse_errors=excluded.parse_errors,
            updated_at=excluded.updated_at
        """,
        (
            str(path),
            project_id,
            scanned_bytes,
            counts["turn_count"],
            counts["compaction_count"],
            counts["parse_errors"],
            utc_now(),
        ),
    )
    return counts


def read_active_threads(config: dict[str, Any], store: sqlite3.Connection) -> list[dict[str, Any]]:
    state_db = expanded_path(config["state_db_path"])
    if not state_db.exists():
        raise FileNotFoundError(f"Codex state database not found: {state_db}")
    connection = sqlite3.connect(f"file:{state_db}?mode=ro", uri=True)
    connection.row_factory = sqlite3.Row
    try:
        rows = connection.execute(
            """
            SELECT id, title, rollout_path, archived, tokens_used, updated_at, cwd
            FROM threads
            WHERE archived = 0
            ORDER BY updated_at DESC, id DESC
            """
        ).fetchall()
    finally:
        connection.close()
    result = []
    project_root = expanded_path(config["project_root"])
    for row in rows:
        if expanded_path(row["cwd"]) != project_root:
            continue
        rollout = expanded_path(row["rollout_path"])
        counts = rollout_counts(rollout, store, config["project_id"])
        secret_markers = high_confidence_secret_markers(rollout)
        title_preview = str(row["title"] or "").splitlines()[0][:160]
        result.append(
            {
                "conversation_id": row["id"],
                "title": title_preview,
                "rollout_path": str(rollout),
                "rollout_exists": rollout.exists(),
                "log_bytes": rollout.stat().st_size if rollout.exists() else 0,
                "tokens_used": int(row["tokens_used"] or 0),
                "turn_count": counts["turn_count"],
                "compaction_count": counts["compaction_count"],
                "parse_errors": counts["parse_errors"],
                "secret_markers": secret_markers,
                "updated_at_epoch": int(row["updated_at"] or 0),
                "archived": bool(row["archived"]),
            }
        )
    return result


def evaluate_thread(metrics: dict[str, Any], thresholds: dict[str, Any]) -> dict[str, Any]:
    secret_markers = list(metrics.get("secret_markers") or [])
    if secret_markers:
        reasons = [{"metric": "secret_markers", "value": len(secret_markers), "threshold": 0}]
        return {
            "severity": "error",
            "reasons": reasons,
            "fingerprint": content_hash(
                {
                    "conversation_id": metrics.get("conversation_id"),
                    "severity": "error",
                    "secret_markers": secret_markers,
                }
            ),
        }
    warning_reasons = []
    rotate_reasons = []
    for metric in ("log_bytes", "tokens_used", "compaction_count", "turn_count"):
        value = int(metrics.get(metric) or 0)
        warning = int(thresholds[f"{metric}_warning"])
        rotate = int(thresholds[f"{metric}_rotate"])
        if value >= rotate:
            rotate_reasons.append({"metric": metric, "value": value, "threshold": rotate})
        elif value >= warning:
            warning_reasons.append({"metric": metric, "value": value, "threshold": warning})
    if rotate_reasons:
        severity = "rotate_required"
        reasons = rotate_reasons + warning_reasons
    elif warning_reasons:
        severity = "warning"
        reasons = warning_reasons
    else:
        severity = "healthy"
        reasons = []
    fingerprint = content_hash(
        {
            "conversation_id": metrics.get("conversation_id"),
            "severity": severity,
            "reasons": [
                {"metric": row["metric"], "threshold": row["threshold"]}
                for row in reasons
            ],
        }
    )
    return {"severity": severity, "reasons": reasons, "fingerprint": fingerprint}


def persist_thread_check(
    connection: sqlite3.Connection,
    config: dict[str, Any],
    metrics: dict[str, Any],
    evaluation: dict[str, Any],
) -> dict[str, Any]:
    checked_at = utc_now()
    conversation_id = metrics["conversation_id"]
    connection.execute(
        """
        INSERT INTO conversations(
            conversation_id, project_id, title, rollout_path, archived, log_bytes,
            tokens_used, turn_count, compaction_count, severity, checked_at
        ) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(conversation_id) DO UPDATE SET
            title=excluded.title,
            rollout_path=excluded.rollout_path,
            archived=excluded.archived,
            log_bytes=excluded.log_bytes,
            tokens_used=excluded.tokens_used,
            turn_count=excluded.turn_count,
            compaction_count=excluded.compaction_count,
            severity=excluded.severity,
            checked_at=excluded.checked_at
        """,
        (
            conversation_id,
            config["project_id"],
            metrics.get("title", ""),
            metrics.get("rollout_path", ""),
            int(bool(metrics.get("archived"))),
            metrics.get("log_bytes", 0),
            metrics.get("tokens_used", 0),
            metrics.get("turn_count", 0),
            metrics.get("compaction_count", 0),
            evaluation["severity"],
            checked_at,
        ),
    )
    check_id = str(uuid.uuid4())
    connection.execute(
        """
        INSERT INTO thread_checks(
            check_id, project_id, conversation_id, created_at, severity,
            fingerprint, metrics_json, reasons_json
        ) VALUES(?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            check_id,
            config["project_id"],
            conversation_id,
            checked_at,
            evaluation["severity"],
            evaluation["fingerprint"],
            json.dumps(metrics, ensure_ascii=False, sort_keys=True),
            json.dumps(evaluation["reasons"], ensure_ascii=False, sort_keys=True),
        ),
    )
    connection.commit()
    return {
        "check_id": check_id,
        "checked_at": checked_at,
        "metrics": metrics,
        **evaluation,
    }


def run_git(project_root: Path, *args: str) -> str:
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=project_root,
            text=True,
            capture_output=True,
            timeout=10,
            check=False,
        )
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return ""
    return result.stdout.strip() if result.returncode == 0 else ""


def git_snapshot(project_root: Path) -> dict[str, Any]:
    status_lines = run_git(project_root, "status", "--short").splitlines()
    return {
        "head": run_git(project_root, "rev-parse", "HEAD"),
        "branch": run_git(project_root, "branch", "--show-current"),
        "origin": run_git(project_root, "remote", "get-url", "origin"),
        "dirty": bool(status_lines),
        "status": status_lines[:50],
    }


def file_snapshot(entry: Any, config_path: Path) -> dict[str, Any]:
    if isinstance(entry, str):
        path_value, role, required = entry, "context", True
    elif isinstance(entry, dict):
        path_value = entry.get("path", "")
        role = str(entry.get("role") or "context")
        required = bool(entry.get("required", True))
    else:
        return {"path": "", "role": "invalid", "required": True, "exists": False}
    path = expanded_path(path_value, config_path.parent)
    exists = path.is_file()
    return {
        "path": str(path),
        "role": role,
        "required": required,
        "exists": exists,
        "size": path.stat().st_size if exists else 0,
        "modified_at_epoch": int(path.stat().st_mtime) if exists else 0,
        "sha256": sha256_file(path) if exists else "",
    }


def insert_lineage_node(
    connection: sqlite3.Connection,
    config: dict[str, Any],
    conversation_id: str | None,
    run_id: str,
    layer: str,
    kind: str,
    *,
    uri: str = "",
    sha256: str = "",
    payload: Any = None,
) -> str:
    if layer not in LAYERS:
        raise ValueError(f"unsupported lineage layer: {layer}")
    node_id = str(uuid.uuid4())
    connection.execute(
        """
        INSERT INTO lineage_nodes(
            node_id, project_id, conversation_id, run_id, layer, kind, uri,
            content_sha256, payload_json, created_at
        ) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            node_id,
            config["project_id"],
            conversation_id,
            run_id,
            layer,
            kind,
            uri,
            sha256,
            json.dumps(payload or {}, ensure_ascii=False, sort_keys=True),
            utc_now(),
        ),
    )
    return node_id


def link_nodes(connection: sqlite3.Connection, parent: str, child: str, relation: str) -> None:
    connection.execute(
        "INSERT INTO lineage_edges(parent_node_id, child_node_id, relation, created_at) VALUES(?, ?, ?, ?)",
        (parent, child, relation, utc_now()),
    )


def render_resume_packet(snapshot: dict[str, Any]) -> str:
    thread = snapshot.get("thread") or {}
    evaluation = snapshot.get("evaluation") or {}
    git = snapshot.get("git") or {}
    lines = [
        "# Project Resume Packet",
        "",
        f"- project_id: `{snapshot['project_id']}`",
        f"- project_name: `{snapshot['project_name']}`",
        f"- checkpoint_id: `{snapshot['checkpoint_id']}`",
        f"- created_at: `{snapshot['created_at']}`",
        f"- reason: `{snapshot['reason']}`",
        f"- severity: `{evaluation.get('severity', 'healthy')}`",
        f"- project_root: `{snapshot['project_root']}`",
        f"- git: `{git.get('branch', '')}` / `{git.get('head', '')[:12]}` / dirty=`{git.get('dirty', False)}`",
        "",
        "## Conversation State",
        "",
        f"- conversation_id: `{thread.get('conversation_id', '')}`",
        f"- log_bytes: `{thread.get('log_bytes', 0)}`",
        f"- tokens_used: `{thread.get('tokens_used', 0)}`",
        f"- turn_count: `{thread.get('turn_count', 0)}`",
        f"- compaction_count: `{thread.get('compaction_count', 0)}`",
        "",
        "## Required Context",
        "",
    ]
    for row in snapshot.get("context_files", []):
        state = "ok" if row.get("exists") else "missing"
        lines.append(f"- `{row.get('role')}`: `{row.get('path')}` ({state})")
    lines.extend(["", "## Runtime Evidence", ""])
    for row in snapshot.get("health_files", []):
        state = "ok" if row.get("exists") else "missing"
        lines.append(f"- `{row.get('role')}`: `{row.get('path')}` ({state})")
    lines.extend(
        [
            "",
            "## Recovery Safety",
            "",
            "1. Read only the listed context/runtime files and narrowly selected Git-tracked source.",
            "2. Do not recursively search hidden or untracked paths such as `.deploy`, `.env*`, private-key files, credential stores, or session files.",
            "3. Use listed secret-free runbooks or deployment entrypoints for connection metadata.",
            "4. If secret-like output appears, stop without reproducing it, rotate the credential, and reject this task for continued use.",
            "",
            "## Resume Procedure",
            "",
            "1. Read the required context files listed above.",
            "2. Run `git status --short --branch` in the project root.",
            "3. Verify current runtime evidence before making a live conclusion.",
            "4. Continue unresolved work from project memory; do not replay completed operations.",
            "5. Keep large raw outputs in files or SQLite and return only summaries plus evidence IDs.",
            "",
            "## New Conversation Bootstrap",
            "",
            f"Resume project `{snapshot['project_id']}` from checkpoint `{snapshot['checkpoint_id']}`. "
            "Load the latest project-continuity resume packet, verify git/runtime state, and continue without importing the old conversation log.",
            "",
        ]
    )
    return "\n".join(lines)


def create_checkpoint(
    connection: sqlite3.Connection,
    config: dict[str, Any],
    config_path: Path,
    check: dict[str, Any],
    reason: str,
) -> dict[str, Any]:
    checkpoint_id = str(uuid.uuid4())
    created_at = utc_now()
    project_root = expanded_path(config["project_root"])
    context_files = [file_snapshot(row, config_path) for row in config.get("context_files", [])]
    health_files = [file_snapshot(row, config_path) for row in config.get("health_files", [])]
    snapshot = {
        "schema": SCHEMA_VERSION,
        "checkpoint_id": checkpoint_id,
        "project_id": config["project_id"],
        "project_name": config["name"],
        "project_root": str(project_root),
        "created_at": created_at,
        "reason": reason,
        "thread": check.get("metrics") or {},
        "evaluation": {
            "severity": check.get("severity", "healthy"),
            "reasons": check.get("reasons") or [],
            "fingerprint": check.get("fingerprint", ""),
        },
        "git": git_snapshot(project_root),
        "context_files": context_files,
        "health_files": health_files,
        "resume_command": (
            f"python3 ~/.codex/skills/project-continuity/scripts/project_continuity.py resume "
            f"--config {config_path}"
        ),
    }
    handoff_dir = runtime_dir(config) / "handoff"
    stamp = created_at.replace("+00:00", "Z").replace(":", "").replace("-", "")
    json_path = handoff_dir / f"{stamp}_{checkpoint_id}.json"
    markdown_path = handoff_dir / f"{stamp}_{checkpoint_id}.md"
    write_json_atomic(json_path, snapshot)
    markdown = render_resume_packet(snapshot)
    write_text_atomic(markdown_path, markdown)
    write_json_atomic(handoff_dir / "latest.json", snapshot)
    write_text_atomic(handoff_dir / "latest.md", markdown)
    wiki_path = runtime_dir(config) / "wiki" / "project-state.md"
    write_text_atomic(wiki_path, markdown)
    snapshot_sha = sha256_file(json_path)
    conversation_id = str((check.get("metrics") or {}).get("conversation_id") or "") or None
    connection.execute(
        """
        INSERT INTO checkpoints(
            checkpoint_id, project_id, conversation_id, created_at, reason, severity,
            json_path, markdown_path, content_sha256, git_sha, snapshot_json
        ) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            checkpoint_id,
            config["project_id"],
            conversation_id,
            created_at,
            reason,
            check.get("severity", "healthy"),
            str(json_path),
            str(markdown_path),
            snapshot_sha,
            snapshot["git"].get("head", ""),
            json.dumps(snapshot, ensure_ascii=False, sort_keys=True),
        ),
    )
    raw_path = expanded_path((check.get("metrics") or {}).get("rollout_path", ""))
    raw_node = insert_lineage_node(
        connection,
        config,
        conversation_id,
        checkpoint_id,
        "raw",
        "codex_rollout",
        uri=str(raw_path),
        sha256=sha256_file(raw_path) if raw_path.is_file() else "",
        payload={"size": raw_path.stat().st_size if raw_path.is_file() else 0},
    )
    normalized_node = insert_lineage_node(
        connection,
        config,
        conversation_id,
        checkpoint_id,
        "normalized",
        "thread_metrics",
        payload=check,
    )
    curated_node = insert_lineage_node(
        connection,
        config,
        conversation_id,
        checkpoint_id,
        "curated",
        "checkpoint",
        uri=str(json_path),
        sha256=snapshot_sha,
    )
    result_node = insert_lineage_node(
        connection,
        config,
        conversation_id,
        checkpoint_id,
        "result",
        "resume_packet",
        uri=str(markdown_path),
        sha256=sha256_file(markdown_path),
    )
    link_nodes(connection, raw_node, normalized_node, "summarized_as")
    link_nodes(connection, normalized_node, curated_node, "checkpointed_as")
    link_nodes(connection, curated_node, result_node, "rendered_as")
    connection.commit()
    return {
        "checkpoint_id": checkpoint_id,
        "json_path": str(json_path),
        "markdown_path": str(markdown_path),
        "wiki_path": str(wiki_path),
        "sha256": snapshot_sha,
    }


def latest_checkpoint(connection: sqlite3.Connection, project_id: str) -> sqlite3.Row | None:
    return connection.execute(
        "SELECT * FROM checkpoints WHERE project_id=? ORDER BY created_at DESC LIMIT 1",
        (project_id,),
    ).fetchone()


def notification_needed(
    connection: sqlite3.Connection,
    config: dict[str, Any],
    check: dict[str, Any],
) -> bool:
    if check["severity"] == "healthy":
        return False
    latest = connection.execute(
        """
        SELECT fingerprint, created_at FROM notifications
        WHERE project_id=? AND conversation_id=? AND delivered=1
        ORDER BY created_at DESC LIMIT 1
        """,
        (config["project_id"], check["metrics"]["conversation_id"]),
    ).fetchone()
    if not latest or latest["fingerprint"] != check["fingerprint"]:
        return True
    sent_at = parse_time(latest["created_at"])
    cooldown = int(config["thresholds"].get("notification_cooldown_seconds", 43200))
    return sent_at is None or (datetime.now(timezone.utc) - sent_at).total_seconds() >= cooldown


def notify_macos(config: dict[str, Any], check: dict[str, Any]) -> bool:
    if sys.platform != "darwin" or not shutil.which("osascript"):
        return False
    severity = check["severity"]
    metrics = check["metrics"]
    if severity == "error":
        message = f"{config['name']} 对话检测到高置信度敏感输出，请立即停止使用并轮换凭证。"
    elif severity == "rotate_required":
        message = f"{config['name']} 对话达到轮换阈值，请使用最新恢复包新建对话。"
    else:
        message = (
            f"{config['name']} 对话进入预警区：压缩{metrics.get('compaction_count', 0)}次，"
            f"日志{metrics.get('log_bytes', 0) // (1024 * 1024)}MB。"
        )
    script = (
        f'display notification {json.dumps(message, ensure_ascii=False)} '
        f'with title {json.dumps("Codex 对话阈值提醒", ensure_ascii=False)}'
    )
    result = subprocess.run(["osascript", "-e", script], capture_output=True, text=True, check=False)
    return result.returncode == 0


def maybe_record_notification(
    connection: sqlite3.Connection,
    config: dict[str, Any],
    check: dict[str, Any],
    *,
    notify: bool,
) -> dict[str, Any]:
    needed = notification_needed(connection, config, check)
    delivered = False
    if needed and notify:
        delivered = notify_macos(config, check)
        connection.execute(
            """
            INSERT INTO notifications(
                notification_id, project_id, conversation_id, severity,
                fingerprint, channel, delivered, created_at
            ) VALUES(?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                str(uuid.uuid4()),
                config["project_id"],
                check["metrics"]["conversation_id"],
                check["severity"],
                check["fingerprint"],
                "macos_notification",
                int(delivered),
                utc_now(),
            ),
        )
        connection.commit()
    return {"needed": needed, "attempted": bool(needed and notify), "delivered": delivered}


def should_checkpoint(connection: sqlite3.Connection, config: dict[str, Any], check: dict[str, Any]) -> bool:
    if check["severity"] in {"healthy", "error"}:
        return False
    latest = latest_checkpoint(connection, config["project_id"])
    if not latest:
        return True
    snapshot = json.loads(latest["snapshot_json"])
    previous_fingerprint = (snapshot.get("evaluation") or {}).get("fingerprint")
    if previous_fingerprint != check["fingerprint"]:
        return True
    created_at = parse_time(latest["created_at"])
    cooldown = int(config["thresholds"].get("checkpoint_cooldown_seconds", 86400))
    return created_at is None or (datetime.now(timezone.utc) - created_at).total_seconds() >= cooldown


def check_project(
    config_path_value: str | Path,
    *,
    notify: bool = False,
    auto_checkpoint: bool = True,
) -> dict[str, Any]:
    config, config_path = load_config(config_path_value)
    connection = open_store(config)
    try:
        threads = read_active_threads(config, connection)
        if not threads:
            result = {
                "schema": SCHEMA_VERSION,
                "project_id": config["project_id"],
                "checked_at": utc_now(),
                "severity": "error",
                "reasons": [{"metric": "active_thread", "value": 0, "threshold": 1}],
                "notification": {"needed": False, "attempted": False, "delivered": False},
                "error": "no active Codex thread found for project_root",
            }
        else:
            metrics = next((row for row in threads if row.get("secret_markers")), threads[0])
            evaluation = evaluate_thread(metrics, config["thresholds"])
            check = persist_thread_check(connection, config, metrics, evaluation)
            checkpoint = None
            if auto_checkpoint and should_checkpoint(connection, config, check):
                checkpoint = create_checkpoint(
                    connection,
                    config,
                    config_path,
                    check,
                    reason=f"automatic_{check['severity']}",
                )
            notification = maybe_record_notification(connection, config, check, notify=notify)
            result = {
                "schema": SCHEMA_VERSION,
                "project_id": config["project_id"],
                "project_name": config["name"],
                "checked_at": check["checked_at"],
                "severity": check["severity"],
                "reasons": check["reasons"],
                "metrics": check["metrics"],
                "checkpoint": checkpoint,
                "notification": notification,
                "runtime_dir": str(runtime_dir(config)),
            }
        write_json_atomic(runtime_dir(config) / "alerts" / "latest.json", result)
        write_text_atomic(runtime_dir(config) / "alerts" / "latest.md", render_check(result))
        return result
    finally:
        connection.close()


def render_check(result: dict[str, Any]) -> str:
    metrics = result.get("metrics") or {}
    lines = [
        "# Project Continuity Check",
        "",
        f"- project_id: `{result.get('project_id', '')}`",
        f"- checked_at: `{result.get('checked_at', '')}`",
        f"- severity: `{result.get('severity', '')}`",
        f"- conversation_id: `{metrics.get('conversation_id', '')}`",
        f"- log_bytes: `{metrics.get('log_bytes', 0)}`",
        f"- tokens_used: `{metrics.get('tokens_used', 0)}`",
        f"- turn_count: `{metrics.get('turn_count', 0)}`",
        f"- compaction_count: `{metrics.get('compaction_count', 0)}`",
        "",
    ]
    if result.get("reasons"):
        lines.extend(["## Reasons", ""])
        for reason in result["reasons"]:
            lines.append(f"- `{reason.get('metric')}`: `{reason.get('value')}` >= `{reason.get('threshold')}`")
        lines.append("")
    return "\n".join(lines)


def load_registry(path_value: str | Path) -> tuple[dict[str, Any], Path]:
    path = expanded_path(path_value)
    payload = read_json(path, {"schema": REGISTRY_SCHEMA, "projects": []})
    if not isinstance(payload, dict) or payload.get("schema") != REGISTRY_SCHEMA:
        raise ValueError(f"invalid registry: {path}")
    if not isinstance(payload.get("projects"), list):
        raise ValueError(f"registry projects must be a list: {path}")
    return payload, path


def register_config(config_path_value: str | Path, registry_path_value: str | Path) -> dict[str, Any]:
    config, config_path = load_config(config_path_value)
    registry, registry_path = load_registry(registry_path_value)
    projects = [row for row in registry["projects"] if row.get("config") != str(config_path)]
    projects.append({"project_id": config["project_id"], "config": str(config_path), "enabled": True})
    registry["projects"] = sorted(projects, key=lambda row: str(row.get("project_id") or ""))
    registry["updated_at"] = utc_now()
    write_json_atomic(registry_path, registry)
    return {"registry": str(registry_path), "project_id": config["project_id"], "registered": True}


def check_all(registry_path_value: str | Path, *, notify: bool = False) -> dict[str, Any]:
    registry, registry_path = load_registry(registry_path_value)
    results = []
    for row in registry["projects"]:
        if not row.get("enabled", True):
            continue
        try:
            results.append(check_project(row["config"], notify=notify, auto_checkpoint=True))
        except Exception as exc:
            results.append(
                {
                    "project_id": row.get("project_id", ""),
                    "severity": "error",
                    "error": str(exc),
                    "notification": {"needed": True, "attempted": False, "delivered": False},
                }
            )
    severity = max((row.get("severity", "healthy") for row in results), key=lambda item: SEVERITY_ORDER[item], default="healthy")
    return {
        "schema": SCHEMA_VERSION,
        "registry": str(registry_path),
        "checked_at": utc_now(),
        "severity": severity,
        "project_count": len(results),
        "alert_count": sum(1 for row in results if row.get("severity") != "healthy"),
        "notification_count": sum(1 for row in results if (row.get("notification") or {}).get("needed")),
        "projects": results,
    }


def checkpoint_command(config_path_value: str | Path, reason: str) -> dict[str, Any]:
    config, config_path = load_config(config_path_value)
    connection = open_store(config)
    try:
        threads = read_active_threads(config, connection)
        if not threads:
            raise RuntimeError("no active Codex thread found for project_root")
        metrics = threads[0]
        evaluation = evaluate_thread(metrics, config["thresholds"])
        check = persist_thread_check(connection, config, metrics, evaluation)
        return create_checkpoint(connection, config, config_path, check, reason=reason)
    finally:
        connection.close()


def resume_project(config_path_value: str | Path, *, as_json: bool = False) -> tuple[str, int]:
    config, _ = load_config(config_path_value)
    connection = open_store(config)
    try:
        row = latest_checkpoint(connection, config["project_id"])
        if not row:
            return "No checkpoint exists. Run the checkpoint command first.\n", 1
        json_path = expanded_path(row["json_path"])
        markdown_path = expanded_path(row["markdown_path"])
        valid_hash = json_path.is_file() and sha256_file(json_path) == row["content_sha256"]
        live_git = git_snapshot(expanded_path(config["project_root"]))
        if as_json:
            payload = {
                "schema": SCHEMA_VERSION,
                "project_id": config["project_id"],
                "checkpoint_id": row["checkpoint_id"],
                "checkpoint_hash_valid": valid_hash,
                "checkpoint": read_json(json_path, {}),
                "live_git": live_git,
            }
            return json.dumps(payload, ensure_ascii=False, indent=2) + "\n", 0 if valid_hash else 1
        body = markdown_path.read_text(encoding="utf-8") if markdown_path.is_file() else ""
        tail = [
            "## Live Resume Verification",
            "",
            f"- checkpoint_hash_valid: `{valid_hash}`",
            f"- live_git_head: `{live_git.get('head', '')[:12]}`",
            f"- live_git_branch: `{live_git.get('branch', '')}`",
            f"- live_git_dirty: `{live_git.get('dirty', False)}`",
            "",
        ]
        return body.rstrip() + "\n\n" + "\n".join(tail), 0 if valid_hash else 1
    finally:
        connection.close()


def audit_project(config_path_value: str | Path) -> tuple[dict[str, Any], int]:
    config, config_path = load_config(config_path_value)
    connection = open_store(config)
    checks = []
    try:
        foreign_keys = connection.execute("PRAGMA foreign_key_check").fetchall()
        checks.append({"name": "foreign keys", "ok": not foreign_keys, "detail": f"violations={len(foreign_keys)}"})
        orphan_edges = connection.execute(
            """
            SELECT COUNT(*) FROM lineage_edges edge
            LEFT JOIN lineage_nodes parent ON parent.node_id=edge.parent_node_id
            LEFT JOIN lineage_nodes child ON child.node_id=edge.child_node_id
            WHERE parent.node_id IS NULL OR child.node_id IS NULL
            """
        ).fetchone()[0]
        checks.append({"name": "lineage edges", "ok": orphan_edges == 0, "detail": f"orphans={orphan_edges}"})
        latest = latest_checkpoint(connection, config["project_id"])
        if latest:
            path = expanded_path(latest["json_path"])
            hash_ok = path.is_file() and sha256_file(path) == latest["content_sha256"]
            checks.append({"name": "latest checkpoint hash", "ok": hash_ok, "detail": str(path)})
        else:
            checks.append({"name": "latest checkpoint hash", "ok": False, "detail": "missing checkpoint"})
        for entry in config.get("context_files", []):
            row = file_snapshot(entry, config_path)
            if row["required"]:
                checks.append({"name": f"required context: {row['role']}", "ok": row["exists"], "detail": row["path"]})
        active_threads = read_active_threads(config, connection)
        exposed = [row for row in active_threads if row.get("secret_markers")]
        marker_names = sorted({name for row in exposed for name in row.get("secret_markers", [])})
        checks.append(
            {
                "name": "active rollout secret markers",
                "ok": not exposed,
                "detail": f"conversations={len(exposed)}, markers={','.join(marker_names) or 'none'}",
            }
        )
        node_count = connection.execute(
            "SELECT COUNT(*) FROM lineage_nodes WHERE project_id=?", (config["project_id"],)
        ).fetchone()[0]
        checks.append({"name": "lineage populated", "ok": node_count >= 4, "detail": f"nodes={node_count}"})
        run_id = f"audit-{uuid.uuid4()}"
        for row in checks:
            connection.execute(
                """
                INSERT INTO quality_checks(
                    quality_id, project_id, run_id, check_name, ok, detail, created_at
                ) VALUES(?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    str(uuid.uuid4()),
                    config["project_id"],
                    run_id,
                    row["name"],
                    int(row["ok"]),
                    row["detail"],
                    utc_now(),
                ),
            )
        connection.commit()
        failed = [row for row in checks if not row["ok"]]
        payload = {
            "schema": SCHEMA_VERSION,
            "project_id": config["project_id"],
            "generated_at": utc_now(),
            "status": "pass" if not failed else "fail",
            "failed_count": len(failed),
            "checks": checks,
        }
        audit_dir = runtime_dir(config) / "audit"
        write_json_atomic(audit_dir / "latest.json", payload)
        lines = ["# Project Continuity Audit", "", f"- status: `{payload['status']}`", "", "| Check | Status | Detail |", "| --- | --- | --- |"]
        for row in checks:
            lines.append(f"| {row['name']} | {'PASS' if row['ok'] else 'FAIL'} | {row['detail']} |")
        lines.append("")
        write_text_atomic(audit_dir / "latest.md", "\n".join(lines))
        return payload, 0 if not failed else 1
    finally:
        connection.close()


def purge_plan(config_path_value: str | Path, scope: str, conversation_id: str = "") -> dict[str, Any]:
    config, _ = load_config(config_path_value)
    root = runtime_dir(config)
    connection = open_store(config)
    try:
        if scope == "project":
            counts = {}
            for table in ("conversations", "thread_checks", "checkpoints", "lineage_nodes", "lineage_edges", "quality_checks", "notifications"):
                counts[table] = connection.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
            files = [str(path) for path in root.rglob("*") if path.is_file()]
        else:
            if not conversation_id:
                raise ValueError("conversation_id is required for conversation purge")
            counts = {
                "conversations": connection.execute("SELECT COUNT(*) FROM conversations WHERE conversation_id=?", (conversation_id,)).fetchone()[0],
                "thread_checks": connection.execute("SELECT COUNT(*) FROM thread_checks WHERE conversation_id=?", (conversation_id,)).fetchone()[0],
                "checkpoints": connection.execute("SELECT COUNT(*) FROM checkpoints WHERE conversation_id=?", (conversation_id,)).fetchone()[0],
                "lineage_nodes": connection.execute("SELECT COUNT(*) FROM lineage_nodes WHERE conversation_id=?", (conversation_id,)).fetchone()[0],
            }
            checkpoint_rows = connection.execute(
                "SELECT json_path, markdown_path FROM checkpoints WHERE conversation_id=?", (conversation_id,)
            ).fetchall()
            files = [str(path) for row in checkpoint_rows for path in (expanded_path(row["json_path"]), expanded_path(row["markdown_path"]))]
        return {
            "schema": SCHEMA_VERSION,
            "project_id": config["project_id"],
            "scope": scope,
            "conversation_id": conversation_id,
            "runtime_root": str(root),
            "database_counts": counts,
            "managed_files": files,
            "external_data_not_managed": [
                config["project_root"],
                "Codex cloud chat retention",
                "Saved Memory",
                "Git remotes and deployed servers",
            ],
            "confirmation": f"DELETE:{config['project_id']}" + (f":{conversation_id}" if scope == "conversation" else ""),
        }
    finally:
        connection.close()


def purge_runtime(
    config_path_value: str | Path,
    scope: str,
    confirmation: str,
    conversation_id: str = "",
) -> dict[str, Any]:
    plan = purge_plan(config_path_value, scope, conversation_id)
    if confirmation != plan["confirmation"]:
        raise ValueError("confirmation token does not match purge plan")
    config, _ = load_config(config_path_value)
    root = runtime_dir(config)
    allowed_parent = expanded_path(config["runtime_root"])
    if root.parent != allowed_parent or root.name != config["project_id"]:
        raise RuntimeError(f"refusing to purge unsafe runtime path: {root}")
    if scope == "project":
        registry_path = config.get("registry_path")
        if registry_path and expanded_path(registry_path).exists():
            registry, registry_file = load_registry(registry_path)
            for row in registry["projects"]:
                if row.get("project_id") == config["project_id"]:
                    row["enabled"] = False
            registry["updated_at"] = utc_now()
            write_json_atomic(registry_file, registry)
        if root.exists():
            shutil.rmtree(root)
        return {"project_id": config["project_id"], "scope": scope, "purged": True, "path": str(root)}
    connection = open_store(config)
    try:
        paths = connection.execute(
            "SELECT json_path, markdown_path FROM checkpoints WHERE conversation_id=?", (conversation_id,)
        ).fetchall()
        connection.execute("DELETE FROM lineage_nodes WHERE conversation_id=?", (conversation_id,))
        connection.execute("DELETE FROM checkpoints WHERE conversation_id=?", (conversation_id,))
        connection.execute("DELETE FROM notifications WHERE conversation_id=?", (conversation_id,))
        connection.execute("DELETE FROM conversations WHERE conversation_id=?", (conversation_id,))
        connection.commit()
        for row in paths:
            for value in (row["json_path"], row["markdown_path"]):
                path = expanded_path(value)
                if root in path.parents:
                    path.unlink(missing_ok=True)
        remaining = latest_checkpoint(connection, config["project_id"])
        latest_json = root / "handoff" / "latest.json"
        latest_markdown = root / "handoff" / "latest.md"
        wiki_path = root / "wiki" / "project-state.md"
        if remaining:
            source_json = expanded_path(remaining["json_path"])
            source_markdown = expanded_path(remaining["markdown_path"])
            if source_json.is_file():
                write_text_atomic(latest_json, source_json.read_text(encoding="utf-8"))
            if source_markdown.is_file():
                markdown = source_markdown.read_text(encoding="utf-8")
                write_text_atomic(latest_markdown, markdown)
                write_text_atomic(wiki_path, markdown)
        else:
            latest_json.unlink(missing_ok=True)
            latest_markdown.unlink(missing_ok=True)
            wiki_path.unlink(missing_ok=True)
        return {
            "project_id": config["project_id"],
            "scope": scope,
            "conversation_id": conversation_id,
            "purged": True,
        }
    finally:
        connection.close()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Track project lineage and rotate long Codex tasks safely.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser("init", help="Initialize the project continuity database.")
    init_parser.add_argument("--config", required=True)

    check_parser = subparsers.add_parser("check", help="Check the newest active thread for one project.")
    check_parser.add_argument("--config", required=True)
    check_parser.add_argument("--notify", action="store_true")
    check_parser.add_argument("--no-checkpoint", action="store_true")

    all_parser = subparsers.add_parser("check-all", help="Check every enabled project in a registry.")
    all_parser.add_argument("--registry", required=True)
    all_parser.add_argument("--notify", action="store_true")

    register_parser = subparsers.add_parser("register", help="Register a project config for scheduled checks.")
    register_parser.add_argument("--config", required=True)
    register_parser.add_argument("--registry", required=True)

    checkpoint_parser = subparsers.add_parser("checkpoint", help="Create a project checkpoint and resume packet.")
    checkpoint_parser.add_argument("--config", required=True)
    checkpoint_parser.add_argument("--reason", default="manual")

    resume_parser = subparsers.add_parser("resume", help="Render the latest verified resume packet.")
    resume_parser.add_argument("--config", required=True)
    resume_parser.add_argument("--json", action="store_true")

    audit_parser = subparsers.add_parser("audit", help="Audit database lineage and checkpoint integrity.")
    audit_parser.add_argument("--config", required=True)

    plan_parser = subparsers.add_parser("purge-plan", help="Preview runtime data affected by a purge.")
    plan_parser.add_argument("--config", required=True)
    plan_parser.add_argument("--scope", choices=("conversation", "project"), required=True)
    plan_parser.add_argument("--conversation-id", default="")

    purge_parser = subparsers.add_parser("purge", help="Purge managed runtime data after exact confirmation.")
    purge_parser.add_argument("--config", required=True)
    purge_parser.add_argument("--scope", choices=("conversation", "project"), required=True)
    purge_parser.add_argument("--conversation-id", default="")
    purge_parser.add_argument("--confirm", required=True)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        if args.command == "init":
            config, _ = load_config(args.config)
            connection = open_store(config)
            connection.close()
            payload = {
                "schema": SCHEMA_VERSION,
                "project_id": config["project_id"],
                "database": str(database_path(config)),
                "initialized": True,
            }
            print(json.dumps(payload, ensure_ascii=False, indent=2))
            return 0
        if args.command == "check":
            payload = check_project(args.config, notify=args.notify, auto_checkpoint=not args.no_checkpoint)
            print(json.dumps(payload, ensure_ascii=False, indent=2))
            return 0 if payload["severity"] != "error" else 1
        if args.command == "check-all":
            payload = check_all(args.registry, notify=args.notify)
            print(json.dumps(payload, ensure_ascii=False, indent=2))
            return 0 if payload["severity"] != "error" else 1
        if args.command == "register":
            print(json.dumps(register_config(args.config, args.registry), ensure_ascii=False, indent=2))
            return 0
        if args.command == "checkpoint":
            print(json.dumps(checkpoint_command(args.config, args.reason), ensure_ascii=False, indent=2))
            return 0
        if args.command == "resume":
            text, status = resume_project(args.config, as_json=args.json)
            print(text, end="")
            return status
        if args.command == "audit":
            payload, status = audit_project(args.config)
            print(json.dumps(payload, ensure_ascii=False, indent=2))
            return status
        if args.command == "purge-plan":
            print(json.dumps(purge_plan(args.config, args.scope, args.conversation_id), ensure_ascii=False, indent=2))
            return 0
        if args.command == "purge":
            payload = purge_runtime(args.config, args.scope, args.confirm, args.conversation_id)
            print(json.dumps(payload, ensure_ascii=False, indent=2))
            return 0
    except Exception as exc:
        print(json.dumps({"status": "error", "error": str(exc)}, ensure_ascii=False, indent=2), file=sys.stderr)
        return 1
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
