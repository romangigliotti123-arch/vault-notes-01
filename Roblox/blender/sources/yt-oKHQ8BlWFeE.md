---
type: research-source
id: yt-oKHQ8BlWFeE
title: "How to make UGC Headphones for Roblox - Beginner"
source_type: "youtube"
creator: "Bluesteel"
url: "https://www.youtube.com/watch?v=oKHQ8BlWFeE"
published: "2023-08-28"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0023
relevance: 2
density: medium
tags: ["research-source", "youtube", "common-mistakes-fixes", "roblox-export-settings", "roblox-import-pipeline", "texturing-baking-uv"]
---
# yt-oKHQ8BlWFeE

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Beginner Blender tutorial for making UGC headphones for Roblox. Exports a default R15/block avatar rig from Roblox Studio as OBJ, imports it into Blender, models headphone band and ear cups with modifiers, UV-projects onto a color palette image, exports selected headphone mesh as OBJ, and imports it back into Studio. No bpy, MCP, or Claude content.

## Claims
- c1: [0:08] Rig is exported from Roblox Studio by selecting the Block Avatar in Explorer, right-click Export Selection, saved as OBJ. *(demo, high; roblox-export-settings)*
- c2: [1:08] Imported rig is off-centre; fixed by setting origin to 3D cursor in Blender. *(demo, high; common-mistakes-fixes)*
- c3: [14:46] Creator says shading in Blender is not representative; it will look better in Roblox Studio. *(opinion, medium; roblox-import-pipeline)*
- c4: [15:26] Headphones are imported into Studio via Home tab Import 3D button using the OBJ file; import settings said not to matter. *(demo, high; roblox-import-pipeline)*
- c5: [13:02] Colour is applied by UV project from view, then a palette image is set as Base Color image texture in the material tab, not a generated texture. *(demo, high; texturing-baking-uv)*
- c6: [14:46] OBJ export uses Limit to Selection Only so the rig is excluded from the headphone file. *(demo, high; roblox-export-settings)*
- c7: [10:56] Mirror modifier on Z axis with clipping enabled is needed so band and ear cup meshes connect. *(demo, medium; common-mistakes-fixes)*
- c8: [11:38] Mark Sharp on edges plus Auto Smooth is used to keep hard edges while smoothing shading. *(demo, medium; texturing-baking-uv)*

## Numbers
- n1: **Circle vertex count**: 24 verts for head circle and cylinder 
- n2: **Rig file format**: OBJ (Wavefront) exported from Studio 

## Techniques
- t1: **Rig reference export**: In Studio select Block Avatar in Explorer, right-click Export Selection, save as OBJ; import that OBJ into Blender as a size/position reference.
- t2: **Mirror modifier for band**: Join band and ear-cup meshes (Ctrl J), add Mirror modifier on Z axis, enable clipping, so halves connect across the head.
- t3: **Palette UV colouring**: Select faces, UV project from view, move UV island onto a colour in the palette, set Base Color image texture to the palette in material tab.
- t4: **Selective OBJ export**: Select headphone objects, File > Export > Wavefront OBJ with Limit to Selection Only enabled, then import into Studio.

## Quotes (brief, for attribution)
> it will look better in Roblox Studios like the shading all that kind of stuff because in blender it's kind of just like it's a blank slate  (at 14:46, Bluesteel)

## Points to
- Roblox Studio download (description link)
- Blender download (description link)
- colour palette image (description link)

## Visual notes
Contact sheet shows Blender modeling stages (head, cylinder ear cups, band), a colour palette image in UV editor, and Studio import/material panes with a file dialog.
