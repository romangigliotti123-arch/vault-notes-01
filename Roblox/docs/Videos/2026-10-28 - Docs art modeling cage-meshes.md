---
title: "Docs: art / modeling / cage-meshes"
url: https://create.roblox.com/docs/art/modeling/cage-meshes.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: art / modeling / cage-meshes

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/art/modeling/cage-meshes.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs on cage meshes: invisible wrapping surfaces on MeshParts that let paired meshes deform over each other. Pairing is by shared UV coordinates, not position. Covers WrapTarget/WrapLayer components, Blender setup (_OuterCage/_InnerCage), and the Uses Cages import option.

## Tips
- [page](https://create.roblox.com/docs/art/modeling/cage-meshes) **[[building-art-and-assets]]** Enable "Uses Cages" in the 3D Importer when importing a model with cage meshes so Studio creates the cage objects.
- [page](https://create.roblox.com/docs/art/modeling/cage-meshes) **[[building-art-and-assets]]** All targets and layers that pair with each other must share identical UV maps; cages pair by UV coordinates, not position.
- [page](https://create.roblox.com/docs/art/modeling/cage-meshes) **[[3d-modeling-rigging-and-animation]]** In Blender, a target needs a render mesh with one _OuterCage mesh; a layer needs a render mesh with _InnerCage and _OuterCage meshes.
- [page](https://create.roblox.com/docs/art/modeling/cage-meshes) **[[3d-modeling-rigging-and-animation]]** Start from Roblox's provided reference cages when creating a layered accessory rather than building cages from scratch.

## Tools
Blender, Maya, Roblox Studio 3D Importer

## Topics
[[3d-modeling-rigging-and-animation]] [[building-art-and-assets]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
