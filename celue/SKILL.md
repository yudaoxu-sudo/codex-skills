---
name: celue
description: "Crypto strategy operating skill for on-chain opportunity review, Binance Alpha/new-token monitoring, CEX flow interpretation, KOL signal distillation, position risk decisions, and updating the user's reusable trading rules. Use when the user says celue, 策略, 策略准则, 链上机会, 妖币, Alpha, 新币, KOL经验, 帮我判断币, 买不买, 卖不卖, 减仓, 追不追, 复盘, or asks to integrate market lessons into the user's system."
---

# Celue

## Purpose

Turn crypto market noise into a disciplined operating decision. Use this skill to evaluate a token, event, KOL signal, wallet movement, unlock, listing, Alpha pool, or suspicious on-chain flow, then produce a clear action plan with evidence levels and invalidation rules.

This skill is a living operating system. When the user asks to update strategy, add the smallest durable rule to this skill and keep the source evidence traceable.

## Source Discipline

Start every analysis by separating claim types:

- `official`: exchange/project/founder/docs/contract source.
- `onchain`: transaction, receipt, log, holder, wallet, CEX path, pool, bridge, unlock contract.
- `market`: price, volume, OI, funding, liquidation, order book, CEX listing.
- `social`: KOL post, Telegram channel, screenshot, third-party report.
- `inference`: your reasoned conclusion from the above.

Do not let social claims directly become trading actions. Convert social claims into fields to verify.

## Default Workflow

1. Define the token/event and time window.
2. Build the evidence map: official, on-chain, market, social, inference.
3. Classify the setup:
   - accumulation / distribution / listing catalyst / unlock risk / opening-block snipe / meme rotation / old-coin narrative / market-maker control / unknown.
4. Check the core lenses:
   - CEX flow: exchange outflow, exchange inflow, cold-to-hot, deposit path, unknown-wallet next hop.
   - OI/funding: open interest expansion, funding direction, liquidation pressure, long/short crowding.
   - FDV/MC/OI scale: whether derivatives exposure is large relative to circulating value.
   - Holder and unlock: concentration, known locked supply, unlock calendar, top-holder movement.
   - Venue class: Alpha/CEX-led, on-chain-led, mixed, or unknown.
   - Timing: listing time, opening block, unlock start, sector rotation, overnight risk.
5. Assign action:
   - `Avoid`: evidence is dirty, sell path active, unlock/holder risk dominates, or liquidity is hostile.
   - `Observe`: early anomaly, missing confirmation, or market structure incomplete.
   - `Reduce`: held position faces confirmed distribution or CEX inflow risk.
   - `Small test`: bounded-cost setup with verified sellability, low crowding, and clear stop.
   - `Follow only after confirmation`: early signal requires price/OI/on-chain confirmation.
6. Output stop rules and update triggers.

## Core Rules

- Treat KOL posts as discovery. Verify with chain, CEX, and market data before action.
- Treat CEX inflow from project/MM/early-holder paths as sell pressure until next-hop evidence clears it.
- Treat CEX outflow into fresh wallets as possible accumulation, then wait for the next hop.
- Track cold wallet to hot wallet to deposit wallet to sell venue paths. The path matters more than a single transfer.
- Record the path stage explicitly: source wallet, exchange cold/hot/deposit wallet, fresh wallet cluster, gas source, sell wallet, quote-token recovery.
- Batch-created wallets, multisig fan-out, gas priming, and repeated exchange deposit tests carry more weight than a single large transfer.
- Deposit-port status matters. Closure, reopening, chain migration, and restored exchange deposits can change the sell-pressure window.
- Do not mark a transfer as confirmed sell unless receipt or next-hop evidence shows quote-token recovery or exchange deposit with sell intent.
- If a sell route moves from CEX hot/cold wallets into an intermediate wallet and then into a perp venue treasury or trading venue, record it as `cex_to_perp_venue_sell_route` instead of treating the intermediate wallet as retail.
- Exchange index composition, deposit-port reopening, and venue support changes are market-structure events. They can raise or lower manipulation cost even before a large token transfer appears.
- For low-cap tokens, combine FDV, MC, OI, funding, and CEX flow. A large OI relative to MC changes the risk surface.
- If OI or volume is abnormal while chain movement is quiet, classify the setup as derivatives-led and avoid chain-only conclusions.
- Track OI/MC and 24h volume/MC ratios for manipulated small caps; extreme ratios can reveal market-maker control before chain flow appears.
- Do not chase the first anomaly. Early chain activity is a watchlist trigger, not an entry by itself.
- If a token already had one manipulation cycle, keep monitoring it. Repeat cycles can occur after redistribution, wash volume, and OI reset.
- For old large-cap or "regular army" tokens, weigh news, business catalysts, tech upgrades, sector rotation, and broad market structure more heavily than small on-chain flows.
- Respect sector liquidity migration. When meme flow absorbs attention, reduce confidence in secondary Alpha/yield narratives unless fresh CEX/chain evidence appears.
- For listing catalysts, record exact exchange, listing time, deposit status, market pair, and whether deposits opened before trading.
- For monitored-tag or possible delisting tokens, ask whether the move is market-cap maintenance, index-weight defense, or forced liquidity work.
- For meme/news triggers, record original catalyst, source authority, first-seen time, market cap at discovery, liquidity, holder quality, and time lag to price move.
- Major-account reposts, founder posts, exchange posts, and official campaign posts are event triggers; they require speed and exit discipline, not blind conviction.
- For post-run meme names, treat 5x-10x moves after the first public trigger as late-stage unless fresh liquidity and holder quality support continuation.
- For tokenomics catalysts, separate burn, buyback, buyback-to-liquidity, fee donation, foundation formation, airdrop, and initial circulation. Each creates a different pressure profile.
- For celebrity/founder/institution wallet claims, verify label quality before action. Custody, foundation, market maker, and whale wallets are not interchangeable.
- Treat small test deposits to exchange wallets as early sell-route probes when the same wallet has repeated this pattern historically.
- For funding extremes, separate short squeeze risk from distribution risk. Negative funding with active CEX sell paths is different from negative funding with no sell path.
- For opening-block snipes, do not follow until sellability, opening cohort, wallet source, venue class, and price capacity pass.
- Preserve capital when evidence is incomplete. Missed upside is acceptable; ruin or trapped liquidity is unacceptable.

## Output Shape

Use Chinese by default.

```markdown
**一句话判断**
...

**证据分层**
| 类型 | 证据 | 可信度 | 还缺什么 |
|---|---|---|---|

**当前结构**
- Setup:
- 主导场所:
- 钱包路径:
- 路径阶段:
- 集群/批量行为:
- OI/funding:
- FDV/MC/OI:
- 事件窗口:
- 催化源:
- meme阶段:
- 代币经济学事件:
- 场所轮动:
- 解锁/持仓:

**动作**
- 现货:
- 合约:
- 仓位:
- 最晚处理时间:

**触发器**
- 加强:
- 失效:
- 退出:

**需要继续盯**
1. ...
2. ...
3. ...
```

## Resource Loading

Load only the needed reference:

- `references/elonkely-review-2026-07-07.md`: distilled lessons from the reviewed `@elonkely_` posts.
- `references/lab-native-address-review-2026-07-07.md`: LAB address and CEX-to-Aster route case study.
- `references/aliideez-alpha-opening-review-2026-07-07.md`: `@aLiiDeez` Alpha opening, pool range, bribe/bundle, cross-chain, and launch-capacity rules.
- `references/crypto-max-market-structure-review-2026-07-07.md`: `@0xcrypto_max` market-structure, buyer-stack, capacity, cost-basis, and second-wave rules.
- `references/system-logic.md`: the user's current sniper/Alpha monitoring logic and evidence hierarchy.
- `references/update-protocol.md`: how to update this skill after new cases.
