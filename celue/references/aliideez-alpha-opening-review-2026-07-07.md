# aLiiDeez Alpha Opening Review 2026-07-07

Source scope: local `@aLiiDeez` X research output in `/Users/xuyufan/Documents/狙击手进程/output/aliideez_x_research`.

Source quality:

- `sampled`: 97 retained posts, 92 method-index rows, 86 case-index rows.
- `sampled`: 142 media URLs were downloaded and OCR processed.
- `social`: author conclusions remain KOL material until local tx, block, LP, holder, and CEX evidence is reconstructed.
- `onchain`: rows with tx hashes, addresses, block numbers, and LP position IDs provide verification entry points.

Local source files:

- `/Users/xuyufan/Documents/狙击手进程/output/aliideez_x_research/analysis/method_library.md`
- `/Users/xuyufan/Documents/狙击手进程/output/aliideez_x_research/analysis/case_index.md`
- `/Users/xuyufan/Documents/狙击手进程/output/aliideez_x_research/analysis/review_queue.md`
- `/Users/xuyufan/Documents/狙击手进程/output/sniper_weapon_system.md`

## Method Concentration

| Method class | Count |
| --- | ---: |
| Address / monitoring / tools | 66 |
| Pool / liquidity / price range | 61 |
| CEX / Alpha / listing | 60 |
| Chips / unlock / tokenomics | 55 |
| Opening / snipe / new launch | 54 |
| Cross-chain / bridge / multi-chain spread | 21 |
| Bribe / bundle / MEV | 16 |
| Market maker / control / cost | 8 |

## Durable Rules

### 1. Treat Alpha openings as a pool-structure problem first

Before action language, record:

- exact start time and timezone;
- token contract and trading pair;
- DEX version or hook type;
- LP position ID;
- initial price, min price, max price;
- one-sided or two-sided liquidity;
- token-side depth and quote-side depth;
- estimated price after `100k / 200k / 400k / 1m` USD buy pressure.

If a small buy can push price through the V3 range, classify capacity as hostile even when narrative is strong.

### 2. Verify tokenomics through addresses, not only documents

Build an address table before judging quality:

- team / investor / ecosystem / community / airdrop / Alpha / CEX / MM allocation;
- timelock or vesting contract address, owner, and unlock function;
- multisig owner and secondary owner when visible;
- bridge inventory by chain;
- project wallet residual supply;
- CEX or Alpha wallet funding path.

Address allocation that matches tokenomics raises review confidence. Unlocked allocation or unexplained custody lowers it.

### 3. Model sniper cost with bribe and slippage

Opening-block cost is:

```text
buy notional + slippage + explicit fee + internal bribe / bundle payment
```

For BSC and similar chains, inspect block order, `transactionIndex`, internal transfers, failed transactions, and builder or validator payments. A low visible gas fee does not clear a wallet when internal payment or bundle sequencing exists.

### 4. Investigate project-side buying when order priority looks unnatural

If a low-fee wallet executes before high-bribe failed attempts, inspect whether LP mint, approve, swap, and payment paths were bundled or controlled by the project. Do not call the front buyer a normal sniper until same-block relationships are cleared.

### 5. Separate sniper dump from project or MM support

After the first opening wave, track:

- how much the sniper bought;
- realized average cost after bribe;
- sell amount, sell venue, and sell completion;
- whether project/MM wallets buy after sniper selling;
- whether liquidity is replenished or withdrawn.

Sniper sell completion can create a second-entry window only when sellability, price support, and remaining supply are verified.

### 6. Treat pool edits as events

Repeated add/remove/reprice actions are not noise. Mark:

- pool withdrawal;
- new price range;
- single-sided sell pool;
- range extension after price exits the old range;
- project wallet adding owned tokens into a high-price pool.

Single-sided sell liquidity from project-controlled wallets is distribution risk until quote recovery or MM mandate is proven.

### 7. Treat cross-chain state as supply risk

For multi-chain launches, check:

- bridge opened or closed;
- chain path initialized;
- remaining token inventory on each chain;
- burn/mint records;
- whether only the project can bridge at the time of trading;
- price spread between chains and CEX or premarket.

Another chain with large residual supply can cap continuation even when the active chain looks low-float.

### 8. Keep Alpha wallet and CEX wallet labels precise

Transfers into Alpha campaign wallets, CEX wallets, MM wallets, or project custody wallets have different meanings. Do not call an Alpha allocation transfer a project dump without next-hop sell evidence.

### 9. Do not follow high opening FDV without a buyer stack

Before any `Small test`, answer:

- who buys after the opening sniper;
- whether Alpha/CEX/MM/retail demand can absorb the float;
- whether the pool supports the intended size;
- whether entry cost stays below the verified support level;
- what invalidates the setup.

### 10. Convert KOL launch posts into structured fields

Extract fields from a launch post, then verify locally:

| Field | Required verification |
| --- | --- |
| start time | official page, contract timestamp, pool tx |
| contract | explorer and token metadata |
| LP position | DEX position and pool logs |
| initial price | pool state and token decimals |
| estimated snipe price | local price-impact calculation |
| bribe/bundle claim | block trace and internal tx |
| CEX/Alpha allocation | transfer path and wallet label |
| cross-chain claim | bridge logs and chain inventory |

## Action Mapping

- `Avoid`: pool is too thin, range is already exhausted, project wallet is selling, cross-chain residual supply is large, or address allocation is unverifiable.
- `Observe`: launch time and contract are known, but LP range, sellability, or opening cohort is missing.
- `Small test`: opening price, pool capacity, holder path, sellability, and exit level are all verified; size stays inside the modeled depth.
- `Follow only after confirmation`: KOL finds a launch early, but pool and buyer stack still need local checks.
- `Reduce`: held exposure meets pool withdrawal, CEX inflow, bridge-open supply shock, or project single-sided sell liquidity.
