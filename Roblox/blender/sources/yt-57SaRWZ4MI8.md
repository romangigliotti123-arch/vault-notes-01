---
type: research-source
id: yt-57SaRWZ4MI8
title: "Blender 2.90 Tutorial: Falling Cubes (Abstract, Stylized, Animation)"
source_type: "youtube"
creator: "Darkfall"
url: "https://www.youtube.com/watch?v=57SaRWZ4MI8"
published: "2021-01-28"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0018
relevance: 1
density: medium
tags: ["research-source", "youtube", "other"]
---
# yt-57SaRWZ4MI8

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Blender 2.90 GUI tutorial on an abstract falling-cubes animation: particle system instancing default cube, Brownian physics, baking, shader mixing, Musgrave volumetrics animated via keyframes, EEVEE bloom and motion blur, compositing, FFmpeg H.264 MP4 output. Covers no Roblox, Claude, MCP, bpy, or export workflow.

## Claims
- c1: Video is a manual Blender 2.90 GUI tutorial with no scripting, Python, bpy, or Claude/AI tooling shown. *(doc, high; other)*
- c2: Video does not cover Roblox Studio, FBX/glTF export, scale/axis settings, or any Roblox import step. *(doc, high; other)*
- c3: [2:47] Particle emitter set to 200 particles, frame end 250; render type changed from Halo to Object to instance the default cube. *(demo, medium; other)*
- c4: [5:22] Particle simulation must be baked to keep results; changing settings requires deleting the bake and re-baking. *(demo, medium; other)*
- c5: [9:45] Node Wrangler Ctrl+T adds mapping and texture coordinate nodes; without it, connect Texture Coordinate to Mapping manually. *(demo, medium; other)*
- c6: [10:27] Timeline keyframe interpolation set to Vector to remove ease-in/ease-out so node motion runs at constant speed. *(demo, medium; other)*
- c7: [13:45] Output set to FFmpeg video with H.264 in MP4 container for final render. *(demo, medium; other)*

## Numbers
- n1: **particle count**: 200 emitter particle number reduced to 200
- n2: **frame end**: 250 particle emitter end frame
- n3: **Brownian value**: 20 stated soft limit before typing higher values manually

## Techniques
- t1: **Particle instancing of default cube**: Add plane emitter, add particle system, set Render to Object, pick cube; use Dampen and Brownian to slow fall and add random motion; bake.
- t2: **Compositor color mix**: Load image into Mix node, cycle blend types via Node Wrangler Alt+Down, then add Hue/Saturation and Color Balance.

## Points to
- Darkfall Node Wrangler add-on
- Darkfall VFX nodes add-on
