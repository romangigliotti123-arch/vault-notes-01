---
type: research-source
id: off-avatar_layered-accessories_index
title: "Roblox Creator Docs: avatar_layered-accessories_index"
source_type: "web"
creator: "create.roblox.com"
url: "https://create.roblox.com/docs/avatar/layered-accessories/index"
published: "2026-10-31"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0018
relevance: 3
density: medium
tags: ["research-source", "web", "automation-and-creator-workflows", "avatar-ugc-accessories", "blender-roblox-export-import"]
---
# off-avatar_layered-accessories_index

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox Creator Docs overview of layered accessories (layered clothing): 3 layers (mesh/textures, rigging armature, cage meshes and attachments). Explains Studio classes (MeshPart in Model, SurfaceAppearance/TextureID, WrapLayer cages, Attachment), export as single .fbx or .gltf from Blender/Maya, and Avatar Setup tool. Mostly conceptual; little Blender-specific scripting.

## Claims
- c1: Layered accessories stretch and fit over any body type using rigging armature and cage meshes; three main layers: mesh and textures, rigging armature, cage meshes and attachments. *(doc, high; avatar-ugc-accessories)*
- c2: In Studio, cage meshes are represented by WrapLayer objects (inner cage = inside surface where clothes wrap; outer cage = surface other layers wrap over). *(doc, high; avatar-ugc-accessories)*
- c3: Attachments (Class.Attachment) set which body part the accessory attaches to when the body ragdolls or dismembers. *(doc, high; avatar-ugc-accessories)*
- c4: All avatar components must be exported together in a single .fbx or .gltf file for import into Studio. *(doc, high; blender-roblox-export-import)*
- c5: Textures are set on MeshPart either via child SurfaceAppearance object or the MeshPart.TextureID property. *(doc, high; blender-roblox-export-import)*
- c6: Attachment points can be auto-generated with the Accessory Fitting Tool; the Avatar Setup tool processes imported creations into marketplace-ready avatar assets. *(doc, high; automation-and-creator-workflows)*
- c7: Rigid accessories do not deform and attach to a single point; layered accessories wrap until they fit. *(doc, high; avatar-ugc-accessories)*
- c8: Validation resources include the Calisthenics tool and Clothing validation tool; a basic sweater tutorial in Blender is provided. *(doc, medium; automation-and-creator-workflows)*

## Techniques
- t1: **Single-file export of full avatar**: Model mesh, rig, and cages in Blender or Maya; export all avatar components in one .fbx or .gltf; import to Studio; run Avatar Setup tool.

## Quotes (brief, for attribution)
> you must export all of the avatar components in a single .fbx or .gltf for import into Studio.  (create.roblox.com)

## Points to
- https://www.blender.org/
- https://www.autodesk.com/products/maya/overview
- ../../art/accessories/creating/index.md
- ../../art/modeling/export-requirements.md
- ../../art/accessories/validation-tool.md
- ../accessory-fitting-tool.md
