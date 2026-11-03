---
type: research-source
id: gh-HoldMyBeer-gg-blenderwright-rel-v3.0.0
title: "HoldMyBeer-gg/blenderwright v3.0.0: v3.0.0"
source_type: "github"
creator: "HoldMyBeer-gg"
url: "https://github.com/HoldMyBeer-gg/blenderwright/releases/tag/v3.0.0"
published: "2026-10-24"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0015
relevance: 3
density: high
tags: ["research-source", "github", "bpy-scripting-headless", "claude-blender-mcp", "creator-workflows", "procedural-generation", "rigging-animation", "texturing-baking-uv"]
---
# gh-HoldMyBeer-gg-blenderwright-rel-v3.0.0

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Release notes for blenderwright 3.0.0, a Blender MCP add-on/server letting Claude drive Blender, targeting Blender 5.2 LTS. Covers fixed tools on 5.2, a challenge-response socket auth, about 40 new tools (render settings, modelling, vertex groups/shape keys, texture baking, UV ops, link/append). Nothing on Roblox export or import.

## Claims
- c1: blenderwright 3.0.0 is breaking: requires Blender 5.2 LTS; add-on and MCP server must be updated together. *(doc, high; claude-blender-mcp)*
- c2: Six tools broken on Blender 5.2 were fixed: geometry node inputs, sculpt brushes, keyframe interpolation/listing, physics baking, Minimum Stretch unwrap (formerly SLIM), image output after video render. *(doc, high; claude-blender-mcp)*
- c3: Socket uses challenge-response auth; token never crosses socket; every command is signed and numbered to block injection, alteration, replay. *(doc, high; claude-blender-mcp)*
- c4: MCP server sends nothing to a port process that cannot prove it is Blender; on Windows the port is claimed exclusively. *(doc, high; claude-blender-mcp)*
- c5: Release adds about 40 new tools across finished look, light, modelling, deformation, game assets and reuse categories. *(doc, high; claude-blender-mcp)*
- c6: New bake_texture tool supports albedo, normal maps (high-to-low poly), AO and more; UV island operations and texel density added. *(doc, high; texturing-baking-uv)*
- c7: Essentials node modifiers added via tools: array, scatter on surface, curve to tube and more. *(doc, high; procedural-generation)*
- c8: Vertex group and weight operations plus shape keys that can be sculpted, blended and animated were added. *(doc, high; rigging-animation)*
- c9: Removed Collada and X3D export (Blender 5 no longer ships them) and SVG export (never worked). *(doc, high; bpy-scripting-headless)*
- c10: Adds link/append from other .blend files and collection instances for asset reuse. *(doc, high; creator-workflows)*
- c11: Fixes include selected-only export for every format, Cycles/Workbench engine choice, render-busy guard, assign_material on single-material objects, and viewport capture restoring render settings on failure. *(doc, high; claude-blender-mcp)*

## Numbers
- n1: **new tools**: about 40 
- n2: **broken tools fixed on 5.2**: 6 
- n3: **compositor effects**: glare, vignette, film grain + 17 more 
- n4: **release date**: 2026-10-24 

## Techniques
- t1: **Upgrade blenderwright to 3.0**: Install Blender 5.2 LTS. Update the add-on and MCP server together, since 3.0.0 is breaking. Pre-3.0 Blender versions are not supported.

## Quotes (brief, for attribution)
> Breaking: requires Blender 5.2 LTS. Update the add-on and the MCP server together.  (HoldMyBeer-gg)
> The token never crosses the socket, and every command is signed and numbered, so nothing can be injected, altered or replayed.  (HoldMyBeer-gg)

## Points to
- https://github.com/HoldMyBeer-gg/blenderwright/compare/v2.3.0...v3.0.0
