# LAB Native Address Review 2026-07-07

Source quality:

- `social`: @ElonKely_ LAB posts from the 500-post sample and live `twitter tweet` fetch.
- `onchain`: local BSC RPC reconstruction for LAB token transfers around block `106102800` to `106105200`.
- `external label`: BscScan labels shown in screenshots and local label file where available.
- `inference`: reusable rules below.

Primary source:

- X post: `https://x.com/ElonKely_/status/2069776065376264525`
- Expanded source link: `https://bscscan.com/token/0x7ec43cf65f1663f820427c62a5780b8f2e25593a?a=0xec01c918e2f700f47332ddc2d216ae9e747bd1a5#transactions`
- LAB BSC token: `0x7ec43cf65f1663f820427c62a5780b8f2e25593a`
- Intermediate wallet: `0xec01c918e2f700f47332ddc2d216ae9e747bd1a5`

## What Was Verified

The source post claimed that LAB moved from Gate cold to hot, then into wallets ending in `d1a5` and `cb65`, then into ASTER for staged selling. It also claimed FDV around `1.7B`, MC around `530M`, OI around `70M`, and funding near `-1`.

Local RPC verified the `d1a5` leg:

- Token metadata: `LAB`, decimals `18`.
- Address `0xec01c918e2f700f47332ddc2d216ae9e747bd1a5` had `17` LAB Transfer logs in blocks `106102845` to `106105044`.
- Repeated pattern: LAB flowed in from CEX-labeled or externally CEX-labeled addresses, then almost immediately flowed out to `0x128463a60784c4d3f46c23af3f65ed859ba87974`.
- Local labels confirmed `0x0d0707963952f2fba59dd06f2b425ace40b492fe` as `Gate 1 Hot Wallet` and `0x53f78a071d04224b8e254e243fffc6d9f2f3fa23` as `KuCoin Hot Wallet 2`.
- Screenshot labels, not yet local labels, identify `0x1ab4973a48dc892cd9971ece8e01dcc7688f8f23` as `Bitget 6`, `0x4982085c9e2f89f2ecb8131eca71afad896e89cb` as `MEXC 13`, and `0x128463a60784c4d3f46c23af3f65ed859ba87974` as `Aster: Treasury`.

Representative RPC rows:

| Block | Direction | Amount LAB | From | To | Tx |
| ---: | --- | ---: | --- | --- | --- |
| 106102845 | out | 3042.9 | `0xec01...bd1a5` | `0x1284...7974` | `0x389928049c68854cbe2af67b984f7b7b21c1930983defc61c4c11dfda44f5991` |
| 106102949 | in | 450.9691 | Gate 1 local label | `0xec01...bd1a5` | `0x2a98afcb876a4e257a1c989a32c0eb65c96f11e811a3ba759bc4e9a85df83d1d` |
| 106104335 | in | 1126.95 | KuCoin Hot Wallet 2 local label | `0xec01...bd1a5` | `0xb43070e095786a4411a08d216def0cb5a8a35d4aae932a6de590ef4bd8546327` |
| 106104541 | in | 1143.9691 | Gate 1 local label | `0xec01...bd1a5` | `0x42dfb6b7ababb051add7101869f79926f179f143d04a1726eedfac946c9b1287` |
| 106104667 | in | 3750.9691 | Gate 1 local label | `0xec01...bd1a5` | `0x1bb47fffb1c64651306e1bdd57eca5d4decf50e308bec11986fae89d57fd227d` |
| 106104693 | out | 3819.919 | `0xec01...bd1a5` | `0x1284...7974` | `0x4358b9e83e50c55144df05138a5c7193a8cfd3c2438e87ed57a13e3804fe15cc` |
| 106105044 | out | 2401.9 | `0xec01...bd1a5` | `0x1284...7974` | `0x54f2cf78de26478ccd6b9777ce339fced16a8069b1bec4571d946a2d9da49b8e` |

## Reusable Interpretation

Classify this setup as `cex_to_perp_venue_sell_route` plus `derivatives-led high-control token`.

Fields to record:

- `path_stage`: CEX hot/cold or deposit source -> intermediate wallet -> Aster/perp venue treasury.
- `cluster_evidence`: multiple CEX sources, same intermediate wallet, repeated near-immediate outflow, repeated amounts in one short time window.
- `identity_label_quality`: local label for Gate and KuCoin; screenshot label for Bitget, MEXC, and Aster Treasury until imported.
- `derivatives_ratio`: OI/MC, OI/FDV, funding, volume/MC, index-venue composition.
- `event_window`: deposit closure/reopening, index composition change, repeated route tests, funding flip.
- `venue_rotation`: Gate, Bitget, KuCoin, MEXC, Aster, Binance perps/index.

## Rules To Add

- A CEX-to-intermediate-to-perp-venue route is stronger than a plain CEX outflow. It suggests active venue routing and possible sell execution rather than simple custody reshuffling.
- Repeated small and medium batches matter when the same intermediate wallet immediately forwards to a trading venue. Amount size alone understates the signal.
- Negative funding with an active sell route is a hostile structure for spot holders, but it can still punish crowded shorts. Action language should be `Reduce` or `Avoid`; short entries need separate liquidation/funding risk checks.
- Deposit-port reopening after a large run-up is a sell-window event. The next confirmation is route activity from project/MM/associated wallets to CEX or perp venue.
- Index composition changes are part of the manipulation surface. If a small CEX is removed from a Binance index basket, old CEX-centric control can lose effectiveness and operators may route through other venues.
- Do not import screenshot-only labels into global CEX labels until a local label review or explorer verification confirms them.

## System Follow-Ups

- Add a review mode that accepts token, suspect wallet, block range, and local label file, then emits `path_stage`, `cluster_evidence`, and missing label quality.
- Add a field to daily reports for `index_or_deposit_policy_event` when venue support, index basket, deposit closure, or deposit reopening appears in source evidence.
- Keep LAB-like high-control tokens in dormant monitor state after a sell cycle. Restart checks when CEX routing, Aster/perp venue deposits, OI, funding, or deposit-port status changes.
