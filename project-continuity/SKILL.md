---
name: project-continuity
description: Keep long-running Codex projects recoverable across conversations with SQLite lineage, thread-size thresholds, deduplicated reminders, verified checkpoints, compact resume packets, and scoped purge plans. Use when the user mentions long conversations, context compression, task logs, seamless handoff, changing chat windows, project memory, checkpoint/resume, watcher agents, deleting a conversation/project memory, or asks Codex to warn before a task becomes too large.
---

# Project Continuity

Use the deterministic CLI in `scripts/project_continuity.py`. Keep raw chat content out of the continuity database; store paths, hashes, metrics, checkpoints, and lineage IDs.

## Locate Configuration

Prefer `<project-root>/config/project_continuity.json`. If it is missing, read `references/schema.md`, create a project-specific config, then register it in the central registry.

## Check A Task

```bash
python3 ~/.codex/skills/project-continuity/scripts/project_continuity.py check \
  --config <project-root>/config/project_continuity.json
```

Interpret status strictly:

- `healthy`: continue and keep large outputs in files or SQLite.
- `warning`: tell the user the triggering metrics and confirm that a fresh checkpoint exists.
- `rotate_required`: finish the current safe unit, run `checkpoint` and `audit`, then tell the user to open a completely new conversation.
- `error`: repair missing state/config/runtime evidence before claiming continuity is ready.

Never use a handoff path that copies the old full conversation log after `rotate_required`. The new conversation must load the compact resume packet.

## Checkpoint And Resume

Create a checkpoint before risky edits, thread rotation, or archival:

```bash
python3 ~/.codex/skills/project-continuity/scripts/project_continuity.py checkpoint \
  --config <config> --reason manual
```

In a fresh conversation, load and verify the latest packet:

```bash
python3 ~/.codex/skills/project-continuity/scripts/project_continuity.py resume \
  --config <config>
python3 ~/.codex/skills/project-continuity/scripts/project_continuity.py audit \
  --config <config>
```

Then read the listed project-memory files, inspect `git status`, and verify current runtime evidence. Do not replay completed operations.

## Scheduled Guard

Register each project once, then schedule `check-all --notify` through a Codex automation. The CLI deduplicates identical reminders and writes a checkpoint when warning state changes.

```bash
python3 ~/.codex/skills/project-continuity/scripts/project_continuity.py register \
  --config <config> --registry <registry>
python3 ~/.codex/skills/project-continuity/scripts/project_continuity.py check-all \
  --registry <registry> --notify
```

The scheduled automation should report only `warning`, `rotate_required`, or `error`. Healthy checks remain silent.

## Purge Safely

Always preview managed data first:

```bash
python3 ~/.codex/skills/project-continuity/scripts/project_continuity.py purge-plan \
  --config <config> --scope conversation --conversation-id <id>
```

Run `purge` only after the user explicitly confirms the exact token returned by `purge-plan`. Project purge removes the managed continuity runtime and disables its registry entry. It does not remove source code, Codex cloud chats, Saved Memory, Git remotes, deployed servers, or backups; report those remaining scopes explicitly.

## Data Discipline

- Raw tool output larger than a concise answer belongs in an artifact, not chat.
- Every checkpoint records `project_id`, `conversation_id`, hashes, git state, context files, health files, and lineage edges.
- Generated Wiki/context packs must point to exact evidence paths and remain small.
- Do not store credentials, cookies, private keys, seed phrases, access tokens, or raw private conversations.
- Read `references/schema.md` when creating a config, changing thresholds, or extending the lineage model.
