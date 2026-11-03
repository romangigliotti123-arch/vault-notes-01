---
type: research-source
id: web-1fc8c14e04
title: "Roblox docs: avatar/rigid-accessories/specifications"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/avatar/rigid-accessories/specifications.md"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0044
relevance: 2
density: high
tags: ["research-source", "web", "avatar-ugc-accessories", "blender-roblox-export-import", "mesh-texture-limits", "rigging-animation"]
---
# web-1fc8c14e04

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox rigid accessory spec page: single watertight mesh, 4k triangle cap, quads preferred, per-body-scale size limits (Normal/Slender/Classic) with Importer Rig Scale mapping, 2048x2048 texture cap, attachment naming, Marketplace material and vertex color rules. Contains no Blender bpy, MCP, or Claude workflow content; export details are on a separate page.

## Claims
- c1: Rigid accessories must be a single mesh, cannot exceed 4k triangles, and must be watertight with no exposed holes or backfaces. *(doc, high; mesh-texture-limits)*
- c2: Rigid accessory textures for Marketplace assets cannot exceed 2048x2048; high-res textures are auto-downscaled. *(doc, high; mesh-texture-limits)*
- c3: Body scales are Normal, Slender, and Classic; Importer Rig Scale Rthro maps to Normal, Rthro Narrow to Slender, Default to Classic. *(doc, high; avatar-ugc-accessories)*
- c4: Shoulder attachments via RightShoulderAttachment/LeftShoulderAttachment move with the arm; Collar attachments do not. *(doc, high; rigging-animation)*
- c5: Marketplace rigid accessories need Material Plastic, Transparency 0, VertexColor 1,1,1, and no extra Script or Part objects in the Accessory. *(doc, high; avatar-ugc-accessories)*
- c6: Importing third-party attachment objects is not supported for rigid accessories (supported for character bodies). *(doc, high; avatar-ugc-accessories)*
- c7: Rigid accessories are modeled in Blender or Maya against a mannequin; export settings are on a separate export page. *(doc, medium; blender-roblox-export-import)*
- c8: Classic hat box is 3x4x3 studs; Normal hat is 1.87x2.5x1.87; Slender hat is 1.78x2.5x1.78. *(doc, high; avatar-ugc-accessories)*
- c9: Normal mannequin is roughly 5.75-6.5 studs tall; Slender 5.25-6.25; Classic about 4.75. *(doc, medium; avatar-ugc-accessories)*
- c10: Use quads where possible and avoid faces with 5 or more sides. *(doc, high; mesh-texture-limits)*

## Numbers
- n1: **Triangle budget**: 4k max per rigid accessory Rigid accessories can't exceed 4k triangles
- n2: **Max texture resolution**: 2048x2048 Marketplace rigid accessory textures
- n3: **Normal Hat max size**: 1.87 x 2.5 x 1.87 studs Width x Height x Depth, Rthro Normal
- n4: **Slender Hat max size**: 1.78 x 2.5 x 1.78 studs Rthro Narrow
- n5: **Classic Hat max size**: 3 x 4 x 3 studs Default rig scale
- n6: **Normal Back max size**: 9.86 x 8.59 x 4.87 studs Not centered: 1.623 front, 3.246 behind
- n7: **Classic Back max size**: 10 x 7 x 4.5 studs Not centered: 1.5 front, 3 behind
- n8: **Normal Waist max size**: 3.94 x 4.29 x 7.57 studs Not centered: 1.842 up, 2.457 down
- n9: **Normal Hair max size**: 1.87 x 3.12 x 2.18 studs Not centered vertically: 1.25 up, 1.875 down

## Techniques
- t1: **Mannequin-based sizing**: Import downloadable mannequin via Importer, choose Rig Scale (Rthro / Rthro Narrow / Default), model accessory within size bounds, check with Accessory Fitting Tool.
- t2: **Attachment naming for manual setup**: Name Class.Attachment per accessory type (HatAttachment, HairAttachment, BodyBackAttachment, Waist*, Shoulder/Collar/NeckAttachment, Face*, BodyFrontAttachment); AFT generates these automatically.

## Quotes (brief, for attribution)
> Rigid accessories can't exceed 4k triangles.  (create.roblox.com)
> Items using RightShoulderAttachment or LeftShoulderAttachment move with the character's arm.  (create.roblox.com)

## Points to
- https://www.blender.org/
- https://www.autodesk.com/products/maya/overview
- ../../avatar/accessory-fitting-tool.md
- ../../studio/importer.md
- ../../art/modeling/texture-specifications.md
- ../../marketplace/marketplace-policy.md
