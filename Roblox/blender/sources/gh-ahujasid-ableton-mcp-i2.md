---
type: research-source
id: gh-ahujasid-ableton-mcp-i2
title: "ahujasid/ableton-mcp#2 Targeting other DAWS?"
source_type: "github"
creator: "ahujasid"
url: "https://github.com/ahujasid/ableton-mcp/issues/2"
published: "2025-03-20"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0007
relevance: 0
density: low
tags: ["research-source", "github", "claude-blender-ai"]
---
# gh-ahujasid-ableton-mcp-i2

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
GitHub issue on ahujasid/ableton-mcp asking about porting the MCP approach to other DAWs (LMMS, Reaper, Bitwig). Describes the architecture: an Ableton Python Remote Script runs a socket server, and a separate MCP server (server.py) connects Claude to it. Not about Blender, Roblox, or bpy. Low relevance.

## Claims
- c1: Source is about ableton-mcp for DAWs, not blender-mcp or bpy; no Blender or Roblox content. *(doc, high; claude-blender-ai)*
- c2: ableton-mcp pattern: in-app Python Remote Script runs a socket server, separate MCP server (server.py) bridges Claude to it. Blender analogue would need a similar add-on, unverified here. *(doc, medium; claude-blender-ai)*

## Techniques
- t1: **Socket-bridge MCP architecture**: Host app runs an in-app script exposing a socket server. A separate MCP server translates model tool calls into socket commands. Ableton uses a Python MIDI Remote Script; Bitwig would use a Java Controller Extension.

## Points to
- https://github.com/ahujasid/ableton-mcp/issues/2
