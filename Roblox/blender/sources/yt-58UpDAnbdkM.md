---
type: research-source
id: yt-58UpDAnbdkM
title: "New Local AI Turns Any Video Into Mixamo Animation"
source_type: "youtube"
creator: "Stefan 3D AI"
url: "https://www.youtube.com/watch?v=58UpDAnbdkM"
published: "2026-10-24"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0022
relevance: 1
density: low
tags: ["research-source", "youtube", "claude-blender-ai", "other", "rigging-animation"]
---
# yt-58UpDAnbdkM

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Overview of recent AI animation/3D tools: Motion2Mixamo (local video-to-Mixamo animation, needs LLM cleanup), Characuru (modular characters with spring bones), ActionForge (browser animation library), Asset Furnace (Mac auto-rig), Eden Live, PartLLM, GLOSS, DirtyMoCap, PAMI. Contains no Roblox export, bpy, or blender-mcp workflow; relevance to the Roblox pipeline is minimal.

## Claims
- c1: [0:00] Video is about Motion2Mixamo-style local video-to-animation and general AI character/animation tools; no Blender-to-Roblox export or bpy/blender-mcp workflow is actually shown. *(doc, high; claude-blender-ai)*
- c2: [5:43] Anthropic-engineer-built prompt system uses Claude (Opus) to generate Blender creatures: skeleton designed first, then anatomy, with a step-by-step guide that pins environment versions. *(doc, medium; claude-blender-ai)*
- c3: [7:59] ActionForge is a free browser-based Mixamo competitor with a large animation library, optional local folder sync, and prop attachment (sword, staff) for characters. *(doc, medium; rigging-animation)*
- c4: [4:57] Raw Motion2Mixamo output had leg sliding and root problems; author recommends a Claude or ChatGPT cleanup pass, which he says stabilized legs (opinion). *(experience, medium; rigging-animation)*
- c5: [13:23] Asset Furnace added auto-rigging and animation from images; it is mainly targeted at Mac and runs locally, with no Linux/Windows build yet. *(doc, medium; rigging-animation)*
- c6: [11:02] Eden Live is an open-source real-time generative video rendering engine by Vast AI, stated at 24 fps with 480p or 720p output on a single GPU. *(doc, medium; other)*
- c7: [3:07] Characuru generates modular characters with spring bones (e.g. dress bones) and previews their animation; it requires a Tripo account and runs as a local web page. *(demo, low; rigging-animation)*

## Numbers
- n1: **cost ratio**: Gemini 4 about 10x cheaper than Opus 5.5 (author's test) 
- n2: **frame rate**: 24 fps, 480p or 720p 
- n3: **quality**: raw Motion2Mixamo output not usable without cleanup (opinion) 

## Techniques
- t1: **LLM cleanup pass on mocap**: Generate motion locally with Motion2Mixamo from a reference video, then ask Claude or ChatGPT to refine foot sliding and root motion before retargeting.
- t2: **Retarget to custom skeleton via LLM**: Ask Claude or ChatGPT to convert the generated animation to a non-Mixamo skeleton.
- t3: **Run tool locally via coding agent**: Clone the repo and have ChatGPT Codex or Claude Code set up a local Python environment and server.

## Points to
- Motion2Mixamo
- Characuru
- ActionForge
- Asset Furnace
- Eden Live
- PartLLM
- GLOSS
- DirtyMoCap
- PAMI
- Tripo
