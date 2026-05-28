# Decision Checklist

Use this file when the user wants analysis of a real decision, strategy, investment, product, career move, or policy.

## Intake

Clarify only if necessary. Otherwise infer and mark assumptions.

Minimum facts:

- Decision:
- Options:
- Time horizon:
- Capital at risk:
- Reputation or relationship risk:
- Worst acceptable loss:
- Ruin condition:
- Who decides:
- Who pays if wrong:
- What data exists:
- What the user wants: verdict, red-team, redesign, checklist, or memo.

## Step 1: Domain Classification

Ask:

- Is the payoff bounded or unbounded?
- Can one event dominate total outcome?
- Does the system involve markets, networks, epidemics, virality, leverage, social status, war, cyber risk, finance, startup returns, or platform dynamics?
- Is the process stable, or can rules change?
- Are observations independent, or do they cascade?
- Is the decision path-dependent, where one bad path prevents future participation?
- Are we using ensemble averages when the user lives through one time path?

Label:

- `Thin-tail leaning`: bounded outcomes, many independent observations, no single observation dominates.
- `Fat-tail leaning`: extremes dominate, scaling effects, feedback loops, winner-take-all, rare events matter.
- `Unknown tail`: insufficient evidence; treat as fatter-tailed when downside is severe.

Default rule:

When downside includes ruin and the tail is uncertain, behave as if the tail is fat until proven otherwise.

Path rule:

If the user can be removed from the game by one path, do not rely on ensemble-average logic. Treat survival across time as the primary constraint.

## Step 2: Randomness Versus Skill

Ask:

- What alternative histories were possible?
- Are failed cases missing from the story?
- Is the claimed skill observable before the outcome?
- Did the actor carry hidden tail risk?
- Was the evaluation window long enough across regimes?

Red flags:

- One spectacular win used as proof of general ability.
- Backtest without dead strategies.
- Founder or investor myth built only after success.
- High returns with smooth reported volatility.
- "No losses so far" in a strategy that sells rare-event insurance.

Output:

- `Skill evidence`:
- `Luck exposure`:
- `Silent evidence missing`:
- `Confidence level`:

## Step 3: Payoff Shape

Map the payoff under four states:

| State | What happens? | Loss/gain | Reversible? | Notes |
|---|---|---:|---|---|
| Normal | | | | |
| Moderate stress | | | | |
| Severe stress | | | | |
| Extreme event | | | | |

Classify:

- `Convex`: small known downside, large possible upside, benefits from volatility.
- `Concave`: small steady gains, rare large loss, harmed by volatility.
- `Linear-ish`: proportional gains and losses.
- `Unclear`: needs more evidence.

Key test:

If volatility doubles, does the plan become better or worse?

## Step 3B: Forecast Versus Exposure

Use this especially for markets, policy, product bets, elections, pandemics, and any yes/no forecast.

Ask:

- Is the user asking "what is more likely" or "what should I do"?
- Are event probabilities being confused with payoff magnitude?
- Can the more likely event produce small gains while the less likely event produces ruin?
- Is the payoff continuous even though the forecast is binary?
- Does being right often matter less than avoiding one catastrophic loss?

Output:

- `Forecast claim`:
- `Actual exposure`:
- `Magnitude asymmetry`:
- `Decision implication`:

## Step 4: Ruin Filter

Before optimizing, ask:

- Can this bankrupt the person or organization?
- Can it permanently damage reputation, health, legal standing, family stability, or core assets?
- Can it trap the user in debt, dependency, or irreversible commitment?
- Can a single failure remove the ability to keep playing?

If yes:

- Do not proceed to expected-value optimization.
- First cap loss, reduce size, add redundancy, remove leverage, or reject.

Ruin conditions to flag:

- Unbounded liability
- Margin/leverage
- Concentrated exposure
- Illiquidity under stress
- Legal or regulatory unknowns
- Health risk
- Core reputation risk
- Dependency on one platform, supplier, partner, customer, founder, or model

## Step 5: Black Swan Search

Ask:

- What event is absent from recent data but plausible over the decision horizon?
- What assumption is treated as fixed but can change suddenly?
- Where are correlations hidden?
- What external actor can change the rules?
- Which "impossible" event would be obvious in hindsight?

Common hidden Black Swan channels:

- Liquidity disappears.
- Platform policy changes.
- Supplier fails.
- Key person leaves.
- Model breaks under regime change.
- Regulation shifts.
- Social narrative flips.
- Interest rates, currency, or credit conditions move sharply.
- Cyber or operational failure.
- A small issue becomes public and reputational.

Output:

- `Named tail scenarios`:
- `Unknown unknown allowance`:
- `Plan survives if forecast wrong? yes/no`

## Step 6: Fragility Diagnosis

Score each dimension from 0 to 3:

| Dimension | 0 Robust | 1 Mild | 2 Fragile | 3 Ruinous |
|---|---|---|---|---|
| Leverage | none | manageable | high | forced liquidation |
| Dependency | many options | few options | single dependency | no fallback |
| Coupling | modular | some links | tight | cascading failure |
| Slack | abundant | adequate | thin | none |
| Reversibility | easy | moderate | hard | impossible |
| Opacity | transparent | mixed | unclear | unknowable |
| Incentives | aligned | mixed | skewed | downside shifted |

Interpretation:

- Any `3` must be addressed before recommending action.
- Multiple `2`s often combine into hidden fragility.
- Fragility is not just probability; it is damage conditional on stress.

## Step 7: Skin In The Game

Map incentives:

| Actor | Upside if right | Downside if wrong | Can exit? | Alignment |
|---|---:|---:|---|---|
| User | | | | |
| Advisor/expert | | | | |
| Operator/manager | | | | |
| Customer/user/public | | | | |

Ask:

- Who is paid for confidence?
- Who pays for error?
- Who can recommend risk without owning risk?
- Is reputational accountability real or cosmetic?
- Are there delayed harms imposed on people not in the room?

Recommendation rule:

Discount advice when upside is private and downside is transferred.

## Step 8: Redesign Options

Use these moves in order:

1. Remove fragilizers
   - Reduce leverage.
   - Cap liability.
   - Remove single points of failure.
   - Add slack.
   - Shorten irreversible commitments.
   - Make contracts and ownership clear.

2. Build robustness
   - Hold cash or reserves.
   - Diversify dependencies that fail together.
   - Create fallback channels.
   - Use boring infrastructure for critical functions.
   - Add monitoring for early stress.

3. Add optionality
   - Run small experiments.
   - Prototype before scaling.
   - Buy time.
   - Keep learning loops close to reality.
   - Negotiate rights without obligations.

4. Create barbell
   - Protect core assets.
   - Keep most exposure safe or robust.
   - Allocate small, capped-risk bets to high-upside opportunities.
   - Avoid the "moderate" exposure that still contains hidden ruin.

5. Add skin in the game
   - Make advisors share downside.
   - Tie compensation to long-term outcomes.
   - Require decision-makers to use the product or bear consequences.
   - Prefer operators with direct exposure.

## Step 9: Final Recommendation

Use one of these verdicts:

- `Proceed`: downside capped, assumptions acceptable, incentives aligned.
- `Proceed as small experiment`: upside interesting, but uncertainty high.
- `Redesign first`: core idea good, current structure fragile.
- `Avoid`: ruin risk, bad asymmetry, or incentives too misaligned.
- `Need source/data`: the user asks for book fidelity or numerical precision not available.

Always include:

- What would make the recommendation wrong.
- The smallest reversible next step.
- The main hidden fragility.

## Domain-Specific Notes

### Investing

Focus:

- Tail risk
- Leverage
- Liquidity
- Concentration
- Strategy death rate
- Backtest survivorship
- Correlation under stress
- Position sizing

Avoid:

- Treating average returns as sufficient.
- Ignoring max drawdown and forced selling.
- Trusting smooth return histories.
- Using Gaussian language casually in crash-prone assets.

### Startups And Products

Focus:

- Optionality
- Small experiments
- Distribution power laws
- Founder skin in the game
- Platform dependency
- Cash runway as survival
- Convex upside from learning

Avoid:

- Scaling before feedback.
- Over-optimizing for one forecast.
- Building a fragile product dependent on one channel.

### Career

Focus:

- Reversible versus irreversible moves
- Skill optionality
- Reputation downside
- Exposure to growing networks
- Personal barbell: stable base plus exploratory upside

Avoid:

- Confusing prestige with robustness.
- Taking irreversible downside for capped upside.
- Outsourcing judgment to people who do not bear your consequences.

### Policy Or Organization

Focus:

- Iatrogenics
- Delayed side effects
- Decentralized trial and error
- Incentive alignment
- Redundancy
- Failure containment

Avoid:

- Large irreversible interventions without feedback.
- Removing all local variation.
- Centralizing failure modes.
