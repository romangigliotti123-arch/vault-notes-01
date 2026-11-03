---
type: research-source
id: yt-G5j0fBOa8f0
title: "I Tested Claude's Ultracode Mode in Blender"
source_type: "youtube"
creator: "Aidan Stanik"
url: "https://www.youtube.com/watch?v=G5j0fBOa8f0"
published: "2026-06-04"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0018
relevance: 2
density: low
tags: ["research-source", "youtube", "claude-blender-mcp", "creator-workflows"]
---
# yt-G5j0fBOa8f0

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Video demo of Claude Code "Ultracode" effort mode (X-high reasoning plus automatic sub-agent orchestration) driving the official Blender MCP to animate a Blender Studio rigged character singing with a mic on a stage, camera depth of field. Nothing on Roblox export/import. Useful only as a claude-blender-mcp workflow example; no bpy or Roblox specifics.

## Claims
- c1: [0:20] Ultracode is described as X-high reasoning effort with automatic workflow orchestration; Claude decides when to spin up sub-agents. Uses more tokens; creator recommends Max plan. *(doc, medium; claude-blender-mcp)*
- c2: [1:01] Simple prompt to animate rigged character singing with mic on stage produced output in about 2 minutes via parallel sub-agents (stage, face, hand pose, mic). *(demo, medium; claude-blender-mcp)*
- c3: [3:00] Creator runs claude with --dangerously-skip-permissions to avoid accept-edits prompts; advises against use with private/work data. *(opinion, medium; claude-blender-mcp)*
- c4: [4:07] Ultracode is selected via /effort menu in Claude Code (levels: low, medium, high, xhigh, max, ultracode). *(demo, high; claude-blender-mcp)*
- c5: [4:49] Check connected servers with /mcp; Blender MCP from blender.com connects to Claude Code and exposes many tools to control Blender. *(demo, medium; claude-blender-mcp)*
- c6: [6:11] Claude attaches to an already-open Blender session with the MCP connected and builds scene inside it. *(demo, medium; claude-blender-mcp)*
- c7: [7:28] Claude first queries scene contents, measures rig height and control bone world positions (head, jaw, mouth, brows), and verifies control names before building. *(demo, medium; claude-blender-mcp)*
- c8: [8:15] Creator judges the output as looking bad; lighting/stage quality needs manual revision. Opinion. *(opinion, high; creator-workflows)*

## Numbers
- n1: **generation time**: about 2 minutes 
- n2: **sub-agents spawned initially**: 5 listed, plus 3 more planned 
- n3: **effort levels in /effort menu**: low, medium, high, xhigh, max, ultracode 

## Techniques
- t1: **Ultracode via /effort**: Run claude in VS Code terminal, type /effort, select ultracode. Claude then orchestrates sub-agents per task. Check connection with /mcp first.
- t2: **Single-prompt scene build in open Blender session**: Open Blender Studio .blend with rig, then give one prompt describing mic, camera, mouth/face animation, sway, stage lights and depth of field. Claude splits work across agents.

## Quotes (brief, for attribution)
> Claude decides when a task warrants a workflow.  (at 0:20, Aidan Stanik)
> we have X high, and then ... we have max ... and then we have Ultra code.  (at 4:07, Aidan Stanik)

## Points to
- Blender Studio (rigged character asset, Storm V1)
- Official Blender MCP (blender.com)
- Claude Code VS Code extension
- Anthropic docs on Ultracode
