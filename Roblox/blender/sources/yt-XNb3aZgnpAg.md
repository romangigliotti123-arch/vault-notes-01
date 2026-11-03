---
type: research-source
id: yt-XNb3aZgnpAg
title: "How to Make a UGC Fedora for Roblox - Beginners"
source_type: "youtube"
creator: "Bluesteel"
url: "https://www.youtube.com/watch?v=XNb3aZgnpAg"
published: "2023-04-15"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0024
relevance: 2
density: medium
tags: ["research-source", "youtube", "avatar-ugc-accessories", "common-mistakes-fixes", "procedural-generation", "roblox-export-settings", "roblox-import-pipeline", "texturing-baking-uv"]
---
# yt-XNb3aZgnpAg

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Beginner tutorial (Roblox Studio + Blender 2.x era, no scripting or MCP) making a blue/white UGC fedora. Workflow: export R6 Block Avatar rig from Studio as OBJ, import to Blender, set origin, model hat from circle primitive, UV-unwrap onto a palette texture, export selection as OBJ, load into a MeshPart via MeshId, fix transparency with double-sided. Manual GUI only.

## Claims
- c1: [0:00] Rig is exported from Studio via Explorer right-click > Export Selection, saved to disk, then opened in Blender as an OBJ (File > Import > Wavefront .obj). *(demo, high; roblox-import-pipeline)*
- c2: [0:40] Imported rig spawns off-origin; fix with Set Origin > Origin to 3D Cursor, then Geometry to Origin before moving it. *(demo, medium; common-mistakes-fixes)*
- c3: [1:20] Imported rig looks slightly transparent in Material Preview; fix by setting material Blend Mode to Opaque. *(demo, medium; common-mistakes-fixes)*
- c4: [2:05] Hat base is a circle primitive with 20 vertices, scaled on Y to form a fedora profile; extrude/inset/scale used to build crown. *(demo, medium; procedural-generation)*
- c5: [4:47] Band is made with Ctrl+R loop cut, Alt+E extrude along normals, Ctrl+B bevel, then Shade Smooth plus Auto Smooth in Normals. *(demo, medium; avatar-ugc-accessories)*
- c6: [6:09] Bevel must be done before distorting (moving) faces, because moving faces after beveling distorts the bevel. *(experience, medium; common-mistakes-fixes)*
- c7: [6:59] Texturing uses a palette image as an Image Texture base color on a new material; UV islands are selected and scaled to zero to pick a palette colour (blue band, white rest). *(demo, medium; texturing-baking-uv)*
- c8: [8:13] Export the hat as OBJ from Blender with Limit to Selection enabled so the character is not included. *(demo, high; roblox-export-settings)*
- c9: [8:13] In Studio, insert a MeshPart and set its MeshId property to the saved OBJ path, then confirm the import dialog. *(demo, medium; roblox-import-pipeline)*
- c10: [8:56] Imported mesh appearing transparent is a common issue; fix by enabling Double-Sided on the part. *(demo, medium; common-mistakes-fixes)*
- c11: [8:56] Hat is positioned and scaled against the rig in Studio using move/scale tools; Shift-scale is used to scale one part of a mesh. *(demo, low; avatar-ugc-accessories)*

## Numbers
- n1: **circle vertex count**: 20 
- n2: **Rig Builder rig type**: R6, Block Avatar 

## Techniques
- t1: **Studio rig OBJ round-trip**: Explorer > right-click rig > Export Selection (OBJ). Import into Blender, fix origin, model accessory around the head, export selection as OBJ, set MeshPart.MeshId in Studio.
- t2: **Origin fix**: Set Origin > Origin to 3D Cursor, then Geometry to Origin so the imported mesh sits at world origin before positioning.
- t3: **Band build**: Ctrl+R loop cut for band width; Alt-select face loop; Alt+E extrude along normals; Ctrl+B bevel; Shade Smooth then Auto Smooth.
- t4: **Palette colour picking via UV**: Assign new material with Image Texture base colour from palette image; select UV island and scale to zero to sample one palette colour.

## Contradictions flagged
- Bevel must be applied before face distortion (6:09). (vs Video itself earlier beveled band edges after extruding; creator notes a later bevel was distorted, so ordering matters.)

## Points to
- Roblox Studio download (linked in description, not given)
- Blender download (linked in description, not given)
- UV colour palette image (linked in description, not given)
