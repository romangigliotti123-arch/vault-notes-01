---
type: research-source
id: yt-C0UgGAoIpIg
title: "Connect Claude MCP Opus 5.5 With Roblox Studio - AI Makes a Working Hourglass in 2 Minutes"
source_type: "youtube"
creator: "MrWonderHow"
url: "https://www.youtube.com/watch?v=C0UgGAoIpIg"
published: "2026-10-24"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0010
relevance: 1
density: low
tags: ["research-source", "youtube", "claude-blender-ai", "other"]
---
# yt-C0UgGAoIpIg

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Video on connecting Claude (Desktop and Claude Code CLI) to Roblox Studio via an MCP server, then prompting Claude to build and test a working sand hourglass. It does not cover Blender, bpy, blender-mcp, or the Blender-to-Roblox export pipeline. Only the MCP setup path for Roblox Studio is relevant, as an analogy.

## Claims
- c1: [0:42] Roblox Studio assistant settings have an MCP servers tab listing connections; Claude Desktop and Claude Code CLI appear as instances, disabled until Claude is running. *(demo, medium; claude-blender-ai)*
- c2: [1:22] Once Claude is running, the MCP connection shows a green indicator with two connected clients. *(demo, medium; claude-blender-ai)*
- c3: [2:03] Claude built a sand hourglass in Roblox Studio (frame, glass bulbs, sand, falling stream, timer) and wrote the controlling script in about 2 minutes from one prompt. *(demo, low; other)*
- c4: [2:03] Claude started the game to test flow and flipping, checked output for errors, stopped the game, and took a screenshot to inspect the result. *(demo, medium; claude-blender-ai)*

## Numbers
- n1: **build-and-test time**: about 2 minutes 

## Techniques
- t1: **Self-test loop via MCP in Studio**: Prompt the agent to build the scene, run play mode, check output for errors, flip-test interactions, stop play, and capture a screenshot to verify.

## Points to
- Roblox Studio assistant (Galaxy icon, top right)
- Claude Desktop
- Claude Code CLI
