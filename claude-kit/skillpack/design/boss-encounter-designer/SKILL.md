---
name: boss-encounter-designer
description: "Design a readable boss or wave encounter: phases, telegraphs with wind-up times, damage per hit, practice route, reward and length, then check fairness with bosscheck.py. Use for any boss, wave defence or timed set-piece, before building the AI."
category: design
tags: boss, wave, encounter, telegraph, phases, fairness, combat, pve, set piece
kb: Roblox/roblox-kb/combat-and-gameplay-systems.md, Roblox/roblox-kb/genre-mechanics.md, Roblox/roblox-kb/core-loops-and-game-design.md, Roblox/roblox-kb/case-studies-doors.md, Roblox/roblox-kb/case-studies-piggy.md
related: difficulty-tuner, level-flow-planner, game-feel-polisher, npc-spawner-builder, reward-schedule-designer, tutorial-designer
---

# boss-encounter-designer

Vault: split every attack into anticipation, contact and recovery; give enemies distinct silhouettes and exaggerated wind-ups; keep boss fights longer than a minute or two; avoid bosses that kill quickly while the player deals tickle damage; the first boss must teach and not be cheesable by running; practice must be viable.

## When to use
Designing a boss, mini-boss, wave defence or chase set-piece. Not for: the AI code (`npc-spawner-builder`) or overall stage difficulty (`difficulty-tuner`).

## Inputs (max 3)
1. What the encounter teaches or tests (default: the game's core mechanic). 2. Player DPS and HP at that point (default: from `design/progression.md`; else mark values `estimated`). 3. Arena size and player count (default: 1-8 players).

## Procedure
1. State the role: what the player must have learned to win (a dodge, a block, positioning, teamwork). One test per boss.
2. Design 2-3 phases. Per phase: 1-3 attacks. Per attack: name, wind-up seconds (telegraph with a distinct silhouette, colour or sound), contact effect, recovery window (when the player can punish), damage percent of player HP, and how it is avoided.
3. Add a rhythm: attack, recovery, opening for damage; no stun-lock (poise or limited stagger, multiple attackers staggered); at least one behaviour that is not walk-and-hit.
4. Length: set boss HP so time to kill is between 60 s and about 10 minutes at expected DPS; more than a minute or two matches the vault; the upper bound is the skill's default against padding.
5. Fill `boss.json` (`hp`, `player_dps`, `phases[].attacks[]` with `windup_s`, `damage_pct`, `avoidable`, plus `practice_available`, `reward_on_clear`) and run `python boss-encounter-designer/scripts/bosscheck.py boss.json`. Fix every FLAG: wind-up under 0.5 s, a single hit over 50 percent of player HP, an unavoidable attack, fewer than 2 phases, no practice route, no reward. The numeric limits are the skill's defaults; a playtest overrides them.
6. Practice and fairness: a way to practise the attacks (a training dummy or an easy mode) that is not a trivial exploit; the boss cannot be defeated by running away; death returns the player to a lobby or spawn with something to do (spectate) and not into the same danger.
7. Reward: matched to the effort, shown during the fight (a loot preview), granted on clear; a consolation for near-wins.
8. Hand the phase table to `game-feel-polisher` (hit stop, telegraph sounds) and to `npc-spawner-builder`.
9. Save `design/boss-<name>.md` with the spec and script output.

## Studio MCP path
After build: `start_stop_play`, `execute_luau` (Server) to set player HP and DPS and time the fight with `os.clock()`; `screen_capture` at each wind-up; `get_console_output`.

## Fallback
Table and JSON only; mark times `estimated`.

## Evidence
`combat-and-gameplay-systems` (attack phases; prevent stun-lock; readable attacks; boss length; bosses that feel powerful), `genre-mechanics` (bosses and practice must teach; vary enemy behaviours and scale PvE difficulty), `core-loops-and-game-design` (telegraph attacks; pace difficulty with a peak at bosses), `case-studies-doors`, `case-studies-piggy` (chase and escape set-piece patterns).

## Output
`design/boss-<name>.md`: role, phase table, timing numbers, bosscheck output ending OK, practice route, reward.

## Acceptance checks
- [ ] Executed: `python boss-encounter-designer/scripts/bosscheck.py --selftest` prints `selftest ok`; the spec run ends with `OK`.
- [ ] Every attack has a wind-up, a recovery window and an avoidance.
- [ ] A practice route and a reward exist.
- [ ] The boss tests exactly one learned skill.

## Pitfalls
Damage sponge with one attack. Unreadable VFX that hide the telegraph. Instant-death with no warning. A boss that is trivial with a single exploit position.

## Related
`difficulty-tuner`, `level-flow-planner`, `game-feel-polisher`, `npc-spawner-builder`, `reward-schedule-designer`.
