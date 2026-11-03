---
type: research-source
id: gh-sandraschi-blender-mcp-f-docs-blender-BLENDER_MCP_FUNCTIONALITY_PLAN.md
title: "sandraschi/blender-mcp/docs/blender/BLENDER_MCP_FUNCTIONALITY_PLAN.md"
source_type: "github"
creator: "sandraschi"
url: "https://github.com/sandraschi/blender-mcp/blob/HEAD/docs/blender/BLENDER_MCP_FUNCTIONALITY_PLAN.md"
published: "2026-10-25"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0030
relevance: 2
density: medium
tags: ["research-source", "github", "bpy-scripting-headless", "claude-blender-mcp", "common-mistakes-fixes", "creator-workflows", "procedural-generation", "rigging-animation", "roblox-export-settings", "roblox-import-pipeline", "texturing-baking-uv"]
---
# gh-sandraschi-blender-mcp-f-docs-blender-BLENDER_MCP_FUNCTIONALITY_PLAN.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Feature inventory for sandraschi's blender-mcp server (FastMCP 2.12), grouped into portmanteau tools for modelling, lighting, rigging, physics, UV, rendering and export. It has no Roblox-specific export or import path (exports target Unity and VRChat). Tool-count and test claims are self-reported and internally inconsistent.

## Claims
- c1: Server is built on FastMCP 2.12 and exposes grouped 'portmanteau' tools (e.g. blender_mesh, blender_rigging) with sub-operations passed as parameters. *(doc, high; claude-blender-mcp)*
- c2: Doc states 50 working tools across 19 categories, but its Conclusion section says 20 functional tools; the counts contradict each other. *(doc, high; claude-blender-mcp)*
- c3: Tested against Blender 4.4.0; only list_scenes has a logged live run (0.56 s), so most 'WORKING' labels lack shown evidence. *(doc, medium; claude-blender-mcp)*
- c4: Export tools list only Unity and VRChat targets; no Roblox export preset, scale or axis handling is described. *(doc, high; roblox-export-settings)*
- c5: Import covers FBX, OBJ, GLTF, STL, PLY, COLLADA, USD, Alembic and BVH; no Roblox-specific import step is mentioned. *(doc, high; roblox-import-pipeline)*
- c6: Each tool call runs a Blender script via a handler layer (log shows 'Blender script completed successfully' with captured stdout), not a live socket-only API. *(doc, medium; bpy-scripting-headless)*
- c7: UV tools include unwrap, smart_project, cube/cylinder/sphere projection and reset_uvs; a bake_texture operation is listed but no bake settings or texture size limits are given. *(doc, medium; texturing-baking-uv)*
- c8: Rigging tool offers create_armature, add_bone, create_bone_ik and create_basic_rig (biped); no weight painting or animation-export-to-Roblox steps are documented. *(doc, high; rigging-animation)*
- c9: Procedural textures (noise, voronoi, musgrave, wave, checker, brick, gradient) and furniture generators are provided; no geometry-nodes or text-to-3D (Hunyuan/Rodin/Meshy) support is listed. *(doc, medium; procedural-generation)*
- c10: Transform tools include apply_transform and reset_transform, which bear on scale and pivot issues, but the doc gives no guidance on unit or scale conventions. *(doc, low; common-mistakes-fixes)*
- c11: Doc labels its own feature set as 'Complete' and 'Professional', with no benchmarks or limits; treat as author claim, not verified. *(opinion, medium; creator-workflows)*

## Numbers
- n1: **Total tools claimed**: 50 tools / 19 categories Opening section; conflicts with Conclusion
- n2: **Conclusion tool count**: 20 functional tools Conclusion section of same doc
- n3: **Blender version tested**: 4.4.0 Live test log and implementation status
- n4: **list_scenes run time**: 0.56 s Logged live run, scene with 3 objects
- n5: **Furniture types**: 8 generators create_chair through create_stool in blender_furniture

## Techniques
- t1: **Portmanteau tool grouping**: Group related operations (e.g. create_cube, create_sphere) under one MCP tool with an operation parameter to limit tool count; doc says this is the approach for new categories.
- t2: **Handler-to-script execution**: MCP tool calls Python handler in src/blender_mcp/handlers/, which runs a Blender script and returns stdout as the tool result.

### Code: Tool signature pattern the doc requires (FastMCP 2.12, lazy handler import)
```python
@app.tool
async def tool_name(param1: type = default_value, param2: type = default_value) -> str:
    """
    Brief description of what the tool does.

    Args:
        param1: Description of first parameter
    Returns:
        Description of return value
    """
    from blender_mcp.handlers.handler_module import handler_function

    return await handler_function(param1=param1, param2=param2)
```

## Contradictions flagged
- Total of 50 working tools across 19 categories (vs Same document's Conclusion: 20 functional tools, 20/20 implemented)
- Export & Import covers 'All major 3D formats' with 'Complete Blender MCP Server Working' (vs Only a single list_scenes run is logged as live evidence in Testing Results)

## Points to
- https://github.com/sandraschi/blender-mcp
- FastMCP 2.12
- Blender 4.4.0
