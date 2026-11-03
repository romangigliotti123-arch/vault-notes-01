---
type: research-source
id: yt-GIoNAXTyuao
title: "Blender 5.3 PROJECTS! 🤝 Blender Today LIVE #283"
source_type: "youtube"
creator: "Blender"
url: "https://www.youtube.com/watch?v=GIoNAXTyuao"
published: "2026-06-09"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0057
relevance: 1
density: low
tags: ["research-source", "youtube", "automation-and-creator-workflows", "other"]
---
# yt-GIoNAXTyuao

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Blender Today Live #283 covers Blender 5.2 LTS and 5.3 alpha UI and feature changes (animation, assets, compositor, geometry nodes, grease pencil, UV, VR, sequencer, weight paint). It has no Roblox, Claude, blender-mcp, or Roblox export content. Only tangential items: a built-in project system in 5.3 alpha, and Python access to texture-cache file paths.

## Claims
- c1: [1:43:54] Source does not mention Roblox, Roblox Studio, FBX/glTF export, MeshPart, R15 rigs, Claude, blender-mcp, or bpy batch workflows; it is a Blender 5.2/5.3 feature roundup. *(doc, high; other)*
- c2: [20:32] Blender 5.3 alpha adds a built-in project setup: a project root marked by a hidden 'Blender project' folder; blend files saved inside it belong to that project. Project variables are still in development. *(demo, medium; automation-and-creator-workflows)*
- c3: [30:21] Output path variable templates such as {blend name} and {project name} work in File Output; the speaker says there is no documentation yet for project variables. *(demo, medium; automation-and-creator-workflows)*
- c4: [56:05] Python API exposes file paths for each Cycles texture-cache file, covering UDIM, image sequences and TX files, intended for render farms and scripts that collect relevant files. *(doc, medium; automation-and-creator-workflows)*
- c5: [1:19:01] Sequencer speed-up: a 4K render took 135 ms on GPU versus 235 ms before, and 1420 ms on CPU versus 1550 ms before. *(demo, low; other)*

## Numbers
- n1: **4K sequencer render time, GPU**: 235 ms -> 135 ms Speaker's reported timing for compositor-effect/modifier optimization
- n2: **Blender 5.3 release date**: 10 November Stated by speaker from projects.blender.org LTS schedule

## Techniques
- t1: **Set up a Blender 5.3 project**: Save the untitled file, then in Preferences > Project Setup click New Project and choose a root folder. Blender creates a hidden 'Blender project' marker folder at that root.
