---
name: npc-cost-reducer
description: "Scale NPC AI, pathfinding and movement updates by distance and relevance with update rings and frame staggering, park far NPCs, move cosmetics to the client and pool spawns, then show the per-frame update count and server CPU before and after. Use when server CPU grows with NPC count or crowds lag."
category: perf
tags: npc, ai, update rate, stagger, pathfinding, parked, crowd, pooling, distance, server cpu
kb: Roblox/roblox-kb/optimization-and-streaming.md, Roblox/roblox-kb/physics-pathfinding-and-npc-ai.md, Roblox/roblox-kb/scripting-and-performance.md
related: npc-spawner-builder, animation-cost-reducer, heartbeat-loop-auditor, object-pool-builder, script-profiler, server-tick-analyzer, network-traffic-auditor
---

# npc-cost-reducer

An NPC does not need to think at 60 Hz when nobody is near it. This skill gives each NPC an update rate from its distance to the nearest player, staggers the updates across frames so the work spreads evenly, parks the far ones, and moves everything cosmetic off the server.

## When to use
Server heartbeat or script time grows with NPC count, enemies/pets/crowd members each run their own loops, pathfinding calls spike. Not for: animation cost itself (`animation-cost-reducer`), spawn and aggro rules (`npc-spawner-builder`), or generic loops (`heartbeat-loop-auditor`).

## Inputs (max 2)
1. NPC count at peak and what each does per update (path, raycast, target search). 2. Gameplay distance that matters (aggro range, render range).

## Procedure
1. Baseline: count NPCs, measure per-update cost (Script Profiler function time divided by calls) and server heartbeat/script time in the busy scene (`server-tick-analyzer` for the sampler). Stop if the per-update cost is under about 0.05 ms and NPCs under about 50: the saving would be small.
2. Define rings with `scripts/UpdateRate.luau`: default `{<=100 studs: 30 Hz, <=250: 10 Hz, <=500: 3 Hz, beyond: parked}`. These rates are the skill's heuristic; the vault's examples are 100 studs (test) and 500 studs (final) for animation focus. Set rings from your gameplay: aggro range gets the top rate.
3. Schedule with one central loop, not one loop per NPC: each frame call `UpdateRate.shouldUpdate(frameIndex, npcId, UpdateRate.hzFor(distance, rings))` and update only those NPCs. Staggering by id spreads the load evenly (60 NPCs at 10 Hz is 10 updates per frame, no spikes). Compute distance to the nearest player once per NPC per second, not per frame.
4. Check the saving on paper first: `UpdateRate.updatesPerFrame(distances)` and `savedPercent(distances)` for the real distance distribution; expected updates per frame times per-update ms is the new cost.
5. Make far NPCs cheap: park them (anchored, animator off, no pathfinding; keep them in ReplicatedStorage as data if streaming allows), re-activate when a player enters the outer ring, and teleport rather than walk to catch up.
6. Pathfinding: feed waypoints one at a time to `Humanoid:MoveTo` advancing on `MoveToFinished`; avoid recomputing paths every update (moving non-navigable parts invalidates tiles); spawn NPCs only on loaded terrain (check current and target positions).
7. Cosmetics to the client: visual-only movement, wave math, bobbing; sync NPC state through attributes. Pool respawned NPCs (`object-pool-builder`) instead of destroy/clone.
8. Re-measure in the same scene; keep only changes that lowered script/server time without breaking aggro, targeting or fairness.

## Studio MCP path
`script_grep` (`while true|Heartbeat|MoveTo|ComputeAsync`) -> `script_read` AI modules -> `multi_edit` to the central scheduler -> `start_stop_play` -> `execute_luau` (Server) to spawn N test NPCs and read `tick_sampler.luau` from `server-tick-analyzer` -> `get_console_output`. Server CPU timing needs the profiler: ask or label `untested`.

## Fallback
Rojo files for the scheduler module; the ring table can be tested under Lune with a list of distances (`UpdateRate` tests do exactly this). Gameplay feel (does an NPC wake in time?) is `untested` without a playtest.

## Evidence
`Roblox/roblox-kb/optimization-and-streaming.md`: animate NPCs only near the camera focus (test 100, final 500 studs; parked outside), client-run visual movement kept network near zero in a 200-NPC demo (indie), serial AI for 72 deer about 50 ms versus about 16 ms in parallel, pool respawned NPCs, pathfinding recomputation notes. `Roblox/roblox-kb/physics-pathfinding-and-npc-ai.md`: keep NPC AI cheap, MoveTo waypoint stepping. Official: `Roblox/docs/Videos/2026-10-28 - Docs scripting multithreading.md` (Actors for parallel compute that does not touch the DataModel). Ring Hz values are heuristics.

## Output
```
NPC COST <scene> <date>   NPCs 300 (peak)
Rings: <=100 st 30 Hz | <=250 10 Hz | <=500 3 Hz | beyond parked
Distribution: 12 / 40 / 90 / 158 -> updates/frame 4.9 (was 300) = 98% fewer
Server script time 11.2 ms -> 1.6 ms [profiler | estimate]. Behaviour check: aggro within 100 studs unchanged.
```

## Acceptance checks
- [ ] Ring table stated with the gameplay reason for each distance.
- [ ] Updates per frame before/after computed from the real distance list.
- [ ] Server time before/after measured, or labelled estimate/`untested`.
- [ ] A playtest confirms NPCs near players behave exactly as before.
- [ ] Executed check: `UpdateRate.test.luau` (5 tests) passes under Lune; scripts pass luau-check.

## Pitfalls
Parking NPCs that must keep ticking (timers, world events). One loop per NPC. Running distance checks per frame for every NPC. Letting all NPCs update on the same frame after respawn. Letting the client decide gameplay-relevant NPC state.

## Related
`animation-cost-reducer`, `heartbeat-loop-auditor`, `object-pool-builder`, `script-profiler`, `server-tick-analyzer`.
