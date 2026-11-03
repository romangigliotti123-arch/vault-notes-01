---
type: research-source
id: yt-v8r1d80DxOY
title: "How to start coding with AI on Roblox (MCP)"
source_type: "youtube"
creator: "Roblox Creators"
url: "https://www.youtube.com/watch?v=v8r1d80DxOY"
published: "2026-06-11"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0011
relevance: 1
density: low
tags: ["research-source", "youtube", "automation-and-creator-workflows", "other"]
---
# yt-v8r1d80DxOY

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox Creators beginner video on AI coding for Roblox Studio, not Blender. It covers installing Cursor or VS Code, Roblox Studio, and Git, then enabling ScriptSync (beta) and Roblox Studio's built-in MCP server. Nothing on Blender, bpy, blender-mcp, or the Blender-to-Roblox asset pipeline.

## Claims
- c1: [1:45] ScriptSync is in beta and must be enabled first, then Studio rebooted; it is set up per folder via right-click on the project folder. *(doc, high; automation-and-creator-workflows)*
- c2: [1:45] Rojo is described as a more advanced file-based workflow; RBXLX save format is said to work with Rojo more easily. *(doc, medium; automation-and-creator-workflows)*
- c3: [2:31] Roblox Studio's built-in MCP server is enabled via the assistant window's manage MCP servers, with quick connect for the chosen text editor or a JSON snippet for other tools. *(doc, high; automation-and-creator-workflows)*
- c4: [0:13] Git is recommended as a safety net so an AI agent's changes can be reverted to a known good state with one command. *(opinion, medium; automation-and-creator-workflows)*
- c5: [0:13] Presenter personally prefers Cursor over VS Code because of built-in AI model support and easy Studio connection (opinion). *(opinion, low; other)*

## Techniques
- t1: **Verify MCP connection**: Prompt the AI agent to read the Studio game tree and list Workspace contents to confirm the MCP link works before building.
- t2: **Git checkpoint before building**: After setup works, make an initial Git commit so changes can be reverted with git restore or a previous commit.

## Points to
- Roblox Studio MCP server
- ScriptSync
- Rojo
- Git (git-scm.com)
- Cursor
- Visual Studio Code
