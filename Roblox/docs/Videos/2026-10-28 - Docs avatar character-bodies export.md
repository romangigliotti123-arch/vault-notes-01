---
title: "Docs: avatar / character-bodies / export"
url: https://create.roblox.com/docs/avatar/character-bodies/export.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: avatar / character-bodies / export

[Open](https://create.roblox.com/docs/avatar/character-bodies/export.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on exporting character body models (avatar bodies with 15 mesh parts, 19 attachments) from Blender (.fbx/.gltf) and Maya (.fbx) for import into Studio as Class.Model characters, then applying a HumanoidDescription.

## Tips
- [page](https://create.roblox.com/docs/avatar/character-bodies/export) **[[3d-modeling-rigging-and-animation]]** Apply or delete all modifiers and remove non-Roblox objects before exporting a character body; leftover objects break the export.
- [page](https://create.roblox.com/docs/avatar/character-bodies/export) **[[3d-modeling-rigging-and-animation]]** Parent each of the 15 body-part meshes under an armature and include all 19 attachments with correct naming affixes.
- [page](https://create.roblox.com/docs/avatar/character-bodies/export) **[[3d-modeling-rigging-and-animation]]** Ensure each of the 15 body parts has an outer cage object, grouped under one empty parent to simplify the workspace.
- [page](https://create.roblox.com/docs/avatar/character-bodies/export) **[[3d-modeling-rigging-and-animation]]** Set the animation timeline Start and End to cover the full range of all animations before exporting.
- [page](https://create.roblox.com/docs/avatar/character-bodies/export) **[[3d-modeling-rigging-and-animation]]** In Blender FBX export, set Apply Scalings to FBX Unit Scale and uncheck Add Leaf Bones to avoid scale and bone problems on import.
- [page](https://create.roblox.com/docs/avatar/character-bodies/export) **[[3d-modeling-rigging-and-animation]]** In Blender FBX export, uncheck NLA Strips, All Actions and Force Start/End Keyframes, and set Simplify to 0.0.
- [page](https://create.roblox.com/docs/avatar/character-bodies/export) **[[3d-modeling-rigging-and-animation]]** In Maya FBX export, enable Smooth Mesh, Animation and Bake Animation, and set Units to Automatic and Up Axis to Y.
- [page](https://create.roblox.com/docs/avatar/character-bodies/export) **[[3d-modeling-rigging-and-animation]]** Avatar characters with dynamic heads require animation data in the export.
- [page](https://create.roblox.com/docs/avatar/character-bodies/export) **[[building-art-and-assets]]** If using Roblox's avatar template files, complete the cleanup steps or the assets will fail validation.

## Numbers
- [page](https://create.roblox.com/docs/avatar/character-bodies/export) Body parts: **15 mesh objects with outer cages, one per body part**
- [page](https://create.roblox.com/docs/avatar/character-bodies/export) Attachments: **19 attachments required in armature object**
- [page](https://create.roblox.com/docs/avatar/character-bodies/export) Blender Simplify: **0.0**

## Tools
Blender, Maya, Roblox Studio Importer, HumanoidDescription

## He points to
- Character specifications (Roblox docs)
- Blender FBX scaling (Roblox docs)

## Topics
[[3d-modeling-rigging-and-animation]] [[building-art-and-assets]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
