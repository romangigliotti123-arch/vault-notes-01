---
name: attachment-fixer
description: "Find and repair attachments, welds and constraints that break models - dead WeldConstraints, constraints with a missing or shared attachment, welds across unrelated models, builds that split into several loose assemblies - removing dead welds and re-welding loose pieces to the PrimaryPart in one undo step. Use when a model falls apart or a hinge, rope or spring does nothing."
category: build
tags: attachment, weld, weldconstraint, constraint, motor6d, assembly, hinge, rope, model, joint
kb: Roblox/roblox-kb/physics-pathfinding-and-npc-ai.md, Roblox/roblox-kb/3d-modeling-rigging-and-animation.md, Roblox/roblox-kb/building-and-level-design.md
related: anchor-checker, rig-checker, model-cleaner, pivot-fixer, accessory-fitting-guide
---

# attachment-fixer

Joints are how a model stays one thing. This lists every joint that cannot work (nil ends, self-joins, attachments parented to nothing useful) and every model that has quietly become several free assemblies. Character rigs are `rig-checker`'s job; this is for props, vehicles, doors and builds.

## When to use
A build collapses when unanchored, a hinge or rope constraint is inert, a prop drags another model with it, or after pasting or deleting parts out of a welded group. Not for: Humanoid rigs and animation joints (`rig-checker`), or anchoring scenery (`anchor-checker`).

## Inputs (max 2)
1. The model or folder (Studio selection by default, else Workspace). 2. Does it have a PrimaryPart that is the structural root? Default: only models that already have one are auto re-welded.

## Procedure
1. Connect (below). Save or confirm version history.
2. Run `scripts/attach_audit.luau` with both flags false. Read each category: attachment not under a part, constraint with a missing attachment, attachments on the same part, weld with a missing part, weld joining two models, Motor6D with a missing part, models splitting into N free assemblies.
3. Fix by category:
   - Dead weld (Part0 or Part1 nil): safe to delete, `APPLY_REMOVE_DEAD = true`. It holds nothing.
   - Constraint with a missing attachment: find what it was meant to join (name and neighbours) and re-assign by hand; do not delete a constraint a script enables at runtime without checking `script_grep` for its name.
   - Weld across two top-level models: almost always an accident from copy-paste; the two models move together. Delete it or restructure; ask the owner.
   - Model splits into N assemblies: add welds from each loose assembly root to the PrimaryPart with `APPLY_REWELD = true` (models with a PrimaryPart only). Models without one need a PrimaryPart first (largest structural part).
4. Run the apply pass. Both flags apply in one undo step; the report counts each.
5. Re-run read-only. The categories fixed must read zero; remaining ones are listed as owner decisions.
6. Behaviour test in Play (`start_stop_play`): unanchor a copy and drop it; the model must stay in one piece. Screenshot it.

## Studio MCP path
`list_roblox_studios` -> `search_game_tree` -> `execute_luau` (Edit) with `scripts/attach_audit.luau` -> `script_grep` for names of constraints you doubt -> flags on -> re-run -> `start_stop_play` for the drop test -> `get_console_output`.

## Fallback
Command bar with the model selected. Without Studio, from a `.rbxm`/Rojo export you can find nil ends and wrong parents by reading the XML/model JSON; the assembly-split check needs the engine: `untested`.

## Evidence
`Roblox/roblox-kb/physics-pathfinding-and-npc-ai.md` (constraints and assemblies), `Roblox/roblox-kb/3d-modeling-rigging-and-animation.md` (Motor6D and tool attachment, set AssemblyRootPart not PrimaryPart for custom Motor6D rigs), `Roblox/roblox-kb/building-and-level-design.md`. Re-welding to the PrimaryPart is this skill's convention; confirm the PrimaryPart really is the structural root.

## Output
```
ATTACHMENT AUDIT: Workspace.Vehicles
[12] weld with a missing part -> removed   [3] model splits into 2-4 free assemblies -> re-welded
[2] weld joins two different top-level models -> owner decision (Bus_1 / Sign_7)
```

## Acceptance checks
- [ ] Audit ran before and after; counts copied from the output.
- [ ] No constraint a script toggles was removed (grepped).
- [ ] Re-weld targets were checked: each loose part belongs to the model it was welded into.
- [ ] A Play drop test kept each fixed model in one piece.
- [ ] Apply was one undo step.

## Pitfalls
Re-welding hinge or door parts that are supposed to rotate: they are separate assemblies on purpose (use the constraint, not a rigid weld). Welding to a PrimaryPart that is itself a free assembly. Runtime-created welds do not exist in Edit mode, so the audit over-reports there. Deleting a Motor6D in a character rig (use `rig-checker`).

## Related
`anchor-checker`, `rig-checker`, `model-cleaner`, `pivot-fixer`, `accessory-fitting-guide`.
