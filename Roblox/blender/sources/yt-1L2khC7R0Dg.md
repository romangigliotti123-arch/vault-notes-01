---
type: research-source
id: yt-1L2khC7R0Dg
title: "I'M MAKING A ROBLOX GAME WITHOUT AI."
source_type: "youtube"
creator: "SmartyRBX"
url: "https://www.youtube.com/watch?v=1L2khC7R0Dg"
published: "2026-10-12"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0145
relevance: 1
density: low
tags: ["research-source", "youtube", "automation-and-creator-workflows", "other"]
---
# yt-1L2khC7R0Dg

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Off-topic for Blender-to-Roblox work. A Roblox streamer's rant on solo-dev difficulty, AI-assisted development, and hand-building maps in Studio. Blender is mentioned once, only as an option he considered for building assets and then set aside in favor of Studio. No blender-mcp, bpy, FBX/glTF export, or Roblox import settings are covered. Relevance is minimal.

## Claims
- c1: [53:33] Streamer says he is considering whether to build arena assets in Blender or inside Roblox Studio, and prefers Studio. *(opinion, high; other)*
- c2: [37:11] Streamer's stated workflow: build the map and UI by hand first, then use AI for coding at the end, arguing slower manual building forces game-design thinking. *(opinion, medium; other)*
- c3: [30:58] Streamer says Rojo is an extra manual step he dislikes and built his own sync tool, MCP board, to auto-sync repos; not Blender-related. *(opinion, medium; automation-and-creator-workflows)*
- c4: [18:49] Only Roblox Studio plugin he says he uses regularly is Moon Animator; he mentions maybe B tools for studded parts. *(experience, medium; automation-and-creator-workflows)*
- c5: [1:03:14] In Studio, a decal set as a texture can be cropped by changing tiling and offset values, e.g. 300 by 300 studs with offset V 300. *(demo, medium; other)*
- c6: [54:56] Adding a reference image as a Decal on a part in Studio works as a build reference; disable cast shadow after loading. *(demo, medium; other)*

## Numbers
- n1: **texture tiling**: 300 by 300 studs, offset V 300 
- n2: **Rojo requirement**: run rojo serve once per work session; auto-resyncs on file changes 

## Techniques
- t1: **Reference image as decal in Studio**: Upload reference image as a Decal on a part, turn off cast shadow after load, then build geometry by hand against it.
- t2: **Texture crop via tiling/offset**: Set texture StudsPerTile and offset values to crop a decal image to a sub-region on a single part.

## Quotes (brief, for attribution)
> I kind of want to do this inside of Studio.  (at 53:33, SmartyRBX)

## Points to
- Rojo
- MCP board (streamer's own tool)
- Moon Animator plugin
- Eclipse Animator plugin
