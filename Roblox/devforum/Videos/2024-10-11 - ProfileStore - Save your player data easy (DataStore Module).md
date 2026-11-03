---
title: "ProfileStore - Save your player data easy (DataStore Module)"
url: https://devforum.roblox.com/t/profilestore-save-your-player-data-easy-datastore-module/3190543
creator: Roblox DevForum
official: false
advice_density: medium
date: 2024-10-11
views: 1528
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# ProfileStore - Save your player data easy (DataStore Module)

[Open](https://devforum.roblox.com/t/profilestore-save-your-player-data-easy-datastore-module/3190543) | Roblox DevForum | 1,528 views | 2024-10-11

## Summary
Documentation page for ProfileStore, a DataStore wrapper module by loleris and successor to ProfileService. Covers session locking, auto-save, MessagingService-based conflict resolution, changes from ProfileService, backwards compatibility, and a sample PlayerAdded/PlayerRemoving integration.

## Tips
- [page](https://devforum.roblox.com/t/profilestore-save-your-player-data-easy-datastore-module/3190543) **[[data-persistence]]** Use one profile per player with a session lock so data is not accessed by multiple servers at once, preventing item dupes in trading games.
- [page](https://devforum.roblox.com/t/profilestore-save-your-player-data-easy-datastore-module/3190543) **[[data-persistence]]** Call profile:Reconcile() after StartSessionAsync and set defaults in the PROFILE_TEMPLATE so new keys are filled in and nil checks are unnecessary.
- [page](https://devforum.roblox.com/t/profilestore-save-your-player-data-easy-datastore-module/3190543) **[[data-persistence]]** Call profile:AddUserId(player.UserId) on load for GDPR compliance.
- [page](https://devforum.roblox.com/t/profilestore-save-your-player-data-easy-datastore-module/3190543) **[[data-persistence]]** Pass a Cancel function to StartSessionAsync that returns true when the player has left, so loads for departed players stop early.
- [page](https://devforum.roblox.com/t/profilestore-save-your-player-data-easy-datastore-module/3190543) **[[data-persistence]]** Call profile:EndSession() in PlayerRemoving and kick players on OnSessionEnd so stale sessions are not kept.
- [page](https://devforum.roblox.com/t/profilestore-save-your-player-data-easy-datastore-module/3190543) **[[data-persistence]]** Use ProfileStore:MessageAsync() for cross-server data writes such as player gifting instead of writing to DataStores directly.
- [page](https://devforum.roblox.com/t/profilestore-save-your-player-data-easy-datastore-module/3190543) **[[data-persistence]]** Do not use ProfileStore for leaderboards or global state; it is designed only for per-player data.
- [page](https://devforum.roblox.com/t/profilestore-save-your-player-data-easy-datastore-module/3190543) **[[data-persistence]]** Test migration from ProfileService in Studio with API access before deploying live, since old ProfileService may fail to reload profiles after MessageAsync is used.
- [page](https://devforum.roblox.com/t/profilestore-save-your-player-data-easy-datastore-module/3190543) **[[luau-language-and-types]]** Type profile tables with typeof(PlayerStore:StartSessionAsync()) to get autocompletion from ProfileStore's Luau types.

## Numbers
- [page](https://devforum.roblox.com/t/profilestore-save-your-player-data-easy-datastore-module/3190543) Default auto-save period: **300 seconds (up from 30 in ProfileService)** (ProfileStore default auto-save interval, about 10x fewer DataStore calls)
- [page](https://devforum.roblox.com/t/profilestore-save-your-player-data-easy-datastore-module/3190543) DataStore queue: **Replaced 7 second queue with queue that runs as soon as previous calls finish** (Applies to calls on the same DataStore key)
- [page](https://devforum.roblox.com/t/profilestore-save-your-player-data-easy-datastore-module/3190543) Notable game visits: **Grow a Garden over 30B; Dead Rails over 5B** (Games listed as using ProfileStore)

## Games
- **Grow a Garden**: Listed as using ProfileStore with over 30B visits.
- **Dead Rails**: Listed as using ProfileStore with over 5B visits.

## Tools
ProfileStore, ProfileService, MessagingService, Replica, Sera

## He points to
- ProfileStore wiki
- Rileybytes YouTube tutorials on ProfileStore overview and developer product handling
- Replica
- Sera

## Quotes
- [page](https://devforum.roblox.com/t/profilestore-save-your-player-data-easy-datastore-module/3190543) "ProfileStore is not designed (and never will be) for in-game leaderboards or any kind of global state."
- [page](https://devforum.roblox.com/t/profilestore-save-your-player-data-easy-datastore-module/3190543) "Session locking addresses the issue of data access from more than one game server (which can cause item dupes in games with trading)."

## Topics
[[data-persistence]] [[luau-language-and-types]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
