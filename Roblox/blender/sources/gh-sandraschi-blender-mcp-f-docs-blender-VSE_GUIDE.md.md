---
type: research-source
id: gh-sandraschi-blender-mcp-f-docs-blender-VSE_GUIDE.md
title: "sandraschi/blender-mcp/docs/blender/VSE_GUIDE.md"
source_type: "github"
creator: "sandraschi"
url: "https://github.com/sandraschi/blender-mcp/blob/HEAD/docs/blender/VSE_GUIDE.md"
published: "2026-10-25"
retrieved: 2026-11-01
extracted_by: "sonnet"
extraction_cost_usd: 0.0306
relevance: 1
density: low
tags: ["research-source", "github", "automation-and-creator-workflows", "claude-blender-ai"]
---
# gh-sandraschi-blender-mcp-f-docs-blender-VSE_GUIDE.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Guide to the sandraschi blender-mcp `blender_vse` tool: 20 operations driving Blender's Video Sequence Editor headlessly (--background) via an MCP executor. Covers strip creation/editing, effects, rendering codecs. Shows the MCP-tool-wrapping-headless-Blender pattern, but nothing on Roblox, FBX export, meshes, or rigging. Marginal relevance.

## Claims
- c1: The blender-mcp fork by sandraschi exposes a `blender_vse` MCP tool with 20 operations for video editing without opening Blender's GUI. *(doc, high; claude-blender-ai)*
- c2: All VSE operations run through a Blender executor in `--background` mode, so there is no real-time preview and processing is CPU-only. *(doc, high; claude-blender-ai)*
- c3: Limitations: strip names must be tracked by the caller, no audio waveform, and strip transforms are static, with no keyframed properties. *(doc, high; claude-blender-ai)*
- c4: The executable is located via `BLENDER_EXECUTABLE` in config.py; a 'Blender not found' error is fixed by setting that or checking the install path. *(doc, medium; claude-blender-ai)*
- c5: The server chains with a separate `blender_render` tool, such as turntable render to image sequence to VSE, and with other MCP servers like filesystem-mcp. This shows multi-tool MCP pipelines. *(doc, medium; automation-and-creator-workflows)*
- c6: `render_video` sets `scene.render.use_sequencer = True` automatically. A blank render is attributed to this flag not being set. *(doc, medium; claude-blender-ai)*

## Numbers
- n1: **VSE operations exposed**: 20 operations in blender_vse MCP tool
- n2: **Default FPS**: 30 VSE default frame rate

## Techniques
- t1: **Turntable render to video via MCP**: Call blender_render render_turntable (output_dir, frames=60), then blender_vse add_image_sequence on that directory, add_text overlay, then render_video to an mp4 path.

### Code: Chain turntable render into VSE video render via MCP tool calls
```python
blender_render(operation="render_turntable", output_dir="C:/turntable", frames=60)
blender_vse(operation="add_image_sequence", directory="C:/turntable", channel=1)
blender_vse(operation="add_text", text="Product Showcase", channel=2, length=60)
blender_vse(operation="render_video", output_path="C:/output/showcase.mp4")
```

## Points to
- sandraschi/blender-mcp
- qcad-mcp
- filesystem-mcp
- plex-mcp
