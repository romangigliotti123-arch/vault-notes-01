---
type: research-source
id: yt-32xW9yw27ww
title: "How To Make A Roblox Rig: EP1, Preparing Your Model (Blender)"
source_type: "youtube"
creator: "Comix Productions"
url: "https://www.youtube.com/watch?v=32xW9yw27ww"
published: "2023-08-15"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0018
relevance: 2
density: low
tags: ["research-source", "youtube", "common-mistakes-fixes", "creator-workflows", "rigging-animation", "roblox-import-pipeline"]
---
# yt-32xW9yw27ww

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Beginner Blender tutorial (ep1 of a Roblox rig series) on preparing a Roblox avatar OBJ for rigging: import OBJ split by group, parent parts to head, rename parts, merge by distance, add loop cuts, fix auto-smooth shading, set materials to opaque, add subdivision modifiers. No Claude, blender-mcp, bpy, or Roblox export/upload content.

## Claims
- c1: [0:12] Avatar model imported via File > Import > Wavefront OBJ with 'Split by Group' enabled, producing separate parts per accessory/body piece. *(demo, high; roblox-import-pipeline)*
- c2: [0:35] Parts are parented to the head by selecting accessories first and the head last, then Ctrl+P > Object, so head moves drive the rest. *(demo, medium; rigging-animation)*
- c3: [1:55] Original Roblox-style body parts have practically no geometry, so they cannot bend; the tutorial adds density first via Merge by Distance, Tris to Quads, then loop cuts (three horizontal on head and body parts). *(demo, medium; rigging-animation)*
- c4: [3:06] Adding loop cuts made the model look broken due to Auto Smooth; fix is turning off Auto Smooth in Object Data normals, then Shade Smooth on body parts (not accessories). *(demo, medium; common-mistakes-fixes)*
- c5: [3:39] Presenter says the broken-looking material issue appears in EEVEE because of alpha; Cycles/Material view not affected; fix is setting Blend Mode to Opaque in material properties. *(opinion, low; common-mistakes-fixes)*
- c6: [5:20] Subdivision Surface modifier set to viewport level 3 and render level 3 on body parts, then copied to other parts via Copy Modifiers > Copy Selected. *(demo, medium; creator-workflows)*

## Numbers
- n1: **loop cuts**: 3 horizontal per part added to head, torso, arms, legs before rigging
- n2: **subdivision level**: viewport 3, render 3 Subdivision Surface modifier on body parts

## Techniques
- t1: **OBJ split-by-group import**: File > Import > Wavefront, enable Split by Group, then parent and rename resulting parts.
- t2: **Merge by Distance and Tris to Quads**: Edit mode, select body parts, Alt+J to convert triangles to quads, then M > By Distance to merge verts.
- t3: **Copy Modifiers to multiple parts**: Shift-select parts, make the Torso active last, Copy Selected from modifier dropdown.

## Quotes (brief, for attribution)
> turn off auto smooth on all of these so now our model looks practically exactly how it did before  (at 3:06, Comix Productions)

## Points to
- Hazen OBJ model (source asset)
