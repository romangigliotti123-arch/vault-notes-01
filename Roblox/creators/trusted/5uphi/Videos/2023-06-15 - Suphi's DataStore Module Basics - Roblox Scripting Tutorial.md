---
title: "Suphi's DataStore Module Basics - Roblox Scripting Tutorial"
url: https://youtu.be/UAdE8-AfuMo
creator: Suphi Kaner
official: false
advice_density: medium
date: 2023-06-15
views: 27707
transcript: auto-captions
confidence: high
tags: [roblox, 5uphi, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.8
---

> [!note] Trust: TRUSTED (credibility audit score 8.8): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Suphi's DataStore Module Basics - Roblox Scripting Tutorial

[Watch](https://youtu.be/UAdE8-AfuMo) | 5uphi | 27,707 views | 2023-06-15

## Summary
Tutorial on Suphi's DataStore module: setup, open/save/destroy lifecycle, states and events, templates, and a small game (apples, NPC selling for coins, developer product with forced save, playtime tracking via server-time attribute, and HUD).

## Tips
- [0:21](https://youtu.be/UAdE8-AfuMo?t=21) **[[data-persistence]]** Enable Studio access to API services in game settings Security before testing DataStore; otherwise saves will not work in Studio.
- [2:08](https://youtu.be/UAdE8-AfuMo?t=128) **[[data-persistence]]** DataStore name/scope/key map to folder/subfolder/file; omit scope to use the default 'global' scope.
- [16:39](https://youtu.be/UAdE8-AfuMo?t=999) **[[data-persistence]]** Use a template table in open(); it only fills keys missing from saved data, so adding new keys later won't reset existing values.
- [19:42](https://youtu.be/UAdE8-AfuMo?t=1182) **[[data-persistence]]** Always nil-check DataStore.find results; the module auto-destroys objects on server shutdown.
- [20:22](https://youtu.be/UAdE8-AfuMo?t=1222) **[[data-persistence]]** Don't kick players when open fails; retry open in a loop with a ~6 second wait while the player remains in the server.
- [23:51](https://youtu.be/UAdE8-AfuMo?t=1431) **[[data-persistence]]** Listen to state changed and reopen the DataStore when it closes after repeated save failures, reusing the same handler function.
- [25:14](https://youtu.be/UAdE8-AfuMo?t=1514) **[[scripting-and-performance]]** Read the live state from the DataStore object, not a cached variable captured earlier, since the cached value never updates after open.
- [30:43](https://youtu.be/UAdE8-AfuMo?t=1843) **[[data-persistence]]** Use DataStore.new (not find) in every script that needs the object; it returns the existing object if already created, avoiding race conditions between player-added handlers.
- [31:23](https://youtu.be/UAdE8-AfuMo?t=1883) **[[data-persistence]]** Store custom references (leaderstats folder, player) on the DataStore object to share them across handlers without extra lookups.
- [27:59](https://youtu.be/UAdE8-AfuMo?t=1679) **[[code-architecture-and-frameworks]]** Split systems into separate scripts (leaderstats, player data, shop) that all interact with the same DataStore object instead of one growing script.
- [40:06](https://youtu.be/UAdE8-AfuMo?t=2406) **[[data-persistence]]** Check state == true before writing to a DataStore; writes while closed are never saved.
- [57:14](https://youtu.be/UAdE8-AfuMo?t=3434) **[[monetisation-devproducts]]** For purchases, force DataStore:save() before granting the item; if save fails, deduct the granted amount and return NotProcessedYet so the player can't get it free later.
- [52:26](https://youtu.be/UAdE8-AfuMo?t=3146) **[[monetisation-devproducts]]** Route ProcessReceipt through a table keyed by product ID to add new products by adding one function.
- [1:05:01](https://youtu.be/UAdE8-AfuMo?t=3901) **[[data-persistence]]** Track playtime with a server-time-relative attribute updated in the saving event; the client computes elapsed time locally with no remote calls.
- [1:16:01](https://youtu.be/UAdE8-AfuMo?t=4561) **[[ui-ux-design]]** Align per-second HUD timers to whole seconds by waiting 1 minus (time % 1) so the display ticks cleanly.
- [0:21](https://youtu.be/UAdE8-AfuMo?t=21) **[[scripting-and-performance]]** Set ProximityPrompt hold duration and disable requires line of sight for quick NPC interactions like selling.

## Numbers
- [8:23](https://youtu.be/UAdE8-AfuMo?t=503) DataStore autosave interval: **30 seconds** (Open DataStore saves automatically every 30 seconds)
- [22:27](https://youtu.be/UAdE8-AfuMo?t=1347) Open retry wait: **6 seconds** (Wait between failed open attempts in retry loop)
- [36:39](https://youtu.be/UAdE8-AfuMo?t=2199) Apple spawn interval: **3 seconds** (Demo spawn loop for collectible apples)
- [48:20](https://youtu.be/UAdE8-AfuMo?t=2900) Test product price: **100 Robux** (Demo coin developer product)

## Tools
Roblox Studio, Toolbox, Suphi's DataStore module, Marketplace ProcessReceipt, Roblox Developer Products

## He points to
- Suphi's DataStore module (Roblox Creator Hub Projects forum post and Discord linked in video description)

## Topics
[[code-architecture-and-frameworks]] [[data-persistence]] [[monetisation-devproducts]] [[scripting-and-performance]] [[ui-ux-design]]

Back to [[5uphi - How to make successful Roblox games]]
