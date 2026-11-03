---
type: research-source
id: yt-W6AYTbqAlcI
title: "TEXTURE CACHE MIPMAPS — Blender Today LIVE #278"
source_type: "youtube"
creator: "Blender"
url: "https://www.youtube.com/watch?v=W6AYTbqAlcI"
published: "2026-03-31"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0057
relevance: 1
density: low
tags: ["research-source", "youtube", "mesh-texture-limits", "other"]
---
# yt-W6AYTbqAlcI

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Blender Today Live #278 (2026-03-31) covers Blender 5.2 LTS dev features. Relevant only tangentially: Cycles texture cache (.tx mipmaps) to cut texture memory. Nothing on Roblox, blender-mcp, bpy-driven Claude workflows, or the Roblox export pipeline.

## Claims
- c1: [13:48] Cycles texture cache generates mipmap-like .tx files beside source images, reducing texture memory; toggle under Render Properties > Performance > Texture Cache, on by default. *(demo, high; mesh-texture-limits)*
- c2: [17:52] Presenter's benchmark numbers: Attic scene memory 5.5 GB to 1.5 GB with render time ~12.57s to 12.64s; Bistro 4.3 GB to 1 GB; Junk shop ~2 s slower. *(data, medium; mesh-texture-limits)*
- c3: [14:29] Texture cache is in Blender 5.2 LTS (release July 14; beta June 3), not 5.1. *(doc, high; other)*
- c4: [20:00] TX files can be generated from the command line without opening the UI, enabling render-farm or script pre-generation; exact command was garbled in transcript. *(opinion, low; other)*
- c5: [16:31] Simplify panel texture limit replaced by a texture resolution percentage that works with and without texture cache. *(demo, medium; mesh-texture-limits)*

## Numbers
- n1: **Attic scene memory**: 5.5 GB -> 1.5 GB 
- n2: **Bistro memory**: 4.3 GB -> 1 GB 
- n3: **Attic render time**: 12.57 s -> 12.64 s 

## Techniques
- t1: **Enable Cycles texture cache**: Render Properties > Performance > Texture Cache; enable Auto Generate; optionally set cache path in Preferences > File Paths > Texture Cache (relative or absolute).
