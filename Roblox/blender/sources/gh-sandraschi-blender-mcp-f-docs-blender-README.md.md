---
type: research-source
id: gh-sandraschi-blender-mcp-f-docs-blender-README.md
title: "sandraschi/blender-mcp/docs/blender/README.md"
source_type: "github"
creator: "sandraschi"
url: "https://github.com/sandraschi/blender-mcp/blob/HEAD/docs/blender/README.md"
published: "2026-10-25"
retrieved: 2026-11-01
extracted_by: "sonnet"
extraction_cost_usd: 0.0261
relevance: 1
density: low
tags: ["research-source", "github", "automation-and-creator-workflows", "blender-roblox-export-import", "claude-blender-ai"]
---
# gh-sandraschi-blender-mcp-f-docs-blender-README.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Index README for sandraschi/blender-mcp docs: lists doc files (tool plan, tool reference, GUI mode, BlenderKit, free assets, asset repositories) and generic workflows. No Roblox content, no export settings, no bpy code. Only mentions 50+ tools in 19 categories and a blender_download(url) tool.

## Claims
- c1: sandraschi/blender-mcp documents 50+ working tools across 19 categories, with implementation status, operation mappings and known limitations in BLENDER_MCP_FUNCTIONALITY_PLAN.md. *(doc, medium; claude-blender-ai)*
- c2: The server supports a GUI mode (GUI_MODE.md) with interactive workflow setup, performance considerations and troubleshooting; details not given in this index. *(doc, low; claude-blender-ai)*
- c3: Recommended hybrid workflow: install BlenderKit add-on, download assets via its panel, then use MCP tools for scene composition, materials/lighting, animation/rigging, rendering and export. *(doc, medium; automation-and-creator-workflows)*
- c4: Free-asset workflow: copy download URLs from Poly Haven, AmbientCG etc., call blender_download(url=...), then manipulate with MCP tools. ASSET_REPOSITORIES.md covers Poly Haven and Kenney with API limitations. *(doc, medium; automation-and-creator-workflows)*
- c5: The index mentions export only generically (rendering and export); no Roblox, FBX, glTF, scale or axis guidance is present. *(doc, high; blender-roblox-export-import)*

## Numbers
- n1: **working MCP tools**: 50+ across 19 categories per functionality plan
- n2: **recommended free asset sites**: 7 FREE_ASSETS_GUIDE.md top recommended sites

## Techniques
- t1: **BlenderKit + Blender MCP hybrid**: Install BlenderKit add-on; browse/download assets in its panel; use MCP tools for composition, materials, lighting, animation/rigging, rendering, export.
- t2: **URL download via MCP**: Find asset on Poly Haven/AmbientCG, copy URL, call blender_download(url="https://..."), then edit with MCP tools.

### Code: MCP asset download tool call
```text
blender_download(url="https://...")
```

## Points to
- BlenderKit https://www.blenderkit.com/
- Poly Haven
- AmbientCG
- Kenney
- Blender Manual https://docs.blender.org/
