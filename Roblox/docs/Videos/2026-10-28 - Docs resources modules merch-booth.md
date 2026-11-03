---
title: "Docs: resources / modules / merch-booth"
url: https://create.roblox.com/docs/resources/modules/merch-booth.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: resources / modules / merch-booth

[Open](https://create.roblox.com/docs/resources/modules/merch-booth.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox developer docs for the MerchBooth module: an in-game shop that sells avatar assets, passes and developer products. Covers installation, configuration, adding items by asset/pass/product ID, shoppable regions, proximity prompts, and the full API (configure, addItemAsync, setCatalogSort, events). Notes a 40% affiliate fee on third-party UGC sales.

## Tips
- [page](https://create.roblox.com/docs/resources/modules/merch-booth) **[[monetisation-other]]** Enable 'Allow Third Party Sales' in Experience Settings > Security, or you cannot sell other creators' UGC assets in the merch booth.
- [page](https://create.roblox.com/docs/resources/modules/merch-booth) **[[monetisation-gamepasses]]** Add passes with addItemAsync(id, Enum.InfoType.GamePass); pass IDs come from Creator Dashboard > Passes > Copy Asset ID.
- [page](https://create.roblox.com/docs/resources/modules/merch-booth) **[[monetisation-devproducts]]** Add developer products with addItemAsync(id, Enum.InfoType.Product); product IDs come from Creator Dashboard > Developer Products.
- [page](https://create.roblox.com/docs/resources/modules/merch-booth) **[[common-mistakes]]** Wrap addItemAsync in pcall; it is a network call that can fail occasionally.
- [page](https://create.roblox.com/docs/resources/modules/merch-booth) **[[ui-ux-design]]** Use proximity prompts over in-game objects as an alternative to the 2D catalog so players discover items in the 3D world and try them on.
- [page](https://create.roblox.com/docs/resources/modules/merch-booth) **[[ui-ux-design]]** Remove the default catalog button with toggleCatalogButton(false) when using custom buttons, shop regions or proximity prompts.
- [page](https://create.roblox.com/docs/resources/modules/merch-booth) **[[ui-ux-design]]** Set disableCharacterMovement = true while the booth is open if you want the character to stay still in a shop.
- [page](https://create.roblox.com/docs/resources/modules/merch-booth) **[[monetisation-other]]** The booth earns a 40% affiliate fee on sales of other creators' items.

## Numbers
- [page](https://create.roblox.com/docs/resources/modules/merch-booth) Affiliate fee on third-party item sales: **40%** (Revenue share from selling other creators' avatar items via MerchBooth)
- [page](https://create.roblox.com/docs/resources/modules/merch-booth) Default proximity prompt activation distance: **10 studs** (proximityButtonActivationDistance default for prompts)
- [page](https://create.roblox.com/docs/resources/modules/merch-booth) Default proximity pulse count: **3** (proximityButtonPulseCount default)
- [page](https://create.roblox.com/docs/resources/modules/merch-booth) Default text size: **14** (configure textSize default)

## Tools
MerchBooth module (Creator Store package), Creator Dashboard, Roblox Studio Toolbox

## He points to
- Roblox Creator Store Packages

## Topics
[[common-mistakes]] [[monetisation-devproducts]] [[monetisation-gamepasses]] [[monetisation-other]] [[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
