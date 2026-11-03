---
type: research-source
id: gh-sandraschi-blender-mcp-f-mcpb-assets-prompts-user.md
title: "sandraschi/blender-mcp/mcpb/assets/prompts/user.md"
source_type: "github"
creator: "sandraschi"
url: "https://github.com/sandraschi/blender-mcp/blob/HEAD/mcpb/assets/prompts/user.md"
published: "2026-10-25"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0020
relevance: 2
density: low
tags: ["research-source", "github", "automation-and-creator-workflows", "blender-roblox-export-import", "claude-blender-ai", "mesh-texture-limits", "other", "rigging-animation"]
---
# gh-sandraschi-blender-mcp-f-mcpb-assets-prompts-user.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
User manual for sandraschi's blender-mcp (MCP server for Blender driven by natural language). Covers prerequisites (Blender 4.2+, FastMCP 3.2, Python 3.10+), tool names, basic modeling, keyframe bounce example, lighting, and a Unity/VRChat export preset. No Roblox export settings, no bpy script code, no Roblox limits. Mostly generic, with unverified marketing claims.

## Claims
- c1: Blender MCP guide claims Blender 4.2+, FastMCP 3.2, and Python 3.10+ are prerequisites; no version tested or source given. *(doc, medium; claude-blender-ai)*
- c2: Example first-scene prompt chains blender_mesh(create_cube), blender_materials (Principled BSDF), blender_camera, and blender_render to output a PNG. *(doc, medium; claude-blender-ai)*
- c3: Guide says errors like 'Object not found' need the exact case-sensitive object name; 'Timeout' default is 300s, adjustable via OPERATION_TIMEOUT env var. *(doc, medium; claude-blender-ai)*
- c4: Geometry Nodes are not built directly: guide says add a Geometry Nodes modifier via blender_modifiers, then link the node tree via a custom script tool; no script shown. *(doc, low; claude-blender-ai)*
- c5: Guide's game-engine export section covers Unity/VRChat (export_unity preset, -90 X rotation, apply scale first), not Roblox; no Roblox-specific settings given. *(doc, high; blender-roblox-export-import)*
- c6: Guide advises FBX for rigged Unity/Unreal assets and GLB/GLTF for web or AR; does not mention Roblox import formats. *(doc, medium; blender-roblox-export-import)*
- c7: Guide suggests Cycles samples 32-64 for iteration and 128-256 with denoising for final delivery; opinion-level guidance, no Roblox limits. *(doc, medium; mesh-texture-limits)*
- c8: Guide warns high-poly boolean modifiers are slow; recommends applying them after shape is finalized. *(doc, medium; mesh-texture-limits)*
- c9: Bouncing-ball keyframe recipe: Z=5 at frame 1, Z=0 at frame 12, Z=5 at frame 24, play range 1-24 via blender_animation. *(doc, medium; rigging-animation)*
- c10: Guide says call bake_physics before rendering animations with rigid body or cloth simulations; no rigging or skinning content present. *(doc, medium; rigging-animation)*
- c11: Guide frames the tool as a natural-language agentic layer over Blender's Python API; no bpy script examples or blender -b batch usage shown. *(doc, medium; automation-and-creator-workflows)*
- c12: Guide contains marketing-style claims (SOTA 14.1, 'industrial-grade', 'zero stdout pollution') that are unverified by the document itself. *(opinion, high; other)*

## Numbers
- n1: **Blender minimum version**: 4.2+ Required for Geometry Nodes and Eevee Next per guide
- n2: **FastMCP version**: 3.2 Prerequisite listed for tool registration and sampling
- n3: **Python minimum**: 3.10+ Core execution runtime per guide
- n4: **Default operation timeout**: 300s Overridable via OPERATION_TIMEOUT in environment config
- n5: **Cycles samples iteration**: 32-64 Internal iteration; guide opinion
- n6: **Cycles samples final**: 128-256 with denoising Final delivery; guide opinion
- n7: **Floor plane size**: 10m x 10m Modern living room example
- n8: **Bounce keyframes**: frames 1, 12, 24 (Z=5, 0, 5) Animation basics example
- n9: **Test cube size and camera distance**: 2m cube, camera 5m away First-scene verification prompt

## Techniques
- t1: **Natural-language to MCP tool chain**: Describe the scene goal in plain language; the agent calls blender_mesh, blender_materials, blender_camera, blender_render in sequence. Verify with a simple cube render first.
- t2: **Apply booleans late**: Keep high-poly boolean modifiers off until geometry is final; apply them once shape is finalized to avoid slow viewport work.
- t3: **Bake physics before render**: For rigid body or cloth sims, call bake_physics before blender_animation render so simulated frames are stored.
- t4: **Apply transforms before export**: Use blender_transform apply_transform to freeze scale before exporting; guide states this for Unity/VRChat, not Roblox.

## Quotes (brief, for attribution)
> Blender MCP is not just a collection of tools; it is a Command and Control Center for Blender.  (sandraschi)
> This tool automatically applies the -90 degree X-rotation required to translate Blender's Z-up to Unity's Y-up  (sandraschi)

## Contradictions flagged
- Guide says exporting to game engines is covered for Unity/VRChat only; Roblox pipeline is absent despite the Roblox-focused topic. (vs Topic framing: Blender-to-Roblox asset pipeline)
- Guide states the tool automatically applies a -90 X rotation for export_unity, while step 2 requires manual apply_transform first. (vs Internal: section 5.1 steps)

## Points to
- https://github.com/sandraschi/blender-mcp
- FastMCP
- Blender Geometry Nodes
- Eevee Next
