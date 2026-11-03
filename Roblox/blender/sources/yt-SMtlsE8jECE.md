---
type: research-source
id: yt-SMtlsE8jECE
title: "OUTLINER goodies! - Blender Today LIVE #246"
source_type: "youtube"
creator: "Blender"
url: "https://www.youtube.com/watch?v=SMtlsE8jECE"
published: "2024-01-22"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0035
relevance: 1
density: low
tags: ["research-source", "youtube", "bpy-scripting-headless", "other"]
---
# yt-SMtlsE8jECE

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Blender Today live stream (Jan 2024) covering Blender 4.1-dev changes: Outliner double-click to select collection contents, Grease Pencil v3, geometry nodes panels, performance patches. No Roblox, Claude, blender-mcp, or export-pipeline content. Only tangential bpy API notes.

## Claims
- c1: Calling the bake operator with exec method now bakes synchronously, returning only after baking finishes; UI invoke keeps the old background-job behaviour. Useful for script-driven baking. *(doc, medium; bpy-scripting-headless)*
- c2: Shape key points access via Python got faster: about 2.8x with Python lists, about 11.7x for 100 elements and about 200x for 100,000 elements with compatible buffers. *(data, medium; bpy-scripting-headless)*
- c3: Video is off-topic for Roblox Studio, Claude, or blender-mcp; it is a general Blender 4.1-dev news recap with no export or import guidance. *(doc, high; other)*

## Numbers
- n1: **shape key points access speedup**: 2.8x (list) to ~200x (100k elements) Python API speedup for shape key data in 4.1 dev

## Points to
- blender.org release notes wiki archive
- developer.blender.org
