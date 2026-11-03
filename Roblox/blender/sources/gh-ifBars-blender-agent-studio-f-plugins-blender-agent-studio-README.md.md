---
type: research-source
id: gh-ifBars-blender-agent-studio-f-plugins-blender-agent-studio-README.md
title: "ifBars/blender-agent-studio/plugins/blender-agent-studio/README.md"
source_type: "github"
creator: "ifBars"
url: "https://github.com/ifBars/blender-agent-studio/blob/HEAD/plugins/blender-agent-studio/README.md"
published: "2026-10-25"
retrieved: 2026-11-01
extracted_by: "sonnet"
extraction_cost_usd: 0.0652
relevance: 2
density: medium
tags: ["research-source", "github", "bpy-scripting-headless", "claude-blender-mcp", "common-mistakes-fixes", "creator-workflows", "procedural-generation", "rigging-animation"]
---
# gh-ifBars-blender-agent-studio-f-plugins-blender-agent-studio-README.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
README for Blender Agent Studio, a Codex/Claude Code plugin with skills for Blender 5.2 modeling, validation, GLB re-import checks, and a bounded local MCP that omits arbitrary Python execution. It recommends Blender's official Lab MCP for live use. It has no Roblox content, so it only helps with Claude-driven Blender workflow and validation habits.

## Claims
- c1: The plugin works in both Codex and Claude Code. Both load the same skills, bounded MCP server (mcp/server.ts) and SceneIR runtime. Claude Code reads .claude-plugin/plugin.json and uses ${CLAUDE_PLUGIN_ROOT}. *(doc, high; claude-blender-mcp)*
- c2: The local MCP exposes Blender version, asset inspection and evidence render tools. It deliberately does not expose generic arbitrary Python execution. *(doc, high; claude-blender-mcp)*
- c3: The author recommends Blender's official Lab MCP for live Blender interaction and bundled API docs. The local MCP is only a deterministic evaluation convenience, and MCP should be evaluated as its own condition. *(doc, high; claude-blender-mcp)*
- c4: Claude Code resolves relative MCP paths from the session's project directory, so pass absolute paths when location matters. *(doc, high; claude-blender-mcp)*
- c5: The workflow is script-first. The modeling skill asks for a reproducible create_asset.py that produces asset.blend and asset.glb. Completion requires clean-source reproduction. *(doc, medium; bpy-scripting-headless)*
- c6: Validation uses evaluated geometry inspection, fresh GLB re-import and fixed evidence renders. blender_diagnose_topology finds degenerate faces and zero-length edges in evaluated world space. Open boundaries are not auto-classified as defects. *(doc, high; common-mistakes-fixes)*
- c7: The procedural skill covers editable Geometry Nodes, modifiers, instancing, terrain and generator validation. *(doc, medium; procedural-generation)*
- c8: The character skill covers topology, armatures, skinning, deformation poses, actions and fresh-import checks. The animation skill covers critical-frame review and mechanical pivots. *(doc, medium; rigging-animation)*
- c9: The automated benchmark score uses structural and finish-signal proxies. Visual-quality claims need blinded pairwise comparison. Measure skill changes on one fixed model before comparing models. *(doc, medium; creator-workflows)*
- c10: Bounds overlap and anchor agreement are only candidates for problems. Neither proves mesh intersection or surface contact, so visual verification is still required. *(doc, high; creator-workflows)*

## Numbers
- n1: **Blender version targeted**: 5.2 
- n2: **Plugin version**: 0.5.0 
- n3: **Inline viewer limits**: 12 PNGs, 10 MB image bytes 
- n4: **Fire-lantern fixture video**: 15 s, 24 fps MP4 

## Techniques
- t1: **Fresh GLB import validation**: Export the asset as GLB, re-import it into a clean Blender session, inspect evaluated geometry, and render fixed evidence views. Reproduce from clean source before declaring completion.
- t2: **Topology diagnosis**: Run blender_diagnose_topology to locate degenerate faces and zero-length edges by object name, repair them in the source script, then recheck the exported asset.
- t3: **Invoke skill in Claude Code**: Run /blender-agent-studio:blender-modeling-workflow with the request. Add the animation or validation skills by name for articulated assets or review-only work.

### Code: Run the benchmark in skills mode
```powershell
bun run benchmark --suite quick --mode skills --output C:\bench\skills
```

## Points to
- Blender Lab MCP (official)
- skills/blender-mcp-integration/references/mcp-options.md
- docs/scene-understanding.md
- Codex
- Claude Code
- Bun
