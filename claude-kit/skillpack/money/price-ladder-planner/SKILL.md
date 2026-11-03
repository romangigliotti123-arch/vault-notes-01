---
name: price-ladder-planner
description: "Build a Robux price ladder for passes, products and bundles - entry, core, premium and whale tiers with sensible spacing - from the vault's sourced rules, assign each offer to a tier and write the test plan (what to change, how long, what result moves a price). Use when pricing a new shop or when conversion or ARPPU looks off."
category: money
tags: price, pricing, ladder, robux, tiers, regional pricing, price optimization, test, conversion, bundle
kb: Roblox/roblox-kb/pricing.md, Roblox/roblox-kb/_tools/PRICE-LADDER.md, Roblox/roblox-kb/monetisation-gamepasses.md, Roblox/roblox-kb/monetisation-devproducts.md, Roblox/roblox-kb/ab-testing-and-experiments.md
related: gamepass-maker, devproduct-handler, starter-pack-designer, regional-pricing-checker, price-optimization-readiness, shop-conversion-optimizer, roblox-monetization-audit
---

# price-ladder-planner

There is no pricing formula in the vault: start, observe, adjust (pricing, "start, observe, adjust"). What helps is a ladder with wide spacing, a very cheap entry rung and a plan to test. Almost every price point in the KB is creator-reported (indie flag); only the mechanics (Price Optimization, regional pricing) are official.

## When to use
Pricing a new set of offers, repricing after weak conversion, or checking that a shop has an entry rung and a top rung. Not for: deciding WHAT to sell (`gamepass-maker`, `starter-pack-designer`).

## Inputs (max 3)
1. The offers: name, type (pass/product/bundle), what it gives. 2. Audience (default: young, mobile, low spend in first 30 minutes). 3. Current prices and sales counts if any (default: none).

## Procedure
1. Read the rules: `python -I ~/.claude/claude-kit/tools/kbq.py section pricing rules --max-chars 4000` and the default ladder in `Roblox/roblox-kb/_tools/PRICE-LADDER.md` (Impulse/entry about 25-100, Core about 100-400, Premium about 400-2000+, Whale 6000-10000+, all indie-labelled).
2. Choose the entry price (the cheapest real purchase; vault: offer a wide ladder including very cheap points; new players rarely spend much in the first 10-30 minutes). Run the helper for spacing: `python -I ~/.claude/claude-kit/skillpack/money/price-ladder-planner/scripts/ladder.py --entry 49 --tiers 6 --rule double100` (rule `double100` = previous x 2 + 100, from one DevForum guide; `x2` and `x2.5` also available). Treat the output as a starting grid.
3. Assign each offer to a tier by player value, not cost to you: impulse boosts and the starter pack at the low rungs; permanent convenience and bundles in the middle; large currency packs and limited exclusives at the top. Every important need moment (cannot afford X) should have a matching exact-need product.
4. Check coverage: at least one rung under 100, one in core, one premium; no two offers within 15 percent of each other doing the same job; the best-value pack is visibly better per Robux than the smaller ones (volume discount) without insulting small buyers.
5. Regional pricing and Price Optimization: check the official mechanics live (`kbq.py docs "price optimization"`); the vault notes Price Optimization needs roughly 60,000 transactions in the prior 30 days and all passes/products in scope, and tests run about 3 weeks. If not eligible, run manual tests.
6. Test plan: change one price at a time; hold for at least a week of comparable traffic; success = revenue per visitor or per DAU up, not units sold alone; keep a log (`decisions.md`: date, price, result). Lower when few buy; raise on the next version when sales are strong.
7. Output the ladder and the plan. Never state a price as correct, only as the starting test.

## Studio MCP path
Not needed (planning). Optional: `execute_luau` (Edit) to list existing pass/product config modules, or `script_grep` for hard-coded prices in code that should read from one config.

## Fallback
The same procedure from the KB and the script; no tooling beyond Python.

## Evidence
`Roblox/roblox-kb/pricing.md` (no formula; test on live data; Price Optimization prerequisites and mechanics; regional pricing; wide ladder; cheap early offers), `Roblox/roblox-kb/_tools/PRICE-LADDER.md` (tier table; "almost all price points are creator-reported; only mechanics and limits are official"), `Roblox/roblox-kb/monetisation-gamepasses.md`, `Roblox/roblox-kb/monetisation-devproducts.md`, `Roblox/roblox-kb/ab-testing-and-experiments.md`.

## Output
`design/price-ladder.md`: ladder table (tier, Robux, band, offers assigned, why), coverage check, regional/optimisation notes with date, test plan table (change, start, hold period, metric, decision rule).

## Acceptance checks
- [ ] Helper output pasted or its selftest passes (`python -I scripts/ladder.py --selftest` prints "selftest ok").
- [ ] Entry rung under 100 exists; every offer sits on a rung.
- [ ] No claim that a price is right; every row carries "test".
- [ ] Source flags (indie/official) shown for any benchmark quoted.
- [ ] Test plan changes one variable at a time with a metric.

## Pitfalls
Copying a competitor's price (different audience and economy). Pricing in a vacuum from developer cost. Comparing units sold instead of revenue per visitor. Changing prices during an event. Ignoring the Robux the buyer has: kids buy fixed Robux packs, so odd prices leave awkward remainders.

## Related
`gamepass-maker`, `devproduct-handler`, `starter-pack-designer`, `regional-pricing-checker`, `price-optimization-readiness`, `roblox-monetization-audit`.
