---
type: research-source
id: yt-6MSSVwN45cg
title: "I Turned an AI Image Into a 40cm 3D Printed Figure"
source_type: "youtube"
creator: "Stefan 3D AI"
url: "https://www.youtube.com/watch?v=6MSSVwN45cg"
published: "2026-08-22"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0035
relevance: 1
density: low
tags: ["research-source", "youtube", "blender-roblox-export-import", "other"]
---
# yt-6MSSVwN45cg

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Stefan 3D AI video on AI-generated figure pipeline for resin/FDM 3D printing: generate parts in Tripo (3.1), import to Blender, sculpt-mode fixes, boolean dovetail connectors, remesh joins, vertex-color multicolor prep. Not about Roblox, Claude, blender-mcp, or bpy scripting. Only tangential Blender tips.

## Claims
- c1: [1:02] Video is about 3D printing a 40cm AI-generated figure; no Roblox, Claude, blender-mcp, or bpy content. *(doc, high; other)*
- c2: [3:30] Author uses Tripo 3.1 for generation, ultra mesh quality, texture removed; opinion that it is the best generator for this. *(opinion, low; other)*
- c3: [6:04] Blender Sculpt mode is used for high-poly cleanup; Shift temporarily switches to Smooth brush. *(experience, medium; other)*
- c4: [10:38] Author recommends Ctrl+A > Rotation and Scale after scaling/rotating objects so modifiers use correct transforms. General Blender tip, not Roblox-specific. *(experience, medium; blender-roblox-export-import)*
- c5: [13:37] Dovetail connectors made with Boolean Difference using a slightly scaled duplicate of the part to leave a print gap. *(experience, medium; other)*
- c6: [16:42] Join separate meshes with Ctrl+J, then Remesh in sculpt mode with a large voxel size to get one solid mesh. *(experience, medium; other)*
- c7: [25:18] Multicolor printing on Bambu Lab uses vertex colors, not textures; author plans six colors; Blender vertex paint plus a material with Attribute node to Base Color lets colors show in Object mode. *(experience, medium; other)*
- c8: [25:58] AI texture-based color extraction tools gave the author poor results compared with manual vertex painting. *(opinion, low; other)*

## Numbers
- n1: **Figure height**: 40 cm 
- n2: **Blender unit setting**: millimeters; 40 cm = 400 mm size cap 
- n3: **Blender prep time**: 1 h 10 min for all parts and dovetails 
- n4: **Dovetail gap check**: 0.35 mm 
- n5: **Vertex colors planned**: 6 (Bambu Lab supports up to 32) 
- n6: **Print time for largest part**: about 10 hours; total printing a few days 

## Techniques
- t1: **Sculpt-mode cleanup**: Switch to Sculpt mode. Use Clay to add volume, Smooth for transitions (hold Shift), Elastic Grab to align parts, Inflate/Ctrl to close gaps.
- t2: **Boolean dovetail**: Create a solid primitive cube, Boolean Difference on the target, then apply the modifier (Ctrl+A). Use a scaled-up duplicate to leave a print gap.
- t3: **Join and Remesh**: Position parts close, select both, Ctrl+J, then in Sculpt mode use Remesh with a large voxel size to merge into one mesh.
- t4: **Mask slice**: Paint mask with laser or brush mask, then Mask > Slice and Fill Holes; invert mask (Ctrl+I) to cut the opposite side.
- t5: **Vertex paint for multicolor**: Set vertex colors in Vertex Paint; create one material with Attribute node into Base Color so colors show in Material Preview.

## Quotes (brief, for attribution)
> Basically, color printing is based on vertex colors.  (at 25:18, Stefan 3D AI)
> select all the models, control A and rotation and scale and apply rotation and scale.  (at 10:38, Stefan 3D AI)

## Contradictions flagged
- Figure was made with AI tools in less than 1 hour. (vs Same video says Blender prep alone took 1 h 10 min, and printing took several days.)

## Points to
- Tripo (3D AI generator, cited as 3.1)
- Nano Banana Pro
- GPT Image 2
- Gemini
- Bambu Lab
- Elegoo 16K resin printer
