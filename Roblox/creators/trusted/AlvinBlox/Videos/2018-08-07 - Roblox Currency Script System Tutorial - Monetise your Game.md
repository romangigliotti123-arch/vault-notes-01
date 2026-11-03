---
title: "Roblox Currency Script System Tutorial - Monetise your Game"
url: https://youtu.be/h92s4Xn26oc
creator: AlvinBlox
official: false
advice_density: medium
date: 2018-08-07
views: 302535
transcript: auto-captions
confidence: high
tags: [roblox, alvinblox, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.1
---

> [!note] Trust: TRUSTED (credibility audit score 8.1): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Roblox Currency Script System Tutorial - Monetise your Game

[Watch](https://youtu.be/h92s4Xn26oc) | AlvinBlox | 302,535 views | 2018-08-07

## Summary
Tutorial on building a basic Roblox currency system: leaderstats creation, DataStore save/load on join/leave and BindToClose, then Developer Product purchases via MarketplaceService.ProcessReceipt with receipt-based duplicate prevention and a prompt button. Scripting walkthrough, not a growth or monetisation strategy video.

## Tips
- [2:31](https://youtu.be/h92s4Xn26oc?t=151) **[[scripting-and-performance]]** Name the folder exactly 'leaderstats' (lowercase l, correct casing) or the leaderboard will not appear in the top-right corner.
- [5:12](https://youtu.be/h92s4Xn26oc?t=312) **[[scripting-and-performance]]** Use the player's UserId in the DataStore key, not their name, and never rename the DataStore after publishing or player data gets wiped.
- [9:17](https://youtu.be/h92s4Xn26oc?t=557) **[[scripting-and-performance]]** Wrap DataStore GetAsync in pcall so a DataStore error is handled instead of breaking the whole script.
- [12:58](https://youtu.be/h92s4Xn26oc?t=778) **[[scripting-and-performance]]** Save player data in PlayerRemoving and kick all players in BindToClose with a short wait, so the last player's data is saved before the server shuts down.
- [20:37](https://youtu.be/h92s4Xn26oc?t=1237) **[[scripting-and-performance]]** Enable Studio Access to API Services in game config to test DataStores in Play Solo; note Studio writes to the live DataStore used by real servers.
- [26:40](https://youtu.be/h92s4Xn26oc?t=1600) **[[monetisation-devproducts]]** Use Developer Products (not gamepasses) for consumable currency, since they can be bought repeatedly; gamepasses are one-time purchases.
- [31:31](https://youtu.be/h92s4Xn26oc?t=1891) **[[scripting-and-performance]]** In ProcessReceipt, store each PurchaseId in a DataStore and check it before granting, so a purchase is never granted twice; return PurchaseGranted only after rewards are saved.
- [35:45](https://youtu.be/h92s4Xn26oc?t=2145) **[[scripting-and-performance]]** If the buyer has left before ProcessReceipt fires, return NotProcessedYet so the reward is granted when they rejoin.
- [26:40](https://youtu.be/h92s4Xn26oc?t=1600) **[[pricing]]** In the speaker's example, 100 cash was priced at 10 Robux; set Developer Product prices in the Configure Place Developer Products tab.

## Numbers
- [26:40](https://youtu.be/h92s4Xn26oc?t=1600) Developer Product price: **100 cash = 10 Robux (example)**
- [5:12](https://youtu.be/h92s4Xn26oc?t=312) Starting currency for new players: **50 (example default)**
- [16:24](https://youtu.be/h92s4Xn26oc?t=984) BindToClose delay: **~5 seconds**
- [23:20](https://youtu.be/h92s4Xn26oc?t=1400) Server shutdown wait observed: **about 5 seconds before server removed**

## Games
- **Generic currency/shop demo game (unnamed)** [0:00](https://youtu.be/h92s4Xn26oc?t=0): Video uses a demo place only; no named commercial game discussed. Currency system is the teaching example.

## Tools
Roblox Studio, Luau scripts (ServerScriptService), DataStoreService, MarketplaceService, Developer Products page on Roblox website

## He points to
- Albin Blocks YouTube channel (next video: shop system)

## Quotes
- [25:18](https://youtu.be/h92s4Xn26oc?t=1518) "A developer product can be bought multiple times, so it's a great way to monetize your game along with game passes."
- [5:12](https://youtu.be/h92s4Xn26oc?t=312) "It's not good practice to put the player's name in the DataStore; it's best to use their user ID."

## On screen
Shows Studio explorer and a leaderstats display with Coins 0 in-game, the Configure Place Developer Products tab listing a '100 cash' product at 10 Robux, a Create Developer Product form, and the ProcessReceipt-era script editor. No analytics numbers or thumbnails beyond a Roblox game page preview.

## Topics
[[monetisation-devproducts]] [[pricing]] [[scripting-and-performance]]

Back to [[AlvinBlox - How to make successful Roblox games]]
