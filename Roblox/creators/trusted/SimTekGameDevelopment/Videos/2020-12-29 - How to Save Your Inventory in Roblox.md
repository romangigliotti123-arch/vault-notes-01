---
title: "How to Save Your Inventory in Roblox"
url: https://youtu.be/bFoHE1qWe64
creator: SimTek Game Development
official: false
advice_density: medium
date: 2020-12-29
views: 6380
transcript: auto-captions
confidence: high
tags: [roblox, simtekgamedevelopment, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.2
---

> [!note] Trust: TRUSTED (credibility audit score 8.2): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# How to Save Your Inventory in Roblox

[Watch](https://youtu.be/bFoHE1qWe64) | SimTekGameDevelopment | 6,380 views | 2020-12-29

## Summary
Tutorial on saving a Roblox inventory bag with DataStoreService: enabling API services, a save-on-leave handler, a periodic save loop, and loading saved items back into the client's bag on join. Includes a reduced remote payload (item name instead of whole item).

## Tips
- [0:42](https://youtu.be/bFoHE1qWe64?t=42) **[[data-persistence]]** Enable Game Settings > Security > 'Enable Studio Access to API Services' or DataStores will not work in Studio.
- [4:48](https://youtu.be/bFoHE1qWe64?t=288) **[[data-persistence]]** Create a unique DataStore name per game with GetDataStore and store all player data keyed by player.UserId.
- [5:32](https://youtu.be/bFoHE1qWe64?t=332) **[[data-persistence]]** Save on PlayerRemoving and also run a periodic save loop (~60s in production) to cover crashes or disconnects where leave-save never fires.
- [5:32](https://youtu.be/bFoHE1qWe64?t=332) **[[data-persistence]]** Wrap DataStore calls in pcall for communication errors; the video skips this and calls it risky.
- [8:19](https://youtu.be/bFoHE1qWe64?t=499) **[[data-persistence]]** On load, check the saved data exists before populating; new players have no data and should start empty.
- [3:25](https://youtu.be/bFoHE1qWe64?t=205) **[[client-server-and-remotes]]** Send only the item name through RemoteEvents instead of the whole item table to reduce payload size.
- [10:22](https://youtu.be/bFoHE1qWe64?t=622) **[[data-persistence]]** Expect the last items to be lost if the player leaves abruptly, since the final save may not reach the DataStore before the client closes.

## Numbers
- [6:14](https://youtu.be/bFoHE1qWe64?t=374) Save loop interval: **10 seconds for testing, ~60 seconds suggested for live game** (Periodic save loop interval)

## Tools
Roblox Studio, DataStoreService

## Topics
[[client-server-and-remotes]] [[data-persistence]]

Back to [[SimTekGameDevelopment - How to make successful Roblox games]]
