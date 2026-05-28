# Source Notes And Fidelity Rules

Use this file when the user wants confidence that the skill is not inventing book content.

## Completion Status

This skill currently contains:

- A source-calibrated conceptual map of the five books in scope.
- A reusable decision checklist derived from the recurring ideas.
- Anti-hallucination rules for quotes, pages, anecdotes, and modern applications.

This skill does not yet contain:

- A chapter-by-chapter extraction for each Chinese edition.
- Page-numbered evidence from the user's physical books.
- Exhaustive examples, stories, aphorisms, and technical derivations.
- A full technical reconstruction of `Statistical Consequences of Fat Tails`.

Do not tell the user that every book is "fully distilled" unless those missing layers have been added from verifiable source material.

## Verified Anchors

These anchors were checked during initial skill creation:

- Nassim Nicholas Taleb's official homepage describes the Incerto as a multi-volume investigation of opacity, luck, uncertainty, probability, human error, risk, and decision-making under limited understanding.
- The Incerto set includes `Fooled by Randomness`, `The Black Swan`, `The Bed of Procrustes`, `Antifragile`, and `Skin in the Game`. The user's image focuses on five works: four Incerto books plus `Statistical Consequences of Fat Tails`.
- The arXiv abstract for `Statistical Consequences of Fat Tails: Real World Preasymptotics, Epistemology, and Applications` identifies the work as the first volume of the Technical Incerto and frames it around the misuse of conventional statistical techniques under fat-tailed distributions.
- Publisher and catalog descriptions consistently position `The Black Swan` around high-impact improbable events, `Antifragile` around systems that gain from disorder, and `Skin in the Game` around hidden asymmetries and consequence-bearing.

Reference links:

- Author homepage: https://www.fooledbyrandomness.com/index.html
- `Fooled by Randomness` publisher page: https://www.penguinrandomhouse.com/books/176225/fooled-by-randomness-by-nassim-nicholas-taleb/9781400067930/
- `The Black Swan: Second Edition` publisher page: https://www.penguinrandomhouse.com/books/176226/the-black-swan-second-edition-by-nassim-nicholas-taleb/9781400063512/
- `Antifragile` publisher page: https://www.penguinrandomhouse.com/books/176227/antifragile-by-nassim-nicholas-taleb/hardcover/
- `Skin in the Game` publisher page: https://www.penguinrandomhouse.com/books/537828/skin-in-the-game-by-nassim-nicholas-taleb/
- `Statistical Consequences of Fat Tails` arXiv page: https://arxiv.org/abs/2001.10488
- Taleb official post for the fat-tails monograph: https://nassimtaleb.org/2025/09/3rd-edition-statistical-consequences-of-fat-tails/

Local downloaded source:

- `sources/statistical-consequences-fat-tails.pdf`, downloaded from arXiv on 2026-05-28.

## Fidelity Policy

When answering:

- Safe to present as core Taleb concepts:
  - Randomness can masquerade as skill.
  - Survivorship bias and narrative explanations distort learning.
  - Rare high-impact events can dominate outcomes.
  - Fat-tailed domains break many thin-tail intuitions.
  - Fragile systems are harmed by volatility; antifragile systems can benefit from bounded disorder.
  - Optionality and barbell structures can improve decisions under uncertainty.
  - Skin in the game matters because consequences discipline judgment.

- Must present as application or inference:
  - Any advice about a user's specific investment, business, career, or product.
  - Any claim about a modern market, project, regulation, token, company, or person unless separately verified.
  - Any quantitative estimate not derived from provided data.

- Must refuse or qualify:
  - Exact quotations without source text.
  - Page numbers without source text.
  - Claims that "Taleb would definitely recommend X."
  - Overconfident probability estimates in fat-tailed domains.

## If User Provides Photos, OCR, Or Notes

Use this workflow:

1. Extract the passage faithfully.
2. Separate:
   - original claim,
   - concept label,
   - practical decision question,
   - modern application,
   - possible misuses.
3. Avoid long verbatim copying. Quote only short fragments when necessary.
4. Mark page, edition, and source image if provided.
5. Add the distilled item to the relevant reference file only if it improves the reusable skill.

## Anti-Hallucination Checklist

Before finalizing an answer:

- Did I invent a quote, page, anecdote, or chapter?
- Did I distinguish book concept from my application?
- Did I overstate certainty in a fat-tailed setting?
- Did I ignore ruin risk because the expected value sounded positive?
- Did I treat a visible winner as proof while ignoring silent evidence?
- Did I give advice from a comfortable distance without checking who bears downside?
