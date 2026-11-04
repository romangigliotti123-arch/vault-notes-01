---
name: script-profiler
description: "Find and fix Luau hot spots: capture a Script Profiler / MicroProfiler session, rank scripts and functions by cost, read the usual culprits (per-frame loops, GetDescendants, FindFirstChild storms, per-part scripts, string building), then prove each rewrite with a micro-benchmark and a before/after capture. Use when a profiler shows script time or a script feels expensive."
category: perf
tags: profiler, microprofiler, script profiler, luau, hot spot, benchmark, heartbeat, loop, cpu, optimise code
kb: Roblox/roblox-kb/optimization-and-streaming.md, Roblox/roblox-kb/scripting-and-performance.md, Roblox/roblox-kb/code-architecture-and-frameworks.md, Roblox/roblox-kb/luau-language-and-types.md
related: game-optimizer, lag-hunter, heartbeat-loop-auditor, object-pool-builder, collection-tag-wiring, actor-parallel-converter, connection-leak-auditor, rbx-code-rate
---

# script-profiler

Measure where Luau time goes, change one thing, measure again. The benchmark helper compares two implementations in isolation; the real game decides whether the change mattered. Whole-game triage is `game-optimizer`; a symptom without a script is `lag-hunter`.

## When to use
Script Profiler/MicroProfiler shows a script near the top, a system "feels heavy", or you are choosing between two implementations of a hot function. Not for: rendering or physics cost (`render-cost-auditor`, `physics-load-reducer`).

## Inputs (max 2)
1. The scenario that is slow (a place, a player count, an action). 2. The suspect script, if known (default: find it from the capture).

## Procedure
1. Capture: Script Profiler (Developer Console F9 > Server/Client scripts, or the Script Profiler window in Studio) for 30-60 s of the slow scenario; MicroProfiler (Ctrl+Alt+F6, pause with Ctrl+P) to tell steady cost from spikes. Record the top 5 scripts/functions by time and the frame time. MCP cannot drive these windows: ask the owner for the numbers or say untested.
2. Read the hot script. Look for the usual causes:
   - Work every frame (`Heartbeat`/`RenderStepped`/`while task.wait()` with short waits) that could be event-driven or throttled.
   - Scanning: `workspace:GetDescendants()`, `GetChildren()` in loops, repeated `FindFirstChild`/`WaitForChild` chains instead of cached references.
   - One script per part (hundreds of identical Scripts) instead of one script driving a CollectionService tag.
   - Iterating all players for every event; O(n^2) loops over NPCs.
   - String concatenation in loops; creating tables/closures every frame; unpooled `Instance.new`/`Destroy` churn.
   - Unbounded caches (leaks) and signal connections never disconnected (`connection-leak-auditor`).
   - Expensive calls in hot paths: raycasts every frame per NPC, `Region3`/overlap queries with big radii, pathfinding spam.
3. Hypothesis: "Replacing X with Y cuts this function from A to B microseconds per call". Write both versions as small functions with the same inputs.
4. Benchmark: copy `scripts/bench.luau` next to your test script (or inline it) and run `print(bench.compare("old", fnOld, "new", fnNew, 20000))` in Studio's command bar/Lune. It runs a warm-up, then 7 timed batches and reports the median microseconds per call, the ratio, and `NOISY` when the spread is over 20 percent (then increase iterations). Benchmarks answer "is Y faster in isolation", not "does the game feel better".
5. Apply the change in the real script. Keep behaviour identical: run the scenario and the core loop (`playtest-bot-writer`).
6. Re-capture with the profiler for the same scenario and duration; compare the function's share and the frame time. Keep the change only if the capture improved.
7. Options for the biggest remaining costs: throttle (run every N frames or on change), batch, cache, event-drive, pool objects, CollectionService tags, or move CPU-heavy independent work to Actors with parallel Luau (`actor-parallel-converter`; only for work that does not touch shared state each step).

## Studio MCP path
`script_read` / `script_grep` (find the loops: `Heartbeat|RenderStepped|while true|GetDescendants`) -> `multi_edit` rewrite -> `execute_luau` to run the benchmark (Edit or Server) and return the string -> `start_stop_play` -> `get_console_output`. Profiler captures are manual.

## Fallback
Lune (`lune run`) for pure-function benchmarks (no Roblox APIs); Rojo files for edits; profiler numbers from the owner. Claims about frame time without captures are `untested`.

## Evidence
`Roblox/roblox-kb/optimization-and-streaming.md` (measure before optimising; Script Profiler and MicroProfiler roles), `Roblox/roblox-kb/scripting-and-performance.md`, `Roblox/roblox-kb/code-architecture-and-frameworks.md`, `Roblox/roblox-kb/luau-language-and-types.md`. API performance characteristics change between engine versions; confirm in Creator Docs (`kbq.py docs "parallel luau"`).

## Output
```
SCRIPT PROFILE <scenario>
Top costs before: 1. Systems/Spawner Heartbeat 3.1 ms ...   frame avg ...
Change: <what>  micro-benchmark: old 41.2 us vs new 6.8 us (6.1x, noise 4%)
After: Spawner 0.4 ms, frame avg ...   Verdict: kept|reverted
```

## Acceptance checks
- [ ] A before capture exists (numbers or labelled untested) for the same scenario as the after.
- [ ] The benchmark output is quoted and not NOISY (or iterations raised).
- [ ] Behaviour verified unchanged by a playtest/bot run.
- [ ] Reverted changes that did not improve the capture.
- [ ] `bench.luau` passes the pack's luau-check run (stylua, selene, luau-lsp).

## Pitfalls
Optimising a function that is not on the profile. Micro-benchmarks that the compiler optimises away (use the result). Throttling something gameplay needs every frame. Parallel Luau on code that shares state. Leaving debug prints in hot paths.

## Related
`game-optimizer`, `lag-hunter`, `heartbeat-loop-auditor`, `object-pool-builder`, `collection-tag-wiring`, `actor-parallel-converter`.
