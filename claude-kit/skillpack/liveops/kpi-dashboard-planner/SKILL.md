---
name: kpi-dashboard-planner
description: "Choose the few metrics that matter for a Roblox game's current stage, give each a target, an owner action and a data source (Creator Hub page, Analytics Query API metric, or custom event), and lay out one summary page. Use at launch, after a pivot, or when the dashboard has twenty charts and no decisions."
category: liveops
tags: kpi, dashboard, metrics, targets, scorecard, retention, revenue, analytics api, stage, benchmarks
kb: Roblox/roblox-kb/analytics-metrics.md, Roblox/roblox-kb/_tools/BENCHMARKS.md, Roblox/roblox-kb/retention-d1-d7.md, Roblox/roblox-kb/discovery-algorithm.md, Roblox/roblox-kb/monetisation-other.md
related: retention-diagnoser, metrics-snapshot-logger, stat-sheet-explainer, funnel-analyzer, economy-health-monitor, roblox-metrics-benchmarks, roblox-analytics-review, game-dev-weekly
---

# kpi-dashboard-planner

A dashboard is a decision list. The vault says not to min-max every metric but to monitor the handful that map to actions, judge against your own history, and fix the weakest first. This skill picks that handful for the game's stage and says where each number comes from. It plans; it does not build charts (for a rendered dashboard use the `dataviz` skill on the numbers from `metrics-snapshot-logger`).

## When to use
Launch prep, a pivot, a new teammate asking "what do we watch", or a dashboard nobody acts on. Not for: reading one bad metric (`retention-diagnoser`), or learning what a Creator Hub page means (`stat-sheet-explainer`).

## Inputs (max 3)
1. Stage: prototype, beta/ad-driven, on the algorithm, or mature (default: beta). 2. Monetisation in place: none, passes, products, ads (default: passes). 3. Does an Open Cloud analytics key exist (default: no; the plan then lists Creator Hub pages).

## Procedure
1. Fix the question for the stage. Prototype: skip metrics, rely on qualitative playtests (vault). Beta/ads: D1, play-through rate, average session, first-session funnel, like ratio. On the algorithm: D1, D7, session minutes per active player, home-recommendation signals, payer conversion. Mature: DAU/MAU stickiness, ARPDAU/ARPPU, economy drift, update impact.
2. Choose at most 6 KPIs, each as: name, definition, source, cadence (daily or weekly), target, and the action it triggers. Use the Creator Hub benchmark scorecard (similar experiences) for targets when available; otherwise take ranges from `BENCHMARKS.md` with their flags (indie targets are labelled indie) and write "own history" targets after four weeks of data.
3. Map each KPI to a source. Analytics Query API metrics known from the docs: DailyActiveUsers, DailyRevenue, ForwardD1Retention, PayingUsersCVR (beta, live-check the Supported-metrics page). Check the query shape without a key: `python -I ~/.claude/claude-kit/tools/analytics-pull.py --universe 1 --metric ForwardD1Retention --dry-run`. Anything not in the API is read by hand from Creator Hub or logged as a custom event with the kit `Analytics` system.
4. Note data latency per KPI (most signals about 24 h, monetisation KPIs about 2 days, ad metrics 48 h, event charts about 24 h) so nobody reacts to an incomplete day.
5. Add two guard metrics (crash rate, error count) and one economy line if the game has currency (`economy-health-monitor`).
6. Lay out one page: top row the 3 outcome KPIs with a 7-day trend and the same-weekday-last-week change; below, the funnel and the economy line; a side note listing the last 3 updates so spikes have context. Set alerts only for stability metrics (crash rate, OOM exits) and require persistence (consecutive occurrences) so alerts fire on real spikes.
7. Write the review ritual: who looks, when (weekly via `game-dev-weekly`), and the rule "one KPI below target gets one change tested".
8. Log the numbers daily or weekly with `metrics-snapshot-logger` so the trends exist.

## Studio MCP path
Not needed. Optional: `script_grep` for `AnalyticsService` calls to see which custom KPIs are already logged.

## Fallback
All of it works from Creator Hub pages and a spreadsheet; the API line is optional. Dry-run only checks the request shape, not access.

## Evidence
`Roblox/roblox-kb/analytics-metrics.md`: retention is the core health metric; do not over-optimise every metric; compare against same-genre benchmarks and fix the weakest first; self-referenced, genre-realistic targets; use percentiles not averages; data latency and thresholds; custom dashboards with calculated metrics; alerts with consecutive occurrences; stage-gated playtime targets (10+ min ad-driven, 20+ once on the algorithm, indie). `_tools/BENCHMARKS.md` for flagged ranges.

## Output
`liveops/kpis.md`: table (KPI, definition, source, cadence, target + flag, trigger action), latency notes, page layout, alert list, review ritual.

## Acceptance checks
- [ ] No more than 6 KPIs; each has a source, a target with its flag, and an action.
- [ ] The dry-run command printed a POST line for the chosen API metric (executed, shows shape only).
- [ ] Stability alerts exist and require consecutive occurrences.
- [ ] Targets are labelled indie, official or own-history; none is presented as a law.
- [ ] Latency per KPI is noted so partial days are not read.

## Pitfalls
Vanity totals (visits). Averages where percentiles matter. Summing daily uniques into weekly totals. Judging against front-page games. Targets without an action. Reading monetisation numbers that omit refunds or include your own purchases.

## Related
`retention-diagnoser`, `metrics-snapshot-logger`, `stat-sheet-explainer`, `funnel-analyzer`, `economy-health-monitor`.
