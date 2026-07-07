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
- Does OI/funding support or conflict with the chain read?
- Is FDV/MC/OI proportion abnormal?
- Is there an unlock, claim, distribution, or deposit-status change?
- Is the token led by Alpha/CEX, DEX, old-coin narrative, meme flow, or unknown venue?
- What evidence would flip the current action?
