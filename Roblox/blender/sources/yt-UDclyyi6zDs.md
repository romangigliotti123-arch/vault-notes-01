---
type: research-source
id: yt-UDclyyi6zDs
title: "I Created a Game with AI and Got 1000 Players"
source_type: "youtube"
creator: "Stefan 3D AI"
url: "https://www.youtube.com/watch?v=UDclyyi6zDs"
published: "2026-10-11"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0028
relevance: 1
density: low
tags: ["research-source", "youtube", "mesh-texture-limits", "other"]
---
# yt-UDclyyi6zDs

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Video about building a browser/online racing game "Zero G" with Claude plus Tripo P2 generated 3D car models. No Blender, bpy, blender-mcp, or Roblox content. Only tangential points: Tripo P2 models ran around 10k triangles, and the creator advises specifying a poly budget up front.

## Claims
- c1: [4:02] Tripo P2 models were mostly around 10,000 triangles; creator says this is not bad but could be lower. Not a Roblox limit. *(experience, medium; mesh-texture-limits)*
- c2: [5:22] For Tripo P2, specify an approximate poly count budget in prompt, or have Claude analyze the image and pick a quad budget, to avoid regenerating models. *(experience, medium; mesh-texture-limits)*
- c3: [4:42] Tripo Studio credits are cheaper than Tripo API fixed pricing; Studio and API credits are separate pools. *(experience, low; other)*
- c4: [6:20] Whole project took a little over two days with a Claude Max subscription; total asset spend about $69 plus subscription. *(experience, low; other)*

## Numbers
- n1: **Tripo P2 model triangle count**: ~10,000 triangles 
- n2: **Iterations for art feedback**: at least 30 
- n3: **Total asset spend**: ~$69 plus Claude Max subscription 

## Techniques
- t1: **Poly budget in prompt for image-to-3D**: Before generating in Tripo P2, state the target polygon or quad count, or ask Claude to analyze the reference image and choose a budget. Skipping this forced regeneration or optimization.

## Points to
- Tripo P2
- Tripo API
- Claude Max
- Opus 5
