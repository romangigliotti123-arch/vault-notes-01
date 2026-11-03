---
type: research-source
id: yt-x3znZU4YUME
title: "GAUSSIAN SPLATS, DLSS, Outliner, and more! - Blender Today LIVE #290"
source_type: "youtube"
creator: "Blender"
url: "https://www.youtube.com/watch?v=x3znZU4YUME"
published: "2026-09-30"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0051
relevance: 1
density: low
tags: ["research-source", "youtube", "bpy-scripting-headless", "common-mistakes-fixes", "other"]
---
# yt-x3znZU4YUME

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Blender Today #290 weekly recap of Blender 5.3 alpha changes (animation, compositor, Cycles DLSS 4.5 denoise, Eevee, geometry nodes, Gaussian splat import, outliner custom sort, markdown labels, projects, UI). No Roblox, Claude, blender-mcp, or export-pipeline content. Only tangential bpy API and add-on-compat notes.

## Claims
- c1: [1:31:35] Source contains no Roblox, Claude, blender-mcp, or Roblox export content; it covers Blender 5.3 alpha features only. *(doc, high; other)*
- c2: [6:17] Built-in Blender color spaces were added to the interoperability list and exposed to the Python API so scripts can reference them reliably. *(doc, high; bpy-scripting-headless)*
- c3: [1:11:11] Add-ons using the new label markdown widget will likely fail or break when opened in Blender 5.2 (LTS); presenter suggests version-gating add-ons to 5.3+. Untested. *(opinion, medium; bpy-scripting-headless)*
- c4: [1:07:45] Blender 5.3 defaults untrusted-file Python auto-run to not executing and makes the 'always allow' auto-run option harder to reach, with a warning when enabled. *(doc, high; common-mistakes-fixes)*
- c5: [1:22:56] New Python property 'property split factor' replaces hardcoded 0.4 label/content column splits in add-on UI code. *(doc, high; bpy-scripting-headless)*
- c6: [0:24] Blender 5.3 release is in alpha; beta expected after the episode, and the release notes cover about 539 commits since the prior recap three weeks earlier. *(doc, medium; other)*

## Numbers
- n1: **commits since last recap**: ~539 
- n2: **minimum NVIDIA driver for Cycles DLSS denoise**: 59 (per presenter) 

## Points to
- https://devtalk.blender.org (forum, replacing community Q&A)
- CG Matter Gaussian splatting video
- SuperSplat
