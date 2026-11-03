---
type: research-source
id: web-04cef4e0ee
title: "Roblox docs: avatar/layered-accessories/specifications"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/avatar/layered-accessories/specifications.md"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0022
relevance: 3
density: high
tags: ["research-source", "web", "automation-and-creator-workflows", "avatar-ugc-accessories", "blender-roblox-export-import", "mesh-texture-limits", "rigging-animation"]
---
# web-04cef4e0ee

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox official spec page for layered accessories (clothing-layering meshes) for Studio compatibility. Covers single-mesh requirement, 4k triangle budget, watertight geometry, mesh size limits per asset type, 2048x2048 texture cap for Marketplace, required attachment names, R15 rigging with max 4 bone influences per vertex, and inner/outer cage naming. Source does not cover Blender MCP, bpy scripting, or rigid-accessory import settings.

## Claims
- c1: Layered accessories must be a single mesh and cannot exceed 4k (4000) triangles. *(doc, high; mesh-texture-limits)*
- c2: All geometry must be watertight with no exposed holes or backfaces; use quads where possible, avoid faces with 5+ sides. *(doc, high; mesh-texture-limits)*
- c3: Max mesh size centered on attachment: clothing types 8x8x8 studs; eyebrow/eyelashes 1.5 x 0.5 x 0.5 studs. *(doc, high; mesh-texture-limits)*
- c4: Marketplace layered accessory textures cannot exceed 2048x2048; higher-res textures are auto-downscaled. *(doc, high; mesh-texture-limits)*
- c5: Attachment names are fixed per accessory type (e.g., Layered tops use BodyFrontAttachment; layered bottoms use WaistCenterAttachment); Accessory Fitting Tool generates them automatically. *(doc, high; avatar-ugc-accessories)*
- c6: Importer treats mesh objects with the _Att affix as attachment points, only when importing caged meshes. *(doc, medium; avatar-ugc-accessories)*
- c7: Eyebrows and eyelashes cannot be uploaded standalone; must be bundled with a character body or makeup asset, named EyebrowAccessory, EyelashAccessory, HairAccessory. *(doc, high; avatar-ugc-accessories)*
- c8: Layered accessories must be weighted and bound to an R15 armature; max 4 bone assignments (Blender) / joint influences (Maya) per vertex. *(doc, high; rigging-animation)*
- c9: Layered accessories need an inner cage (named <AccessoryName>_InnerCage) and outer cage (<AccessoryName>_OuterCage); outer cage starts identical to inner and is the only one to adjust; cage vertices/UVs must not be deleted. *(doc, high; avatar-ugc-accessories)*
- c10: Character bodies must include an outer cage to be layered-accessory compatible. *(doc, high; avatar-ugc-accessories)*
- c11: Marketplace upload checks: MeshPart Material Plastic, Transparency 0, VertexColor 1,1,1, and no extra Script or Part objects in the Accessory. *(doc, high; automation-and-creator-workflows)*
- c12: Automatic skinning transfer can generate accessory skinning data at runtime as an alternative to manual weighting. *(doc, medium; automation-and-creator-workflows)*
- c13: Export settings for Blender and Maya are documented on a separate export page; layered accessories are exported as .fbx and converted to an Accessory via the Accessory Fitting Tool. *(doc, high; blender-roblox-export-import)*

## Numbers
- n1: **Triangle budget**: <=4k triangles 
- n2: **Clothing max mesh size (X,Y,Z)**: 8 x 8 x 8 studs 
- n3: **Eyebrow/eyelash max size (X,Y,Z)**: 1.5 x 0.5 x 0.5 studs 
- n4: **Marketplace texture max**: 2048x2048 
- n5: **Max bone influences per vertex**: 4 
- n6: **Attachments required**: at least 1 

## Techniques
- t1: **Caging setup**: Duplicate Roblox template inner cage; name it <Accessory>_InnerCage. Match outer cage shape to inner first, then edit only the outer cage (<Accessory>_OuterCage) to fully cover the asset. Do not delete cage verts/UVs.
- t2: **Skin with bone limit**: Weight and bind the accessory to R15 armature in Blender (Automatic Weights) or Maya; cap per-vertex bone assignments at 4.

## Quotes (brief, for attribution)
> Layered accessories can't exceed 4k triangles.  (create.roblox.com)
> Eyebrows and eyelashes cannot be uploaded as standalone accessories and must be bundled either with a character body or makeup assets.  (create.roblox.com)

## Points to
- https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/avatar/layered-accessories/export.md
- https://github.com/Roblox/creator-docs/blob/main/content/en-us/avatar/layered-accessories/caging-best-practices.md
- https://www.blender.org/
- https://docs.blender.org/manual/en/latest/animation/armatures/skinning/parenting.html#with-automatic-weights
