---
type: research-source
id: yt-C_NnXTJ1jME
title: "How To Model a Gun In 20 Minutes | Blender"
source_type: "youtube"
creator: "Kingkade 3D"
url: "https://www.youtube.com/watch?v=C_NnXTJ1jME"
published: "2026-01-17"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0029
relevance: 1
density: low
tags: ["research-source", "youtube", "mesh-texture-limits", "other"]
---
# yt-C_NnXTJ1jME

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Blender low-poly gun modeling tutorial (no Claude, blender-mcp, bpy, Roblox export, or texturing content). Covers reference-image setup, cylinder-based barrel extrusion, vertex-by-vertex outlining, bevel limits, and boolean holes. Useful only for general mesh hygiene: avoid intersecting verts, separate parts before boolean, fill hollow holes to avoid in-game glitches.

## Claims
- c1: [17:02] Boolean hole cutting can make random pieces disappear; the tutorial's fix is separating those parts (P > Selection) and applying booleans one object at a time. *(experience, medium; mesh-texture-limits)*
- c2: [20:25] Hollow boolean holes with open faces will glitch in-game, so the author fills the opening by connecting edges with F. *(opinion, low; mesh-texture-limits)*
- c3: [8:36] Over-beveling can push vertices into each other, which the author describes as causing a glitch; keep bevels small. *(opinion, low; mesh-texture-limits)*
- c4: [21:05] Separate parts can be rejoined into one object by selecting them with the main body active and pressing Ctrl+J. *(demo, medium; mesh-texture-limits)*
- c5: [1:34] Barrel base built from a cylinder set to 8 vertices (low-poly look), then extruded faces along normals. *(demo, medium; other)*
- c6: [0:00] Reference image can be generated with ChatGPT (side-view low-poly gun prompt) and loaded via Shift+A > Image > Reference. *(demo, medium; other)*

## Numbers
- n1: **cylinder vertex count**: 8 
- n2: **loop cuts added with Ctrl+R**: 2 

## Techniques
- t1: **Separate-then-boolean**: Separate hole-cutter pieces (P > Selection), then add Boolean modifier, pick cutter with eyedropper, apply; one cutter at a time to avoid parts vanishing.
- t2: **Fill boolean openings**: After boolean leaves open faces, delete the extra faces, then connect rim edges with F to close the hole.

## Quotes (brief, for attribution)
> it is better to remove like one thing at a time just so your parts don't disappear like that  (at 19:03, Kingkade 3D)

## Points to
- ChatGPT (reference image generation)
