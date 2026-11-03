---
title: "Docs: art / modeling / skin-a-humanoid-model"
url: https://create.roblox.com/docs/art/modeling/skin-a-humanoid-model.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: art / modeling / skin-a-humanoid-model

[Open](https://create.roblox.com/docs/art/modeling/skin-a-humanoid-model.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Official Roblox docs guide on skinning a humanoid R15 model in Blender 3.0: setting up bone visualization (Sticks) and Auto Normalize, then weight painting head, hand, lower arm, upper arm, and shoulder meshes, and exporting to FBX.

## Tips
- [page](https://create.roblox.com/docs/art/modeling/skin-a-humanoid-model) **[[building-art-and-assets]]** Set armature Display As to Sticks in Object Data Properties to keep bones from obstructing weight painting.
- [page](https://create.roblox.com/docs/art/modeling/skin-a-humanoid-model) **[[3d-modeling-rigging-and-animation]]** Enable Auto Normalize in Weight Paint Tool options so each vertex stays fully influenced by one bone and mistakes are easy to spot.
- [page](https://create.roblox.com/docs/art/modeling/skin-a-humanoid-model) **[[3d-modeling-rigging-and-animation]]** Never apply influences to the Root or HumanoidRootNode bones; added influences are dropped on import into Studio.
- [page](https://create.roblox.com/docs/art/modeling/skin-a-humanoid-model) **[[3d-modeling-rigging-and-animation]]** Studio does not support more than 4 bones influencing a single vertex; check for this in complex rigs or when Auto Normalize is off.
- [page](https://create.roblox.com/docs/art/modeling/skin-a-humanoid-model) **[[3d-modeling-rigging-and-animation]]** Set brush strength to 1 for joint areas like neck, wrist and elbow; use about 0.25 for subtle shoulder/torso influence.
- [page](https://create.roblox.com/docs/art/modeling/skin-a-humanoid-model) **[[3d-modeling-rigging-and-animation]]** Test each weight set by selecting a bone and pressing R to rotate it, checking the bend before moving on.
- [page](https://create.roblox.com/docs/art/modeling/skin-a-humanoid-model) **[[3d-modeling-rigging-and-animation]]** Hide neighboring meshes in the Outliner to access vertices at joints such as the neckline, wrist, and elbow.
- [page](https://create.roblox.com/docs/art/modeling/skin-a-humanoid-model) **[[common-mistakes]]** Selecting the wrong bone while weight painting is a common error; confirm the active bone name shown in the viewport before painting.
- [page](https://create.roblox.com/docs/art/modeling/skin-a-humanoid-model) **[[3d-modeling-rigging-and-animation]]** Expect a candy-wrapper volume loss at the shoulder at full arm range; it may not be avoidable in many cases.
- [page](https://create.roblox.com/docs/art/modeling/skin-a-humanoid-model) **[[ugc-and-avatar-economy]]** Models without inner and outer cage mesh data cannot equip layered accessories.
- [page](https://create.roblox.com/docs/art/modeling/skin-a-humanoid-model) **[[building-art-and-assets]]** Export the skinned model as FBX using Blender export settings for use in Studio.
- [page](https://create.roblox.com/docs/art/modeling/skin-a-humanoid-model) **[[3d-modeling-rigging-and-animation]]** Extra skinned bones not named as Humanoid bones (e.g. fingers) import as Class.Bone with their Blender names, giving extra control.

## Numbers
- [page](https://create.roblox.com/docs/art/modeling/skin-a-humanoid-model) Max bones influencing one vertex in Studio: **4**
- [page](https://create.roblox.com/docs/art/modeling/skin-a-humanoid-model) Brush strength for head/hand/elbow painting: **1**
- [page](https://create.roblox.com/docs/art/modeling/skin-a-humanoid-model) Brush strength for shoulder/upper torso painting: **0.25**
- [page](https://create.roblox.com/docs/art/modeling/skin-a-humanoid-model) Blender version used in guide: **3.0**

## Tools
Blender 3.0, Roblox Studio

## He points to
- Rig a humanoid model (Roblox docs)
- Skin a simple mesh (Roblox docs)
- Blender Character Rigging fundamentals guide
- Blender Vertex Groups fundamentals guide
- Blender Auto Normalize documentation

## Topics
[[3d-modeling-rigging-and-animation]] [[building-art-and-assets]] [[common-mistakes]] [[ugc-and-avatar-economy]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
