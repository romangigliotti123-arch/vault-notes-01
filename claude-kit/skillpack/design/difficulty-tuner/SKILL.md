---
name: difficulty-tuner
description: "Set difficulty ramps and fail states from playtest data so players are challenged but not stuck: collect per-stage attempts, fails and quits, find spikes, walls and slack with difficulty.py, then change one variable per stage. Use for obbies, waves, bosses and any stage-based game after a playtest."
category: design
tags: difficulty, ramp, balance, fail state, spike, wall, playtest, drop-off, obby, stages
kb: Roblox/roblox-kb/core-loops-and-game-design.md, Roblox/roblox-kb/genre-mechanics.md, Roblox/roblox-kb/combat-and-gameplay-systems.md, Roblox/roblox-kb/playtesting-and-feedback.md, Roblox/roblox-kb/case-studies-tower-of-hell.md
related: level-flow-planner, boss-encounter-designer, progression-curve-designer, playtest-bot-writer, funnel-analyzer, tutorial-designer
---

# difficulty-tuner

Vault: pace difficulty as a curve (ramp up, peak at bosses, then dip), launch slightly harder than target and ease later, give breathing room, smooth spikes with hints, keep changes within player control, use drop-off data. Separate challenging from impossible.

## When to use
You have stages, waves or rooms and some player data, or want a plan to collect it. Not for: XP curve (`progression-curve-designer`), a single boss (`boss-encounter-designer`), live telemetry analysis (`funnel-analyzer`).

## Inputs (max 2)
1. Per-stage data as CSV `stage,attempts,fails,quits[,reached]` (default: collect it, see step 1). 2. Target fail rate band (default: 15-35 percent per stage, the skill's default, 40-50 at designated bosses).

## Procedure
1. If no data: add the logging plan. Per stage log attempt start, fail (with cause: fall, enemy, timer), clear and quit. At least 30 attempts per stage from at least 5 different players; fewer is marked LOW N and not judged.
2. Run `python difficulty-tuner/scripts/difficulty.py stages.csv`. It flags spikes (fail rate above 1.6x the median of the previous 3 stages), walls (quit rate above 8 percent) and slack (3 falling stages). Thresholds are the skill's defaults.
3. For each flag, diagnose with the three questions: was it readable (telegraph, sight line, clear goal)? was it fair (no instant death without warning, no luck)? was it taught earlier (a lead-in stage with the mechanic alone)? Change exactly one variable: gap size, enemy speed, timer, checkpoint spacing, or add a hint after N fails.
4. Fail states: respawn at the stage start or checkpoint, never at the last save; one miss must not restart a long section (vault: padding and full restarts kill momentum); never reset all progress on death in a non-roguelike.
5. Choice at spikes: offer an optional easier route or a skip after repeated failures, labelled by neutral names (Normal/Hard/Extreme; the vault says "Easy" feels intimidating to choose).
6. Re-test the changed stages with fresh players; stop when no stage is flagged or after three tuning rounds, then ship and watch live data.
7. Save `design/difficulty.md` with before and after table.

## Studio MCP path
`start_stop_play`, then drive a bot with `character_navigation` / `user_keyboard_input` through the stage and `execute_luau` (Server) to print attempts and fails per stage; paste the numbers into the CSV. A bot is not a player: mark bot data `bot`.

## Fallback
Collect by hand: five testers, a notes sheet with a tally per stage.

## Evidence
`core-loops-and-game-design` (pace difficulty as a curve; fair; telegraph; fade platforms; drop-off data), `genre-mechanics` (ramp difficulty; name difficulties Normal/Hard/Extreme), `combat-and-gameplay-systems` (readable attacks), `playtesting-and-feedback`, `case-studies-tower-of-hell` (stage-based obby pattern).

## Output
`design/difficulty.md`: stage table with fail%, quit%, flags; one change per flagged stage; fail-state rules; re-test results.

## Acceptance checks
- [ ] Executed: `python difficulty-tuner/scripts/difficulty.py --selftest` prints `selftest ok`; the design's data run is pasted with its final line.
- [ ] No stage is judged on fewer than 30 attempts.
- [ ] Each flagged stage has exactly one change and a re-test result.
- [ ] No fail state drops the player into the danger that killed them or loses unrelated progress.

## Pitfalls
Tuning on teammates who know the route. Fixing a quit wall by making everything easier. Stacking new mechanic and spike in one stage. Treating bot clears as human difficulty.

## Related
`level-flow-planner`, `boss-encounter-designer`, `progression-curve-designer`, `tutorial-designer`, `playtest-bot-writer`.
