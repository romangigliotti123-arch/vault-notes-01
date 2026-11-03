---
type: research-source
id: gh-HoldMyBeer-gg-blenderwright-readme
title: "HoldMyBeer-gg/blenderwright README: MCP server for Blender. Hundreds of tools for modeling, materials, rendering and more, driven by Claude,"
source_type: "github"
creator: "HoldMyBeer-gg"
url: "https://github.com/HoldMyBeer-gg/blenderwright"
published: "2026-10-28"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0078
relevance: 3
density: high
tags: ["research-source", "github", "bpy-scripting-headless", "claude-blender-mcp", "common-mistakes-fixes", "creator-workflows", "procedural-generation", "roblox-export-settings", "texturing-baking-uv"]
---
# gh-HoldMyBeer-gg-blenderwright-readme

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
README for blenderwright, a community MCP server that lets Claude drive a live Blender 5.2 LTS through a TCP addon. Covers install (uvx/pip plus Blender extension), connection config, 276 tools across 32 modules, 13 expert prompts, security model, toolsets, and limitations. Contains no Roblox-specific content; relevant only as a Claude-to-Blender control layer.

## Claims
- c1: Architecture: AI assistant <-stdio/MCP-> blenderwright server <-TCP-> Blender addon <-bpy-> Blender; addon queues commands and runs them on main thread via bpy.app.timers. *(doc, high; claude-blender-mcp)*
- c2: Requires Blender 5.2 LTS; Blender 5.1 and earlier refused at install. Developed and tested only on 5.2. *(doc, high; claude-blender-mcp)*
- c3: Client setup for Claude Code is `claude mcp add blenderwright -- uvx blenderwright`; Blender addon must be started first (N-panel > blenderwright > Start Server). *(doc, high; claude-blender-mcp)*
- c4: Default TCP port 9876, configurable 1024-65535; each MCP server talks to one Blender port, so two Blenders need two servers using BLENDERWRIGHT_PORT. *(doc, high; claude-blender-mcp)*
- c5: Toolsets: all 276 schemas cost roughly 48k tokens per request; BLENDERWRIGHT_TOOLSETS=auto or a comma list (e.g. core,physics,animation) trims it; auto relies on tools/list_changed notification. *(doc, high; claude-blender-mcp)*
- c6: execute_blender_code (raw Python) is off until 'Allow raw Python' is ticked per session; it is not a sandbox: 25 imports blocked and builtins like exec/open removed, but bpy alone can save files and run any operator. *(doc, high; claude-blender-mcp)*
- c7: Auth: Start Server writes a random token file (per-user path, e.g. ~/.config/blenderwright/token on Linux); handshake is HMAC-SHA256 challenge-response; commands are signed and numbered. Stop deletes the token. *(doc, high; claude-blender-mcp)*
- c8: Updating requires a full Blender restart, not Reload Scripts, because the TCP server thread survives script reload and leaves the socket bound. *(doc, high; claude-blender-mcp)*
- c9: Duplicate addon installs under an older Blender version are the usual cause of strange behaviour; use `python install_addon.py doctor` to list installs. *(doc, medium; common-mistakes-fixes)*
- c10: Version mismatch: MCP server and addon check protocol version on connect and refuse mismatched pairs; update both to the same release. *(doc, high; claude-blender-mcp)*
- c11: Known limits: Blender must be open with server started; no MCP-level undo; shared selection state means two assistants on one mesh conflict; sculpt strokes cannot be simulated; viewport capture may fail headless; no streaming progress. *(doc, high; claude-blender-mcp)*
- c12: Shader node trees are built one node/connection per call; geometry node trees can be built in one call via build_geometry_nodes. *(doc, high; claude-blender-mcp)*
- c13: Render guard: server returns busy during renders, queues commands, and recovers from crashed renders via load_post handler and a reset_render_guard command. *(doc, medium; claude-blender-mcp)*
- c14: Development tests: unit tests run with Blender faked; live tests (tests_live) run against a real headless Blender 5.2 via BLENDER env var; CI matrix ubuntu/macos/windows x py3.11/3.13. *(doc, high; bpy-scripting-headless)*
- c15: Baking tool bakes albedo, normal (high-poly to low-poly with cage), AO, roughness, emission or lit maps to PNG/EXR/TIFF using Cycles; UV tools include smart project, unwrap (ANGLE_BASED, CONFORMAL, MINIMUM_STRETCH), pack islands, texel density. *(doc, high; texturing-baking-uv)*
- c16: File I/O tools cover import/export of FBX, OBJ, glTF, USD, STL; the README gives no Roblox-specific export settings (scale, axes, apply transforms, embed textures). *(doc, high; roblox-export-settings)*
- c17: Geometry nodes: build_geometry_nodes builds a whole node graph in one call; Essentials modifiers like array, scatter on surface, instance on elements, curve to tube are exposed. *(doc, medium; procedural-generation)*
- c18: Mesh quality tool reports non-manifold edges, loose verts, zero-area faces, duplicate verts, wire edges and can repair them; decimate reduces polycount. *(doc, high; common-mistakes-fixes)*
- c19: Prompt 'imported_mesh_cleanup' covers import, analyze, repair, decimate, normals, scale and UVs for meshes from scans, downloads or generators. *(doc, medium; creator-workflows)*
- c20: Procedural materials: create_procedural_material builds a full node graph (coordinate, mapping, noise, height mask, colour ramp, Principled BSDF) in one call, per author's demo of fifteen materials. *(demo, medium; procedural-generation)*
- c21: Author claims a multi-part scene (shuttle, saloon) was built from one prompt in ~20 minutes with Claude Code; marketing demo, unverified. *(opinion, low; creator-workflows)*
- c22: Features include auto-critique loop: fast OpenGL viewport screenshots (~ms) plus prompts telling the LLM when to screenshot and what to check. *(doc, medium; claude-blender-mcp)*
- c23: Extension suggestions: server recommends Bool Tool, LoopTools, Node Wrangler when useful, skipping installed ones. *(doc, medium; claude-blender-mcp)*
- c24: Zero telemetry; binds to 127.0.0.1 only; installs with uvx from PyPI; addon uses stdlib + bpy only. *(doc, high; claude-blender-mcp)*
- c25: Restricted-namespace guard: model-driven code can't import os/subprocess/socket etc.; author says this guards against accidents only. *(doc, medium; creator-workflows)*

## Numbers
- n1: **tool count**: 276 tools in 32 modules 
- n2: **prompts**: 13 expert MCP prompts 
- n3: **schema token cost**: ~48k tokens per request for all tools 
- n4: **default port**: 9876 (range 1024-65535) 
- n5: **blocked imports**: 25 modules refused under raw Python 
- n6: **shader node types allowed**: 93 
- n7: **tests**: 2900+ unit, 600+ live against Blender 5.2 
- n8: **Blender version**: 5.2 LTS only 

## Techniques
- t1: **Toolset trimming**: Set BLENDERWRIGHT_TOOLSETS to auto or a comma list (e.g. core,physics) in the MCP client env to cut the ~48k-token schema load.
- t2: **Per-session raw Python gate**: Leave execute_blender_code off; tick 'Allow raw Python' in the N-panel only when needed, read each snippet echoed to console, untick after.
- t3: **Clean addon reinstall**: Stop server, run install_addon.py doctor to find duplicate installs, uninstall all, fully restart Blender (not Reload Scripts), reinstall zip.

### Code: Register the MCP server with Claude Code
```bash
claude mcp add blenderwright -- uvx blenderwright
```

### Code: Limit toolsets to reduce schema token cost
```json
{
  "mcpServers": {
    "blenderwright": {
      "command": "uvx",
      "args": ["blenderwright"],
      "env": { "BLENDERWRIGHT_TOOLSETS": "auto" }
    }
  }
}
```

## Quotes (brief, for attribution)
> Raw Python is opt-in: execute_blender_code is off until you tick "Allow raw Python" in the N-panel, per session.  (HoldMyBeer-gg)
> Blender must be fully restarted, not "Reload Scripts".  (HoldMyBeer-gg)

## Contradictions flagged
- Restricted namespace blocks dangerous imports and builtins. (vs Same README: bpy alone can save files anywhere and run any operator, so it is not a sandbox.)
- Marketing text says it goes beyond tool exposure to produce professional results. (vs Same README's limitations: no undo integration, sculpt strokes not simulated, shared selection causes conflicts.)

## Points to
- https://blenderwright.holdmybeer.gg/
- https://docs.astral.sh/uv/
- https://www.blender.org/download/
- https://github.com/HoldMyBeer-gg/blenderwright/releases
