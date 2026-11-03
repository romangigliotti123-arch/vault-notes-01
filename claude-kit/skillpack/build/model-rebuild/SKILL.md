---
name: model-rebuild
description: "Rebuild a messy, over-detailed or badly imported model as a clean, efficient one that looks the same: dump a manifest, plan a simpler part and mesh structure, rebuild it with a sane hierarchy, pivot, materials and collision, and verify it against the original. Use when model-cleaner's fixes are not enough or the structure itself is the problem."
category: build
tags: rebuild, remodel, recreate, simplify, import, mesh, hierarchy, pivot, efficient, model
kb: Roblox/roblox-kb/building-art-and-assets.md, Roblox/roblox-kb/3d-modeling-rigging-and-animation.md, Roblox/roblox-kb/optimization-and-streaming.md, Roblox/roblox-kb/building-and-level-design.md
related: model-cleaner, part-to-mesh-planner, union-fixer, pivot-fixer, asset-license-checker, lod-planner, game-optimizer
---

# model-rebuild

Same look, better structure. First run `model-cleaner`; rebuild only when the audit shows the structure is the problem (thousands of tiny parts, nested unions, broken hierarchy, imported mesh soup). Rebuilding someone else's asset may violate its licence: run `asset-license-checker` first. You rebuild shapes you are allowed to use, never a copy of a protected design.

## When to use
A model with hundreds of small parts where a few meshes or parts would do; a union chain that breaks; an import with a wrong scale/pivot/orientation; a kit-bash you want to turn into one reusable prop. Not for: characters or rigs (`rig-checker`, `accessory-fitting-guide`), terrain.

## Inputs (max 3)
1. The model (selection/path). 2. Target budget: max part count and whether meshes are allowed (default: at most 25 percent of the original parts, collidable shell simple). 3. Style notes (default: match the original; palette from the manifest).

## Procedure
1. Licence/provenance gate: if the model is from the Toolbox or an import, run `/rbx asset-license-checker`. Stop if it is not yours to modify.
2. Manifest: run `scripts/manifest.luau` (TARGET set). It prints compact JSON: names, sizes, positions relative to the pivot, rotation, material, colour hex, mesh/texture ids, collision flags. Save to `reports/<name>-manifest.json` and keep a screenshot set (front, side, top; `screen_capture`) as the visual reference.
3. Group: cluster parts by function (structure, trim, props, glass, lights). For each cluster decide the cheapest honest representation: one Part with a Material and Colour; a few Parts with CornerWedge/Wedge shapes; one MeshPart (made in Blender or `generate_mesh`, see `part-to-mesh-planner`); keep as-is. Detail that is under about a quarter of a stud at play distance is not worth a part.
4. Plan in a table (cluster, original count, new representation, expected count, risk). Show it to the owner when the saving is large or the look could change; otherwise continue.
5. Rebuild into a NEW model next to the original (name `<Name>_v2`), never edit in place: hierarchy `Model > Structure/Props/Details` folders; unique names; PrimaryPart at a sensible pivot (base centre for placed props; `PivotTo` then behaves); anchored unless it moves; CanCollide only on the collision shell; CanTouch/CanQuery off on decoration; CollisionFidelity Box/Hull on meshes.
5b. Mesh limits (official, art/modeling/specifications; cheat sheet `Roblox/blender/blender-cheat-sheet-claude-blender-roblox.md` section 3): each MeshPart at most 20,000 triangles (4,000 for rigid or layered accessories), one material per mesh, one UV set inside 0:1, closed geometry with no N-gons. A merge that pushes a mesh over 20,000 triangles is split, not shipped.
6. Compare: manifests of old vs new (counts), bounding boxes within 2 percent, screenshots from the same camera. Measure: part count, MeshPart/union count, and render cost note.
7. Swap only after the owner agrees; keep the original in ServerStorage or a backup folder until a playtest passes. Run `model-cleaner` on the new model as the final check.

## Studio MCP path
`list_roblox_studios` -> `search_game_tree` -> `execute_luau` (Edit) with `scripts/manifest.luau` -> build parts with `execute_luau` scripts you write from the plan (create Parts with `Instance.new`, parent into the `_v2` model) -> `generate_mesh` / `generate_procedural_model` for mesh clusters (`wait_job_finished`) -> `screen_capture` for comparison -> `get_console_output`.

## Fallback
Command bar: run `manifest.luau`, paste the JSON back; produce the rebuild as a Luau builder script the owner runs in the command bar (it creates `<Name>_v2`); or export meshes from Blender (see `Roblox/roblox-kb/3d-modeling-rigging-and-animation.md`: FBX scale/orientation, unique bone and mesh names). Without Studio mark appearance checks `untested`.

## Evidence
`Roblox/roblox-kb/building-art-and-assets.md` (graybox first, consistent materials, silhouette), `Roblox/roblox-kb/optimization-and-streaming.md` (collision fidelity cheapest-first, non-interactive parts do not collide or query, streaming modes), `Roblox/roblox-kb/3d-modeling-rigging-and-animation.md` (export settings, naming). Property semantics: Creator Docs via `kbq.py docs`.

## Output
`reports/<name>-rebuild.md`: original vs new counts, the cluster plan table, risks, screenshots paths, what was swapped, rollback instruction. The new model in the place (or the builder script file `build_<name>.luau`).

## Acceptance checks
- [ ] Licence gate passed or the model is the owner's.
- [ ] New part count <= budget and the manifest shows it (numbers quoted).
- [ ] Bounding box within 2 percent of the original; screenshots side by side from the same camera show no visible difference at play distance.
- [ ] Every new MeshPart is at most 20,000 triangles, has one material and UVs inside 0:1 (counted in Blender or the importer, not guessed).
- [ ] Meshes exported from Blender used Apply Scalings = FBX Unit Scale (still 1/100 size: object transforms 1.000 or glTF) and a deliberate Scale Unit (non-Stud units are 25:7 studs per metre since 2026-06-16, was 20:1; devforum.roblox.com/t/4644371).
- [ ] PrimaryPart/pivot set; `PivotTo` test places it correctly; names unique.
- [ ] Original preserved until the owner confirms; swap is reversible.
- [ ] `model-cleaner` audit on the new model reports no high-severity rows.

## Pitfalls
Merging parts with different collision needs into one mesh (players get stuck or fall through). Losing a script's expected child names. Rebuilding a protected design. Meshes with wrong scale/pivot from export. Renaming meshes or moving pivots before a Reimport (Alt+Shift+R matches by name and path) creates duplicates instead of updating. Doing it in place with no backup.

## Related
`model-cleaner`, `part-to-mesh-planner`, `union-fixer`, `pivot-fixer`, `asset-license-checker`, `game-optimizer`.
