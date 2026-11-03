---
type: research-source
id: gh-sandraschi-blender-mcp-f-assets-prompts-3d_creation_assistant.md
title: "sandraschi/blender-mcp/assets/prompts/3d_creation_assistant.md"
source_type: "github"
creator: "sandraschi"
url: "https://github.com/sandraschi/blender-mcp/blob/HEAD/assets/prompts/3d_creation_assistant.md"
published: "2026-10-25"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0020
relevance: 1
density: low
tags: ["research-source", "github", "blender-roblox-export-import", "claude-blender-ai", "mesh-texture-limits"]
---
# gh-sandraschi-blender-mcp-f-assets-prompts-3d_creation_assistant.md

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
A system-prompt-style doc for a Blender MCP creation assistant. It sets a persona and a five-step workflow (understand, break down, execute, iterate, deliver) and lists generic Blender capabilities. It has an error-handling section. It has no Roblox content, no bpy code, no version numbers and no export settings, so it is of little use for the Blender-to-Roblox pipeline.

## Claims
- c1: The blender-mcp assistant prompt claims access to Blender automation tools for scene creation, materials, lighting, camera, animation, rendering and batch processing. *(doc, high; claude-blender-ai)*
- c2: Recommended workflow: understand vision, break down request, execute systematically, iterate with feedback, then deliver render and next steps. *(doc, high; claude-blender-ai)*
- c3: On failure the prompt says to diagnose Blender version, available tools and resource constraints, then offer simpler alternatives. *(doc, high; claude-blender-ai)*
- c4: Prompt advises starting with basic shapes, using subdivisions for detail and matching material properties to object function; no numeric limits given. *(doc, medium; mesh-texture-limits)*
- c5: The source contains no Roblox-specific guidance on FBX/glTF export, scale, axes, MeshPart import or the Roblox Blender plugin. *(doc, high; blender-roblox-export-import)*

## Techniques
- t1: **Five-step iterative creation loop**: Clarify style and purpose, split request into objects/materials/lighting/composition, build base shapes first, add detail, show progress and take feedback, then render and suggest next steps.
- t2: **Failure diagnosis fallback**: Check Blender version, available tools and resource limits; offer a simpler technique; explain the likely fix to the user.

## Quotes (brief, for attribution)
> Start simple, add complexity - Begin with basic shapes, then refine  (sandraschi)

## Points to
- https://github.com/sandraschi/blender-mcp
