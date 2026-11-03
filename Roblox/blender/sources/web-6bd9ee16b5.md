---
type: research-source
id: web-6bd9ee16b5
title: "Roblox docs: art/modeling/index"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/art/modeling/index.md"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0032
relevance: 2
density: low
tags: ["research-source", "web", "automation-and-creator-workflows", "avatar-ugc-accessories", "blender-roblox-export-import", "claude-blender-ai", "mesh-texture-limits", "rigging-animation"]
---
# web-6bd9ee16b5

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox docs overview of custom 3D assets: MeshPart import from modeling tools like Blender, mesh types, rigging/skinning, PBR textures, and Studio auto-created objects (Attachment, WrapTarget, WrapLayer, FaceControls) driven by naming suffixes. Covers no Claude, blender-mcp, or bpy workflows and no concrete export settings or triangle limits.

## Claims
- c1: Roblox custom 3D assets are imported as Class.MeshPart objects (descendants of BasePart); a basic asset needs at least one MeshPart plus one texture image. *(doc, high; mesh-texture-limits)*
- c2: Studio 3D Importer auto-creates Attachment from mesh names ending in _Att. *(doc, high; blender-roblox-export-import)*
- c3: Names ending in _OuterCage create WrapTarget; _InnerCage plus matching _OuterCage create WrapLayer. *(doc, high; blender-roblox-export-import)*
- c4: Studio auto-creates FaceControls when an avatar head mesh and appropriate facial animation data are detected in the model. *(doc, high; avatar-ugc-accessories)*
- c5: Rigged meshes have an internal skeleton; skinning lets mesh bend at joints instead of rotating rigidly on one axis. *(doc, high; rigging-animation)*
- c6: PBR textures use multiple maps (color, roughness, reflectivity) on one asset via SurfaceAppearance. *(doc, high; mesh-texture-limits)*
- c7: Three mesh application types: environment decoration, individual body parts for avatars/NPCs, and cosmetic accessories; each must meet its own specs. *(doc, high; avatar-ugc-accessories)*
- c8: Roblox docs list Calisthenics Tool and Clothing Validation Tool for testing/validation; Accessory Fitting Tool and automatic skinning transfer also documented. *(doc, medium; automation-and-creator-workflows)*
- c9: Creators can sell model collections parented to one Model on Creator Store and keep 100% of net proceeds, per the doc. *(doc, medium; automation-and-creator-workflows)*
- c10: The source does not mention blender-mcp, bpy scripting, or Claude; it only names Blender as a third-party modeling app. *(doc, high; claude-blender-ai)*

## Numbers
- n1: **Creator Store net proceeds**: 100% Sell models on Creator Store, earn 100% of net proceeds per transaction
- n2: **Mesh types**: 3 Environment, body parts, cosmetic accessories

## Techniques
- t1: **Name-suffix object creation**: Name mesh objects with _Att, _OuterCage, or _InnerCage/_OuterCage suffixes so the 3D Importer creates Attachment, WrapTarget, or WrapLayer objects on import.

## Points to
- https://www.blender.org
- https://www.autodesk.com/products/maya/overview
- art/modeling/specifications.md
- art/modeling/export-requirements.md
- art/modeling/rigging.md
- art/modeling/surface-appearance.md
- art/modeling/cage-meshes/index.md
- avatar/automatic-skinning-transfer.md
- avatar/accessory-fitting-tool.md
- art/modeling/calisthenics-tool.md
