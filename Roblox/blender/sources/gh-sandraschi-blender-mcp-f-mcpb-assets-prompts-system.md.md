---
type: research-source
id: gh-sandraschi-blender-mcp-f-mcpb-assets-prompts-system.md
title: "sandraschi/blender-mcp/mcpb/assets/prompts/system.md"
source_type: "github"
creator: "sandraschi"
url: "https://github.com/sandraschi/blender-mcp/blob/HEAD/mcpb/assets/prompts/system.md"
published: "2026-10-25"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0018
relevance: 1
density: low
tags: ["research-source", "github", "bpy-scripting-headless", "claude-blender-mcp", "common-mistakes-fixes", "procedural-generation", "rigging-animation", "roblox-export-settings", "texturing-baking-uv"]
---
# gh-sandraschi-blender-mcp-f-mcpb-assets-prompts-system.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Internal system-prompt document for a blender-mcp server (sandraschi). Describes an MCP "orchestrator" persona, a bridge to Blender via a subprocess executor, and tool categories (mesh, transform, furniture, modifiers, materials, rigging, animation, camera, lighting, physics, particles, export). Roblox is not mentioned; Unity/VRChat export is the focus. Mostly generic and includes unverified claims.

## Claims
- c1: Server uses a BlenderExecutor class managing a subprocess bridge to a Blender instance, claimed to isolate crashes from the MCP server. *(doc, medium; claude-blender-mcp)*
- c2: Tools are grouped into 19 categories as portmanteau tools, each handling multiple operation types via an operation parameter. *(doc, medium; claude-blender-mcp)*
- c3: Export pipelines listed cover Unity (automated 0.01 scale correction, Y-forward) and VRChat; no Roblox export path is documented. *(doc, high; roblox-export-settings)*
- c4: bake_texture tool is described as exporting procedural materials to FBX-compliant formats; no baking parameters given. *(doc, medium; texturing-baking-uv)*
- c5: Advice: apply scale before Bevel or Solidify modifiers to avoid distorted bevels. *(opinion, medium; common-mistakes-fixes)*
- c6: Furniture generator offers create_chair/table/bed/sofa/cabinet/desk/shelf/stool with styles modern, classic, rustic, industrial. *(doc, medium; procedural-generation)*
- c7: Rigging tools listed: armature, add_bone, set_parent_with_weights, create_bone_ik; no export or Roblox rig constraints given. *(doc, medium; rigging-animation)*
- c8: For game engine meshes, keep low poly count or add Subdivision Surface modifier unapplied until export. *(opinion, medium; common-mistakes-fixes)*
- c9: Claims 'Clean Engine' rule since v0.5.0: never print to stdout; log to stderr to avoid breaking JSON-RPC stream. *(doc, medium; claude-blender-mcp)*
- c10: Recommends bpy.ops.outliner.orphans_purge() for large scene cleanup; physics bake flagged as time-intensive. *(doc, low; bpy-scripting-headless)*
- c11: Document claims 'SOTA v14.1' and 'FastMCP 3.2' compatibility and 2026 JSON-RPC standards; unverified marketing-like claims. *(opinion, low; claude-blender-mcp)*

## Numbers
- n1: **tool categories**: 19 categories; header says 50+ tools 
- n2: **Unity export scale correction**: 0.01 
- n3: **Subdivision render level**: Level 2 for renders, Level 1 for viewport 
- n4: **Clean Engine rule version**: v0.5.0 

## Techniques
- t1: **Apply scale before bevel/solidify**: Apply scale transform (reset to 1.0) before adding Bevel or Solidify so modifier thickness is not distorted.
- t2: **Verify via preview render**: After each batch of tool calls, call blender_render in preview mode to check progress.

## Quotes (brief, for attribution)
> Never use print() or console.log() for diagnostic output during execution. All diagnostic telemetry must flow through the logger (stderr).  (sandraschi)

## Contradictions flagged
- Recommends low poly or unapplied subdivision for game engines, while also saying 'Level 2 is usually sufficient for renders'. (vs No Roblox-specific triangle or mesh limits given; internal tension on subdivision guidance.)

## Points to
- https://github.com/sandraschi/blender-mcp
