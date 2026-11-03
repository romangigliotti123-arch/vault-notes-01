---
type: research-source
id: web-7a25e5ca8a
title: "Roblox docs: art/overview-dcc"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/art/overview-dcc.md"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0011
relevance: 2
density: low
tags: ["research-source", "web", "automation-and-creator-workflows", "blender-roblox-export-import", "mesh-texture-limits", "other"]
---
# web-7a25e5ca8a

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox staff overview of third-party DCC workflow: create assets in external tools (Blender, Maya, Cinema 4D, Photoshop, Substance Painter, Audacity, Reaper), export a common file type, then import to Studio. Lists Studio import paths for models (.gltf/.fbx/.obj via Importer, Roblox Blender plugin), textures and sounds (Asset Manager formats), and video (.mp4/.mov). Does not cover Blender scripting, MCP, scale/axes, or rigging.

## Claims
- c1: Studio's Importer supports .gltf, .fbx, and .obj model file formats. *(doc, high; blender-roblox-export-import)*
- c2: Roblox Blender plugin connects modeling software to Studio and lets creators upload modeling assets directly between applications. *(doc, high; blender-roblox-export-import)*
- c3: Uploaded models and textures must follow Studio's modeling and texture specifications; the page gives no numeric limits. *(doc, high; mesh-texture-limits)*
- c4: Asset Manager supports .png, .jpg, .gif, .tga, .bmp images and .ogg, .mp3, .flac, .wav sounds, with bulk file import. *(doc, high; automation-and-creator-workflows)*
- c5: Video assets can be imported as .mp4 or .mov if listed requirements are met. *(doc, high; other)*
- c6: Roblox performs asset moderation on upload and can moderate assets after initial upload. *(doc, high; automation-and-creator-workflows)*

## Numbers
- n1: **Model import formats**: .gltf, .fbx, .obj 
- n2: **Image formats**: .png, .jpg, .gif, .tga, .bmp 
- n3: **Sound formats**: .ogg, .mp3, .flac, .wav 
- n4: **Video formats**: .mp4, .mov 

## Techniques
- t1: **Standard DCC-to-Studio workflow**: Create asset in third-party tool, export common file type (fbx/gltf/obj), import via Studio Importer; or use Roblox Blender plugin for direct upload.

## Quotes (brief, for attribution)
> In most workflows, you create custom assets in third-party software, export them as a common file type, and then import the file into Studio.  (create.roblox.com)

## Points to
- https://www.blender.org/
- https://devforum.roblox.com/tags/c/resources/roblox-staff/278/art
- ../art/modeling/roblox-blender-plugin.md
- ../studio/importer.md
- ../art/modeling/specifications.md
