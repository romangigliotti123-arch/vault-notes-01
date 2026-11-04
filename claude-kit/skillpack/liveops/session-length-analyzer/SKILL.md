---
name: session-length-analyzer
description: "Analyse the session length distribution (P10/P50/P90, buckets, short-session share) and find stop points where sessions cluster, then add a goal 2-3 minutes beyond each. Use when average session time is low, when stage targets are missed, or after a change meant to lengthen sessions."
category: liveops
tags: session length, playtime, percentiles, stop points, pacing, engagement, distribution, analytics
kb: Roblox/roblox-kb/analytics-metrics.md, Roblox/roblox-kb/retention-d1-d7.md, Roblox/roblox-kb/core-loops-and-game-design.md, Roblox/roblox-kb/player-psychology-and-game-feel.md, Roblox/roblox-kb/_tools/BENCHMARKS.md
related: retention-diagnoser, churn-reason-finder, funnel-analyzer, core-loop-designer, first-minute-designer, metrics-snapshot-logger, rbx-metrics
---

# session-length-analyzer

Average session time hides the shape. Vault: use percentiles (P10, P50, P90), size content with average session time, and compare before and after a feature. This skill reads the shape, flags buckets where sessions pile up (candidate stop points), and turns each into a design change. Where players leave in a funnel is `churn-reason-finder`.

## When to use
Low session minutes, a retention fix aimed at pacing, or a new mode whose sessions look odd. Not for: D1/D7 diagnosis (`retention-diagnoser`) or ranking exit stages with return data (`churn-reason-finder`).

## Inputs (max 3)
1. Session lengths in minutes, one per session (server join/leave times; at least 50, ideally 500 or more). 2. Platform split if you have it. 3. The stage target (default: judge by your own history; vault gives 10+ minutes during ad-driven traffic and 20+ once on the algorithm as indie stage targets).

## Procedure
1. Log session start and end on the server (join time at PlayerAdded, leave at PlayerRemoving; handle shutdown) as a custom event or a counter; do not count time spent AFK or in a menu if you can tell.
2. Export lengths to `minutes.txt` (one per line) or a CSV with a `session_minutes` column.
3. Run `python -I ~/.claude/claude-kit/skillpack/liveops/session-length-analyzer/scripts/session.py --minutes minutes.txt`. It prints mean, P10, P50, P90, the share under 2 minutes, a bucket histogram and stop-point candidates (a bucket holding at least 8 percent of sessions and at least 1.8 times its neighbours, a default of this skill).
4. Read the shape: a big under-2-minute share is a first-impression or load problem (`first-minute-designer`, packaging); a spike at 5-8 minutes is a natural end (a round, a quest, a timer); a long tail is your engaged core and worth protecting.
5. Tie each candidate bucket to a game event: what happens at that elapsed time (match end, shop close, tutorial end, energy empty)? Check with the server log or a playtest.
6. Add a goal 2-3 minutes out at that point (vault stop-point rule): a visible next reward, a queued next match, a progress bar that is nearly full. Do not use dark patterns (fake urgency, hidden odds).
7. Re-run after two weeks on the same traffic mix. Compare P50 and the stop bucket share, not only the mean; a longer mean from a few marathon sessions is not a win.

## Studio MCP path
`script_grep` for PlayerAdded/PlayerRemoving handlers and existing analytics -> `multi_edit` to add the session log -> `start_stop_play` and `execute_luau` (Server) to simulate join/leave -> `get_console_output`.

## Fallback
Paste lengths from any source; the script is Python 3. Creator Hub reports an average only; percentiles need your own log.

## Evidence
`Roblox/roblox-kb/analytics-metrics.md`: use percentiles (P10/P50/P90) not averages; judge session length in context (social games 10+ minutes); stage-gated playtime targets; minutes per active player as the engagement signal (Roblox guidance). `_tools/BENCHMARKS.md` for the flagged average-session sample. `retention-d1-d7.md` for why the first sessions matter.

## Output
```
SESSIONS n=...  mean | P10 | P50 | P90 | under 2 min %
histogram, stop-point candidates
Per candidate: what happens there -> change -> expected effect -> re-check date
```

## Acceptance checks
- [ ] `session.py --selftest` prints "selftest ok (5 checks)".
- [ ] At least 50 sessions; the real run did not print the ERROR line.
- [ ] Percentiles reported, not only the mean.
- [ ] Every stop candidate is tied to a named game event.
- [ ] The change adds a goal, not a pressure tactic.

## Pitfalls
Counting AFK time. Comparing a weekend to a weekday distribution. Celebrating a longer mean caused by a few outliers. Lengthening sessions with grind while D1 falls. Treating a natural round end as a problem.

## Related
`retention-diagnoser`, `churn-reason-finder`, `funnel-analyzer`, `core-loop-designer`, `first-minute-designer`.
