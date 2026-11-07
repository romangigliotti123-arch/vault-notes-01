---
name: stat-sheet-explainer
description: "Explain the Creator Hub analytics pages (overview benchmark scorecard, acquisition and home recommendations, engagement, retention, monetization, audience, performance and stability) and what to do about each number, with data latency and traps. Use when someone is staring at the dashboard and does not know what is important."
category: liveops
tags: creator hub, analytics, dashboard, overview, acquisition, home recommendations, retention, monetization, performance, explain, latency
kb: Roblox/roblox-kb/analytics-metrics.md, Roblox/roblox-kb/discovery-algorithm.md, Roblox/roblox-kb/_tools/BENCHMARKS.md, Roblox/roblox-kb/retention-d1-d7.md, Roblox/roblox-kb/optimization-and-streaming.md
related: kpi-dashboard-planner, retention-diagnoser, metrics-snapshot-logger, dau-drop-investigator, funnel-analyzer, rbx-analytics, rbx-metrics
---

# stat-sheet-explainer

A translator between the dashboard and a decision. Page names in Creator Hub change; this skill is built from the vault's reading rules, so each explanation names the page by what it measures and says to live-check the exact label. The kit skill `rbx-analytics` reviews a whole dashboard; this answers "what is this number and what do I do".

## When to use
A new creator or teammate learning the dashboard, a number that surprises you, or a weekly review where nobody knows which page matters. Not for: choosing KPIs (`kpi-dashboard-planner`) or diagnosing one metric (`retention-diagnoser`).

## Inputs (max 2)
1. The page or metric in question (or a pasted screenshot's numbers). 2. Game stage and DAU (the benchmark scorecard needs 100+ DAU).

## Procedure
1. Identify the page and the question it answers, using the table below. Check the date range and whether the data has settled (latency per page).
2. Give the meaning in one line, the benchmark if any (with its flag), the common misreading, and the next action. Never invent a threshold; point to `BENCHMARKS.md`.
3. Always add the slice advice: break the number down (platform, device, source, new vs returning) before concluding.
4. End with one action and the skill that carries it out.

| page (live-check names) | what it tells you | trap | next skill |
|---|---|---|---|
| Overview benchmark scorecard (100+ DAU) | your six core stats against similar experiences, 50th-90th percentile spread | a mixed picture early is normal; do not min-max every stat | `retention-diagnoser` |
| Acquisition: Home Recommendations | whether the algorithm is serving you; play-through rate, play days, playtime first | stop ads once organic recommendations appear; a kill criterion if none by about day 5-8 (indie) | `ctr-ab-test-planner` |
| Acquisition: traffic sources | where players come from | a retention drop may be a source-mix change | `cohort-reader` |
| Engagement: concurrent, session time, minutes per active player | pacing and love (minutes per active player is the best proxy, Roblox guidance) | averages hide outliers; AFK inflates time | `session-length-analyzer` |
| Retention (by first play date) | D1 / D7 / D30 per new-player cohort | recent dates are empty; the change shows in that day's cohort | `cohort-reader` |
| Funnels and custom events | where players drop in a flow you logged | steps appear only on days reached; use a 90-day lookback | `funnel-analyzer` |
| Monetization | revenue, conversion, ARPPU, ARPDAU | omits refunds; lags about 2 days; exclude your own purchases | `shop-conversion-optimizer` |
| Audience and demographics | age, country, platform mix | pricing and difficulty must fit who actually plays | `payer-segment-planner` |
| Performance and stability | FPS, memory, crash rate by device and place version | data kept about 28 days; export it; low-end percentiles matter | `lag-hunter` |
| Thumbnails and ratings | click-through, like ratio | judge ratings on a recent window after a fix | `thumbnail-maker` |

5. Latency rules to repeat: most signals about 24 hours, monetisation KPIs about 2 days, ad metrics 48 hours, event charts about 24 hours; day-7 retention is meaningless before a week.
6. For the API: `python -I .rbx/claude-kit/tools/analytics-pull.py --universe <id> --metric ForwardD1Retention --dry-run` shows the request shape for a metric (executed check, no key needed); metric names and breakdowns live on the Supported-metrics page of the analytics docs.

## Studio MCP path
Not applicable (dashboards live in Creator Hub). For logging gaps, `script_grep` for `AnalyticsService` calls and use the kit `Analytics` system.

## Fallback
Plain explanation from pasted numbers. Where the live page layout differs from the table, trust the page and say so.

## Evidence
`Roblox/roblox-kb/analytics-metrics.md`: benchmark scorecard needs 100+ DAU and you fix the weakest metric first; Home Recommendation signals (play-through rate, play days, playtime first); data latency; retention as first-play-date cohorts; minutes per active player as the engagement signal; performance data kept 28 days, thumbnail metrics 30; monetization KPIs omit refunds. `discovery-algorithm.md` and `_tools/BENCHMARKS.md` (flagged ranges). Page labels may have changed (live-check).

## Output
A short answer per question: meaning, benchmark with flag, trap, next action and skill.

## Acceptance checks
- [ ] Every explanation names its latency or date-range caveat.
- [ ] Any benchmark quoted carries its source flag from `BENCHMARKS.md`, or is omitted.
- [ ] Each answer ends in one action and a named skill.
- [ ] `analytics-pull.py --dry-run` printed a POST line for the metric discussed (shape only).
- [ ] No claim about a page layout is stated as certain without "live-check".

## Pitfalls
Quoting an indie rule of thumb as a law. Explaining a number with no breakdown. Treating revenue lags as a drop. Reading a thumbnail click-through without impressions. Over-reading a day-1 snapshot of paid traffic.

## Related
`kpi-dashboard-planner`, `retention-diagnoser`, `metrics-snapshot-logger`, `dau-drop-investigator`, `funnel-analyzer`.
