---
type: research-source
id: gh-sandraschi-blender-mcp-f-docs-MCP_PRODUCTION_CHECKLIST.md
title: "sandraschi/blender-mcp/docs/MCP_PRODUCTION_CHECKLIST.md"
source_type: "github"
creator: "sandraschi"
url: "https://github.com/sandraschi/blender-mcp/blob/HEAD/docs/MCP_PRODUCTION_CHECKLIST.md"
published: "2026-10-25"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0017
relevance: 1
density: low
tags: ["research-source", "github", "automation-and-creator-workflows", "claude-blender-ai", "other"]
---
# gh-sandraschi-blender-mcp-f-docs-MCP_PRODUCTION_CHECKLIST.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Generic production-audit checklist for MCP servers (FastMCP 2.12+, dual MCP + FastAPI interface, tools/ modular layout, mcpb validate/pack packaging, Windows PowerShell rules). Despite living in a blender-mcp repo, it contains no Blender, bpy, or Roblox content: no blender-mcp tool details, no FBX/glTF export settings, no Roblox import or mesh/rig rules. Little use for this topic.

## Claims
- c1: The document is a generic MCP server audit checklist with 95 items; it does not describe Blender, bpy scripting, or the Roblox asset pipeline. *(doc, high; other)*
- c2: Checklist requires FastMCP 2.12+ with a thin server.py (<150 lines) and tools organized by category under src/mcp/tools/. *(doc, high; automation-and-creator-workflows)*
- c3: For DXT/MCPB packaging, the checklist says to use only 'mcpb validate' and 'mcpb pack', and not 'mcpb init' or 'mcpb publish'. *(doc, high; automation-and-creator-workflows)*
- c4: Checklist sets a dual-interface rule: every MCP server must also expose a FastAPI interface with /api/docs and /health endpoints. Blender-specific tools are not discussed. *(doc, medium; claude-blender-ai)*

## Numbers
- n1: **checklist items**: 95 total 
- n2: **server.py max lines**: <150 
- n3: **FastMCP minimum version**: 2.12+ 
- n4: **test coverage target**: >80% 

## Points to
- https://github.com/sandraschi/blender-mcp/blob/HEAD/docs/MCP_PRODUCTION_CHECKLIST.md
