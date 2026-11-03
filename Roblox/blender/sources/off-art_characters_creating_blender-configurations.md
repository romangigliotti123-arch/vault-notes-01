---
type: research-source
id: off-art_characters_creating_blender-configurations
title: "Roblox Creator Docs: art_characters_creating_blender-configurations"
source_type: "web"
creator: "create.roblox.com"
url: "https://create.roblox.com/docs/art/characters/creating/blender-configurations"
published: "2026-10-31"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0016
relevance: 3
density: medium
tags: ["research-source", "web", "blender-roblox-export-import", "claude-blender-ai", "rigging-animation"]
---
# off-art_characters_creating_blender-configurations

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox official doc on the helper configuration in Blender avatar template .blend files: hierarchy (Cage, Joints/armature, _Geo, _Att, lights), disabled attachment objects, a Blender 3.4+ skin tone preview shader, export steps for color maps, FBX Unit Scale, and 0–330 animation range. Covers no blender-mcp, bpy, or Claude workflows.

## Claims
- c1: Roblox avatar .blend templates contain extra helper configs not in raw .fbx templates: Cage (15 outer body cage meshes), Joints armature with Bones, _Geo, _Att and animation data, plus Fill and Sun lights (not part of avatar). *(doc, high; blender-roblox-export-import)*
- c2: Attachment objects are set to Disable In Viewport by default; enable the Outliner filter 'Disable In Viewport' to toggle them. *(doc, high; blender-roblox-export-import)*
- c3: Skin tone preview shader requires Blender 3.4+; older versions may render textures incorrectly. *(doc, high; blender-roblox-export-import)*
- c4: Skin tone preview needs Viewport Shading mode; swapping textures reverts normal map colorspace to SRGB instead of NonColor, which must be fixed manually. *(doc, high; blender-roblox-export-import)*
- c5: Preview PartColor does not export. To package color map: replace Mix node with ColorMap node in Shading tab, or export textures manually and add in Studio. *(doc, high; blender-roblox-export-import)*
- c6: FBX export: Transform > Apply Scalings set to FBX Unit Scale for correct scale. Templates already have this configured. *(doc, high; blender-roblox-export-import)*
- c7: For custom characters with facial animation, set animation timeline Start=0 and End=330. *(doc, high; rigging-animation)*
- c8: Setting project defaults: File > Defaults > Save Startup File stores project settings for future Blender files. *(doc, medium; blender-roblox-export-import)*
- c9: Source does not mention blender-mcp, bpy scripting, Claude, or Open Cloud; it covers only Roblox avatar template Blender configuration. *(doc, high; claude-blender-ai)*

## Numbers
- n1: **cage meshes**: 15 outer body cage meshes in avatar template
- n2: **animation timeline range**: 0-330 facial animation custom characters
- n3: **minimum Blender version**: 3.4+ skin tone preview shader

## Techniques
- t1: **Outliner Disable In Viewport filter**: Click Outliner Filter dropdown, enable Disable In Viewport filter, then toggle the icon per object to show disabled attachments.
- t2: **ColorMap export workaround**: In Shading tab, disconnect Mix node, insert ColorMap node so color map packages with FBX; alternatively export textures separately and add in Studio.

## Quotes (brief, for attribution)
> You must use Blender 3.4+ to ensure that the helper shader configurations render correctly.  (create.roblox.com)

## Points to
- https://create.roblox.com/docs/art/characters/creating/export-textures
- https://create.roblox.com/docs/art/blender.md#adjust-scale-fbx
- https://create.roblox.com/docs/art/characters/creating/modeling-best-practices

## Visual notes
.
