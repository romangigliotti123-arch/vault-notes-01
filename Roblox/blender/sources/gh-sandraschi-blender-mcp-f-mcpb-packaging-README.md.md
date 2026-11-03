---
type: research-source
id: gh-sandraschi-blender-mcp-f-mcpb-packaging-README.md
title: "sandraschi/blender-mcp/mcpb-packaging/README.md"
source_type: "github"
creator: "sandraschi"
url: "https://github.com/sandraschi/blender-mcp/blob/HEAD/mcpb-packaging/README.md"
published: "2026-10-25"
retrieved: 2026-11-01
extracted_by: "sonnet"
extraction_cost_usd: 0.0383
relevance: 2
density: low
tags: ["research-source", "github", "automation-and-creator-workflows", "blender-roblox-export-import", "claude-blender-ai", "mesh-texture-limits", "rigging-animation"]
---
# gh-sandraschi-blender-mcp-f-mcpb-packaging-README.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
README for an MCPB packaging of sandraschi's blender-mcp server (FastMCP 2.12) for one-click Claude Desktop install. Lists tool categories (mesh, rigging, UV, export, import, etc.), build/validate scripts, and config. Export targets are Unity and VRChat only; no Roblox-specific guidance, limits, or settings. Tool counts are inconsistent (50 vs 37).

## Claims
- c1: Package bundles a Blender MCP server built on FastMCP 2.12, installable in Claude Desktop by dragging a .mcpb file and then setting the Blender path. *(doc, medium; claude-blender-ai)*
- c2: Requirements: Node.js with @anthropic-ai/mcpb CLI, Python 3.10+, Blender 4.0+. *(doc, high; claude-blender-ai)*
- c3: blender_export covers only Unity and VRChat pipelines (2 operations); no Roblox export preset. blender_import supports FBX, OBJ, glTF, VRM. *(doc, high; blender-roblox-export-import)*
- c4: blender_rigging offers 4 operations for armature creation and bone manipulation; blender_animation has 7 (keyframes, motion paths, playback). No R15/Motor6D support is mentioned. *(doc, high; rigging-animation)*
- c5: blender_uv offers 4 operations (unwrap/mapping); blender_textures 3 (procedural and image-based). No baking, triangle-limit or PBR export tooling is listed. *(doc, medium; mesh-texture-limits)*
- c6: Doc is internally inconsistent: says 50 tools across 19 categories, but the section header says 37 tools and lists 16 categories. *(doc, high; claude-blender-ai)*
- c7: Security claims: scripts run in a controlled environment, file access limited to specified directories, network disabled by default, subprocess limited to Blender. Not verified in the doc. *(doc, low; claude-blender-ai)*
- c8: Config options include Blender executable path (auto-detect or manual), timeout, parallel ops, GPU rendering, temp/log/backup dirs, and log level via BLENDER_MCP_LOG_LEVEL. *(doc, medium; automation-and-creator-workflows)*

## Numbers
- n1: **claimed tool count**: 50 tools / 19 categories (header lists 37) README inconsistency
- n2: **FastMCP version**: 2.12 implementation framework
- n3: **minimum Blender version**: 4.0+ prerequisite
- n4: **minimum Python**: 3.10+ prerequisite

## Techniques
- t1: **Install blender-mcp as MCPB**: Install npm @anthropic-ai/mcpb, run build-mcpb-package.ps1, validate with validate-mcpb-package.ps1 -Detailed, drag dist\blender-mcp.mcpb into Claude Desktop, set Blender path.
- t2: **Manual run without bundle**: mcpb extract blender-mcp.mcpb --output install-dir; cd install-dir; pip install -r requirements.txt; python -m blender_mcp.

### Code: Manual install and run of the MCP server
```powershell
mcpb extract blender-mcp.mcpb --output install-dir
cd install-dir
python -m pip install -r requirements.txt
python -m blender_mcp
```

## Contradictions flagged
- Claims 50 tools across 19 categories but section header says 37 tools with 16 listed categories (vs itself)

## Points to
- @anthropic-ai/mcpb
- FastMCP 2.12 (fastmcp.com)
- Blender Python API docs
- modelcontextprotocol.io
