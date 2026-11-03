---
title: "Docs: avatar / layered-accessories / import"
url: https://create.roblox.com/docs/avatar/layered-accessories/import.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: avatar / layered-accessories / import

[Open](https://create.roblox.com/docs/avatar/layered-accessories/import.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on importing layered accessory FBX/glTF files via the Studio Importer, fixing textures manually in Asset Manager (ALB/MTL/NOR/RGH SurfaceAppearance maps), and converting Models into Accessories with the Accessory Fitting Tool, including the separate-left/right shoe rule.

## Tips
- [page](https://create.roblox.com/docs/avatar/layered-accessories/import) **[[building-art-and-assets]]** Import layered accessories via Home > Import as FBX or glTF; the Importer previews the asset and checks it against general 3D requirements.
- [page](https://create.roblox.com/docs/avatar/layered-accessories/import) **[[building-art-and-assets]]** If textures fail to load, upload images in Asset Manager and wait for moderation to clear before assigning them.
- [page](https://create.roblox.com/docs/avatar/layered-accessories/import) **[[building-art-and-assets]]** For a single basic texture, set MeshPart.TextureID; for PBR, add a SurfaceAppearance and assign ColorMap (_ALB), MetalnessMap (_MTL), NormalMap (_NOR), RoughnessMap (_RGH).
- [page](https://create.roblox.com/docs/avatar/layered-accessories/import) **[[3d-modeling-rigging-and-animation]]** Test the layered accessory on sample characters and animations in the AFT preview to confirm it deforms and moves correctly before generating.
- [page](https://create.roblox.com/docs/avatar/layered-accessories/import) **[[3d-modeling-rigging-and-animation]]** Make only minor cage adjustments in AFT; large cage changes require fixing the model in your modeling software and re-exporting.
- [page](https://create.roblox.com/docs/avatar/layered-accessories/import) **[[3d-modeling-rigging-and-animation]]** Convert left and right shoes as separate layered accessories, then group both as a Model when saving to Roblox.
- [page](https://create.roblox.com/docs/avatar/layered-accessories/import) **[[ugc-and-avatar-economy]]** Generated Accessory objects can be published to the Marketplace, equipped via HumanoidDescription, or saved to Toolbox/Creator Store for sharing.

## Tools
Studio Importer, Asset Manager, Accessory Fitting Tool (AFT), Creator Store, Toolbox

## He points to
- Roblox layered accessory specifications

## Topics
[[3d-modeling-rigging-and-animation]] [[building-art-and-assets]] [[ugc-and-avatar-economy]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
