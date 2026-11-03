---
type: research-source
id: yt-YtVkmDnRgcI
title: "How to make a UGC Witch Hat for Roblox - Beginners"
source_type: "youtube"
creator: "Bluesteel"
url: "https://www.youtube.com/watch?v=YtVkmDnRgcI"
published: "2023-06-04"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0017
relevance: 3
density: medium
tags: ["research-source", "youtube", "common-mistakes-fixes", "creator-workflows", "procedural-generation", "roblox-export-settings", "roblox-import-pipeline", "texturing-baking-uv"]
---
# yt-YtVkmDnRgcI

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Beginner tutorial (Bluesteel, 2023-06-04, 8:39) making a Roblox UGC witch hat in Blender. Exports the default R15-style block rig via Roblox Studio Explorer "Export Selection" as OBJ, imports into Blender, models hat with extrude/inset/bevel/proportional editing, UV-unwraps onto a colour palette image texture, exports OBJ, and imports into Roblox as a MeshPart. No blender-mcp, bpy, or Claude content.

## Claims
- c1: [0:00] Rig is exported from Studio by right-clicking the rig in Explorer and choosing Export Selection, saving as OBJ. *(demo, medium; roblox-import-pipeline)*
- c2: [1:14] Rig appears slightly transparent in Blender material view; fix by setting material blend mode to Opaque. *(demo, medium; common-mistakes-fixes)*
- c3: [0:34] Imported OBJ is centred using Set Origin > Origin to 3D Cursor and Geometry to Origin. *(demo, medium; common-mistakes-fixes)*
- c4: [5:29] Texture uses a colour palette image (screenshot from Row Builder Discord) as image texture base colour; faces UV-unwrapped to palette colours. *(demo, medium; texturing-baking-uv)*
- c5: [7:30] Export selected hat via File > Export > Wavefront OBJ with Selection Only enabled. *(demo, medium; roblox-export-settings)*
- c6: [7:30] In Studio, insert MeshPart and set MeshId property to the uploaded OBJ mesh to get the hat. *(demo, medium; roblox-import-pipeline)*
- c7: [4:26] Hat base shaped with proportional editing (O) and grab/scale to add curve; no scale/unit numbers given. *(demo, low; procedural-generation)*
- c8: [6:09] Author noted hat was scaled too big relative to the head and resized after import; no units given. *(opinion, medium; common-mistakes-fixes)*
- c9: [3:43] Hat shading: Shade Smooth plus Auto Smooth in normals tab used for smooth look. *(demo, low; creator-workflows)*

## Numbers
- n1: **Export format**: Wavefront OBJ, selection only 
- n2: **Test rig**: Block rig dragged onto head for fit check 

## Techniques
- t1: **Round-trip rig for fitting**: Studio Explorer > rig > Export Selection (OBJ); import to Blender; model hat on it; export hat OBJ; insert MeshPart in Studio and set MeshId.
- t2: **Palette UV colouring**: Select faces group, U unwrap, scale UV to a palette colour area; Ctrl+I invert selection for other faces; new material with Image Texture base colour set to palette.
- t3: **Hat modelling by hand**: Circle brim, extrude up, inset and extrude for crown, merge at centre, bevel edges, proportional editing for curve.

## Quotes (brief, for attribution)
> hit file export and wavefront.obj and then just export it somewhere you can get it in  (at 7:30, Bluesteel)

## Points to
- Row Builder Discord (palette source)
