---
name: load-test-planner
description: "Plan a load test with many clients: turn expected traffic into messages and bytes per second, set pass/fail budgets, ramp clients in steps, decide what to measure, and read the result into a safe player capacity. Use before a launch, event or update that expects a spike, or when servers degrade as they fill."
category: qa
tags: load test, stress test, capacity, many clients, remote traffic, ramp, budget, server performance, scalability, players
kb: Roblox/roblox-kb/testing-debugging-and-qa.md, Roblox/roblox-kb/scripting-and-performance.md, Roblox/roblox-kb/all-numbers-and-benchmarks.md, Roblox/roblox-kb/anti-exploit-and-security.md
related: lag-hunter, script-profiler, game-optimizer, multiplayer-test-planner, remote-fuzzer, device-test-matrix
---

# load-test-planner

A load test answers one question: how many players can one server (and the game) take before a budget breaks? This skill plans it with arithmetic you can check (`scripts/LoadMath.luau`, tested): traffic totals, worst case at your rate limits, a ramp, and a pass/fail verdict per budget. It does not know Roblox's current limits; you supply them and live-check the docs.

## When to use
Before a launch, sponsored push, update event or a raised player cap; when lag appears as servers fill. Not for: finding which script is slow (`script-profiler`), network lag diagnosis (`lag-hunter`), or one-client performance (`game-optimizer`).

## Inputs (max 3)
1. Target concurrent players per server and expected spike (default: the server cap). 2. The traffic per player per second for each remote (default: read it from the code or from a profiled session). 3. The budgets (default: server frame time inside the frame budget, memory below your ceiling, per-remote message rate at or below the limiter, no DataStore queue warnings).

## Procedure
1. List the remotes and their rates per client (movement, input, chat, UI updates, DataStore autosave) and bytes per message. Put them in `LoadMath.totals({ clients, traffic })` and read messages/s and bytes/s and per-client bytes/s. Stop when every remote that fires more than once per second is in the table.
2. Compute the worst honest case: `LoadMath.worstCase(clients, limits)` with every client at your per-remote rate limits. If the server cannot take that, the limits are too loose.
3. Choose budgets and write them as `Budget` rows (name, measured, limit, higherIsWorse). Typical rows: server heartbeat ms against the frame budget, memory MB against your ceiling, remote messages/s, DataStore calls per minute, instance count. Live-check platform limits in the docs; do not hard-code them.
4. Ramp: `LoadMath.ramp(start, max, factor, holdSeconds)`, e.g. 2 -> 40 doubling with 120 s holds. Hold long enough for memory trends (`crash-log-reader` memory trend) and autosave cycles to show.
5. Generate load. Real clients: Studio local server with several clients (Test tab, number of players) and `playtest-bot-writer` bots; many more needs real devices or friends and private servers. Never load-test the live game with fake traffic that touches the live DataStore.
6. Measure at each step: MicroProfiler (server), Developer Console F9 (memory, script activity, network), `get_console_output` for errors; record the numbers into `Budget.measured` and call `LoadMath.verdicts`.
7. `LoadMath.safeCapacity(steps)` gives the largest client count before the first failing step; set the server cap below it with margin and note the bottleneck (CPU, memory, network, DataStore).

## Studio MCP path
`list_roblox_studios` -> `start_stop_play` -> `execute_luau` (Server) to sample `os.clock()` per Heartbeat, `collectgarbage("count")`, instance counts and remote counters each ramp step -> `get_console_output` -> `start_stop_play` (stop). Studio is not the platform: absolute numbers need a published private-server run.

## Fallback
No Studio or no bots: do the arithmetic only (`lune run ../skillpack/qa/load-test-planner/scripts/tests/LoadMath.test.luau` from `claude-kit/systems`) and write the ramp and budgets for the owner to run with friends. Every measured number is then `untested`.

## Evidence
`Roblox/roblox-kb/testing-debugging-and-qa.md`: test solo and with 2+ players, use Network Simulator for latency and loss, do not judge performance from Studio or emulators, fix test conditions for comparable results, compare heap snapshots over long sessions. `Roblox/roblox-kb/scripting-and-performance.md`: memory is the binding constraint on mobile; most crashes are out-of-memory (indie-sourced thresholds, live-check). `Roblox/roblox-kb/anti-exploit-and-security.md`: server-side per-player rate limits.

## Output
```
LOAD PLAN <game> <date>: target N clients
traffic table + messages/s, bytes/s, worst case at limits
ramp: 2,4,8,16,32,40 (hold 120 s)
budgets table; result per step; safe capacity = X; bottleneck = Y
```

## Acceptance checks
- [ ] `lune run` of the LoadMath test prints "6 passed, 0 failed".
- [ ] Traffic table and worst case computed from real handler/limiter values (quoted).
- [ ] Each budget has a limit, a source for the limit, and a measured value or `untested`.
- [ ] The test did not touch the live game or live DataStore.
- [ ] Safe capacity is stated with the bottleneck, or the plan is labelled "not run".

## Pitfalls
Averaging instead of looking at the first failing step. Holds too short to show a leak. Testing only the happy path (join storms and mass leaves are the real spikes). Treating Studio numbers as platform numbers. Bots that are unrealistically quiet.

## Related
`lag-hunter`, `script-profiler`, `game-optimizer`, `multiplayer-test-planner`, `device-test-matrix`.
