---
name: multiplayer-test-planner
description: "Plan multi-client tests for sync and race bugs: which scenarios need two or more players, how to run them in Studio (local server with several clients, artificial lag, Network Simulator), what to assert on each side, and how to repeat them with bots. Use for any feature where one player's action must appear correctly to another."
category: qa
tags: multiplayer, multi-client, local server, sync, replication, lag, race, network simulator, test plan, two players
kb: Roblox/roblox-kb/testing-debugging-and-qa.md, Roblox/roblox-kb/client-server-and-remotes.md, Roblox/roblox-kb/playtesting-and-feedback.md, Roblox/roblox-kb/data-persistence.md
related: join-leave-race-tester, playtest-bot-writer, device-test-matrix, load-test-planner, repro-step-writer, dupe-exploit-hunter, regression-checklist-builder
---

# multiplayer-test-planner

Solo testing hides every bug that needs a second player: stale replication, ownership, rubber-banding, trades, party and round logic, race conditions. This skill picks the scenarios that need 2+ clients, says how to run each in Studio, and defines what each side must see. Races themselves are enumerated by `join-leave-race-tester`; here you plan the real-engine runs.

## When to use
Features with shared state: trading, parties, rounds, combat, shared objects, leaderboards, chat-like text, matchmaking, teleports between places. Not for: single-player logic (`playtest-bot-writer`), capacity (`load-test-planner`), or race enumeration (`join-leave-race-tester`).

## Inputs (max 2)
1. The feature and its shared state (default: read the remotes and replicated values). 2. How many players it supports (default: test 2, then the cap if small).

## Procedure
1. List each shared fact and who must see it: "A's pet appears on B's screen within 1 s", "the round timer is equal on all clients", "only the seller's inventory loses the item". One scenario per fact.
2. For each scenario write the actors, steps and the assertion on EACH side: server state, client A view, client B view. Use `Harness` checks (`playtest-bot-writer/scripts/Harness.luau`) so each assertion prints PASS/FAIL.
3. Add the standard multiplayer cases: late join (a client joins mid-round and must see current state), leave mid-action (`join-leave-race-tester`), two actors hitting the same object at once, spectator vs participant, host-only actions rejected for others, server stop while others are mid-action.
4. Run: Studio Test tab with a local server and 2+ players (Clients and Server), or separate Studio instances; use the Client/Server toggle and filtered Output to see which side errors. Add 0.5-1 s artificial replication lag and the Network Simulator (50-150 ms latency, some loss; change one setting at a time) and repeat the failing scenarios.
5. Automate the repeatable ones: `execute_luau` per datamodel (Server for state, Client for views) running Harness checks, then `get_console_output`; capture each client with `screen_capture` where the visual matters. Friend tests on a published private server cover real internet conditions.
6. Record results per scenario: PASS/FAIL, which side, the Output lines, and the lag setting. A scenario that fails only under lag is a real bug, not a flake.
7. Feed failures to `repro-step-writer` and `bug-report-template`; add each fixed scenario to `regression-checklist-builder`.

## Studio MCP path
`list_roblox_studios` -> `start_stop_play` (with the multi-client option) -> `execute_luau` (datamodel_type Server, then Client for each client) running the scenario checks -> `get_console_output` -> `screen_capture` per client -> `start_stop_play` (stop). One agent drives the session at a time.

## Fallback
No multi-client automation: write the scenario table for people to run in Studio's Test tab (Players: 2) and tick results; model the order-dependent ones in Lune with `join-leave-race-tester`. Real replication timing and internet conditions are `untested` until a published private server run.

## Evidence
`Roblox/roblox-kb/testing-debugging-and-qa.md`: test in the right mode (solo client-server, multiplayer with 2+ players, friend features with multiple clients); use the Client/Server toggle; reproduce race conditions with 0.5-1 s artificial lag; simulate network conditions one at a time with 50-150 ms baseline latency and loss; debug replication by comparing data ping, network traffic and ownership; private servers are test-safe. `Roblox/roblox-kb/client-server-and-remotes.md` for what replicates. `Roblox/roblox-kb/playtesting-and-feedback.md` for friend tests.

## Output
```
MULTIPLAYER PLAN <feature> <date>: scenarios N, players P
| # | scenario | actors | server asserts | client A | client B | lag setting | result |
Run log: PASS/FAIL per row, Output lines for fails      Untested: <internet conditions, >P players>
```

## Acceptance checks
- [ ] Every shared fact has a scenario with an assertion for server and each client.
- [ ] Late join, leave mid-action and simultaneous-action cases are present or explicitly excluded with a reason.
- [ ] Failing scenarios were re-run under artificial lag and the result recorded.
- [ ] Results are PASS/FAIL/untested per row; no row is "looked fine".
- [ ] Fixed scenarios were added to the regression checklist.

## Pitfalls
Only testing at zero latency. Two clients controlled by one tester who never leaves. Assuming the server view equals the client view. Checking only the happy order. Treating a bug that needs lag as "unrealistic". Forgetting the third player.

## Related
`join-leave-race-tester`, `playtest-bot-writer`, `device-test-matrix`, `load-test-planner`, `repro-step-writer`, `regression-checklist-builder`.
