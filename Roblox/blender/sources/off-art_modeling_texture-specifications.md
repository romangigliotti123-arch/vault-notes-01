---
type: research-source
id: off-art_modeling_texture-specifications
title: "Roblox Creator Docs: art_modeling_texture-specifications"
source_type: "web"
creator: "create.roblox.com"
url: "https://create.roblox.com/docs/art/modeling/texture-specifications"
published: "2026-10-31"
retrieved: 2026-11-01
extracted_by: "haiku"
extraction_cost_usd: 0.0016
relevance: 3
density: high
tags: ["research-source", "web", "avatar-ugc-accessories", "blender-roblox-export-import", "mesh-texture-limits"]
---
# off-art_modeling_texture-specifications

Personal-use research note. Brief quotes only, with attribution; see the original at the URL above.

## Summary
Roblox Creator Docs spec page for textures made outside Studio. Covers allowed file formats (png/jpg/tga/bmp), resolution guidance by stud size, one material per mesh, PBR map bit depths (RGB albedo/normal, grayscale roughness/metalness/emissive), PBR texel budget per 2×2×2 unit, and UV rules (single set, 0:1 space). Does not cover Blender scripting, blender-mcp, or export settings directly.

## Claims
- c1: Texture files uploaded separately in Studio must be .png, .jpg, .tga, or .bmp. *(doc, high; blender-roblox-export-import)*
- c2: Roblox supports texture resolutions up to 4096×4096 (4K); engine starts with lower-quality versions and ramps up based on device resources. *(doc, high; mesh-texture-limits)*
- c3: Guideline: 5×5 stud objects use 256×256; 10×10 use 512×512; 20×20 use 1024×1024 textures. *(doc, high; mesh-texture-limits)*
- c4: Mesh objects can only have one material assigned. *(doc, high; mesh-texture-limits)*
- c5: Roblox default materials: Parts show 1024×1024 on an 8×8 stud face; Terrain shows 512×512 across 8×8 studs. *(doc, high; mesh-texture-limits)*
- c6: PBR budget rule: 256×256 per 2×2×2 unit space; next highest resolution if larger than 2×2×2. *(doc, high; mesh-texture-limits)*
- c7: PBR size examples: 64–128 for 1×1×1 (jewelry, sunglasses); 256 for 2×2×2 (hair, shoes, t-shirts); 512 for 4×4×4 (jackets, pants); 1024 max for 8×8×8 (full-body clothing, humanoids). *(doc, high; mesh-texture-limits)*
- c8: 256×256 is the maximum budget for non-albedo maps for rigid accessories. *(doc, high; avatar-ugc-accessories)*
- c9: Roblox may downsample textures when many render at once. *(doc, medium; mesh-texture-limits)*
- c10: Albedo maps: RGB 24-bit. Normal maps: RGB 24-bit, OpenGL tangent-space only. Roughness, Metalness, Emissive Mask: single-channel grayscale 8-bit. *(doc, high; mesh-texture-limits)*
- c11: UV rules: single UV set per component (Studio disallows multiple UV sets); all UVs within 0:1 space; overlapping UVs allowed; max 1024×1024 texture map. *(doc, high; mesh-texture-limits)*
- c12: Doc points to 'Blender / Maya texture settings' (assign-textures) page for connecting textures to models for Studio import. *(doc, medium; blender-roblox-export-import)*

## Numbers
- n1: **max texture resolution**: 4096×4096 
- n2: **UV map max**: 1024×1024 
- n3: **PBR budget**: 256×256 per 2×2×2 units 
- n4: **rigid accessory non-albedo max**: 256×256 
- n5: **Part default material texel**: 1024×1024 on 8×8 studs 

## Contradictions flagged
- Max UV texture map resolution listed as 1024×1024 while general texture max is 4096×4096. (vs Same document's 'Resolution' bullet (4096×4096 max))

## Points to
- https://create.roblox.com/docs/parts/textures-decals
- https://create.roblox.com/docs/art/modeling/surface-appearance
- https://create.roblox.com/docs/art/modeling/assign-textures
- https://create.roblox.com/docs/parts/materials
- https://create.roblox.com/docs/avatar/rigid-accessories/specifications
