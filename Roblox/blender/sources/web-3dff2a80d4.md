---
type: research-source
id: web-3dff2a80d4
title: "Roblox docs: avatar/rigid-accessories/import"
source_type: "web"
creator: "create.roblox.com"
url: "https://raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/avatar/rigid-accessories/import.md"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0026
relevance: 2
density: medium
tags: ["research-source", "web", "automation-and-creator-workflows", "avatar-ugc-accessories", "blender-roblox-export-import", "claude-blender-ai", "mesh-texture-limits"]
---
# web-3dff2a80d4

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox creator doc on importing rigid accessory FBX/glTF into Studio, fixing missing textures via SurfaceAppearance with _ALB/_MTL/_NOR/_RGH maps, and fitting with the Accessory Fitting Tool to generate an Accessory. No Blender, Claude, or bpy content; relevant only as the Roblox-side end of the pipeline.

## Claims
- c1: Studio Importer accepts .fbx or .gltf rigid accessory files; Import click creates a Class.Model with textures applied as SurfaceAppearance or MeshPart.TextureID. *(doc, high; blender-roblox-export-import)*
- c2: If textures fail to import, manual fix: upload images via Asset Manager, wait for moderation, add SurfaceAppearance under MeshPart, set ColorMap=_ALB, MetalnessMap=_MTL, NormalMap=_NOR, RoughnessMap=_RGH. *(doc, high; mesh-texture-limits)*
- c3: Model must be fitted with the Accessory Fitting Tool (Avatar tab > Accessory): select MeshPart as Part, set Asset Type to Accessory with attachment location and body scale, then pick a mannequin humanoid. *(doc, high; avatar-ugc-accessories)*
- c4: AFT preview window is the accurate fit check; the viewport clothing mannequin does not accurately show how rigid accessories attach. *(doc, high; avatar-ugc-accessories)*
- c5: Clicking Generate MeshPart Accessory converts the fitted model into a Class.Accessory, usable via HumanoidDescription, Marketplace upload, Toolbox, or Creator Store. *(doc, high; automation-and-creator-workflows)*
- c6: Imported asset should meet Roblox rigid accessory specifications; Importer error checks do not guarantee avatar-ready output, errors can surface later in workflow. *(doc, high; avatar-ugc-accessories)*
- c7: Source does not mention Blender, blender-mcp, Claude, or bpy scripting; it covers only Studio-side import. *(doc, high; claude-blender-ai)*

## Techniques
- t1: **Rigid accessory import and convert**: Home > Import .fbx/.gltf, then Avatar > Accessory, select MeshPart, set asset type and body scale, choose mannequin, adjust with Move/Scale/Rotate, click Generate MeshPart Accessory.
- t2: **Manual texture reattachment**: Upload images in Asset Manager, wait for moderation, add SurfaceAppearance to MeshPart, assign ColorMap, MetalnessMap, NormalMap, RoughnessMap from _ALB/_MTL/_NOR/_RGH.

## Points to
- https://create.roblox.com/docs/avatar/rigid-accessories/specifications
- https://create.roblox.com/docs/avatar/accessory-fitting-tool
- https://create.roblox.com/docs/projects/assets/manager
- https://create.roblox.com/docs/projects/assets/toolbox
- https://create.roblox.com/docs/production/creator-store
