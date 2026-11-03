---
type: research-source
id: yt-ZlXA6QwJrHM
title: "Next-gen workflows on Roblox"
source_type: "youtube"
creator: "Roblox Creators"
url: "https://www.youtube.com/watch?v=ZlXA6QwJrHM"
published: "2026-04-30"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0018
relevance: 1
density: low
tags: ["research-source", "youtube", "automation-and-creator-workflows", "other"]
---
# yt-ZlXA6QwJrHM

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox Creators talk on Studio AI features: procedural models (Lua function generating instances from parameters, edit-time), planning mode, and scene analysis with a Claude Code "scene health" command. It does not cover Blender, bpy, blender-mcp, or the FBX/glTF export pipeline. Only the Studio MCP-server note is tangentially related.

## Claims
- c1: [0:42] Procedural models wrap one Lua function that takes parameters and writes out instances; works at edit time in Studio. Not Blender-based. *(doc, high; other)*
- c2: [5:22] Studio exposes an MCP server; Cursor, Claude or other third-party AI tools connecting to it get the same plan/build/test functions as Roblox Assistant. *(doc, medium; automation-and-creator-workflows)*
- c3: [14:10] Scene analysis can be driven from Claude Code via a 'scene health' command that runs play mode and queries; this is Roblox-side, not Blender. *(demo, medium; automation-and-creator-workflows)*
- c4: [8:08] Presenter's opinion: use planning mode only for ambiguous or complex tasks, not simple edits like changing a part's color. *(opinion, medium; automation-and-creator-workflows)*

## Numbers
- n1: **audio memory on client**: about 8 MB 
- n2: **single freefall sound memory**: nearly 2 MB (~quarter of budget) 
- n3: **scene triangle count in demo project**: under 30,000 
- n4: **leaking module memory**: 350 KB 

## Quotes (brief, for attribution)
> either you are using cursor or cloud or any other third-party AI tools connecting to studio MCP server, you're going to get exactly the same functionalities.  (at 5:22, Roblox Creators)

## Points to
- Roblox Assistant
- Studio MCP server
- Cursor
- Claude Code
