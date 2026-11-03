---
type: research-source
id: web-fc6f1b67db
title: "Roblox docs: avatar/layered-accessories/import"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/avatar/layered-accessories/import.md"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0014
relevance: 2
density: medium
tags: ["research-source", "web", "automation-and-creator-workflows", "avatar-ugc-accessories", "claude-blender-ai", "mesh-texture-limits"]
---
# web-fc6f1b67db

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Official Roblox doc on importing layered clothing accessories (.fbx/.gltf) via Studio's Importer, fixing textures via Asset Manager and PBR SurfaceAppearance maps, then converting to Accessory with the Accessory Fitting Tool. Relevant only to the Studio side of the pipeline; no Blender, Claude, or bpy content.

## Claims
- c1: Roblox Importer imports a layered accessory .fbx or .gltf as a Model; textures become SurfaceAppearance or MeshPart.TextureID automatically. *(doc, high; avatar-ugc-accessories)*
- c2: Shoes must be converted as separate left and right layered accessories, then grouped as a Model before upload. *(doc, high; avatar-ugc-accessories)*
- c3: Accessory Fitting Tool (Avatar tab > Accessory): select MeshPart, Next, set asset type to Clothing with a clothing type, then Generate MeshPart Accessory. *(doc, high; avatar-ugc-accessories)*
- c4: If textures fail to import, upload via Asset Manager; PBR maps go into SurfaceAppearance: ColorMap=_ALB, MetalnessMap=_MTL, NormalMap=_NOR, RoughnessMap=_RGH. *(doc, high; mesh-texture-limits)*
- c5: Large cage changes may require re-exporting from third-party modeling software; minor cage adjustments can be made in the AFT. *(doc, high; avatar-ugc-accessories)*
- c6: Assets must also meet layered accessory specifications, not just general 3D requirements, or errors appear later in the workflow. *(doc, medium; avatar-ugc-accessories)*
- c7: Converted Accessory can be equipped via HumanoidDescription, published to Marketplace, or saved to Toolbox/Creator Store. *(doc, high; automation-and-creator-workflows)*
- c8: Source does not mention Blender, Claude, blender-mcp, or bpy; it covers only Studio-side import and AFT conversion. *(doc, high; claude-blender-ai)*

## Techniques
- t1: **Layered accessory import and convert**: 1. Home > Import, pick .fbx/.gltf. 2. Import to get Model. 3. Avatar > Accessory opens AFT. 4. Select MeshPart, Next. 5. Asset type Clothing + type. 6. Test on sample characters. 7. Generate MeshPart Accessory.
- t2: **Manual PBR texture assignment**: Add SurfaceAppearance to MeshPart; set ColorMap (_ALB), MetalnessMap (_MTL), NormalMap (_NOR), RoughnessMap (_RGH) from asset dropdown after moderation clears.

## Quotes (brief, for attribution)
> Import a layered accessory .fbx or .gltf file into Studio as a Model object and convert it into an Accessory object.  (create.roblox.com)
> For shoes, you must convert the left shoe and the right shoe as separate layered accessories.  (create.roblox.com)

## Points to
- https://create.roblox.com/docs/avatar/layered-accessories/specifications
- https://create.roblox.com/docs/avatar/accessory-fitting-tool
- https://create.roblox.com/docs/projects/assets/manager
- https://create.roblox.com/docs/marketplace/publish-to-marketplace
