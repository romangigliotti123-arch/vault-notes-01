---
name: connection-leak-auditor
description: "Find the connections, loops, instances and per-player tables that are never cleaned up, rank files by risk with a heuristic scanner, and fix them with a Janitor (one object that owns and releases everything). Use when memory climbs over a server's life, a script runs after its model is gone, or before launch."
category: scripting
tags: memory leak, connection, disconnect, cleanup, janitor, maid, trove, while true, playerremoving, destroy, debris
kb: Roblox/roblox-kb/scripting-and-performance.md, Roblox/roblox-kb/luau-language-and-types.md, Roblox/roblox-kb/testing-debugging-and-qa.md
related: event-bus-builder, object-pool-builder, lag-hunter, script-profiler, game-optimizer, roblox-performance-pass
---

# connection-leak-auditor

A leak is anything that outlives its owner: a connection on a destroyed part, a table entry for a player who left, a loop whose model is gone, instances created and never destroyed. Finding it by reading is slow; this skill ranks suspects by text pattern, then you confirm in the memory tools. `lag-hunter` and `script-profiler` cover speed; this covers growth.

## When to use
Server memory grows through a session, scripts keep working on removed objects, a `PlayerAdded` handler holds state, or as a pre-launch sweep. Not for: frame-time problems (use `script-profiler`).

## Inputs (max 2)
1. Source root or the suspect scripts (default: all server scripts, then client). 2. How long a server lives (default 1 hour+; leaks matter more the longer it runs).

## Procedure
1. Collect `{ name = source }`. Run `LeakScan.scan(source)` per file (`scripts/LeakScan.luau`). Rules: `busy-loop` (a `while true` with no wait or frame event), `repeat-connect` (a connection made inside PlayerAdded/CharacterAdded/loops/event handlers and never stored), `unstored-connect` (frame-event connection with no handle), `player-state-not-cleared` (state keyed by player, no PlayerRemoving), `instances-not-destroyed`, `unpaired-render-bind`. It is a heuristic over indented text (works best on StyLua-formatted code): treat every hit as a suspect.
2. Rank files by `LeakScan.summarize` count and by how long the owner lives (a per-player script matters more than a one-off).
3. Confirm the top suspects with the engine: the Developer Console memory tags and instance counts over a 10-minute play session, or `execute_luau` printing `#workspace:GetDescendants()` before and after repeating the action. A growing count after the action is repeated and cleaned is a real leak.
4. Fix with `scripts/Janitor.luau`: create one Janitor per owner (player, round, model, NPC). Add connections (`jan:Connect(signal, fn)`), instances, threads and cleanup functions; call `jan:Cleanup()` when the owner ends (PlayerRemoving, `Destroying`, round end). Cleanup runs newest first, is safe to call twice, and keeps going if an item throws.
5. Loops: give every long-running loop an owner and a stop condition (`while alive do ... task.wait(dt) end`, or a stored thread that the Janitor cancels). Replace polling with events.
6. Instances: parent last, track what you create, destroy on every path (also the error path) or use `Debris:AddItem` for timed objects; high-churn objects go to `object-pool-builder`.
7. Per-player tables: set the entry to nil in PlayerRemoving; for caches keyed by Instance use weak keys (`setmetatable(t, { __mode = "k" })`).
8. Re-run the scan and the memory check; the count must not grow on repeat.

## Studio MCP path
`list_roblox_studios` -> `script_grep` for `:Connect(|while true|Instance.new|BindToRenderStep` -> `script_read` -> `multi_edit` the fixes -> `start_stop_play` -> `execute_luau` before/after instance counts -> `get_console_output`.

## Fallback
Rojo repo with Lune for the scan; memory growth needs a running place (Developer Console), `untested` otherwise.

## Evidence
`Roblox/roblox-kb/scripting-and-performance.md`: track every connection and instance in one Trove or Maid; fix memory leaks and check startup spikes; closures keep strong references; weak tables for caches; clear per-player tables on leave; destroy tracked instances on every creation path; locate memory with memory tags and the MicroProfiler. `Roblox/roblox-kb/luau-language-and-types.md`: clean up signal connections and fire a Destroying-style signal first.

## Output
`leaks.md`: ranked suspects (file, line, rule), what was confirmed with the engine, the fix per owner, before/after counts.

## Acceptance checks
- [ ] Executed: the scanner and the Lune tests (`lune run ../skillpack/scripting/connection-leak-auditor/scripts/tests/LeakScan.test.luau`, quote `9 passed, 0 failed`).
- [ ] Every confirmed leak has an owner and a `Cleanup` call site.
- [ ] Instance count is flat across repeated action and cleanup (numbers quoted) or marked untested.
- [ ] No `while true` without a stop condition remains in owned scripts.
- [ ] PlayerRemoving clears every per-player table.

## Pitfalls
Treating the scanner's hits as proof. Fixing by `Destroy()` on the instance but leaving connections to other objects. A Janitor that is itself never cleaned up. Keeping a strong reference to a Player in a table (`state[player]`): prefer UserId keys and clear on leave.

## Related
`event-bus-builder`, `object-pool-builder`, `lag-hunter`, `script-profiler`, `game-optimizer`.
