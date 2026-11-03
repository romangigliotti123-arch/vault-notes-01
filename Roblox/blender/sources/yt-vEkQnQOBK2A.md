---
type: research-source
id: yt-vEkQnQOBK2A
title: "Mathemagics: Building Assets for Realtime Effects — BCON26"
source_type: "youtube"
creator: "Blender"
url: "https://www.youtube.com/watch?v=vEkQnQOBK2A"
published: "2026-09-25"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0051
relevance: 1
density: medium
tags: ["research-source", "youtube", "mesh-texture-limits", "other"]
---
# yt-vEkQnQOBK2A

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
BCON26 talk on Blender assets for real-time engines (Unity, Apple Vision Pro case study), not Roblox, Claude, or blender-mcp. Covers using UV maps as a data channel for scrolling, drawn-on line animation via alpha clipping in a static mesh, looping radial rings, and a tiled 3D Voronoi cloud baked to PNG. Only tangentially relevant to the Roblox pipeline.

## Claims
- c1: Blender does not support 3D textures; a 3D Voronoi volume had to be split into per-slice PNG tiles, and Eevee rendering became unreliable at 64 layers, so the demo used about half. *(demo, medium; mesh-texture-limits)*
- c2: Blender cannot store a 3-component vector in a UV map, unlike Unity, so the presenter used surface normals plus radius to recover tube midline positions. *(experience, medium; mesh-texture-limits)*
- c3: Static mesh with vertex displacement and UV-stored animation data was chosen over particles or CPU mesh updates to keep stroke width constant and avoid CPU limits on the target platform. *(opinion, medium; other)*
- c4: Prototyping real-time effects in Blender with Eevee first is useful because Eevee shares concepts with game engine real-time renderers. *(opinion, low; other)*
- c5: Curve-to-tube in recent Blender versions with UV factor mode yields a normalized 0-1 length UV without the manual cyclic-seam workaround. *(demo, medium; other)*

## Numbers
- n1: **Voronoi tile resolution**: 64x64 px per tile, 8x8 = 64 tiles packed into one PNG 
- n2: **3D tiling repeats**: 27 copies of point cube for seamless 3D repeat 
- n3: **UV loop durations**: 2 s and 4 s, suggests prime numbers to reduce visible repetition 
- n4: **Radial ring animation**: 5 elements, step 0.2 in UV space, ring spacing 0.1 

## Techniques
- t1: **UV as data channel**: Store per-vertex parameters (spline length factor, offsets) in UV coordinates; read them in the real-time shader to animate a static mesh without runtime mesh updates.
- t2: **Procedural looping via fraction of scene time**: Divide scene time by animation duration, take fractional part, add to UV value; use two different durations for layered textures to avoid visible repetition.
- t3: **Alpha-clip draw-on via vertex displacement**: Map tube UV length to show/hide thresholds with smoothstep, scale radius toward midline using surface normal, displace vertices in vertex shader.
- t4: **Tiled 3D Voronoi baked to PNG**: Generate jittered point grid in Geometry Nodes, replicate points 27 times for seamless tiling, store distance/normal data in RGB, render slices to atlas.

## Points to
- Blender Studio
- GitHub repo with source .blend files and a RenderKit plugin (named in talk, no URL given)
