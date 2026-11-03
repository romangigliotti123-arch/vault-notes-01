---
type: research-source
id: yt-6flxMjhaX0E
title: "I Tested Claude Opus 5 In Blender"
source_type: "youtube"
creator: "Aidan Stanik"
url: "https://www.youtube.com/watch?v=6flxMjhaX0E"
published: "2026-07-25"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0031
relevance: 2
density: medium
tags: ["research-source", "youtube", "bpy-scripting-headless", "claude-blender-mcp", "creator-workflows", "other", "procedural-generation"]
---
# yt-6flxMjhaX0E

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Video demo of Claude Opus 5 driving Blender, with a walkthrough of the official Blender MCP setup (blender.org/lab/mcp server, Blender 5.1+, Claude Desktop connector). Three one-prompt builds (sci-fi corridor, liquid product shot, eroded canyon) with timings. Does not mention Roblox, Studio, or any export pipeline.

## Claims
- c1: [10:15] Official Blender MCP server requires Blender 5.1 or newer; installed as add-on by adding it to Blender once, then installing it on a second pass. *(demo, medium; claude-blender-mcp)*
- c2: [10:56] Connect via Claude Desktop: Customize > Connectors > Browse connectors > search Blender > install and authorize. Verify with /mcp in chat. *(demo, medium; claude-blender-mcp)*
- c3: [11:37] Blender connector was installed globally, so it is available in all Claude sessions; Claude Code in VS Code also verifies via /mcp. *(demo, medium; claude-blender-mcp)*
- c4: [1:52] One-shot sci-fi corridor (modular geometry-node panels, Boolean hard surface, procedural materials built in Python) took about 25 minutes; author says Opus 4.8 would take about 5 minutes. *(experience, low; procedural-generation)*
- c5: [5:01] Liquid product shot from one prompt used Mantaflow liquid and rigid-body cell fracture with cached/baked simulation; took 40-45 minutes of thinking and about 15% of context. *(experience, low; bpy-scripting-headless)*
- c6: [8:13] Grand Canyon attempt with geometry nodes and multi-layer displacement looked video-game-like; author was not happy with realism. Author removed generated camera animation, disliking Claude's camera animation. *(opinion, low; procedural-generation)*
- c7: [0:36] Vendor-reported benchmarks cited: computer use 70.6% for Opus 5 vs 55.7% for Opus 4.8; agentic terminal coding 43.2% vs 21.0%; agentic search 90.8% vs 84%. *(doc, medium; other)*
- c8: [5:43] Author says Opus 5 costs half as much as Fable 5 (opinion, no figures given). *(opinion, low; creator-workflows)*
- c9: [2:32] Author reports Claude-generated materials and lighting were clunky; output is usable as background VFX but not professional quality. *(opinion, medium; claude-blender-mcp)*
- c10: [3:03] Scene prompts were short descriptive briefs (structure, lighting, camera, FX terms) with no reference images; author stresses prompt structure as the approach. *(demo, medium; creator-workflows)*

## Numbers
- n1: **Minimum Blender version**: 5.1 or newer 
- n2: **Corridor build time, Opus 5 vs 4.8**: ~25 min vs ~5 min (author estimate) 
- n3: **Liquid scene thinking time**: 40-45 min 
- n4: **Context used for liquid scene**: ~15% 
- n5: **Computer use score Opus 5 vs 4.8**: 70.6% vs 55.7% 
- n6: **Community size (promo, not technical)**: 1.6 thousand members 

## Techniques
- t1: **Official Blender MCP install**: Get official add-on from blender.org/lab/mcp server; in Blender add-ons, install the file (two passes per video), allow prompts, confirm in Preferences > Add-ons by searching MCP and noting file path.
- t2: **Claude Desktop connector link**: Claude Desktop > Customize > Connectors > Browse connectors > Blender > Install > authorize; then type /mcp to confirm link.
- t3: **Prompt-built procedural materials**: Ask Claude to build the node tree in Python; specify wear from pointiness and curvature masks, volume scatter, Cycles denoise, compositing.
- t4: **One-prompt simulation brief**: Describe subject, liquid pour/pool, rigid-body shatter timing, studio 3-point lighting, DOF, motion blur, IOR; Claude sets up and caches the sim.

## Quotes (brief, for attribution)
> This is not from GitHub. It's like it is the official one that Blender has provided for Claude.  (at 9:35, Aidan Stanik)

## Contradictions flagged
- Opus 5 scene builds are 'super accurate' and one-shot ready (vs Author's own critique: materials clunky, lighting off, canyon looks fake, camera animation removed)

## Points to
- blender.org/lab/mcp server
- Claude Desktop connectors
- Creative AI Network (community, promo)

## Visual notes
Frame shows blender.org MCP page with Add-on, LLM Client, MCP Server sections and a Blender preferences add-on search; Claude Desktop connector/MCP list visible. Other frames are rendered Blender scenes (corridor, liquid, canyon) and a Claude chat with MCP servers panel.
