---
type: research-source
id: web-90eaed384c
title: "Roblox docs: art/accessories/creating/importing"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/art/accessories/creating/importing.md"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0008
relevance: 3
density: low
tags: ["research-source", "web", "common-mistakes-fixes", "roblox-import-pipeline"]
---
# web-90eaed384c

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox creator doc on importing a Blender-made accessory (t-shirt) into Studio. Export as .fbx, then use Studio's Importer (Home tab > Import) to get a Class.Model with textures applied to MeshPart.TextureID. Fallback for missing textures: upload image via Asset Manager and set TextureID manually. Thin on Blender specifics; no blender-mcp or bpy content.

## Claims
- c1: Studio's Importer (Home tab > Import) loads a .fbx, shows a preview of the layered accessory, and imports it as a Class.Model. *(doc, high; roblox-import-pipeline)*
- c2: Imported textures are applied as Class.MeshPart.TextureID on the resulting MeshPart. *(doc, high; roblox-import-pipeline)*
- c3: If textures fail to load, upload the image via Asset Manager and wait for moderation to clear it before using it. *(doc, high; common-mistakes-fixes)*
- c4: If Asset Manager is inaccessible, the doc says to save and publish the game first. *(doc, high; common-mistakes-fixes)*
- c5: Manual texture fix: select the MeshPart inside the imported Model, then enter the texture image asset ID in the TextureID property. *(doc, high; common-mistakes-fixes)*

## Techniques
- t1: **Manual TextureID fix**: Upload image in Asset Manager, wait for moderation, select the MeshPart under the imported Model, paste the texture asset ID into TextureID.

## Points to
- https://create.roblox.com/docs/art/accessories/creating/exporting
- https://create.roblox.com/docs/projects/assets/manager
