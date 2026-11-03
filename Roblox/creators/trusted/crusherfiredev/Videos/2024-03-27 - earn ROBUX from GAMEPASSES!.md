---
title: "earn ROBUX from GAMEPASSES!"
url: https://youtu.be/kDCLGPMpLl0
creator: Crusherfire
official: false
advice_density: medium
date: 2024-03-27
views: 2262
transcript: auto-captions
confidence: high
tags: [roblox, crusherfiredev, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.7
---

> [!note] Trust: TRUSTED (credibility audit score 8.7): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# earn ROBUX from GAMEPASSES!

[Watch](https://youtu.be/kDCLGPMpLl0) | crusherfiredev | 2,262 views | 2024-03-27

## Summary
Tutorial on creating Roblox gamepasses in the Creator Hub, prompting purchases client-side with MarketplaceService:PromptGamePassPurchase, caching ownership on the server via attributes, checking ownership on join with UserOwnsGamePassAsync, and testing in a one-player server.

## Tips
- [0:00](https://youtu.be/kDCLGPMpLl0?t=0) **[[monetisation-gamepasses]]** Create gamepasses in Creator Hub under the game's Monetization > Passes section, then mark them 'for sale' in the Sales tab to set a price.
- [0:40](https://youtu.be/kDCLGPMpLl0?t=40) **[[monetisation-gamepasses]]** Copy the gamepass asset ID from the three-dot menu; you need it in code to prompt purchases and check ownership.
- [1:38](https://youtu.be/kDCLGPMpLl0?t=98) **[[scripting-and-performance]]** Prompt purchases with MarketplaceService:PromptGamePassPurchase(player, gamePassId) from a LocalScript triggered by a button click.
- [3:09](https://youtu.be/kDCLGPMpLl0?t=189) **[[monetisation-gamepasses]]** Connect to MarketplaceService.PromptGamePassPurchaseFinished on the server; it fires on both cancel and success, so check the purchased flag before granting benefits.
- [3:49](https://youtu.be/kDCLGPMpLl0?t=229) **[[data-persistence]]** Cache owned passes on the player as attributes (attribute name = gamepass ID, value true) so other scripts can check ownership cheaply.
- [4:44](https://youtu.be/kDCLGPMpLl0?t=284) **[[monetisation-gamepasses]]** On PlayerAdded, call MarketplaceService:UserOwnsGamePassAsync(userId, passId) wrapped in pcall, since it yields and can error.
- [5:25](https://youtu.be/kDCLGPMpLl0?t=325) **[[code-architecture-and-frameworks]]** Store gamepass IDs in a single ModuleScript so server and client scripts share the same list instead of duplicating IDs.
- [6:59](https://youtu.be/kDCLGPMpLl0?t=419) **[[testing-debugging-and-qa]]** Test purchases in a one-player server; the game owner already owns their own passes and gets 'already own this item' errors otherwise.
- [6:59](https://youtu.be/kDCLGPMpLl0?t=419) **[[monetisation-gamepasses]]** If purchase prompts fail with 'third party sales disabled', enable Allow Third Party Sales under Game Settings > Security.
- [4:44](https://youtu.be/kDCLGPMpLl0?t=284) **[[monetisation-gamepasses]]** Handle both live purchases mid-session and ownership checks at join so benefits update dynamically when a player buys a pass.

## Tools
Roblox Studio, Creator Hub, MarketplaceService, Players service

## Topics
[[code-architecture-and-frameworks]] [[data-persistence]] [[monetisation-gamepasses]] [[scripting-and-performance]] [[testing-debugging-and-qa]]

Back to [[crusherfiredev - How to make successful Roblox games]]
