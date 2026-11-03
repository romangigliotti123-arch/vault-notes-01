---
type: research-source
id: yt-7CfDEnHxPWA
title: "Scientific Data on Surfaces — BCON26"
source_type: "youtube"
creator: "Blender"
url: "https://www.youtube.com/watch?v=7CfDEnHxPWA"
published: "2026-09-25"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0023
relevance: 0
density: low
tags: ["research-source", "youtube", "other"]
---
# yt-7CfDEnHxPWA

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Scientific-visualization talk by a geometry-processing researcher on using Blender for figures. Covers colormap textures on surfaces, setting View Transform to Standard instead of AGX/Filmic, adding emission to avoid lighting effects, shadow catchers, Freestyle and toon shading for illustrations. No mention of Roblox, Claude, blender-mcp, bpy, or FBX/glTF export.

## Claims
- c1: [6:55] Blender's default AGX/Filmic view transform shifts colors away from the colormap; set View Transform to Standard for accurate color. *(experience, high; other)*
- c2: [7:36] Mixing an emission shader with the BSDF equally gives colormap colors that are less affected by scene lighting; too much emission flattens the 3D shape. *(experience, medium; other)*
- c3: [16:22] Proportional editing acts as a fat brush for quickly modeling blobby generic surfaces for conceptual diagrams. *(opinion, medium; other)*
- c4: [19:09] Freestyle rendering and Blender's toon shading node are used for illustrated, non-photorealistic figures. *(experience, medium; other)*
- c5: [12:25] A ground plane with shadow catcher gives 3D feel; shadow can use a separate light setup and be composited over the surface render. *(experience, medium; other)*

## Techniques
- t1: **Colormap as image texture in shader nodes**: Export mesh with UVs and scalar values as OBJ; interpolate values; feed matplotlib-style colormap image into shader nodes; set View Transform to Standard.
- t2: **Isocontour bands via sine darkening**: Use math nodes to compute a periodic sine pattern of the scalar field; use output to blend surface color with dark isobands.
- t3: **Vector field arrows via geometry nodes instancing**: Write sample positions and vectors as vertex positions/normals; instance arrow objects on points; rotate each instance by the vector.

## Points to
- matplotlib
- ShaderToy
- Mathematica
