---
title: "Docs: art / modeling / skin-a-simple-mesh"
url: https://create.roblox.com/docs/art/modeling/skin-a-simple-mesh.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: art / modeling / skin-a-simple-mesh

[Open](https://create.roblox.com/docs/art/modeling/skin-a-simple-mesh.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs guide on skinning a simple mesh in Blender: set up scene units, import an FBX tree, add an armature with 3 bones, parent with automatic weights, then weight paint using Auto Normalize and projected brushes before exporting to Studio.

## Tips
- [page](https://create.roblox.com/docs/art/modeling/skin-a-simple-mesh) **[[3d-modeling-rigging-and-animation]]** Set Blender to Studio's relative scene units before importing the model so bone and mesh scale matches in Studio.
- [page](https://create.roblox.com/docs/art/modeling/skin-a-simple-mesh) **[[3d-modeling-rigging-and-animation]]** Skinning must be done after the model is rigged; complete the rig first, then skin.
- [page](https://create.roblox.com/docs/art/modeling/skin-a-simple-mesh) **[[3d-modeling-rigging-and-animation]]** Rename bones in the Outliner before export; bone names carry over when importing the mesh into Studio.
- [page](https://create.roblox.com/docs/art/modeling/skin-a-simple-mesh) **[[3d-modeling-rigging-and-animation]]** Parent the armature with Automatic Weights to auto-assign influences, saving time before weight painting.
- [page](https://create.roblox.com/docs/art/modeling/skin-a-simple-mesh) **[[3d-modeling-rigging-and-animation]]** Select the armature first, then the mesh, before entering Weight Paint mode; otherwise hybrid pose-and-paint testing does not work.
- [page](https://create.roblox.com/docs/art/modeling/skin-a-simple-mesh) **[[3d-modeling-rigging-and-animation]]** Enable Auto Normalize so each vertex sums to full influence; paint full influence first, then adjust each bone.
- [page](https://create.roblox.com/docs/art/modeling/skin-a-simple-mesh) **[[3d-modeling-rigging-and-animation]]** Set Falloff to Projected and disable Front Faces Only so layered foliage gets weights through the mesh, not just the surface.
- [page](https://create.roblox.com/docs/art/modeling/skin-a-simple-mesh) **[[3d-modeling-rigging-and-animation]]** Use weight values as guides: 1.0 for trunk-controlling bone, 0.5 for middle foliage, 0.25 for top leaves, for subtle movement.
- [page](https://create.roblox.com/docs/art/modeling/skin-a-simple-mesh) **[[3d-modeling-rigging-and-animation]]** Test bone rotation with R after every painting pass, and test poses you plan to use in Studio animations.

## Numbers
- [page](https://create.roblox.com/docs/art/modeling/skin-a-simple-mesh) bone count: **3** (bones in armature so tree moves and rotates at three points)
- [page](https://create.roblox.com/docs/art/modeling/skin-a-simple-mesh) middle bone weight: **0.5** (50% (green) influence from middle bone upward for subtle effect)
- [page](https://create.roblox.com/docs/art/modeling/skin-a-simple-mesh) top bone weight: **0.25** (25% (teal) influence on top leaf area)
- [page](https://create.roblox.com/docs/art/modeling/skin-a-simple-mesh) bottom bone weight: **1.0** (full red influence on trunk and entire tree)

## Tools
Blender 3.0, Roblox Studio, FBX export

## He points to
- Rig a simple mesh (Roblox docs)
- Object Modes (Blender docs)

## Topics
[[3d-modeling-rigging-and-animation]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
