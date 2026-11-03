---
name: union-fixer
description: "Inventory every UnionOperation in a place, rank the heaviest and riskiest, decide per union whether it becomes plain parts, a mesh export, or stays, and lower the collision cost of the ones that stay. Use when a place is full of unions, collision is Precise, or memory is high."
category: build
tags: union, unionoperation, csg, negate, mesh, collision, memory, replace, parts
kb: Roblox/roblox-kb/optimization-and-streaming.md, Roblox/roblox-kb/building-art-and-assets.md, Roblox/roblox-kb/3d-modeling-rigging-and-animation.md
related: model-cleaner, part-to-mesh-planner, collision-fidelity-tuner, model-rebuild, game-optimizer
---

# union-fixer

Unions are solid-modelling results stored as generated geometry. The vault is blunt about them: avoid most UnionOperations, reuse mesh ids, prefer parts or meshes. This skill finds them, ranks them, and applies exactly one automatic fix (cheaper collision). Replacing a union is a human or modelling job, so the script never does it.

## When to use
Imported or hand-built maps with many unions; a memory or collision complaint; before an optimisation pass. Not for: choosing which part clusters become meshes (`part-to-mesh-planner`), or one messy model (`model-cleaner`).

## Inputs (max 2)
1. Scope (Workspace default). 2. Is there a modelling tool available (Blender, Studio's mesh tools)? Default: no, so only plain-part replacements are proposed.

## Procedure
1. Connect (below). Save or confirm version history.
2. Run `scripts/audit_unions.luau` with `APPLY_FIDELITY = false`. Note total unions, how many use PreciseConvexDecomposition, tiny unions, leftover NegateOperation parts, and the largest unions.
3. Decide per union, largest first (the script lists them with size and fidelity):
   - Box, wedge or cylinder in disguise (a "union" of two overlapping blocks that is one block): rebuild as plain Part(s). This is the cheapest and most common win.
   - Tiny union (every side under 1 stud): replace with a Part.
   - Carved or curved shape players see up close: export as a mesh (see `part-to-mesh-planner`), re-import, reuse the same MeshId everywhere it repeats.
   - Large union that really is unique: keep it, set collision to Hull or Box.
4. Do the replacements by hand or with `model-rebuild`; keep names and the union's position, size and colour so the look is unchanged. Screenshot before and after (`screen_capture`).
5. Set `APPLY_FIDELITY = true` to lower Precise unions to `FIDELITY_TARGET` (Hull by default). One undo step. Walk any union players stand on or pass through.
6. Re-run read-only; the union count should fall and no Precise unions should remain unless chosen.

## Studio MCP path
`list_roblox_studios` -> `get_studio_state` -> `execute_luau` (Edit) with `scripts/audit_unions.luau` -> `inspect_instance` on the worst few -> replacements via `execute_luau` -> `screen_capture` before/after -> re-run.

## Fallback
Command bar. Without Studio, work from an export: unions are visible as `UnionOperation` instances but their geometry is not, so shape judgements are `untested`.

## Evidence
`Roblox/roblox-kb/optimization-and-streaming.md` (reuse MeshIds; avoid SpecialMesh and most UnionOperations; combine static meshes late; cheapest collision first), `Roblox/roblox-kb/building-art-and-assets.md`. Whether a union fails to replicate under streaming is a Creator Docs question: live-check before telling an owner it will.

## Output
```
UNION AUDIT: Workspace unions 214 -> 61 | precise 38 -> 0 (Hull) | tiny 22 -> 0
Replaced by parts: 120  By mesh: 33  Kept (reason): 61   Untested: collision feel in Play
```

## Acceptance checks
- [ ] The audit ran before and after; counts are copied from the output.
- [ ] Each replacement matches the original in size, position and colour (screenshots compared).
- [ ] No union was deleted without a replacement or an explicit decision.
- [ ] The fidelity change was one undo step and was walked in Play.
- [ ] Kept unions each have a one-line reason.

## Pitfalls
Replacing a union that scripts reference by name without keeping the name. Deleting NegateOperation parts that still define a union you plan to keep (they are consumed by the union; leftovers are junk, but check). Hull on a union with a hole players pass through. Treating the "tiny" list as safe to delete: some are decals-by-geometry.

## Related
`model-cleaner`, `part-to-mesh-planner`, `collision-fidelity-tuner`, `model-rebuild`, `game-optimizer`.
