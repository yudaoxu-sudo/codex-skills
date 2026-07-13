#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import sqlite3
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


MODULE_PATH = Path(__file__).with_name("project_continuity.py")
SPEC = importlib.util.spec_from_file_location("project_continuity", MODULE_PATH)
assert SPEC and SPEC.loader
PC = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(PC)


class ProjectContinuityTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.project = self.root / "project"
        self.project.mkdir()
        self.memory = self.root / "memory.md"
        self.memory.write_text("# Project Memory\n\n- current state\n", encoding="utf-8")
        self.health = self.project / "health.json"
        self.health.write_text('{"status":"healthy"}\n', encoding="utf-8")
        self.rollout = self.root / "rollout.jsonl"
        self.write_rollout(turns=4, compactions=3)
        self.state_db = self.root / "state.sqlite"
        self.create_state_db(tokens_used=600)
        self.registry = self.root / "registry.json"
        self.config = self.project / "continuity.json"
        self.config.write_text(
            json.dumps(
                {
                    "schema": "project_continuity_config.v1",
                    "project_id": "test-project",
                    "name": "Test Project",
                    "project_root": str(self.project),
                    "state_db_path": str(self.state_db),
                    "runtime_root": str(self.root / "runtime"),
                    "registry_path": str(self.registry),
                    "context_files": [
                        {"path": str(self.memory), "role": "project_memory", "required": True}
                    ],
                    "health_files": [
                        {"path": str(self.health), "role": "runtime_health", "required": False}
                    ],
                    "thresholds": {
                        "log_bytes_warning": 100,
                        "log_bytes_rotate": 100000,
                        "tokens_used_warning": 500,
                        "tokens_used_rotate": 1000,
                        "compaction_count_warning": 2,
                        "compaction_count_rotate": 5,
                        "turn_count_warning": 10,
                        "turn_count_rotate": 20,
                        "notification_cooldown_seconds": 3600,
                        "checkpoint_cooldown_seconds": 86400,
                    },
                },
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def write_rollout(self, turns: int, compactions: int) -> None:
        rows = [{"type": "session_meta", "payload": {"id": "thread-test"}}]
        rows.extend({"type": "turn_context", "payload": {"turn_id": str(index)}} for index in range(turns))
        rows.extend({"type": "compacted", "payload": {"index": index}} for index in range(compactions))
        self.rollout.write_text(
            "\n".join(json.dumps(row) for row in rows) + "\n",
            encoding="utf-8",
        )

    def create_state_db(self, tokens_used: int) -> None:
        connection = sqlite3.connect(self.state_db)
        connection.execute(
            """
            CREATE TABLE threads (
                id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                rollout_path TEXT NOT NULL,
                archived INTEGER NOT NULL,
                tokens_used INTEGER NOT NULL,
                updated_at INTEGER NOT NULL,
                cwd TEXT NOT NULL
            )
            """
        )
        connection.execute(
            "INSERT INTO threads VALUES(?, ?, ?, ?, ?, ?, ?)",
            ("thread-test", "Test Thread", str(self.rollout), 0, tokens_used, 100, str(self.project)),
        )
        connection.commit()
        connection.close()

    def update_tokens(self, tokens_used: int) -> None:
        connection = sqlite3.connect(self.state_db)
        connection.execute("UPDATE threads SET tokens_used=? WHERE id='thread-test'", (tokens_used,))
        connection.commit()
        connection.close()

    def test_warning_checkpoint_resume_and_audit(self) -> None:
        result = PC.check_project(self.config, notify=False, auto_checkpoint=True)
        self.assertEqual(result["severity"], "warning")
        self.assertIsNotNone(result["checkpoint"])
        self.assertTrue(result["notification"]["needed"])
        self.assertEqual(result["metrics"]["turn_count"], 4)
        self.assertEqual(result["metrics"]["compaction_count"], 3)

        resume, status = PC.resume_project(self.config)
        self.assertEqual(status, 0)
        self.assertIn("checkpoint_hash_valid: `True`", resume)
        self.assertIn("thread-test", resume)
        self.assertIn("## Recovery Safety", resume)
        self.assertIn("`.deploy`", resume)

        audit, audit_status = PC.audit_project(self.config)
        self.assertEqual(audit_status, 0, audit)
        self.assertEqual(audit["failed_count"], 0)

        with self.rollout.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps({"type": "turn_context", "payload": {"turn_id": "new"}}) + "\n")
            handle.write(json.dumps({"type": "compacted", "payload": {"index": 99}}) + "\n")
        second = PC.check_project(self.config, notify=False, auto_checkpoint=True)
        self.assertEqual(second["severity"], "warning")
        self.assertIsNone(second["checkpoint"])
        self.assertEqual(second["metrics"]["turn_count"], 5)
        self.assertEqual(second["metrics"]["compaction_count"], 4)

        config, _ = PC.load_config(self.config)
        connection = sqlite3.connect(PC.database_path(config))
        node_count = connection.execute("SELECT COUNT(*) FROM lineage_nodes").fetchone()[0]
        edge_count = connection.execute("SELECT COUNT(*) FROM lineage_edges").fetchone()[0]
        quality_count = connection.execute("SELECT COUNT(*) FROM quality_checks").fetchone()[0]
        scan_state = connection.execute(
            "SELECT scanned_bytes, turn_count, compaction_count FROM rollout_scan_state"
        ).fetchone()
        connection.close()
        self.assertEqual(node_count, 4)
        self.assertEqual(edge_count, 3)
        self.assertGreaterEqual(quality_count, 4)
        self.assertEqual(scan_state, (self.rollout.stat().st_size, 5, 4))

    def test_rotate_required_when_hard_threshold_is_reached(self) -> None:
        self.update_tokens(1200)
        result = PC.check_project(self.config, notify=False, auto_checkpoint=True)
        self.assertEqual(result["severity"], "rotate_required")
        metrics = {row["metric"] for row in result["reasons"]}
        self.assertIn("tokens_used", metrics)

    def test_empty_thread_title_is_safe(self) -> None:
        connection = sqlite3.connect(self.state_db)
        connection.execute("UPDATE threads SET title='' WHERE id='thread-test'")
        connection.commit()
        connection.close()

        result = PC.check_project(self.config, notify=False, auto_checkpoint=True)
        self.assertEqual(result["severity"], "warning")

        config, _ = PC.load_config(self.config)
        store = PC.open_store(config)
        try:
            threads = PC.read_active_threads(config, store)
        finally:
            store.close()
        self.assertEqual(threads[0]["title"], "")

        audit, status = PC.audit_project(self.config)
        self.assertEqual(status, 0, audit)

    def test_registry_and_safe_purge(self) -> None:
        registered = PC.register_config(self.config, self.registry)
        self.assertTrue(registered["registered"])
        aggregate = PC.check_all(self.registry, notify=False)
        self.assertEqual(aggregate["project_count"], 1)
        self.assertEqual(aggregate["severity"], "warning")

        conversation_plan = PC.purge_plan(self.config, "conversation", "thread-test")
        self.assertEqual(conversation_plan["database_counts"]["conversations"], 1)
        with self.assertRaises(ValueError):
            PC.purge_runtime(self.config, "conversation", "wrong", "thread-test")
        purged = PC.purge_runtime(
            self.config,
            "conversation",
            conversation_plan["confirmation"],
            "thread-test",
        )
        self.assertTrue(purged["purged"])
        config, _ = PC.load_config(self.config)
        self.assertFalse((PC.runtime_dir(config) / "handoff" / "latest.json").exists())

        PC.check_project(self.config, notify=False, auto_checkpoint=True)
        project_plan = PC.purge_plan(self.config, "project")
        project_purged = PC.purge_runtime(
            self.config,
            "project",
            project_plan["confirmation"],
        )
        self.assertTrue(project_purged["purged"])
        self.assertFalse(PC.runtime_dir(config).exists())
        registry = json.loads(self.registry.read_text(encoding="utf-8"))
        self.assertFalse(registry["projects"][0]["enabled"])

    def test_failed_notification_is_retried_until_delivered(self) -> None:
        with patch.object(PC, "notify_macos", return_value=False):
            first = PC.check_project(self.config, notify=True, auto_checkpoint=False)
            second = PC.check_project(self.config, notify=True, auto_checkpoint=False)
        self.assertTrue(first["notification"]["needed"])
        self.assertFalse(first["notification"]["delivered"])
        self.assertTrue(second["notification"]["needed"])

        with patch.object(PC, "notify_macos", return_value=True):
            delivered = PC.check_project(self.config, notify=True, auto_checkpoint=False)
            suppressed = PC.check_project(self.config, notify=True, auto_checkpoint=False)
        self.assertTrue(delivered["notification"]["delivered"])
        self.assertFalse(suppressed["notification"]["needed"])

    def test_private_key_marker_rejects_active_task(self) -> None:
        first = PC.check_project(self.config, notify=False, auto_checkpoint=True)
        self.assertIsNotNone(first["checkpoint"])
        private_key_begin = "-----BEGIN " + "OPENSSH PRIVATE KEY-----"
        private_key_end = "-----END " + "OPENSSH PRIVATE KEY-----"
        with self.rollout.open("a", encoding="utf-8") as handle:
            handle.write(
                json.dumps(
                    {
                        "type": "response_item",
                        "payload": {
                            "type": "custom_tool_call_output",
                            "output": [
                                {
                                    "type": "input_text",
                                    "text": (
                                        private_key_begin
                                        + "\n"
                                        + "A" * 80
                                        + "\n"
                                        + private_key_end
                                        + "\n"
                                        + "NODEREAL_API_KEY="
                                        + "B" * 32
                                    ),
                                }
                            ],
                        },
                    }
                )
                + "\n"
            )
        result = PC.check_project(self.config, notify=False, auto_checkpoint=True)
        self.assertEqual(result["severity"], "error")
        self.assertIsNone(result["checkpoint"])
        self.assertEqual(result["reasons"][0]["metric"], "secret_markers")
        self.assertEqual(
            result["metrics"]["secret_markers"],
            ["credential_assignment", "open_ssh_private_key"],
        )
        audit, status = PC.audit_project(self.config)
        self.assertEqual(status, 1)
        secret_check = next(row for row in audit["checks"] if row["name"] == "active rollout secret markers")
        self.assertFalse(secret_check["ok"])

    def test_rendered_private_key_test_source_is_ignored(self) -> None:
        private_key_begin = "-----BEGIN " + "OPENSSH PRIVATE KEY-----"
        private_key_end = "-----END " + "OPENSSH PRIVATE KEY-----"
        rendered_source = "\n".join(
            [
                "def test_private_key_marker_rejects_active_task(self):",
                f'    "{private_key_begin}\\n"',
                '    + "A" * 80',
                f'    + "\\n{private_key_end}\\n"',
            ]
        )
        with self.rollout.open("a", encoding="utf-8") as handle:
            handle.write(
                json.dumps(
                    {
                        "type": "response_item",
                        "payload": {
                            "type": "custom_tool_call_output",
                            "output": [{"type": "input_text", "text": rendered_source}],
                        },
                    }
                )
                + "\n"
            )
        self.assertEqual(PC.high_confidence_secret_markers(self.rollout), [])

        real_marker = private_key_begin + "\n" + "B" * 80 + "\n" + private_key_end
        with self.rollout.open("a", encoding="utf-8") as handle:
            handle.write(
                json.dumps(
                    {
                        "type": "response_item",
                        "payload": {
                            "type": "custom_tool_call_output",
                            "output": [{"type": "input_text", "text": rendered_source + "\n" + real_marker}],
                        },
                    }
                )
                + "\n"
            )
        self.assertEqual(PC.high_confidence_secret_markers(self.rollout), ["open_ssh_private_key"])


if __name__ == "__main__":
    unittest.main()
