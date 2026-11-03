---
type: research-source
id: yt-t9vW-93qaN4
title: "Grooming Seth Rogen: Restoring a Hairline for a High-Stakes Commercial — BCON26"
source_type: "youtube"
creator: "Blender"
url: "https://www.youtube.com/watch?v=t9vW-93qaN4"
published: "2026-09-24"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0020
relevance: 0
density: low
tags: ["research-source", "youtube", "other"]
---
# yt-t9vW-93qaN4

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Conference talk on grooming and restoring a hairline for a Skip the Dishes TV commercial starring Seth Rogan, made in Blender. It covers hair curves in sculpt mode, Geometry Nodes hair, curve-based design iterations, 3D tracking, and ACES/EXR delivery. It has no content on Claude, blender-mcp, bpy scripting, or Roblox export. Relevance to the topic is very low.

## Claims
- c1: Source is a VFX commercial-grooming talk; it does not discuss Claude, blender-mcp, bpy scripting, or Blender-to-Roblox export. *(doc, high; other)*
- c2: Blender 5.0 added native ACES support; the speaker's project used Blender 4.4, which lacked it. *(experience, medium; other)*
- c3: Speaker says hair grooms can now be started by adding an empty hair curve object, entering sculpt mode, and placing guide curves, instead of the old emitter system. *(experience, medium; other)*

## Numbers
- n1: **Blender version with native ACES**: 5.0 (4.4 lacked it) 
- n2: **Hair growth trim-curve keyframe duration**: 15 frames 

## Techniques
- t1: **Hair guide curves in sculpt mode**: Add empty hair curve object to mesh, enter sculpt mode, place guide hairs; interpolated later. Adjust curliness/noise/frizz via asset browser modifiers.
- t2: **Color-coded groom communication**: Color curve groups (e.g., big curls purple, hairline pink, fine details green) and send images to client to focus feedback on regions.
- t3: **Hair growth via trim curves**: Keyframe trim curves node over 15 frames for hair-growth effect; shadow catcher then marries shot.
