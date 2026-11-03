---
type: research-source
id: gh-ahujasid-godot-ai-plugin-f-Spec.md
title: "ahujasid/godot-ai-plugin/Spec.md"
source_type: "github"
creator: "ahujasid"
url: "https://github.com/ahujasid/godot-ai-plugin/blob/HEAD/Spec.md"
published: "2025-05-16"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0007
relevance: 1
density: low
tags: ["research-source", "github", "claude-blender-ai", "other"]
---
# gh-ahujasid-godot-ai-plugin-f-Spec.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Spec for a minimal Godot 4 editor plugin (ahujasid/godot-ai-plugin) that routes a chat panel through the Claude 3.7 API to create scenes and simple gameplay scripts. It covers no Blender, bpy, blender-mcp, or Roblox content. Only the general idea of an AI chat driving an editor via an EditorPlugin is relevant.

## Claims
- c1: Source is a Godot-focused plugin spec; it does not cover Blender, bpy, blender-mcp, or the Blender-to-Roblox pipeline. *(doc, high; other)*
- c2: Proposed architecture: EditorPlugin hosting a dockable chat panel that sends requests to Claude 3.7 API and executes resulting editor operations. Pattern is analogous to a Blender MCP-style setup but for Godot. *(doc, low; claude-blender-ai)*

## Numbers
- n1: **Claude model version named in spec**: Claude 3.7 API 

## Techniques
- t1: **Chat-to-editor command plugin**: Create plugin dir and config, implement EditorPlugin script, add dockable chat panel, connect to Claude API, manage conversation context, translate intents into scene-tree and script operations.

## Points to
- https://github.com/ahujasid/godot-ai-plugin
