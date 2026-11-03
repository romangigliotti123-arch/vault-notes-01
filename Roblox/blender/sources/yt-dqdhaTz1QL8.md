---
type: research-source
id: yt-dqdhaTz1QL8
title: "How To Make The Backrooms In Blender + Claude + Seendance 2.5"
source_type: "youtube"
creator: "Aidan Stanik"
url: "https://www.youtube.com/watch?v=dqdhaTz1QL8"
published: "2026-09-01"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0023
relevance: 1
density: low
tags: ["research-source", "youtube", "claude-blender-mcp", "creator-workflows", "procedural-generation"]
---
# yt-dqdhaTz1QL8

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Video shows an AI-video previz workflow: Claude Code drives a live Blender session via the official Blender MCP connector and a downloadable skill .md, building a block-character walking scene from a reference image. Renders are then used as references for Seedance 2.5 (on Artlist) to make 30-second 1080p videos. No Roblox export, bpy scripting, or asset pipeline content.

## Claims
- c1: [2:29] Workflow runs Claude Code (desktop app) in bypass-permissions mode inside a Blender project folder, with a custom skill .md uploaded via Claude settings. *(demo, medium; claude-blender-mcp)*
- c2: [3:24] Blender is connected to Claude via the official Blender connector; check connected tools with /mcp and search for Blender. *(demo, medium; claude-blender-mcp)*
- c3: [3:24] Claude builds the scene directly in the open Blender viewport session; user starts with a fresh scene and deletes defaults first. *(demo, medium; claude-blender-mcp)*
- c4: [4:07] A simple prompt (block character walking through backrooms open space, continuous camera motion) plus one reference image produced a Blender previz that is rendered out and used as the camera-motion reference. *(demo, medium; claude-blender-mcp)*
- c5: [4:48] Author's opinion: Blender-to-video workflow gives better camera control than prompt-only AI video generation. *(opinion, low; procedural-generation)*
- c6: [5:38] Character sheet and scene reference boards are generated from Claude-written prompts using ChatGPT image generation; Higgsfield MCP optional. *(demo, medium; creator-workflows)*
- c7: [7:05] Seedance input is image 1 (character board), image 2 (scene board), video 1 (Blender previz render); each must be tagged in the prompt and toggled in Artlist. *(demo, medium; creator-workflows)*
- c8: [8:17] Artlist generation settings used: 1080p, auto duration, 16:9 ratio; source states 30-second outputs. *(demo, high; creator-workflows)*
- c9: [8:43] Result: camera motion matched the previz closely, but arms and face proportions were off and needed iteration. *(demo, medium; creator-workflows)*

## Numbers
- n1: **output length and resolution**: 30 s, 1080p (Seedance 2.5 via Artlist) 
- n2: **aspect ratio**: 16:9 
- n3: **model used by author**: 'Fable 5 or Opus 5' (as stated) 

## Techniques
- t1: **Claude-driven Blender previz**: Open a fresh Blender scene, clear defaults, connect Blender MCP, invoke skill with a scene prompt plus reference image, let Claude build camera and blocking, render previz video.
- t2: **Multi-reference video generation**: Tag character board (image 1), scene board (image 2) and previz render (video 1) in the Seedance prompt; enable each reference in the UI before generating.

## Quotes (brief, for attribution)
> the Blender to C Dance workflow is better cuz you have better camera control and control over your scene.  (at 4:48, Aidan Stanik)

## Points to
- Official Blender connector (MCP)
- Artlist.io (Seedance 2.5 access)
- ChatGPT image generation
- Higgsfield MCP
- Creative AI Network (author's community)

## Visual notes
Contact sheet shows Blender viewport with a previz of a block figure in a corridor, Claude Code terminal with skill output, and Artlist UI with image/video reference slots and Seedance settings.
