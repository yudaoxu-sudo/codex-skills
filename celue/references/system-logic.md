# Current System Logic

This reference summarizes the user's current sniper/Alpha monitoring system as of 2026-07-07.

## Operating Principle

External sources discover. Local systems verify, explain, store, and alert.

## Evidence Stack

1. Official source: exchange announcement, project/founder/docs, contract source.
2. On-chain source: transactions, receipts, logs, wallet paths, holders, pool actions.
3. Market source: price, volume, OI, funding, liquidation, order book, CEX listing.
4. External social source: Telegram, X/KOL, screenshots, third-party reports.
5. Inference: only after the first four layers are separated.

## Existing Monitors

- Telegram/project ingestion writes deduped projects into the project registry.
- Prelaunch watch tracks known launch windows.
- Opening block watch scans first transfers, swaps, bribes, first buyer cohorts, sellability, and buyer traces.
- Intraday flow watch scans large buys/sells, runtime CEX deposit candidates, and CEX gas priming.
- Perp/OI/funding watch covers Binance/OKX/Bybit public derivatives context.
- Price momentum watch covers Binance Alpha price/depth changes.
- Holder concentration watch separates raw holder concentration from infrastructure-adjusted concentration.
- Surf auxiliary market watch supplies external market context.
- External auxiliary readiness tracks Coinglass/CoinAnk/GMGN/DeBot status; unvalidated sources remain context-only.
- Daily report combines watchlist, opening, intraday, OI, price, holders, external sources, and verification.

## Hard Rules

- No private keys, seed phrases, exchange passwords, cookies, 2FA codes, or Telegram verification codes in chat or memory.
- Current system is read-only.
- Current system does not sign transactions.
- Current system does not execute trades.
- External tools are context until live-probe validated.
- Do not treat CEX hot/deposit wallets, contracts, routers, bridges, LP managers, quote tokens, or exchange aggregators as funding-cluster parents.
- Do not call a project/MM transfer a confirmed sell without next-hop evidence or quote recovery.
- For Pancake v4/Infinity, follow wording requires sellability and recovery-rate gate plus opening-block/cohort/venue/distribution rules.
- For Alpha-dominant tokens, on-chain netflow cannot create bullish follow language unless venue reliability is explicitly enabled.

## Action Language

Use these action labels consistently:

- `Avoid`: toxic or unverifiable structure.
- `Observe`: signal exists, confirmation missing.
- `Reduce`: held exposure faces distribution, unlock, CEX inflow, or sellability risk.
- `Small test`: bounded risk and verified exit path.
- `Follow only after confirmation`: early setup requiring additional evidence.

## Default Questions

- What exact event is happening?
- Which wallet path changed?
- Is it CEX inflow, CEX outflow, cold-to-hot, bridge, pool, unknown wallet, or contract movement?
- What path stage is visible now: source wallet, CEX cold/hot/deposit, fresh cluster, gas source, sell venue, or quote recovery?
- Is there batch behavior: new-wallet cluster, multisig fan-out, same deposit port, synchronized gas funding, or repeated test deposits?
- Does OI/funding support or conflict with the chain read?
- What are OI/MC, OI/FDV, and 24h volume/MC?
- Is the setup chain-led, derivatives-led, listing/deposit-led, unlock-led, or sector-led?
- Is FDV/MC/OI proportion abnormal?
- Is there an unlock, claim, distribution, or deposit-status change?
- Did deposit status change: closed, open, reopened, migrated chain, or unknown?
- Is the token led by Alpha/CEX, DEX, old-coin narrative, meme flow, or unknown venue?
- Is there monitored-tag, delisting, index-weight, or market-cap-maintenance pressure?
- What is the catalyst source: official, founder, exchange, KOL, media, community, or unknown?
- For meme/news trades, what was the first-seen time, market cap at discovery, liquidity, holder quality, and current stage?
- For tokenomics catalysts, is it burn, buyback, buyback-to-liquidity, fee donation, foundation, airdrop, initial float, or utility change?
- Is a wallet label verified as founder/foundation/custody/MM/whale, or only inferred?
- Which venue currently owns attention: Binance Alpha, Binance spot/perps, Binance Wallet, Coinbase, Korea CEX, SOL/Pump, Base, ASTER, or other?
- For Alpha openings, what are initial price, LP range, token-side depth, quote-side depth, and modeled price after `100k / 200k / 400k / 1m` buy pressure?
- What is the opening-block evidence: `transactionIndex`, internal payments, failed bribe attempts, bundle relationships, and first buyer cohort?
- Who buys after the user: official campaign, CEX/Alpha flow, MM, whale, KOL/community, retail, or arbitrage?
- What is the user's cost basis versus known accumulation cost, support range, and realistic market-cap ceiling?
- What evidence would flip the current action?

## ElonKely-Derived Checks

- Treat CEX path as a staged process and report the current stage before action language.
- Upgrade urgency when cluster evidence appears: batch wallets, same source, same deposit port, same gas source, or synchronized timing.
- Mark deposit reopenings after a large run-up as sell-window risk until local chain evidence clears it.
- Label derivatives-led setups when OI or volume becomes abnormal before chain movement.
- Keep dormant monitors for prior high-control tokens; restart attention when CEX flow, OI, gas priming, or sector flow returns.
- Separate wash volume, Alpha brushing, maker inventory movement, organic buys, and confirmed sell pressure.
- Treat meme/news triggers as speed trades with explicit exit discipline and stage labels.
- Treat listing, seed tag, monitoring tag, delisting, and wallet support as a calendar queue requiring exact timestamps and pressure checks.
- Label tokenomics mechanisms before judging direction; burn, buyback, airdrop, initial float, and foundation formation create different risks.
- Verify identity labels before using founder, foundation, custody, MM, whale, or KOL behavior as evidence.
- Track venue rotation so weak signals are downgraded when attention has migrated elsewhere.

## LAB-Derived Checks

- Treat CEX -> intermediate wallet -> perp venue treasury as a distinct sell-route class, not a generic CEX transfer.
- Record label quality separately for each hop; local labels, explorer screenshot labels, and inferred labels are not equal.
- When repeated in/out batches use the same intermediate wallet and short time window, summarize the cluster before judging direction.
- Pair route evidence with OI/MC, OI/FDV, funding, volume/MC, and index composition because high-control tokens can absorb chain selling through derivatives control.
- Treat deposit-port reopening, venue support, and index-basket changes as event-window inputs even before a large transfer appears.

## aLiiDeez-Derived Checks

- Treat Binance Alpha and similar openings as pool-structure problems before narrative calls: start time, hook, LP position, initial price, range, and modeled buy pressure are required fields.
- For V3-style pools, classify capacity as hostile when small buy pressure can exhaust the active range or force extreme slippage.
- Verify tokenomics through holder paths, lock contracts, Alpha/CEX/MM allocation wallets, bridge inventory, and project residual supply.
- Inspect opening blocks with `transactionIndex`, internal transfers, failed txs, and builder/validator payments; visible gas alone cannot clear bundle or bribe risk.
- When low-fee first buyers outrank high-bribe attempts, check for project-side bundle, self-buy, or LP/swap coupling before labeling the buyer as a normal sniper.
- Treat repeated pool edits, single-sided sell pools, and range resets as events that can signal support, distribution, or price maintenance.
- Track sniper cost, sell completion, and project/MM support before considering post-dump second-entry setups.
- Treat cross-chain bridge state and residual supply as continuation risk for low-float openings.

## 0xcrypto_max-Derived Checks

- Treat information edge as a time-decay asset: record first source, first-seen time, market cap, liquidity, and delay to public spread.
- Require a buyer stack before entry: official/campaign flow, CEX/Alpha flow, MM, whale, KOL/community, retail, or arbitrage.
- Split market-maker or "庄" labels into accumulation, pump, dump, distribution, bot/sniper, retail, and unknown roles based on repeated behavior.
- Treat cost basis, stop distance, realistic upside, and position size as the first risk gate.
- Downgrade setups when capacity is poor, attention is split, or the next buyer is mostly slower retail.
- For second-wave trades, require reset plus new demand: accumulation, reduced sell pressure, narrative restart, MM/whale support, OI/volume, or sector liquidity.
- Treat major posts and investigations as attention events that can create liquidity windows; confirm with chain and market reaction before action language.
- Define sell logic before entry: buyer-stack failure, flow reversal, time stop, price level, or market-cap ceiling.
