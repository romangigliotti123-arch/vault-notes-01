---
name: post-launch-monitor
description: "Plan the first 72 hours after launch: which metrics to read at which hours, healthy and alarm values with a stated basis, who acts, and the rollback trigger. monitor_plan.py rejects plans with invented thresholds, missing owners or no rollback. Use before launch and for major updates."
category: publish
tags: launch, monitoring, first 72 hours, metrics, alarms, rollback, analytics, error rate, retention, live ops
kb: Roblox/roblox-kb/updates-live-ops.md, Roblox/roblox-kb/analytics-metrics.md, Roblox/roblox-kb/retention-d1-d7.md, Roblox/roblox-kb/_tools/CHECKLIST-launch.md
related: publish-readiness-gate, version-history-keeper, place-backup-planner, retention-diagnoser, privacy-data-checker, regional-availability-checker
---

# post-launch-monitor

One job: decide in advance what "going badly" looks like, so nobody argues about it at 3 a.m. The plan lists metrics with a source, a healthy value, an alarm value, the BASIS for both (a playtest run, a prior update, a named benchmark: never a number made up), an action and an owner, plus checkpoints and a rollback trigger. `scripts/monitor_plan.py` rejects incomplete plans and prints the schedule with real clock times. Which dashboards exist and what they are called is `live-check`: the Creator Hub changes; the Creator Docs analytics pages are opened first.

## When to use
The day before launch and before major updates. Not for: diagnosing retention after launch (`retention-diagnoser`), performance deep dives (`lag-hunter`), planning the update cadence (`update-cadence-planner`).

## Inputs (max 2)
1. Launch time (with time zone). 2. Who is on watch for each window (default: the owner, with sleep gaps named).

## Procedure
1. Open the live analytics pages (Evidence) and list which metrics exist today (errors/crashes, data save failures, purchases and receipts, retention/playtime, concurrent users, by-country if shown). Record the date.
2. `python -I .rbx/claude-kit/skillpack/publish/post-launch-monitor/scripts/monitor_plan.py --template > release/monitor.json` and fill it. Healthy and alarm values come from the pre-launch playtest and earlier updates (`basis` says which); where no basis exists write "unknown, baseline at hour 1" and set the alarm to "any rise above the hour-1 baseline by a stated factor you choose" rather than a fake benchmark.
3. Checkpoints: at least one in the first two hours and one at 72 hours (defaults 1, 6, 24, 48, 72). Put them in calendars with the owner's time zone.
4. Rollback block: trigger (specific metric + condition), how (`version-history-keeper` restore, publish, restart servers), and the named restore point from the release log.
5. Include a privacy line: check the inbox for right-to-be-forgotten messages daily (`privacy-data-checker`) and a by-country look if a region restriction could apply (`regional-availability-checker`).
6. Run `python -I .../monitor_plan.py release/monitor.json`. Exit 1 lists what is missing; the OK line plus the schedule is the deliverable.
7. During the window, append observations to `release/monitor-log.md` (time, metric, value, decision). After 72 hours write the summary and the changes to the plan for next time.

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `execute_luau` (Server) in the live place only to print `game.PlaceVersion` and the time -> `get_console_output`. Metrics are read in Creator Hub / the Analytics system; Studio cannot read live dashboards. If the kit `Analytics` system is installed, its event names go in `source`.

## Fallback
The plan is JSON and a log file. Real values at hours 1, 6 and so on are `untested` until the window runs.

## Evidence
Official (live-check): `Roblox/docs/Videos/2026-10-28 - Docs cloud guides analytics.md`, `... Docs cloud guides analytics metrics.md`, `... Docs cloud guides alerts.md`, `... Docs cloud guides error-reporting.md` (what can be monitored and alerted), `... Docs production publishing RTBF-and-creators.md` (daily RTBF messages), `... Docs projects version-history.md` (restore does not publish). Pack: `Roblox/roblox-kb/updates-live-ops.md`, `Roblox/roblox-kb/analytics-metrics.md`, `Roblox/roblox-kb/retention-d1-d7.md`; any benchmark taken from indie sources is labelled indie.

## Output
`release/monitor.json` (validated), the printed schedule, and `release/monitor-log.md` during the window.

## Acceptance checks
- [ ] `monitor_plan.py release/monitor.json` exits 0 (quote the OK line).
- [ ] Every threshold has a basis; none is typed from memory.
- [ ] The rollback block names a restore point that exists.
- [ ] Owners are named per window, including who sleeps when.
- [ ] `monitor_plan.py --selftest` prints `selftest ok`.

## Pitfalls
Alarms with no action attached. Reading only concurrent users and missing a data-save failure. Rolling back without checking that the restore was published and servers restarted. Changing three things at once during the window.

## Related
`publish-readiness-gate`, `version-history-keeper`, `place-backup-planner`, `retention-diagnoser`, `privacy-data-checker`.
