---
type: research-source
id: gh-sandraschi-blender-mcp-rel-v0.11.0
title: "sandraschi/blender-mcp v0.11.0: v0.11.0"
source_type: "github"
creator: "sandraschi"
url: "https://github.com/sandraschi/blender-mcp/releases/tag/v0.11.0"
published: "2026-07-14"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0011
relevance: 3
density: medium
tags: ["research-source", "github", "claude-blender-mcp", "common-mistakes-fixes", "creator-workflows", "other"]
---
# gh-sandraschi-blender-mcp-rel-v0.11.0

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Release notes for sandraschi/blender-mcp v0.11.0 (dated 2026-07-14). Covers a TCP socket bridge addon replacing the HTTP poll bridge, remote Blender host env vars, tool annotations and docstrings on 68 MCP tools, UI/chat/skills pages, and CORS/build fixes. Nothing on Roblox export or import; relevant only to the Claude-drives-Blender side.

## Claims
- c1: v0.11.0 replaces the HTTP poll bridge with a bidirectional TCP socket bridge addon; API keys are set in Blender Addon Preferences. *(doc, high; claude-blender-mcp)*
- c2: BLENDER_HOST / BLENDER_BRIDGE_HOST env vars add remote Blender connection support. *(doc, high; claude-blender-mcp)*
- c3: All 68 MCP tools get SOTA docstring sections (Return Format, Examples) and READ_ONLY/MUTATING/DESTRUCTIVE annotations on @app.tool decorators. *(doc, high; claude-blender-mcp)*
- c4: Adds prefab UI cards show_blender_status_app, show_tools_app, show_logs_app and a chat page with localStorage persistence (100 msg cap), 4 personalities, export/clear buttons. *(doc, high; claude-blender-mcp)*
- c5: CORS allow_origin_regex is now unconditional, covering Tailscale/LAN/CGNAT, instead of gated on an env var. *(doc, high; other)*
- c6: build.ps1 gained API_BASE port verification, frozen binary smoke test and a >=5 MB size gate. *(doc, high; common-mistakes-fixes)*
- c7: Ships a /skills route and .opencode/skills/ directory for opencode agent awareness. *(doc, medium; creator-workflows)*

## Numbers
- n1: **MCP tools documented and annotated**: 68 All @app.tool decorators in v0.11.0
- n2: **Chat message cap**: 100 messages Chat page localStorage persistence
- n3: **Minimum frozen binary size gate**: 5 MB build.ps1 size check
- n4: **NSIS installer size**: 31.3 MB Blender MCP_0.1.0_x64-setup.exe artifact
- n5: **MCPB bundle size**: 58.7 MB blender-mcp-v0.1.0.mcpb artifact

## Techniques
- t1: **Tool annotation tagging**: Tag every @app.tool decorator with READ_ONLY, MUTATING or DESTRUCTIVE so clients can judge risk; add Return Format and Examples docstring sections.

## Contradictions flagged
- Release tag is v0.11.0 but installer and bundle artifacts are named 0.1.0. (vs Version naming in the same release)

## Points to
- https://github.com/sandraschi/blender-mcp/compare/v0.10.0...v0.11.0
