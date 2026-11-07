---
name: price-optimization-readiness
description: "Check whether a game can use the platform's automatic price tests: confirm the eligibility conditions with the owner, scan the project for hard-coded Robux prices, replace them with prices read from the platform, and prepare the opt-in list. Use before asking Roblox to run price optimisation or managed pricing; choosing prices by hand is price-ladder-planner."
category: money
tags: price optimization, managed pricing, hard-coded price, getproductinfo, eligibility, transactions, dynamic price check, plus discount
kb: Roblox/roblox-kb/pricing.md, Roblox/roblox-kb/monetisation-gamepasses.md, Roblox/roblox-kb/monetisation-other.md, Roblox/roblox-kb/_tools/CHECKLIST-monetization.md, Roblox/roblox-kb/case-studies-adopt-me.md
related: price-ladder-planner, gamepass-maker, devproduct-handler, regional-pricing-checker, shop-conversion-optimizer
---

# price-optimization-readiness

One job: get the code and catalogue ready so the platform's price tests can run and discounts display correctly. The vault says Price Optimization auto-tests prices on user subsets and applies prices only when incremental total revenue is positive; it needs about 60,000 transactions in the previous 30 days and every pass and product included; prices must be scripted through `MarketplaceService`, not hard-coded, using `GetProductInfo` with the product or game-pass info type; and the platform's Dynamic Price Check (up to 5 test accounts) finds hard-coded prices. Reported results vary: Adopt Me +3.5% over 12 weeks, Driving Empire no uplift because it had already tested manually (Roblox talks). All of this is Roblox Creator Docs 2026-10: live-check the price-optimization and managed-pricing pages before acting.

## When to use
Before opting in, when a game's traffic is large, or when "Plus discounts do not show". Not for: choosing price points (`price-ladder-planner`), regional prices (`regional-pricing-checker`).

## Inputs (max 2)
1. The project folder (default: the current Rojo project). 2. Transactions per 30 days (default: read from the dashboard; ask).

## Procedure
1. Read the rules: `python -I .rbx/claude-kit/tools/kbq.py section pricing rules --max-chars 5000`. Write down the eligibility conditions with dates; live-check them.
2. Eligibility with the owner: transaction volume near the stated minimum, all passes and products included, no promoted pass conflicts, decision between managed pricing (on by default, can be disabled per pass) and price optimization.
3. Scan the code: `python -I .rbx/claude-kit/skillpack/money/price-optimization-readiness/scripts/price_scan.py <project dir>`. It lists strings like "Buy for 99 Robux" and assignments like `price = 99` outside Packages, and reports whether `GetProductInfo` is used anywhere. Exit 1 means hard-coded prices exist.
4. Fix each finding: UI shows the price returned by the platform for that player (live-check the exact API: the vault names `GetProductInfo` with the product or game-pass info type and per-player product-info observers for display); catalogue code keeps ids and names, never prices; any "price" constants that remain must be non-Robux (cooldowns, in-game currency).
5. Re-scan until clean. A clean scan is NOT proof of eligibility; it removes the most common blocker.
6. Prepare the opt-in list: every pass and product with id and name; mark any promoted pass (price band rules differ; live-check).
7. After opt-in, do not change prices by hand during a test unless the docs say so; measure with `shop-conversion-optimizer` and keep a before/after revenue log. Expect "no uplift" as a valid result.
8. Write the owner's checklist (Dynamic Price Check with test accounts, opt-in toggles). You never change prices or opt in.

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `multi_edit` to replace hard-coded prices -> `start_stop_play` -> `execute_luau` (Server) to call the product-info wrapper for one id and print the price -> `get_console_output`. Studio shows the live price only for published ids: UI display with Plus discounts is `untested`.

## Fallback
The scanner and hand edits (headless). Platform eligibility stays `untested`.

## Evidence
`Roblox/roblox-kb/pricing.md` ("Use Price Optimization where eligible"; "Meet Price Optimization prerequisites and script prices correctly"; managed pricing; Adopt Me and Driving Empire results), `Roblox/roblox-kb/monetisation-gamepasses.md` (promotion and pricing tools; promoted passes priced above 49 and below 801 Robux, a docs fact), `Roblox/roblox-kb/_tools/CHECKLIST-monetization.md`, `Roblox/roblox-kb/case-studies-adopt-me.md`. No claim here that optimisation raises revenue for any particular game.

## Output
`design/price-readiness.md`: eligibility table (condition, status, source, live-check date), scanner output before and after, opt-in list, owner checklist.

## Acceptance checks
- [ ] `price_scan.py` exits 0 on the project (quote the last line), or each remaining finding is justified.
- [ ] `python -I .../price_scan.py --selftest` prints "4 checks ok".
- [ ] `GetProductInfo` (or the live-checked equivalent) is used for every displayed Robux price.
- [ ] Eligibility facts are marked live-checked with a date or unverified.
- [ ] No price was changed and no opt-in was made by the agent.

## Pitfalls
Declaring readiness from a clean scan alone. Hard-coded prices in images or GUI text. Forgetting products only sold in a second place. Changing prices manually in the middle of a test. Expecting a guaranteed uplift.

## Related
`price-ladder-planner`, `gamepass-maker`, `devproduct-handler`, `regional-pricing-checker`, `shop-conversion-optimizer`.
