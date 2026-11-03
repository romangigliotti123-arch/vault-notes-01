---
type: research-source
id: yt-vD6O-0U4P2k
title: "Blender Particles Tutorial: How to Make Particles Follow a Path (Animation)"
source_type: "youtube"
creator: "Darkfall"
url: "https://www.youtube.com/watch?v=vD6O-0U4P2k"
published: "2021-07-15"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0012
relevance: 1
density: low
tags: ["research-source", "youtube", "other"]
---
# yt-vD6O-0U4P2k

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Darkfall 2021 Blender GUI tutorial on making particles follow a path: emitter cube with object-rendered particles, a curve from a subdivided plane used as a force field (Flow, Strength), gravity disabled, particle baking, and H.264 MP4 render. No Claude, blender-mcp, bpy, or Roblox content.

## Claims
- c1: Source is a manual Blender GUI particle tutorial; it does not cover Claude, blender-mcp, bpy scripting, or Roblox export. *(doc, high; other)*
- c2: [8:56] Particle cache must be baked after tuning so the simulation is stored before rendering. *(demo, medium; other)*

## Techniques
- t1: **Curve force field for particle paths**: Convert subdivided plane to curve, enable Force Field set to Curve, raise Flow (about 10) to keep particles on the line; negative Strength attracts.
