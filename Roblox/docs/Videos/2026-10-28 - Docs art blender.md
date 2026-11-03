---
title: "Docs: art / blender"
url: https://create.roblox.com/docs/art/blender.md
creator: Roblox Creator Docs
official: true
advice_density: high
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: art / blender

[Open](https://create.roblox.com/docs/art/blender.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox official docs page on Blender for Roblox 3D art: setting units to studs, import/export axis and scale settings between Blender and Studio, FBX scale fixes, Blender workspaces and modes, and core modeling tools with hotkeys.

## Tips
- [page](https://create.roblox.com/docs/art/blender) **[[building-art-and-assets]]** Set Blender Scene > Units > Unit System to None and Rotation to Degrees so measurements match Studio studs.
- [page](https://create.roblox.com/docs/art/blender) **[[3d-modeling-rigging-and-animation]]** Blender to Studio export: Forward = Z Forward, Up = Y Up, and enable Limit to Selected Objects to keep orientation and selection clean.
- [page](https://create.roblox.com/docs/art/blender) **[[3d-modeling-rigging-and-animation]]** When exporting FBX, set Apply Scalings to FBX Unit Scale and keep other scale values at 1.0; this is the recommended fix for oversized imports.
- [page](https://create.roblox.com/docs/art/blender) **[[3d-modeling-rigging-and-animation]]** GLTF (.gltf/.glb) avoids the FBX scaling workaround; consider it if you want fewer scale adjustments.
- [page](https://create.roblox.com/docs/art/blender) **[[building-art-and-assets]]** Use UV Editing trim sheets applied to many objects to add visual detail without extra texture imports, reducing memory impact.
- [page](https://create.roblox.com/docs/art/blender) **[[building-art-and-assets]]** Avoid Scene Unit Scale 0.01 for modeling: it causes camera, modifier and other Blender issues. Prefer FBX Unit Scale export.
- [page](https://create.roblox.com/docs/art/blender) **[[3d-modeling-rigging-and-animation]]** Use Dissolve instead of Delete when restructuring meshes to avoid leaving holes; use Fill or New Faces from Edges to make meshes watertight.
- [page](https://create.roblox.com/docs/art/blender) **[[building-art-and-assets]]** Set Studio import Scale Unit to Stud and enable Insert Using Scene Position so objects keep Blender scale and position.

## Numbers
- [page](https://create.roblox.com/docs/art/blender) Blender Unit System: **None (studs-compatible)** (Required Blender scene unit setting for Roblox)
- [page](https://create.roblox.com/docs/art/blender) FBX Scale (alt method): **0.01** (Export scale or Scene Unit Scale workaround for oversized FBX imports)
- [page](https://create.roblox.com/docs/art/blender) Sculpting brushes: **over 20** (Brush types available in Sculpting workspace)

## Tools
Blender, Roblox Studio, Blender Snapping tool, Blender Sculpting workspace, Blender UV Editing workspace, Blender Texture Paint workspace

## He points to
- Blender.org
- Roblox Environmental art curriculum: Develop polished assets - Trim sheets
- Roblox accessory specifications and export settings
- Roblox avatar specifications and export settings
- Blender official documentation (Workspaces, Object Modes, Snapping, Unwrapping, Texture Paint)

## Topics
[[3d-modeling-rigging-and-animation]] [[building-art-and-assets]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
