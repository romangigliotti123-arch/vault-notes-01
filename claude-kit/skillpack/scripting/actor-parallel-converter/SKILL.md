---
name: actor-parallel-converter
description: "Move one hot, independent loop onto Actors with parallel Luau: measure first, decide with a plan function, split the data, compute in Actors, merge results in order back on the main thread. Use only after a profile shows a pure-compute loop eating the frame; most loops should stay serial."
category: scripting
tags: actor, parallel luau, desynchronize, synchronize, bindtomessageparallel, performance, threads, compute, npc, raycast
kb: Roblox/roblox-kb/scripting-and-performance.md, Roblox/roblox-kb/luau-language-and-types.md, Roblox/roblox-kb/optimization-and-streaming.md
related: script-profiler, lag-hunter, game-optimizer, object-pool-builder, rbx-perf
---

# actor-parallel-converter

Parallel Luau runs code on several threads, but only inside Actors and only for code that does not touch shared state. The usual best answer to a slow loop is to do less work (cache, spread across frames, use events); parallel is for the loop that is still too big after that. Measuring is `script-profiler`; this converts one loop.

## When to use
A profile (MicroProfiler or `script-profiler`) shows one loop of many independent items (AI sensing, distance or visibility checks, raycasts, pure maths) dominating a frame. Not for: loops that write the DataModel on every item, order-dependent logic, or anything under a few hundred items.

## Inputs (max 2)
1. The loop (script and line) and its per-item cost in ms from a measurement. 2. Frame budget (default 16 ms client, server budget from the profile).

## Procedure
1. Measure the loop: item count and per-item time. Do not proceed without the numbers.
2. `ParallelBatch.plan(itemCount, perItemMs, frameBudgetMs, maxWorkers, overheadMs)` (`scripts/ParallelBatch.luau`) estimates whether splitting pays after message overhead. If it says serial, stop and reduce work instead. `overheadMs` must be measured on your server; the default is a placeholder.
3. Make the work a pure function `compute(item) -> result`: reads only its argument and parallel-safe APIs, no yields, no writes to instances, no shared upvalue tables. Check each API's thread-safety tier in the docs; most members default to unsafe in parallel.
4. Create N Actors (start with the plan's worker count; the vault's only guidance is an indie 32 to 64 Actors figure and an indie client cap of 3 parallel threads, both unverified, so live-check and benchmark). Put a copy of `scripts/ParallelWorker.luau` inside each Actor with `compute` filled in.
5. On the main thread build the dispatcher: `ActorDispatcher.new(actors, "Work", require(path.to.ParallelBatch))` (an optional fourth `io` argument injects the event factory, wait and clock for tests) and call `dispatcher:Run(items, timeoutSeconds)`. It partitions the items, sends one chunk per Actor with `SendMessage`, waits (bounded) and returns merged results in item order. Messages deep-copy tables, so send plain data (positions, ids), not Instances you will write.
6. Apply results on the main thread in one pass (the worker fires its completion after `task.synchronize()`; never write to instances from the parallel phase).
7. Compare: same inputs must give identical results to the serial loop (run both on a fixed sample and diff), then re-measure the frame. Keep the serial path behind a flag.
8. Test the pure parts: `lune run ../skillpack/scripting/actor-parallel-converter/scripts/tests/ParallelBatch.test.luau` from the kit `systems` folder.

## Studio MCP path
`list_roblox_studios` -> `script_read` the loop -> `multi_edit` to add Actors, worker and dispatcher (or `execute_luau` to build Actors under a folder) -> `start_stop_play` -> `get_console_output` for timings and the serial-versus-parallel diff -> MicroProfiler for the frame (manual).

## Fallback
Pure tests under Lune pass without Studio, including the dispatcher's split, collect, order and timeout logic against fake Actors (`lune run ../skillpack/scripting/actor-parallel-converter/scripts/tests/ActorDispatcher.test.luau`). Real Actor messaging and the worker template need a running place and are static-checked only: report them `untested` until run.

## Evidence
`Roblox/roblox-kb/scripting-and-performance.md`: heavy compute can go in Actors using desynchronize/synchronize; keep parallel code free of unsafe writes and shared state; most API members are not parallel-safe by default. `Roblox/roblox-kb/luau-language-and-types.md`: do not rely on the order in which parallel scripts run; Actor count and client thread cap are indie figures to verify; new parallel simulation and animation binds are listed as pending in the 2026-10 notes (live-check availability).

## Output
Worker script, dispatcher call site, the plan numbers, serial-versus-parallel diff result and before/after frame times.

## Acceptance checks
- [ ] Executed: `ParallelBatch.plan` output quoted; Lune tests pass (`7 passed, 0 failed` and dispatcher `5 passed, 0 failed`).
- [ ] `compute` is pure; no instance writes happen before `task.synchronize()`.
- [ ] Parallel results equal serial results on a fixed sample (diff quoted) or marked untested.
- [ ] Results merge in item order regardless of Actor finish order.
- [ ] Frame time measured before and after, or marked untested.

## Pitfalls
Parallelising a loop that was cheap (overhead exceeds the gain). Sending Instances and expecting shared mutation. Assuming execution order. Creating Actors per item. Leaving the timeout out (a failed Actor hangs the caller).

## Related
`script-profiler`, `lag-hunter`, `game-optimizer`, `object-pool-builder`.
