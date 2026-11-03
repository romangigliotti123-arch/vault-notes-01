---
title: "Docs: art / characters / creating / export-textures"
url: https://create.roblox.com/docs/art/characters/creating/export-textures.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: art / characters / creating / export-textures

[Open](https://create.roblox.com/docs/art/characters/creating/export-textures.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox official docs page on exporting character textures from Blender for Studio import. Covers embedding textures in the .fbx (reconfiguring custom skin tone shader nodes to a Color node connected to Base Color) versus unpacking textures as separate .png files for quicker swapping.

## Tips
- [page](https://create.roblox.com/docs/art/characters/creating/export-textures) **[[building-art-and-assets]]** Test character assets multiple times at every stage, both inside Blender and after importing into Studio, not just at final export.
- [page](https://create.roblox.com/docs/art/characters/creating/export-textures) **[[3d-modeling-rigging-and-animation]]** Before embedding textures in the .fbx, set custom skin tone shader nodes so a Color node connects directly to Principled BSDF Base Color; default Mix node setup won't export correctly.
- [page](https://create.roblox.com/docs/art/characters/creating/export-textures) **[[building-art-and-assets]]** Choose texture workflow by need: embed textures for a single self-contained .fbx that simplifies import; unpack to .png when you need to test and swap texture maps quickly.
- [page](https://create.roblox.com/docs/art/characters/creating/export-textures) **[[3d-modeling-rigging-and-animation]]** To unpack textures in Blender use File > External Data > Unpack Resources, then choose Use files in current directory to write them to a textures folder beside the project.

## Numbers
- [page](https://create.roblox.com/docs/art/characters/creating/export-textures) Texture maps on template character: **4 separate image maps (including default PBR textures)**

## Tools
Blender, Roblox Studio, Principled BSDF shader node

## He points to
- Test character bodies (Roblox docs)

## Topics
[[3d-modeling-rigging-and-animation]] [[building-art-and-assets]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
