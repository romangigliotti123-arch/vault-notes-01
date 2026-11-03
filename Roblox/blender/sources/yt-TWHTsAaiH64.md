---
type: research-source
id: yt-TWHTsAaiH64
title: "CUSTOM FACE Support & More! (Roblox Rigs Suite UPDATE)"
source_type: "youtube"
creator: "Comix Productions"
url: "https://www.youtube.com/watch?v=TWHTsAaiH64"
published: "2025-05-23"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0018
relevance: 2
density: medium
tags: ["research-source", "youtube", "avatar-ugc-accessories", "common-mistakes-fixes", "other", "rigging-animation", "texturing-baking-uv"]
---
# yt-TWHTsAaiH64

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Showcase of Roblox Rig Suite v1.1, a Blender add-on for Roblox-style rigs (not blender-mcp or bpy scripting). Covers custom face texture support, rig rename/delete, a driver-removal material panel, R15 rig rebuilt as one mesh with vertex groups, attach-to-rig options, and a Blender 4.4 animation linker fix. Little on Claude or headless pipelines.

## Claims
- c1: [0:00] Roblox Rig Suite v1.1 is a Blender add-on update adding custom face support, QoL changes and bug fixes in rigs and UI. *(demo, high; other)*
- c2: [1:14] Rig manager lets user rename a rig (renames main collection) and delete it with a confirmation; undoable. *(demo, high; other)*
- c3: [1:56] Deleting a rig removes its collections, meshes, curves, armatures and materials but keeps textures. *(demo, high; other)*
- c4: [2:25] Custom faces option is enabled per rig in material settings; any texture (Roblox decal, own drawing, face pack) can be used as face; no scale/position/rotation control yet. *(demo, high; texturing-baking-uv)*
- c5: [3:16] Advanced panel removes material drivers so bump and gloss can't be applied and values can be edited manually in Shading; author says this is a stripped-back version of a planned option. *(demo, high; rigging-animation)*
- c6: [4:38] R15 rigs were rebuilt: body is now one mesh rotating via vertex groups instead of separate parts; author says this is more optimal but has not A/B tested it. *(demo, medium; rigging-animation)*
- c7: [6:21] Attach custom head tool asks whether to link materials; works only on meshes and is disabled for armatures. *(demo, high; avatar-ugc-accessories)*
- c8: [7:02] Surface deform method in 3D layered clothing tool now parents objects to the rig; previously it did not. *(demo, high; avatar-ugc-accessories)*
- c9: [7:43] Attach accessories tool has Add to rig option (on by default) that moves accessory into rig's mesh collection, so deleting the rig deletes the accessory. *(demo, high; avatar-ugc-accessories)*
- c10: [8:24] Animation linker did not work on Blender 4.4 but worked on 4.3; v1.1 fixes it on 4.4. *(demo, high; common-mistakes-fixes)*

## Numbers
- n1: **Blender version with animation linker bug**: 4.4 broken, 4.3 worked 
- n2: **Add-on version**: 1.1 (previous 1.0.0) 

## Techniques
- t1: **Vertex-group rotation for R15 rig**: Combine body parts into one mesh; rotate joints via vertex groups instead of separate parts, reducing relationship lines. Author reports it is easier to manage, not benchmarked.

## Points to
- GFX Rhino video on the rig
- Author's Discord server for bug reports
