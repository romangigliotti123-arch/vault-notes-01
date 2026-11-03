---
title: "Docs: tutorials / use-case-tutorials / scripting / intermediate-scripting / save-data"
url: https://create.roblox.com/docs/tutorials/use-case-tutorials/scripting/intermediate-scripting/save-data.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: tutorials / use-case-tutorials / scripting / intermediate-scripting / save-data

[Open](https://create.roblox.com/docs/tutorials/use-case-tutorials/scripting/intermediate-scripting/save-data.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs tutorial on persistent data: enabling Studio API access, creating a DataStore, SetAsync/GetAsync wrapped in pcall, caching gold in a table and saving on PlayerRemoving, and saving character position as separate numbers.

## Tips
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/scripting/intermediate-scripting/save-data) **[[data-persistence]]** Enable Studio Access to API Services in Experience Settings > Security (game must be published) or DataStore calls won't work in Studio playtests.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/scripting/intermediate-scripting/save-data) **[[data-persistence]]** Wrap GetAsync/SetAsync in pcall; these are network calls that can fail, and failures should be logged with warn.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/scripting/intermediate-scripting/save-data) **[[data-persistence]]** Don't write to a DataStore on every event (e.g. each gold pickup). Keep values in a local table and save periodically or on PlayerRemoving; excess requests are queued and dropped when the queue fills.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/scripting/intermediate-scripting/save-data) **[[data-persistence]]** Clear the player's entry from the local cache table on PlayerRemoving so the table doesn't grow over the server's lifetime.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/scripting/intermediate-scripting/save-data) **[[data-persistence]]** DataStores only store basic types; store Vector3/CFrame as separate X, Y, Z numbers in a table.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/scripting/intermediate-scripting/save-data) **[[scripting-and-performance]]** Handle a nil result from GetAsync (new player) by defaulting to 0 before using it; also check the pcall success flag before indexing returned data.

## Games
- **Gold Rush**: Official sample game the tutorial points to for testing data saving and an enhanced GoldManager with UI and auto-save.

## Tools
DataStoreService, Players service, pcall, Roblox Studio Experience Settings

## He points to
- Gold Rush sample game

## Topics
[[data-persistence]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
