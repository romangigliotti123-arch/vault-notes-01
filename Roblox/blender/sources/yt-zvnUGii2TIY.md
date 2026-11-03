---
type: research-source
id: yt-zvnUGii2TIY
title: "AutoTrack: Smart, Easy and Automated Camera Tracking — BCON26"
source_type: "youtube"
creator: "Blender"
url: "https://www.youtube.com/watch?v=zvnUGii2TIY"
published: "2026-09-24"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0018
relevance: 1
density: low
tags: ["research-source", "youtube", "other"]
---
# yt-zvnUGii2TIY

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Talk on AutoTrack, a free Blender add-on for automated camera tracking (dual-direction tracking over substeps, filtering, 10-pass solving, surface generator, annotation masks). Not about Roblox, Claude, blender-mcp, bpy-driven workflows, or Roblox export. Only tangential Blender scripting context.

## Claims
- c1: AutoTrack is a Blender add-on that automates camera tracking; it is free and open source and installs via the Blender Extensions platform. *(opinion, high; other)*
- c2: AutoTrack works from Blender 4.2 to latest; compatibility with Blender 5.3 was promised as upcoming. An earlier Blender 5.2 update briefly broke it. *(experience, medium; other)*
- c3: Limitations: focal length cannot change during a shot (no zoom); repeating patterns confuse the tracker; needs detail to track. *(experience, medium; other)*
- c4: Does not reliably handle AI-generated footage from 2023-era models; works on coherent footage. *(opinion, low; other)*

## Numbers
- n1: **average solve error target**: <0.75 px (speaker calls it good; <1 px cited as norm for 1080p) 
- n2: **claimed speedup**: >30x vs manual tracking 
- n3: **default marker keep ratio in filtering**: 80% kept, not below ~20% remaining 
- n4: **solve passes**: 10 solves with default settings, plus a cleaning pass 
- n5: **demo clip**: 173 frames, ~5 min tracking, 720p; final solve 0.71 px 

## Techniques
- t1: **Substep scanning**: Track whole clip at low detail, flag high-motion frames as substeps, then distribute tracker markers across substeps and track forward and backward from each.

## Points to
- Blender Extensions platform (AutoTrack distribution)
- Packt Publishing (speaker's book, Procedural Geometry)
