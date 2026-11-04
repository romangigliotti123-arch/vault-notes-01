---
name: metrics-snapshot-logger
description: "Log the day's headline numbers (DAU, D1, revenue, conversion, custom KPIs) to a plain CSV from the Open Cloud analytics pull or by hand, then compare each with the same weekday last week. Use to start the habit before you need the trend, and weekly in live ops."
category: liveops
tags: metrics, snapshot, daily log, trend, csv, analytics api, baseline, weekday, kpi, history
kb: Roblox/roblox-kb/analytics-metrics.md, Roblox/roblox-kb/updates-live-ops.md, Roblox/roblox-kb/_tools/BENCHMARKS.md
related: kpi-dashboard-planner, dau-drop-investigator, cohort-reader, retention-diagnoser, economy-health-monitor, rbx-analytics, rbx-weekly
---

# metrics-snapshot-logger

Creator Hub dashboard charts show a limited past window, performance and stability data is kept 28 days, and thumbnail metrics 30 days (vault), so the history you will want in six months must be copied somewhere you own. This skill keeps one small CSV of numbers, one row per metric per day, and shows the change against the same weekday last week. Dashboards and charts from that file: `dataviz`.

## When to use
Starting live ops, before any update you will want to judge, weekly in `rbx-weekly`. Not for: deciding which KPIs matter (`kpi-dashboard-planner`) or interpreting a drop (`dau-drop-investigator`).

## Inputs (max 3)
1. The metrics to log (default: the KPIs from `kpi-dashboard-planner`; else DailyActiveUsers, ForwardD1Retention, DailyRevenue, PayingUsersCVR). 2. Source: `analytics-pull.py` (needs an Open Cloud key) or typed values. 3. Log path (default: `Games/<slug>/metrics-log.csv`).

## Procedure
1. Choose the date to log: a day whose numbers have settled (most signals update within 24 hours, monetisation KPIs lag about 2 days, ad metrics 48 hours). Log yesterday for engagement, two days ago for revenue. Never log a partial day.
2. Pull (optional): `python -I ~/.claude/claude-kit/tools/analytics-pull.py --universe <id> --metric DailyActiveUsers --metric ForwardD1Retention --days 14 --json > pull.json`. The key is read from the environment or `~/.config/roblox/analytics-api-key` and never printed; keep it outside any vault or `Games` folder. Check the request shape first without a key with `--dry-run`. The Analytics Query API is beta (live-check metric names).
3. Write the numbers: `python -I ~/.claude/claude-kit/skillpack/liveops/metrics-snapshot-logger/scripts/snapshot.py --log metrics-log.csv --from-pull pull.json` (uses the last point of each unbroken series) or `--date 2026-11-02 --set DailyActiveUsers=5400 --set ForwardD1Retention=11.8 --note "update 12 live"`. Re-running a day replaces that metric for that day.
4. Read the comparison it prints: each metric against the same weekday last week, flagged CHECK at 10 percent or more (default). A flag is a question for `dau-drop-investigator` or `cohort-reader`, not a conclusion.
5. Put releases in the notes (`--note`), so spikes have a cause on the same row.
6. Do not log weekly or monthly uniques by adding days; log the period value from the dashboard if you need it (distinct users are not additive).
7. Weekly: run `--report`, paste the CHECK lines into the weekly note, and decide one action.
8. Back the CSV up with the project; it holds only your own game's numbers. If the numbers are private, keep it out of public repositories.

## Studio MCP path
Not needed. In-game counters, if you keep them, come from your server code, not Studio.

## Fallback
Typed values and the script; no key, no network. For a chart from the CSV use the `dataviz` skill.

## Evidence
`Roblox/roblox-kb/analytics-metrics.md`: compare each day with the same weekday last week; data latency per signal; export performance and thumbnail data before it expires (28 and 30 days); dashboard charts show only the past 30 days; do not sum daily uniques into weekly or monthly totals; ignore unreliable (not statistically significant or projected) data points; read the post-spike baseline. `updates-live-ops.md`: check key metrics after every update against the pre-update baseline. Kit `tools/analytics-pull.py` header for the key handling and the beta caveat.

## Output
`metrics-log.csv` (`date,metric,value,note`) plus the printed week-over-week table.

## Acceptance checks
- [ ] `snapshot.py --selftest` prints "selftest ok (5 checks)".
- [ ] `analytics-pull.py --dry-run` printed the POST line for each metric (shape check; no key was needed or used).
- [ ] No partial day was logged; notes carry the release context.
- [ ] The CSV contains numbers only; no key or secret anywhere near it.
- [ ] A CHECK flag produced a named follow-up, not a conclusion.

## Pitfalls
Logging before data settles. Mixing daily peak and daily mean in one series. Adding days to get weeks. Committing the API key file or keeping it in the vault. Treating the log as a substitute for qualitative reads.

## Related
`kpi-dashboard-planner`, `dau-drop-investigator`, `cohort-reader`, `retention-diagnoser`, `economy-health-monitor`.
