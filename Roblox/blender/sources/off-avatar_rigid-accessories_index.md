---
type: research-source
id: off-avatar_rigid-accessories_index
title: "Roblox Creator Docs: avatar_rigid-accessories_index"
source_type: "web"
creator: "create.roblox.com"
url: "https://create.roblox.com/docs/avatar/rigid-accessories/index"
published: "2026-10-31"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0015
relevance: 1
density: low
tags: ["research-source", "web", "avatar-ugc-accessories", "blender-roblox-export-import"]
---
# off-avatar_rigid-accessories_index

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox creator doc on rigid accessories: 3D objects attached to avatar attachment points. Two layers: mesh/textures and Attachment objects. Accessories exported as single .fbx or .gltf from Blender or Maya; attachments must meet strict specs; Accessory Fitting Tool can generate attachments. Does not cover bpy, blender-mcp, or Claude workflows.

## Claims
- c1: Rigid accessory has two main layers: mesh and textures, plus Attachment objects that determine attachment to the character body. *(doc, high; avatar-ugc-accessories)*
- c2: Rigid accessory requires a single MeshPart nested under a single Model in Studio. *(doc, high; avatar-ugc-accessories)*
- c3: All avatar components must be exported together in a single .fbx or .gltf file for import into Studio. *(doc, high; blender-roblox-export-import)*
- c4: Accessory Fitting Tool can automatically generate attachment points for rigid accessories. *(doc, high; avatar-ugc-accessories)*
- c5: Textures are applied via a child SurfaceAppearance object or the MeshPart TextureID property. *(doc, high; avatar-ugc-accessories)*

## Points to
- https://create.roblox.com/docs/avatar/rigid-accessories/specifications
- https://create.roblox.com/docs/avatar/accessory-fitting-tool
- https://www.blender.org/
- https://www.autodesk.com/products/maya/overview
