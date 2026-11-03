---
type: research-source
id: web-f47ef8b226
title: "Roblox docs: avatar/makeup/specifications"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/avatar/makeup/specifications.md"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0012
relevance: 2
density: medium
tags: ["research-source", "web", "avatar-ugc-accessories", "blender-roblox-export-import", "mesh-texture-limits", "rigging-animation"]
---
# web-f47ef8b226

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox doc for makeup specs (not Blender-specific): required objects (TransferTarget_ head and cage, TransferTexture_Eyes/Lips/Face_NN regions), 4K in-game vs 1K Marketplace texture limits, and optional eyebrow/eyelash layered accessories with inner/outer cages and 4k tri budgets. Points to Blender and Maya export settings pages (not included). Little on bpy, Claude, or blender-mcp.

## Claims
- c1: Makeup template file must contain a head mesh and a cage mesh, both named with prefix "TransferTarget_". *(doc, high; blender-roblox-export-import)*
- c2: TransferTexture mesh objects are required per region using naming like TransferTexture_Eyes_01, TransferTexture_Lips_01, TransferTexture_Face_01; increment the number for extra regions. *(doc, high; blender-roblox-export-import)*
- c3: Avoid renaming or deleting the data model of Roblox's provided makeup template head, or import may break. *(doc, high; blender-roblox-export-import)*
- c4: Makeup texture limit is 4K for in-game makeup creation, but 1K for makeup uploaded to the Marketplace. *(doc, high; mesh-texture-limits)*
- c5: Makeup textures must also meet general accessory texture specs and PBR texture guidance. *(doc, medium; mesh-texture-limits)*
- c6: Eyebrows and eyelashes are optional layered accessories; each needs its own inner and outer cage. *(doc, high; avatar-ugc-accessories)*
- c7: Eye accessories (eyebrows/eyelashes) are limited to 4k triangles each and must stay within layered accessory max dimensions. *(doc, high; avatar-ugc-accessories)*
- c8: Eyebrows and eyelashes can use automatic skinning with special skinning transfer joints. *(doc, medium; rigging-animation)*

## Numbers
- n1: **In-game makeup texture limit**: 4K 
- n2: **Marketplace makeup texture limit**: 1K 
- n3: **Eye accessory triangle budget (each)**: 4k triangles 

## Techniques
- t1: **Makeup template setup**: Start from Roblox's makeup template head; keep its data model; name head and cage with TransferTarget_; name each region TransferTexture_<Region>_<NN>.

## Quotes (brief, for attribution)
> Makeup is a cosmetic look made up of multiple facial textures and optional eyebrow and eyelashes.  (create.roblox.com)
> There is a 4K texture limit for in-game makeup creation. There is a 1K texture limit for makeup that you upload to the Marketplace.  (create.roblox.com)

## Points to
- https://github.com/Roblox/avatar/tree/main/Makeup
- ../../art/modeling/texture-specifications.md
- ../../art/modeling/surface-appearance.md
- ../../avatar/automatic-skinning-transfer.md
- ../../avatar/layered-accessories/specifications.md
