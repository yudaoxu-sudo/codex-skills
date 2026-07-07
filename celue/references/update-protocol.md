# Celue Update Protocol

Use this when the user asks to update `celue`, integrate a new KOL, add a case study, or change future trading behavior.

## Update Rules

1. Read `SKILL.md` first.
2. Read the smallest relevant reference file.
3. Gather fresh source evidence if the update depends on public claims or current market behavior.
4. Add the smallest durable rule.
5. Mark source quality:
   - `verified`: official or locally reconstructed evidence.
   - `sampled`: strong sample but incomplete coverage.
   - `social`: KOL/social evidence requiring verification.
   - `inference`: system conclusion.
6. Keep raw transcripts out of the skill.
7. Store only reusable principles, case references, and operating rules.
8. Validate the skill after edits.
9. If the skill repo is available, commit and push to GitHub.
10. If the local Codex skill directory is separate from the repo, sync `celue` into `~/.codex/skills/celue`.

## What Counts As A Durable Rule

- A repeated wallet-flow pattern.
- A new CEX or bridge interpretation rule.
- A failure mode from a real case.
- A stronger exit or no-trade condition.
- A new data source and its authority level.
- A field that must be added to reports or alerts.

## What To Exclude

- Hype.
- Unverified profit screenshots.
- One-off opinions with no reusable rule.
- Long copied posts.
- Private credentials or wallet material.
- Exact trading calls that expire quickly.

## Validation Checklist

- `SKILL.md` has valid frontmatter.
- References are linked from `SKILL.md`.
- Rules do not conflict with read-only safety.
- Social claims are not promoted above on-chain or official evidence.
- Output template still produces clear action, trigger, and invalidation.
