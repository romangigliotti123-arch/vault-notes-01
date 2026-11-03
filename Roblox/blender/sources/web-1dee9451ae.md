---
type: research-source
id: web-1dee9451ae
title: "Roblox docs: avatar/rigid-accessories/export"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/avatar/rigid-accessories/export.md"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0013
relevance: 3
density: medium
tags: ["research-source", "web", "avatar-ugc-accessories", "blender-roblox-export-import", "claude-blender-ai"]
---
# web-1dee9451ae

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox docs for exporting rigid accessories to Studio-ready FBX from Blender and Maya. Blender: Path Mode Copy, Embed Textures, Apply Scalings FBX Unit Scale. Maya: Smooth Mesh, Animation off, Units Automatic, Up Axis Y. Import as Class.Model, then Accessory Fitting Tool. No blender-mcp, bpy, or Claude content.

## Claims
- c1: Roblox rigid accessory export from Blender: File > Export > FBX (.fbx); set Path Mode to Copy, enable Embed Textures; Transform > Apply Scalings set to FBX Unit Scale. *(doc, high; blender-roblox-export-import)*
- c2: Apply or delete all modifiers on mesh and project objects before export, per Roblox warning. *(doc, high; blender-roblox-export-import)*
- c3: Blender can export rigid accessories as .fbx or .gltf; FBX scale issues are addressed via linked Blender FBX scaling guidance. *(doc, high; blender-roblox-export-import)*
- c4: Maya FBX export: Smooth Mesh and Referenced Asset Content enabled; Animation disabled; Units Automatic; Up Axis set to Y; Embed Media enabled only if textures must import as .png. *(doc, high; blender-roblox-export-import)*
- c5: Exported rigid accessory .fbx imports into Studio as a Class.Model; then Accessory Fitting Tool converts it into an accessory. *(doc, high; avatar-ugc-accessories)*
- c6: Rigid accessory models must contain mesh, texture and attachment data for correct attachment to character bodies. *(doc, medium; avatar-ugc-accessories)*
- c7: Source does not cover blender-mcp, bpy scripting, or Claude integration; off-topic for AI workflow. *(doc, high; claude-blender-ai)*

## Numbers
- n1: **Blender Path Mode**: Copy 
- n2: **Blender Apply Scalings**: FBX Unit Scale 
- n3: **Maya Up Axis**: Y 

## Techniques
- t1: **Blender FBX export for Roblox rigid accessory**: Apply/delete modifiers. File>Export>FBX. Path Mode Copy, Embed Textures on. Apply Scalings: FBX Unit Scale. Export, then import to Studio as Class.Model.
- t2: **Maya FBX export for Roblox**: File>Export All, type FBX export. Geometry: Smooth Mesh, Referenced Asset Content. Animation off. Units Automatic, Up Axis Y. Embed Media only for .png textures.

## Points to
- https://create.roblox.com/docs/art/blender.md#adjust-scale-fbx
- https://create.roblox.com/docs/avatar/accessory-fitting-tool
- https://create.roblox.com/docs/studio/importer
- https://create.roblox.com/docs/art/modeling/export-requirements
- https://create.roblox.com/docs/avatar/layered-accessories/export
