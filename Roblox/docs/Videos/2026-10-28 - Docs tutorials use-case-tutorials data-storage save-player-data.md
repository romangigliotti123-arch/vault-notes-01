---
title: "Docs: tutorials / use-case-tutorials / data-storage / save-player-data"
url: https://create.roblox.com/docs/tutorials/use-case-tutorials/data-storage/save-player-data.md
creator: Roblox Creator Docs
official: true
advice_density: high
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: tutorials / use-case-tutorials / data-storage / save-player-data

[Open](https://create.roblox.com/docs/tutorials/use-case-tutorials/data-storage/save-player-data.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Official Roblox docs tutorial on saving player gold and position with standard data stores: enabling Studio API access, creating a server-side DataStore, key/value rules, SetAsync/GetAsync with pcall, autosave loop, and splitting Vector3 into numbers for storage.

## Tips
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/data-storage/save-player-data) **[[data-persistence]]** Only call DataStoreService from server-side Scripts. Clients have no data store access, and exploiters could steal or overwrite other players' data otherwise.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/data-storage/save-player-data) **[[data-persistence]]** Give each data store a unique name (e.g. "PlayerGold") so data stays organized and doesn't conflict with other stores.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/data-storage/save-player-data) **[[data-persistence]]** Data store keys must be strings; values can be numbers, strings, booleans or tables. Use the player's userId as the key.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/data-storage/save-player-data) **[[data-persistence]]** Wrap GetAsync and SetAsync in pcall and warn on failure, so errors are logged and you can debug failed saves or loads.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/data-storage/save-player-data) **[[data-persistence]]** Save on PlayerRemoving as well as on an autosave loop, so progress isn't lost on unexpected disconnects.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/data-storage/save-player-data) **[[data-persistence]]** Set autosave interval between 30 and 120 seconds, depending on how often players gain meaningful progress, to avoid throttling and request limits.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/data-storage/save-player-data) **[[data-persistence]]** Data stores can't store Vector3 or CFrame directly. Split positions into X, Y, Z numbers in a table and rebuild the Vector3 on load.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/data-storage/save-player-data) **[[scripting-and-performance]]** Run autosave loops in coroutine.wrap so they don't block the rest of the script; loop while player.Parent is set.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/data-storage/save-player-data) **[[scripting-and-performance]]** Use a constant such as AUTOSAVE_INTERVAL for save frequency so it can be tuned in one place.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/data-storage/save-player-data) **[[client-server-and-remotes]]** Pass the UI update through a RemoteEvent to the client with the saved value and a doTween flag, so the HUD shows loaded gold without tweening on join.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/data-storage/save-player-data) **[[testing-debugging-and-qa]]** To test data stores in Studio, publish the place first, then enable File > Experience Settings > Security > Enable Studio Access to API Services.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/data-storage/save-player-data) **[[common-mistakes]]** Without data stores, player score and position reset every time they leave, so persistence must be added explicitly.

## Numbers
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/data-storage/save-player-data) autosave interval: **30 to 120 seconds (tutorial uses 30)** (Recommended range; depends on how often players gain progress)

## Tools
DataStoreService, Studio Experience Settings > Security, coroutine.wrap, task.wait, PivotTo / GetPivot

## He points to
- Gold Rush data store tutorial start and complete .rbxl files

## Topics
[[client-server-and-remotes]] [[common-mistakes]] [[data-persistence]] [[scripting-and-performance]] [[testing-debugging-and-qa]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
