---
name: regional-pricing-checker
description: "Review regional pricing for passes and products: confirm the default price is right, check a price table against the platform's reported bounds, decide where regional pricing should be off (donation-style items, gifting and trading risk), and list the Creator Hub steps. Use before launch or when regional prices look odd."
category: money
tags: regional pricing, price levels, purchasing power, default price, bounds, gifting, donation pass, localisation
kb: Roblox/roblox-kb/pricing.md, Roblox/roblox-kb/monetisation-other.md, Roblox/roblox-kb/localization-and-international.md, Roblox/roblox-kb/_tools/CHECKLIST-monetization.md, Roblox/roblox-kb/monetisation-gamepasses.md
related: price-ladder-planner, gamepass-maker, devproduct-handler, donation-system-builder, ugc-item-planner, price-optimization-readiness
---

# regional-pricing-checker

One job: make sure regional pricing helps instead of surprising you. The vault reports that regional prices never exceed the default price and never fall more than 70% below it (a 100 Robux default gives a 30 Robux floor), so the default price is the decision that matters; it also reports cases where regional pricing misbehaved on donation-style passes. The rules and the list of regions belong to Roblox and change, so this skill never encodes region lists, only checks numbers you supply.

## When to use
Before launch, after a price change, or when buyers report odd prices. Not for choosing the price itself (`price-ladder-planner`) or cash-out maths (`devex-planner`).

## Inputs (max 2)
1. The list of passes, products and subscriptions with default prices (default: read the catalogue files, ids and prices from the owner's Creator Hub, never invented). 2. Any regional prices the owner wants to set or has seen (default: none; the platform may recommend its own).

## Procedure
1. Read the rules: `python -I ~/.claude/claude-kit/tools/kbq.py section pricing rules --max-chars 5000`. Note: opt-in and recommendations, the 30-100% bound, the per-player price APIs, and the donation-pass warning. Live-check the Creator Docs regional-pricing page the same day.
2. Review each default price first. The bound means a default of 100 can reach 30 in cheaper regions; make sure the floor still makes sense for what the item costs you to give (currency amounts, rares).
3. Put the table in `prices.json` (`{"items":[{"name","base","regions":{"BR":50}}]}`) and run `python -I ~/.claude/claude-kit/skillpack/money/regional-pricing-checker/scripts/regional.py prices.json --min-ratio 0.3 --max-ratio 1.0`. It fails on prices outside the bound, non-whole prices, gaps between items, and inversions along an `--order poorest,...,richest` list you pass.
4. Decide where it should be OFF: donation-style passes or any item where a lower price in one country lets players there pay less than intended (the vault cites a 10 Robux US price becoming 4 in lower-income countries). Gifting and trading between price levels is a separate risk: use the platform's price-level API server-side before allowing gifts or trades (vault: `GetUsersPriceLevelsAsync`).
5. Never show hard-coded prices in your UI: read the player's actual price from the platform (vault names per-player product-info APIs). `price-optimization-readiness` has the scanner.
6. Test with a regional test account if the owner has one: compare displayed prices to the table. `untested` otherwise.
7. Write the Creator Hub checklist: opt-in per item, what to turn off and why, a monthly review of revenue by country (analytics breakdowns).

## Studio MCP path
Not needed for the check. For the UI part: `list_roblox_studios` -> `get_studio_state` -> `multi_edit` (price display code) -> `start_stop_play` -> `get_console_output`. Studio cannot show regional prices: `untested`.

## Fallback
The script and a hand checklist (headless). Platform behaviour stays `untested`.

## Evidence
`Roblox/roblox-kb/pricing.md` (regional prices bounded to 30-100% of the default; opt in and review recommendations; per-player localised prices via API; a 2025-12 creator report that donation passes can misprice with regional pricing, one source), `Roblox/roblox-kb/monetisation-other.md` ("Regional pricing, gifting and Robux transfers": price-level API for gifting and trading; +26% in emerging markets for regionalised avatar pricing, a Roblox talk), `Roblox/roblox-kb/localization-and-international.md`. The bounds are Roblox Creator Docs 2026-10: live-check.

## Output
`design/regional-pricing.md`: default price review, `regional.py` output, items with regional pricing OFF and why, gifting/trading rule, owner checklist.

## Acceptance checks
- [ ] `regional.py prices.json` exits 0, or every error is explained (quote "0 error(s)").
- [ ] `python -I .../regional.py --selftest` prints "7 checks ok".
- [ ] Every donation-style item is listed with an explicit on/off decision.
- [ ] The Creator Docs regional-pricing page was live-checked (date written) or the plan says unverified.
- [ ] No hard-coded price strings are left in UI code for regionally priced items.

## Pitfalls
Setting the default without considering the 30% floor. Leaving regional pricing on for tips. Allowing gifts across price levels. Assuming a table you invented matches the platform's. Treating the +26% as a promise for your game.

## Related
`price-ladder-planner`, `gamepass-maker`, `devproduct-handler`, `donation-system-builder`, `price-optimization-readiness`.
