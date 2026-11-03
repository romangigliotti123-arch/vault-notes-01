---
name: ccu-forecaster
description: "Forecast concurrent players around an event, update or promotion from your own same-weekday history: low, base and high scenarios, a decay back to baseline, the server count to prepare, and the date to judge the real effect. Use before a launch, collab, ad push or holiday event."
category: liveops
tags: ccu, concurrent users, forecast, event spike, capacity, servers, baseline, decay, launch, collab
kb: Roblox/roblox-kb/updates-live-ops.md, Roblox/roblox-kb/events-and-seasonal-content.md, Roblox/roblox-kb/analytics-metrics.md, Roblox/roblox-kb/optimization-and-streaming.md, Roblox/roblox-kb/matchmaking-and-teleport.md
related: event-planner, update-cadence-planner, seasonal-calendar-builder, hotfix-playbook, rollback-planner, lag-hunter, metrics-snapshot-logger
---

# ccu-forecaster

A forecast is a range with stated assumptions, not a number. The vault only has reported extremes (+75.5 percent average CCU for one official event, 500 percent plus for another, both presenter-reported) and a warning that collab spikes fade sharply, so this skill builds scenarios from YOUR past events and your same-weekday baseline, then tells you how many servers to be ready for and when to judge the result.

## When to use
Before an update launch, a fixed-time event, a creator collab or an ad burst, when capacity, server stability or staffing depends on peak size. Not for: planning the event itself (`event-planner`) or diagnosing a drop after it (`dau-drop-investigator`).

## Inputs (max 3)
1. History: date and daily peak CCU for at least 28 days (same measure every day). 2. Event date and kind (update, collab, ad push, holiday). 3. Uplift multipliers from your own past events (peak on event day / same-weekday baseline); if none exist, say so and use low 1.2, base 1.5, high 2.5 as labelled placeholders.

## Procedure
1. Gather history in `ccu.csv` (`date,peak_ccu`). Compute past uplifts by hand for any earlier event: event-day peak divided by the mean of the same weekday over the previous four weeks.
2. Run `python -I ~/.claude/claude-kit/skillpack/liveops/ccu-forecaster/scripts/ccu.py --history ccu.csv --event 2026-11-13 --uplift 1.6 --uplift-low 1.25 --uplift-high 2.5 --decay-days 7 --post-baseline 1.05 --players-per-server 30`. It prints the same-weekday baseline, three scenario peaks with the server count each needs, and the expected decay. Stop condition: it refuses with fewer than 3 same-weekday observations.
3. Add the sources of uplift the number ignores: a fixed launch time concentrates arrivals (community arrives together), a pre-launch countdown and sign-ups (reported to double or triple players in one case), influencer videos on the day. Collab spikes are followed by a sharper drop (vault), so keep the decay.
4. Capacity check: servers needed, join and teleport rate limits, DataStore request budget at the peak join rate, and your lowest-staff hours. Use `lag-hunter` and the Performance dashboard on the last big day to see what broke. Have `hotfix-playbook` and `rollback-planner` ready for launch day.
5. Decide thresholds in advance: what CCU makes you pause the ad spend or lower the per-server cap; who watches the first 30 minutes (vault: watch errors and crash rate in the first minutes).
6. After the event, record the actual multiplier next to the forecast in `decisions.md`; judge the update on the baseline seven days later (the script prints the date), not on the spike (vault: read the post-spike baseline).
7. Update your own uplift table so the next forecast is better.

## Studio MCP path
Not needed for the forecast. For the capacity step: `execute_luau` (Server) to read `Players.MaxPlayers` and your cap constants; `get_console_output` after a rehearsal.

## Fallback
Python 3 and a CSV; Creator Hub charts supply the history by hand.

## Evidence
`Roblox/roblox-kb/updates-live-ops.md`: live events draw dense player counts; countdowns reported to double or triple players (reported); events should be fixed-time; illustrative CCU numbers are hypothetical there. `events-and-seasonal-content.md`: expect a sharp CCU drop after collab spikes; Lunar Overture +75.5 percent average CCU (official presenter figure). `analytics-metrics.md`: compare with the same weekday; read the post-spike baseline about a week later; seasonality overlays.

## Output
```
CCU FORECAST <event> <date>
baseline (same weekday, 4 wks) N
low x.xx -> peak -> servers | base ... | high ...
decay (base): day0 ... day7
Capacity risks + thresholds + watch owner
Judge on <date +7> vs baseline
```

## Acceptance checks
- [ ] `ccu.py --selftest` prints "selftest ok (4 checks)".
- [ ] Baseline uses the same weekday over several weeks.
- [ ] Three scenarios, each with a server count; multipliers labelled own-history or placeholder.
- [ ] A named person watches the first 30 minutes and thresholds are written down.
- [ ] A seven-day post-event read is scheduled.

## Pitfalls
One forecast number. Using a front-page game's spike as your multiplier. Forgetting that the baseline moves (trend). Capacity planned for the average, not the peak join rate. Judging success at the spike.

## Related
`event-planner`, `update-cadence-planner`, `hotfix-playbook`, `rollback-planner`, `lag-hunter`.
