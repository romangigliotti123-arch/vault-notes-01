---
title: "Docs: art / modeling / texture-specifications"
url: https://create.roblox.com/docs/art/modeling/texture-specifications.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: art / modeling / texture-specifications

[Open](https://create.roblox.com/docs/art/modeling/texture-specifications.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on texture specifications: supported file formats, resolution guidance by stud size, SurfaceAppearance texture map formats, PBR texture budgets by asset size, and UV mapping requirements.

## Tips
- [page](https://create.roblox.com/docs/art/modeling/texture-specifications) **[[building-art-and-assets]]** Upload textures as .png, .jpg, .tga, or .bmp; these are the only formats accepted for separately uploaded textures in Studio.
- [page](https://create.roblox.com/docs/art/modeling/texture-specifications) **[[building-art-and-assets]]** Size textures to surface area: 256x256 for 5x5 stud objects, 512x512 for 10x10, 1024x1024 for 20x20. Manual sizing can reduce memory use.
- [page](https://create.roblox.com/docs/art/modeling/texture-specifications) **[[building-art-and-assets]]** Keep mesh objects to one material; a mesh can only have one material assigned.
- [page](https://create.roblox.com/docs/art/modeling/texture-specifications) **[[3d-modeling-rigging-and-animation]]** Export Normal maps as OpenGL format, Tangent Space; Roblox does not support other normal map formats.
- [page](https://create.roblox.com/docs/art/modeling/texture-specifications) **[[3d-modeling-rigging-and-animation]]** Save Albedo and Normal maps as RGB 24-bit; save Roughness, Metalness and Emissive Mask maps as single-channel grayscale 8-bit.
- [page](https://create.roblox.com/docs/art/modeling/texture-specifications) **[[optimization-and-streaming]]** Budget PBR maps at 256x256 per 2x2x2 units of asset volume; use the next higher size if larger, capping at 1024x1024 for 8x8x8 units.
- [page](https://create.roblox.com/docs/art/modeling/texture-specifications) **[[optimization-and-streaming]]** Cap non-albedo PBR maps on rigid accessories (hair, shoes, shirts) at 256x256; the maximum budget is 256x256 for these.
- [page](https://create.roblox.com/docs/art/modeling/texture-specifications) **[[building-art-and-assets]]** Use a single UV set per component (humanoid or accessory); Studio does not allow multiple UV sets.
- [page](https://create.roblox.com/docs/art/modeling/texture-specifications) **[[3d-modeling-rigging-and-animation]]** Keep all UV coordinates within the 0:1 space; overlapping UVs are allowed.
- [page](https://create.roblox.com/docs/art/modeling/texture-specifications) **[[optimization-and-streaming]]** Expect Roblox to downsample textures when many render at once; the engine also starts with lower quality and ramps up based on device resources.

## Numbers
- [page](https://create.roblox.com/docs/art/modeling/texture-specifications) Max texture resolution: **4096x4096 (4K) for textures; 1024x1024 for UV map spaces** (Official docs texture resolution limits)
- [page](https://create.roblox.com/docs/art/modeling/texture-specifications) Texture size for 5x5 stud object: **256x256** (General sizing guidance)
- [page](https://create.roblox.com/docs/art/modeling/texture-specifications) Texture size for 10x10 stud object: **512x512** (General sizing guidance)
- [page](https://create.roblox.com/docs/art/modeling/texture-specifications) Texture size for 20x20 stud object: **1024x1024** (General sizing guidance)
- [page](https://create.roblox.com/docs/art/modeling/texture-specifications) Default Part texel density: **1024x1024 on an 8x8 stud face** (Roblox default material reference)
- [page](https://create.roblox.com/docs/art/modeling/texture-specifications) Default Terrain texel density: **512x512 across 8x8 studs** (Roblox default material reference)
- [page](https://create.roblox.com/docs/art/modeling/texture-specifications) PBR map size for 1x1x1 unit asset: **64x64 to 128x128** (Jewelry, sunglasses, eyebrows, mustaches)
- [page](https://create.roblox.com/docs/art/modeling/texture-specifications) PBR map size for 2x2x2 unit asset: **256x256 (max for rigid accessories non-albedo)** (Hair, shoes, tank tops, t-shirts, shorts)
- [page](https://create.roblox.com/docs/art/modeling/texture-specifications) PBR map size for 4x4x4 unit asset: **512x512** (Jackets, pants, overalls, long-sleeve shirts)
- [page](https://create.roblox.com/docs/art/modeling/texture-specifications) PBR map size for 8x8x8 unit asset: **1024x1024 (maximum)** (Full body clothing and humanoid characters)

## Tools
Roblox Studio, Blender, Maya

## He points to
- Blender / Maya texture settings (Roblox docs)
- PBR texture budgets (Roblox docs)
- Textures and decals (Roblox docs)

## Topics
[[3d-modeling-rigging-and-animation]] [[building-art-and-assets]] [[optimization-and-streaming]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
