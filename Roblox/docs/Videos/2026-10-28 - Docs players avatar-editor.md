---
title: "Docs: players / avatar-editor"
url: https://create.roblox.com/docs/players/avatar-editor.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: players / avatar-editor

[Open](https://create.roblox.com/docs/players/avatar-editor.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs for the Avatar Editor Service: requesting per-session inventory read access, reading inventory, searching the catalog with CatalogSearchParams, saving avatars and outfits via prompts, and handling purchases of unowned items.

## Tips
- [page](https://create.roblox.com/docs/players/avatar-editor) **[[ugc-and-avatar-economy]]** Build an in-game avatar editor on top of AvatarEditorService; Roblox recommends it for a complete character customization experience.
- [page](https://create.roblox.com/docs/players/avatar-editor) **[[ugc-and-avatar-economy]]** Request inventory access with PromptAllowInventoryReadAccess once per session before calling GetInventory.
- [page](https://create.roblox.com/docs/players/avatar-editor) **[[ugc-and-avatar-economy]]** Check ownership with MarketplaceService:PlayerOwnsAsset before saving an avatar or outfit, since users don't receive items they don't own.
- [page](https://create.roblox.com/docs/players/avatar-editor) **[[ugc-and-avatar-economy]]** Offer MarketplaceService:PromptPurchase for unowned items, or use PromptSetFavorite to let users favorite them instead if you skip purchases.
- [page](https://create.roblox.com/docs/players/avatar-editor) **[[business-and-payouts]]** Robux commissions are not earned if users buy items outside your game, so prompt purchases in-experience.
- [page](https://create.roblox.com/docs/players/avatar-editor) **[[client-server-and-remotes]]** PromptSaveAvatar and PromptCreateOutfit do not yield; listen to PromptSaveAvatarCompleted / PromptCreateOutfitCompleted for the result.

## Games
- **Simple Avatar Editor Demo**: Reference place Roblox provides as an example of an in-game avatar editor built with AvatarEditorService.

## Tools
AvatarEditorService, MarketplaceService, HumanoidDescription, CatalogSearchParams

## He points to
- Simple Avatar Editor Demo reference place

## Topics
[[business-and-payouts]] [[client-server-and-remotes]] [[ugc-and-avatar-economy]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
