---
title: "Docs: avatar / layered-accessories / specifications"
url: https://create.roblox.com/docs/avatar/layered-accessories/specifications.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: avatar / layered-accessories / specifications

[Open](https://create.roblox.com/docs/avatar/layered-accessories/specifications.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs spec for layered accessories: geometry and triangle budgets, size limits, texture caps, attachment naming, face accessory bundling, rigging limits, inner/outer cage requirements, and Marketplace upload requirements.

## Tips
- [page](https://create.roblox.com/docs/avatar/layered-accessories/specifications) **[[building-art-and-assets]]** Keep layered accessories a single mesh, at most 4k triangles, watertight with no exposed holes or backfaces; prefer quads and avoid faces with 5+ sides.
- [page](https://create.roblox.com/docs/avatar/layered-accessories/specifications) **[[building-art-and-assets]]** Keep layered clothing within 8 x 8 x 8 studs (centered on attachment point); eyebrows and eyelashes within 1.5 x 0.5 x 0.5 studs.
- [page](https://create.roblox.com/docs/avatar/layered-accessories/specifications) **[[building-art-and-assets]]** Keep Marketplace layered accessory textures at or below 2048x2048; higher resolutions are auto-downscaled.
- [page](https://create.roblox.com/docs/avatar/layered-accessories/specifications) **[[3d-modeling-rigging-and-animation]]** Limit skinning to 4 joint influences (Maya) or bone assignments (Blender) per vertex.
- [page](https://create.roblox.com/docs/avatar/layered-accessories/specifications) **[[3d-modeling-rigging-and-animation]]** Weight and bind layered accessories to an R15 rig armature; include both inner and outer cage meshes named AccessoryName_InnerCage and AccessoryName_OuterCage.
- [page](https://create.roblox.com/docs/avatar/layered-accessories/specifications) **[[3d-modeling-rigging-and-animation]]** Never delete vertices or UVs from inner/outer cage meshes; keep outer cage identical to inner cage until fitted, matching shapes before expanding the outer cage.
- [page](https://create.roblox.com/docs/avatar/layered-accessories/specifications) **[[building-art-and-assets]]** Use Studio's Accessory Fitting Tool to auto-generate correct attachment names; manually use the names listed per accessory type (e.g. BodyFrontAttachment for tops, WaistCenterAttachment for bottoms).
- [page](https://create.roblox.com/docs/avatar/layered-accessories/specifications) **[[building-art-and-assets]]** Set MeshPart Material to Plastic, Transparency to 0, and VertexColor to 1,1,1; remove scripts and extra parts from the Accessory before Marketplace upload.
- [page](https://create.roblox.com/docs/avatar/layered-accessories/specifications) **[[common-mistakes]]** Invalid cage configurations fail validation and can be subject to moderation; fix caging issues before uploading.
- [page](https://create.roblox.com/docs/avatar/layered-accessories/specifications) **[[ugc-and-avatar-economy]]** Eyebrows and eyelashes cannot be uploaded standalone; bundle them with a character body or makeup asset, using EyebrowAccessory, EyelashAccessory, HairAccessory names.

## Numbers
- [page](https://create.roblox.com/docs/avatar/layered-accessories/specifications) Max triangles: **4k per layered accessory** (Layered accessory polycount budget)
- [page](https://create.roblox.com/docs/avatar/layered-accessories/specifications) Max mesh size (tops/bottoms/dresses): **8 x 8 x 8 studs** (Shirt, Pants, Jacket, Dress etc., centered on attachment)
- [page](https://create.roblox.com/docs/avatar/layered-accessories/specifications) Max mesh size (eyebrow/eyelash): **1.5 x 0.5 x 0.5 studs** (Centered on attachment point)
- [page](https://create.roblox.com/docs/avatar/layered-accessories/specifications) Max texture resolution (Marketplace): **2048x2048** (Layered accessory textures for Marketplace assets)
- [page](https://create.roblox.com/docs/avatar/layered-accessories/specifications) Max bone influences per vertex: **4** (Joint Influences (Maya) or Bone Assignments (Blender))
- [page](https://create.roblox.com/docs/avatar/layered-accessories/specifications) Attachments per accessory: **At least 1** (Attachment to associated body part)

## Tools
Accessory Fitting Tool (AFT), Blender, Maya, Roblox Studio Importer

## He points to
- Create your first layered accessory
- Accessory Fitting Tool
- Caging best practices
- Publish bodies with eyelashes and eyebrows
- Skin a simple mesh tutorial

## Topics
[[3d-modeling-rigging-and-animation]] [[building-art-and-assets]] [[common-mistakes]] [[ugc-and-avatar-economy]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
