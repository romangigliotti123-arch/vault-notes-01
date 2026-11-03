---
type: research-source
id: yt-9lFE4T7iZKM
title: "I Ran GPT-6 for 3 Days Non-Stop and It Created This…"
source_type: "youtube"
creator: "Stefan 3D AI"
url: "https://www.youtube.com/watch?v=9lFE4T7iZKM"
published: "2026-09-16"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0020
relevance: 1
density: low
tags: ["research-source", "youtube", "claude-blender-mcp", "creator-workflows", "other"]
---
# yt-9lFE4T7iZKM

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Video on running GPT-6 for ~3 days to build a zombie FPS in Unity and a GTA-style city in Unreal Engine 5. Off-topic for Blender/Roblox: no bpy scripting, no Roblox export or import steps. Only tangential item: a Higgsfield MCP/Blender plugin used to generate 3D models via third-party 3D AI services, with a rough asset cost estimate.

## Claims
- c1: [4:40] Creator used a Higgsfield MCP plus Higgsfield Blender plugin; says it exposes multiple 3D AI services (Tripo, Meshy, Hunyuan) under one subscription, unlike single-vendor APIs. *(opinion, low; claude-blender-mcp)*
- c2: [9:11] Creator estimates total asset generation cost for the zombie game at roughly $40-85, and says daily 3D generation for his own project stays under about $5. *(opinion, low; creator-workflows)*
- c3: [8:31] Creator reports the zombie game consumed about 1.29 billion tokens, and the GTA-style game about 2.5 billion, over several days of prompting. *(demo, medium; other)*

## Numbers
- n1: **token usage**: 1.29 billion Total tokens for zombie FPS game built with GPT-6 in Unity
- n2: **asset cost estimate**: $40-85 (creator rounds to ~$100) Estimated cost for 100 images, 50 models, ~35 rigs for zombie game
- n3: **daily 3D generation spend**: under $5/day Creator's own ongoing 3D model generation spend, per his statement

## Techniques
- t1: **Iterative prototyping**: Start with a 2D or basic procedural prototype, verify mechanics, then add layers (3D, realistic assets, animation) in small steps rather than one-shot prompts.
- t2: **Video-reference animation**: Record a video of the motion (e.g. sitting in a car), feed it to the AI as reference, and have it generate the animation; creator says it failed without the video reference.

## Points to
- Higgsfield (MCP and Blender plugin)
- Unity MCP (official and Ankle Breaker)
- GVHMR motion library
- Mixamo
