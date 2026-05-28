# Distillation Protocol

Use this file when upgrading the skill from conceptual v1 into a source-backed, book-by-book skill.

## Honest Status Language

Use these labels:

- `v1 conceptual`: core ideas and decision workflow are captured, but not full source extraction.
- `v2 source-backed`: the user's notes, OCR, photos, table of contents, or verified sources have been processed.
- `v3 operational`: source-backed concepts have been converted into checklists, templates, examples, and anti-misuse rules.

Never call a book "fully distilled" unless the work includes:

- Scope: which edition, translation, or source was used.
- Coverage: chapters or sections processed.
- Evidence: page, image, OCR, or source note for important claims.
- Essence: concepts, arguments, examples, and practical decision rules.
- Misuse warnings: how the idea is commonly overextended.
- Integration: how this book changes the skill's workflow.

## Per-Book Output File

For rigorous distillation, create one file per book:

```text
references/books/
├── fooled-by-randomness.md
├── black-swan.md
├── statistical-consequences-fat-tails.md
├── antifragile.md
└── skin-in-the-game.md
```

Each file should use this structure:

```markdown
# Book Title

## Source Scope

- Edition/source:
- Coverage:
- Evidence available:
- What is not covered:

## One-Sentence Thesis

...

## Core Arguments

| Argument | Evidence/source | Decision implication | Misuse warning |
|---|---|---|---|

## Key Concepts

| Concept | Meaning | Diagnostic question | Use when |
|---|---|---|---|

## Important Examples Or Stories

Summarize only. Do not reproduce long passages.

| Example | Point | How to apply | Source |
|---|---|---|---|

## Practical Checklist

...

## Integration Into Skill

- Add to workflow:
- Add to concepts:
- Add to templates:
- Add to examples:
```

## Distillation Workflow

1. Capture source scope
   - Identify title, edition, translator if relevant, and input type.
   - Mark whether the source is user-provided, official, public, or inferred.

2. Extract chapter skeleton
   - Use table of contents, headings, or user notes.
   - Do not invent missing chapters.

3. Extract claims
   - For each chapter or section, capture the main claim in your own words.
   - Mark the claim as `source-backed`, `general known concept`, or `inference`.

4. Convert claims into decision questions
   - A useful skill does not only remember ideas; it asks the right question at decision time.

5. Capture examples without copying
   - Summarize the role of the example.
   - Quote only short fragments when necessary and allowed.

6. Add misuse warnings
   - Ask how a smart user might abuse or overgeneralize the idea.

7. Integrate carefully
   - Update `concepts.md` only for reusable concepts.
   - Update `decision-checklist.md` only for operational questions.
   - Update `output-templates.md` only for repeated output shapes.
   - Update `examples.md` only for reusable patterns.

8. Validate
   - Search for invented details.
   - Check that source-backed and inferred claims are separated.
   - Test the skill on one real user decision.

## Minimum Inputs For Deep Distillation

Best:

- User photos of table of contents and marked pages.
- OCR or notes from each chapter.
- User's own highlights and questions.

Good:

- Public official descriptions plus user notes.
- A verified technical paper PDF for the fat-tails book.

Not enough for "complete":

- A cover photo.
- Memory of famous concepts.
- Internet summaries.
- The assistant's general knowledge alone.

## Quality Bar

A good distilled item looks like:

```markdown
- Concept: Survivorship bias
- Source status: general known concept, not page-backed here
- Decision question: What failed cases are missing from the sample?
- Use when: evaluating successful traders, founders, creators, strategies, or products
- Misuse warning: Do not dismiss all success as luck; separate process evidence from outcome evidence.
```

A bad distilled item looks like:

```markdown
- A fake exact page claim followed by an overbroad attack on all experts.
```

Reasons it is bad:

- Invented page.
- Overbroad claim.
- Not operational.
- No source boundary.
