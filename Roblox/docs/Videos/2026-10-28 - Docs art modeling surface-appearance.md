---
title: "Docs: art / modeling / surface-appearance"
url: https://create.roblox.com/docs/art/modeling/surface-appearance.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: art / modeling / surface-appearance

[Open](https://create.roblox.com/docs/art/modeling/surface-appearance.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on PBR surface appearance: how to add SurfaceAppearance to MeshParts and the five supported maps (color, normal, roughness, metalness, emissive mask), alpha modes, tinting, and value guidance.

## Tips
- [page](https://create.roblox.com/docs/art/modeling/surface-appearance) **[[building-art-and-assets]]** Insert a SurfaceAppearance under a MeshPart and enter asset IDs in its map properties; it overrides the MeshPart's original texture.
- [page](https://create.roblox.com/docs/art/modeling/surface-appearance) **[[building-art-and-assets]]** Use an albedo (color) map, not a diffuse map with baked lighting; baked shading looks wrong when lighting changes. Let normal, roughness and metalness maps handle detail.
- [page](https://create.roblox.com/docs/art/modeling/surface-appearance) **[[building-art-and-assets]]** Set Transparency alpha mode with MeshPart.Transparency at 0 for hard-edged cutouts (foliage, lace) so depth occlusion renders correctly.
- [page](https://create.roblox.com/docs/art/modeling/surface-appearance) **[[building-art-and-assets]]** Set MeshPart.Transparency to at least 0.02 when alpha adds detail to semi-transparent objects like dirty glass or soft feathers.
- [page](https://create.roblox.com/docs/art/modeling/surface-appearance) **[[building-art-and-assets]]** Author color maps in near-white grayscale so SurfaceAppearance.Color tinting gives the strongest effect; reuse one map with multiple tints to save memory.
- [page](https://create.roblox.com/docs/art/modeling/surface-appearance) **[[building-art-and-assets]]** Keep normal map seams hidden; normal maps accentuate awkward seams. Use OpenGL tangent-space normal maps only, since Roblox supports no other format.
- [page](https://create.roblox.com/docs/art/modeling/surface-appearance) **[[building-art-and-assets]]** Base material values on physical characteristics rather than tuning for one lighting setup; test across lighting environments.
- [page](https://create.roblox.com/docs/art/modeling/surface-appearance) **[[building-art-and-assets]]** For fresnel-related unexpected sheen on rough surfaces, increase the roughness map value by about 0.1.
- [page](https://create.roblox.com/docs/art/modeling/surface-appearance) **[[building-art-and-assets]]** Use partial metalness only for moderate-reflectance materials like satin or silk; otherwise use 0% or 100%.
- [page](https://create.roblox.com/docs/art/modeling/surface-appearance) **[[building-art-and-assets]]** Use an emissive mask instead of the all-or-nothing Neon material for detailed glow like illuminated text or bioluminescence. Marketplace avatar items must keep EmissiveStrength between 0 and 40.
- [page](https://create.roblox.com/docs/art/modeling/surface-appearance) **[[optimization-and-streaming]]** Use alpha-based transparency instead of intricate mesh geometry for lace or netting to avoid geometry performance cost.
- [page](https://create.roblox.com/docs/art/modeling/surface-appearance) **[[scripting-and-performance]]** Do not modify SurfaceAppearance properties by script at runtime; the engine needs pre-processing. Use Color tinting, which is free performance-wise, for runtime changes.

## Numbers
- [page](https://create.roblox.com/docs/art/modeling/surface-appearance) Transparency threshold for alpha blending: **0 (cutouts) or at least 0.02 (semi-transparent)** (MeshPart.Transparency setting in Transparency alpha mode)
- [page](https://create.roblox.com/docs/art/modeling/surface-appearance) Flat normal map color: **[127, 127, 255]** (Uniform color producing a completely flat normal map)
- [page](https://create.roblox.com/docs/art/modeling/surface-appearance) Roughness adjustment for fresnel compensation: **about +0.1** (Increase roughness map value to get consistent lighting on rough surfaces)
- [page](https://create.roblox.com/docs/art/modeling/surface-appearance) Marketplace emissive strength limit: **0 to 40** (EmissiveStrength range for avatar items to pass validation)
- [page](https://create.roblox.com/docs/art/modeling/surface-appearance) Metalness values: **0% or 100% typically** (Partial values only for moderate reflectance such as satin or silk)

## Games
- **The Mystery of Duvall Drive**: Referenced as source of statue mesh used to demonstrate color tinting.

## Tools
Roblox Studio, Blender, Maya, Substance Painter

## He points to
- Blender / Maya texture settings
- Texture requirements
- Material references
- Clothing examples
- Custom skin tone

## Topics
[[building-art-and-assets]] [[optimization-and-streaming]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
