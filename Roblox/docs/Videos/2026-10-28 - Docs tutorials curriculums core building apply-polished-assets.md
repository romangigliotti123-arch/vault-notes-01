---
title: "Docs: tutorials / curriculums / core / building / apply-polished-assets"
url: https://create.roblox.com/docs/tutorials/curriculums/core/building/apply-polished-assets.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: tutorials / curriculums / core / building / apply-polished-assets

[Open](https://create.roblox.com/docs/tutorials/curriculums/core/building/apply-polished-assets.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox Creator Docs tutorial page on applying polished assets to a greybox environment. Covers getting the Core Building and Scripting asset library from the Creator Store, fixing gray meshes by adding MaterialVariants to MaterialService, extending the Explorer folder structure, and placing platforms, sea stacks, coins and mountains via exact Position/Size/Orientation values.

## Tips
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/building/apply-polished-assets) **[[building-art-and-assets]]** Organize polished assets into folders (Platforms, Mountains, Coins) under World and mirror greybox level names so swaps are easy to track.
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/building/apply-polished-assets) **[[building-art-and-assets]]** If meshes appear gray after importing a library, drag the referenced MaterialVariant objects into MaterialService to install their textures.
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/building/apply-polished-assets) **[[building-art-and-assets]]** Keep polished coins named exactly 'Coin' inside the Coins folder so existing scripts that reference coins by name keep working.
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/building/apply-polished-assets) **[[building-art-and-assets]]** Rotate and scale repeated background meshes (e.g. mountains) with varied Orientation and Scale so the repetition is not noticeable.
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/building/apply-polished-assets) **[[building-art-and-assets]]** Delete placeholder greybox parts only after every polished replacement is placed, so you can compare progress against the greybox layout.
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/building/apply-polished-assets) **[[common-mistakes]]** Do not skip installing MaterialVariants; meshes that reference uninstalled MaterialVariants render gray instead of textured.
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/building/apply-polished-assets) **[[ai-and-tools]]** Assistant is effective for repetitive, deterministic setup such as placing many assets at exact CFrame values, though manual placement is also offered.

## Numbers
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/building/apply-polished-assets) Assets in sample library: **6 3D meshes, 2 custom MaterialVariant materials, 1 particle effect set**
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/building/apply-polished-assets) Sample platform model containers: **18 in Platforms folder**
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/building/apply-polished-assets) Sample coin placements: **35 coin positions**
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/building/apply-polished-assets) Sample mountain placements: **16 MountainMesh instances**

## Games
- **Island Jump**: Tutorial sample game used as the reference for applying the polished Core Building and Scripting asset library to a greybox.

## Tools
Creator Store, Toolbox, Explorer, Properties window, Assistant (Build with Assistant), MaterialService

## He points to
- Materials - Custom Materials and PBR Textures
- Core Building and Scripting asset library (Creator Store)

## Topics
[[ai-and-tools]] [[building-art-and-assets]] [[common-mistakes]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
