---
type: research-source
id: web-c2b8df4406
title: "Roblox docs: projects/assets/manager"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/projects/assets/manager.md"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0021
relevance: 1
density: low
tags: ["research-source", "web", "blender-roblox-export-import"]
---
# web-c2b8df4406

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox Creator Docs page for Studio's Asset Manager: inventories, folder limits, move/search operators, and quick actions. It does not cover Blender, Claude, blender-mcp, bpy, FBX/glTF export, or mesh/rig rules. Only tangential: bulk-imported meshes go to moderation, and Copy Asset ID feeds MeshPart.MeshId.

## Claims
- c1: Assets bulk-imported via Asset Manager enter the moderation queue and are added to the owning user/group inventory only after approval. *(doc, high; blender-roblox-export-import)*
- c2: Asset Manager 'Copy Asset ID' copies an asset ID for pasting into MeshPart.MeshId, relevant to placing imported meshes. *(doc, medium; blender-roblox-export-import)*

## Numbers
- n1: **folders per account or root inventory**: 50,000 
- n2: **max nesting levels**: 20 
- n3: **assets per folder**: 20,000 

## Points to
- https://create.roblox.com/docs/studio/importer
- https://create.roblox.com/docs/parts/meshes
