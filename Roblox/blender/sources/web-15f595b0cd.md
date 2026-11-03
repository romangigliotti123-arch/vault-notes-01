---
type: research-source
id: web-15f595b0cd
title: "Roblox docs: avatar/layered-accessories/export"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/avatar/layered-accessories/export.md"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0014
relevance: 2
density: medium
tags: ["research-source", "web", "avatar-ugc-accessories", "blender-roblox-export-import", "other"]
---
# web-15f595b0cd

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox doc on exporting layered accessories from Blender and Maya as FBX (or glTF) for Studio. Gives Blender steps (Copy path mode, Embed Textures, FBX Unit Scale, uncheck Add Leaf Bones) and Maya steps (Smooth Mesh, Referenced Asset Content, Automatic units, Y up). Requires armature parent with cage parent containing inner and outer cages. Import as Class.Model, then Accessory Fitting Tool. No Claude/blender-mcp/bpy content.

## Claims
- c1: Blender layered accessory FBX export: File > Export > FBX; Path Mode Copy; enable Embed Textures; Apply Scalings = FBX Unit Scale; uncheck Add Leaf Bones in Armature section. *(doc, high; blender-roblox-export-import)*
- c2: Maya layered accessory FBX export: Geometry enable Smooth Mesh and Referenced Asset Content; Embed Media only if textures needed as PNG; Units Automatic; Up Axis = Y. *(doc, high; blender-roblox-export-import)*
- c3: Layered accessory structure: Armature parent (bones + primary mesh) and Cage parent (inner and outer cage meshes). Each shoe needs its own inner and outer cage. *(doc, high; avatar-ugc-accessories)*
- c4: Shoes can be exported individually or together under one armature with left/right shoe meshes and four cage meshes. *(doc, high; avatar-ugc-accessories)*
- c5: After importing the .fbx into Studio as a Class.Model, use the Accessory Fitting Tool to convert it into an accessory. *(doc, high; avatar-ugc-accessories)*
- c6: Apply or delete all modifiers and export only Roblox-supported objects before export. *(doc, high; blender-roblox-export-import)*
- c7: Source does not cover Claude, blender-mcp, or bpy scripting; relevance to the topic is limited to export settings. *(doc, high; other)*

## Techniques
- t1: **Blender layered accessory FBX export**: File>Export>FBX; Path Mode Copy; Embed Textures on; Apply Scalings FBX Unit Scale; Armature: uncheck Add Leaf Bones; Export FBX.
- t2: **Maya layered accessory FBX export**: File>Export All; Files of type FBX export; Geometry: Smooth Mesh + Referenced Asset Content; Units Automatic; Axis Up = Y; Export All.

## Quotes (brief, for attribution)
> Each shoe must include their own inner and outer cage.  (create.roblox.com)

## Points to
- Blender FBX scaling: ../../art/blender.md#adjust-scale-fbx
- Layered accessory specifications: ./specifications.md
- Studio Importer: ../../studio/importer.md
- Accessory Fitting Tool: ../../avatar/accessory-fitting-tool.md
- General mesh export: ../../art/modeling/export-requirements.md
- Rigid accessory export: ../rigid-accessories/export.md
