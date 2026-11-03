---
type: research-source
id: gh-sandraschi-blender-mcp-f-assets-prompts-system.md
title: "sandraschi/blender-mcp/assets/prompts/system.md"
source_type: "github"
creator: "sandraschi"
url: "https://github.com/sandraschi/blender-mcp/blob/HEAD/assets/prompts/system.md"
published: "2026-10-25"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0038
relevance: 1
density: low
tags: ["research-source", "github", "automation-and-creator-workflows", "blender-roblox-export-import", "claude-blender-ai", "mesh-texture-limits", "rigging-animation"]
---
# gh-sandraschi-blender-mcp-f-assets-prompts-system.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
System-prompt style directive for a blender-mcp server (sandraschi). Lists tool categories (mesh, transform, modifiers, materials, rigging, animation, export) and rules: Z-up metric scale, apply scale before bevel, no print() to stdout, orphans purge. Targets Unity/VRChat, not Roblox. No Roblox export, rig, or mesh-limit guidance.

## Claims
- c1: Server exposes 19 tool categories, each a portmanteau tool with operation types; the doc's header claims 50+ tools. *(doc, medium; claude-blender-ai)*
- c2: Bridge pattern: BlenderExecutor manages a subprocess bridge to a Blender instance so script crashes do not take down the MCP server. *(doc, medium; claude-blender-ai)*
- c3: Rule: never use print() or console.log() for diagnostics since v0.5.0; stdout pollution breaks the JSON-RPC stream. Logger to stderr instead. *(doc, high; claude-blender-ai)*
- c4: Best practice: apply scale transform before applying Bevel or Solidify to avoid distorted bevels. *(opinion, medium; claude-blender-ai)*
- c5: Large scene cleanup should use bpy.ops.outliner.orphans_purge(). *(doc, medium; claude-blender-ai)*
- c6: Verification step: call blender_render in preview mode after batched tool calls to show progress. *(opinion, low; claude-blender-ai)*
- c7: Doc's export section targets Unity (automated 0.01 scale correction, Y-forward) and VRChat FBX packaging; no Roblox export settings are given. *(doc, high; blender-roblox-export-import)*
- c8: Doc says Blender is Z-up and Unity is Y-up, and the exporter handles rotation; model forward face should face Blender -Y. *(doc, medium; blender-roblox-export-import)*
- c9: Game-engine meshes should stay low poly, with Subdivision Surface added but unapplied until export. *(opinion, low; mesh-texture-limits)*
- c10: Subdivision levels: Level 2 usually enough for renders, Level 1 for viewport. *(opinion, low; mesh-texture-limits)*
- c11: bake_texture is said to be needed to export procedural materials to FBX-compliant formats; no texture size or UV limits given. *(doc, low; mesh-texture-limits)*
- c12: Rigging tools listed: armature, add_bone, set_parent_with_weights, create_bone_ik. No skinning limits or export details. *(doc, medium; rigging-animation)*
- c13: Physics bake (bake_physics) is time-intensive; the agent should warn the user of likely timeouts. *(doc, medium; automation-and-creator-workflows)*
- c14: Doc mixes version labels (v0.5.0 rule, SOTA v14.1, FastMCP 3.2) and states a 2026 JSON-RPC standard without specifics; version scheme is unclear. *(doc, low; claude-blender-ai)*

## Numbers
- n1: **tool categories**: 19 
- n2: **tool count claimed**: 50+ 
- n3: **Unity export scale correction**: 0.01 
- n4: **subdivision level for render / viewport**: Level 2 render, Level 1 viewport 

## Techniques
- t1: **Apply scale before modifiers**: Apply scale transform to reset scale to 1 before adding Bevel or Solidify to avoid distorted results.
- t2: **Stdout-safe logging**: Send diagnostics to logger on stderr, not print(), so the JSON-RPC stream stays clean.

### Code: Memory cleanup call named in the doc for large scene cleanup
```python
bpy.ops.outliner.orphans_purge()
```

## Quotes (brief, for attribution)
> As of v0.5.0, you must NEVER use print() or console.log() for diagnostic output during execution.  (sandraschi)
> Always apply_transform (Scale) before applying modifiers like Bevel or Solidify to avoid distorted bevels.  (sandraschi)

## Contradictions flagged
- Doc says 50+ industrial tools. (vs Doc itself states 19 distinct tool categories.)
- Doc's pipeline sections describe Unity and VRChat exports. (vs Doc title and topic are Blender for Roblox; no Roblox content present.)

## Points to
- https://github.com/sandraschi/blender-mcp
