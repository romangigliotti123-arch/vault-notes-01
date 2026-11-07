---
name: shop-conversion-optimizer
description: "Find why a shop does not convert by measuring the funnel from sessions to purchase, locating the biggest drop, and choosing one fix to A/B test (visibility, item order, first purchase, price, trust). Use when shop views or purchases are low; finding offer moments from event logs is upsell-moment-finder."
category: money
tags: shop, conversion, funnel, ab test, item order, visibility, first purchase, payer conversion, arppu
kb: Roblox/roblox-kb/monetisation-other.md, Roblox/roblox-kb/ab-testing-and-experiments.md, Roblox/roblox-kb/analytics-metrics.md, Roblox/roblox-kb/pricing.md, Roblox/roblox-kb/ui-ux-design.md
related: upsell-moment-finder, offer-timing-planner, starter-pack-designer, price-ladder-planner, payer-segment-planner, retention-diagnoser, ctr-ab-test-planner
---

# shop-conversion-optimizer

One job: turn "the shop doesn't sell" into one measured leak and one test. The vault's levers: shop visibility, starter packs and new-purchaser discounts raise conversion; diverse seasonal items and refills raise ARPPU; the first purchase is pivotal. The tool `scripts/funnel.py` locates the biggest relative drop in an ordered funnel; judgement chooses the fix; `ab-testing-and-experiments` decides if it worked.

## When to use
Low shop opens, low prompts, low purchases. Not for: choosing offer moments from event logs (`upsell-moment-finder`), spend segmentation (`payer-segment-planner`), the price ladder (`price-ladder-planner`).

## Inputs (max 2)
1. Funnel counts for one window, as unique players if possible: sessions, shop opened, item viewed, prompt shown, purchased (default: pull them from the Analytics system's funnel events or the dashboard). 2. Platform split (default: all; mobile often differs).

## Procedure
1. Read the rules: `python -I .rbx/claude-kit/tools/kbq.py section monetisation-other rules --max-chars 4000` (shop design, first purchase, conversion) and `section ab-testing-and-experiments rules --max-chars 2500`.
2. Instrument if needed: the Analytics system's `Funnel` and `Economy` methods; steps need stable names and counts per unique player.
3. Run `python -I .rbx/claude-kit/skillpack/money/shop-conversion-optimizer/scripts/funnel.py --steps sessions=<n>,shop_opened=<n>,item_viewed=<n>,prompt_shown=<n>,purchased=<n>`. It prints conversion from the previous step and from the first, names the biggest relative drop, and exits 1 if counts rise (a logging bug: fix events before reading anything).
4. Map the leak to a fix class: sessions to shop open (visibility, button size and placement on mobile, an offer at a need moment: `offer-timing-planner`); opened to viewed (item order, clutter, a featured item); viewed to prompt (price, value display, no first item they can afford); prompt to purchase (price shock, unclear grant, platform friction, regional price: `regional-pricing-checker`).
5. Choose ONE change and a hypothesis ("moving the starter pack to slot one raises view-to-prompt by X"). Check it is not pay-to-win (`pay-to-win-checker`) and not a dark pattern.
6. Test it: split players, one variable, a decision rule written first (`ctr-ab-test-planner` pattern: sample size, duration, minimum effect). Read the result with the funnel again. Payer conversion is a sensitive metric: do not call a win from one day.
7. Keep a log of tests (change, hypothesis, result) in `design/shop-tests.md`.

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `multi_edit` for UI/ordering changes and analytics events -> `start_stop_play` -> `get_console_output` to confirm events fire once. Funnel numbers come from the dashboard or Open Cloud analytics, not Studio; a live A/B needs a published place: `untested`.

## Fallback
Funnel script on numbers the owner reads from the Creator Dashboard (headless). Experiments stay `untested` until run.

## Evidence
`Roblox/roblox-kb/monetisation-other.md` (shop design; first purchase; conversion and ARPPU levers; "track payer conversion, ARPPU and revenue breakdowns"; one creator's payer conversion of 0.82%, self-reported), `Roblox/roblox-kb/ab-testing-and-experiments.md`, `Roblox/roblox-kb/analytics-metrics.md`, `Roblox/roblox-kb/ui-ux-design.md`, `Roblox/roblox-kb/pricing.md` (test prices live). No universal conversion target exists in the vault: compare with similar games.

## Output
`design/shop-conversion.md`: funnel table, the leak, the chosen test with its decision rule, and later the result.

## Acceptance checks
- [ ] `funnel.py` output is quoted with the window and platform.
- [ ] `python -I .../funnel.py --selftest` prints "4 checks ok".
- [ ] The test changes exactly one variable and states a decision rule before running.
- [ ] The change passes `pay-to-win-checker` (0 blocks).
- [ ] Events fire once per player action (confirmed in the console).

## Pitfalls
Fixing price when the leak is visibility. Changing several things at once. Reading noise from a few payers. Counting prompt clicks as purchases. Comparing mobile and PC as one population.

## Related
`upsell-moment-finder`, `offer-timing-planner`, `starter-pack-designer`, `price-ladder-planner`, `payer-segment-planner`.
