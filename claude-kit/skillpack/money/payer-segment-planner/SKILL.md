---
name: payer-segment-planner
description: "Segment players into spend bands from a spend export, show who pays for the game (band sizes, revenue shares, ARPPU, concentration), and tailor offers and content per segment without pressure. Use when deciding who to build offers for or why revenue is lumpy; fixing the shop funnel is shop-conversion-optimizer."
category: money
tags: segments, whales, minnows, dolphins, arppu, spend bands, ltv, veterans, tourists, concentration
kb: Roblox/roblox-kb/monetisation-other.md, Roblox/roblox-kb/analytics-metrics.md, Roblox/roblox-kb/pricing.md, Roblox/roblox-kb/retention-d1-d7.md, Roblox/roblox-kb/all-numbers-and-benchmarks-TLDR.md
related: shop-conversion-optimizer, upsell-moment-finder, price-ladder-planner, starter-pack-designer, retention-diagnoser, limited-offer-designer
---

# payer-segment-planner

One job: know who actually pays and design for each group honestly. The vault's picture: 61% of spenders sit in the smallest lifetime-value bucket (1-800 Robux), veterans (90+ days) drive most revenue, concentration claims range from top 15% giving about 50% to 1-5% giving 75% (different sources and eras), tourists want immediate visible items and locals want long-term value. `scripts/segments.py` computes your own numbers from an export so you can compare, not assume.

## When to use
Planning offers or events, explaining lumpy revenue, or deciding whether to build for high spenders. Not for: funnel leaks (`shop-conversion-optimizer`), moment finding (`upsell-moment-finder`). Never to target individual players with pressure.

## Inputs (max 2)
1. A CSV `userId,robux` of spend per player in a window, including zero spenders, ids hashed (default: ask the owner to export from their own analytics; if none exists, say what to log with the Analytics system first). 2. Band edges (default 1,801,5001).

## Procedure
1. Read the rules: `python -I .rbx/claude-kit/tools/kbq.py section monetisation-other rules --max-chars 4000` (veterans, tourists, tiered price range, first purchase).
2. Check the export has no names or personal data; if it does, stop and ask for a hashed version.
3. Run `python -I .rbx/claude-kit/skillpack/money/payer-segment-planner/scripts/segments.py spend.csv --bands 1,801,5001`. It prints players and Robux per band, payer conversion, ARPPU and the revenue share of the top 1, 5 and 10% of payers.
4. Read it: if one band dominates revenue, offers for it matter most; if the smallest paying band is the largest group, the entry rung and starter pack matter most (`starter-pack-designer`).
5. Per segment plan, in plain terms: non-payers (free paths, soft-currency routes, Premium and rewarded-ad income: `premium-benefits-planner`, `rewarded-ad-planner`), small payers (entry rung, first-purchase moment), core payers (bundles, recurring value, season passes), top payers (cosmetic depth, status, community recognition; never pay-to-win or pressure).
6. Fairness check: no offer for any segment may gate core progress or give pvp power (`pay-to-win-checker`); do not use anything about a payer's spend to apply pressure or change prices per person (price tests are platform-run).
7. Compare the output with the vault's claims only to see where you sit; if your concentration is far higher, broaden the audience (the vault's note: high ARPPU with low ARPDAU means revenue from few users).
8. Re-run monthly and after each big update; store results in `design/segments.md`.

## Studio MCP path
Not applicable: data comes from analytics exports. If events need adding: `list_roblox_studios` -> `get_studio_state` -> `multi_edit` -> `start_stop_play` -> `get_console_output` to confirm the spend events fire.

## Fallback
Run the script on any CSV (headless). Anything about causes stays a hypothesis until an experiment.

## Evidence
`Roblox/roblox-kb/monetisation-other.md` ("Target veterans and big spenders, but don't ignore tourists"; "Offer a tiered price range": 61% of spenders in the 1-800 bucket; concentration claims from Roblox DevForum 2019, a Roblox talk 2023, a creator and Roblox docs), `Roblox/roblox-kb/analytics-metrics.md` (ARPPU, conversion, breakdowns), `Roblox/roblox-kb/pricing.md`, `Roblox/roblox-kb/retention-d1-d7.md`, `Roblox/roblox-kb/all-numbers-and-benchmarks-TLDR.md`. Several concentration figures are creator-claimed: labelled so.

## Output
`design/segments.md`: the band table, concentration, per-segment plan, fairness check, next month's data to collect.

## Acceptance checks
- [ ] `segments.py` output is quoted with the window and player count.
- [ ] `python -I .../segments.py --selftest` prints "6 checks ok".
- [ ] The export contains no names or personal data (stated).
- [ ] No segment plan includes pressure tactics, per-person pricing or core gating.
- [ ] Vault claims are cited as claims with their source labels, not as targets.

## Pitfalls
Calling a few big spenders a business model. Ignoring non-payers who bring Premium and ad income. Excluding low spenders because they are small individually. Treating one month as stable. Sharing identifiable spend data.

## Related
`shop-conversion-optimizer`, `upsell-moment-finder`, `price-ladder-planner`, `starter-pack-designer`, `retention-diagnoser`.
