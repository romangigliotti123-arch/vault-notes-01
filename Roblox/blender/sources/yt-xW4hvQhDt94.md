---
type: research-source
id: yt-xW4hvQhDt94
title: "Making UGC Live | Watch the process + Q/A | Free UGC Drop"
source_type: "youtube"
creator: "Zander"
url: "https://www.youtube.com/watch?v=xW4hvQhDt94"
published: "2024-06-08"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0029
relevance: 1
density: low
tags: ["research-source", "youtube", "mesh-texture-limits", "other"]
---
# yt-xW4hvQhDt94

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Livestream of a UGC creator modeling Blender props (cake, chain, Bob the Blob hat) and texturing in a Substance-style app. Covers Decimate and Subdivision tradeoffs and triangle counts, with a target of about 100 triangles per chain link. Nothing on blender-mcp, Claude, bpy, the Roblox importer, or Studio.

## Claims
- c1: [12:38] Decimate applied to a cake mesh removed about 600 triangles, used as a quick way to cut poly count. *(demo, medium; mesh-texture-limits)*
- c2: [27:52] Creator said a chain with 4,000 triangles divided by 30 links implies about 100 triangles per link; 1,000 total was not enough. *(opinion, low; mesh-texture-limits)*
- c3: [28:57] Chain mesh measured about 16,000 triangles at one stage, described as too many. *(demo, medium; mesh-texture-limits)*
- c4: [27:10] Chain model reached about 60,000 triangles before reduction. *(demo, medium; mesh-texture-limits)*
- c5: [37:12] Subdivision Surface makes a low-poly model look smoother but adds far too many triangles; creator applied it, then deleted unneeded faces. *(demo, medium; mesh-texture-limits)*
- c6: [39:23] Creator kept a copy with Subdivision at about 3.9k triangles, applied it, then removed faces to get under the triangle budget. *(demo, low; mesh-texture-limits)*
- c7: [46:45] Creator said textures looked bad because they forgot to bake textures; after baking (MS thickness, position, AO) results improved. *(experience, medium; mesh-texture-limits)*
- c8: [21:35] Chain was built from circles with a Curve modifier; circles did not follow the curve until spacing was added manually. *(demo, low; other)*
- c9: [25:27] Creator named Substance Painter as the texturing app and used smart materials such as Iron Forge. *(demo, low; mesh-texture-limits)*
- c10: [1:07:48] Creator ran PBR validation and found a material with no metal, which explained why gold did not render as metal. *(experience, low; mesh-texture-limits)*

## Numbers
- n1: **triangles removed by Decimate**: ~600 
- n2: **target triangles per chain link**: ~100 
- n3: **chain triangle count**: ~16,000 
- n4: **chain triangle count before reduction**: ~60,000 
- n5: **Subdivision copy triangle count**: ~3.9k 

## Techniques
- t1: **Decimate then apply**: Add Decimate modifier to reduce triangles, then apply it. Used to cut about 600 triangles from a cake mesh.
- t2: **Subdivision then delete faces**: Duplicate mesh, apply Subdivision Surface for smoothing, then delete non-essential faces to stay under the triangle budget.
- t3: **Bake before texturing**: Bake MS thickness, position and AO maps from high-poly to low-poly; skipping the bake caused bad textures.

## Quotes (brief, for attribution)
> 1,000 triangles isn't going to cut it 4,000 divided by 30 we need these to be 100 triangles each  (at 27:52, Zander)
> I forgot to bake the textures  (at 46:45, Zander)

## Points to
- Substance Painter
