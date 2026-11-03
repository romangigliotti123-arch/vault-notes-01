---
type: research-source
id: yt-8MUk-tQTiwE
title: "New Absolute King of 3D & Blender - GPT-6 Astra"
source_type: "youtube"
creator: "Stefan 3D AI"
url: "https://www.youtube.com/watch?v=8MUk-tQTiwE"
published: "2026-09-07"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0021
relevance: 1
density: low
tags: ["research-source", "youtube", "bpy-scripting-headless", "claude-blender-mcp", "creator-workflows", "procedural-generation"]
---
# yt-8MUk-tQTiwE

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Promotional video claiming GPT-6 "Astra" (via Codex CLI) drives Blender for rigging, procedural scene building, car modelling, playblast-to-video and a LED-soffit addon. Almost no Roblox content. Useful only as a note that computer-use is slow versus scripted MCP control, and that Higgsfield offers a Blender MCP plugin. Claims are unverified demos.

## Claims
- c1: [2:04] Author says computer-use (GUI clicking) Blender control was very slow; a test file save took about 10 minutes, versus MCP exposing engine functions which he says is much faster. *(demo, low; claude-blender-mcp)*
- c2: [2:04] Uses Higgsfield Blender MCP plugin with Codex CLI; author says it is free to use as an MCP, while 3D/video generation needs a Higgsfield account. *(opinion, low; claude-blender-mcp)*
- c3: [4:36] Agent built a multi-object scene from one prompt by blocking first then adding detail; flames and backgrounds procedurally generated, per author. *(demo, low; procedural-generation)*
- c4: [6:45] Author says full scene made from primitives totals about 140 triangles (~70K faces as he states); the two figures are inconsistent. *(demo, low; procedural-generation)*
- c5: [8:32] Author reports more than 10 tests consumed only about 7% of weekly Max plan limits, cheaper than Fable 5.1 per his view. *(experience, low; creator-workflows)*
- c6: [9:23] Workflow: agent builds dynamic race scene, exports a Blender playblast, then feeds it to a video model (Seedance-style 2.5) for final render; author says ~95% AI-made. *(demo, low; creator-workflows)*
- c7: [11:46] Agent produced a Blender addon for an LED soffit configurator with presets, logo upload and connector calculation; author did not check all parameters. *(demo, low; bpy-scripting-headless)*
- c8: [3:26] Author says building characters from primitives does not work well yet and recommends 3D AI generation for organic meshes. *(opinion, medium; procedural-generation)*

## Numbers
- n1: **file save duration via computer-use**: ~10 minutes 
- n2: **scene triangle count**: 140 triangles (also stated ~70K faces) 
- n3: **weekly limit used for 10+ tests**: 7% 
- n4: **reference-rebuild duration**: about one hour 

## Techniques
- t1: **Playblast-to-video**: Have agent block a scene in Blender, export playblast, then pass playblast as input to an AI video model for stylised final render.
- t2: **MCP over computer use**: Expose engine functions via MCP tools instead of having the agent click the GUI; author claims far faster results.

## Quotes (brief, for attribution)
> if you provide it with MCPs that expose all the engine functionality, it will do way more than that  (at 2:04, Stefan 3D AI)

## Contradictions flagged
- Scene is 140 triangles (vs Same video says ~70K faces)

## Points to
- Higgsfield Blender MCP plugin
- Codex CLI
- Higgsfield CLI
