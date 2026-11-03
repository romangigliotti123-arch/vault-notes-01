---
name: churn-reason-finder
description: "Find why players leave: rank the stages where sessions end and players do not return, by players lost, then pair the top stage with feedback and a playtest to name the cause. Use when D1 or D7 is low and the funnel does not show one obvious step."
category: liveops
tags: churn, why players leave, last stage, stop points, retention, session end, feedback, drop-off, analytics
kb: Roblox/roblox-kb/retention-d1-d7.md, Roblox/roblox-kb/analytics-metrics.md, Roblox/roblox-kb/first-session-onboarding.md, Roblox/roblox-kb/playtesting-and-feedback.md, Roblox/roblox-kb/player-psychology-and-game-feel.md
related: retention-diagnoser, funnel-analyzer, session-length-analyzer, feedback-synthesizer, cohort-reader, game-dev-playtest, roblox-analytics-review
---

# churn-reason-finder

`retention-diagnoser` names the window, `funnel-analyzer` finds a step in a scripted path. This skill is for open games: record where each session ended (last stage, area or activity) and whether the player came back, then rank by players lost. Telemetry shows how many and where; a small qualitative sample shows why (vault).

## When to use
D1 or D7 is low, the funnel looks flat, and players could be leaving at many places. Not for: a sudden drop in total players (`dau-drop-investigator`), or session length shape alone (`session-length-analyzer`).

## Inputs (max 3)
1. Per-session records: user id (hash it), session minutes, last stage or area, returned next day (1/0), optional platform. 2. How `last_stage` is defined (default: the last funnel/progression step or zone the server saw). 3. Feedback lines, if any.

## Procedure
1. Define `last_stage` in code, not in analysis: the server remembers the current stage (kit `Analytics:Progression`/`Funnel` already records it) and logs it as a low-cardinality custom field when the player leaves. Never log user names or free text.
2. Export sessions for new players (first session) separately from returning players; their reasons differ (onboarding vs content).
3. Run `python -I ~/.claude/claude-kit/skillpack/liveops/churn-reason-finder/scripts/churn.py --csv sessions.csv --min-group 30 [--split platform]`. It ranks stages by players lost and shows the lost share per stage, the share of all lost players and the median minutes. Groups under 30 sessions are listed as too small.
4. Take the top two stages. For each, answer from evidence: what do those players have in common (device, source, level, last action)? Slice by platform first; a mobile-only spike points to controls or memory, not design (vault).
5. Pair with qualitative data: read feedback for that stage (`feedback-synthesizer`) and watch two playtests of the stage (`game-dev-playtest`). The stage that loses players without complaints is usually a confusion or pacing problem, not a content problem.
6. State a cause hypothesis as a testable change: add a goal 2-3 minutes out, remove a wall, fix a control, show the next reward. Keep it to one change per stage (`experiment-designer`).
7. Re-run after the change on the same cut; the stage's lost share should fall without another stage rising.

## Studio MCP path
`script_grep` for where stage/area state is set -> `multi_edit` to add the stage field to the leave event -> `start_stop_play` -> `execute_luau` (Server) to simulate a leave and `get_console_output` for the log line. Needs a connected Studio.

## Fallback
Any CSV with those columns works, including a hand-made one from a playtest log. Without a stage field the analysis cannot run; say so.

## Evidence
`Roblox/roblox-kb/retention-d1-d7.md` (low D1 is onboarding; free players not hooked in about 5 minutes rarely return). `Roblox/roblox-kb/analytics-metrics.md`: slice data to find the cause of a change; break retention down by source; pair telemetry with qualitative playtests; funnel drop-offs. `playtesting-and-feedback.md` for sample sizes of qualitative tests.

## Output
```
CHURN <range>  players not back next day: N
stage | sessions | lost | lost% | share of all lost | median min
Top 2 stages: segment, evidence, qualitative note, hypothesis, one change, re-check date
```

## Acceptance checks
- [ ] `churn.py --selftest` prints "selftest ok (4 checks)".
- [ ] Ranking is by players lost, not only percentage; small groups are excluded and listed.
- [ ] First-session players analysed apart from returning players.
- [ ] Top stage segmented by platform and checked against qualitative evidence.
- [ ] Output states correlation, not proof, and names one change.

## Pitfalls
High churn at the end of a natural stopping point (a match end) is normal. Who reaches a stage differs from who is made to leave by it. Logging the stage client-side. Keeping raw user ids in a shared file (hash or drop them before export).

## Related
`retention-diagnoser`, `funnel-analyzer`, `session-length-analyzer`, `feedback-synthesizer`, `cohort-reader`.
