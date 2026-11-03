---
type: research-source
id: yt-iHckdjtnseA
title: "I Tested Claude Opus 5.5 In Blender"
source_type: "youtube"
creator: "Aidan Stanik"
url: "https://www.youtube.com/watch?v=iHckdjtnseA"
published: "2026-09-24"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0022
relevance: 1
density: low
tags: ["research-source", "youtube", "claude-blender-mcp", "creator-workflows", "other"]
---
# yt-iHckdjtnseA

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Creator's test of Claude Opus 5.5 driving a live Blender viewport via a Claude session, building a cathedral from a reference image. Covers token and dollar cost per build, agent-team cost scaling, and a Blender-previz-to-Seedance video pipeline using an Artlist MCP connector. No Roblox content, export steps, or bpy code.

## Claims
- c1: [0:00] Opus 5.5 was prompted in natural language to build a reference-image cathedral in the open Blender viewport connected to the Claude session. *(demo, high; claude-blender-mcp)*
- c2: [3:30] A full cathedral build with Opus 5.5 used about 2.7 million tokens. *(experience, medium; creator-workflows)*
- c3: [4:12] Creator's estimate: basic blockout build costs about $5-8; more detail about $10-20; agent-team 10-round build about $32-40. Author says these are estimates on a subscription plan. *(experience, low; creator-workflows)*
- c4: [2:16] Author says Opus 5.5 is cheaper than Opus 5 per build; no pricing found for Fable 5.1 in the doc. Opinion-level comparison. *(opinion, low; creator-workflows)*
- c5: [4:38] Creator's Blender previz pipeline: low-poly Blender render fed to Seedance 2.5 to generate textures, materials and realistic detail. *(experience, medium; other)*
- c6: [8:23] Artlist MCP connector (artlist.io/mcp) lets Claude generate Seedance 2.5 video directly from the chat via OAuth sign-in and a Claude-connected account. *(demo, medium; other)*
- c7: [9:48] Final Seedance render via Artlist MCP cost about $1.75-2 (about $2.79 total); creator says comparable flagship-model workflow ~ $6 and took 5-7 minutes vs ~10 minutes for Blender render plus upload. *(experience, low; creator-workflows)*
- c8: [1:35] Creator describes agentic coding as Claude writing scripts for Blender, and computer use as Claude interacting with the Blender interface; no setup steps given. *(opinion, medium; claude-blender-mcp)*

## Numbers
- n1: **tokens per cathedral build (Opus 5.5)**: ~2.7M 
- n2: **estimated cost, basic blockout build**: $5-8 
- n3: **estimated cost, agent-team ~10 iteration rounds**: $32-40 
- n4: **Seedance 2.5 Artlist MCP video cost**: ~$1.75-2 (total ~$2.79) 
- n5: **time, Artlist workflow vs Blender render+upload**: 5-7 min vs ~10 min 

## Techniques
- t1: **Single-prompt scene build in live Blender**: Connect Blender viewport to Claude session; upload reference image; send short natural-language prompt asking for the scene to be built as closely as possible. Creator states scene uses geometry nodes and procedural building.
- t2: **Director-agent multi-model setup**: Top model (Opus) acts as project manager; sub-agents handle scripting, world building, lights, rendering. Creator's setup is in a paid/free resource link, not shown.
- t3: **Previz-to-video skill**: Generate low-poly Blender previz with a skill, then use Seedance 2.5 to add textures and realism; skill also generates character/environment sheets and master prompts.

## Quotes (brief, for attribution)
> Can you build this cathedral from the reference image as closely as possible in the open Blender viewport which is connected to my Claude session.  (at 0:00, Aidan Stanik)
> it's saying what we have now costed 32 40 dollars with about 10 rounds of iteration.  (at 4:12, Aidan Stanik)

## Points to
- artlist.io/mcp
- Seedance 2.5
- GPT image 2
- Creative AI Network (community)
