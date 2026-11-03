---
type: research-source
id: yt-FUe4jbV_gNc
title: "I Tested Sakana Fugu in Blender"
source_type: "youtube"
creator: "Aidan Stanik"
url: "https://www.youtube.com/watch?v=FUe4jbV_gNc"
published: "2026-06-23"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0022
relevance: 2
density: low
tags: ["research-source", "youtube", "automation-and-creator-workflows", "claude-blender-ai"]
---
# yt-FUe4jbV_gNc

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Video compares Opus 4.8 and Fugu Ultra (a multi-model orchestrator) building the same alien-biome procedural scene in Blender via Claude Code in VS Code with a shared prompt MD file. Opus finished in ~17 min for ~$18.30 with 4 errors; Fugu took ~34 min, was canceled after repeated render failures at $30, with 36 errors and duplicated instead of instanced objects. Single test, author's opinion favors Opus. No Roblox pipeline content.

## Claims
- c1: [0:46] Fugu is an orchestrator (OpenRouter-like) routing tasks across connected providers (Claude, GPT, Gemini); it is not a model itself, per the video. *(demo, medium; claude-blender-ai)*
- c2: [8:15] Opus 4.8 run: ~17 min build time, ~$18.30 cost, 97 geometry nodes, 4 errors, 5,840 true geometry node instances. *(demo, medium; claude-blender-ai)*
- c3: [8:15] Fugu Ultra run: ~33.6 min before cancel, ~$30 credit spent, 28 geometry nodes, 36 errors, 354 scatter instances (554 reported, 552 real mesh objects, duplicated not instanced). *(demo, medium; claude-blender-ai)*
- c4: [9:38] Fugu repeatedly failed to render a single image in Blender and was canceled; author suspects Opus's computer-use ability gives better Blender UI understanding. *(demo, medium; claude-blender-ai)*
- c5: [4:46] Single prompt-MD file (alien biome brief) drove Claude Code in VS Code to build geometry-nodes terrain, materials, lighting, atmosphere, camera and hero element in Blender; output rendered acceptably. *(demo, medium; claude-blender-ai)*
- c6: [6:24] Fugu output had misblended grass/rock materials, downward-pointing light and misaligned fog; rendered via Cycles with GPU compute, but less detailed than Opus. *(demo, medium; claude-blender-ai)*
- c7: [10:08] Author's scoring: Opus 37/40, Fugu 26/40 on a basic procedural scene; recommends staying with Opus 4.8 for Blender work (opinion, single test). *(opinion, low; claude-blender-ai)*
- c8: [7:48] Author recommends using AI as an assistant rather than fully generating scenes, animations and workflows (opinion). *(opinion, low; claude-blender-ai)*
- c9: [10:42] Fugu outperformed Opus in some HTML/3D web visualization examples shared on X (black hole visual), but not in Blender; author's claim from others' posts. *(opinion, low; claude-blender-ai)*
- c10: [3:07] Test workflow: put the same brief MD file into each Claude Code session (Opus 4.8 1M context vs Fugu Ultra 1M), with an empty Blender scene connected, then compare time, cost, tokens and errors. *(demo, medium; automation-and-creator-workflows)*

## Numbers
- n1: **Opus build time / cost**: ~17 min / ~$18.30 
- n2: **Fugu build time / cost**: ~33.6 min (canceled) / ~$30 
- n3: **Geometry nodes Opus vs Fugu**: 97 vs 28 
- n4: **Errors Opus vs Fugu**: 4 vs 36 
- n5: **Scatter instances Opus vs Fugu**: 5,840 true instances vs 354 (554 reported, 552 real meshes) 
- n6: **Author score**: Opus 37/40, Fugu 26/40 

## Techniques
- t1: **Single-prompt MD brief for scene build**: Write a markdown brief (style, geometry nodes, procedural terrain, materials, lighting, atmosphere, camera, hero object). Paste its path into Claude Code connected to Blender; let agent build the scene.
- t2: **Render check via Cycles GPU compute**: After agent output, set Cycles and GPU compute in Blender, select camera, render to verify. Fugu failed this step repeatedly.

## Quotes (brief, for attribution)
> It could not figure out how to render out an image inside of Blender inside of Fugu.  (at 9:38, Aidan Stanik)
> Fugu shows 554 instances, but 552 real mesh objects. It duplicated objects rather than instancing.  (at 9:38, Aidan Stanik)

## Contradictions flagged
- Fugu is a model that beats Opus on benchmarks (vs Video's own Blender test where Fugu scored lower; author notes benchmark claims are from the vendor chart)

## Points to
- Sakana Fugu
- OpenRouter (comparison)
- Claude Code in VS Code
- Blender Cycles
