---
name: instance-leak-finder
description: "Find instance, connection or memory counts that grow over time: sample whole-DataModel instance counts per class on server and client, fit the trend, diff class counts, then trace the growth to the script that creates but never cleans up, using Scene Analysis and Luau heap snapshots. Use when lag or memory worsens the longer a server or session runs."
category: perf
tags: leak, memory leak, instance count, unparented, heap snapshot, growth, cleanup, destroy, connections, long sessions
kb: Roblox/roblox-kb/optimization-and-streaming.md, Roblox/roblox-kb/scripting-and-performance.md, Roblox/roblox-kb/testing-debugging-and-qa.md, Roblox/roblox-kb/common-mistakes.md
related: lag-hunter, memory-budget-planner, connection-leak-auditor, script-profiler, mobile-perf-tester, object-pool-builder
---

# instance-leak-finder

"It gets laggier the longer it runs" is a growth problem, not a speed problem. This skill measures the growth, fits a trend, names the classes that grew, and walks from the class to the cause, then proves the fix flattens the curve.

## When to use
Servers degrade over hours, crash rates rise with session length, memory climbs in a soak test, or the instance count in Scene Analysis keeps going up. Not for: steady high memory (`memory-budget-planner`), a single slow script (`script-profiler`), or connection leaks as a pattern audit (`connection-leak-auditor`, which complements this).

## Inputs (max 2)
1. Where it grows (server, client, or both) and the repro length. 2. A steady-state scenario: fixed players, no wave in progress, so legitimate spawns do not look like leaks.

## Procedure
1. Sample: run `scripts/leak_watch.luau` (default 10 samples every 30 s) on the Server datamodel during a playtest and again on the client. It prints the total instance series and the classes that grew most between first and last sample.
2. Judge the trend with `scripts/LeakTrend.luau`: `LeakTrend.analyze(series, 30)` returns slope per minute, R squared and a verdict: growing (slope at least 1 per minute and R squared at least 0.8 and last above first), noisy-growth, flat, shrinking, or too-few-samples. Use `LeakTrend.diff(before, after)` on two class-count tables for a ranked list. A sawtooth that returns to baseline is not a leak. Stop here if the verdict is flat after a long enough run (10 samples or more).
3. Locate: for the top growing class, ask what creates it. `script_grep` for `Instance.new("<Class>")`, `:Clone()` and the class name; open Scene Analysis (Window > Performance Summary) Instance Composition and Unparented Instances views, and Developer Console > Luau heap: take two snapshots minutes apart and compare, reading Graph view paths (registry, upvalue, env, array) to see what keeps objects alive. In the Memory tool watch PlaceScriptMemory.
4. Typical causes to check: instances created per event and never destroyed (effects, sounds, hit markers, billboards); `Destroy()` missing on removed players' objects; connections holding references (`PlayerRemoving` cleanup absent); tables that only ever grow (caches keyed by player or instance); animation tracks and sounds kept alive after the model is destroyed; parts parked in nil (unparented but referenced); `Debris` not used for fragments.
5. Fix at the cause: destroy on despawn and on `PlayerRemoving`; disconnect connections; use a Janitor/Maid or pool (`object-pool-builder`); bound every cache (size or time); remove references to animations and sounds so they unload.
6. Prove: rerun step 1-2 on the same scenario; the verdict must move to flat (or slope under the threshold). For server crashes, watch the dashboard's server out-of-memory chart by place version after release; the crash viewer's treemap shows what dominated at crash time.

## Studio MCP path
`list_roblox_studios` -> `start_stop_play` -> `execute_luau` (Server) `scripts/leak_watch.luau` (it waits, so allow the full duration) -> `execute_luau` (Client) the same -> `script_grep` for creators of the growing class -> `multi_edit` the cleanup -> repeat. Heap snapshots and Scene Analysis windows are manual (ask the owner, or `untested`).

## Fallback
Command bar in a Play session. Without a long enough session the trend verdict is `too-few-samples`: say so. Studio server+client in one process mixes both sides; run each side's script separately to attribute.

## Evidence
Official: `Roblox/docs/Videos/2026-10-28 - Docs studio optimization memory-usage.md` (take multiple Luau heap snapshots over time and compare; Unique References / Unparented Instances views for leaked instances; Graph view reference paths), `Roblox/docs/Videos/2026-10-28 - Docs performance-optimization scene-analysis.md` (Instance Composition; animation assets are a common leak; pair Unparented Instances with the heap tool), `Roblox/docs/Videos/2026-10-28 - Docs production analytics crashes.md` (server memory snapshots; filter by place version). `Roblox/roblox-kb/optimization-and-streaming.md` (Luau heap snapshot diffs for leaks; Debris cleanup). The slope and R squared thresholds are heuristics: gameplay can legitimately grow counts.

## Output
```
LEAK REPORT <place> <side> <date>   10 samples x 30 s
Series: 61,200 ... 74,800 (+13,600) | slope +2,800/min R2 0.99 -> growing
Top classes: +9,100 Sound, +3,900 Attachment, +600 Beam
Cause: HitEffects.luau:58 creates Sound per hit, never destroyed. Fix: Debris:AddItem(sound, 3).
After: series flat (slope +2/min). Remaining risk: client not sampled -> untested
```

## Acceptance checks
- [ ] At least 10 samples at a fixed interval in a steady scenario; verdict from `LeakTrend`.
- [ ] Growth traced to a named script and line, not just a class.
- [ ] After the fix, the same run is flat; the numbers are quoted.
- [ ] Both server and client sampled, or the missing side is listed as not checked.
- [ ] Executed check: `LeakTrend.test.luau` (6 tests) passes under Lune; `leak_watch.luau` passes luau-check.

## Pitfalls
Calling normal gameplay growth a leak (waves, building). Sampling a too-short window. Fixing the symptom class (Attachment) instead of the creator. Destroying instances that scripts still reference (errors) instead of fixing the owner. Ignoring Luau-side tables, which do not show up as instances. Fixing the server and forgetting the client.

## Related
`lag-hunter`, `memory-budget-planner`, `connection-leak-auditor`, `script-profiler`, `object-pool-builder`.
