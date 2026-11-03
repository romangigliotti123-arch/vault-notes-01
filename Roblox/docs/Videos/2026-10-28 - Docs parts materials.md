---
title: "Docs: parts / materials"
url: https://create.roblox.com/docs/parts/materials.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: parts / materials

[Open](https://create.roblox.com/docs/parts/materials.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on Materials: base materials with physical properties, applying materials via Material widget and Material Manager (apply-to-selected and paint tool), creating custom MaterialVariant materials, material overrides, terrain details, per-part and per-material physical properties precedence, and adaptive materials naming conventions. Includes asset ID and default color/physics reference tables.

## Tips
- [page](https://create.roblox.com/docs/parts/materials) **[[building-art-and-assets]]** Use a consistent PascalCase naming convention for MaterialVariants with the base material as first word (GrassWet, GrassDry, GrassBurned) to enable adaptive materials.
- [page](https://create.roblox.com/docs/parts/materials) **[[building-art-and-assets]]** Rename a custom material before applying it to parts; renaming after application requires re-applying it to those parts.
- [page](https://create.roblox.com/docs/parts/materials) **[[building-art-and-assets]]** Use square textures for custom material texture maps; unassigned texture maps remain blank.
- [page](https://create.roblox.com/docs/parts/materials) **[[building-art-and-assets]]** Create MaterialVariant instances in MaterialService and include them when distributing models to the Creator Store, otherwise custom materials won't carry over.
- [page](https://create.roblox.com/docs/parts/materials) **[[building-art-and-assets]]** Use material overrides to restyle all instances of a base material in a place at once, rather than re-applying materials to each part.
- [page](https://create.roblox.com/docs/parts/materials) **[[player-psychology-and-game-feel]]** Create a custom MaterialVariant from a base material and set custom PhysicalProperties (e.g. extremely slippery Ice variant) to change gameplay behaviour globally.
- [page](https://create.roblox.com/docs/parts/materials) **[[common-mistakes]]** Be aware that per-part CustomPhysicalProperties override the part's material variant, which overrides the material override, which overrides the base material's default physics.
- [page](https://create.roblox.com/docs/parts/materials) **[[building-art-and-assets]]** Use MaterialVariant for reusable tileable textures; use SurfaceAppearance for a specific UV-mapped mesh.

## Numbers
- [page](https://create.roblox.com/docs/parts/materials) Default part material: **Plastic** (Default Enum.Material for new Part instances)
- [page](https://create.roblox.com/docs/parts/materials) Glass refraction: **Not supported on mobile** (Glass material refraction unsupported on mobile devices)

## Tools
Material Manager, Material widget, Material Generator, Roblox Studio MaterialService, Creator Store

## He points to
- Creator Store Materials category
- Distributing Assets docs
- Custom terrain materials docs
- Parts docs
- Packages docs

## Topics
[[building-art-and-assets]] [[common-mistakes]] [[player-psychology-and-game-feel]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
