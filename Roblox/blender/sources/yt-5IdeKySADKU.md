---
type: research-source
id: yt-5IdeKySADKU
title: "How to make an Aura Generator in Blender for Roblox"
source_type: "youtube"
creator: "Zander"
url: "https://www.youtube.com/watch?v=5IdeKySADKU"
published: "2026-07-29"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0012
relevance: 1
density: low
tags: ["research-source", "youtube", "avatar-ugc-accessories", "mesh-texture-limits", "other"]
---
# yt-5IdeKySADKU

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Zander's short Blender tutorial for an aura generator using geometry nodes: Ctrl+A transforms, a bounding-box cube, Collection Info with separate children, random float (scale) and vector (rotation), point count as the density lever, Realize Instances. No Claude, bpy, blender-mcp, or Roblox export/import steps.

## Claims
- c1: [0:00] Video is about building a customizable aura generator in Blender using geometry nodes, not Claude/bpy/blender-mcp or the Roblox export pipeline. *(demo, high; other)*
- c2: [0:57] Creator says bounding box must be smaller than the maximum UGC bounding box size; items are placed by origin so edge-origin items may stick out. *(experience, medium; mesh-texture-limits)*
- c3: [1:38] Items can be placed inside the avatar and clip; creator deletes them manually and says he has not solved it with geometry nodes. *(experience, medium; avatar-ugc-accessories)*
- c4: [0:15] Apply Ctrl+A (all transforms) to added objects so origin and scale sit at world origin before using them in the setup. *(demo, medium; other)*
- c5: [3:05] Geometry node setup: Object Info (bounding box) + Collection Info (separate children on) + random float (scale) + random vector (rotation) + Points count, feeding Distribute/Instance on Points, then Realize Instances. *(demo, high; other)*
- c6: [8:06] Float random must drive scale and vector random must drive rotation; swapping them caused the goofed-up result. *(demo, high; other)*
- c7: [8:35] Creator says a single UV-unwrapped item gets stacked UVs across all instances, so all share one texture; everything must be on the same texture map as UGC. *(experience, medium; mesh-texture-limits)*
- c8: [4:22] Point count controls number of items, so it is a lever for triangle count in the aura. *(demo, medium; mesh-texture-limits)*

## Numbers
- n1: **Triangle budget lever**: Point count input Creator says more or fewer points adjust triangle count

## Techniques
- t1: **Geometry Nodes aura generator**: Object Info bounding box -> random points inside box -> Instance on Points with collection instances, random scale/rotation -> Realize Instances -> Group Output. Rename group inputs via N panel.
