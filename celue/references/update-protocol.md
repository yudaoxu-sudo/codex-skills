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

## Required Integration Points

For every durable strategy update, decide which of these files must change:

- `SKILL.md`: add or update the reference link when a new KOL, case family, or strategy category is added.
- `references/system-logic.md`: add only global rules, default questions, hard gates, or project/runtime evidence fields that should affect future decisions.
- A dedicated `references/*.md`: store the reviewed KOL/case strategy, source scope, source quality, durable rules, and action mapping.
- Project workspace files under `/Users/xuyufan/Documents/狙击手进程`: update templates, reports, watchlist fields, scripts, or cases only when the rule needs runtime visibility or generated output.
- `/Users/xuyufan/Documents/Codex/projects/sniper-monitor.md`: record the durable update, commit id, validation result, and remaining external blockers.

Use one reference per KOL, case family, or strategy category. Keep raw posts, screenshots, long transcripts, and monitor outputs in the project workspace or temporary source files.

## Update Decision

Classify the new material before editing:

| Material | Action |
| --- | --- |
| Repeated wallet-flow pattern | Add durable rule and reference example |
| New CEX, bridge, pool, or venue interpretation | Add to `system-logic.md` if global |
| One-off live call | Keep in project case/report; do not promote yet |
| KOL thread with reusable process | Add or update a KOL reference |
| Real failure mode | Add stricter no-trade, reduce, exit, or validation gate |
| New runtime field needed in reports | Update project template/report script and verification |
| API/source availability | Add authority level and live-probe requirement |

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
