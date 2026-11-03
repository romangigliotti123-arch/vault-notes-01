---
type: research-source
id: yt-6ExAg0WSUQs
title: "Open-Source AI Took Over 3D Again - GLM 5.3 & Qwen 3.8 Max"
source_type: "youtube"
creator: "Stefan 3D AI"
url: "https://www.youtube.com/watch?v=6ExAg0WSUQs"
published: "2026-08-26"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0025
relevance: 1
density: low
tags: ["research-source", "youtube", "automation-and-creator-workflows", "claude-blender-ai"]
---
# yt-6ExAg0WSUQs

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Off-topic AI model comparison (GLM 5.3, Qwen 3.8, Grok) on 10 3D tasks, mostly generated via LLM-driven Blender or Unity. Gives only anecdotal results: no Roblox export/import, no bpy code, no mesh/rig specs, no blender-mcp setup details. Useful only as weak anecdotes on which models handled Blender tasks.

## Claims
- c1: [7:22] Tree-animation task run in Blender by LLM: Grok 4.6 finished in ~30 min; GLM took ~4 hours per the video; Qwen output looked like a bush, not a tree. *(demo, low; claude-blender-ai)*
- c2: [17:53] Procedural city in Blender: GLM output had poor lighting and geometry nodes collapsed into one stack; Grok and Qwen judged better. Author's opinion, single run. *(opinion, low; claude-blender-ai)*
- c3: [6:17] GLM with max thinking effort often stalled or crashed on the official API, with long think-without-acting loops. Author reports this as a workflow problem, not a model-quality one. *(experience, low; claude-blender-ai)*
- c4: [13:03] Demolition test was run in Unity via MCP rather than Blender; the author says his Blender/Unity MCP setup is covered in other videos, not this one. *(experience, low; automation-and-creator-workflows)*
- c5: [20:33] Kite-physics test in Unity: only Grok was judged to meet the request; GLM never reported finishing; Grok took ~53 min, Qwen ~23 min. *(demo, low; claude-blender-ai)*

## Numbers
- n1: **Tree-animation task duration**: Grok ~30 min vs GLM ~4 h 
- n2: **Kite task duration**: Grok 53 min; Qwen 23 min 
- n3: **Model parameters claimed**: GLM 5.3 ~750B vs Kimi K3 ~2.7T (claimed by author) 

## Points to
- Fish Audio (sponsor, not relevant)
- Tripo (3D generation API used in tests)
