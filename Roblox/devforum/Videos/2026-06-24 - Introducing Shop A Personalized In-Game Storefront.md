---
title: "Introducing Shop: A Personalized In-Game Storefront"
url: https://devforum.roblox.com/t/introducing-shop-a-personalized-in-game-storefront/4701505
creator: Roblox DevForum
official: false
advice_density: medium
date: 2026-06-24
views: 347
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Introducing Shop: A Personalized In-Game Storefront

[Open](https://devforum.roblox.com/t/introducing-shop-a-personalized-in-game-storefront/4701505) | Roblox DevForum | 347 views | 2026-06-24

## Summary
Roblox docs/DevForum announcement for Shop, a personalized in-game storefront auto-published July 7, 2026. Covers personalization (Top Picks, categories, search, Robux packages), Creator Hub management, Listed vs Not Listed item settings, global Shop button, and OpenShop API.

## Tips
- [page](https://devforum.roblox.com/t/introducing-shop-a-personalized-in-game-storefront/4701505) **[[monetisation-devproducts]]** Review developer product Listed/Not Listed status before July 7; new developer products default to Not Listed and won't appear in Shop until set to Listed.
- [page](https://devforum.roblox.com/t/introducing-shop-a-personalized-in-game-storefront/4701505) **[[monetisation-devproducts]]** Implement ProcessReceipt properly for developer products; required for eligibility for external surfacing and ensures purchases are delivered immediately.
- [page](https://devforum.roblox.com/t/introducing-shop-a-personalized-in-game-storefront/4701505) **[[monetisation-other]]** Enable the global Shop button (off by default); it is a persistent always-visible entry point that makes Shop far easier to find than the hamburger menu.
- [page](https://devforum.roblox.com/t/introducing-shop-a-personalized-in-game-storefront/4701505) **[[monetisation-other]]** Rename, reorganize and move items between Shop categories so the storefront matches the experience you want players to see.
- [page](https://devforum.roblox.com/t/introducing-shop-a-personalized-in-game-storefront/4701505) **[[monetisation-other]]** Use Bonus Items on the Buy Robux page; they drive visits, time spent and Robux spent, and now also appear in the Shop Robux tab.
- [page](https://devforum.roblox.com/t/introducing-shop-a-personalized-in-game-storefront/4701505) **[[ui-ux-design]]** Call MarketplaceService:OpenShop(player) from custom buttons, NPCs or trigger zones to open Shop while keeping your own UI design; requires PromptExternalPurchase capability.
- [page](https://devforum.roblox.com/t/introducing-shop-a-personalized-in-game-storefront/4701505) **[[monetisation-gamepasses]]** Passes are always Listed and appear in Shop and the Experience Details Page automatically; their listing status cannot be changed.
- [page](https://devforum.roblox.com/t/introducing-shop-a-personalized-in-game-storefront/4701505) **[[client-server-and-remotes]]** Shop purchases use existing purchase handling; if grants only happen after rejoin, switch to ProcessReceipt so players get items right away.
- [page](https://devforum.roblox.com/t/introducing-shop-a-personalized-in-game-storefront/4701505) **[[ui-ux-design]]** To hide the Shop button in the hamburger menu, call StarterGui:SetCoreGuiEnabled(Enum.CoreGuiType.ExperienceShop, false) from a client script.
- [page](https://devforum.roblox.com/t/introducing-shop-a-personalized-in-game-storefront/4701505) **[[analytics-metrics]]** Preview the Shop in Roblox Studio and review it in Creator Hub before launch; if no changes are made, Roblox's suggested categories and listing settings auto-publish.

## Numbers
- [page](https://devforum.roblox.com/t/introducing-shop-a-personalized-in-game-storefront/4701505) Robux spend per user increase: **over 5% (Steal a Brainrot, after Product Intelligence personalization)** (Shop powered by Product Intelligence APIs)
- [page](https://devforum.roblox.com/t/introducing-shop-a-personalized-in-game-storefront/4701505) Shop auto-publish date: **July 7, 2026** (Shop publishes to all players automatically)

## Games
- **Steal a Brainrot**: Cited as seeing over 5% increase in Robux spend per user from Shop's personalization.

## Tools
Creator Hub Shop and Item catalog, Roblox Studio Shop preview, MarketplaceService:OpenShop, StarterGui:SetCoreGuiEnabled

## He points to
- MarketplaceService:OpenShop technical documentation
- Product Intelligence APIs

## Topics
[[analytics-metrics]] [[client-server-and-remotes]] [[monetisation-devproducts]] [[monetisation-gamepasses]] [[monetisation-other]] [[ui-ux-design]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
