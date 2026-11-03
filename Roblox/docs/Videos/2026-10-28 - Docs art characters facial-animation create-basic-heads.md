---
title: "Docs: art / characters / facial-animation / create-basic-heads"
url: https://create.roblox.com/docs/art/characters/facial-animation/create-basic-heads.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: art / characters / facial-animation / create-basic-heads

[Open](https://create.roblox.com/docs/art/characters/facial-animation/create-basic-heads.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs tutorial on building a dynamic head in Blender: adding a RootFaceJoint and eye/eyelid joints, skinning, building controllers with constraints, posing FACS poses on frames (neutral at frame 0), mapping poses via custom properties, and exporting FBX. Requires 17 specific poses to sell on Marketplace; 50 base poses available.

## Tips
- [page](https://create.roblox.com/docs/art/characters/facial-animation/create-basic-heads) **[[building-art-and-assets]]** Plan the full range of facial poses before rigging so you avoid re-adjusting head joints later.
- [page](https://create.roblox.com/docs/art/characters/facial-animation/create-basic-heads) **[[3d-modeling-rigging-and-animation]]** Keep face joints under 50 where possible; high vertex and joint counts can hurt game performance.
- [page](https://create.roblox.com/docs/art/characters/facial-animation/create-basic-heads) **[[3d-modeling-rigging-and-animation]]** Parent all face joints under a single RootFaceJoint (commonly named DynamicHead) so Studio can locate and hide them on import.
- [page](https://create.roblox.com/docs/art/characters/facial-animation/create-basic-heads) **[[3d-modeling-rigging-and-animation]]** Separate lip vertices so the mouth can open, and model mouth/eye bags to contain teeth, tongue and eye contents.
- [page](https://create.roblox.com/docs/art/characters/facial-animation/create-basic-heads) **[[3d-modeling-rigging-and-animation]]** Ensure face part children of Head_Geo have no history or frozen transformations.
- [page](https://create.roblox.com/docs/art/characters/facial-animation/create-basic-heads) **[[3d-modeling-rigging-and-animation]]** Set frame 0 as the neutral pose with default joint values; save FACS poses starting at frame 1 so Studio can compute differences.
- [page](https://create.roblox.com/docs/art/characters/facial-animation/create-basic-heads) **[[3d-modeling-rigging-and-animation]]** Save one FACS pose per frame; each pose needs its own frame, and each frame must be mapped, or the head fails import.
- [page](https://create.roblox.com/docs/art/characters/facial-animation/create-basic-heads) **[[3d-modeling-rigging-and-animation]]** Save base poses in alphabetical order, then use later frames for combination poses.
- [page](https://create.roblox.com/docs/art/characters/facial-animation/create-basic-heads) **[[3d-modeling-rigging-and-animation]]** Combine 2-3 FACS poses per frame only when they affect different regions; for overlapping regions, add a corrective combination pose to prevent mesh collisions.
- [page](https://create.roblox.com/docs/art/characters/facial-animation/create-basic-heads) **[[3d-modeling-rigging-and-animation]]** Enable Auto Normalize when applying detailed or shared skin influences to prevent joint influence conflicts.
- [page](https://create.roblox.com/docs/art/characters/facial-animation/create-basic-heads) **[[3d-modeling-rigging-and-animation]]** Test each joint's influence in Pose mode by moving it after skinning to confirm the mesh follows correctly.
- [page](https://create.roblox.com/docs/art/characters/facial-animation/create-basic-heads) **[[3d-modeling-rigging-and-animation]]** Set animation Start to 0 and End to the last pose frame when exporting; set Animation Offset to 0 on import to include frame 0.
- [page](https://create.roblox.com/docs/art/characters/facial-animation/create-basic-heads) **[[building-art-and-assets]]** Export FBX with Add Leaf Bones disabled, Custom Properties enabled, and NLA Strips, All Actions and Force Start/End Keyframes unchecked.
- [page](https://create.roblox.com/docs/art/characters/facial-animation/create-basic-heads) **[[3d-modeling-rigging-and-animation]]** Save the head texture separately and apply it as the head part's TextureID after importing into Studio.

## Numbers
- [page](https://create.roblox.com/docs/art/characters/facial-animation/create-basic-heads) Base FACS poses: **50 available** (Roblox base poses for dynamic head expressions)
- [page](https://create.roblox.com/docs/art/characters/facial-animation/create-basic-heads) Required Marketplace poses: **17 specific poses** (Minimum poses needed to sell a dynamic head on Marketplace)
- [page](https://create.roblox.com/docs/art/characters/facial-animation/create-basic-heads) Face joints recommended: **under 50** (Keep face rig joints below this where possible for performance)
- [page](https://create.roblox.com/docs/art/characters/facial-animation/create-basic-heads) Combination pose base poses: **2-3 FACS poses** (Max poses combined in a single frame)
- [page](https://create.roblox.com/docs/art/characters/facial-animation/create-basic-heads) Eye joint tail offset: **0.2 cm on Z** (Tutorial's eye joint Tail Z offset from Head Z)
- [page](https://create.roblox.com/docs/art/characters/facial-animation/create-basic-heads) Tutorial eyelid joints: **8 total** (4 per eye: upper/lower, outer/inner corners)

## Tools
Blender 5.2, Maya, Roblox Studio

## He points to
- Character body specifications - Inner and outer cages
- Test heads in Studio

## Topics
[[3d-modeling-rigging-and-animation]] [[building-art-and-assets]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
