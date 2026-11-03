---
name: part-to-mesh-planner
description: "Decide which clusters of static parts should become single meshes: dump parts from Studio, group them by cell, material and colour, drop anything interactive or unanchored, and get a ranked list with the part reduction and an export plan. Use when part count or draw calls are high and the art is final enough to merge."
category: build
tags: mesh, merge, parts, draw calls, export, cluster, optimisation, static, part count
kb: Roblox/roblox-kb/optimization-and-streaming.md, Roblox/roblox-kb/building-art-and-assets.md, Roblox/roblox-kb/3d-modeling-rigging-and-animation.md
related: union-fixer, model-rebuild, model-cleaner, lod-planner, game-optimizer
---

# part-to-mesh-planner

The vault's advice: merge groups of static meshes into one asset late in development (an example went from 8 draw calls to 1), accept that it locks per-part editing, and reuse MeshIds. This skill finds the clusters worth merging so you do not guess. It plans; the modelling and upload are the owner's, and it never merges anything.

## When to use
Part count or draw calls are high, a build is thousands of identical or similar static parts, art is final. Not for: unions (`union-fixer`), a single messy model (`model-cleaner`), or anything that moves or is scripted.

## Inputs (max 2)
1. Scope (a model, folder, or Workspace). 2. Cell size and minimum cluster size (defaults 64 studs and 10 parts; bigger cells merge more but streaming and culling get coarser).

## Procedure
1. Connect (below). Merging is late-stage: confirm the art is final and a source copy of the unmerged model will be kept.
2. Dump the parts with `scripts/dump_parts.luau` (read-only). It prints one Lua table line per part (name, position, material, colour, anchored, interactive, meshId). Parts count as interactive when unanchored, tagged, scripted, carrying a ClickDetector or ProximityPrompt, or inside a model with scripts.
3. In a Lune runner beside `scripts/Cluster.luau` paste the lines as `local parts = { ... }` and run `Cluster.find(parts, 64, 10)`. Groups are keyed by grid cell + Material + colour; unanchored and interactive parts are skipped and counted.
4. Read the result: candidate groups (largest first), parts saved (count minus one per group), and the skipped counts. A group of 200 identical-material wall parts in one cell is the ideal candidate.
5. For each top group: select its parts in Studio, export as one mesh (Studio's mesh export or a modelling tool; the owner does this), re-import and place with the same MeshId, then delete the originals only after a screenshot match. Keep the originals in ServerStorage or a backup place until the result is confirmed.
5b. Check the result against the import limits (official, `Roblox/blender/blender-cheat-sheet-claude-blender-roblox.md`): at most 20,000 triangles per mesh, one material per mesh, one UV set inside 0:1. A group of many parts can exceed 20,000 triangles once merged; split the group in that case. Exporting from Blender: Apply Scalings = FBX Unit Scale, selected objects only, apply modifiers first, and read the exit code of `blender -b --factory-startup --python-exit-code 1 --python script.py -- args` plus that the output file exists.
6. Keep merged meshes within sensible streaming sizes: the vault suggests keeping model extents small, so prefer several mid-sized meshes to one giant one (see `lod-planner`).
7. Set collision on the merged mesh deliberately (Box or Hull), not Precise (`collision-fidelity-tuner`).
8. Re-count parts and draw cost; report before/after.

## Studio MCP path
`list_roblox_studios` -> `search_game_tree` -> `execute_luau` (Edit) with `scripts/dump_parts.luau` -> offline Lune cluster run -> owner exports/imports meshes -> `screen_capture` before/after -> `execute_luau` to count parts.

## Fallback
Without Studio, a part list from a Rojo tree or `.rbxl` export can be turned into the same table by hand; export and visual match are `untested`.

## Evidence
`Roblox/roblox-kb/optimization-and-streaming.md` (merge and reuse meshes to cut draw calls and part counts; combine static meshes late in development, locking per-part edits; reuse MeshIds; meshes are not compressed in memory, a 1 MB mesh costs 1 MB), `Roblox/roblox-kb/building-art-and-assets.md` (cloned mesh parts keep memory roughly constant), `Roblox/roblox-kb/3d-modeling-rigging-and-animation.md` (export hygiene). The cell and minimum-size defaults are the skill's own.

## Output
```
PART-TO-MESH: 8120 parts scanned | skipped: unanchored 140, interactive 310
Candidates: 22 groups, 1,940 parts -> 22 meshes (saves 1,918)
Top: cell 2,0,1 | Brick | #aa5533 -> 214 parts   Untested: export fidelity, memory change
```

## Acceptance checks
- [ ] The dump covers the scope (total vs dumped counts match, or the limit is stated).
- [ ] Skipped interactive/unanchored counts are reported, and none is in a group.
- [ ] Every merge keeps a backup of the originals.
- [ ] Before/after screenshots match for each merged group.
- [ ] Each merged mesh is at most 20,000 triangles with one material (numbers quoted, or `untested`).
- [ ] Memory and part counts after merging were measured, not assumed.

## Pitfalls
Merging early and then needing to edit. One mesh for the whole map (hurts streaming and culling, and the mesh costs its full size in memory). Merging parts with different transparency, textures or decals. Forgetting collision and shadow settings on the new mesh. Merging parts that scripts reach by name.

## Related
`union-fixer`, `model-rebuild`, `model-cleaner`, `lod-planner`, `game-optimizer`.
