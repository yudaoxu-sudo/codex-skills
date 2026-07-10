# Project Continuity Schema

## Contents

1. Configuration
2. Adoption Levels
3. Threshold Semantics
4. SQLite Tables
5. Lineage
6. Deletion Scope

## Configuration

Each project owns a tracked `config/project_continuity.json`. Runtime databases and handoff packets live under the central, untracked `runtime_root`.

```json
{
  "schema": "project_continuity_config.v1",
  "project_id": "example-project",
  "name": "Example Project",
  "project_root": "/absolute/project/path",
  "state_db_path": "~/.codex/state_5.sqlite",
  "runtime_root": "~/Documents/Codex/runtime/project-continuity",
  "registry_path": "~/Documents/Codex/agent/project-continuity-projects.json",
  "context_files": [
    {"path": "~/Documents/Codex/projects/example.md", "role": "project_memory", "required": true}
  ],
  "health_files": [
    {"path": "output/runtime_health/latest.json", "role": "runtime_health", "required": false}
  ],
  "thresholds": {
    "log_bytes_warning": 52428800,
    "log_bytes_rotate": 104857600,
    "tokens_used_warning": 150000000,
    "tokens_used_rotate": 300000000,
    "compaction_count_warning": 6,
    "compaction_count_rotate": 10,
    "turn_count_warning": 120,
    "turn_count_rotate": 200,
    "notification_cooldown_seconds": 43200,
    "checkpoint_cooldown_seconds": 86400
  }
}
```

Relative context and health paths resolve from the config directory. Prefer absolute project and memory paths for cross-thread reliability.

## Adoption Levels

| Level | Intended projects | Required state |
| --- | --- | --- |
| `baseline` | Durable but low-risk work | Concise project memory, open items, external artifacts, Git checkpoints where applicable |
| `managed` | Long-running, important, automated, multi-conversation, or costly-to-reconstruct work | Baseline plus config, SQLite, registry, checkpoints, resume packets, and audits |
| `observed` | Production work where incorrect results can cause material harm | Managed plus runtime health evidence, lineage, and quality checks |

Only managed and observed projects belong in the central scheduled registry. Promote a project when its activity, operational risk, or reconstruction cost grows.

## Threshold Semantics

- A warning threshold creates a compact checkpoint and reminds the user once per state fingerprint/cooldown.
- A rotate threshold marks the conversation `rotate_required`.
- A metric crossing a new threshold changes the fingerprint and permits a new reminder.
- Small metric growth inside the same threshold band does not create repeated reminders.

Thresholds are conservative starting values based on local failure evidence. Tune them only after measuring healthy and failed tasks.

## SQLite Tables

- `projects`: project identity and config/root paths.
- `conversations`: current Codex rollout metrics and severity.
- `rollout_scan_state`: incremental JSONL byte offsets and cached turn/compaction counts.
- `thread_checks`: append-only threshold evaluations.
- `checkpoints`: immutable project snapshots and resume packet paths.
- `lineage_nodes`: raw, normalized, curated, analysis, and result nodes.
- `lineage_edges`: parent-to-child transformation relations.
- `quality_checks`: watcher audit results.
- `notifications`: deduplication and delivery history.

SQLite runs with WAL mode, foreign keys, and a busy timeout. Every project uses a separate database directory.

## Lineage

Checkpoint generation records this initial trace:

```text
Codex rollout path and hash (raw)
  -> thread metrics (normalized)
  -> checkpoint JSON (curated)
  -> resume packet Markdown (result)
```

Future project pipelines may add analysis nodes between curated data and results. Every node retains a `run_id`, `conversation_id`, URI, content hash, and structured payload.

## Deletion Scope

- Conversation purge removes managed checks, checkpoints, lineage, notifications, and handoff files for one `conversation_id`.
- Project purge removes the entire managed runtime directory and disables the project registry entry.
- Source repositories, OpenAI-retained chats, Saved Memory, uploaded files, Git remotes, deployments, and backups require separate deletion actions.
- Always execute `purge-plan` first and use its exact confirmation token.
