---
type: research-source
id: yt-GgSbelzSFUs
title: "Blender 4.4 Beta + New LTS!  - Blender Today LIVE #254"
source_type: "youtube"
creator: "Blender"
url: "https://www.youtube.com/watch?v=GgSbelzSFUs"
published: "2025-02-18"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0058
relevance: 0
density: low
tags: ["research-source", "youtube", "automation-and-creator-workflows", "claude-blender-ai", "other"]
---
# yt-GgSbelzSFUs

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Blender Today live #254 (Feb 2025) covering Blender 4.4 beta, 4.5 alpha/LTS schedule, and weekly commit highlights. Nothing about Roblox, Claude, blender-mcp, or the Blender-to-Roblox pipeline. Only tangential bpy/Python API notes and release-schedule facts.

## Claims
- c1: [4:43] Blender 4.4 scheduled for March 18, 2025; 4.5 LTS for July 15, 2025; Blender 5.0 for November 2025 per the stream. *(doc, high; other)*
- c2: [20:07] Core change lets Python access RNA ancestors (e.g., a layer collection's view layer and scene); this is aimed at developers and add-on authors. *(doc, medium; claude-blender-ai)*
- c3: [21:29] Blender 4.5 LTS is intended as a compatibility bridge for 5.0 breaking changes, sometimes exposing both old and new Python property names. *(doc, medium; claude-blender-ai)*
- c4: [49:09] Image save gained a Python-only save-copy option that writes a file without changing the image datablock's source path. *(doc, medium; claude-blender-ai)*
- c5: [19:27] Blender 4.5 will be the last release supporting Intel Mac; Blender 5.0 targets Apple silicon only. *(doc, high; other)*
- c6: [20:12] Build bot exposes a JSON API listing latest and alpha/beta builds with download links, which launchers can use instead of scraping HTML. *(doc, medium; automation-and-creator-workflows)*

## Numbers
- n1: **Blender 4.4 release date**: March 18, 2025 
- n2: **Blender 4.5 release date**: July 15, 2025 
- n3: **Windows Blender release build time (shader compile)**: 185 s to 47 s 

## Points to
- blender.org/lts
- projects.blender.org
- opendata.blender.org
- developer.blender.org/docs (compatibility 5.0)
- vfxplatform.com
