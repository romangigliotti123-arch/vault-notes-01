---
type: research-source
id: yt-dCdbjOV7ksw
title: "How to Make a UGC Top Hat for Roblox - Beginners"
source_type: "youtube"
creator: "Bluesteel"
url: "https://www.youtube.com/watch?v=dCdbjOV7ksw"
published: "2023-03-18"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0018
relevance: 2
density: medium
tags: ["research-source", "youtube", "common-mistakes-fixes", "procedural-generation", "roblox-export-settings", "roblox-import-pipeline", "texturing-baking-uv"]
---
# yt-dCdbjOV7ksw

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Beginner Blender-to-Roblox UGC top hat tutorial (Bluesteel, 2023). Covers exporting an R15/R6 block-rig dummy from Roblox Studio as OBJ, importing into Blender, fixing transparency, modeling a cylinder-based hat, UV project-from-view, palette texture, and re-importing the OBJ as a MeshPart. No blender-mcp, bpy or Claude content; relevance to the stated topic is low.

## Claims
- c1: [0:00] Dummy is exported from Studio by inserting a block rig (Avatar tab, R15 rig builder) then right-click Explorer > Export Selection as an OBJ-style file for Blender import. *(demo, medium; roblox-export-settings)*
- c2: [1:22] Imported dummy material appears slightly transparent; fix by setting material Blend Mode to Opaque. *(demo, medium; common-mistakes-fixes)*
- c3: [6:22] Hat exported from Blender as Wavefront OBJ with 'limit to selection only' checked so the dummy is not included, then imported into Studio via Insert Mesh Part and Properties file picker. *(demo, medium; roblox-import-pipeline)*
- c4: [4:08] UVs made by selecting front face, U > Project from View; a shared colour palette image is applied via Material > New > Base Color > Image Texture. *(demo, medium; texturing-baking-uv)*
- c5: [1:34] Hat built manually from a cylinder with 18 vertices, extruded/inset/scaled by hand; no generator or AI text-to-3D used. *(demo, medium; procedural-generation)*
- c6: [7:02] Imported hat is scaled up in Studio with the scale tool, using shift to scale proportionally; scale mismatch is handled manually, not by export settings. *(demo, low; common-mistakes-fixes)*
- c7: [0:41] Blender origin set to 3D cursor and geometry origin applied to the imported dummy before modelling, to align the hat with the rig. *(demo, medium; roblox-export-settings)*

## Numbers
- n1: **cylinder vertex count**: 18 Low-poly top hat base cylinder, vertices set in add-cylinder panel
- n2: **rig type**: R15 block rig (R6 name used for saved file) Block rig from Avatar > Rig Builder used as dummy

## Techniques
- t1: **Project from View UV unwrap**: Edit mode, select front face, U > Project from View; then scale UV islands with A, S, 0 to colour bands and fill rest white.
- t2: **Palette texture assignment**: Material tab > New > Base Color > Image Texture, pick palette image; shade smooth and auto smooth normals.
- t3: **Manual band with loop cut and inset**: Ctrl+R loop cut, Alt-select band, E extrude, Shift+Alt+S scale on X/Y to flare brim.

## Quotes (brief, for attribution)
> click export so now just jump back into Roblox Studios  (at 6:22, Bluesteel)

## Points to
- Roblox Studio download (link in description)
- Blender download (link in description)
- colour palette (link in description)
