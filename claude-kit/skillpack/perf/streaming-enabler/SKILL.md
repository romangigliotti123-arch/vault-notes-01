---
name: streaming-enabler
description: "Turn on and tune StreamingEnabled for a Roblox place, choose Persistent or Atomic for the models that need it, fix the client scripts streaming breaks, and prove the gain with join time and client memory before and after. Use when a map is big, joins are slow or phones run out of memory."
category: perf
tags: streaming, StreamingEnabled, instance streaming, persistent, atomic, radius, join time, memory, pop-in, slim
kb: Roblox/roblox-kb/optimization-and-streaming.md, Roblox/roblox-kb/scripting-and-performance.md, Roblox/roblox-kb/testing-debugging-and-qa.md
related: game-optimizer, join-time-reducer, memory-budget-planner, lod-planner, replicated-loader-builder, mobile-perf-tester
---

# streaming-enabler

StreamingEnabled is the vault's highest-impact single change for client memory and join time on large maps: only the area near each player replicates. The work is not flipping the switch, it is making the scripts and models survive parts appearing and disappearing. This skill audits, proposes settings, lists what breaks, and measures.

## When to use
A big or dense map, slow joins, mobile out-of-memory crashes, or "turn on streaming" as a task. Not for: tiny single-room games where everything is always needed (measure first, it may not pay), or per-model polygon cost (`lod-planner`, `part-count-auditor`).

## Inputs (max 2)
1. How large the playable world is and whether players teleport/fast-travel/spectate (default: assume yes to teleports). 2. Target device (default: low-end Android phone).

## Procedure
1. Baseline, before any change: client memory (Developer Console F9 Memory tab: PlaceMemory), time-to-first-playable from a cold join on the target device (`join-time-reducer`), and the current Workspace settings. Run `scripts/stream_audit.luau` (read-only) and save its output. Stop if you cannot measure either number: label every later claim `untested`.
2. Choose settings from the docs defaults: StreamingMinRadius 64, StreamingTargetRadius 1024. Keep them unless a measurement says otherwise; lower the target radius only if memory is still too high after step 5, raise it only for open worlds where pop-in hurts.
3. Classify models from the audit output. Persistent: content that must always exist (spawn area, objective, anything scripts index directly). Atomic: groups that scripts need whole (a vehicle, a door with its frame). Default: everything else. Flatten nesting: a Persistent model inside an Atomic model makes the Atomic one behave as persistent. Docs guidance: keep a model's extent to about 64 studs so it streams in whole.
4. Fix the scripts the audit flagged: client code that reads `workspace.A.B.C` directly must use `WaitForChild` with a timeout or `StreamingIntegrity` aware checks; never assume a distant part exists; raycasts and overlap queries can miss unloaded parts; do not Clone/Reparent/Destroy streamed instances on the client (it desyncs replication). For must-load transitions use `Player:RequestStreamAroundAsync(position, timeout)` before teleports, and `AddReplicationFocus` sparingly.
5. Test deliberately at the harsh setting: set StreamingTargetRadius to 64 in a test copy, then traverse, teleport and revisit areas, because bugs appear at stream edges. Check the Network Stats streaming debug view (red <64, yellow 64-1024, blue =1024, green >1024).
6. Re-measure memory and join time on the same device and scenario. Keep the setting only if memory or join time improved and the core loop still works (`playtest-bot-writer` or a manual run).
7. Only if distant visibility is a core feature (sniper scope, flight): consider frustum streaming (server-side `Player.FrustumStreaming`), knowing it raises client memory and CPU, has no occlusion culling and is disabled on low-end devices.

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `execute_luau` (Edit) with `scripts/stream_audit.luau` -> `script_grep` for `workspace%.` chains and `FindFirstChild` on world parts -> `multi_edit` the fixes -> `start_stop_play` -> `get_console_output` for errors such as "X is not a valid member of Workspace" -> `screen_capture` at the edge of the radius. StreamingEnabled and the radii are place settings: ask the owner to set them (or confirm they are set) in the Workspace properties; report `untested` if you could not see the effect on a real device.

## Fallback
Without Studio: paste `stream_audit.luau` in the command bar; with Rojo, edit scripts as files and give the owner the property list to set by hand. Memory and join-time numbers need a device: mark them `untested` otherwise.

## Evidence
Vault KB `Roblox/roblox-kb/optimization-and-streaming.md` (enable streaming; Persistent/Atomic rules; do not desync streamed instances; frustum streaming trade-offs; test with radius 64). Official Creator Docs notes in the vault: `Roblox/docs/Videos/2026-10-28 - Docs workspace streaming.md` (defaults 64 and 1024, 9 moving foci about equal 10 players of server load), `Roblox/docs/Videos/2026-10-28 - Docs workspace streaming techniques.md` (about 64 stud model extent), `Roblox/docs/Videos/2026-10-28 - Docs workspace streaming frustum.md`, `Roblox/docs/Videos/2026-10-28 - Docs performance-optimization design.md` (streaming improves join, memory and frame rate). Scripting KB (creator report): about 1 KB per part replicated. Live-check the API names in Creator Docs before editing scripts.

## Output
```
STREAMING PLAN <place> <date>
Settings: Enabled=true Min=64 Target=1024 Integrity=<mode>   [docs defaults / changed because ...]
Models: Persistent <n> (list), Atomic <n> (list), Default rest
Script fixes: <path>: <what> ...
Before -> after (device, scenario): memory MB ... | time-to-playable s ... | edge bugs found/fixed ...
```

## Acceptance checks
- [ ] Before and after numbers exist for memory and join time on the same device, or are labelled `untested`.
- [ ] `stream_audit.luau` output saved and every flagged script either fixed or listed with a reason.
- [ ] Tested at radius 64 with a teleport and a revisit of a streamed-out area; no errors in the console.
- [ ] No Persistent model nested inside an Atomic one.
- [ ] Executed check: `stream_audit.luau` passes the pack's luau-check run (stylua, selene, luau-lsp).

## Pitfalls
Switching it on late and discovering client scripts that index the world directly. Making everything Persistent (no gain). Teleporting players into unloaded space without `RequestStreamAroundAsync`. Treating tiny test maps as proof. Cloning or destroying streamed instances on the client. Believing frustum streaming is free.

## Related
`game-optimizer`, `join-time-reducer`, `memory-budget-planner`, `lod-planner`, `replicated-loader-builder`.
