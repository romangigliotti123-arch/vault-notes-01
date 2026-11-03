---
type: research-source
id: yt-GHAsbxulH8c
title: "How Much Does It ACTUALLY Cost To Build 3D Scenes With AI (GPT-6 Astra + Blender)"
source_type: "youtube"
creator: "Aidan Stanik"
url: "https://www.youtube.com/watch?v=GHAsbxulH8c"
published: "2026-09-18"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0023
relevance: 1
density: low
tags: ["research-source", "youtube", "claude-blender-mcp", "creator-workflows"]
---
# yt-GHAsbxulH8c

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Creator video comparing token, context and API-equivalent cost of three one-shot AI-driven Blender scene builds (GPT-6 Astra, high effort). Covers cost figures, a single-chat context problem, and an agent-team advice list (lower-cost models for repetitive checks and renders). No Roblox export, import or mesh content. Promotes a free skill; ignored.

## Claims
- c1: [1:59] Simple house scene build from a reference image used about 3.9M tokens, about $6 API-equivalent, and about 2% of weekly Pro-plan usage. *(demo, medium; claude-blender-mcp)*
- c2: [3:44] Vegetation-heavy portal scene used 3.81M tokens yet cost more than the house build (transcribed as $612, likely $6.12 or $61.2), because many distinct leaf objects were customised. *(demo, low; claude-blender-mcp)*
- c3: [4:25] Two one-shot scene builds consumed about 4% of weekly usage (98% to 96% remaining) with no iterations. *(demo, medium; claude-blender-mcp)*
- c4: [6:08] Night alley bike-shop scene with four reference images used about 7M tokens, about $10.41 API-equivalent (transcribed as $1041), and took 11.5 minutes. *(demo, medium; claude-blender-mcp)*
- c5: [6:33] Across three builds: about 15M tokens, about $23 API cost, about 73 minutes of creator time total. *(demo, medium; creator-workflows)*
- c6: [7:13] Advice: keep one focus task per scene in one chat; split research into a separate chat using a cheaper model. *(opinion, medium; creator-workflows)*
- c7: [7:53] Advice: use scripts for repetitive checks (render status, logs, errors) rather than the expensive model. *(opinion, medium; creator-workflows)*
- c8: [8:19] Agent-team pattern: a top-tier model acts as project manager, lower-tier sub-agents run simple tasks such as rendering and camera checks, reusing saved scripts and assets. *(opinion, medium; creator-workflows)*
- c9: [9:02] Reserve high-reasoning effort for hard decisions; request specific corrections and compact diagnostics to save context. *(opinion, medium; creator-workflows)*
- c10: [6:33] Creator opinion: good prompts and basic Blender knowledge are needed so the agent is not used to edit everything; manual iteration in Blender is cheaper. *(opinion, medium; creator-workflows)*

## Numbers
- n1: **tokens**: ~3.9M 
- n2: **API-equivalent cost**: ~$6 
- n3: **tokens**: 3.81M 
- n4: **tokens**: ~7M 
- n5: **API-equivalent cost**: ~$10.41 (transcribed $1041) 
- n6: **build time**: 11.5 min 
- n7: **total tokens / cost / time**: 15M / ~$23 / ~73 min 

## Techniques
- t1: **One focus task per chat**: Separate research, build and checks into different chats so context does not accumulate. Use a cheaper model for research before switching to the build chat.
- t2: **Agent team / sub-agents**: Top model directs; cheaper models handle render jobs and camera checks; scripts handle status and log polling; reuse saved scripts and assets.

## Quotes (brief, for attribution)
> Reserve high reasoning for difficult decisions which is like the project management side.  (at 7:13, Aidan Stanik)

## Contradictions flagged
- The second scene used fewer tokens (3.81M) than the first (~3.9M) but cost more in API-equivalent terms, so token count alone does not predict cost. (vs Implicit assumption that cost scales with tokens)
