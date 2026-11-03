---
type: research-source
id: gh-sandraschi-blender-mcp-f-docs-blender-BLENDER_MCP_FUNCTIONALITY_PLAN_NEW.md
title: "sandraschi/blender-mcp/docs/blender/BLENDER_MCP_FUNCTIONALITY_PLAN_NEW.md"
source_type: "github"
creator: "sandraschi"
url: "https://github.com/sandraschi/blender-mcp/blob/HEAD/docs/blender/BLENDER_MCP_FUNCTIONALITY_PLAN_NEW.md"
published: "2026-10-25"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0024
relevance: 1
density: low
tags: ["research-source", "github", "bpy-scripting-headless", "claude-blender-mcp", "common-mistakes-fixes", "open-cloud-automation", "procedural-generation", "rigging-animation", "texturing-baking-uv"]
---
# gh-sandraschi-blender-mcp-f-docs-blender-BLENDER_MCP_FUNCTIONALITY_PLAN_NEW.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Planning doc for sandraschi's blender-mcp server (FastMCP 2.12). Describes a 15-tool "portmanteau" design where each tool takes an operation parameter, lists planned operations per category, and gives implementation status. It has no Roblox content, no bpy/export pipeline detail, and no measured results. Status claims are internally inconsistent.

## Claims
- c1: Server plans 15 portmanteau tools, each a single MCP tool with an operation parameter, instead of 150+ separate tools. *(doc, high; claude-blender-mcp)*
- c2: Doc says 3 tools are implemented (blender_scene, blender_materials, blender_furniture); 3/15 status repeated at the end. *(doc, high; claude-blender-mcp)*
- c3: blender_scene is marked fully implemented with 12 operations (create, list, clear, set_active, collections, lighting, camera, render settings). *(doc, medium; claude-blender-mcp)*
- c4: blender_materials is marked complete with 8 operations (fabric, metal, wood, glass, ceramic, plastic, emissive, assign). *(doc, medium; claude-blender-mcp)*
- c5: Status is contradictory: blender_furniture is 'Completed' in the summary but 'PLANNED' in its section; blender_mesh, lighting, camera listed as 'In progress' yet also 'PLANNED' in their sections. *(doc, high; claude-blender-mcp)*
- c6: Planned blender_io tool covers import/export of FBX, OBJ, glTF plus batch_export; no Roblox-specific export settings are described. *(doc, high; claude-blender-mcp)*
- c7: Testing plan: unit tests for Pydantic schemas need no Blender; integration tests run real Blender with temporary files; no mention of background mode or bpy version. *(doc, medium; bpy-scripting-headless)*
- c8: Planned blender_furniture and blender_mesh cover primitives, text, curves, NURBS surfaces, room and building generation; no text-to-3D (Hunyuan, Rodin, Meshy) mentioned. *(doc, medium; procedural-generation)*
- c9: Planned blender_animation covers armatures, automated character rigging, walk cycles and animation export, but none are implemented per the doc. *(doc, medium; rigging-animation)*
- c10: Planned blender_textures covers procedural textures, image loading, UV unwrap, island packing and baking; not implemented per the doc. *(doc, medium; texturing-baking-uv)*
- c11: Planned blender_advanced includes validate_geometry (mesh validation) and optimize_scene; no details on what is checked. *(doc, low; common-mistakes-fixes)*
- c12: Doc describes no Roblox, Open Cloud, Rojo or plugin integration. *(doc, high; open-cloud-automation)*

## Numbers
- n1: **planned portmanteau tools**: 15 (vs 150+ separate tools avoided) 
- n2: **implemented tools**: 3 of 15 
- n3: **blender_scene operations**: 12 
- n4: **blender_materials operations**: 8 
- n5: **FastMCP version**: 2.12 

## Techniques
- t1: **Portmanteau tool design**: Group related operations into one MCP tool per category; dispatch on an operation string argument (e.g. 'create','list') to async handler functions; keep handlers in src/blender_mcp/handlers/.

### Code: Portmanteau tool pattern used by the planned FastMCP 2.12 server
```python
@app.tool
async def blender_category(
    operation: str = "default_operation",
    # ... operation-specific parameters
) -> str:
    if operation == "create":
        return await handler_create_function(params)
    elif operation == "list":
        return await handler_list_function()
```

## Quotes (brief, for attribution)
> Instead of 150+ separate tools, we use portmanteau tools - single tools with sub-commands that handle multiple related operations  (sandraschi)
> Current Status: 3/15 tools implemented  (sandraschi)

## Contradictions flagged
- blender_furniture listed as Completed in Implementation Status summary (vs its own section marked 🔄 PLANNED)
- blender_mesh, blender_lighting, blender_camera 'In Progress' (vs their sections marked 🔄 PLANNED)
- Current Implementation: 3 working tools (vs Implementation Status list includes blender_furniture as completed alongside scene and materials; ambiguous count)

## Points to
- FastMCP 2.12 (framework named in doc)
- src/blender_mcp/handlers/ and src/blender_mcp/tools/{category}/ (repo layout)
