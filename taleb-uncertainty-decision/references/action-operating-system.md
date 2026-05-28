# Action Operating System

Use this file when the user has not read the books and wants the most useful practical framework for future decisions and projects.

## One-Sentence System

Do not try to predict the future precisely; structure actions so bad surprises do not kill you, good surprises can help you, and people making decisions share the consequences.

## The Eight Operating Principles

### 1. Survival Before Optimization

Before asking "how much can we make?", ask "can this remove us from the game?"

Default moves:

- cap maximum loss,
- avoid forced liquidation,
- protect health, reputation, cash, relationships, core assets,
- keep enough slack to survive being wrong.

Use when:

- investing,
- quitting a job,
- taking debt,
- signing long commitments,
- building on one platform,
- exposing private keys/data/reputation.

### 2. Exposure Before Prediction

The important question is often not "what will happen?", but "what happens to us under each path?"

Ask:

- If we are right, how much do we gain?
- If we are wrong, how much do we lose?
- Which error is fatal?
- Are we paid for being right often, or paid for payoff magnitude?

Rule:

Do not debate probabilities until the payoff shape is visible.

### 3. Tail Before Average

In fat-tailed domains, averages can mislead. One event, client, product, trade, creator, exploit, lawsuit, platform change, or market crash can dominate.

Ask:

- Can one event dominate the result?
- Does the top 1 percent matter more than the average?
- Would one missing extreme reverse the conclusion?
- Is the downside open-ended?

Rule:

When one event can dominate and downside is severe, act as if the tail is fatter than the spreadsheet says.

### 4. Optionality Before Certainty

When uncertainty is high, buy or create options: small costs, capped downside, open upside, future choice.

Examples:

- prototype before full build,
- pilot before contract,
- small position before large allocation,
- side project before quitting,
- multiple channels before scaling,
- learning skill before committing identity.

Rule:

Prefer actions that teach and preserve future choices.

### 5. Barbell Before All-In

Protect the base, then take small high-upside bets. Avoid the seductive middle when it has hidden ruin.

Structure:

- safe side: cash, health, stable income, secure custody, core reputation, boring reliability,
- risky side: many capped-loss experiments with asymmetric upside.

Rule:

The speculative side is only allowed because the safe side is truly protected.

### 6. Via Negativa Before Adding Complexity

Often the best improvement is removing what harms.

Remove first:

- leverage,
- unnecessary dependencies,
- opaque counterparties,
- bad incentives,
- irreversible commitments,
- fragile architecture,
- toxic information sources,
- single points of failure.

Rule:

Before adding tools, models, people, or plans, ask what can be deleted.

### 7. Skin In The Game Before Trust

Advice is more valuable when the advisor bears consequences.

Ask:

- Who gets upside?
- Who eats downside?
- Who can exit before damage appears?
- Who is rewarded for confidence rather than correctness?
- Does the person use the thing they recommend?

Rule:

Discount advice that transfers risk to you while giving upside to the speaker.

### 8. Reality Contact Before Narrative

Stories are cheap. Reality contact is expensive but useful.

Prefer:

- real users over opinions,
- paid demand over compliments,
- live tests over decks,
- small losses over large theories,
- repeated evidence across regimes over one success.

Rule:

Convert beliefs into cheap tests as soon as possible.

## Default Analysis Flow

Use this when the user asks "帮我分析 X".

### Step 1: Name The Game

- What game are we playing?
- What counts as winning?
- What counts as losing?
- What is the time horizon?
- Is this a one-shot decision or repeated game?

### Step 2: Classify The Terrain

Label the domain:

- `thin-tail leaning`: bounded, stable, repeatable, many independent trials.
- `fat-tail leaning`: extremes dominate, network effects, leverage, virality, markets, hidden dependence.
- `unknown-tail`: insufficient evidence; treat as fat-tail if downside is severe.

Also label:

- reversible or irreversible,
- path-dependent or not,
- transparent or opaque,
- stable rules or changing rules.

### Step 3: Run The Ruin Filter

Ruin includes:

- bankruptcy,
- forced liquidation,
- permanent reputation damage,
- legal/regulatory disaster,
- health damage,
- account ban or platform dependency,
- loss of core relationship,
- private key/data compromise,
- being trapped with no exit.

If ruin exists:

- reduce size,
- cap liability,
- add fallback,
- change structure,
- or avoid.

Do not optimize until this is solved.

### Step 4: Draw The Payoff Shape

Use a simple table:

| State | What happens | Gain/loss | Reversible? |
|---|---|---:|---|
| Normal | | | |
| Good surprise | | | |
| Bad surprise | | | |
| Extreme event | | | |

Classify:

- `convex`: small capped loss, large upside.
- `concave`: small steady gain, rare large loss.
- `fragile`: needs calm conditions.
- `robust`: survives stress.
- `antifragile`: improves from bounded stress.

### Step 5: Check Incentives

Map:

| Actor | Upside | Downside | Can exit? | Trust adjustment |
|---|---:|---:|---|---|

Look especially at:

- advisors,
- platforms,
- vendors,
- fund managers,
- partners,
- influencers,
- employees/managers,
- your future self.

### Step 6: Choose The Action Type

Use one of five actions:

- `Avoid`: bad asymmetry or ruin cannot be capped.
- `Redesign`: idea may be good, structure is fragile.
- `Small experiment`: uncertainty high but downside can be capped.
- `Barbell`: protect base while taking limited upside bets.
- `Commit`: evidence is strong, downside capped, incentives aligned.

### Step 7: Define Guardrails

Every action needs:

- max loss,
- stop condition,
- review date,
- evidence that would change the decision,
- owner,
- fallback plan.

### Step 8: Review Alternative Histories

After outcome:

- Was the process good or merely lucky?
- What could have happened but did not?
- What failed cases are missing?
- Did we survive because of design or chance?
- What should be made smaller, safer, or more optional next time?

## Default Output For Future Work

```markdown
**一句话判断**
...

**地形**
- Tail:
- 可逆性:
- 路径依赖:
- 透明度:

**Ruin 过滤**
- 出局风险:
- 单点依赖:
- 最大可承受损失:
- 需要先改的结构:

**Payoff 暴露**
| 情况 | 结果 | 损益 | 结论 |
|---|---:|---:|---|

**激励与责任**
- 谁拿好处:
- 谁承担坏处:
- 信任折扣:

**建议动作**
[Avoid / Redesign / Small experiment / Barbell / Commit]

**下一步**
1. ...
2. ...
3. ...

**停止条件**
- ...
```

## Decision Heuristics

Use these as quick defaults:

- If downside is ruin and upside is only moderate, avoid.
- If downside is capped and upside is open, consider small experiments.
- If a strategy makes small steady money and hides rare disaster, be suspicious.
- If the plan requires accurate prediction, redesign toward optionality.
- If the actor giving advice has no downside, discount confidence.
- If data excludes the relevant crisis, do not trust the comfort.
- If a commitment closes many future options, demand stronger evidence.
- If a system becomes more complex to hide simple fragility, simplify.
- If small failures teach cheaply, run more of them.
- If failures are correlated, diversification may be fake.

## Red Flags

- "历史上没亏过"
- "这次不一样"
- "风险很小，收益很高"
- "模型已经考虑了所有情况"
- "大不了之后再退出"
- "先梭哈，错了再说"
- "专家都这么说"
- "平台不会改规则"
- "只要增长继续就没事"
- "平均收益很好"
- "这个概率几乎为零"

## Green Flags

- Downside capped in writing or by structure.
- The user can survive multiple failures.
- The first step creates information.
- The plan has clear exit conditions.
- Incentives are aligned.
- The upside can scale without scaling downside equally.
- The system improves through small stress.
- No single dependency can kill the project.
- The safe base is genuinely safe.

## What This System Is Not

- It is not fortune telling.
- It is not anti-risk.
- It is not "always be conservative."
- It is not a substitute for domain research.
- It is not an excuse to dismiss experts.

It is a way to take better risks.
