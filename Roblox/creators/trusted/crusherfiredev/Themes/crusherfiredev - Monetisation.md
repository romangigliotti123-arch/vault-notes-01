---
title: crusherfiredev - Monetisation
creator: crusherfiredev
tags: [roblox, crusherfiredev, theme]
creator_trust: TRUSTED
creator_score: 8.7
---

> [!note] Trust: TRUSTED (credibility audit score 8.7): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# crusherfiredev: Monetisation

All crusherfiredev tips on this theme, grouped by topic, oldest first. Cross-creator synthesis: see [[README]] in roblox-kb.

## [[monetisation-gamepasses]]
- 2024-03-27 [0:00](https://youtu.be/kDCLGPMpLl0?t=0) Create gamepasses in Creator Hub under the game's Monetization > Passes section, then mark them 'for sale' in the Sales tab to set a price. ([[2024-03-27 - earn ROBUX from GAMEPASSES!|earn ROBUX from GAMEPASSES!]])
- 2024-03-27 [0:40](https://youtu.be/kDCLGPMpLl0?t=40) Copy the gamepass asset ID from the three-dot menu; you need it in code to prompt purchases and check ownership. ([[2024-03-27 - earn ROBUX from GAMEPASSES!|earn ROBUX from GAMEPASSES!]])
- 2024-03-27 [3:09](https://youtu.be/kDCLGPMpLl0?t=189) Connect to MarketplaceService.PromptGamePassPurchaseFinished on the server; it fires on both cancel and success, so check the purchased flag before granting benefits. ([[2024-03-27 - earn ROBUX from GAMEPASSES!|earn ROBUX from GAMEPASSES!]])
- 2024-03-27 [4:44](https://youtu.be/kDCLGPMpLl0?t=284) On PlayerAdded, call MarketplaceService:UserOwnsGamePassAsync(userId, passId) wrapped in pcall, since it yields and can error. ([[2024-03-27 - earn ROBUX from GAMEPASSES!|earn ROBUX from GAMEPASSES!]])
- 2024-03-27 [6:59](https://youtu.be/kDCLGPMpLl0?t=419) If purchase prompts fail with 'third party sales disabled', enable Allow Third Party Sales under Game Settings > Security. ([[2024-03-27 - earn ROBUX from GAMEPASSES!|earn ROBUX from GAMEPASSES!]])
- 2024-03-27 [4:44](https://youtu.be/kDCLGPMpLl0?t=284) Handle both live purchases mid-session and ownership checks at join so benefits update dynamically when a player buys a pass. ([[2024-03-27 - earn ROBUX from GAMEPASSES!|earn ROBUX from GAMEPASSES!]])

## [[monetisation-devproducts]]
- 2025-12-13 [5:40](https://youtu.be/6Q_p2ObUXSo?t=340) Roblox can't gift game passes directly. Sell a developer product, treat it as a pass, and record ownership in a DataStore. Purchases stack and can be gifted. ([[2025-12-13 - Roblox Devs, Stop Rewriting Code (Do THIS Instead)|Roblox Devs, Stop Rewriting Code (Do THIS Instead)]])

Up: [[crusherfiredev - How to make successful Roblox games]]
