---
type: research-source
id: web-19fbb4beda
title: "Roblox docs: art/characters/creating/blender-configurations"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/art/characters/creating/blender-configurations.md"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0015
relevance: 3
density: medium
tags: ["research-source", "web", "avatar-ugc-accessories", "blender-roblox-export-import", "rigging-animation"]
---
# web-19fbb4beda

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox official doc on avatar template .blend helper setup: hierarchy (Cage, Joints with Bones/_Geo/_Att, Fill/Sun lights), disabled attachment objects, Blender 3.4+ skin tone shader preview, export workarounds for the Mix node, FBX Unit Scale export, and 0–330 animation range for facial animation. Says nothing on blender-mcp or bpy scripting.

## Claims
- c1: Roblox avatar .blend templates contain helper configs absent from raw .fbx templates; hierarchy includes Cage (15 outer body cage meshes), Joints armature, _Geo, _Att, Fill and Sun lights. *(doc, high; blender-roblox-export-import)*
- c2: Attachment (_Att) objects ship with Disable In Viewport enabled; toggle via Outliner Filter menu to access them. *(doc, high; avatar-ugc-accessories)*
- c3: Skin tone preview requires Blender 3.4+ and Viewport Shading mode; older versions may render textures incorrectly. *(doc, high; blender-roblox-export-import)*
- c4: Swapping textures reverts normal map colorspace to SRGB; set back to NonColor for correct normal rendering. *(doc, high; blender-roblox-export-import)*
- c5: Skin tone preview Mix node prevents color texture map from packaging into FBX; fix by replacing Mix with ColorMap node or exporting textures manually. *(doc, high; blender-roblox-export-import)*
- c6: FBX export: set Transform > Apply Scalings to FBX Unit Scale to get correct scale; skip if using downloadable .blend template. *(doc, high; blender-roblox-export-import)*
- c7: Custom characters with facial animation need timeline range Start 0 and End 330 in Animation Panel. *(doc, high; rigging-animation)*
- c8: Save Startup File via File > Defaults to persist project settings like timeline range. *(doc, medium; blender-roblox-export-import)*

## Numbers
- n1: **outer body cage meshes**: 15 Cage object in avatar template .blend
- n2: **minimum Blender version for skin preview shaders**: 3.4+ Helper shader configurations render correctly
- n3: **animation timeline range**: 0 to 330 Facial animation on custom characters

## Techniques
- t1: **Export skin preview as ColorMap**: In Shading tab, disconnect Mix node and replace with ColorMap node before FBX export so color texture packages automatically.
- t2: **Reveal disabled objects**: Outliner Filter dropdown, enable Disable In Viewport filter, then toggle the icon per object.
- t3: **Preview custom skin tone**: Layout tab, select Head_Geo, Shading tab, set Shader Type to Object, pick color on PartColor node attached to Mix; use Viewport Shading mode.

## Quotes (brief, for attribution)
> You must use Blender 3.4+ to ensure that the helper shader configurations render correctly.  (create.roblox.com)

## Points to
- https://create.roblox.com/docs/art/blender.md#adjust-scale-fbx
- https://create.roblox.com/docs/art/characters/creating/export-textures
- https://create.roblox.com/docs/art/characters/creating/modeling-best-practices
