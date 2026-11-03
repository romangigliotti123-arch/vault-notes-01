---
title: "Docs: avatar / dynamic-heads"
url: https://create.roblox.com/docs/avatar/dynamic-heads.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: avatar / dynamic-heads

[Open](https://create.roblox.com/docs/avatar/dynamic-heads.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on dynamic heads: defines the four layers (mesh and textures, face animation data, cage meshes, attachments), lists the required components (one MeshPart, 15 cage objects, 19 attachment points), and outlines the creation workflow from Blender/Maya export through Studio Avatar Setup.

## Tips
- [page](https://create.roblox.com/docs/avatar/dynamic-heads) **[[building-art-and-assets]]** Export all avatar components (head, body, cages, attachments) in a single .fbx or .gltf for import into Studio.
- [page](https://create.roblox.com/docs/avatar/dynamic-heads) **[[3d-modeling-rigging-and-animation]]** Start from Roblox's Blender or Maya project files and the basic dynamic head tutorial rather than building the rig from scratch.
- [page](https://create.roblox.com/docs/avatar/dynamic-heads) **[[3d-modeling-rigging-and-animation]]** Cage each body part with Roblox's standard body cage project file; adding or removing cage vertices breaks accessory deformation and import.
- [page](https://create.roblox.com/docs/avatar/dynamic-heads) **[[3d-modeling-rigging-and-animation]]** Keep the R15 Rig and Attachments project file's standardized attachment names; each character needs its 19 attachment points, including on the head.
- [page](https://create.roblox.com/docs/avatar/dynamic-heads) **[[3d-modeling-rigging-and-animation]]** Map each required face pose as a keyframe and name it via the Head_Geo custom property (Extra Attributes in Maya) so the pose maps correctly.
- [page](https://create.roblox.com/docs/avatar/dynamic-heads) **[[ugc-and-avatar-economy]]** Import the head with a character body into Studio and run the Avatar Setup tool to produce a Marketplace-ready avatar asset.
- [page](https://create.roblox.com/docs/avatar/dynamic-heads) **[[ugc-and-avatar-economy]]** Test and validate the dynamic head (Test dynamic heads, Validation process) before uploading to the Marketplace.
- [page](https://create.roblox.com/docs/avatar/dynamic-heads) **[[age-ratings-moderation-and-tos]]** Ensure all created assets follow Roblox Community Standards and applicable Marketplace policies.

## Numbers
- [page](https://create.roblox.com/docs/avatar/dynamic-heads) Cage objects required: **15 body parts, including the dynamic head**
- [page](https://create.roblox.com/docs/avatar/dynamic-heads) Attachment points required per avatar: **19, including those on the dynamic head**
- [page](https://create.roblox.com/docs/avatar/dynamic-heads) Head mesh objects required: **1 MeshPart nested under a single Model**

## Tools
Blender, Maya, Roblox Studio, Avatar Setup tool, Accessory Fitting Tool, R15 Rig and Attachments project file, Body cage project files

## He points to
- Basic dynamic head creation tutorial
- Basic facial accessory creation tutorial
- Dynamic head caging best practices
- FACS pose references
- Dynamic head specifications
- Validation process

## Topics
[[3d-modeling-rigging-and-animation]] [[age-ratings-moderation-and-tos]] [[building-art-and-assets]] [[ugc-and-avatar-economy]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
