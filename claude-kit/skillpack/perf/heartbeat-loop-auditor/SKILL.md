---
name: heartbeat-loop-auditor
description: "Statically scan every script for per-frame callbacks (Heartbeat, RenderStepped, Stepped), tight wait loops and expensive calls inside them, then replace the worst with events, throttled timers or tagged systems, confirming each win in the Script Profiler. Use when the profiler shows script time, or before adding another per-frame system."
category: perf
tags: heartbeat, renderstepped, loop, per-frame, task.wait, events, throttle, getdescendants, scripts, audit
kb: Roblox/roblox-kb/optimization-and-streaming.md, Roblox/roblox-kb/scripting-and-performance.md, Roblox/roblox-kb/code-architecture-and-frameworks.md
related: script-profiler, game-optimizer, lag-hunter, object-pool-builder, collection-tag-wiring, connection-leak-auditor, npc-cost-reducer
---

# heartbeat-loop-auditor

Per-frame code is the main script cost in most games. This skill finds candidate loops by reading source (cheap, covers every script) and leaves the proof to the profiler: it narrows 300 scripts to the ten worth profiling, then drives the rewrites.

## When to use
Script time is high in the Script Profiler/MicroProfiler but no script is named, a codebase grew organically, or a review before shipping. Not for: measuring one known hot function (`script-profiler`), leaked connections (`connection-leak-auditor`) or NPC update scheduling (`npc-cost-reducer`).

## Inputs (max 2)
1. The scripts to scan (default: everything in the place or the Rojo `src`). 2. Whether anything runs per frame by design (camera, input prediction): list it so it is not "fixed".

## Procedure
1. Scan. In Studio: put `scripts/LoopScan.luau` in ServerStorage as a ModuleScript named LoopScan and run `scripts/loop_scan_studio.luau`. With Rojo files: run `LoopScan.scan(source)` on each file's text under Lune. The scan reports `per-frame-callback`, `tight-wait-loop` (waits of 0.05 s or less), `legacy-wait` (`wait()`), `expensive-in-frame-loop` and `expensive-in-wait-loop` (GetDescendants, GetChildren, GetPlayers, FindFirstChild, WaitForChild, raycasts, overlap queries, Instance.new, Clone). Indentation decides where a callback ends, so treat results as candidates. Stop if no script is found.
2. Rank scripts by findings, then confirm in the Script Profiler (`script-profiler`) which candidates have real cost. Skip candidates that cost nothing.
3. Choose the replacement per finding:
   - State that changes rarely: an event (`Changed`, `GetPropertyChangedSignal`, `AttributeChanged`, a BindableEvent) instead of polling.
   - Work that needs a timer: `task.wait(interval)` with an interval matching the need (not every frame), or `task.delay` chains; replace `wait()` with `task.wait`.
   - Per-object scripts: one script iterating a CollectionService tag.
   - Heavy lookups: cache results in a variable or table once; do not `GetDescendants` or `FindFirstChild` each frame; disconnect connections you no longer need.
   - Long work: slice it across frames (docs example: 5 ms per frame with `task.wait` rather than one 100 ms block that would cap a per-frame task at 10 FPS).
   - Independent compute: Parallel Luau with Actors only for work that does not touch the DataModel (serial 72 deer about 50 ms vs about 16 ms parallel, indie test).
   - RenderStepped only for what must run after input and before rendering (camera, character visuals).
4. Rewrite one script at a time, keeping behaviour identical; run the core loop (`playtest-bot-writer`) after each.
5. Re-profile the same scenario; keep a rewrite only if script time or frame time fell. Update the scan baseline.

## Studio MCP path
`list_roblox_studios` -> `script_grep` (`Heartbeat|RenderStepped|Stepped|while true|GetDescendants`) for a quick look -> `execute_luau` (Edit) to create the LoopScan module and run `loop_scan_studio.luau` -> `script_read` the top candidates -> `multi_edit` the rewrites -> `start_stop_play` -> `get_console_output`. Profiler capture is manual.

## Fallback
Rojo project: run `LoopScan.scan` under Lune on each `.luau` file and print findings by path. Without a profiler the output is a list of text candidates; say so, and label gains `untested`.

## Evidence
`Roblox/roblox-kb/optimization-and-streaming.md` (per-frame and per-part logic is the main code cost; coalesce updates; replace wait with task.wait; spread expensive work across frames; RenderStepped only when needed; parallel Luau example). `Roblox/roblox-kb/scripting-and-performance.md` (events over every-frame loops; slice work; spatial hash instead of all-pairs). Official: `Roblox/docs/Videos/2026-10-28 - Docs performance-optimization design.md` (16.67 ms frame budget; event-driven code; chunking; Disconnect connections; cache method results), `Roblox/docs/Videos/2026-10-28 - Docs scripting scheduler.md`, `Roblox/docs/Videos/2026-10-28 - Docs scripting multithreading.md`. The scan is a textual heuristic and can miss or over-report.

## Output
```
LOOP AUDIT <place> <date>   scripts scanned 214, with candidates 17
1. ServerScriptService/Spawner: Heartbeat + GetDescendants (L41) -> profiler 2.9 ms/frame
   Fix: tag + event; result 0.2 ms
2. ...
Kept/reverted list; profiler before/after for each kept change.
```

## Acceptance checks
- [ ] Scan output saved; every top candidate classed as real (profiled) or dismissed with a reason.
- [ ] Each rewrite has behaviour verified (core loop run) and a profiler before/after, or is labelled `untested`.
- [ ] No legitimate per-frame system (camera, input) was changed without a measured need.
- [ ] Connections created by the new code are disconnected on cleanup.
- [ ] Executed check: `LoopScan.test.luau` (6 tests) passes under Lune; scripts pass luau-check.

## Pitfalls
Trusting the scan as proof of cost. Replacing a per-frame loop with a long wait that breaks responsiveness. Adding events that fire as often as the loop did. Moving DataModel work into Actors. Rewriting cold code. Forgetting to disconnect.

## Related
`script-profiler`, `game-optimizer`, `lag-hunter`, `object-pool-builder`, `collection-tag-wiring`, `connection-leak-auditor`.
