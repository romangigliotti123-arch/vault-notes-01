---
title: "Docs: parts / models"
url: https://create.roblox.com/docs/parts/models.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: parts / models

[Open](https://create.roblox.com/docs/parts/models.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on Models: how to create them (grouping or inserting an empty Model), set a PrimaryPart, select and transform models via MoveTo/PivotTo/TranslateBy, streaming behavior, destroy-height rule, uploading to Roblox as assets, and selling models on the Creator Store.

## Tips
- [page](https://create.roblox.com/docs/parts/models) **[[building-art-and-assets]]** Set a PrimaryPart on models joined by WeldConstraints or Motor6Ds so the pivot and bounding box move with the correct part.
- [page](https://create.roblox.com/docs/parts/models) **[[building-art-and-assets]]** Use Alt (Windows) or Option (Mac) click selection cycling to pick hidden child parts without moving the camera.
- [page](https://create.roblox.com/docs/parts/models) **[[scripting-and-performance]]** Use Model:PivotTo() to move whole models including all descendant PVInstances to a CFrame; MoveTo() only moves the PrimaryPart.
- [page](https://create.roblox.com/docs/parts/models) **[[optimization-and-streaming]]** With streaming enabled, set key models to Persistent so they never stream out, or Atomic to stream as one unit with descendants.
- [page](https://create.roblox.com/docs/parts/models) **[[optimization-and-streaming]]** Set models to SLIM or imposter mesh levels of detail when streamed out to avoid jarring pop-in.
- [page](https://create.roblox.com/docs/parts/models) **[[building-art-and-assets]]** Keep Creator Store model dependencies within 15,000 and each mesh under 20,000 triangles; set reasonable scale and orientation.
- [page](https://create.roblox.com/docs/parts/models) **[[building-art-and-assets]]** Distribute any child audio asset on the Creator Store before parenting it to the model, or the audio will not be audible at runtime.
- [page](https://create.roblox.com/docs/parts/models) **[[monetisation-other]]** Selling models on the Creator Store in USD gives 100% of net proceeds, bypassing platform fees and DevEx rates.
- [page](https://create.roblox.com/docs/parts/models) **[[ugc-and-avatar-economy]]** Upload models via Explorer right-click Save to Roblox as Development Item, category Model, to reuse them across games by asset ID.

## Numbers
- [page](https://create.roblox.com/docs/parts/models) Creator Store dependency limit: **15,000 dependencies per model** (Maximum dependencies for a model to be distributed and sold)
- [page](https://create.roblox.com/docs/parts/models) Mesh triangle limit: **20,000 triangles per mesh dependency** (Creator Store model requirement)
- [page](https://create.roblox.com/docs/parts/models) Creator Store proceeds: **100% of net proceeds** (Selling models on Creator Store, bypassing platform fees and DevEx)

## Tools
Roblox Studio Explorer, Properties window, Asset Configuration window, Creator Store

## He points to
- Character Name/Health Display
- per-model streaming controls
- model level of detail
- Asset privacy
- Creator Store - Distribute and sell assets

## Topics
[[building-art-and-assets]] [[monetisation-other]] [[optimization-and-streaming]] [[scripting-and-performance]] [[ugc-and-avatar-economy]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
