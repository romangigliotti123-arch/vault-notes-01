---
type: research-source
id: off-avatar_emotes_export
title: "Roblox Creator Docs: avatar_emotes_export"
source_type: "web"
creator: "create.roblox.com"
url: "https://create.roblox.com/docs/avatar/emotes/export"
published: "2026-10-31"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0023
relevance: 3
density: high
tags: ["research-source", "web", "blender-roblox-export-import", "rigging-animation"]
---
# off-avatar_emotes_export

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox official doc for exporting emote animation as FBX or glTF from Blender or Maya. Gives exact Blender and Maya FBX export checkbox settings, timeline range requirement, and links to emote specs, import, and Blender FBX scaling. Does not cover blender-mcp, bpy scripting, or triangle/texture limits.

## Claims
- c1: Roblox docs require the timeline Start and End to span the full animation range before export (example Start 0, End 308). *(doc, high; blender-roblox-export-import)*
- c2: Blender FBX export for Roblox: Path Mode Copy, Embed Textures on, Custom Properties on, Apply Scalings = FBX Unit Scale, uncheck Add Leaf Bones. *(doc, high; blender-roblox-export-import)*
- c3: Blender animation export: uncheck NLA Strips, All Actions, Force Start/End Keyframes; set Simplify to 0.0. *(doc, high; blender-roblox-export-import)*
- c4: Maya FBX export for Roblox: Smooth Mesh and Referenced Asset Content on; Animation and Bake Animation on; Units Automatic; Up Axis Y. *(doc, high; blender-roblox-export-import)*
- c5: Avatars with dynamic heads require animation data in the Maya export. *(doc, high; rigging-animation)*
- c6: Blender FBX scaling is covered in a separate Roblox doc section; alternative approaches exist if scaling fails on import. *(doc, medium; blender-roblox-export-import)*

## Numbers
- n1: **timeline End example**: 308 Example Blender timeline Start 0, End 308 in docs image
- n2: **Blender Simplify**: 0.0 Animation export setting

## Techniques
- t1: **Blender emote FBX export**: Set timeline Start/End; File>Export>FBX; Path Mode Copy; embed textures; Custom Properties on; Apply Scalings FBX Unit Scale; uncheck Add Leaf Bones; Animation: uncheck NLA Strips, All Actions, Force Start/End Keyframes; Simplify 0.0.
- t2: **Maya emote FBX export**: File>Export All, FBX; enable Smooth Mesh, Referenced Asset Content, Animation, Bake Animation; Units Automatic; Axis Conversion Up Axis Y.

## Quotes (brief, for attribution)
> ensure that your animation timeline's Start and End include the entire range of your animation.  (create.roblox.com)

## Points to
- https://create.roblox.com/docs/art/blender.md#adjust-scale-fbx
- https://create.roblox.com/docs/avatar/emotes/specifications
- https://create.roblox.com/docs/avatar/emotes/import
- https://create.roblox.com/docs/art/characters/export-avatar-animations-from-maya
