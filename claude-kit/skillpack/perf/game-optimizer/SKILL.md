---
name: game-optimizer
description: "Measure, rank and fix a Roblox game's performance (frame time, memory, network, join time) in measure-first order: census the place, profile on the right device, pick the highest-impact fixes (StreamingEnabled, collision, effects, loops, remotes), apply them one at a time and prove each with before/after numbers. Use when a game lags, takes long to load, or before a launch."
category: perf
tags: optimize, optimise, performance, lag, fps, memory, streaming, microprofiler, mobile, join time, parts
kb: Roblox/roblox-kb/optimization-and-streaming.md, Roblox/roblox-kb/scripting-and-performance.md, Roblox/roblox-kb/testing-debugging-and-qa.md, Roblox/roblox-kb/cross-platform-and-console.md, Roblox/roblox-kb/_tools/CHECKLIST-launch.md
related: lag-hunter, script-profiler, streaming-enabler, part-count-auditor, render-cost-auditor, network-traffic-auditor, mobile-perf-tester, model-cleaner
---

# game-optimizer

The coordinator. It decides WHAT to optimise by measurement and hands single problems to specialists (`lag-hunter` for a symptom, `script-profiler` for Luau hot spots, `streaming-enabler`, `network-traffic-auditor`, `model-cleaner`). Rule one from the vault: measure before optimising, and judge on a low-end real client, because Studio skews the numbers.

## When to use
"My game lags / is slow to load / crashes on phones", before launch, after a big content update. Not for: gameplay bugs, or single-script micro-optimisation (`script-profiler`).

## Inputs (max 3)
1. The symptom and where (mobile? one area? server? join?). 2. Target devices (default: low-end phone first). 3. Studio MCP or Rojo project available? (default: detect, see below).

## Procedure
1. Baseline census: run `scripts/scan_place.luau` (read-only). Save the output as `perf/baseline.txt`. Look at: StreamingEnabled, unanchored parts, CanTouch/CanQuery counts, PreciseConvexDecomposition, shadow-casting lights, particle emitters, largest models.
2. Measure on the symptom's device, not Studio alone: Performance Summary (Ctrl+Shift+F5) for FPS/frame time, MicroProfiler (Ctrl+Alt+F6; Ctrl+P pauses) to separate steady cost from spikes, Developer Console (F9, Memory tab) for memory, Script Profiler for Luau. Record: average frame time, worst spikes, memory by category, time-to-first-playable, server heartbeat. If you cannot run them (headless), say "census only: numbers are counts, not times".
3. Classify the bottleneck: CPU-script (long Luau frames), CPU-physics (unanchored parts, constraints, touch events), render/GPU (shadows, transparency, effects, part count in view), memory (textures, meshes, streaming off), network (remote/replication volume), server (slow heartbeat). Use `cpu-vs-gpu-diagnoser` if unclear.
4. Fix in impact order, ONE change at a time, re-measuring after each:
   a. Streaming: turn on `StreamingEnabled` if the map is big (highest-impact cut to client memory and join time); set Persistent/Atomic only on models that break; never desync streamed instances on the client. -> `streaming-enabler`.
   b. Scenery collision and queries: Box/Hull fidelity, CanCollide/CanTouch/CanQuery off on non-interactive parts. -> `collision-fidelity-tuner`.
   c. Effects: cap emitters, trails, beams, shadow-casting lights; distance-fade. -> `render-cost-auditor`, `effects-budget-setter`.
   d. Scripts: replace per-frame loops with events or throttled timers, pool spawned instances, avoid per-part scripts (use CollectionService tags). -> `heartbeat-loop-auditor`, `script-profiler`.
   e. Network: batch or rate-limit remotes, send identifiers not tables. -> `network-traffic-auditor`.
   f. Assets: textures/meshes over budget. -> `texture-budget-checker`.
5. After each fix record before/after on the same scenario; keep a change only if the number improved and nothing broke (playtest the core loop).
6. Stop when the target is met (e.g. stable frame rate on the target device) - do not polish past it.
7. Write the report and the regression guard: the census command and the numbers to re-check each release.

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `execute_luau` (Edit) with `scripts/scan_place.luau` -> `start_stop_play` -> `get_console_output` -> `execute_luau` (Server) with `lag-hunter/scripts/remote_probe.luau` for remote traffic -> property edits by `execute_luau` (record each in the report) -> `screen_capture` to confirm visuals unchanged. Profiler UIs cannot be driven by MCP: ask the owner to read the MicroProfiler/Performance Summary values, or say they are `untested`.

## Fallback
Command bar: paste `scan_place.luau`. Rojo: work on files (scripts, streaming settings are place settings: tell the owner where to click). All time-based claims are `untested` without profiler readings.

## Evidence
`Roblox/roblox-kb/optimization-and-streaming.md` (measure first; real low-end client; StreamingEnabled highest impact; collision fidelity order; disable collision/touch/query on scenery), `Roblox/roblox-kb/scripting-and-performance.md`, `Roblox/roblox-kb/testing-debugging-and-qa.md`, `Roblox/roblox-kb/_tools/CHECKLIST-launch.md`. Limits and API behaviour change: confirm in Creator Docs (`kbq.py docs "StreamingEnabled"`).

## Output
```
OPTIMISATION REPORT <game> <date>
Symptom/target: ...      Device(s): ...
Baseline: frame ms avg/p95 ...  memory MB ...  join s ...  [source: profiler | census only]
Changes (in order): 1. <change> | before -> after | kept/reverted
Remaining risks / not measured: ...
Regression guard: re-run scan_place.luau; keep: <numbers>
```

## Acceptance checks
- [ ] Baseline recorded before any change; each kept change has a before/after on the same scenario.
- [ ] Measurements named by tool and device; census-only claims are labelled counts.
- [ ] Core loop playtested after the last change (or `untested`).
- [ ] No visual regression (screenshot compare) for asset/collision/effect changes.
- [ ] Reverted anything that did not help.

## Pitfalls
Optimising by feel. Testing only on the dev PC. Turning on streaming late and breaking client scripts that assume everything exists (use `WaitForChild`, StreamingIntegrity, Persistent models). Removing collision that gameplay needs. Changing five things at once. Over-optimising past the target.

## Related
`lag-hunter`, `script-profiler`, `streaming-enabler`, `part-count-auditor`, `network-traffic-auditor`, `model-cleaner`, `rbx-perf` (kit skill).
