---
type: research-source
id: yt-_GRRf6m91RM
title: "3D-to-2D Animation Smear Effect Technique Based on Japanese Hand-Drawn Style — BCON26"
source_type: "youtube"
creator: "Blender"
url: "https://www.youtube.com/watch?v=_GRRf6m91RM"
published: "2026-09-25"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0017
relevance: 1
density: medium
tags: ["research-source", "youtube", "other"]
---
# yt-_GRRf6m91RM

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Conference talk (BCON26) on Smear FX, a Blender addon that generates Japanese-style 2D smear effects with geometry nodes, driven by sampled anchor-point motion paths. Covers timing/smear theory, constant vs linear interpolation trick, freestyle and compositing post-production. No Roblox, Claude, blender-mcp, or bpy-pipeline content.

## Claims
- c1: [3:43] Speaker built Smear FX as a Blender addon by writing Blender scripts, using built-in features. *(opinion, medium; other)*
- c2: [13:56] Sampling motion path: set armature interpolation to linear, then click back-trajectory so addon samples anchor point through subframes and feeds geometry nodes. *(demo, medium; other)*
- c3: [22:22] Inside geometry nodes, multiplying points by the inverse of an Empty's transform matrix then abs(x,y,z)<1 gives a simple inside-box test. *(demo, medium; other)*
- c4: [28:54] Post-production: enable Freestyle and transparent render passes, use separate view layers (outline, freestyle, diffuse), combine via depth testing in compositor. *(demo, medium; other)*

## Numbers
- n1: **Conference poster**: CG Asia 2024 
- n2: **Animation frame rate**: 24 fps; animated on twos/threes 

## Techniques
- t1: **Linear-interpolated anchor for subframe sampling**: Duplicate armature, parent anchor point to linear-interpolated armature, click back trajectory to sample subframe positions for motion path.
- t2: **Freestyle + compositor depth combine**: Render outline and Freestyle line-art in separate view layers, combine with depth test math node, multiply with diffuse color render.

## Quotes (brief, for attribution)
> 3D to 2D animation smear effect technique based on Japanese handdrawn animation style.  (at 0:03, Blender)

## Points to
- Smear FX addon (download link in talk, free until weekend)
- CG Asia 2024 poster paper
- Affinity (coloring tool)
