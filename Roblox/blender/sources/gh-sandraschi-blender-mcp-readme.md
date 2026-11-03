---
type: research-source
id: gh-sandraschi-blender-mcp-readme
title: "sandraschi/blender-mcp README: Headless Blender automation via FastMCP — 41 portmanteau tools (150+ ops). Batch mesh/VSE/Grease Pencil, VRM,"
source_type: "github"
creator: "sandraschi"
url: "https://github.com/sandraschi/blender-mcp"
published: "2026-10-25"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0025
relevance: 2
density: medium
tags: ["research-source", "github", "claude-blender-mcp", "common-mistakes-fixes", "other", "procedural-generation"]
---
# gh-sandraschi-blender-mcp-readme

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
README for sandraschi/blender-mcp, an MCP server that lets Claude drive Blender. Default mode runs headless Blender as a subprocess; an optional bridge addon gives a live viewport. Covers install (.mcpb, uvx, env BLENDER_EXECUTABLE), export formats, and generative mesh hooks. It never mentions Roblox, so it is only tangential to the Roblox pipeline topic.

## Claims
- c1: Default mode runs Blender headless via a 'blender --background' subprocess; suited to batch export, CI, and agents without a display. *(doc, high; claude-blender-mcp)*
- c2: Live viewport requires the optional blender_bridge_addon.py installed in Blender; skip it for headless use. *(doc, high; claude-blender-mcp)*
- c3: Per-tool override prefer_session=False forces headless execution even when the bridge is connected. *(doc, high; claude-blender-mcp)*
- c4: Install paths: Claude Desktop .mcpb bundle, a PowerShell one-liner running install.ps1, or manual MCP config using command uvx with args [blender-mcp] and env BLENDER_EXECUTABLE. *(doc, high; claude-blender-mcp)*
- c5: Blender is never bundled; the user installs it separately and points BLENDER_EXECUTABLE at the binary path. *(doc, high; claude-blender-mcp)*
- c6: README gives conflicting versions: title says 41 portmanteau tools (150+ ops), Features says 48+ MCP tools. *(doc, high; common-mistakes-fixes)*
- c7: Python version is inconsistent: badge says 3.13+, Requirements section says Python 3.12+ (only for clone-from-source options). *(doc, high; claude-blender-mcp)*
- c8: Stated minimum is Blender 3.0+, but the example config path points to Blender 4.4. *(doc, high; claude-blender-mcp)*
- c9: blender_export covers GLB, GLTF, FBX, OBJ, USD headless; VRM/VRChat avatar export has a validation pipeline; Unity is listed in features. *(doc, high; other)*
- c10: Generative hooks exist for Rodin, Tripo and Hunyuan mesh URLs via blender_ai_generate, plus vision-based refine; no quality or limits are documented. *(doc, medium; procedural-generation)*
- c11: Headless tools include VSE video rendering, geometry nodes, most mesh ops, and viewport PNG rendering; live-only items include screenshots and sculpt feedback. *(doc, high; claude-blender-mcp)*
- c12: The README contains no Roblox-specific guidance: no Roblox scale, axis, mesh or texture limits, or Studio import steps. *(doc, high; other)*
- c13: Optional companions (qcad-mcp, freecad-mcp, resonite-mcp, speech-mcp) are listed as independent add-ons; none is Roblox-related. *(doc, medium; claude-blender-mcp)*

## Numbers
- n1: **MCP tool count**: 41 portmanteau tools (150+ ops) in title; 48+ in Features Conflicting counts in same README
- n2: **Python requirement**: 3.13+ (badge) vs 3.12+ (Requirements) Clone-from-source only
- n3: **Blender minimum**: 3.0+ Example config uses Blender 4.4 path
- n4: **Tauri desktop installer size**: ~15 MB No Python required; built with just build-native
- n5: **Dashboard port**: http://localhost:10848 Optional webapp via start.ps1

## Techniques
- t1: **Headless-first with optional live bridge**: Install .mcpb or uvx config; set BLENDER_EXECUTABLE; the server spawns blender --background per call. Start blender_session plus the bridge addon only when a live viewport is wanted. Use prefer_session=False for batch jobs.

### Code: Manual MCP client config for blender-mcp via uvx, from README
```json
{
  "mcpServers": {
    "blender-mcp": {
      "command": "uvx",
      "args": ["blender-mcp"],
      "env": { "BLENDER_EXECUTABLE": "C:\\Program Files\\Blender Foundation\\Blender 4.4\\blender.exe" }
    }
  }
}
```

## Quotes (brief, for attribution)
> You do not need to open Blender's UI for most MCP tools — the server spawns headless Blender automatically and falls back from live session when no bridge is connected.  (sandraschi)
> Skip the live viewport bridge addon for headless use.  (sandraschi)

## Contradictions flagged
- Tool count is 41 portmanteau tools (150+ ops) in title (vs Features section says 48+ MCP tools)
- Python 3.13+ required (badge) (vs Requirements section says Python 3.12+)
- Blender 3.0+ is the requirement (vs Example config points at Blender 4.4 install path)

## Points to
- https://github.com/sandraschi/blender-mcp/releases/latest
- https://www.blender.org/download/
- https://github.com/PrefectHQ/fastmcp
- https://github.com/sandraschi/qcad-mcp
- https://github.com/sandraschi/freecad-mcp
- https://github.com/sandraschi/resonite-mcp
- https://github.com/sandraschi/speech-mcp
- docs/CONFIGURATION.md
- docs/FEATURES.md
- docs/TROUBLESHOOTING.md
