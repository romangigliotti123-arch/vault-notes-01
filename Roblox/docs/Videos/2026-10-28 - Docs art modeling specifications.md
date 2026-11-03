---
title: "Docs: art / modeling / specifications"
url: https://create.roblox.com/docs/art/modeling/specifications.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: art / modeling / specifications

[Open](https://create.roblox.com/docs/art/modeling/specifications.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on 3D mesh modeling specifications for Studio compatibility: geometry limits (20,000 triangles per mesh, watertight, quads, nonzero volume), rigging rules (frozen transforms, max 4 bone influences, no root influences), texture support, single-track animation export, and inner/outer cage naming and handling.

## Tips
- [page](https://create.roblox.com/docs/art/modeling/specifications) **[[building-art-and-assets]]** Keep individual meshes under 20,000 triangles; avatar items have their own separate budgets for bodies, rigid and layered accessories.
- [page](https://create.roblox.com/docs/art/modeling/specifications) **[[building-art-and-assets]]** Make meshes watertight with no exposed holes or backfaces, and give them real volume (no zero-thickness geometry).
- [page](https://create.roblox.com/docs/art/modeling/specifications) **[[building-art-and-assets]]** Model with quads where possible and avoid N-gons.
- [page](https://create.roblox.com/docs/art/modeling/specifications) **[[3d-modeling-rigging-and-animation]]** Freeze all bones/joints so scale is 1,1,1 and rotation is 0,0,0; set the root joint to 0,0,0.
- [page](https://create.roblox.com/docs/art/modeling/specifications) **[[3d-modeling-rigging-and-animation]]** Limit each vertex to at most 4 bone influences and do not apply influences to the Root bone.
- [page](https://create.roblox.com/docs/art/modeling/specifications) **[[3d-modeling-rigging-and-animation]]** Maintain symmetry when applying rig influences; use the modeling software's symmetry tools.
- [page](https://create.roblox.com/docs/art/modeling/specifications) **[[3d-modeling-rigging-and-animation]]** Export only one animation track per mesh; export a separate file for each animation you need.
- [page](https://create.roblox.com/docs/art/modeling/specifications) **[[building-art-and-assets]]** Name inner and outer cages after the primary mesh with _InnerCage and _OuterCage suffixes.
- [page](https://create.roblox.com/docs/art/modeling/specifications) **[[common-mistakes]]** Do not delete vertices or alter UVs on inner/outer cages; this causes import errors in Studio or failures when equipping.
- [page](https://create.roblox.com/docs/art/modeling/specifications) **[[3d-modeling-rigging-and-animation]]** Character models must include an outer cage or layered accessories will not equip properly.
- [page](https://create.roblox.com/docs/art/modeling/specifications) **[[building-art-and-assets]]** Keep cage faces consistently sized and symmetrical; use symmetry tools in your modeling software.

## Numbers
- [page](https://create.roblox.com/docs/art/modeling/specifications) Max triangles per individual mesh: **20,000** (General mesh budget; avatar items have separate budgets)
- [page](https://create.roblox.com/docs/art/modeling/specifications) Max bone/joint influences per vertex: **4** (Vertex cannot be influenced by more than 4 bones)
- [page](https://create.roblox.com/docs/art/modeling/specifications) Animation tracks per export: **1** (Only a single animation track per mesh or model export)
- [page](https://create.roblox.com/docs/art/modeling/specifications) Bone scale and rotation at rest: **scale 1,1,1; rotation 0,0,0** (Required for all frozen bones/joints; root at 0,0,0)

## Tools
Blender, Maya

## He points to
- Assign textures in modeling tools
- Texture specifications
- Character body specifications
- Accessory specifications and export settings
- Layered accessory specifications
- Avatar specifications and export settings

## Topics
[[3d-modeling-rigging-and-animation]] [[building-art-and-assets]] [[common-mistakes]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
