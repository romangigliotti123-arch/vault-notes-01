---
title: "Docs: art / modeling / assign-textures"
url: https://create.roblox.com/docs/art/modeling/assign-textures.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: art / modeling / assign-textures

[Open](https://create.roblox.com/docs/art/modeling/assign-textures.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on assigning PBR/basic textures to meshes in Blender and Maya so they import into Studio. Covers Principled BSDF material setup, connecting image texture nodes (Color to Base Color, Metallic, Roughness), and normal map wiring via a NormalMap node (Blender) or Bump 2d set to Tangent Space (Maya). Notes makeup assets have separate guidance.

## Tips
- [page](https://create.roblox.com/docs/art/modeling/assign-textures) **[[building-art-and-assets]]** In Blender, the material's Surface must be Principled BSDF; add a new material first if none exists, or textures will not import correctly.
- [page](https://create.roblox.com/docs/art/modeling/assign-textures) **[[3d-modeling-rigging-and-animation]]** Normal map textures must go through a Normal Map node: Image Color to NormalMap Color, then NormalMap Normal to Principled BSDF Normal.
- [page](https://create.roblox.com/docs/art/modeling/assign-textures) **[[3d-modeling-rigging-and-animation]]** In Maya, set the Bump 2d node to Tangent Space Normals when using a normal map on a Standard Surface material.
- [page](https://create.roblox.com/docs/art/modeling/assign-textures) **[[3d-modeling-rigging-and-animation]]** After replacing PBR textures, export the entire model and then import it into Studio following the import instructions.
- [page](https://create.roblox.com/docs/art/modeling/assign-textures) **[[building-art-and-assets]]** Makeup assets have their own texture reassignment process; do not apply this general guide to them.

## Tools
Blender, Maya, Roblox Studio

## He points to
- Reassign textures in Blender and Maya (makeup assets)

## Topics
[[3d-modeling-rigging-and-animation]] [[building-art-and-assets]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
