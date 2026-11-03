---
name: session-length-designer
description: "Shape a target session length, its natural stopping points and the return hooks that bring players back: write a minute-by-minute beat plan and check it with sessionplan.py for reward gaps, missing stop or hook and a paywall before the first reward. Use when sessions are short or the loop has no natural end."
category: design
tags: session, session length, stopping point, return hook, retention, playtime reward, d1, pacing
kb: Roblox/roblox-kb/retention-d1-d7.md, Roblox/roblox-kb/analytics-metrics.md, Roblox/roblox-kb/first-session-onboarding.md, Roblox/roblox-kb/core-loops-and-game-design.md, Roblox/roblox-kb/case-studies-fish-it.md
related: core-loop-designer, reward-schedule-designer, first-minute-designer, session-length-analyzer, social-hook-designer, kit-system-integrator
---

# session-length-designer

Vault: design for 10+ minute sessions, mobile-first; free players not hooked in about 5 minutes rarely return; playtime rewards at about 10, 30 and 60 minutes (official suggestion); end with a moment of joy and a reason to return. This skill plans the beats; `session-length-analyzer` measures them live.

## When to use
Designing the arc of one play session, or fixing a game where players leave at minute 3. Not for: measuring real sessions (`session-length-analyzer`), login rewards (`kit-system-integrator`).

## Inputs (max 3)
1. Target session length (default: 12 minutes; vault's self-reported floor 10-12, under 5 is boring). 2. Core loop cycle time. 3. Player type (default: young, mobile).

## Procedure
1. Fix the target and the "good stop": the moment a player could leave satisfied (a zone cleared, a pet hatched, a round ended). Aim for at least one stop point around the target and one earlier.
2. Write the beat plan as CSV `minute,beat,kind` with kinds reward, goal, decision, stop, hook, social, paywall. Include: first reward by minute 1, a goal every 2-3 minutes, one decision (what to buy, where to go, when to cash in) per 5 minutes, playtime rewards at your chosen thresholds (try 3, 10, 30 as a starting set), a social beat (friend prompt or visible others), a stop, a hook.
3. Run `python session-length-designer/scripts/sessionplan.py plan.csv --target 12`. Fix flags: gap over 3 minutes without reward or goal, no stop, no hook after the last stop, first reward after minute 1, paywall before first reward, plan 2 minutes short of target.
4. Make the stop a choice: show a summary or "done for now" moment, not a hard wall. Players who can see a clean ending leave happy and return; players who leave mid-frustration do not.
5. Return hooks: one unfinished goal shown on the main screen, one timer (crop, egg, reward chest), one daily reward, and one social reason (a friend's progress). Do not punish absence.
6. Plan the measurement: p10/p50/p90 of session minutes with `session-length-analyzer` after launch; compare with the target.
7. Save `design/sessions.md` with plan, script output and measurement plan.

## Studio MCP path
Design only; after a prototype, `start_stop_play` and a timed run through the plan with `execute_luau` logging `os.clock()` at each beat to confirm the beats happen when planned.

## Fallback
Time a manual run with a stopwatch; mark times `estimated`.

## Evidence
`retention-d1-d7` (hooked in about 5 minutes; playtime rewards; stack several independent reasons to log in; a moment of joy and a reason to return), `analytics-metrics` (use percentiles; judge session length in context), `core-loops-and-game-design` (10+ minute sessions, mobile-first, AFK and offline progress deliberately), `case-studies-fish-it` (idle-leaning casual loop: pattern only; tracker claims).

## Output
`design/sessions.md`: target, stop points, beat table, sessionplan output ending OK, return hooks, measurement plan.

## Acceptance checks
- [ ] Executed: `python session-length-designer/scripts/sessionplan.py --selftest` prints `selftest ok`; the design CSV run ends with `OK`.
- [ ] First reward by minute 1 and no 3+ minute reward gap.
- [ ] At least one stop and one hook at or after the last stop.
- [ ] Nothing sold before the first reward.

## Pitfalls
Padding the session with waiting instead of choices. A hook that is a punishment (lose streak). Equating long sessions with good retention. Targets copied from other genres.

## Related
`core-loop-designer`, `reward-schedule-designer`, `first-minute-designer`, `session-length-analyzer`, `social-hook-designer`.
