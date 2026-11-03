---
type: research-source
id: gh-sandraschi-blender-mcp-f-assets-prompts-user.md
title: "sandraschi/blender-mcp/assets/prompts/user.md"
source_type: "github"
creator: "sandraschi"
url: "https://github.com/sandraschi/blender-mcp/blob/HEAD/assets/prompts/user.md"
published: "2026-10-25"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0020
relevance: 2
density: low
tags: ["research-source", "github", "blender-roblox-export-import", "claude-blender-ai", "mesh-texture-limits", "other", "rigging-animation"]
---
# gh-sandraschi-blender-mcp-f-assets-prompts-user.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Generic user manual for the sandraschi blender-mcp server: prompt-driven Blender control via named tools (blender_mesh, blender_materials, blender_animation, etc.). Prerequisites: Blender 4.2+, FastMCP 3.2, Python 3.10+. Covers modeling, keyframes, physics, lighting, and Unity/VRChat/FBX/GLB export. No Roblox-specific content; claims are unverified doc assertions.

## Claims
- c1: Prerequisites listed: Blender 4.2+, FastMCP 3.2, Python 3.10+. Versions stated without test matrix. *(doc, medium; claude-blender-ai)*
- c2: Server exposes tools named blender_mesh, blender_transform, blender_modifiers, blender_materials, blender_camera, blender_render, blender_animation, blender_physics, blender_lighting, blender_export, blender_furniture. *(doc, medium; claude-blender-ai)*
- c3: Agent-driven workflow: natural-language prompt is mapped to tool calls that run Blender Python API under the hood. *(doc, low; claude-blender-ai)*
- c4: Guide has no Roblox Studio, Roblox FBX import, MeshPart, or Roblox texture/limit guidance; only Unity/VRChat/Unreal/web export is covered. *(doc, high; other)*
- c5: Export section recommends apply_transform to freeze scale before export and claims export_unity preset auto-applies -90 degree X rotation for Z-up to Y-up; applies to Unity, not Roblox. *(doc, low; blender-roblox-export-import)*
- c6: Recommends FBX when rigging/bone hierarchies are needed; GLB/GLTF for web or lightweight AR. *(opinion, low; blender-roblox-export-import)*
- c7: Bouncing-ball keyframe recipe: keys at frames 1, 12, 24 with Z=5, 0, 5; play range 1-24. *(doc, medium; rigging-animation)*
- c8: Physics baking: call bake_physics before rendering animations involving rigid body or cloth simulations. *(doc, medium; rigging-animation)*
- c9: Cycles sample guidance: 32-64 for iteration, 128-256 with denoising for final delivery. *(opinion, low; other)*
- c10: Object-not-found errors occur when object names are not used with exact case-sensitive names from the selection tool. *(experience, low; claude-blender-ai)*
- c11: Timeout default 300s; increase OPERATION_TIMEOUT env var for heavy simulations or high-res renders. *(doc, medium; claude-blender-ai)*
- c12: Geometry Nodes are not created by a dedicated tool; the doc says to add a Geometry Nodes modifier via blender_modifiers and link the node tree through a custom script tool. *(doc, low; claude-blender-ai)*
- c13: Boolean modifiers on high-poly meshes are slow; apply them once the shape is final. *(opinion, medium; mesh-texture-limits)*

## Numbers
- n1: **Minimum Blender version**: 4.2+ 
- n2: **FastMCP version**: 3.2 
- n3: **Python version**: 3.10+ 
- n4: **Operation timeout default**: 300s 
- n5: **Export rotation for Unity Z-up to Y-up**: -90 deg X 
- n6: **Bounce keyframes**: frames 1, 12, 24; Z 5, 0, 5 
- n7: **Cycles samples**: 32-64 iteration; 128-256 final 

## Techniques
- t1: **Prompt-to-tool-call scene setup**: Describe scene in natural language; agent calls blender_mesh create_cube, blender_materials for Principled BSDF, blender_camera, blender_render for PNG preview.
- t2: **Keyframe bounce**: Move object to Z=5, set key at frame 1; move to Z=0, key at 12; back to Z=5, key at 24; set range 1-24; play.
- t3: **Physics bake before render**: Set rigid body or cloth with blender_physics; call bake_physics before rendering animation.
- t4: **Apply transforms before export**: Select objects, run blender_transform apply_transform to freeze scale, then export (doc uses Unity preset).

## Quotes (brief, for attribution)
> Blender MCP is not just a collection of tools; it is a Command and Control Center for Blender.  (sandraschi)
> Use blender_export (operation: export_unity). This tool automatically applies the -90 degree X-rotation required...  (sandraschi)

## Points to
- https://github.com/sandraschi/blender-mcp
