---
type: research-source
id: off-art_accessories_creating_importing
title: "Roblox Creator Docs: art_accessories_creating_importing"
source_type: "web"
creator: "create.roblox.com"
url: "https://create.roblox.com/docs/art/accessories/creating/importing"
published: "2026-10-31"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0008
relevance: 2
density: low
tags: ["research-source", "web", "avatar-ugc-accessories", "blender-roblox-export-import"]
---
# off-art_accessories_creating_importing

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Short Roblox doc page on importing a Blender-made t-shirt .fbx into Studio via the Importer, which creates a Class.Model with textures on MeshPart.TextureID. Covers manual texture fallback through Asset Manager (requires moderation clearance, then setting TextureID). Says nothing on Blender scripting, blender-mcp, scale, axes, or rigging.

## Claims
- c1: Roblox docs: after making a t-shirt in Blender, export as .fbx, then use Studio Importer (Home tab > Import) to load it as a Class.Model with textures applied to MeshPart.TextureID. *(doc, high; blender-roblox-export-import)*
- c2: If textures fail to load on Importer, manually upload image via Asset Manager Import, wait for moderation, then set MeshPart TextureID to the texture asset ID. *(doc, high; blender-roblox-export-import)*
- c3: Asset Manager import requires game saved and published first if Asset Manager is inaccessible. *(doc, high; blender-roblox-export-import)*
- c4: Importer preview shows the layered accessory before import, implying layered clothing is handled by the Importer. *(doc, medium; avatar-ugc-accessories)*

## Techniques
- t1: **Studio Importer FBX import**: Home tab > Import, select .fbx, review preview, click Import; result is Class.Model with textures applied.
- t2: **Manual texture fix**: Asset Manager > Import image; after moderation, select child MeshPart, set TextureID to texture asset ID.

## Quotes (brief, for attribution)
> import the .fbx using Studio's Importer tool to add the t-shirt to your project as a Class.Model.  (create.roblox.com)

## Points to
- https://create.roblox.com/docs/art/accessories/creating/exporting
- https://create.roblox.com/docs/art/accessories/creating/converting
- https://create.roblox.com/docs/projects/assets/manager
