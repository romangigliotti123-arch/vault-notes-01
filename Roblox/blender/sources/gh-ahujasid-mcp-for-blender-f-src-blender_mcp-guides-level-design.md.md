---
type: research-source
id: gh-ahujasid-mcp-for-blender-f-src-blender_mcp-guides-level-design.md
title: "ahujasid/mcp-for-blender/src/blender_mcp/guides/level-design.md"
source_type: "github"
creator: "ahujasid"
url: "https://github.com/ahujasid/mcp-for-blender/blob/HEAD/src/blender_mcp/guides/level-design.md"
published: "2026-10-29"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0012
relevance: 1
density: low
tags: ["research-source", "github", "bpy-scripting-headless", "claude-blender-mcp", "common-mistakes-fixes", "creator-workflows", "other"]
---
# gh-ahujasid-mcp-for-blender-f-src-blender_mcp-guides-level-design.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Generic Blender level-design guide, not Roblox-specific. Covers human-scale metrics (1.8 m player, 2-4 m grid modules), blockout, modular kits with linked duplicates, and engine export for Unreal/Godot/Unity via glTF/FBX. Mentions blender-mcp-style calls (look, get_scene_info). No Roblox export, import, or mesh-limit guidance.

## Claims
- c1: Source contains no Roblox-specific guidance; export section targets Unreal, Godot, Unity, web via glTF/FBX. *(doc, high; other)*
- c2: Default human-scale sizes: player capsule 1.8 m tall, 0.6 m wide; step 0.2 m rise, 0.3 m run; max jump ledge ~1 m. *(doc, high; creator-workflows)*
- c3: Modular kit grid: wall 4x3 m, floor 4x4 m, modules on 2 m or 4 m grid; origin at corner or bottom-centre so pieces snap. *(doc, high; creator-workflows)*
- c4: Apply transforms (scale 1, rotation 0) on every exported mesh before export. *(doc, high; common-mistakes-fixes)*
- c5: Keep collision simple (boxes, convex hulls), not the render mesh. *(doc, high; common-mistakes-fixes)*
- c6: Guide references blender-mcp tool calls look(mode="angles", views=["top"]) and get_scene_info(fields=["topology"]) for review and triangle counts. *(doc, medium; claude-blender-mcp)*
- c7: Linked duplicates via obj.copy() without copying data keep one fix updating all copies; advises reading export operator arguments since they change between versions. *(doc, medium; bpy-scripting-headless)*

## Numbers
- n1: **Doorway size**: 1.2–1.5 m wide, 2.4–3 m tall Human-scale FPS/TPS default; wider than real life
- n2: **Cover height**: 1.0 m crouch / 2.0 m full Level design defaults
- n3: **Corridor width**: 3–4 m Level design default

## Techniques
- t1: **Grey-box blockout**: Build rooms, paths, heights and sightlines from simple geometry before art. One collection per area. Snap positions to module size in scripts.
- t2: **Linked duplicates for modular kits**: Use obj.copy() without copying mesh data, or collection instances, so edits to one piece propagate to all copies.

## Points to
- https://github.com/ahujasid/mcp-for-blender
