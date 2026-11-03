---
type: research-source
id: yt-cJH4UgCWrT8
title: "AI Built My Game in 47 Hours So I Can Destroy Everything"
source_type: "youtube"
creator: "Stefan 3D AI"
url: "https://www.youtube.com/watch?v=cJH4UgCWrT8"
published: "2026-10-03"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0023
relevance: 1
density: low
tags: ["research-source", "youtube", "automation-and-creator-workflows", "claude-blender-ai", "rigging-animation"]
---
# yt-cJH4UgCWrT8

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Video about generating an entire destructible Unity game with AI asset APIs (Tripo, Hunyuan, Higgsfield) and Claude over 47 hours. Blender and Roblox are barely mentioned; no Blender MCP, bpy, or Roblox export/import workflow is shown. Only tangential points: prompt-specified tool routing, part-wise generation, and cost/token figures.

## Claims
- c1: [2:41] Creator's Blender usage is not shown; the build targets Unity with an empty Unity project, not Roblox Studio. *(demo, high; claude-blender-ai)*
- c2: [1:20] Creator says prompts must name the tool per task (e.g., which 3D model service to use), since references alone gave worse results. *(opinion, medium; claude-blender-ai)*
- c3: [10:16] Creator told Claude to generate character pieces separately and assemble them; he says combined generation looked better, and manual assembly gives better results still. *(opinion, low; rigging-animation)*
- c4: [1:20] Creator says Tripo 3.1 suits high-poly models but not characters; for rig-ready characters the prompt should specify the model. *(opinion, low; rigging-animation)*
- c5: [6:54] Run ran about 47 hours but only about 38 hours of work; it stalled on an out-of-memory error while Unity was playing and needed a manual Unity restart. *(experience, medium; automation-and-creator-workflows)*
- c6: [6:54] Usage was 5.28B tokens, about 97% cached; API-equivalent cost about $2.5k, actual spend about $300. *(data, medium; automation-and-creator-workflows)*
- c7: [6:14] Pipeline produced over 2,000 images (about 367 image jobs), about 300 model jobs, and 414 ElevenLabs voice jobs costing about $5. *(data, medium; automation-and-creator-workflows)*

## Numbers
- n1: **build duration**: 47 hours (about 38 hours actual) 
- n2: **tokens used**: 5.28B, ~97% cached 
- n3: **cost**: ~$2.5k API-equivalent; ~$300 actual 
- n4: **model jobs**: ~300 
- n5: **image jobs**: 367 (summary says 2000+ images total) 
- n6: **ElevenLabs jobs**: 414 jobs, ~$5 
- n7: **API budget**: $500 total; Chopper and Full AI $50 each 

## Techniques
- t1: **Tool-routing in prompt**: Name which generation service to use for each asset type (e.g., high-poly vs character models), and specify part-wise generation, UV layout and texture-to-emissive steps, so the agent does not pick a wrong model.

## Points to
- Hunyuan
- Tripo
- Higgsfield
- Unity
- ElevenLabs
- Claude Max plan
