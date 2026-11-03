---
title: "Docs: resources / modules / scavenger-hunt"
url: https://create.roblox.com/docs/resources/modules/scavenger-hunt.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: resources / modules / scavenger-hunt

[Open](https://create.roblox.com/docs/resources/modules/scavenger-hunt.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Official Roblox docs for the ScavengerHunt developer module (Creator Store package). Covers installing it, adding tokens or regions tagged ScavengerHuntPart, client/server configuration, collected and allCollected events, custom modals, GUI hiding callbacks, and the enable/disable API. Progress persists via DataStores.

## Tips
- [page](https://create.roblox.com/docs/resources/modules/scavenger-hunt) **[[data-persistence]]** ScavengerHunt uses DataStores; enable Studio Access to API Services in Experience Settings > Security to test it in Studio.
- [page](https://create.roblox.com/docs/resources/modules/scavenger-hunt) **[[building-and-level-design]]** Give every token and region a unique name; the module tracks each player's progress by that name.
- [page](https://create.roblox.com/docs/resources/modules/scavenger-hunt) **[[building-and-level-design]]** Anchor tokens, since the module disables CanCollide at runtime and unanchored parts will fall through geometry.
- [page](https://create.roblox.com/docs/resources/modules/scavenger-hunt) **[[core-loops-and-game-design]]** Use scavenger hunts to introduce players to the whole map; progress persists across sessions, so the hunt can span multiple visits.
- [page](https://create.roblox.com/docs/resources/modules/scavenger-hunt) **[[scripting-and-performance]]** Set resetOnPlayerRemoving = true in configureServer while testing so progress is not saved during development.
- [page](https://create.roblox.com/docs/resources/modules/scavenger-hunt) **[[player-psychology-and-game-feel]]** Reward allCollected once per player with a badge, new area access, or currency; the event fires only once per player.
- [page](https://create.roblox.com/docs/resources/modules/scavenger-hunt) **[[ui-ux-design]]** With useCustomModals, always provide a way to close custom modals or an automatic dismissal after a delay.
- [page](https://create.roblox.com/docs/resources/modules/scavenger-hunt) **[[ui-ux-design]]** Use hideOtherGuis and showOtherGuis callbacks to keep specific ScreenGuis visible when modals appear.
- [page](https://create.roblox.com/docs/resources/modules/scavenger-hunt) **[[ui-ux-design]]** Default autoDismissTime is 20 seconds; set to 0 to disable auto-dismiss.

## Numbers
- [page](https://create.roblox.com/docs/resources/modules/scavenger-hunt) autoDismissTime default: **20 seconds** (Modal auto-dismiss time; 0 disables)
- [page](https://create.roblox.com/docs/resources/modules/scavenger-hunt) tokenRotationSpeed default: **20 degrees/second** (Token rotation; 0 prevents rotation)
- [page](https://create.roblox.com/docs/resources/modules/scavenger-hunt) navigationBeam segments default: **10** (Segments in beam from player to nearest token)

## Tools
ScavengerHunt module (Creator Store package), Roblox Studio Toolbox, CollectionService, DataStore

## He points to
- Roblox Creator Store: ScavengerHunt package

## Topics
[[building-and-level-design]] [[core-loops-and-game-design]] [[data-persistence]] [[player-psychology-and-game-feel]] [[scripting-and-performance]] [[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
