---
type: research-source
id: yt-NJM5V6rQDj8
title: "How to create a HIGH QUALITY Sculpted Beanie | Roblox UGC Tutorial 2025"
source_type: "youtube"
creator: "Zander"
url: "https://www.youtube.com/watch?v=NJM5V6rQDj8"
published: "2025-08-05"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0021
relevance: 1
density: medium
tags: ["research-source", "youtube", "avatar-ugc-accessories", "mesh-texture-limits", "other"]
---
# yt-NJM5V6rQDj8

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Blender/Substance Painter tutorial for sculpting a Roblox UGC beanie: multires subdivide, sculpt, Quad Remesh low poly under triangle limit, seam-based UV unwrap, 4K bake from high to low, texture export. No Claude, blender-mcp, bpy, or Roblox export/import steps. Relevance to the blender-mcp/bpy topic is low.

## Claims
- c1: [8:00] Quad Remesh set to about 900 quads or lower produced a low-poly hat said to be under the Roblox triangle count. *(demo, medium; mesh-texture-limits)*
- c2: [14:32] Bake output set to 4K with 16x anti-aliasing; AO, curvature, and thickness maps set to max; high-poly cage checked for red spots. *(demo, medium; mesh-texture-limits)*
- c3: [3:44] Sculpt base shape after adding Multires modifier subdivided three times; mirroring enabled in sculpt mode. *(demo, medium; other)*
- c4: [12:59] Presenter avoids paid UV packing plugins and arranges UV islands manually; UV Squares plugin used to grid islands. *(opinion, low; mesh-texture-limits)*
- c5: [22:31] If over triangle limit, dissolve edges (Ctrl X) in dense inner areas while keeping seams; excessive dissolving causes noticeable morphing. *(demo, medium; mesh-texture-limits)*
- c6: [13:43] Low and high meshes exported as OBJ (Wavefront) with selection-only enabled before Substance Painter baking. *(demo, medium; mesh-texture-limits)*
- c7: [0:35] Tutorial credits an original creator and recreates his method for newer creators; uses starter rigs for fitting. *(doc, low; avatar-ugc-accessories)*

## Numbers
- n1: **Quad Remesh quad count**: 900 or lower 
- n2: **Bake resolution / AA**: 4K, 16x anti-aliasing 
- n3: **Multires subdivision levels before sculpt**: 3 
- n4: **Bevel segments on starting cube**: 8 

## Techniques
- t1: **Quad Remesh low-poly from sculpt**: Rename high mesh, run Quad Remesh with ~900 quads, symmetry X, to create low poly under triangle limit; fill brim with poke faces for smooth bottom.
- t2: **Seam-based UV unwrap**: Mark seams on high-poly edges, Angle Based unwrap, flatten brim edges with proportional editing, manually pack islands.
- t3: **Substance baking with high-poly cage**: Import low mesh, set high-definition mesh, adjust max frontal distance until no red cage errors, bake AO/curvature/thickness.
- t4: **Layered AO and curvature shading in Substance**: Black mask generator with AO inverted, blur, soft light blend; curvature layer inverted with brightness reduced.
- t5: **Triangle reduction by edge dissolve**: Ctrl X dissolve edges in densely looped inner areas, keep seams, avoid large dissolves to limit morphing.

## Quotes (brief, for attribution)
> it has created a lower poly version of our hat that is under the Roblox triangle account.  (at 8:00, Zander)

## Points to
- Substance Painter
- Quad Remesher (Blender add-on)
- Roblox Studio
- Affinity
- SoftGB starter rigs
