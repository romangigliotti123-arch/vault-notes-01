---
type: research-source
id: web-1f7dfe0e20
title: "DevForum thread 2659618"
source_type: "web"
creator: "devforum.roblox.com"
url: "https://devforum.roblox.com/raw/2659618"
published: ""
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0015
relevance: 2
density: medium
tags: ["research-source", "web", "avatar-ugc-accessories", "roblox-import-pipeline", "texturing-baking-uv"]
---
# web-1f7dfe0e20

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Forum tutorial (RobertCorbet, 2023) on a manual Blender sculpting-to-Roblox pipeline: primitive low-poly modeling, UV mapping, MultiRes high-poly sculpting, baking, Substance Painter texturing (PBR SurfaceAppearance vs Baked Lighting TextureId), and MeshPart/Accessory Fitting Tool upload. No Claude, blender-mcp, or bpy scripting content; largely off-topic for the requested subject.

## Claims
- c1: Subdivide high-poly via MultiRes to about 4-6 levels; author uses 5 on most objects; face count grows exponentially with level. *(opinion, medium; texturing-baking-uv)*
- c2: Bake high-poly onto low-poly by exporting both as separate files and adding the high-poly to the baked maps. *(experience, medium; texturing-baking-uv)*
- c3: PBR (SurfaceAppearance) is used only for 3D clothing in UGC; typical accessories must use Baked Lighting via TextureId. *(opinion, medium; avatar-ugc-accessories)*
- c4: Roblox (Surface Appearance) preset in Substance Painter exports 4 matching PBR texture maps. *(doc, medium; texturing-baking-uv)*
- c5: Accessory Fitting Tool rigs a MeshPart into a wearable accessory; UGC upload via right-click 'Upload to Roblox' requires the UGC feature flag enabled. *(experience, low; avatar-ugc-accessories)*
- c6: UV islands should be near-closed shapes packed into a tight square, with area proportional to 3D surface area. *(opinion, medium; texturing-baking-uv)*
- c7: Create a MeshPart, set MeshId to the low-poly mesh, and add a SurfaceAppearance child or set TextureId to the baked image. *(experience, medium; roblox-import-pipeline)*

## Numbers
- n1: **MultiRes subdivision level**: 4-6 (author uses 5) Sculpt high-poly from low-poly MultiRes; higher levels add faces exponentially
- n2: **Substance Painter price**: $20 USD Listed in tutorial software list

## Techniques
- t1: **Primitive-based low-poly modeling**: Start from primitive matching object (e.g., Cylinder for headwear); extrude, bevel, scale, subdivide until shape fits.
- t2: **MultiRes sculpt-and-bake**: Apply Multi Resolution modifier to low-poly, subdivide ~5 levels, sculpt seams/creases, export high and low meshes, bake high onto low.

## Quotes (brief, for attribution)
> Do not spam the button.  (devforum.roblox.com)

## Points to
- devforum.roblox.com/t/paintnet-basic-clothing-and-design/805431
- substance3d-painter (Adobe)
- blender.org
- Paint.NET
