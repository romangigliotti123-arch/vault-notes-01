---
name: anchor-checker
description: "Find every part in a place that is unanchored and will fall, drift, jitter or cost physics, separate the ones that are meant to move, and anchor the rest in one undo step. Use when a map falls apart on play, props slide, or physics cost is high."
category: build
tags: anchor, anchored, physics, assembly, falling, jitter, weld, unanchored, workspace, performance
kb: Roblox/roblox-kb/optimization-and-streaming.md, Roblox/roblox-kb/building-and-level-design.md, Roblox/roblox-kb/physics-pathfinding-and-npc-ai.md
related: model-cleaner, attachment-fixer, collision-fidelity-tuner, game-optimizer, lag-hunter
---

# anchor-checker

Place-wide (or folder-wide) answer to "what is simulating physics that should not be?". `model-cleaner` does the same for one model; this scans a whole area and groups parts by assembly so welded builds count once. Audit first; the fix is opt-in.

## When to use
The map collapses or props drift when Play starts; a build jitters; the physics step is heavy in the MicroProfiler; before a release pass. Not for: characters and vehicles (they are meant to move), or deciding collision shapes (`collision-fidelity-tuner`).

## Inputs (max 2)
1. Scope: whole Workspace (default) or a folder/model. 2. Which things move on purpose (doors, ragdolls, vehicles, physics props). Default: anything inside a Humanoid model, Tool, Accessory or Seat, plus anything carrying the attribute `KeepUnanchored = true`.

## Procedure
1. Connect to Studio (below). Ask the owner to save, or confirm version history, before any fix.
2. Run `scripts/anchor_check.luau` with `APPLY_ANCHOR = false`. Read the counts: parts, anchored, skipped on purpose, free parts, free assemblies. Stop here if free = 0.
3. Triage the listed examples. A free part is only a problem when its whole assembly has nothing anchored. Welded groups where one part is anchored are fine and are not listed.
4. For things that must move, set the attribute `KeepUnanchored = true` on the model (one call per model with `execute_luau`), then re-run so they drop out of the list. Doors and elevators usually move through constraints or tweens: leave those assemblies unanchored on purpose and note them.
5. Run again with `APPLY_ANCHOR = true`. It anchors every remaining free part in one undo step.
6. Re-run read-only and compare: free must be 0 or only the intentional movers. Play the map for 20 seconds (`start_stop_play`) and watch `get_console_output` and the part positions of three sample builds.
7. Report the before/after numbers copied from the script output.

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `execute_luau` (datamodel_type Edit) with the contents of `scripts/anchor_check.luau` -> set attributes with `execute_luau` -> re-run -> `start_stop_play` and `screen_capture` for the visual check.

## Fallback
Paste the script into the command bar. Without Studio, work from a Rojo tree or `.rbxl` export: only `Anchored` flags can be read (the assembly check needs the engine), so list unanchored parts without welds and mark the result `untested`.

## Evidence
`Roblox/roblox-kb/optimization-and-streaming.md` (physics cost, reduce what simulates), `Roblox/roblox-kb/building-and-level-design.md` (anchor platforms and static builds), `Roblox/roblox-kb/physics-pathfinding-and-npc-ai.md`. The `AssemblyRootPart` test and the attribute convention are this skill's own; verify behaviour in Play.

## Output
```
ANCHOR CHECK: Workspace  before -> after
parts 4120 | anchored 3980 -> 4101 | skipped on purpose 19 | free 121 -> 0 | free assemblies 74 -> 0
Kept unanchored: DoorFrame_3 (attribute), Elevator   Untested: moving builds in multiplayer
```

## Acceptance checks
- [ ] The audit ran before and after and the report copies its numbers.
- [ ] Every remaining free part is named and has a stated reason.
- [ ] Nothing that players, NPCs or scripts move was anchored (checked against input 2 and in Play).
- [ ] Apply ran as one undo step (Ctrl+Z restores).
- [ ] A 20 second Play test showed no collapse and no new console errors.

## Pitfalls
Anchoring doors, drawbridges or breakables so they stop working. Anchoring a welded vehicle. Forgetting that scripts which tween `CFrame` on an anchored part are fine but scripts that set `AssemblyLinearVelocity` are not. Anchoring parts a script later unanchors on purpose (grep for `Anchored = false`). Welds created at runtime do not exist in Edit mode, so those builds look free in the audit.

## Related
`model-cleaner`, `attachment-fixer`, `collision-fidelity-tuner`, `game-optimizer`, `lag-hunter`.
