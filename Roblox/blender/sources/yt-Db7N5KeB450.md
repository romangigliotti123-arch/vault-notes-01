---
type: research-source
id: yt-Db7N5KeB450
title: "Can Opus 5 Beat Open-Source Kimi K3 in 3D Design?"
source_type: "youtube"
creator: "Stefan 3D AI"
url: "https://www.youtube.com/watch?v=Db7N5KeB450"
published: "2026-08-02"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0034
relevance: 2
density: low
tags: ["research-source", "youtube", "claude-blender-ai", "other"]
---
# yt-Db7N5KeB450

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Informal 10-test comparison of Claude Opus 5, GPT-5.6 (Codex) and Kimi K3 doing 3D/Blender tasks through an AI agent with Blender MCP. Reports time and API cost per test; Opus best quality but far more expensive; Kimi judged best value (opinion). No Roblox export, rigging-for-Roblox, or bpy workflow detail. Transcript costs are inconsistent.

## Claims
- c1: [0:50] Test workflow: model builds a gray blockout in Blender (via MCP), then renders a video via an AI video API using the blockout as reference; Opus 5 output was judged toyish. *(demo, medium; claude-blender-ai)*
- c2: [4:24] Spaceship generator test: Opus 5 and Kimi produced Geometry Nodes generators with exposed modifier parameters (engine count, style, weathering); GPT output had about five times fewer geometry nodes than Opus. *(demo, medium; claude-blender-ai)*
- c3: [9:01] Slingshot physics test: GPT-5.6 physics was broken in the run; Kimi physics settings were better but visuals poor; Opus was judged best overall. *(demo, medium; claude-blender-ai)*
- c4: [12:59] Rig repair test on a robot with bad weights: Opus output still had broken hands, GPT skipped inputs and produced a different model, Kimi looked better but still had artifacts in the dance animation. *(demo, medium; claude-blender-ai)*
- c5: [17:54] Joystick configurator test: Opus 5 cost about $241 over 139 minutes; Kimi about $41 over more than four hours; both failed to match the reference; GPT spent less and was faster but also failed. *(demo, medium; claude-blender-ai)*
- c6: [24:42] Bowling test: Opus cost under $50 for the task and Kimi was close in quality; a Kimi render showed inverted normals that confused the first-shot result. *(demo, low; claude-blender-ai)*
- c7: [27:28] Creator estimates that running all tests via API would cost about $900 for Opus 5, about $100 for Kimi and about $80 for GPT. *(opinion, low; claude-blender-ai)*
- c8: [27:28] Creator reports one Opus 5 API task burned about $20 when routed through a Hermes agent setup; he switched that setup to DeepSeek V4 Pro, which he says is roughly 100x cheaper. *(experience, low; claude-blender-ai)*
- c9: [28:50] Opinion: Kimi K3 is about nine times cheaper than Opus 5 and sometimes matches or beats it when given more iterations; Opus 5's agentic self-reuse and multi-process work was the standout strength. *(opinion, low; claude-blender-ai)*
- c10: [0:00] Kimi K3 weights were released on Hugging Face at 1.5 TB or more, as promised by the vendor. *(doc, low; other)*

## Numbers
- n1: **Setup time**: ~3 days of recording/work 
- n2: **Cost ratio blockout test**: Kimi ~8x cheaper than Opus via API 
- n3: **Geometry nodes count**: GPT ~5x fewer than Opus per creator 
- n4: **Ragdoll test cost**: ~$100 for Opus (creator says) 
- n5: **Paper plane game cost/time**: GPT ~$2 / 8 min; Kimi ~$6 / 88 min; Opus ~$88 / 106 min 
- n6: **Joystick cost/time**: Opus $241 / 139 min; Kimi $41 (failed) over 4+ hours 
- n7: **Castle defense cost/time**: Opus $85 / 84 min; Kimi ~$5 (~1 hour); GPT ~$5 / 15 min 
- n8: **Bowling cost**: Opus under $50 
- n9: **Total API estimate**: Opus ~$900, Kimi ~$100, GPT ~$80 
- n10: **Opus single task burn**: ~$20 in one task via API 
- n11: **Kimi K3 weights size**: 1.5 TB or more 

## Techniques
- t1: **Blockout-then-render pipeline**: Ask agent to build gray blockout in Blender via MCP, then pass blockout plus style reference image to a video-generation API for final render.
- t2: **Procedural Geometry Nodes generator with exposed parameters**: Have model build Geometry Nodes group; expose engine count, style, weathering as modifier inputs so the object regenerates when changed.
- t3: **Rig test via control-rig and animation prompts**: Provide a rigged model with bad weights, ask agent to check and fix, record joint-movement video, then add an arm-swing animation.

## Quotes (brief, for attribution)
> the fact that kimi being like nine times less expensive sometimes show similar or even better results  (at 28:50, Stefan 3D AI)

## Contradictions flagged
- Kimi is 8x cheaper (4:14) versus nine times cheaper (28:50) (vs Creator's own earlier cost figure in the same video)
- Opus 5 was the best quality in most tests (vs Creator's own notes that Kimi beat Opus on rig repair and bowling cost-quality tradeoff)

## Points to
- Blender MCP (named as 'blender true mcp')
- Hugging Face (Kimi K3 weights)
- DeepSeek V4 Pro (mentioned as cheaper replacement)
