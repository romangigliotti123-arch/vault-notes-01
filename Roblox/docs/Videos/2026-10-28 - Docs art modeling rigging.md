---
title: "Docs: art / modeling / rigging"
url: https://create.roblox.com/docs/art/modeling/rigging.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: art / modeling / rigging

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/art/modeling/rigging.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on rigging and skinning. Explains rigs and bones (MeshPart influence data, Bone instances, Show Constraint Details), bones don't change collision shape, and the R-naming convention (R1, R15) with when each is appropriate.

## Tips
- [page](https://create.roblox.com/docs/art/modeling/rigging) **[[3d-modeling-rigging-and-animation]]** Skin rigged meshes (bone weights) for organic bending; rigged-only meshes rotate only as rigid parts, not bend naturally.
- [page](https://create.roblox.com/docs/art/modeling/rigging) **[[3d-modeling-rigging-and-animation]]** Assign bone influence in Blender or Maya before import; Roblox saves this weight data to MeshPart on import.
- [page](https://create.roblox.com/docs/art/modeling/rigging) **[[physics-pathfinding-and-npc-ai]]** Bones affect visual appearance only; they do not change collision shape, so collision still uses the original part geometry.
- [page](https://create.roblox.com/docs/art/modeling/rigging) **[[3d-modeling-rigging-and-animation]]** Use R1 rigs for props like trees or accessories; they are cheaper than full characters.

## Numbers
- [page](https://create.roblox.com/docs/art/modeling/rigging) R15 mesh count: **15 meshes parented to one R15 rig** (Standard humanoid rig used for all Roblox avatars)

## Tools
Blender, Maya, Roblox Studio Animation Editor

## Topics
[[3d-modeling-rigging-and-animation]] [[physics-pathfinding-and-npc-ai]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
