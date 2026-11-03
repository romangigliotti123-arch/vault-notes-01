---
name: cpu-vs-gpu-diagnoser
description: "Decide whether a slow frame is GPU-bound, CPU simulation-bound (scripts, physics, animation) or CPU render-prep-bound by reading a paused MicroProfiler frame: frame ms, Jobs, Render and GPU wait, with the bar colours, then hand off to the right skill. Use first when a frame rate drop has no known cause."
category: perf
tags: microprofiler, cpu, gpu, bound, bottleneck, frame time, gpu wait, jobs, render, diagnosis
kb: Roblox/roblox-kb/optimization-and-streaming.md, Roblox/roblox-kb/testing-debugging-and-qa.md, Roblox/roblox-kb/scripting-and-performance.md
related: game-optimizer, render-cost-auditor, script-profiler, physics-load-reducer, part-count-auditor, mobile-perf-tester, server-tick-analyzer
---

# cpu-vs-gpu-diagnoser

Optimising the wrong side wastes days: cutting particles does nothing for a script-bound frame, and rewriting scripts does nothing for a GPU-bound one. This skill reads four numbers off a paused MicroProfiler frame and returns one answer plus the next skill.

## When to use
Low FPS with no known cause, before spending time on any fix, or when a fix did not help. Not for: server-side slowness (`server-tick-analyzer`), steady memory problems (`memory-budget-planner`) or a symptom triage across client/server/network (`lag-hunter`).

## Inputs (max 2)
1. The device and scene (use the real target device; a dev PC hides GPU limits, and Studio skews stats). 2. Frame goal: 16.67 ms (60 FPS) or 33.33 ms (30 FPS on phones).

## Procedure
1. Set the client up honestly: Graphics Mode manual and max quality to remove the frame-rate manager's effects, on the real device or a client outside Studio. Reproduce the slow scene and stay in it.
2. Capture: MicroProfiler (Ctrl+Alt+F6; Cmd+Opt+F6 on Mac), pause on a slow frame with Ctrl+P. Judge spikes against steady cost: pause on both a typical frame and a spike, they can differ. Note: total frame ms; Jobs (script, physics, animation work on the main thread); Render prep; GPU wait.
3. Run the rule: `BoundDiagnosis.diagnose({frameMs=, jobsMs=, renderMs=, gpuWaitMs=}, goalMs)` from `scripts/BoundDiagnosis.luau`.
   - Frame inside the goal: nothing to fix here. Stop.
   - GPU wait over 2.5 ms (red): GPU-bound; scene complexity, texture size, VFX -> `render-cost-auditor`, `texture-budget-checker`, `effects-budget-setter`.
   - Jobs larger than Render (orange): simulation-bound: scripts, physics, animation -> `script-profiler`, `physics-load-reducer`, `animation-cost-reducer`.
   - Render larger than Jobs (blue): render-prep-bound: too many objects in view, movement, lighting -> `part-count-auditor`, `render-cost-auditor`.
   Act on colour only when the frame goal is missed (the guide's own caveat).
4. Cross-check in the Developer Console or Performance Summary: if lowering graphics quality raises FPS a lot, it is GPU or render prep; if it changes nothing, it is simulation.
5. Drill down inside the winning category in the MicroProfiler (a parent bar cannot be shorter than its children) and name the biggest child task, then follow the handoff skill.
6. After a fix, capture the same scene again and use `BoundDiagnosis.improvement(before, after)` to quote the percentage. If the bound has switched sides (a common outcome), run the diagnosis again.

## Studio MCP path
The profiler cannot be driven through MCP. Use `execute_luau` only for supporting counts (`part-count-auditor`, `render_census`), and `get_console_output` to confirm nothing else is running. The four numbers are read by the owner or from a saved dump; without them the result is `untested`.

## Fallback
Ask the owner for a screenshot or typed values of the paused frame; or toggle graphics quality in-game and compare FPS (coarse). The diagnosis function runs under Lune for any numbers supplied.

## Evidence
`Roblox/roblox-kb/optimization-and-streaming.md`: profile with MicroProfiler and classify the bar colour (orange Jobs over Render: scripts, physics, animation; blue Render over Jobs: object density, movement, lighting; red GPU wait over 2.5 ms: complexity, texture size, VFX; act on colour only when the frame goal is missed); parent bars cannot be shorter than children; judge spikes and consistency; Studio skews stats; frame budgets 16.67 and 33.33 ms. Official: `Roblox/docs/Videos/2026-10-28 - Docs performance-optimization identify.md` (frame budget 16.67 ms; evaluate on a client with manual graphics mode), `Roblox/docs/Videos/2026-10-28 - Docs performance-optimization microprofiler.md`, `Roblox/docs/Videos/2026-10-28 - Docs performance-optimization microprofiler use-microprofiler.md`, `Roblox/docs/Videos/2026-10-28 - Docs performance-optimization microprofiler tag-table.md`. Live-check the tag names: they change between engine versions.

## Output
```
BOUND DIAGNOSIS <scene> <device> <date>  goal 33.33 ms
Frame 41 ms | Jobs 14 | Render 9 | GPU wait 6.2 -> GPU-bound (red)
Next: render-cost-auditor (shadow lights 64, partial-transparent 3,200), effects-budget-setter
After fix: frame 29 ms (-29%), bound now: cpu-simulation (orange) -> script-profiler next
```

## Acceptance checks
- [ ] The four numbers came from a paused profiler frame on a named device (not guessed).
- [ ] A typical frame and a spike frame were both checked, or only one is stated.
- [ ] The diagnosis and the handoff skill are named; the colour rule is quoted.
- [ ] A before/after capture shows whether the bound changed.
- [ ] Executed check: `BoundDiagnosis.test.luau` (5 tests) passes under Lune; scripts pass luau-check.

## Pitfalls
Reading numbers in Studio and applying them to phones. Acting on colour when the frame already meets the goal. Treating a single pause as the whole story. Ignoring that a GPU fix can expose a CPU limit. Optimising the average when the problem is a spike frame.

## Related
`game-optimizer`, `render-cost-auditor`, `script-profiler`, `physics-load-reducer`, `part-count-auditor`, `mobile-perf-tester`.
