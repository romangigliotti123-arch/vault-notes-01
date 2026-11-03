---
type: research-source
id: web-b7f50e702b
title: "Roblox docs: avatar/emotes/export"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/avatar/emotes/export.md"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0013
relevance: 3
density: high
tags: ["research-source", "web", "blender-roblox-export-import", "rigging-animation"]
---
# web-b7f50e702b

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox doc for exporting emote animation as FBX/glTF from Blender or Maya for Studio import. Gives step-by-step Blender FBX settings (FBX Unit Scale, leaf bones off, NLA/All Actions off, Simplify 0.0) and Maya settings (Bake Animation, Units Automatic, Up Axis Y). Does not cover blender-mcp, bpy scripting, or triangle/texture limits.

## Claims
- c1: Roblox emote export from Blender: set timeline Start/End to cover the full animation range before exporting FBX, since keyframe range must be correct for import. *(doc, high; blender-roblox-export-import)*
- c2: Blender FBX export for Roblox: Path Mode Copy, Embed Textures on, Custom Properties on, Apply Scalings = FBX Unit Scale, Add Leaf Bones off. *(doc, high; blender-roblox-export-import)*
- c3: Blender FBX animation settings: NLA Strips off, All Actions off, Force Start/End Keyframes off, Simplify set to 0.0. *(doc, high; blender-roblox-export-import)*
- c4: Doc says Blender FBX scaling must be checked (Blender FBX scaling section) to ensure correct Studio scale; alternatives exist if scaling issues occur on import. *(doc, medium; blender-roblox-export-import)*
- c5: Maya FBX export for Roblox: Smooth Mesh and Referenced Asset Content on, Animation and Bake Animation on, Units Automatic, Up Axis Y. *(doc, high; blender-roblox-export-import)*
- c6: Avatar characters with dynamic heads require animation data in the export, so Animation must be enabled in Maya export. *(doc, high; rigging-animation)*
- c7: Maya option Embed Media only needed when textures should be imported as .png. *(doc, medium; blender-roblox-export-import)*

## Numbers
- n1: **Example timeline range**: Start 0, End 308 (Blender screenshot example) Illustrative caption for timeline Start/End
- n2: **Simplify value**: 0.0 Blender FBX export animation section

## Techniques
- t1: **Blender FBX emote export**: Verify timeline Start/End; File>Export>FBX; Path Mode Copy; Embed Textures; Custom Properties; Apply Scalings FBX Unit Scale; uncheck Add Leaf Bones; in Animation uncheck NLA Strips, All Actions, Force Start/End Keyframes; Simplify 0.0; export.
- t2: **Maya FBX emote export**: File>Export All; FBX export; enable Smooth Mesh, Referenced Asset Content, Animation, Bake Animation; Units Automatic; Axis Conversion Up Axis Y; export.

## Points to
- https://create.roblox.com/docs/avatar/emotes/specifications
- https://create.roblox.com/docs/avatar/emotes/import
- https://create.roblox.com/docs/art/blender.md#adjust-scale-fbx
- https://create.roblox.com/docs/art/characters/export-avatar-animations-from-maya
- https://create.roblox.com/docs/avatar/dynamic-heads
