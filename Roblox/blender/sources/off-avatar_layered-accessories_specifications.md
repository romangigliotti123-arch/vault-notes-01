---
type: research-source
id: off-avatar_layered-accessories_specifications
title: "Roblox Creator Docs: avatar_layered-accessories_specifications"
source_type: "web"
creator: "create.roblox.com"
url: "https://create.roblox.com/docs/avatar/layered-accessories/specifications"
published: "2026-10-31"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0023
relevance: 3
density: high
tags: ["research-source", "web", "automation-and-creator-workflows", "avatar-ugc-accessories", "blender-roblox-export-import", "mesh-texture-limits", "rigging-animation"]
---
# off-avatar_layered-accessories_specifications

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox official spec page for layered accessories (layered clothing). Covers single-mesh requirement, 4k triangle budget, watertightness, mesh size limits (8x8x8 studs for clothing, 1.5x0.5x0.5 for eyebrows/eyelashes), 2048x2048 texture cap for Marketplace, attachment naming per accessory type, inner/outer cage naming (_InnerCage/_OuterCage), R15 skinning with max 4 bone influences per vertex, and Marketplace material/transparency/vertex color rules. Nothing on bpy or blender-mcp.

## Claims
- c1: Layered accessories can't exceed 4k triangles and must be a single mesh. *(doc, high; mesh-texture-limits)*
- c2: Layered accessory Marketplace textures cannot exceed 2048x2048; high-res textures are auto-downscaled. *(doc, high; mesh-texture-limits)*
- c3: Max mesh size for clothing types (shirt, pants, dress etc.) is 8x8x8 studs centered on attachment; eyebrows/eyelashes 1.5x0.5x0.5. *(doc, high; mesh-texture-limits)*
- c4: Geometry must be watertight with no exposed holes or backfaces; use quads, avoid 5+ sided faces. *(doc, high; avatar-ugc-accessories)*
- c5: Layered accessories must be weighted and bound to an R15 armature; max 4 bone influences per vertex (Blender Bone Assignments / Maya Joint Influences). *(doc, high; rigging-animation)*
- c6: Layered accessories need an inner cage (name suffix _InnerCage) and outer cage (suffix _OuterCage); outer cage starts identical to inner and is the only one to adjust. *(doc, high; avatar-ugc-accessories)*
- c7: Cage vertices and UVs must not be deleted; invalid cage configs fail validation and go to moderation. *(doc, high; avatar-ugc-accessories)*
- c8: Attachment names depend on type: e.g. layered tops use BodyFrontAttachment, layered bottoms use WaistCenterAttachment, eyebrow/eyelash use FaceFrontAttachment/FaceCenterAttachment. *(doc, high; avatar-ugc-accessories)*
- c9: Eyebrows and eyelashes cannot be standalone uploads; must be bundled with a character body or makeup asset, named EyebrowAccessory/EyelashAccessory/HairAccessory. *(doc, high; avatar-ugc-accessories)*
- c10: Importer auto-recognizes mesh objects with the _Att affix as attachment points, only when importing caged meshes. *(doc, medium; blender-roblox-export-import)*
- c11: Studio Accessory Fitting Tool (AFT) auto-adds and configures Attachments; automatic skinning transfer can generate skinning at runtime as an alternative to manual weighting. *(doc, high; automation-and-creator-workflows)*
- c12: Marketplace upload needs MeshPart Material=Plastic, Transparency=0, VertexColor=1,1,1, and no extra Script or Part objects in the Accessory. *(doc, high; avatar-ugc-accessories)*
- c13: Export from Blender/Maya as FBX; export setting requirements are on a separate export page. *(doc, medium; blender-roblox-export-import)*

## Numbers
- n1: **triangle budget**: 4k (4000) max 
- n2: **Marketplace texture max**: 2048x2048 
- n3: **clothing max mesh size (X/Y/Z)**: 8 x 8 x 8 studs 
- n4: **eyebrow/eyelash max mesh size (X/Y/Z)**: 1.5 x 0.5 x 0.5 studs 
- n5: **bone influences per vertex**: 4 
- n6: **attachments required**: at least 1 per layered accessory 

## Techniques
- t1: **Cage setup from template**: Start from Roblox template cage meshes in layered accessory project files. Shape inner and outer cage to match, then edit only the outer cage to cover the asset. Do not delete cage vertices or UVs.
- t2: **Manual skinning with limits**: Weight and bind to R15 armature in Blender (Automatic Weights) or Maya. Cap bone assignments per vertex at 4.
- t3: **Naming for cages and attachments**: Name cages as <AccessoryName>_InnerCage and <AccessoryName>_OuterCage. Use the attachment name table for the accessory type; _Att suffix on mesh objects for importer auto-detection.

## Quotes (brief, for attribution)
> Layered accessories can't exceed 4k triangles.  (create.roblox.com)
> Joint Influences (Maya) or Bone Assignments (Blender) per vertex should be limited to 4.  (create.roblox.com)

## Points to
- https://www.blender.org
- https://www.autodesk.com/products/maya/overview
- https://docs.blender.org/manual/en/latest/animation/armatures/skinning/parenting.html#with-automatic-weights
- https://www.youtube.com/watch?v=C-DwGRBHvmE&t=512s
