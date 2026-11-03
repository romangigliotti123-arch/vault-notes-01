---
title: "Roblox How to make Hats/Accessories (from models, parts, & meshes) - Tutorial Series [EP 31]"
url: https://youtu.be/DmsbnwtaVi0
creator: Emancyphur
official: false
advice_density: high
date: 2021-04-23
views: 29999
transcript: auto-captions
confidence: high
tags: [roblox, emancyphur, youtube-learn]
creator_trust: TRUSTED
creator_score: 7.6
---

> [!note] Trust: TRUSTED (credibility audit score 7.6): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Roblox How to make Hats/Accessories (from models, parts, & meshes) - Tutorial Series [EP 31]

[Watch](https://youtu.be/DmsbnwtaVi0) | Emancyphur | 29,999 views | 2021-04-23

## Summary
Tutorial on turning parts, meshes, and models into Roblox accessories (hats): naming the Handle, copying MeshPart/SpecialMesh IDs for the 2021 accessory change, welding parts (manually or via a command-bar script), positioning with attachments, and equipping via ProximityPrompt, ClickDetector, Touched, loops with a real/fake hat folder, and CollectionService tags.

## Tips
- [0:20](https://youtu.be/DmsbnwtaVi0?t=20) **[[building-art-and-assets]]** Name the central part of an accessory exactly 'Handle' (capital H); other names won't equip properly on characters.
- [1:43](https://youtu.be/DmsbnwtaVi0?t=103) **[[common-mistakes]]** Keep all parts inside an accessory unanchored, or the character gets stuck in place.
- [2:24](https://youtu.be/DmsbnwtaVi0?t=144) **[[building-art-and-assets]]** Recreate meshes as MeshPart with copied MeshId and TextureId from SpecialMesh before the 2021 accessory/head change to stay compatible.
- [3:46](https://youtu.be/DmsbnwtaVi0?t=226) **[[building-art-and-assets]]** Pick the most central part of a multi-part model as the Handle so the accessory sits centred on the character's head.
- [6:52](https://youtu.be/DmsbnwtaVi0?t=412) **[[building-art-and-assets]]** Name positioning attachments 'HatAttachment' so the accessory positions identically on both R6 and R15 characters.
- [7:34](https://youtu.be/DmsbnwtaVi0?t=454) **[[building-art-and-assets]]** Weld all accessory parts together; unwelded parts are dropped when the accessory is added to a character, only the Handle transfers.
- [8:15](https://youtu.be/DmsbnwtaVi0?t=495) **[[building-art-and-assets]]** Weld-button auto-welding only joins intersecting parts; manually add WeldConstraints for the rest or use a welding script.
- [18:24](https://youtu.be/DmsbnwtaVi0?t=1104) **[[scripting-and-performance]]** Use Humanoid:AddAccessory rather than parenting accessories to the character; it ensures the accessory works correctly.
- [14:18](https://youtu.be/DmsbnwtaVi0?t=858) **[[first-session-onboarding]]** Equip accessories via ProximityPrompt, ClickDetector, or Touched, then destroy the pickup prompt once equipped.
- [20:15](https://youtu.be/DmsbnwtaVi0?t=1215) **[[scripting-and-performance]]** Clone a 'real' accessory from ServerStorage per player so one hat can be granted to many players; check the character doesn't already have it.
- [22:22](https://youtu.be/DmsbnwtaVi0?t=1342) **[[scripting-and-performance]]** Use CollectionService tags to loop over accessories anywhere in the game, so new hats need only be tagged, not moved into a folder.

## Numbers
- [2:24](https://youtu.be/DmsbnwtaVi0?t=144) Accessory compatibility change: **Roblox planned head/accessory changes around May 2021**
- [6:52](https://youtu.be/DmsbnwtaVi0?t=412) Attachment name shared by R6 and R15: **HatAttachment**

## Tools
Roblox Studio, Build Rig plugin, Command Bar, Explorer, Properties, Model tab (Weld, Show Welds & Constraint Details)

## He points to
- Important links section of video description (GitHub repo and Roblox model with welding script)
- Creator's Roblox Studio tutorial series playlist

## Topics
[[building-art-and-assets]] [[common-mistakes]] [[first-session-onboarding]] [[scripting-and-performance]]

Back to [[Emancyphur - How to make successful Roblox games]]
