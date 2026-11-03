---
title: "DataStores - Beginners to Advanced"
url: https://devforum.roblox.com/t/datastores-beginners-to-advanced/1275421
creator: Roblox DevForum
official: false
advice_density: high
date: 2021-06-06
views: 656
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# DataStores - Beginners to Advanced

[Open](https://devforum.roblox.com/t/datastores-beginners-to-advanced/1275421) | Roblox DevForum | 656 views | 2021-06-06

## Summary
Tutorial building a DataStore system in Luau: GetAsync/SetAsync basics, BindToClose for Studio shutdown, pcall and retry loops, UpdateAsync over SetAsync, autosaving, shutdown saving, Berezaa's ordered-DataStore versioning for corruption recovery, and SessionLocking to prevent item duping. Author warns it is less safe than DataStore2 or ProfileService.

## Tips
- [page](https://devforum.roblox.com/t/datastores-beginners-to-advanced/1275421) **[[data-persistence]]** Use DataStore2 or ProfileService for production saving; the author says his hand-rolled version is less tested and may contain bugs.
- [page](https://devforum.roblox.com/t/datastores-beginners-to-advanced/1275421) **[[data-persistence]]** Parent leaderstats to the player last, after GetAsync finishes, so you can tell a loaded 0 from a new player's default 0.
- [page](https://devforum.roblox.com/t/datastores-beginners-to-advanced/1275421) **[[data-persistence]]** Add BindToClose to save all players on shutdown; PlayerRemoving alone often doesn't fire in Studio when the session stops.
- [page](https://devforum.roblox.com/t/datastores-beginners-to-advanced/1275421) **[[data-persistence]]** Wrap DataStore calls in pcall and retry until success or the player leaves, using a request-budget wait before each call.
- [page](https://devforum.roblox.com/t/datastores-beginners-to-advanced/1275421) **[[data-persistence]]** Use UpdateAsync instead of SetAsync so concurrent server writes to the same key re-run your function rather than overwrite data.
- [page](https://devforum.roblox.com/t/datastores-beginners-to-advanced/1275421) **[[data-persistence]]** Autosave periodically (author uses a 60-second loop) so a shutdown loses only part of a session rather than all of it.
- [page](https://devforum.roblox.com/t/datastores-beginners-to-advanced/1275421) **[[data-persistence]]** Under BindToClose, skip waiting when not in Studio, since Roblox gives only 30 seconds before forced shutdown; save all players in parallel.
- [page](https://devforum.roblox.com/t/datastores-beginners-to-advanced/1275421) **[[data-persistence]]** Use a session lock (timestamp, treated as dead after 30 minutes) to stop players rejoining before the last save from duplicating items.
- [page](https://devforum.roblox.com/t/datastores-beginners-to-advanced/1275421) **[[data-persistence]]** Use a dontLeave flag so autosaves keep the session lock while leaving saves release it.
- [page](https://devforum.roblox.com/t/datastores-beginners-to-advanced/1275421) **[[data-persistence]]** Handle GetAsync errors 501/504 as corruption and stop retrying; fall back to an older version if using ordered-DataStore versioning.
- [page](https://devforum.roblox.com/t/datastores-beginners-to-advanced/1275421) **[[scripting-and-performance]]** Pass the function, then self, then arguments to pcall (pcall(dataStore.GetAsync, dataStore, key)) rather than wrapping in an anonymous function.
- [page](https://devforum.roblox.com/t/datastores-beginners-to-advanced/1275421) **[[scripting-and-performance]]** Use ipairs for arrays and Players:GetPlayers() rather than GetChildren on the Players service.

## Numbers
- [page](https://devforum.roblox.com/t/datastores-beginners-to-advanced/1275421) Session lock timeout: **1800 seconds (30 minutes)** (Session treated as dead after this; takeover allowed)
- [page](https://devforum.roblox.com/t/datastores-beginners-to-advanced/1275421) Shutdown wait: **30 seconds** (Roblox grace period before forced shutdown)
- [page](https://devforum.roblox.com/t/datastores-beginners-to-advanced/1275421) Autosave interval: **60 seconds** (Author's autosave loop wait)
- [page](https://devforum.roblox.com/t/datastores-beginners-to-advanced/1275421) Lock retry wait: **5 seconds** (Wait before retrying a locked session)
- [page](https://devforum.roblox.com/t/datastores-beginners-to-advanced/1275421) Ordered page size: **100 elements** (GetSortedAsync page size; only first page checked in example)

## Tools
DataStoreService, OrderedDataStore, Visual Studio Code, ColdCode, DataStore2, ProfileService

## He points to
- DataStore2
- ProfileService
- Berezaa's DataStore method (DevForum)
- ArtFoundation 'Session locking explained' post
- colbert2677 request budget function
- Disgusted by You#8532 exponential wait suggestion

## Topics
[[data-persistence]] [[scripting-and-performance]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
