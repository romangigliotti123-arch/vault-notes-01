---
type: research-source
id: off-avatar_character-bodies_export
title: "Roblox Creator Docs: avatar_character-bodies_export"
source_type: "web"
creator: "create.roblox.com"
url: "https://create.roblox.com/docs/avatar/character-bodies/export"
published: "2026-10-31"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0016
relevance: 3
density: high
tags: ["research-source", "web", "avatar-ugc-accessories", "blender-roblox-export-import", "claude-blender-ai", "rigging-animation"]
---
# off-avatar_character-bodies_export

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox docs page on exporting character bodies as FBX/glTF from Blender and Maya for Studio Importer. Gives exact Blender FBX export toggles, animation timeline/NLA settings, and Maya axis/unit settings. Requires 15 meshes, 15 cages, 19 attachments under an armature. No bpy, blender-mcp, or Claude content.

## Claims
- c1: Roblox character body FBX export from Blender: File > Export > FBX; Path Mode Copy; Embed Textures on; Include Custom Properties on; Apply Scalings = FBX Unit Scale; uncheck Add Leaf Bones. *(doc, high; blender-roblox-export-import)*
- c2: Blender FBX animation export: uncheck NLA Strips, All Actions, Force Start/End Keyframes; set Simplify to 0.0; timeline Start/End must span all keyframes. *(doc, high; blender-roblox-export-import)*
- c3: Maya character FBX export: Smooth Mesh and Referenced Asset Content on; Animation and Bake Animation on; Units Automatic; Axis Conversion Up Axis = Y; Embed Media optional for PNG textures. *(doc, high; blender-roblox-export-import)*
- c4: Character bodies need animation data when exporting dynamic-head avatars; export with animation if FACS animation is used. *(doc, medium; rigging-animation)*
- c5: Character body must contain 15 body-part meshes, 15 outer cage meshes (naming affix), and 19 attachments under an armature; cages parented to one empty object for tidiness. *(doc, high; avatar-ugc-accessories)*
- c6: Avatar template files require the combine-head-geometry cleanup steps before assets validate. *(doc, high; avatar-ugc-accessories)*
- c7: Apply or delete all modifiers and remove non-Roblox objects before export. *(doc, high; blender-roblox-export-import)*
- c8: Exported FBX imports into Studio as a Class.Model character; HumanoidDescription can then apply appearance to it. *(doc, high; blender-roblox-export-import)*
- c9: Source does not mention blender-mcp, bpy scripting, or Claude usage; no AI-assisted workflow content. *(doc, high; claude-blender-ai)*

## Numbers
- n1: **body part meshes**: 15 required in armature object
- n2: **outer cages**: 15 one per body part, naming affix
- n3: **attachments**: 19 required in armature object
- n4: **Simplify**: 0.0 FBX animation export setting

## Techniques
- t1: **Blender FBX character export**: Path Mode Copy, Embed Textures, Custom Properties, FBX Unit Scale, no leaf bones, NLA/All Actions off, Simplify 0.0, verify timeline range, export.
- t2: **Maya FBX character export**: Enable smooth mesh, animation with bake, Units Automatic, Up Axis Y, then Export All.

## Quotes (brief, for attribution)
> If you are using Roblox's avatar template files, you must perform the cleanup steps in order for the assets to properly validate.  (create.roblox.com)

## Points to
- https://create.roblox.com/docs/art/blender.md#adjust-scale-fbx
- https://create.roblox.com/docs/avatar/character-bodies/specifications
- https://create.roblox.com/docs/studio/importer

## Visual notes
Screenshots only show Blender outliner and export panel; no extra facts beyond text.
