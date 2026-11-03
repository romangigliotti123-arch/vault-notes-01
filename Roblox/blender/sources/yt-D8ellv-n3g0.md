---
type: research-source
id: yt-D8ellv-n3g0
title: "How to import Meshes with Textures into Roblox Studio"
source_type: "youtube"
creator: "Bluesteel"
url: "https://www.youtube.com/watch?v=D8ellv-n3g0"
published: "2023-07-16"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0027
relevance: 2
density: medium
tags: ["research-source", "youtube", "common-mistakes-fixes", "roblox-export-settings", "roblox-import-pipeline", "texturing-baking-uv"]
---
# yt-D8ellv-n3g0

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Bluesteel video (Jul 2023, 4:44) shows exporting a Blender mesh with a palette-image texture to Roblox Studio via FBX. Covers face-orientation check and recalculating normals, UV unwrapping per-band onto a colour palette, assigning the palette as an Image Texture base colour, FBX export with Limit to Selection, importing via Import 3D, scaling, and fixing transparency by disabling Double Sided. No blender-mcp, bpy scripting, or Claude content.

## Claims
- c1: [0:00] Check face orientation overlay; faces should all be blue. Fix red faces by entering Edit Mode, selecting them, Shift+N recalculate, then toggle overlay off. *(demo, high; common-mistakes-fixes)*
- c2: [0:42] Colouring method: UV-unwrap each band section separately, position it onto a colour swatch in a palette image in the UV Editor, then assign that palette as an Image Texture base colour. *(demo, medium; texturing-baking-uv)*
- c3: [2:04] Colour shows only in Material Preview; Rendered view is possible but uses much more processing power. Material needs an Image Texture base colour pointing to the palette. *(demo, medium; texturing-baking-uv)*
- c4: [2:44] Export via File > Export > FBX with Limit to Selection enabled so only the selected mesh exports. *(demo, high; roblox-export-settings)*
- c5: [3:27] Import into Roblox Studio via Import 3D, using default import settings, then close the dialog. *(demo, high; roblox-import-pipeline)*
- c6: [4:09] Partial transparency on the mesh is attributed to wrong normals; the video's fix is unchecking Double Sided in the MeshPart properties. *(opinion, medium; common-mistakes-fixes)*

## Numbers
- n1: **video length**: 4:44 
- n2: **views**: 97242 

## Techniques
- t1: **Face orientation check**: Enable Viewport Overlays > Face Orientation; faces should be blue. For red faces, Edit Mode, select, Shift+N to recalc, verify blue.
- t2: **Palette UV colouring**: Load palette image in UV Editor. Select band, U > unwrap, scale and move onto palette swatch. Ctrl+I invert selection for other parts and repeat.
- t3: **Image Texture base colour**: Material tab > New > Base Color > Image Texture > choose palette image. View in Material Preview to see colours.
- t4: **Selected-only FBX export**: File > Export > FBX, enable Limit to Selection, save with memorable name, export.

## Quotes (brief, for attribution)
> make sure to limit to selection only because that will only export what we have selected  (at 2:44, Bluesteel)
> if you're having a weird like slightly transparent problem... then that means you didn't do the normals right  (at 4:09, Bluesteel)

## Contradictions flagged
- Transparency fix via Double Sided toggle is presented as an alternative to fixing normals. (vs Video itself says transparency means normals were wrong, so disabling Double Sided only masks the symptom (opinion-level inference).)

## Points to
- Colour palette link in video description (not given in transcript)
