---
name: server-tick-analyzer
description: "Diagnose a slow server heartbeat: sample Heartbeat deltas, summarise average FPS, p95/p99, worst frame and stall runs against the 16.67 ms budget, then split the cost into scripts, physics and replication with the Server Jobs tab and server MicroProfiler. Use when server FPS is under 60, players rubber-band, or the dashboard shows slow server heartbeat."
category: perf
tags: server, heartbeat, tick, frame time, stall, 60 fps, microprofiler, server jobs, rubber banding, compute
kb: Roblox/roblox-kb/optimization-and-streaming.md, Roblox/roblox-kb/scripting-and-performance.md, Roblox/roblox-kb/analytics-metrics.md, Roblox/roblox-kb/testing-debugging-and-qa.md
related: lag-hunter, script-profiler, physics-load-reducer, network-traffic-auditor, npc-cost-reducer, datastore-throttle-auditor, game-optimizer
---

# server-tick-analyzer

The server's Heartbeat is capped at 60 per second (16.67 ms per frame). Anything lower means the server is behind, and every player feels it. This skill measures the tick in a way that separates steady slowness from spikes and stalls, then attributes the time.

## When to use
Rubber-banding with good ping, dashboard server heartbeat or server CPU time over 16 ms, lag that scales with players or NPCs. Not for: client-side stutter (`mobile-perf-tester`, `cpu-vs-gpu-diagnoser`) or symptom triage across client/server/network (`lag-hunter` comes first if you do not know the side).

## Inputs (max 2)
1. The scenario (player count, NPCs, event). 2. Whether you can run a Studio server session with load, or only read the live dashboard (default: both).

## Procedure
1. Live numbers first: Creator Hub Performance dashboard (server heartbeat P10/P50/P90, server CPU time, server memory); charts need at least 100 DAU. Developer Console > Server Jobs tab shows Steps Per Sec (60 is the cap). If these are healthy, stop.
2. Sample the tick: run `scripts/tick_sampler.luau` on the Server datamodel for 30 s in the loaded scenario and once idle. It prints frames, average FPS, p95, p99, worst, share over 16.7 ms and the longest run over 33 ms, plus raw deltas for `TickStats.summarise(deltas)` (`scripts/TickStats.luau`). Verdicts: ok, slow-average (under 58 FPS average), stalls (3 or more consecutive frames over 33 ms), spiky (p99 over 33 ms), too-few-samples.
3. Read the verdict:
   - slow-average: steady cost every frame; capture the server MicroProfiler and read the biggest tasks. Orange (Jobs over Render) points to scripts, physics, animation: use `script-profiler` and `physics-load-reducer`.
   - stalls: one thing blocks for many frames (a big loop, a synchronous setup, a heavy `GetDescendants`, a load of assets); find it by pausing the profiler on the longest frame.
   - spiky: periodic work (autosave bursts: `datastore-throttle-auditor`; wave spawns; replication bursts: `network-traffic-auditor`).
4. Attribute: scripts (Script Profiler server view), physics (`physics_census`), replication/network (Network Stats, MicroProfiler network events), NPC loops (`npc-cost-reducer`), animation (`animation-cost-reducer`).
5. If the heartbeat stays low after optimisation, the docs mention reserving more CPU with Extended Services for Compute (a spend decision: the owner decides, never the agent).
6. Memory side: server memory is about 6.25 GiB + 100 MiB per max player; keep under 50 percent and plan on peak (`memory-budget-planner`).
7. Re-sample the same scenario after each fix and keep a table of verdicts per build.

## Studio MCP path
`list_roblox_studios` -> `start_stop_play` -> `execute_luau` (Server) `scripts/tick_sampler.luau` (30 s; wait for it) -> `get_console_output` for the `[tick]` lines -> paste deltas into `TickStats.summarise` under Lune or `execute_luau`. Studio server timing is Studio-only; the dashboard is the truth for live servers.

## Fallback
No Studio: read the dashboard and the Server Jobs tab values from the owner; run `TickStats` on any delta list. Production behaviour under real load is `untested` without live data.

## Evidence
Official: `Roblox/docs/Videos/2026-10-28 - Docs performance-optimization identify.md` (server heartbeat capped at 60 FPS, lower suggests a problem; Server Jobs tab Steps Per Sec; frame budget 16.67 ms; memory formula; Extended Services for Compute), `Roblox/docs/Videos/2026-10-28 - Docs production analytics performance.md` (server CPU under 16 ms for 60 FPS; P90 59 FPS and P10 40 FPS examples; 100 DAU minimum), `Roblox/docs/Videos/2026-10-28 - Docs performance-optimization microprofiler task-scheduler.md`. `Roblox/roblox-kb/optimization-and-streaming.md`: judge spikes and consistency, not the average; colour reading of MicroProfiler bars. The 33 ms stall line and the run length of 3 are this skill's heuristics.

## Output
```
SERVER TICK <build> <scenario> <date> (30 s, 1,790 frames)
avg 52.3 FPS | p95 29 ms | p99 61 ms | worst 240 ms | over 16.7 ms: 38% | longest stall run 5
Verdict: stalls. Longest frame: Spawner.SpawnWave (186 ms, synchronous Clone x400)
Fix: spread over 20 frames -> re-run: avg 59.8 FPS, p99 22 ms (verdict ok)
```

## Acceptance checks
- [ ] Sampled under load and idle; both verdicts reported.
- [ ] The verdict comes from `TickStats` output quoted in the report.
- [ ] The dominant task is named from a profiler capture or labelled `untested`.
- [ ] Re-sample after the fix in the same scenario.
- [ ] Executed check: `TickStats.test.luau` passes under Lune; `tick_sampler.luau` passes luau-check.

## Pitfalls
Judging by average FPS when the problem is a periodic stall. Sampling an empty server. Treating Studio timing as production. Buying compute before fixing scripts. Letting the sampler stay in a shipping place. Ignoring server memory growth.

## Related
`lag-hunter`, `script-profiler`, `physics-load-reducer`, `network-traffic-auditor`, `npc-cost-reducer`, `datastore-throttle-auditor`.
