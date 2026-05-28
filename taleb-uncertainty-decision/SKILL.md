---
name: taleb-uncertainty-decision
description: "Use this skill when analyzing decisions under uncertainty through Nassim Nicholas Taleb's Incerto-style ideas: randomness, luck versus skill, Black Swans, fat tails, ruin risk, antifragility, optionality, barbell strategy, via negativa, asymmetric payoff, and skin in the game. Trigger for investing, entrepreneurship, product bets, career decisions, policy choices, risk reviews, forecasting skepticism, and is-this-fragile questions."
---

# Taleb Uncertainty Decision

## Purpose

Turn Taleb-style uncertainty thinking into a practical decision workflow. The goal is not to predict the future better; it is to avoid ruin, reduce hidden fragility, expose yourself to favorable asymmetry, and stop mistaking randomness for knowledge.

Current status: this is a v1 conceptual skill. It captures the recurring decision principles from the books visible in the user's prompt, but it is not a page-by-page or chapter-by-chapter extraction of the user's Chinese editions.

Books in scope:

- `Fooled by Randomness`
- `The Black Swan`
- `Statistical Consequences of Fat Tails`
- `Antifragile`
- `Skin in the Game`

Do not pretend this is a substitute for reading the books. Use it as a decision lens and a structured checklist. If the user has not read the books and wants practical guidance, prioritize the operational system in `references/action-operating-system.md` and `references/future-playbooks.md`. If the user wants "no omitted essence" for a specific book, require source text, OCR, photos, notes, table of contents, or another verifiable input and follow `references/distillation-protocol.md`.

## Non-Fabrication Rules

These rules are part of the skill, not optional style preferences.

- Do not invent exact quotes, page numbers, chapter names, publication details, or anecdotes unless they are present in provided source material or verified during the task.
- Do not claim "Taleb says X on page Y" without the user's text or a reliable source.
- Distinguish three claim types:
  - `Book concept`: a known core idea from the Taleb corpus.
  - `Application`: this skill applying the concept to the user's situation.
  - `Inference`: a reasoned extension that may not be in the books.
- Prefer "Taleb-style diagnosis" over "Taleb would say" unless quoting or citing a verified source.
- If the user asks for faithful book extraction, ask for the passages, notes, OCR, or page photos. Without source text, provide a conceptual distillation and mark it as such.
- Avoid fake precision. In fat-tailed domains, do not present narrow confidence intervals, expected values, or probabilities unless the data and model justify them.
- Never turn the framework into prophecy. The point is exposure management, not fortune telling.

## Workflow

Use this sequence unless the user asks for a narrower output.

1. Define the decision and stakes
   - What is being decided?
   - What is the time horizon?
   - What does failure mean?
   - Is there any ruin condition?

2. Classify the domain
   - Thin-tailed or fat-tailed?
   - Repeatable or one-shot?
   - Bounded or unbounded payoff?
   - Mediocristan-like or Extremistan-like?
   - Is historical data likely to hide the most important event?

3. Separate skill from randomness
   - What alternative histories could have happened?
   - Is the success story survivorship-biased?
   - Are we explaining luck after the fact?
   - Does the actor still look good under bad but plausible paths?

4. Map payoff shape
   - What happens under small stress, large stress, and extreme stress?
   - Is the exposure convex, concave, or linear?
   - Is the downside capped or open-ended?
   - Is the upside capped or open-ended?

5. Hunt for Black Swan exposure
   - What event is treated as impossible because it has not happened recently?
   - Which assumption, if false, breaks the plan?
   - Where does correlation suddenly go to one?
   - What hidden leverage turns a surprise into ruin?

6. Diagnose fragility
   - Fragile: harmed disproportionately by volatility, error, delay, stress, or disorder.
   - Robust: mostly survives volatility.
   - Antifragile: benefits from bounded volatility or errors because losses are capped and gains remain open.

7. Check skin in the game
   - Who gets the upside?
   - Who eats the downside?
   - Who can be wrong without paying?
   - Are advisors, models, managers, founders, experts, or agents exposed to the consequences they recommend?

8. Choose action architecture
   - Remove fragilizers first: leverage, dependency, opacity, tight coupling, hidden ruin.
   - Preserve optionality: small reversible bets, experiments, prototypes, learning loops.
   - Use barbell logic where appropriate: protect the base, place limited-risk upside bets.
   - Prefer robustness before optimization.
   - In opaque domains, design for error rather than requiring forecast accuracy.

9. Produce the answer
   - Core diagnosis
   - Risk map
   - Asymmetry table
   - What to avoid
   - Robust/antifragile redesign
   - Small next actions
   - What evidence would change the recommendation

## Resource Loading

Load only what the task needs:

- `references/book-map.md`: book-by-book distilled essence and what each book contributes.
- `references/action-operating-system.md`: the default practical decision/action system for future work.
- `references/future-playbooks.md`: scenario playbooks for investing, projects, startups, career, partnerships, learning, and operational risk.
- `references/books/fooled-by-randomness.md`: source-scoped operational distillation of `Fooled by Randomness`.
- `references/books/black-swan.md`: source-scoped operational distillation of `The Black Swan`.
- `references/books/statistical-consequences-fat-tails.md`: arXiv-backed scaffold for the technical fat-tails book.
- `references/books/antifragile.md`: source-scoped operational distillation of `Antifragile`.
- `references/books/skin-in-the-game.md`: source-scoped operational distillation of `Skin in the Game`.
- `references/concepts.md`: compact concept dictionary and decision implications.
- `references/decision-checklist.md`: full diagnostic checklist for decisions, investments, careers, startups, and policies.
- `references/output-templates.md`: ready response formats.
- `references/examples.md`: examples of how to apply the framework.
- `references/source-notes.md`: source discipline, verified anchors, and citation rules.
- `references/distillation-protocol.md`: how to upgrade this from conceptual v1 into source-backed per-book distillation.
- `references/coverage-matrix.md`: what has been distilled, evidence level, and remaining gaps.
- `references/zh-terms.md`: Chinese terminology map for consistent Chinese output.

For a general decision request, read `concepts.md`, `decision-checklist.md`, and `output-templates.md`.

For a user who wants help doing future work rather than studying the books, read `action-operating-system.md` first, then `future-playbooks.md` if the domain matches.

For a book-specific request, read `book-map.md` first, then the matching file under `references/books/`.

For a user asking "is this actually from the book?", read `source-notes.md` and clearly mark what is verified versus inferred.

For a user asking to deepen or complete the distillation, read `distillation-protocol.md` first and create/update one evidence-backed reference per book.

## Default Output Shape

Use Chinese unless the user asks otherwise.

```markdown
**一句话诊断**
...

**领域判断**
- Tail type:
- Randomness vs skill:
- Ruin risk:
- Fragility:
- Skin in the game:

**不对称性表**
| 暴露 | 小波动 | 大波动 | 极端事件 | 结论 |
|---|---:|---:|---:|---|

**应该先避免**
- ...

**可改造成反脆弱的地方**
- ...

**下一步小实验**
1. ...
2. ...
3. ...

**我不确定的地方**
- ...
```

## Style

- Be direct, skeptical, and practical.
- Prefer exposure, constraints, and incentives over narrative.
- Use precise uncertainty labels: `known`, `unknown`, `assumption`, `fragility`, `ruin`, `optionality`.
- If the user wants a stronger verdict, give one, but show the key condition that would flip it.
