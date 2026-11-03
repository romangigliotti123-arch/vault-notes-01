---
title: "Docs: resources / the-mystery-of-duvall-drive / materialize-the-world"
url: https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/materialize-the-world.md
creator: Roblox Creator Docs
official: true
advice_density: high
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: resources / the-mystery-of-duvall-drive / materialize-the-world

[Open](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/materialize-the-world.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on materials for the Duvall Drive demo. Covers planning a shared craftsman-style material palette, trim maps vs 1:1 textures, tinting via alpha-masked Overlay surface appearances, texture size reduction, and Material Variants (including terrain overrides) built in Material Manager.

## Tips
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/materialize-the-world) **[[building-art-and-assets]]** Plan a shared material art direction upfront and reuse a small set of materials across many assets to stay within texture memory budgets.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/materialize-the-world) **[[building-art-and-assets]]** Use clean, non-repeating-looking trim maps for assets at varied scales; heavy stains or wear that repeat look wrong, so use a unique 1:1 map for heavily worn assets.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/materialize-the-world) **[[building-art-and-assets]]** Package one Surface Appearance node with trim maps and apply it to many meshes by laying out UVs creatively.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/materialize-the-world) **[[building-art-and-assets]]** Use an alpha mask with AlphaMode set to Overlay and BrickColor/Color3 to tint one surface appearance into many color variations.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/materialize-the-world) **[[optimization-and-streaming]]** Drop ColorMap, RoughnessMap and MetalnessMap resolution by 1-2x based on usage, iterating and inspecting in Studio until quality holds.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/materialize-the-world) **[[optimization-and-streaming]]** Leave MetalnessMap blank for non-metallic surfaces to save texture memory.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/materialize-the-world) **[[optimization-and-streaming]]** After importing custom meshes, delete the auto-applied textureID when reusing a packaged Surface Appearance, or each import bloats texture memory.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/materialize-the-world) **[[building-art-and-assets]]** Name custom Material Variants with an _MV suffix to distinguish them from default materials.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/materialize-the-world) **[[building-art-and-assets]]** Choose the Base Material for a Material Variant by physical properties (friction, density, footstep sounds), since variants inherit these and only visuals change.
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/materialize-the-world) **[[building-art-and-assets]]** Terrain can only be customized by overriding the 22 built-in materials; per-part Material Variants have no such limit.

## Numbers
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/materialize-the-world) Texture size example: **Normal 1024, BaseColor 512, Roughness 256, no Metalness** (Leather trim texture set in demo)
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/materialize-the-world) Material override count: **22** (Built-in materials terrain can override)
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/materialize-the-world) Terrain overrides in demo: **About 10** (Default materials overridden for rain-soaked terrain)
- [page](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/materialize-the-world) Texture resolution reduction: **1-2x** (Reduction of ColorMap/Roughness/Metalness without visible fidelity loss)

## Games
- **The Mystery of Duvall Drive**: Roblox demo house using craftsman-style shared trim maps, Material Variants and wet terrain overrides for rainy outdoor look.
- **Beyond the Dark**: Referenced earlier Roblox demo providing the trim sheet technique documentation.

## Tools
Substance Designer, Substance Painter, Material Manager, Roblox Studio

## He points to
- Beyond the Dark documentation (Create trim sheets section)

## Topics
[[building-art-and-assets]] [[optimization-and-streaming]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
