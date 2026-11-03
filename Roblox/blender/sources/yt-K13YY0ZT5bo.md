---
type: research-source
id: yt-K13YY0ZT5bo
title: "🔴 LIVE 🔴 | UGC Creation + QnA w/ Crimora"
source_type: "youtube"
creator: "Zander"
url: "https://www.youtube.com/watch?v=K13YY0ZT5bo"
published: "2025-12-28"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0017
relevance: 1
density: low
tags: ["research-source", "youtube", "avatar-ugc-accessories", "mesh-texture-limits", "other"]
---
# yt-K13YY0ZT5bo

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Livestream of a Roblox UGC creator making flower accessory models (blue, red, orange variants) in Blender, with off-topic chat. Almost no Blender-to-Roblox pipeline detail: no blender-mcp, bpy, or export settings. Useful only as anecdotal notes on UV seams, packing, and PBR cost perception.

## Claims
- c1: [1:31] Creator checks triangle count of a flower model; reads it as about 2K triangles. No stated Roblox limit. *(demo, low; mesh-texture-limits)*
- c2: [6:34] UV grid layout: creator says it deforms the model slightly but makes packing easier and gives more UV space. *(opinion, medium; mesh-texture-limits)*
- c3: [4:28] Seams placed in natural hidden spots to break up UVs; unwrap after seam, merge, then square and pack. *(demo, medium; mesh-texture-limits)*
- c4: [25:43] Creator says PBR at low texture resolution looks poor and costs 10 more Robux, which matters for young audiences. *(opinion, low; mesh-texture-limits)*
- c5: [27:05] Creator describes PBR as making items react to light but more expensive, so advises against it for this item. *(opinion, low; mesh-texture-limits)*
- c6: [2:23] Sharp shading lines on a model were fixed by raising the angle threshold setting very high. *(demo, low; other)*
- c7: [24:05] Commissioned UGC delivered as three color variants (blue, red, orange) from one base model, with base color textures baked into one image. *(experience, medium; avatar-ugc-accessories)*

## Numbers
- n1: **triangle count**: ~2K flower model, streamer's estimate
- n2: **PBR extra cost**: 10 Robux streamer's claim for PBR textures on Roblox

## Techniques
- t1: **Seam, unwrap, square, pack UVs**: Mark seams at hidden edges, merge, unwrap, square islands, then pack. Accept minor deformation for more UV space.
- t2: **Single baked color texture**: Bake all color into one image per color variant instead of separate PBR maps to avoid the PBR cost.

## Quotes (brief, for attribution)
> PBR just makes it so it like reacts to light, but it makes your items more expensive. So, that's why you probably shouldn't do it.  (at 27:05, Zander)
