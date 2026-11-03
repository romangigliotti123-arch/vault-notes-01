---
type: research-source
id: gh-ahujasid-cabin-in-the-woods-readme
title: "ahujasid/cabin-in-the-woods README: 🌲 Export Blender scenes to Three.js — real-time 3D in the browser from your Blender workflow"
source_type: "github"
creator: "ahujasid"
url: "https://github.com/ahujasid/cabin-in-the-woods"
published: "2026-08-08"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0009
relevance: 1
density: low
tags: ["research-source", "github", "claude-blender-mcp", "other"]
---
# gh-ahujasid-cabin-in-the-woods-readme

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
README for "Cabin in the Woods", a demo that exports a Blender scene to glTF and runs it in Three.js in the browser. Not about Roblox. Only tangential mention of BlenderMCP (Claude controls Blender via MCP) as a related project. Promotional links and the badges are ignored.

## Claims
- c1: BlenderMCP is described as a tool to control Blender with Claude AI via MCP; the README gives no setup, tools or limits. *(doc, high; claude-blender-mcp)*
- c2: Cabin in the Woods exports a Blender scene to glTF and runs it in Three.js in the browser with no server required; it is not a Roblox pipeline. *(doc, high; other)*

### Code: Run the demo locally
```bash
git clone https://github.com/MCPBlender/cabin-in-the-woods
cd cabin-in-the-woods
python -m http.server 8080
```

## Contradictions flagged
- Repo is listed under the ahujasid account in the source header, but all badges and links point to MCPBlender/cabin-in-the-woods. (vs Source URL (github.com/ahujasid/cabin-in-the-woods))

## Points to
- https://github.com/MCPBlender/blender-mcp
- https://blendermcp.org
- https://github.com/MCPBlender/ableton-mcp
- https://threejs.org
- https://www.khronos.org/gltf/
