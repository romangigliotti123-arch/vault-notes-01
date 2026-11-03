---
type: research-source
id: yt-hoO3jCtxnjI
title: "Almost BETA - Blender Today LIVE #248"
source_type: "youtube"
creator: "Blender"
url: "https://www.youtube.com/watch?v=hoO3jCtxnjI"
published: "2024-02-05"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0040
relevance: 1
density: low
tags: ["research-source", "youtube", "claude-blender-ai", "other"]
---
# yt-hoO3jCtxnjI

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Blender Today live #248 (Feb 2024) covers Blender 4.1 development changes: compositor, Cycles, geometry nodes, baking, UI and USD. It does not mention Roblox, blender-mcp, Claude, or the Roblox export/import pipeline. Only tangential bpy items appear (USD import hooks, addon zip __init__ fix).

## Claims
- c1: Addon install from zip failed when the zip's __init__.py lacked its own folder; this was fixed in the 4.1 dev cycle. *(doc, medium; claude-blender-ai)*
- c2: A bpy.types USD hooks class can define an on-import function that runs after USD import, aimed at studio pipelines. *(doc, medium; other)*

## Numbers
- n1: **Blender dev commits in this weekly update**: 261 commits, 26 fixes, 66 cleanups 

## Points to
- blender.org/blog
- studio.blender.org blog (retopology tools)
