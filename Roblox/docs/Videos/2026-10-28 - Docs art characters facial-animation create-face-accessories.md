---
title: "Docs: art / characters / facial-animation / create-face-accessories"
url: https://create.roblox.com/docs/art/characters/facial-animation/create-face-accessories.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: art / characters / facial-animation / create-face-accessories

[Open](https://create.roblox.com/docs/art/characters/facial-animation/create-face-accessories.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs tutorial on creating face accessories (eyebrows, eyelashes, glasses) in Blender/Maya for dynamic heads: rigging to the R15 armature, optional skinning, inner/outer cage creation, export, and testing via the Accessory Fitting Tool in Studio.

## Tips
- [page](https://create.roblox.com/docs/art/characters/facial-animation/create-face-accessories) **[[building-art-and-assets]]** Model face accessories together with the character body model and match accessory edges to head topology; this improves deformation fit.
- [page](https://create.roblox.com/docs/art/characters/facial-animation/create-face-accessories) **[[3d-modeling-rigging-and-animation]]** Parent accessory to the R15 armature with Automatic Weights for faster skinning; use Empty Weights only if you want full manual skinning control.
- [page](https://create.roblox.com/docs/art/characters/facial-animation/create-face-accessories) **[[3d-modeling-rigging-and-animation]]** Combine multi-piece accessories (eyebrows, eyelashes) into a single mesh after modeling and rigging is finished.
- [page](https://create.roblox.com/docs/art/characters/facial-animation/create-face-accessories) **[[3d-modeling-rigging-and-animation]]** Test the accessory on FACS poses saved to the Blender timeline, then adjust skinning weights as needed.
- [page](https://create.roblox.com/docs/art/characters/facial-animation/create-face-accessories) **[[3d-modeling-rigging-and-animation]]** Stretch outer cage vertices to cover the accessory with minimal space; name cages starting with the accessory name before _InnerCage/_OuterCage.
- [page](https://create.roblox.com/docs/art/characters/facial-animation/create-face-accessories) **[[3d-modeling-rigging-and-animation]]** Remove unnecessary cage sections when using Automatic Skinning Transfer so it only affects the intended parts of the accessory.
- [page](https://create.roblox.com/docs/art/characters/facial-animation/create-face-accessories) **[[building-art-and-assets]]** Export only the accessory mesh, armature and cage meshes; remove animation data, lights and cameras before exporting FBX.
- [page](https://create.roblox.com/docs/art/characters/facial-animation/create-face-accessories) **[[testing-debugging-and-qa]]** Test the exported accessory in Studio with the Accessory Fitting Tool and equip it to a humanoid before publishing.

## Numbers
- [page](https://create.roblox.com/docs/art/characters/facial-animation/create-face-accessories) Required rig: **Standard or advanced R15 rig** (Face accessory must be parented or bound to this rig)
- [page](https://create.roblox.com/docs/art/characters/facial-animation/create-face-accessories) Required cages: **Inner and outer cage** (Face accessory must include both cage meshes)
- [page](https://create.roblox.com/docs/art/characters/facial-animation/create-face-accessories) Blender version used: **5.2** (Tutorial version; other versions may differ in UI)

## Tools
Blender, Maya, Roblox Studio, Accessory Fitting Tool, Automatic Skinning Transfer

## He points to
- Create basic dynamic heads
- Automatic Skinning Transfer - Modify character cages
- Blender Automatic Weights documentation
- Layered accessories specifications

## Topics
[[3d-modeling-rigging-and-animation]] [[building-art-and-assets]] [[testing-debugging-and-qa]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
