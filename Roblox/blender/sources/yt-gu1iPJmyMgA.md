---
type: research-source
id: yt-gu1iPJmyMgA
title: "How Procedural Models work on Roblox"
source_type: "youtube"
creator: "Roblox Creators"
url: "https://www.youtube.com/watch?v=gu1iPJmyMgA"
published: "2026-09-03"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0025
relevance: 1
density: medium
tags: ["research-source", "youtube", "other"]
---
# yt-gu1iPJmyMgA

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox Creators talk on procedural models: code-generated geometry that fills a resizable bounding box from modular puzzle pieces (9-slice style). Static output, so no runtime cost beyond final geometry. Context-aware and shape-aware variants need a local plugin. Does not cover Blender, Claude, or the Blender-to-Roblox export pipeline. Editable meshes are unreleased.

## Claims
- c1: [1:04] Speaker says a basic obby gray box takes about 20 edits; procedural models use similar edit counts but output finished geometry. *(opinion, medium; other)*
- c2: [1:44] Procedural models do no work at runtime; only the final output geometry costs rendering. *(opinion, medium; other)*
- c3: [2:50] A procedural bevel block internally generates hundreds of small mesh parts that are instanced together. *(demo, medium; other)*
- c4: [3:27] Procedural models use nine-slice logic: copy edge, corner and fill pieces into a box sized by the user. *(demo, medium; other)*
- c5: [4:07] Puzzle pieces can themselves be built from Roblox parts (metal edge, bevel, bricks) and still assemble at any size. *(demo, medium; other)*
- c6: [6:13] Building procedural models reuse prefab pieces from the Modern City demo (window, door, edging, cafe pieces). *(demo, medium; other)*
- c7: [5:35] Standard procedural models cannot see other objects in the world; a local plugin is needed to share world info between them. *(doc, medium; other)*
- c8: [7:36] Procedural models are currently limited to box shapes; non-block silhouettes such as T-shapes are not supported yet. *(doc, medium; other)*
- c9: [8:17] A context-aware grass procedural model places grass in cracks and corners by checking world geometry as it generates. *(demo, medium; other)*
- c10: [10:23] Adjacent procedural models that know about each other choose matching boundary tiles, removing seams. *(demo, medium; other)*
- c11: [11:43] A hole is made by setting an attribute on a procedural model; neighbors then omit tiles there and add border trims. *(demo, medium; other)*
- c12: [12:26] Editable meshes and polygon primitives (height, shade strength, shade preference attributes) are not ready for production. *(doc, high; other)*
- c13: [14:31] Editable meshes are planned to ship alongside procedural models with the data model content API, date not given. *(doc, medium; other)*

## Numbers
- n1: **gray box edit count**: ~20 edits (obby); 20-30 edits for procedural version 
- n2: **internal mesh parts per procedural block**: hundreds 
- n3: **example polygon height**: 40 

## Techniques
- t1: **Nine-slice puzzle assembly**: Define corner, edge, top-edge and fill pieces; the procedural model copies and pastes them to fill a resized box while keeping bevels intact.
- t2: **Prefab-piece building generator**: Stack floor and window prefabs from the Modern City demo; the model adds floors and windows as the box is dragged taller.
- t3: **Attribute-driven hole**: Set a hole attribute on a procedural model so neighbors leave the volume empty and add edge trims at its border.
- t4: **Context-aware placement via local plugin**: Plugin exposes world info so generators like grass check for crevices and corners before placing pieces.

## Quotes (brief, for attribution)
> procedural models don't have to do anything at runtime. You only pay the cost of the final geometry that's been output.  (at 1:44, Roblox Creators)
> procedural models normally can't tell where they are in the world and what other the models are around them.  (at 5:35, Roblox Creators)

## Contradictions flagged
- Procedural models are presented as a ready Roblox feature with plugin-enabled context awareness. (vs Speaker says procedural models are still under development and the context-aware features need a local plugin, so they are not a shipped default.)

## Points to
- Roblox Modern City demo
- Roblox data model content API
- project file with plugin source (linked in video description)
