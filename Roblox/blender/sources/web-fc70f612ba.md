---
type: research-source
id: web-fc70f612ba
title: "Roblox docs: avatar/dynamic-heads/index"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/avatar/dynamic-heads/index.md"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0018
relevance: 2
density: medium
tags: ["research-source", "web", "automation-and-creator-workflows", "avatar-ugc-accessories", "blender-roblox-export-import", "claude-blender-ai", "mesh-texture-limits", "rigging-animation"]
---
# web-fc70f612ba

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox creator docs overview of dynamic heads: four layers (mesh/textures, face animation data as FaceControls, cage meshes as WrapTarget, attachments), required single MeshPart under Model, 15 cage objects and 19 attachment points, export all components as single .fbx or .gltf from Blender/Maya, then Avatar Setup tool in Studio for Marketplace. Says nothing about blender-mcp, bpy, or Claude.

## Claims
- c1: Dynamic heads require a single mesh object, a MeshPart nested under a single Model in Studio. *(doc, high; avatar-ugc-accessories)*
- c2: Each avatar character must include 15 cage objects (one per body part, including the dynamic head) and 19 attachment points. *(doc, high; avatar-ugc-accessories)*
- c3: Facial animation data is represented in Studio by a FaceControls instance; poses are mapped as custom properties on Head_Geo (Extra Attributes in Maya). *(doc, high; rigging-animation)*
- c4: Outer cage meshes are represented in Studio by WrapTarget instances; deviating from Roblox's standard body cage mesh by adding or removing vertices can break accessory deformation and import. *(doc, high; avatar-ugc-accessories)*
- c5: All avatar components must be exported together in a single .fbx or .gltf file for import into Studio. *(doc, high; blender-roblox-export-import)*
- c6: After importing a custom head with a character body, the Avatar Setup tool in Studio processes it into an avatar asset for Marketplace sale. *(doc, high; automation-and-creator-workflows)*
- c7: Textures are applied via a child SurfaceAppearance object or the MeshPart.TextureID property; MeshPart.Color combined with texture opacity can create skin tones. *(doc, high; mesh-texture-limits)*
- c8: The source does not mention blender-mcp, bpy scripting, or Claude; it only names Blender and Maya as modeling tools. *(doc, high; claude-blender-ai)*

## Numbers
- n1: **cage objects required**: 15 one per body part, including dynamic head
- n2: **attachment points required**: 19 per avatar character, including dynamic head

## Techniques
- t1: **Single-file export**: Model all avatar components in Blender or Maya, then export together as one .fbx or .gltf for Studio import.
- t2: **Pose mapping via custom properties**: Save each facial pose as a keyframe in the timeline and map pose names in Head_Geo custom properties (Extra Attributes in Maya).

## Quotes (brief, for attribution)
> you must export all of the avatar components in a single .fbx or .gltf for import into Studio.  (create.roblox.com)
> Removing or adding vertices from this standard mesh can cause issues with how facial accessories deform and import.  (create.roblox.com)

## Points to
- https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/art/characters/facial-animation/create-basic-heads.md
- https://www.blender.org/
- https://www.autodesk.com/products/maya/overview
- specifications.md
- ../../avatar/resources.md#project-files
