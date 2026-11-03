---
name: join-leave-race-tester
description: "Test joins and leaves during critical flows (loading data, purchases, trades, teleports, round start/end) by modelling each flow as steps between yield points and exploring every ordering for broken invariants, then reproducing the failing order in Studio with artificial lag. Use before shipping any flow that yields while a player can leave or join."
category: qa
tags: race condition, join, leave, playerremoving, yield, interleaving, concurrency, bindtoclose, teleport, lag, test
kb: Roblox/roblox-kb/testing-debugging-and-qa.md, Roblox/roblox-kb/data-persistence.md, Roblox/roblox-kb/anti-exploit-and-security.md, Roblox/roblox-kb/client-server-and-remotes.md
related: dupe-exploit-hunter, multiplayer-test-planner, data-loss-simulator, purchase-flow-tester, playtest-bot-writer, save-load-tester
---

# join-leave-race-tester

Roblox code yields at DataStore and Marketplace calls, `task.wait`, remote round trips and waits for the character. A race bug is a bad order of the pieces between yields: the player leaves while data loads, a purchase finishes after they left, a round ends while someone joins. `scripts/RaceScheduler.luau` enumerates every ordering of actor steps (keeping each actor's own order) and reports the schedules that break your invariant. It is a model: it proves the bug exists in the model and gives a replay order.

## When to use
Any flow with a yield where the player, another player or the server can act in between: load profile on join, `PlayerRemoving` save, trade, purchase grant, round start/end, teleport arrival. Not for: pure logic with no yields, or performance races (`lag-hunter`).

## Inputs (max 2)
1. The flow (default: join -> load data -> spawn, and leave -> save). 2. The invariant that must always hold, in one sentence (default: no data lost, no value duplicated, no errors on a nil player).

## Procedure
1. Write the flow as steps between yields. Example: A = join: `[request load]`, `[data arrives: set session]`, `[spawn]`; B = leave: `[PlayerRemoving: save]`, `[release]`. Stop when each actor's steps are atomic (nothing yields inside a step).
2. Model the state (`setup()` returns a fresh table) and write each step as a function mutating it. Add the invariant as `invariant(state)` returning nil or a message ("session exists for a player who left", "save ran before load finished and wrote the template").
3. `RaceScheduler.explore(setup, actors, invariant)`; keep actors to 2-3 with at most 5 steps each (`RaceScheduler.count` tells the size; the default cap is 20000 schedules and `truncated` says if it was hit).
4. For each failing schedule (shown as `A1 B1 A2`): reproduce in Studio by inserting `task.wait` at the yields in that order, or use the lag setting (0.5-1 s artificial replication lag exposes races, vault); then fix: a cancel check after each yield (`LoadAsync(key, cancel)` in the kit PlayerData), re-check `player.Parent` after every yield, per-request locks, a single owner function for the transition.
5. Re-run until 0 failing schedules; keep the model as a regression test under `tests/races/`.
6. Cover the real checklist: leave during load (kit `LoadAsync` takes a `cancel` and releases the lock again), leave during purchase (receipt returns `NotYet`, retried on rejoin), leave during teleport, server shutdown during a round (`BindToClose` has about 30 s), double join of the same account.
7. Report schedules, fixes and anything left untested.

## Studio MCP path
`list_roblox_studios` -> `start_stop_play` -> `execute_luau` (Server) to install lag/`task.wait` probes and to call `player:Kick()` at a chosen point -> a second client via `multiplayer-test-planner` -> `get_console_output` for errors such as "attempt to index nil" -> `start_stop_play` (stop).

## Fallback
Lune only: model the flow, run `lune run ../skillpack/qa/join-leave-race-tester/scripts/tests/RaceScheduler.test.luau` from `claude-kit/systems` for the pattern. The model's fidelity to the real engine's scheduling is an assumption; mark real two-client confirmation `untested`.

## Evidence
`Roblox/roblox-kb/testing-debugging-and-qa.md`: reproduce race conditions with 0.5-1 s artificial lag; test solo and with 2+ players; stress-test loops, duplicates and persistence. `Roblox/roblox-kb/data-persistence.md`: save on `PlayerRemoving` and in `BindToClose`, periodic saves cover crashes, session locking. `Roblox/roblox-kb/anti-exploit-and-security.md`: tear down player data on `PlayerRemoving` after saving; process purchases idempotently.

## Output
```
RACE <flow>: N schedules, F failing
  FAIL A1 B1 A2: session exists for a player who left
Fix: <what changed>   Re-run: 0 failing
```
Plus the model file path.

## Acceptance checks
- [ ] RaceScheduler Lune test prints "6 passed, 0 failed".
- [ ] The model's failing schedule (if any) was reproduced in Studio or marked untested.
- [ ] After the fix `Race.explore` returns 0 failing schedules and `truncated` is false (or the cap is named).
- [ ] Each yield in the real code has a post-yield player/state check.
- [ ] The model is saved as a regression test.

## Pitfalls
Steps that secretly yield inside (split them). Modelling only the happy order. Forgetting that the same player can join twice quickly. Fixing the symptom with a longer `task.wait`. Assuming `PlayerRemoving` code always finishes (it does not on a crash).

## Related
`dupe-exploit-hunter`, `multiplayer-test-planner`, `data-loss-simulator`, `purchase-flow-tester`, `save-load-tester`.
