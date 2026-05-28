# Book Map

This file is a v1 conceptual map of each book's role in the skill. It intentionally avoids long quotations and exact page claims. It is not yet a complete source-backed distillation of every chapter, argument, example, and technical nuance.

For deeper book-specific use, load:

- `books/fooled-by-randomness.md`
- `books/black-swan.md`
- `books/statistical-consequences-fat-tails.md`
- `books/antifragile.md`
- `books/skin-in-the-game.md`

## Fooled By Randomness

Core question:

What if the success we admire is partly or mostly the visible residue of randomness?

Essence to preserve:

- Outcomes are not enough. A profitable or successful path may be one lucky path among many possible failures.
- People are weak at seeing alternative histories. We judge what happened, not what could easily have happened.
- Survivorship bias hides the dead cases and exaggerates the wisdom of winners.
- Narrative turns randomness into tidy causality after the fact.
- In noisy domains, confidence often follows success rather than truth.
- A person can be right for the wrong reason or wrong despite good reasoning.

Decision use:

- Evaluate process quality separately from outcome.
- Ask what hidden risks were carried to get the result.
- Check whether the actor would have survived nearby bad histories.
- Prefer repeated evidence across regimes to one dramatic win.

Typical traps:

- "He made money, so he understood the world."
- "This company survived, so its strategy was objectively superior."
- "This creator went viral, so the formula is clear."
- "The backtest worked, so the future risk is known."

Questions to ask:

- Where are the failed copies of this success story?
- What would the loser sample look like?
- Did the explanation exist before the outcome?
- Is this skill, exposure, or luck?

## The Black Swan

Core question:

What if the most important events are the ones your model excluded?

Essence to preserve:

- Rare, high-impact events can dominate history, markets, careers, and institutions.
- After surprises, people manufacture explanations that make the event feel less surprising.
- The absence of evidence is not proof of safety when the relevant event is rare.
- Experts can be most dangerous when they provide false certainty in complex domains.
- Some domains are governed by scalable, winner-take-all, fat-tailed dynamics.
- Forecasting can be less useful than arranging exposures so surprises do not destroy you.

Decision use:

- Identify assumptions that, if false, ruin the plan.
- Replace prediction dependence with robustness and optionality.
- Find where one event can dominate the outcome.
- Design for unknown unknowns by limiting downside.

Typical traps:

- "It has never happened, so it will not happen."
- "Our model says the probability is tiny."
- "The experts agree, so the uncertainty is settled."
- "The average case is fine, so the decision is safe."

Questions to ask:

- What is outside the model but inside reality?
- Which event creates irreversible damage?
- Where does diversification disappear during stress?
- Are we prepared for the event we cannot name?

## Statistical Consequences Of Fat Tails

Core question:

What changes when the distribution is fat-tailed instead of thin-tailed?

Essence to preserve:

- Switching from thin tails to fat tails is not a cosmetic adjustment. Many standard statistical habits become unreliable.
- In fat-tailed domains, sample means, variances, correlations, regressions, and risk estimates can be unstable or misleading.
- Real-world samples often live in the preasymptotic zone: not one observation, not infinite observations, and not enough convergence to trust textbook simplifications.
- Parameter uncertainty matters. A small error about the tail can create a large error in risk.
- Some empirical claims are fragile because they silently assume well-behaved distributions.
- Under fat tails, decision logic should focus more on exposure, maxima, drawdowns, ruin, and robustness than average-case optimization.

Decision use:

- Ask whether one observation can dominate the sum.
- Use medians, quantiles, stress tests, max exposure, and ruin constraints when means are unstable.
- Treat precise risk estimates skeptically when the tail is uncertain.
- Avoid concluding "enough data" unless the tail behavior supports convergence.

Typical traps:

- "The average return is positive."
- "The sample is large enough."
- "The correlation is stable."
- "This is a six-sigma event."
- "The backtest includes bad periods, so it covers tail risk."

Questions to ask:

- What happens if the tail is fatter than estimated?
- Is the mean representative or dominated by extremes?
- How does the conclusion change if the largest observations are missing?
- Are we estimating the body and pretending we estimated the tail?

## Antifragile

Core question:

How can a system gain from disorder instead of merely surviving it?

Essence to preserve:

- Fragile things hate volatility. Robust things resist volatility. Antifragile things improve from bounded volatility.
- The key is nonlinear response: harm or benefit changes disproportionately as stress grows.
- Optionality, tinkering, redundancy, decentralization, and small errors can create antifragility.
- Over-optimization, excessive smoothing, tight control, leverage, and naive intervention can create fragility.
- Some systems need stressors to adapt. Removing all variation can store hidden risk.
- Via negativa often works better than additive intervention: remove what harms before adding complexity.
- A barbell can protect against negative tails while preserving exposure to positive tails.

Decision use:

- Identify whether volatility hurts or helps the system.
- Replace large irreversible bets with many small reversible trials.
- Keep slack and redundancy when uncertainty is high.
- Use barbell structures: protect the base, buy or create upside options.
- Remove fragilizers before chasing optimization.

Typical traps:

- "Efficiency always improves resilience."
- "Stability today means safety tomorrow."
- "We should eliminate all volatility."
- "A complex intervention proves expertise."
- "The middle-risk path is automatically prudent."

Questions to ask:

- What stressor would make this better?
- What small failure can we afford repeatedly?
- What error would be fatal?
- Where do we have capped downside and open upside?

## Skin In The Game

Core question:

Who bears the consequences of being wrong?

Essence to preserve:

- Advice and decisions are morally and practically different when the decision-maker shares the downside.
- Hidden asymmetry creates fragility: one group receives upside while another absorbs harm.
- Accountability is an epistemic filter. People who pay for errors often learn faster and speak more carefully.
- Many expert, bureaucratic, financial, and managerial systems separate talk from consequences.
- Risk transfer can make systems appear smart while storing damage elsewhere.
- Minority constraints can shape majority behavior when the system defaults to satisfying the stricter party.

Decision use:

- Track upside and downside across all parties.
- Discount advice from people insulated from failure.
- Prefer builders, owners, and operators with meaningful exposure.
- Align compensation, reputation, and responsibility.
- Ask who pays if the model is wrong.

Typical traps:

- "The expert has credentials, so incentives do not matter."
- "The consultant recommends it, but the client absorbs failure."
- "The manager takes bonuses from upside while society absorbs downside."
- "Users carry the risk while the platform owns the economics."

Questions to ask:

- Who is harmed if this advice fails?
- Can the decision-maker walk away after creating risk?
- Is accountability financial, reputational, legal, or personal?
- Are we listening to someone who has survived the consequences?

## Cross-Book Integration

Use the books together like this:

- `Fooled by Randomness`: do not confuse outcome with skill.
- `The Black Swan`: do not confuse model absence with event impossibility.
- `Statistical Consequences of Fat Tails`: do not use thin-tail tools in fat-tail worlds.
- `Antifragile`: do not merely predict; design exposures that benefit from disorder.
- `Skin in the Game`: do not trust advice detached from consequences.

Compressed operating rule:

Survive bad tails, stop worshipping lucky winners, distrust precise stories in opaque systems, keep optionality, and make sure decision-makers pay for the risks they create.
