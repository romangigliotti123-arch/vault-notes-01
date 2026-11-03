---
type: research-source
id: gh-HoldMyBeer-gg-blenderwright-rel-v3.1.0
title: "HoldMyBeer-gg/blenderwright v3.1.0: v3.1.0"
source_type: "github"
creator: "HoldMyBeer-gg"
url: "https://github.com/HoldMyBeer-gg/blenderwright/releases/tag/v3.1.0"
published: "2026-10-26"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0022
relevance: 3
density: medium
tags: ["research-source", "github", "bpy-scripting-headless", "claude-blender-mcp", "common-mistakes-fixes", "other", "procedural-generation", "rigging-animation", "roblox-export-settings", "texturing-baking-uv"]
---
# gh-HoldMyBeer-gg-blenderwright-rel-v3.1.0

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Release notes for blenderwright v3.1.0, an MCP server that lets Claude drive a live Blender. Covers new tools (animation drivers, keyframes, NLA, rigging, physics, Grease Pencil, Freestyle, geometry node graphs, asset libraries, linked data, export options, colour space), server changes (Start with Blender, per-port tokens), and a CI change running tests against real Blender 5.2. Nothing on Roblox export or import.

## Claims
- c1: blenderwright 3.1.0 tests every tool against a real Blender 5.2 on Linux and Windows on each pull request, replacing mocked tests. *(doc, high; claude-blender-mcp)*
- c2: Writing the real-Blender suite found bugs the old mocked tests missed; 3.1.0 retired fake-Blender tests across many areas. *(doc, high; claude-blender-mcp)*
- c3: Drivers are restricted to Python-free simple expressions. *(doc, high; claude-blender-mcp)*
- c4: keyframe_property can animate material colours, light power, lens and other animatable properties. *(doc, high; claude-blender-mcp)*
- c5: 3.1.0 adds bone collections, IK chains, and more constraints (constraint settings hardened). *(doc, high; rigging-animation)*
- c6: 3.1.0 adds actions, NLA strips and F-curve modifiers. *(doc, high; rigging-animation)*
- c7: add geometry node graphs can be built in one call, including zones (simulation, repeat, for-each); get_node_tree reports node values and settings. *(doc, high; procedural-generation)*
- c8: Adds 30 more shader nodes and 13 more modifiers; modifier targets can be referenced by name. *(doc, high; procedural-generation)*
- c9: Physics additions: force fields, colliders, soft bodies, rigid body constraints and world settings. *(doc, high; other)*
- c10: Drawing additions: Grease Pencil v3 strokes, Line Art, and Freestyle ink line renders. *(doc, high; other)*
- c11: Modelling additions: lattice cages, metaballs, and edit_mesh_operation. *(doc, high; other)*
- c12: Adds color attributes (vertex colours) and multiple UV maps with UV map management; UV tools fixed in edit mode. *(doc, high; texturing-baking-uv)*
- c13: Per-format export options added, including Draco compression, axes and apply-modifiers settings. *(doc, high; roblox-export-settings)*
- c14: set_units tool added for scene units; working colour space tool added. *(doc, high; roblox-export-settings)*
- c15: convert_object now keeps the object's name; get_object_info reports world_location and up-to-date dimensions. *(doc, high; common-mistakes-fixes)*
- c16: Fixed select_by_axis halves, focus_on_object in sculpt and edit mode, add_geometry_node, and threaded shafts now watertight. *(doc, high; common-mistakes-fixes)*
- c17: Server gets optional 'Start with Blender' toggle in the N-panel and one token per port, so two Blenders can each run a server. *(doc, high; claude-blender-mcp)*
- c18: An unencodable reply now returns an error instead of dropping the connection. *(doc, high; claude-blender-mcp)*
- c19: Asset library tools (list and place), manage_linked_data (make local, override, reload), manage_external_paths, and pack/unpack resources were added. *(doc, high; bpy-scripting-headless)*
- c20: Release contains 41 PRs (#99 to #139); a stale blend-ai-v1.0.0.zip was removed from the repo. *(doc, medium; other)*

## Numbers
- n1: **Blender version used in CI tests**: 5.2 (Linux and Windows) 
- n2: **Added shader nodes**: 30 
- n3: **Added modifiers**: 13 
- n4: **PRs in release**: 41 (#99 to #139) 
- n5: **Server tokens**: one per port 

## Techniques
- t1: **Per-port token server**: Each Blender instance runs its own MCP server on a separate port with its own token; enable 'Start with Blender' in N-panel to auto-start.
- t2: **One-call geometry node graph build**: Build a full geometry node tree including zones in a single tool call instead of node-by-node.

## Points to
- https://github.com/HoldMyBeer-gg/blenderwright/releases/tag/v3.1.0
- https://github.com/HoldMyBeer-gg/blenderwright/compare/v3.0.0...v3.1.0
