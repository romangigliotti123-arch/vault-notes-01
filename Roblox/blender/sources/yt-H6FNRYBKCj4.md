---
type: research-source
id: yt-H6FNRYBKCj4
title: "How Blender Changed Theatre — BCON26"
source_type: "youtube"
creator: "Blender"
url: "https://www.youtube.com/watch?v=H6FNRYBKCj4"
published: "2026-09-25"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0021
relevance: 1
density: low
tags: ["research-source", "youtube", "other"]
---
# yt-H6FNRYBKCj4

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Off-topic for Blender-to-Roblox work. A stage designer describes using Blender geometry nodes and math nodes to build a theater stage simulator where motor speeds (cm/s) set movement durations in timeline frames. Covers no Roblox export, bpy/MCP, mesh limits, rigging or UGC. Only the geometry-nodes timing approach is loosely transferable.

## Claims
- c1: [9:03] Geometry nodes used for a custom modifier UI: Combine XYZ on transform for rotation, Collection Info node to link a wall to the main rotation. *(experience, medium; other)*
- c2: [12:41] Movement timing computed with math nodes, displayed via Value to String nodes in a UI in front of camera. *(experience, medium; other)*
- c3: [9:46] Main rotation diameter 40 m gives circumference 43.98 m used to derive movement durations. *(data, high; other)*
- c4: [10:27] Motor speed range 0.2 cm/s to 20 cm/s gives full 360 degree rotation time of about 22,000 s (~6 h) at minimum and 220 s at maximum. *(data, high; other)*
- c5: [10:27] At 30 FPS, the slowest full rotation is about 660,000 frames and the fastest about 6,600 frames in the timeline. *(data, high; other)*
- c6: [8:12] Walls made to emit light using a plane with an emission shader; stage imported from a high-poly OBJ was remodeled from scratch to be lightweight. *(experience, medium; other)*
- c7: [2:50] Speaker first used Rhino 3D, then Blender with Eevee for an animated short; learned keyframes in Blender and used DaVinci Resolve for editing. *(experience, medium; other)*
- c8: [15:35] Speaker opinion: the Blender pre-visualization saved rehearsal time and let the team plan movement durations before the venue was built. *(opinion, low; other)*

## Numbers
- n1: **stage rotation diameter**: 40 m main sled rotation diameter, used to compute circumference
- n2: **circumference**: 43.98 m diameter x pi
- n3: **motor speed range**: 0.2 to 20 cm/s stated range for rotation speed
- n4: **slowest full 360 rotation**: ~22,000 s (~6 h) at minimum speed
- n5: **fastest full 360 rotation**: ~220 s (3 min 40 s) at maximum speed
- n6: **timeline frames at 30 FPS**: 660,000 (slow) / 6,600 (fast) seconds multiplied by FPS

## Techniques
- t1: **Geometry nodes modifier UI for stage control**: Combine XYZ on Transform for rotation; Collection Info to link wall objects; attribute nodes for per-light colors; expose as modifier inputs.
- t2: **Duration from distance and speed**: Distance = target minus current position; time = distance / speed (cm/s converted from speed percent); convert seconds to frames by multiplying FPS; show with Value to String.

## Points to
- Rhino 3D
- Blender Eevee
- DaVinci Resolve
- GarageBand
