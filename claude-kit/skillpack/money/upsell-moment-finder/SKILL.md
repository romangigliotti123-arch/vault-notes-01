---
name: upsell-moment-finder
description: "Find the moments of need where an offer actually follows a purchase, by ranking logged events (out of currency, inventory full, death, blocked) by how often the same player buys within a window, then pick offers that solve each need. Use when you have event logs and want data-driven offer moments; writing the show/hide rules is offer-timing-planner."
category: money
tags: upsell, moment of need, events, analytics, conversion, out of currency, inventory full, contextual offer, ranking
kb: Roblox/roblox-kb/monetisation-other.md, Roblox/roblox-kb/analytics-metrics.md, Roblox/roblox-kb/ab-testing-and-experiments.md, Roblox/roblox-kb/player-psychology-and-game-feel.md, Roblox/roblox-kb/first-session-onboarding.md
related: offer-timing-planner, shop-conversion-optimizer, payer-segment-planner, starter-pack-designer, devproduct-handler
---

# upsell-moment-finder

One job: replace guesses about "when to show the offer" with a ranked list from your own logs. The vault's rule is to offer the right item at the moment of need (blocked, dying, waiting; OneTime bundles when a player runs out of currency), and says contextual upsells are a platform-supported direction in 2025-2026. `scripts/moments.py` counts, per event type, how many occurrences were followed by a purchase from the same player within a window. It reports correlation: a high rate does not prove an offer there would cause more sales.

## When to use
You log gameplay events plus purchases and want to know which friction points convert. Not for: the rules that stop spam (`offer-timing-planner`), funnel leaks (`shop-conversion-optimizer`). Without logs, start by adding events (below) and come back.

## Inputs (max 2)
1. `events.csv` with `userId,t,event` (t in seconds), including a `purchase` event (default: export from the Analytics system's custom events or your own log; hashed ids only). 2. Window and minimum count (defaults 60 s and 30).

## Procedure
1. Read the rules: `python -I ~/.claude/claude-kit/tools/kbq.py section monetisation-other rules --max-chars 4000` ("Don't push purchases with pop-ups; trigger offers at moments of need").
2. If events are missing, add them with the kit Analytics system: `out_of_currency`, `inventory_full`, `death`, `blocked_by_gate`, `wait_timer`, `shop_opened`, plus `purchase` from the receipt handler. Keep names stable. Stop here until a few days of data exist.
3. Run `python -I ~/.claude/claude-kit/skillpack/money/upsell-moment-finder/scripts/moments.py events.csv --window 60 --min-count 30`. Rows marked LOW SAMPLE are not rankable.
4. For the top moments, name the need and the offer that solves it (out of currency: a currency pack as a OneTime bundle; inventory full: storage pass; death streak: a convenience, never pvp power; waiting: nothing paid that removes appointment timers, see the vault rule).
5. Vary the window (30, 60, 300 s) and see if the ranking holds; unstable rankings mean noise.
6. Segment: repeat for new versus returning players (`payer-segment-planner`); a moment that works only for veterans should not appear to tourists.
7. Take the top one or two moments to `offer-timing-planner` for the gate and to an A/B test with a decision rule (`ab-testing-and-experiments`). Do not move the shop based on this ranking alone.
8. Check fairness (`pay-to-win-checker`) for every offer proposed.

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `multi_edit` to add event logging -> `start_stop_play` -> `get_console_output` to confirm each event fires once per occurrence. Logs from real players need a published place: `untested`.

## Fallback
The script on any exported CSV (headless). Causality stays a hypothesis until a test runs.

## Evidence
`Roblox/roblox-kb/monetisation-other.md` (moments of need; OneTime bundles for running out of currency; Jailbreak's garage-UI flow reported at about 40% of purchases), `Roblox/roblox-kb/analytics-metrics.md` (event design and breakdowns), `Roblox/roblox-kb/ab-testing-and-experiments.md` (decide with a test), `Roblox/roblox-kb/player-psychology-and-game-feel.md`, `Roblox/roblox-kb/first-session-onboarding.md`. The 60 s window and 30-event minimum are defaults.

## Output
`design/upsell-moments.md`: the ranked table with sample sizes, the need and offer per top moment, window sensitivity, test plan.

## Acceptance checks
- [ ] `moments.py` output is quoted with window and minimum count.
- [ ] `python -I .../moments.py --selftest` prints "4 checks ok".
- [ ] No LOW SAMPLE row is recommended.
- [ ] Each recommended offer solves the named need and passes `pay-to-win-checker`.
- [ ] The report states that the ranking is correlation and names the A/B test to confirm.

## Pitfalls
Reading correlation as causation. Tiny samples. Logging events twice. A purchase event that fires on prompt open instead of confirmed receipt. Building offers that exploit frustration they themselves cause.

## Related
`offer-timing-planner`, `shop-conversion-optimizer`, `payer-segment-planner`, `starter-pack-designer`, `devproduct-handler`.
