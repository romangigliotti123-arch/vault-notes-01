---
name: round-system-builder
description: "Build the intermission, playing, ending state machine for round games as pure logic: minimum players, countdown abort, grace-window late joiners, last-standing or timer endings, and cleanup that always runs. Use for round-based modes; queue/teleport flow is lobby-matchmaking-builder."
category: systems
tags: rounds, intermission, state machine, late joiners, countdown, cleanup, round based, minigame
kb: Roblox/roblox-kb/core-loops-and-game-design.md, Roblox/roblox-kb/matchmaking-and-teleport.md, Roblox/roblox-kb/playtesting-and-feedback.md, Roblox/roblox-kb/first-session-onboarding.md
related: rbx-rounds, lobby-matchmaking-builder, spawn-system-builder, checkpoint-system-builder, health-damage-builder
---

# round-system-builder

One job: decide what state the match is in. `scripts/Rounds.luau` is driven by `tick(dt, readyPlayers)` and calls your `onStart`, `onEnd` and `cleanup` hooks; it knows nothing about maps, teleports or UI. States: Waiting (not enough players) -> Intermission (countdown that aborts if players leave) -> Playing (ends on time, empty, or last player standing) -> Ending (results) -> cleanup -> Waiting. The installed `rbx-rounds` skill gives the Roblox walkthrough; this one is the tested logic.

## When to use
Round-based games: lobby/intermission/round/results. Not for: queueing into separate servers (`lobby-matchmaking-builder`), map generation, scoring rules.

## Inputs (max 2)
1. Min players, intermission, round length, end screen seconds (default: 2, 15, 120, 6). 2. Late join rule (default: join within the first 10 s of a round, else spectate).

## Procedure
1. Write the round spec: what starts it, what ends it (timer, last standing, objective), what players see in each state. Vault: show objective and status, send defeated players to a lobby/spectate, give ongoing rewards, and run cleanup between rounds.
2. Copy `Rounds.luau`; construct with hooks: `onStart(ids)` teleports to the map and sets health; `onEnd(reason, survivors)` awards winners; `cleanup()` removes map objects, projectiles, connections and temp state.
3. Drive it once per second from one server loop: `rounds:tick(1, #readyPlayers)`; do not run a separate loop per feature. Use `rounds:join(userId)` when a player becomes ready (it answers `play` or `spectate`) and `rounds:out(userId)` on death, leave or elimination.
4. Decide the intermission: vault examples quote 5-10 s for a single indie round game (self-reported); start short and lengthen only if players need time to read. Voting between intermission and round is an optional stage (a vault source suggests ~5 s) handled in the glue before `onStart`.
5. Late joiners: `joinGrace` lets them in during the first N seconds; after that they spectate until the next round. Never insert a late joiner into a round whose map state they have not received.
6. Cleanup discipline: every connection and instance a round creates is registered and destroyed in `cleanup`; test by running 20 rounds in Studio and watching the Memory/Instance counts return to baseline (live observation, not in Lune).
7. Run `cd ~/.claude/claude-kit/systems && lune run ../skillpack/systems/round-system-builder/scripts/tests/Rounds.test.luau` (quote the "N passed, 0 failed" line) for the state logic.

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `multi_edit` (or edit the Rojo files) to add `Rounds.luau` and the round loop script -> `start_stop_play` -> `execute_luau` (Server) to start a local server with two test players, run one full round and read the state log -> `get_console_output` to read the result. Map loading, teleports and the HUD are Studio work: `untested` here.

## Fallback
Files + Lune tests only. Everything that needs a running Studio session (map/teleport glue, leaks across many rounds) stays `untested` until the owner runs it; the Lune tests below are the headless proof for the pure logic.

## Evidence
`Roblox/roblox-kb/core-loops-and-game-design.md` (round games: intermission, prepare, match, end status, cleanup, reset; show the objective; send defeated players to a lobby), `Roblox/roblox-kb/matchmaking-and-teleport.md` (the 5-10 s intermission is a single indie example, not a default; no verified minimum player counts), `Roblox/roblox-kb/playtesting-and-feedback.md`.

## Output
`Rounds.luau`, the hooks, `design/rounds.md` (states, timings, end rules, late-join rule, cleanup list).

## Acceptance checks
- [ ] Waits for the minimum and aborts the countdown when players drop (Rounds tests 1-2).
- [ ] Time, last-standing and empty endings fire `onEnd` once and `cleanup` runs after the end screen (tests 3-4, 6).
- [ ] Late joiners play only inside the grace window (test 5).
- [ ] A 20-round Studio run returns instance counts to baseline (`untested` unless run).
- [ ] Rounds Lune tests pass: `cd ~/.claude/claude-kit/systems && lune run ../skillpack/systems/round-system-builder/scripts/tests/Rounds.test.luau` (quote the "N passed, 0 failed" line).

## Pitfalls
Cleanup that forgets event connections (leak per round). Starting a round with fewer players than the rules need. Tick loops per system that drift out of sync. Letting spectators affect the round. Teleporting players before the map is loaded.

## Related
`rbx-rounds`, `lobby-matchmaking-builder`, `spawn-system-builder`, `checkpoint-system-builder`, `health-damage-builder`.
