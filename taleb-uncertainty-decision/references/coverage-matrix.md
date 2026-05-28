# Coverage Matrix

This file tracks what has actually been distilled and what still requires user-provided source material.

## Status Labels

- `Conceptual`: based on known core ideas and official descriptions, not page-backed.
- `Official-anchor`: checked against publisher/author/arXiv pages.
- `Source-scaffold`: local source exists and table of contents or sections were extracted.
- `Chapter-backed`: chapter-level notes/OCR processed.
- `Page-backed`: page/image/OCR evidence attached to key claims.
- `Operational`: converted into reusable checklist/template/example.

## Current Coverage

| Book | Current status | What is covered | What is missing | Next best input from user |
|---|---|---|---|---|
| `Fooled by Randomness` | Conceptual + official-anchor + operational | luck vs skill, alternative histories, survivorship bias, narrative fallacy, hidden blowup risk | Chinese edition structure, chapter examples, page-backed claims | table of contents photos, highlighted pages, OCR notes |
| `The Black Swan` | Conceptual + official-anchor + operational | rare high-impact events, hindsight explanation, model limits, robustness, unknown unknowns | Chinese edition structure, named examples by chapter, page-backed definitions | table of contents photos, pages around definition and examples |
| `Statistical Consequences of Fat Tails` | Official-anchor + source-scaffold + operational | public PDF downloaded, table of contents extracted, technical themes mapped to decision rules | full theorem-by-theorem extraction, derivations, chapter details beyond TOC/prologue | sections the user cares about first: forecasting, LLN, hidden tails, finance, pandemics |
| `Antifragile` | Conceptual + official-anchor + operational | fragile/robust/antifragile triad, convexity, optionality, barbell, via negativa, tinkering | Chinese edition structure, examples and stories, chapter-backed nuance | table of contents photos, highlighted pages on barbell/via negativa/iatrogenics |
| `Skin in the Game` | Conceptual + official-anchor + operational | incentive symmetry, risk transfer, minority rule, commitment, accountability | Chinese edition structure, examples and ethics details, page-backed claims | table of contents photos, marked passages on symmetry/minority rule/experts |

## What Was Added In V2

- One per-book reference file under `references/books/`.
- Explicit source scope per book.
- A stronger technical file for `Statistical Consequences of Fat Tails` using the local arXiv PDF.
- Coverage matrix to prevent false claims of completion.

## What Was Added In V3 Operational

- `action-operating-system.md`: the practical default decision/action system for users who have not read the books.
- `future-playbooks.md`: domain playbooks for investing, products, career, partnerships, learning, operations, and creator work.
- The skill's priority shifted from book reproduction to future action quality when the user asks for practical guidance.

## What Still Does Not Exist

- No complete chapter-by-chapter distillation for the four copyrighted trade books.
- No page-backed extraction from the user's Chinese editions.
- No long quotations.
- No claim that every book has been fully distilled.

## Upgrade Priority

Recommended order:

1. `Antifragile`: highest practical payoff for action design.
2. `Skin in the Game`: highest payoff for judging advice, partners, experts, and incentives.
3. `Fooled by Randomness`: best for evaluating success stories and trading/investing.
4. `The Black Swan`: best for risk reviews and strategic planning.
5. `Statistical Consequences of Fat Tails`: process in targeted technical passes because it is large and dense.
