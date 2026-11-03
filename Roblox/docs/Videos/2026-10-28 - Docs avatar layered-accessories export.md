---
title: "Docs: avatar / layered-accessories / export"
url: https://create.roblox.com/docs/avatar/layered-accessories/export.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: avatar / layered-accessories / export

[Open](https://create.roblox.com/docs/avatar/layered-accessories/export.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on exporting layered accessory models from Blender (.fbx) and Maya (.fbx). Covers required object hierarchy (armature, bones, primary mesh, cage parent, inner/outer cage meshes), shoe export structure, and export settings, then conversion to accessory via Accessory Fitting Tool in Studio.

## Tips
- [page](https://create.roblox.com/docs/avatar/layered-accessories/export) **[[building-art-and-assets]]** Apply or delete all modifiers and remove non-Roblox-supported objects from the model before exporting a layered accessory.
- [page](https://create.roblox.com/docs/avatar/layered-accessories/export) **[[3d-modeling-rigging-and-animation]]** Export layered accessories with the hierarchy: armature parent, bones, primary mesh, cage parent, inner cage mesh, outer cage mesh.
- [page](https://create.roblox.com/docs/avatar/layered-accessories/export) **[[3d-modeling-rigging-and-animation]]** Give each shoe its own inner and outer cage when exporting left and right shoes together.
- [page](https://create.roblox.com/docs/avatar/layered-accessories/export) **[[3d-modeling-rigging-and-animation]]** In Blender FBX export, set Path Mode to Copy, enable Embed Textures, set Apply Scalings to FBX Unit Scale, and uncheck Add Leaf Bones.
- [page](https://create.roblox.com/docs/avatar/layered-accessories/export) **[[3d-modeling-rigging-and-animation]]** In Maya FBX export, enable Smooth Mesh and Referenced Asset Content, set Units to Automatic, and set Up Axis to Y.
- [page](https://create.roblox.com/docs/avatar/layered-accessories/export) **[[3d-modeling-rigging-and-animation]]** Import the exported FBX into Studio as a Class.Model, then run the Accessory Fitting Tool to convert it into an accessory.
- [page](https://create.roblox.com/docs/avatar/layered-accessories/export) **[[building-art-and-assets]]** If Maya textures must import as .png, enable Embed Media in the FBX export options.

## Tools
Blender, Maya, Roblox Studio, Accessory Fitting Tool

## He points to
- Blender FBX scaling documentation
- General mesh export settings docs
- Rigid accessory export settings docs

## Topics
[[3d-modeling-rigging-and-animation]] [[building-art-and-assets]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
