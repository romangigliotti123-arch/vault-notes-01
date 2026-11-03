---
name: pivot-fixer
description: "Check where every model's pivot sits against where it should (bottom centre of its bounding box by default) and move the pivot, not the parts, so PivotTo, rotation and placement land where you aim. Use when spawned or placed models float, sink or swing around the wrong point."
category: build
tags: pivot, primarypart, worldpivot, pivotto, bounding box, model, placement, rotation, modular
kb: Roblox/roblox-kb/building-and-level-design.md, Roblox/roblox-kb/building-art-and-assets.md, Roblox/roblox-kb/optimization-and-streaming.md
related: model-cleaner, model-rebuild, attachment-fixer, prop-set-planner, naming-convention-enforcer
---

# pivot-fixer

A model's pivot is the point `PivotTo`, rotation and snapping use. With a PrimaryPart it is `PrimaryPart.CFrame * PivotOffset`; without one it is `Model.WorldPivot`. A pivot in the wrong place makes spawned props float or sink and makes rotation orbit something else. This changes only the pivot, never part positions.

## When to use
Props spawned by script land at the wrong height; modular pieces will not snap; a model rotates around a corner. Not for: rebuilding a messy hierarchy (`model-rebuild`), or choosing PrimaryPart for physics assemblies.

## Inputs (max 2)
1. Which models (selection, a folder, or Workspace). 2. Wanted pivot: `bottomCenter` (default, props and buildings sit on the ground at their pivot) or `center`. Modular kits: pick one convention for the whole kit.

## Procedure
1. Connect (below). Save or confirm version history.
2. Run `scripts/fix_pivots.luau` with `APPLY = false` and the scope set. It lists models whose pivot is more than `TOLERANCE` studs from the wanted point, worst first, skipping characters (Humanoid) and models with attribute `PivotLocked = true`.
3. Triage: pivots that are off on purpose (a door pivots at its hinge, a lever at its base) get `PivotLocked = true` and drop out. Everything else should follow the kit's rule.
4. For modular kits, decide the rule first (vault: every piece has the same pivot, for example the forward-most lower corner or the attach point) and use `MODE` accordingly; do not mix conventions inside one kit.
5. Set `APPLY = true`. With a PrimaryPart the script sets `PrimaryPart.PivotOffset`; without one it sets `Model.WorldPivot`. One undo step. Part positions do not change.
6. Re-run read-only: off-pivot must be 0 for the scope. Test with a script: `model:PivotTo(CFrame.new(0, 0, 0))` on a copy, confirm the model's base sits at y = 0 (`execute_luau`, then delete the copy).
7. The maths is `scripts/Pivot.luau` (Lune-tested targets and offsets); run it offline to check a hand-computed value.

## Studio MCP path
`list_roblox_studios` -> `search_game_tree` to find the models -> `execute_luau` (Edit) with `scripts/fix_pivots.luau` -> apply -> `execute_luau` copy-and-PivotTo test -> `screen_capture`.

## Fallback
Command bar with the models selected. By hand: select the model, use the pivot tool in Studio (Home tab, Pivot) and snap to the bottom face. Without Studio the bounding box cannot be computed: `untested`.

## Evidence
`Roblox/roblox-kb/building-and-level-design.md` (set PrimaryPart before rotating or scaling; clearing it resets the pivot to the bounding-box centre; same pivot for every modular piece), `Roblox/roblox-kb/building-art-and-assets.md`. Model.WorldPivot and PivotOffset behaviour: verify in Creator Docs if a property name looks off.

## Output
```
PIVOT AUDIT: Workspace.Props models=96 off-pivot 41 -> 0 (bottomCenter)
Locked on purpose: Door_A, Door_B, Lever   Untested: runtime spawn heights
```

## Acceptance checks
- [ ] Audit ran before and after; counts copied.
- [ ] No part moved (compare three models' part positions before and after with `inspect_instance`).
- [ ] PivotTo copy test puts the base at the target height within 0.05 studs.
- [ ] Locked models are listed with the reason.
- [ ] Apply was one undo step.

## Pitfalls
Using `center` for props that should sit on the ground. Changing the pivot of a model a script already offsets by hand (the script now double-compensates): grep `PivotTo` and `GetPivot` first. Rotated models: the script keeps the current pivot rotation and only moves the position. Changing a PrimaryPart's PivotOffset also moves that part's own pivot for single-part use.

## Related
`model-cleaner`, `model-rebuild`, `attachment-fixer`, `prop-set-planner`, `naming-convention-enforcer`.
