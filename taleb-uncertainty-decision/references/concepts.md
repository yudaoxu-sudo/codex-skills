# Concept Dictionary

This file compresses the core Taleb-style concepts into reusable decision tests. It is a conceptual distillation, not a quotation file.

## Randomness And Luck

### Alternative Histories

A result is only one path out of many paths that could have happened. Judge a decision by the distribution of possible paths, not only by the path that occurred.

Decision test:

- If the same decision were repeated across many nearby worlds, how often would it end in acceptable survival?
- Did success require a narrow sequence of favorable events?
- Would the person still look skilled if we observed the failed parallel cases?

Use when evaluating traders, founders, creators, investors, job choices, viral growth, and any "they won, therefore they are wise" claim.

### Survivorship Bias And Silent Evidence

We see winners and build theories around them, while missing the dead cases that followed similar behavior.

Decision test:

- Who tried the same strategy and disappeared?
- Are the data selected after the outcome?
- Is the lesson coming only from visible winners?
- Does the sample include failed funds, failed stores, failed creators, failed projects, and abandoned experiments?

### Narrative Fallacy

Humans compress messy randomness into clean stories after the fact. The story may explain the remembered outcome while hiding the role of chance.

Decision test:

- Did the explanation exist before the event?
- Does the explanation predict similar cases, or merely make this case feel coherent?
- Are we adding causality because the sequence is emotionally satisfying?

### Luck Versus Skill

Skill shows itself through repeatability under varied conditions, not just a good outcome. Luck often masquerades as competence when payoff distributions are noisy and winners are celebrated.

Decision test:

- Is there a long record across regimes?
- Did the actor take hidden tail risk?
- Are losses visible, or hidden by leverage, accounting, reputation, or time delay?
- Is the strategy scalable in a way that makes winner-take-all outcomes likely?

## Black Swans

### Black Swan Exposure

A Black Swan is a rare, high-impact surprise that is often made explainable after it happens. The practical lesson is not "predict the rare event"; it is "do not be built so that one rare event destroys you."

Decision test:

- What event is treated as impossible mainly because it has not happened recently?
- What assumption would break the whole plan if false?
- What hidden dependency creates cascading failure?
- What single event can wipe out years of gains?

### Epistemic Arrogance

People overstate what they know, especially in complex systems. Forecasting confidence often grows faster than real understanding.

Decision test:

- Where are we using a neat model because reality is uncomfortable?
- Does the confidence interval reflect model error, or only calculation error?
- Are we confusing data abundance with understanding?

### Ludic Fallacy

Game-like probabilities can mislead when imported into real life. Dice, cards, and casino games have known rules; real systems often have changing rules, hidden dependencies, and unknown unknowns.

Decision test:

- Are the states of the world fully known?
- Can the rules change while the game is being played?
- Are extreme outcomes outside the model but inside reality?

### Forecasting Skepticism

In complex, fat-tailed domains, long-range prediction is often less useful than controlling exposure.

Decision test:

- What decision remains acceptable if the forecast is wrong?
- Can we replace prediction with optionality?
- Can we structure losses to be small while keeping upside open?

## Fat Tails

### Thin-Tailed Versus Fat-Tailed Domains

Thin-tailed domains are less dominated by extremes. Fat-tailed domains are shaped by rare large events. In fat-tailed domains, averages can be unstable, sample histories can be misleading, and extremes may dominate outcomes.

Common fat-tailed candidates:

- Venture returns
- Creator attention
- Financial crashes
- Insurance catastrophes
- Pandemics
- Cybersecurity
- Social media distribution
- Wars and large-scale political shocks
- Startup outcomes
- Bestseller dynamics
- Wealth and city-size distributions

Decision test:

- Can one observation dominate the sum?
- Are outcomes bounded on both sides?
- Is the maximum observed outcome likely to grow with the sample?
- Would removing the top 1 percent change the conclusion?

### Mediocristan And Extremistan

Mediocristan-like domains are not dominated by a single observation. Extremistan-like domains are dominated by scale, concentration, and extremes.

Decision test:

- Can one person, client, event, trade, creator, or product dominate total results?
- Is the activity scalable without proportional labor?
- Does the winner capture a disproportionate share?

### The Problem With Averages

In fat-tailed domains, an average can be technically computable but practically misleading. It may depend heavily on rare observations, model assumptions, or unobserved extremes.

Decision test:

- Is the mean stable across subsamples?
- Is the median more informative than the mean?
- Are downside quantiles, maximum loss, and ruin probability more important than expected value?

### Forecast Versus Exposure

A forecast can be directionally right while the payoff is wrong. A binary claim such as "the market is more likely to go up" does not determine whether the trade should be long or short, because magnitude and tail losses matter.

Decision test:

- Are we discussing event frequency or payoff distribution?
- What happens if the less likely event has much larger magnitude?
- Is the user paid by being right often, or by surviving and making money over paths?

### The Empirical Distribution Is Not Enough

In tail-sensitive domains, the historical sample may omit the region that determines risk. A dataset can be real and still not reveal the decisive tail.

Decision test:

- Does the historical period include the relevant stress event?
- Would one missing observation reverse the conclusion?
- Are outliers being removed because they are errors, or because they are uncomfortable?

### No Typical Large Deviation

Under serious fat tails, a "large event" is not represented well by one typical size. Conditional on exceeding a threshold, the excess itself can remain highly variable.

Decision test:

- Are we modeling a crisis as one scenario size?
- What if the large event is 3x, 10x, or 30x larger than the stress case?
- Is the plan robust to the size of the shock, or only to its occurrence?

### Preasymptotics

Real life usually operates before the "large enough sample" promised by textbook asymptotics. The sample may be too small for convergence, especially under fat tails.

Decision test:

- Is the claim relying on "with enough data this averages out"?
- How much data would actually be enough under this tail?
- Could the process change before convergence arrives?

### Ensemble Probability Versus Time Probability

An average across many parallel units is not automatically relevant to one actor living through a sequence of outcomes. If one bad event removes the actor from future rounds, time/path probability dominates ensemble comfort.

Decision test:

- Can the user survive the bad paths required to realize the average?
- Is there a stopping/absorbing barrier such as bankruptcy, liquidation, death, ban, lawsuit, or reputational ruin?
- Are we using population averages to justify a path one person cannot endure?

### Parameter Uncertainty

When model parameters are uncertain, risk estimates can be far more fragile than they look. Error in the parameter estimate compounds with error in the model and error in the world.

Decision test:

- How sensitive is the conclusion to the tail parameter?
- Does a slightly fatter tail reverse the recommendation?
- Is the estimate pretending the parameter is known?

## Fragility And Antifragility

### Fragile

Something is fragile when volatility, errors, delays, shocks, or disorder hurt it more than proportionally.

Signals:

- Leverage
- Tight coupling
- No slack
- Single point of failure
- Hidden correlation
- Complex dependencies
- Need for continuous stability
- Small errors escalating into ruin

Decision test:

- What happens if inputs move by 2x, 5x, or 10x?
- Does harm accelerate as stress increases?
- Is survival dependent on calm conditions?

### Robust

Something is robust when it mostly withstands shocks without gaining from them.

Decision test:

- Can it survive expected stress without heroic intervention?
- Does it avoid ruin while preserving enough function?

### Antifragile

Something is antifragile when bounded stress, volatility, mistakes, or variation improve it. Antifragility requires capped downside and open or repeatable upside.

Signals:

- Small failures teach cheaply
- Many independent trials
- Optionality
- Redundancy that creates adaptive capacity
- Decentralized experimentation
- Upside from volatility

Decision test:

- Can small errors improve the system?
- Are losses capped and gains allowed to run?
- Does variation create information or destroy the base?

### Convexity And Concavity

Convex exposure benefits from variability; concave exposure is harmed by variability. This often matters more than verbal opinions about risk.

Decision test:

- If reality becomes more volatile, does expected outcome improve or worsen?
- Are we long options or short options?
- Are we collecting small gains while carrying rare catastrophic loss?

### Iatrogenics And Naive Intervention

An intervention can create more harm than the problem it tries to solve, especially in complex systems where side effects are hidden or delayed.

Decision test:

- What is the harm of doing nothing?
- What is the harm of intervention?
- Are we treating visible symptoms while adding hidden fragility?
- Is the intervention reversible?

### Via Negativa

Often the strongest improvement is removing what harms: leverage, dependency, toxins, bad incentives, unnecessary complexity, fragile commitments.

Decision test:

- What can be removed to reduce ruin risk?
- Which constraint creates most fragility?
- What unnecessary exposure exists only because it feels sophisticated?

## Optionality And Barbell

### Optionality

An option is the right, not the obligation, to benefit from a favorable future. In real decisions, optionality can come from skills, networks, prototypes, cash reserves, modular design, distribution channels, and reversible commitments.

Decision test:

- What low-cost action increases future choices?
- What commitment closes too many doors?
- Can the user pay small known costs for unknown upside?

### Barbell Strategy

The barbell avoids fragile middle exposure by combining strong protection on one side with small high-upside bets on the other. It is not recklessness; it is a way to survive bad tails while remaining exposed to good tails.

Decision test:

- What must be protected at all costs?
- What small speculative bets have capped downside?
- Are we confusing "moderate" with "safe"?

### Tinkering

In opaque systems, trial and error can outperform theory when failures are small and information is real.

Decision test:

- Can we run many cheap experiments?
- Does each failure teach something?
- Are we trying to plan perfectly because experimentation feels messy?

## Skin In The Game

### Incentive Symmetry

A person has skin in the game when they share meaningful downside from their recommendations or actions. Without downside exposure, advice can become cheap and dangerous.

Decision test:

- Who pays if this fails?
- Does the advisor own the same downside?
- Can decision-makers transfer harm to users, employees, investors, taxpayers, customers, or future selves?

### Agency Risk

Agents may optimize their own visible metrics while shifting hidden downside to principals.

Decision test:

- Is the manager paid for upside but insulated from blowups?
- Is the consultant rewarded for complexity?
- Is the expert rewarded for confidence rather than consequences?

### Minority Rule

A small, committed, inflexible minority can shape outcomes when the majority is flexible and the system accommodates the stricter constraint.

Decision test:

- Is there a small group with hard constraints?
- Does the system default to satisfying the most restrictive requirement?
- Is this a real constraint or merely a loud preference?

### Soul In The Game

Beyond financial exposure, reputation, craft, honor, and personal accountability can create alignment. This is useful for judging builders, teachers, creators, and partners.

Decision test:

- Does the person stand behind the work?
- Do they pay a reputational cost for low quality?
- Are they accountable to people affected by the decision?

## Practical Synthesis

Use this five-question compression when time is short:

1. Can this kill us, bankrupt us, or trap us?
2. Are we in a fat-tailed domain where extremes dominate?
3. Are we mistaking luck, narrative, or visible survivors for skill?
4. Is the payoff convex or concave under volatility?
5. Are the people making the decision exposed to the downside?
