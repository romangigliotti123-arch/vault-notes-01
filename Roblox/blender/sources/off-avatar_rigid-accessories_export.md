---
type: research-source
id: off-avatar_rigid-accessories_export
title: "Roblox Creator Docs: avatar_rigid-accessories_export"
source_type: "web"
creator: "create.roblox.com"
url: "https://create.roblox.com/docs/avatar/rigid-accessories/export"
published: "2026-10-31"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0025
relevance: 2
density: medium
tags: ["research-source", "web", "avatar-ugc-accessories", "blender-roblox-export-import", "other", "rigging-animation"]
---
# off-avatar_rigid-accessories_export

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Official Roblox doc for exporting rigid accessories from Blender or Maya as FBX (or glTF in Blender) for Studio import as Class.Model. Gives exact Blender FBX settings (Path Mode Copy, Embed Textures, Apply Scalings FBX Unit Scale) and Maya settings (Smooth Mesh, Animation off, Units Automatic, Up Axis Y). Says to apply or delete modifiers. Does not cover blender-mcp, bpy, or Claude.

## Claims
- c1: Blender FBX export for rigid accessories: File > Export > FBX; Path Mode = Copy; enable Embed Textures; Transform > Apply Scalings = FBX Unit Scale. *(doc, high; blender-roblox-export-import)*
- c2: Blender also supports glTF export for rigid accessories; FBX is the path the page details, with a link to Blender FBX scaling docs for scale issues. *(doc, high; blender-roblox-export-import)*
- c3: Warning: apply or delete all modifiers on mesh/project objects before export. *(doc, high; blender-roblox-export-import)*
- c4: Maya FBX export: Smooth Mesh and Referenced Asset Content enabled; Animation disabled; Embed Media enabled only if textures must import as PNG. *(doc, high; blender-roblox-export-import)*
- c5: Maya Advanced Options: Units set to Automatic; Axis Conversion Up Axis set to Y. *(doc, high; blender-roblox-export-import)*
- c6: Rigid accessory export disables animation in Maya; the page covers only static meshes plus attachment data. *(doc, medium; rigging-animation)*
- c7: Exported FBX imports into Studio as a Class.Model rigid accessory; then Accessory Fitting Tool converts it into an accessory. *(doc, high; avatar-ugc-accessories)*
- c8: Rigid accessory models must contain mesh, texture and attachment data for correct attachment to character bodies. *(doc, high; avatar-ugc-accessories)*
- c9: Source is an official Roblox doc page on rigid accessory export; it does not mention blender-mcp, bpy, or Claude. *(doc, high; other)*

## Numbers
- n1: **Blender Apply Scalings**: FBX Unit Scale 
- n2: **Blender Path Mode**: Copy 
- n3: **Maya Up Axis**: Y 

## Techniques
- t1: **Blender FBX export for Roblox**: File > Export > FBX; Path Mode Copy; Embed Textures on; Apply Scalings = FBX Unit Scale; Export FBX. Then import to Studio as Class.Model.
- t2: **Maya FBX export for Roblox**: File > Export All; Files of type FBX export; Smooth Mesh + Referenced Asset Content on; Animation off; Units Automatic; Up Axis Y.

## Points to
- https://create.roblox.com/docs/avatar/rigid-accessories/specifications
- https://create.roblox.com/docs/art/blender
- https://create.roblox.com/docs/studio/importer
- https://create.roblox.com/docs/avatar/accessory-fitting-tool
- https://create.roblox.com/docs/avatar/rigid-accessories/import

## Visual notes
Screenshots show Blender and Maya export dialogs; no extra facts beyond the text.
