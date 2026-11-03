---
type: research-source
id: yt-DQrYcheSX-g
title: "Hola 2026! — Blender Today LIVE #272"
source_type: "youtube"
creator: "Blender"
url: "https://www.youtube.com/watch?v=DQrYcheSX-g"
published: "2026-01-06"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0033
relevance: 0
density: low
tags: ["research-source", "youtube", "automation-and-creator-workflows", "other"]
---
# yt-DQrYcheSX-g

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Blender Today live #272 (Jan 2026) covers Blender 5.1 development news: bug fixes, performance work, UI tweaks, and Q&A. Nothing on Roblox, Claude, blender-mcp, bpy workflows, or the FBX/glTF export pipeline. One tangential note: the sculpt sample color operator was removed, so add-ons or scripts calling it will break.

## Claims
- c1: [24:27] Sculpt mode's sculpt sample color operator was removed in 5.1 dev, replaced by unified paint sample color; add-ons or scripts calling the old operator will stop working. *(doc, high; automation-and-creator-workflows)*
- c2: [1:07] Blender 5.1 beta was scheduled for February 2026, with a 5.1 alpha already available from builder.blender.org. *(doc, medium; other)*

## Numbers
- n1: **compositor speedup**: 1.2x to 2x faster for interpolation-based nodes Glare, directional blur, lens distortion, anti-alias, blur, vector blur nodes
- n2: **polyfill speedup**: 5x faster Filling an 80,000-point Australia outline versus Blender 5.0
- n3: **grease pencil FPS**: 48 to 60 FPS Multithreaded draw cache extraction on a 240 FPS-set example file

## Points to
- builder.blender.org
- projects.blender.org
