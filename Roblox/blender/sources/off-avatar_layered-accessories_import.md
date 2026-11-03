---
type: research-source
id: off-avatar_layered-accessories_import
title: "Roblox Creator Docs: avatar_layered-accessories_import"
source_type: "web"
creator: "create.roblox.com"
url: "https://create.roblox.com/docs/avatar/layered-accessories/import"
published: "2026-10-31"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0014
relevance: 3
density: medium
tags: ["research-source", "web", "automation-and-creator-workflows", "avatar-ugc-accessories", "claude-blender-ai", "mesh-texture-limits"]
---
# off-avatar_layered-accessories_import

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox Creator Docs page on importing layered clothing accessories into Studio via the Importer (.fbx/.gltf), manually fixing textures via Asset Manager (SurfaceAppearance PBR map assignment), and converting the Model to an Accessory with the Accessory Fitting Tool (Clothing asset type, test, Generate MeshPart Accessory). Shoes must be converted separately as left and right. Little on Blender specifically.

## Claims
- c1: Layered accessory .fbx or .gltf is imported via Studio Importer (Home > Import) as a Model; textures apply as SurfaceAppearance or MeshPart.TextureID. *(doc, high; avatar-ugc-accessories)*
- c2: Left and right shoes must each be converted to separate layered accessories with the AFT before grouping as a Model for upload. *(doc, high; avatar-ugc-accessories)*
- c3: Accessory Fitting Tool: select MeshPart, Next, set asset type to Clothing and pick clothing type, Next, test on sample characters/animations, then Generate MeshPart Accessory. *(doc, high; avatar-ugc-accessories)*
- c4: Minor cage adjustments can be made in the AFT; larger cage changes require returning to modeling software and re-exporting. *(doc, high; avatar-ugc-accessories)*
- c5: If textures fail to load, upload images via Asset Manager, wait for moderation, then set MeshPart.TextureID (single texture) or add SurfaceAppearance with ColorMap (_ALB), MetalnessMap (_MTL), NormalMap (_NOR), RoughnessMap (_RGH). *(doc, high; mesh-texture-limits)*
- c6: Asset Manager import requires saving and publishing the game first if the Asset Manager is inaccessible. *(doc, medium; automation-and-creator-workflows)*
- c7: Generated Accessory can be published to Marketplace, equipped via HumanoidDescription, or saved to Toolbox/Creator Store. *(doc, high; avatar-ugc-accessories)*
- c8: Page does not mention Blender, blender-mcp, or bpy; no Claude-related content. *(doc, high; claude-blender-ai)*

## Numbers
- n1: **PBR texture suffixes**: _ALB, _MTL, _NOR, _RGH 

## Techniques
- t1: **Layered accessory conversion with AFT**: Import FBX/glTF, select MeshPart in AFT, set Clothing type, preview/test animations, tweak cage, Generate MeshPart Accessory.
- t2: **Manual PBR texture assignment**: Upload textures in Asset Manager, add SurfaceAppearance to MeshPart, assign ColorMap/MetalnessMap/NormalMap/RoughnessMap.

## Quotes (brief, for attribution)
> Use the Importer to add third-party models to Studio before using the Accessory Fitting Tool to convert the model to an Accessory.  (create.roblox.com)
> For shoes, you must convert the left shoe and the right shoe as separate layered accessories.  (create.roblox.com)

## Points to
- https://create.roblox.com/docs/avatar/layered-accessories/specifications
- https://create.roblox.com/docs/avatar/accessory-fitting-tool
- https://create.roblox.com/docs/projects/assets/manager
- https://create.roblox.com/docs/marketplace/publish-to-marketplace
