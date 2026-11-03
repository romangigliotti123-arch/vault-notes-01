---
title: "Docs: resources / feature-packages / bundles"
url: https://create.roblox.com/docs/resources/feature-packages/bundles.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: resources / feature-packages / bundles

[Open](https://create.roblox.com/docs/resources/feature-packages/bundles.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox Creator Docs page for the Bundles feature package: installing Core and Bundles packages, defining currencies and bundles (Marketplace or in-experience pricing), wiring purchase handlers, receipt processing, prompting bundles, and the RelativeTime, FixedTime and OneTime bundle types.

## Tips
- [page](https://create.roblox.com/docs/resources/feature-packages/bundles) **[[monetisation-devproducts]]** Use a new, unique developer product for each bundle so its sales can be tracked separately.
- [page](https://create.roblox.com/docs/resources/feature-packages/bundles) **[[data-persistence]]** Record receiptInfo.PurchaseId in your own data store before processing a bundle receipt so retries never award items twice; your data store is the source of truth.
- [page](https://create.roblox.com/docs/resources/feature-packages/bundles) **[[monetisation-other]]** Set priceInRobux on each included item so the bundle shows its relative value against the sum of its contents.
- [page](https://create.roblox.com/docs/resources/feature-packages/bundles) **[[monetisation-other]]** Use starter bundles with a 15-minute durationInSeconds and singleUse=true to create urgency for new players.
- [page](https://create.roblox.com/docs/resources/feature-packages/bundles) **[[monetisation-other]]** Use bundles at several price points to increase spend depth across different player types.
- [page](https://create.roblox.com/docs/resources/feature-packages/bundles) **[[updates-live-ops]]** Use FixedTime bundles for holiday or month-long limited offers, ending at a set UTC time.
- [page](https://create.roblox.com/docs/resources/feature-packages/bundles) **[[monetisation-other]]** Use OneTime bundles for moment-of-need offers, such as prompting extra currency when a player runs out.
- [page](https://create.roblox.com/docs/resources/feature-packages/bundles) **[[first-session-onboarding]]** Prompt a starter bundle in onPlayerAdded to target low conversion and encourage early spend.
- [page](https://create.roblox.com/docs/resources/feature-packages/bundles) **[[common-mistakes]]** Do not move package UI objects around in the hierarchy without updating UIController, because the code cannot find them.
- [page](https://create.roblox.com/docs/resources/feature-packages/bundles) **[[development-process-and-speed]]** Set singleUse to false only while testing in Studio; keep it true in production so expired offers never re-prompt.
- [page](https://create.roblox.com/docs/resources/feature-packages/bundles) **[[scripting-and-performance]]** Enable Studio Access to API Services in Experience Settings > Security so the package can track purchases with data store calls.

## Numbers
- [page](https://create.roblox.com/docs/resources/feature-packages/bundles) Starter bundle example discount: **Save 75%** (Example metadata description in the starter bundle sample)
- [page](https://create.roblox.com/docs/resources/feature-packages/bundles) Example starter bundle duration: **900 seconds (15 minutes)** (durationInSeconds in the sample RelativeTime bundle)
- [page](https://create.roblox.com/docs/resources/feature-packages/bundles) Example in-experience currency price: **79 Gems** (Sample pricing with CurrencyTypes.PriceType.InExperience)
- [page](https://create.roblox.com/docs/resources/feature-packages/bundles) Example Robux item prices: **49, 99, 149 Robux** (Sample included items in the starter bundle)
- [page](https://create.roblox.com/docs/resources/feature-packages/bundles) RelativeTime offer lifetime example: **24 hours** (Single-use starter pack shown to new players)

## Tools
Roblox Studio, Bundles feature package, Core feature package, Creator Store / Toolbox, MarketplaceService

## He points to
- Contextual Purchases (Roblox docs)

## Topics
[[common-mistakes]] [[data-persistence]] [[development-process-and-speed]] [[first-session-onboarding]] [[monetisation-devproducts]] [[monetisation-other]] [[scripting-and-performance]] [[updates-live-ops]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
