---
title: "Docs: avatar / rigid-accessories / specifications"
url: https://create.roblox.com/docs/avatar/rigid-accessories/specifications.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: avatar / rigid-accessories / specifications

[Open](https://create.roblox.com/docs/avatar/rigid-accessories/specifications.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs spec for rigid accessories: single mesh, 4k triangle budget, watertight quads, per-body-scale size limits (Normal/Slender/Classic), AvatarPartScaleType values, texture max 2048x2048, required attachment names, and Marketplace material/transparency/vertex color requirements.

## Tips
- [page](https://create.roblox.com/docs/avatar/rigid-accessories/specifications) **[[building-art-and-assets]]** Keep rigid accessories to a single mesh with at most 4k triangles; make all geometry watertight with no holes or backfaces.
- [page](https://create.roblox.com/docs/avatar/rigid-accessories/specifications) **[[building-art-and-assets]]** Use quads wherever possible and avoid faces with 5 or more sides.
- [page](https://create.roblox.com/docs/avatar/rigid-accessories/specifications) **[[3d-modeling-rigging-and-animation]]** Model against a Rthro/Rthro Narrow/Default mannequin imported via the Importer to match Normal, Slender or Classic body scales.
- [page](https://create.roblox.com/docs/avatar/rigid-accessories/specifications) **[[3d-modeling-rigging-and-animation]]** Review accessory specs early and often while modeling, since many requirements must be built in from the start in Blender or Maya.
- [page](https://create.roblox.com/docs/avatar/rigid-accessories/specifications) **[[ugc-and-avatar-economy]]** Use the Accessory Fitting Tool to visualize and adjust accessory fit within the size boundary before publishing.
- [page](https://create.roblox.com/docs/avatar/rigid-accessories/specifications) **[[building-art-and-assets]]** Keep Marketplace accessory textures at or below 2048x2048; larger textures are downscaled automatically.
- [page](https://create.roblox.com/docs/avatar/rigid-accessories/specifications) **[[3d-modeling-rigging-and-animation]]** Let the Accessory Fitting Tool generate attachments; do not import attachment objects from third-party tools for rigid accessories.
- [page](https://create.roblox.com/docs/avatar/rigid-accessories/specifications) **[[3d-modeling-rigging-and-animation]]** Use RightShoulder/LeftShoulder attachments if the item should move with the arm; use Collar attachments if it should stay still.
- [page](https://create.roblox.com/docs/avatar/rigid-accessories/specifications) **[[anti-exploit-and-security]]** Head-attached accessories must sit on the visible head surface; floating attachment points violate Marketplace policy.
- [page](https://create.roblox.com/docs/avatar/rigid-accessories/specifications) **[[ugc-and-avatar-economy]]** Set MeshPart Material to Plastic, Transparency to 0, and VertexColor to 1,1,1; remove extra Scripts or Parts from the Accessory.

## Numbers
- [page](https://create.roblox.com/docs/avatar/rigid-accessories/specifications) Triangle budget: **4k triangles max per rigid accessory** (Applies to all rigid accessories)
- [page](https://create.roblox.com/docs/avatar/rigid-accessories/specifications) Texture resolution: **2048x2048 max for Marketplace accessories** (Higher res auto-converted to lower)
- [page](https://create.roblox.com/docs/avatar/rigid-accessories/specifications) Normal body hat size (W x H x D): **1.87 x 2.5 x 1.87 studs** (Rthro Normal mannequin ~5.75-6.5 studs tall)
- [page](https://create.roblox.com/docs/avatar/rigid-accessories/specifications) Slender body hat size (W x H x D): **1.78 x 2.5 x 1.78 studs** (Rthro Narrow mannequin ~5.25-6.25 studs tall)
- [page](https://create.roblox.com/docs/avatar/rigid-accessories/specifications) Classic body hat size (W x H x D): **3 x 4 x 3 studs** (Classic mannequin ~4.75 studs tall)
- [page](https://create.roblox.com/docs/avatar/rigid-accessories/specifications) Normal body back size (W x H x D): **9.86 x 8.59 x 4.87 studs** (Depth not centered: 1.623 front, 3.246 behind)
- [page](https://create.roblox.com/docs/avatar/rigid-accessories/specifications) Classic body face size (W x H x D): **3 x 2 x 2 studs** (Eyebrow/eyelash size 1.5 x 0.5 x 0.5 across scales)

## Tools
Blender, Maya, Roblox Studio Importer, Accessory Fitting Tool (AFT)

## He points to
- Roblox general mesh specifications
- Layered accessory specifications
- Convert rigid accessories tutorial

## Topics
[[3d-modeling-rigging-and-animation]] [[anti-exploit-and-security]] [[building-art-and-assets]] [[ugc-and-avatar-economy]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
