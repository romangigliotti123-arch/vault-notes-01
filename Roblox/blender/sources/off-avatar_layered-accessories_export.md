---
type: research-source
id: off-avatar_layered-accessories_export
title: "Roblox Creator Docs: avatar_layered-accessories_export"
source_type: "web"
creator: "create.roblox.com"
url: "https://create.roblox.com/docs/avatar/layered-accessories/export"
published: "2026-10-31"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0014
relevance: 2
density: medium
tags: ["research-source", "web", "avatar-ugc-accessories", "blender-roblox-export-import", "other"]
---
# off-avatar_layered-accessories_export

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Official Roblox doc for exporting layered accessories as FBX from Blender or Maya for Studio import as Class.Model, then Accessory Fitting Tool. Gives Blender export steps (FBX Unit Scale, uncheck Add Leaf Bones, embed textures) and Maya steps (Y up, Units Automatic). Specifies armature and cage object hierarchy. No Claude, blender-mcp, or bpy content.

## Claims
- c1: Blender layered accessory FBX export: File > Export > FBX; Path Mode Copy; enable Embed Textures; Apply Scalings = FBX Unit Scale; Armature section uncheck Add Leaf Bones. *(doc, high; blender-roblox-export-import)*
- c2: Maya layered accessory FBX export: Export All; Geometry: Smooth Mesh and Referenced Asset Content; Embed Media optional for PNG textures; Units Automatic; Up Axis Y. *(doc, high; blender-roblox-export-import)*
- c3: Layered accessory structure: armature parent containing bones and primary mesh; cage parent containing inner and outer cage meshes. Shoes can export together but each shoe needs its own inner and outer cage. *(doc, high; avatar-ugc-accessories)*
- c4: Layered accessory FBX imports into Studio as a Class.Model, then Accessory Fitting Tool converts it into an accessory. *(doc, high; avatar-ugc-accessories)*
- c5: Modifiers on mesh or project objects should be applied or deleted before export; only Roblox-supported objects should be exported. *(doc, high; blender-roblox-export-import)*
- c6: Source is an official Roblox doc page; it does not cover blender-mcp, bpy scripting, or Claude usage. *(doc, high; other)*

## Numbers
- n1: **Blender Apply Scalings**: FBX Unit Scale 
- n2: **Shoe cages required**: 4 (inner and outer per shoe) 

## Techniques
- t1: **Blender layered accessory FBX export**: File>Export>FBX; Path Mode Copy; Embed Textures on; Apply Scalings FBX Unit Scale; Armature: uncheck Add Leaf Bones; Export FBX.
- t2: **Maya layered accessory FBX export**: Export All; FBX export; Geometry Smooth Mesh + Referenced Asset Content; Units Automatic; Axis Up = Y; optional Embed Media for PNG.

## Quotes (brief, for attribution)
> Each shoe must include their own inner and outer cage.  (create.roblox.com)

## Points to
- https://create.roblox.com/docs/avatar/layered-accessories/specifications
- https://create.roblox.com/docs/art/blender.md#adjust-scale-fbx
- https://create.roblox.com/docs/avatar/accessory-fitting-tool
- https://create.roblox.com/docs/studio/importer
