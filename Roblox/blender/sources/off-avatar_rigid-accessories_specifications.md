---
type: research-source
id: off-avatar_rigid-accessories_specifications
title: "Roblox Creator Docs: avatar_rigid-accessories_specifications"
source_type: "web"
creator: "create.roblox.com"
url: "https://create.roblox.com/docs/avatar/rigid-accessories/specifications"
published: "2026-10-31"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0026
relevance: 2
density: high
tags: ["research-source", "web", "avatar-ugc-accessories", "blender-roblox-export-import", "claude-blender-ai", "mesh-texture-limits", "rigging-animation"]
---
# off-avatar_rigid-accessories_specifications

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox Creator Docs spec page for rigid accessories: single mesh, 4k tri cap, watertight, body-scale size bounds (Normal/Slender/Classic) per asset type, 2048² Marketplace textures, required attachment names, shoulder vs collar behavior, and Marketplace MeshPart/Accessory requirements. Mentions Blender/Maya only generically; no blender-mcp, bpy, or Claude content.

## Claims
- c1: Rigid accessories must be a single mesh, cannot exceed 4k triangles, must be watertight with no exposed holes or backfaces; prefer quads, avoid 5+ sided faces. *(doc, high; avatar-ugc-accessories)*
- c2: Body scales: Normal (Rthro), Slender (Rthro Narrow), Classic (Default). Import mannequin via Importer Rig Scale to match body scale. *(doc, high; avatar-ugc-accessories)*
- c3: Normal hat max size 1.87 x 2.5 x 1.87 studs; Slender hat 1.78 x 2.5 x 1.78; Classic hat 3 x 4 x 3 studs (centered on attachment). *(doc, high; avatar-ugc-accessories)*
- c4: Normal Back max 9.86 x 8.59 x 4.87 studs; Waist 3.94 x 4.29 x 7.57; Neck 2.95 x 3.68 x 2.16. Full per-type tables exist for all three body scales. *(doc, high; avatar-ugc-accessories)*
- c5: Rigid accessory textures for Marketplace assets cannot exceed 2048x2048; high-res textures are auto-downscaled. *(doc, high; mesh-texture-limits)*
- c6: Each rigid accessory needs at least one Attachment with type-specific names (HatAttachment, HairAttachment, BodyBackAttachment, WaistFront/Center/BackAttachment, NeckAttachment, FaceFront/CenterAttachment, BodyFrontAttachment); AFT generates them automatically. *(doc, high; avatar-ugc-accessories)*
- c7: Shoulder attachments RightShoulderAttachment/LeftShoulderAttachment move with the arm; Collar attachments do not move with the arm. *(doc, high; rigging-animation)*
- c8: Importing attachment objects from third-party tools is not supported for rigid accessories (supported for character bodies). *(doc, high; avatar-ugc-accessories)*
- c9: Marketplace MeshPart requirements: Material Plastic, Transparency 0, VertexColor 1,1,1; Accessory must contain no extra Scripts or Parts. *(doc, high; avatar-ugc-accessories)*
- c10: Export settings for Blender and Maya are documented on a separate export page; the spec page says to apply requirements while modeling in Blender or Maya. *(doc, medium; blender-roblox-export-import)*
- c11: Source does not mention blender-mcp, Claude, bpy scripting, or any AI-assisted Blender workflow. *(doc, high; claude-blender-ai)*

## Numbers
- n1: **max triangles**: 4k rigid accessory triangle budget
- n2: **max texture resolution**: 2048x2048 Marketplace rigid accessory textures
- n3: **Normal hat size**: 1.87 x 2.5 x 1.87 studs X/Y/Z, Rthro Normal
- n4: **Slender hat size**: 1.78 x 2.5 x 1.78 studs Rthro Narrow
- n5: **Classic hat size**: 3 x 4 x 3 studs Default body scale
- n6: **Normal waist size**: 3.94 x 4.29 x 7.57 studs Rthro Normal
- n7: **Classic body mannequin height**: ~4.75 studs Classic mannequin reference
- n8: **Normal mannequin height**: ~5.75-6.5 studs Rthro Normal mannequin

## Techniques
- t1: **Mannequin-based sizing**: Import a Roblox mannequin via Importer Rig Scale (Rthro=Normal, Rthro Narrow=Slender, Default=Classic); model accessory against it within size bounds; check with Accessory Fitting Tool.

## Quotes (brief, for attribution)
> Because you must apply many of these requirements as you're designing and modeling the rigid accessory in a third-party modeling program like Blender or Maya, it's important to review these specifications early and often.  (create.roblox.com)

## Points to
- https://create.roblox.com/docs/avatar/rigid-accessories/export.md
- https://create.roblox.com/docs/avatar/accessory-fitting-tool
- https://create.roblox.com/docs/studio/importer
- https://create.roblox.com/docs/art/modeling/texture-specifications
- https://create.roblox.com/docs/marketplace/marketplace-policy
- https://www.blender.org/
