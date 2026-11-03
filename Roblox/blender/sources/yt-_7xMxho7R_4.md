---
type: research-source
id: yt-_7xMxho7R_4
title: "FASTER Blender! ⚡️ Blender Today LIVE #287"
source_type: "youtube"
creator: "Blender"
url: "https://www.youtube.com/watch?v=_7xMxho7R_4"
published: "2026-08-04"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0063
relevance: 1
density: low
tags: ["research-source", "youtube", "bpy-scripting-headless", "creator-workflows", "other", "texturing-baking-uv"]
---
# yt-_7xMxho7R_4

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Blender Today Live #287 (Blender 5.3 dev news). Covers asset-browser speedups, compositor node ports, baking fix for tiny UV triangles, Eevee shadow speedups, Vulkan default for new installs, and experimental collection importer. Nothing on Roblox, blender-mcp, Claude, or Roblox export settings.

## Claims
- c1: Baking fix: tiny UV triangles were skipped by conservative rasterization, leaving gaps; fixed by Roman. Still need enough seam margin around islands. *(demo, high; texturing-baking-uv)*
- c2: Blender 5.3 release date listed as November 10, 2026; 5.3 beta expected about two months after the 30 Sept episode. *(doc, high; other)*
- c3: Vulkan becomes default for new installs/preferences in 5.3 on Windows x64 (not ARM) and Linux; existing user preferences are updated too per the discussed change. *(doc, medium; other)*
- c4: New Python API lets add-on developers activate RNA buttons from Python; top and status bar can be populated from Python. *(doc, medium; bpy-scripting-headless)*
- c5: Collection importer (experimental, USD only for now) lets a collection be re-imported repeatedly without going through File > Import; relative paths supported; re-import of same format may warn. *(demo, medium; other)*
- c6: Texture layers are an early prototype (procedural and paint layers, multilayer EXR export); presented as work in progress, not in main build. *(demo, medium; other)*
- c7: Asset library files can encode minimum Blender version in filename (e.g. @B5_3 style suffix) so Blender hides incompatible versions. *(doc, medium; creator-workflows)*
- c8: EEVEE shadow read-back avoidance reportedly gives about 1.5x shadow performance (one example 21s to ~16s); tester variance noted. *(demo, low; other)*
- c9: FBX exporter is now the built-in C++ version, replacing the old Python one; regressions should be reported. *(opinion, low; other)*

## Numbers
- n1: **Blender 5.3 release date**: 2026-11-10 
- n2: **Commits in 5.3 cycle covered**: 264 total, 136 fixes 
- n3: **Asset preview parallel downloads**: 5 at once 
- n4: **Shader/geometry recursive closure limit**: 100 default 

## Points to
- https://projects.blender.org
- https://code.blender.org
- https://blender.community
