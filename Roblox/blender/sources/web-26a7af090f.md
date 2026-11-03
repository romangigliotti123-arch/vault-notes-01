---
type: research-source
id: web-26a7af090f
title: "Roblox docs: art/characters/creating/index"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/art/characters/creating/index.md"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0008
relevance: 2
density: low
tags: ["research-source", "web", "avatar-ugc-accessories", "blender-roblox-export-import", "claude-blender-ai"]
---
# web-26a7af090f

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox doc introducing avatar body creation in Blender from supplied template models. Covers template selection, sculpting, texture paint, cage-mesh editing, cleanup, and Studio export. Targets Blender 3.4+. Contains no Claude, MCP, bpy scripting, or specific triangle, texture, or export-setting numbers.

## Claims
- c1: Roblox supplies downloadable template models for custom avatar bodies; templates skip manual armature setup, rigging, skinning, and face-animation configuration. *(doc, high; blender-roblox-export-import)*
- c2: Recommended custom-avatar workflow: pick template, sculpt non-destructively, paint textures in Blender texture paint, edit template cage mesh objects, clean up, export to Studio. *(doc, high; avatar-ugc-accessories)*
- c3: Guide targets Blender 3.4+; other DCC programs can follow the same general workflow with equivalent tools. *(doc, high; blender-roblox-export-import)*
- c4: Caging is done by editing the template's cage mesh objects, the key step for fitting the body to the avatar system. *(doc, medium; avatar-ugc-accessories)*
- c5: Source does not mention Claude, blender-mcp, bpy, or any scripting or MCP workflow; it covers only manual Blender template editing. *(doc, high; claude-blender-ai)*

## Numbers
- n1: **Blender version**: 3.4+ minimum version named for the template tutorial

## Techniques
- t1: **Template-based avatar body editing**: Start from Roblox template model with preconfigured armature/rig/face setup. Sculpt, paint textures in Blender, edit cage meshes, clean up, export to Studio.

## Points to
- https://www.blender.org/download/releases/3-4/
- /art/characters/creating/template-files

## Visual notes
Two images: starting template model and example model after modifications.
