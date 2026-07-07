# 0xcrypto_max Market Structure Review 2026-07-07

Source scope: local `@0xcrypto_max` X research output in `/Users/xuyufan/Documents/狙击手进程/output/0xcrypto_max_x_research`.

Source quality:

- `sampled`: 136 retained posts, 106 method-index rows, 72 case-index rows.
- `sampled`: 98 media files were downloaded and OCR processed; oEmbed supplied the core text rows.
- `social`: author conclusions remain KOL material until local chain, market, and execution evidence confirms them.
- `inference`: this reference extracts reusable market-structure rules from repeated posts.

Local source files:

- `/Users/xuyufan/Documents/狙击手进程/output/0xcrypto_max_x_research/analysis/method_library.md`
- `/Users/xuyufan/Documents/狙击手进程/output/0xcrypto_max_x_research/analysis/case_index.md`
- `/Users/xuyufan/Documents/狙击手进程/output/0xcrypto_max_x_research/analysis/review_queue.md`
- `/Users/xuyufan/Documents/狙击手进程/output/sniper_weapon_system.md`

## Method Concentration

| Method class | Count |
| --- | ---: |
| Address / monitoring / tools | 47 |
| CEX / Alpha / listing | 42 |
| Market maker / control / cost | 36 |
| Opening / snipe / new launch | 18 |
| Chips / unlock / tokenomics | 14 |
| Pool / liquidity / price range | 12 |
| Bribe / bundle / MEV | 1 |

## Durable Rules

### 1. Start from information edge and timestamp

For Alpha, meme, and second-wave setups, record:

- first source and first-seen time;
- whether the source is official, smart-money address, group, KOL, CEX page, or market screen;
- market cap and liquidity at discovery;
- time lag between discovery and public spread;
- whether the setup is still early enough for the user's execution speed.

Late discovery converts an Alpha signal into a liquidity-exit risk.

### 2. Ask who buys after the user

Every entry needs a buyer stack:

- official or founder attention;
- exchange campaign or listing flow;
- MM support;
- smart-money accumulation;
- KOL/community spread;
- retail FOMO;
- cross-chain or CEX arbitrage demand.

If the only next buyer is slower retail, downgrade the action.

### 3. Separate wallet roles in market-maker or "庄" reads

Do not use one generic market-maker label. Classify visible wallets:

- accumulation wallet: buys low, rarely sells;
- pump wallet: pushes key levels with visible buys;
- dump wallet: sells into attention or high-liquidity windows;
- distribution wallet: splits and routes inventory across wallets or venues;
- bot/sniper wallet: fast entry and fast exit;
- retail wallet: small and reactive;
- unknown wallet: insufficient evidence.

A wallet role needs behavior across time, not one profitable buy.

### 4. Treat cost basis as the first safety layer

Before `Small test`, answer:

- current entry relative to known accumulation cost;
- distance to stop level;
- expected upside to realistic ceiling;
- whether a 5x-style outcome is still structurally possible;
- whether the position size can survive the stop.

High-cost entry with weak upside becomes `Avoid` or `Observe`.

### 5. Capacity controls expected return

Record:

- current liquidity and depth;
- realistic market-cap ceiling under current sector flow;
- how much size can enter without changing the setup;
- whether similar runners are splitting attention;
- whether the venue has enough new money.

Small wallets can exploit thin mispricing. Larger size needs a verified buyer stack and depth.

### 6. Use second-wave rules for old or post-run tokens

A second-wave setup needs:

- prior attention that can restart;
- evidence of accumulation after first wave;
- reduced immediate sell pressure;
- narrative still capable of spreading;
- MM or whale behavior that supports continuation;
- market or sector liquidity returning.

Prior pump alone is not a reason to re-enter. Prior pump plus reset and new demand can restart monitoring.

### 7. Treat news and influencer posts as attention events

Official posts, founder posts, major-account reposts, and investigative posts can create attention. They can also give market makers a liquidity window.

Convert the post into:

- catalyst source;
- first-seen time;
- related token or ticker;
- price reaction before and after the post;
- volume/OI reaction;
- chain flow response;
- who likely bought the move.

Without chain or market confirmation, keep the signal in `Observe`.

### 8. Make sell logic explicit

Before entry, define:

- where the first buyer stack weakens;
- what price or market cap means the easy money is gone;
- whether the thesis is a speed trade, second-wave trade, or accumulation trade;
- whether the exit is based on price, flow, time, or invalidated buyer stack.

For meme and Alpha trades, delayed exit after buyer-stack exhaustion is usually the largest avoidable loss.

### 9. Do not let "finding the market maker" replace thesis quality

Market-maker behavior is useful only when it improves a complete setup:

- low or acceptable cost;
- visible accumulation;
- narrative or event catalyst;
- enough liquidity;
- defined exit;
- no immediate unlock, bridge, or CEX sell route.

When any of these fields are missing, mark the market-maker claim as `social` or `inference`.

### 10. Convert KOL market-structure posts into fields

| Field | Required verification |
| --- | --- |
| information source | timestamped post, official page, address alert, or group message |
| discovery stage | market cap, liquidity, volume, holder quality |
| buyer stack | official, MM, whale, KOL, retail, CEX, Alpha |
| wallet role | repeated buys/sells and funding path |
| cost basis | average buy, support range, stop distance |
| capacity | pool depth, order book, market cap ceiling |
| continuation evidence | accumulation, OI, volume, sector flow |
| exit trigger | buyer-stack failure, flow reversal, time stop, price level |

## Action Mapping

- `Avoid`: entry is late, buyer stack is mostly retail, wallet role is unverified, capacity is poor, or stop cannot be defined.
- `Observe`: narrative exists, but accumulation, buyer stack, or liquidity still needs confirmation.
- `Small test`: cost basis, buyer stack, capacity, and exit are all defined and position size remains bounded.
- `Follow only after confirmation`: early KOL discovery needs market and chain confirmation before entry.
- `Reduce`: held exposure reaches buyer-stack exhaustion, MM distribution, attention-only pump, or liquidity drain.
