---
type: research-source
id: off-art_modeling_index
title: "Roblox Creator Docs: art_modeling_index"
source_type: "web"
creator: "create.roblox.com"
url: "https://create.roblox.com/docs/art/modeling/index"
published: "2026-10-31"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0033
relevance: 2
density: medium
tags: ["research-source", "web", "automation-and-creator-workflows", "avatar-ugc-accessories", "blender-roblox-export-import", "claude-blender-ai", "mesh-texture-limits", "rigging-animation"]
---
# off-art_modeling_index

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox Creator Docs overview of custom 3D assets (meshes) for Studio. Covers MeshPart as the imported mesh class, the three mesh use types, and the basic asset of a MeshPart plus texture. Lists rigging/skinning, PBR, and Studio-related objects auto-created by the 3D Importer from name suffixes (_Att, _OuterCage, _InnerCage). Says nothing about blender-mcp, bpy, or export settings.

## Claims
- c1: Studio's 3D Importer creates an Attachment for mesh objects whose name ends in _Att. *(doc, high; blender-roblox-export-import)*
- c2: Studio creates WrapTarget for mesh objects ending in _OuterCage; WrapLayer when an _InnerCage mesh and a similarly named _OuterCage mesh are present. *(doc, high; blender-roblox-export-import)*
- c3: Studio creates FaceControls when an avatar head model contains appropriate facial animation data. *(doc, high; blender-roblox-export-import)*
- c4: Imported meshes become Class.MeshPart objects, descendants of BasePart; multi-mesh assets are usually grouped under one Model. *(doc, high; blender-roblox-export-import)*
- c5: A basic custom asset needs at least one MeshPart and one texture image; meshes must satisfy general mesh specifications. *(doc, high; mesh-texture-limits)*
- c6: Rigged meshes are MeshParts with an internal skeleton; skinning lets mesh bend at joints instead of rotating rigidly on one axis. *(doc, high; rigging-animation)*
- c7: PBR textures use multiple maps (color, roughness, reflectivity) on one asset via SurfaceAppearance. *(doc, medium; mesh-texture-limits)*
- c8: Character and accessory meshes must meet extra specs for rigging and skinning; accessory validation uses the Clothing Validation Tool and Calisthenics Tool. *(doc, medium; avatar-ugc-accessories)*
- c9: Models can be sold on the Creator Store with 100% of net proceeds to the creator; avatar models on Marketplace earn commission per sale. *(doc, medium; automation-and-creator-workflows)*
- c10: The page does not mention blender-mcp, MCP, Claude, or bpy scripting; it only names Blender and Maya as modeling tools. *(doc, high; claude-blender-ai)*

## Numbers
- n1: **Minimum basic asset composition**: 1 MeshPart + 1 texture 

## Techniques
- t1: **Name-suffix object tagging**: Name mesh objects with _Att, _OuterCage, or _InnerCage in the modeling app so the 3D Importer creates Attachment, WrapTarget, or WrapLayer objects on import.

## Quotes (brief, for attribution)
> you need to use a third-party modeling application like Blender or Maya to design and model meshes, then import them into Studio.  (create.roblox.com)
> Studio automatically converts certain types of objects found in 3D modeling files as specific workspace objects in the game.  (create.roblox.com)

## Points to
- https://www.blender.org
- https://www.autodesk.com/products/maya/overview
- ../../art/modeling/export-requirements.md
- ../../art/modeling/specifications.md
- ../../art/modeling/rigging.md
- ../../art/modeling/surface-appearance.md
- ../../art/modeling/cage-meshes/index.md
- ../../avatar/accessory-fitting-tool.md
- ../../art/accessories/validation-tool.md
- ../../marketplace/marketplace-policy.md
