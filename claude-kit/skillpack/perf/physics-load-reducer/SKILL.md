---
name: physics-load-reducer
description: "Cut physics cost: count unanchored assemblies, moving assemblies, constraints and CanTouch/CanQuery parts, anchor or sleep what does not need simulating, set Adaptive stepping, clean up debris, and prove the drop in physics time with the MicroProfiler. Use when the server or client physics step is long, or a map has many loose parts."
category: perf
tags: physics, unanchored, assemblies, constraints, CanTouch, CanQuery, sleep, adaptive stepping, network ownership, debris
kb: Roblox/roblox-kb/optimization-and-streaming.md, Roblox/roblox-kb/physics-pathfinding-and-npc-ai.md, Roblox/roblox-kb/scripting-and-performance.md
related: game-optimizer, lag-hunter, collision-fidelity-tuner, anchor-checker, server-tick-analyzer, cpu-vs-gpu-diagnoser
---

# physics-load-reducer

Physics cost scales with the number of simulating assemblies, constraints and contact checks, not with part count. This skill finds what is awake and needlessly physical, removes it from the simulation safely, and measures the physics bars before and after.

## When to use
MicroProfiler shows long physics/simulation tasks (orange Jobs bars), server heartbeat drops with many loose parts, tycoon/sim maps with thousands of props, destruction or ragdoll systems. Not for: scripts hogging the frame (`script-profiler`), collision fidelity choices (`collision-fidelity-tuner`) or anchoring one broken model (`anchor-checker`).

## Inputs (max 2)
1. Where the cost shows (server, client, one area, only with N players). 2. Whether gameplay depends on physical props (vehicles, ragdolls, pushables).

## Procedure
1. Baseline: run `scripts/physics_census.luau` in Edit mode, then again in Play on the Server datamodel. Save both. Read: unanchored share, assemblies, how many are moving right now, CanTouch/CanQuery/CanCollide counts, constraints, welds, Motor6D, the largest assemblies, and PhysicsSteppingMethod. In the MicroProfiler (Ctrl+Alt+F6, pause with Ctrl+P) note the physics task time. Stop if you cannot capture a profiler frame: counts alone are `untested` for time.
2. Anchor what never moves: static props, decor, scenery, static NPCs. Idle unanchored assemblies sleep by themselves (below about 0.33 studs/s linear and 0.42 rotational), so unanchoring is cheap only while they stay still; anything that keeps jittering, is welded to something moving or is hit constantly stays awake.
3. Turn off the interaction flags on scenery: CanTouch off where no `.Touched` handler exists, CanQuery off where nothing raycasts or does overlap queries (CanQuery is only exposed when CanCollide is off), CanCollide off on walk-through decor. Many touch/query parts is a known lag source.
4. Reduce assembly complexity: fewer constraints per contraption, fewer welds and Motor6D chains on the server, replace tiny weld forests with one mesh (`model-cleaner`), prefer RigidConstraint only where attachments need it.
5. Stepping: set `Workspace.PhysicsSteppingMethod` to Adaptive (60/120/240 Hz as needed; fixed mode runs 240 Hz, four steps per 60 FPS frame; docs claim up to 2.5x). Write physics-affecting logic in PreSimulation and read results in PostSimulation.
6. Ownership and debris: give network ownership of vehicles to the driver where safe (not `SetNetworkOwner(nil)` everywhere); let clients simulate cosmetic debris; clean flown-off or fragmented parts with the Debris service (about 30 s is the vault example) and lower FallenPartsDestroyHeight so fallen parts are handled sooner.
7. Re-run the census and the profiler capture on the same scenario. Keep each change only if the physics time dropped and gameplay (pushing, vehicles, destruction) still works.

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `execute_luau` (Edit) `scripts/physics_census.luau` -> `start_stop_play` -> `execute_luau` (Server) the same script -> `script_grep` for `.Touched`, `SetNetworkOwner`, `Debris`, `Anchored = false` -> `multi_edit` / `execute_luau` property edits (log each) -> `get_console_output`. Profiler windows are manual: ask the owner for the physics time or mark it `untested`.

## Fallback
Command bar: paste `physics_census.luau`. Rojo: change scripts as files and give the owner the property list (anchoring parts is place data). Mark time claims `untested` without a profiler reading; mark gameplay checks `untested` unless a playtest was run.

## Evidence
`Roblox/roblox-kb/optimization-and-streaming.md` (anchor what needs no physics; Adaptive stepping; disable CanCollide/CanTouch/CanQuery on non-interactive parts; Debris cleanup; client-owned parts offload physics; 60 tweened vs animated doors, indie test). `Roblox/roblox-kb/physics-pathfinding-and-npc-ai.md` (minimise constraints, network ownership to the driver, PreSimulation/PostSimulation, event-driven hitboxes). Official: `Roblox/docs/Videos/2026-10-28 - Docs physics sleep-system.md` (sleep thresholds: 0.33 and 0.42 studs/s), `Roblox/docs/Videos/2026-10-28 - Docs physics adaptive-timestepping.md` (up to 2.5x; 240/120/60 Hz buckets), `Roblox/docs/Videos/2026-10-28 - Docs physics network-ownership.md`, `Roblox/docs/Videos/2026-10-28 - Docs physics assemblies.md`. Live-check thresholds in Creator Docs.

## Output
```
PHYSICS REPORT <place> <date>
Census before: parts 41,200 | unanchored 3,900 (9.5%) | assemblies 1,120 | moving 85 | CanTouch 22,000 | constraints 410
Physics task (MicroProfiler, <scenario>): 7.8 ms -> 3.1 ms   [measured | untested]
Changes: anchored decor (2,600) | CanTouch off (18,000) | Adaptive stepping | debris cleanup 30 s
Gameplay re-test: vehicles ok / pushables ok / ragdoll ok
```

## Acceptance checks
- [ ] Before and after census saved; changes listed with counts.
- [ ] Physics time before/after quoted from the profiler or labelled `untested`.
- [ ] Every CanTouch/CanQuery change was checked against scripts that use Touched, raycasts or overlap queries.
- [ ] Gameplay that relies on physical props re-tested.
- [ ] Executed check: `physics_census.luau` passes the pack's luau-check run (stylua, selene, luau-lsp).

## Pitfalls
Anchoring things players push or ride. Turning CanQuery off on parts a raycast must hit. Believing that fewer parts equals less physics (assemblies and constraints dominate). Leaving jittering parts that never sleep. Setting network ownership to nil for everything. Forgetting debris from destruction systems.

## Related
`game-optimizer`, `lag-hunter`, `collision-fidelity-tuner`, `anchor-checker`, `server-tick-analyzer`.
