---
title: "Save Player Data with Roblox Datastores"
url: https://youtu.be/H-cDbjd5-bs
creator: GnomeCode
official: false
advice_density: medium
date: 2022-12-28
views: 180984
transcript: auto-captions
confidence: high
tags: [roblox, gnomecode, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.1
---

> [!note] Trust: TRUSTED (credibility audit score 8.1): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Save Player Data with Roblox Datastores

[Watch](https://youtu.be/H-cDbjd5-bs) | GnomeCode | 180,984 views | 2022-12-28

## Summary
Tutorial on saving player data with DataStoreService in Roblox Studio: creating a session table, saving on PlayerRemoving, retry loops with pcall, loading with defaults, enabling Studio API access, syncing leaderstats with stored data, and handling server shutdown via BindToClose.

## Tips
- [4:11](https://youtu.be/H-cDbjd5-bs?t=251) **[[data-persistence]]** Only save data if the player's session entry exists; saving blank data after a failed load wipes their progress.
- [4:11](https://youtu.be/H-cDbjd5-bs?t=251) **[[data-persistence]]** Wrap DataStore SetAsync/GetAsync in pcall inside a retry loop (about 5 attempts, 3s waits) since requests can fail.
- [12:27](https://youtu.be/H-cDbjd5-bs?t=747) **[[data-persistence]]** Enable 'Studio access to API services' in game settings Security after publishing, or DataStore calls fail in Studio.
- [12:27](https://youtu.be/H-cDbjd5-bs?t=747) **[[data-persistence]]** If loading still fails after retries, kick the player with a 'try again later' message rather than playing with default data.
- [14:01](https://youtu.be/H-cDbjd5-bs?t=841) **[[data-persistence]]** Keep leaderstats values and the stored data table in sync by setting stored values on .Changed events.
- [16:17](https://youtu.be/H-cDbjd5-bs?t=977) **[[data-persistence]]** Editing default values in code does not change already-saved data; existing players keep old stored values.
- [17:41](https://youtu.be/H-cDbjd5-bs?t=1061) **[[data-persistence]]** Use game:BindToClose to save all players on shutdown; you get about 30 seconds, so spawn saves in task.spawn threads.
- [19:45](https://youtu.be/H-cDbjd5-bs?t=1185) **[[data-persistence]]** Skip the BindToClose save logic when RunService:IsStudio() is true to speed up Studio testing.
- [9:50](https://youtu.be/H-cDbjd5-bs?t=590) **[[data-persistence]]** Store default player data in a table on first join (e.g., dollars = 50, owned cars) and assign it to the session table.

## Numbers
- [4:11](https://youtu.be/H-cDbjd5-bs?t=251) Retry attempts for DataStore calls: **5 attempts, 3 seconds apart** (Used for both saving and loading in the tutorial)
- [17:41](https://youtu.be/H-cDbjd5-bs?t=1061) Shutdown save window: **30 seconds** (Time available in BindToClose before server closes)
- [12:27](https://youtu.be/H-cDbjd5-bs?t=747) Load timeout before kick: **About 15 seconds** (Five failed attempts at 3-second waits before kicking)

## Tools
Roblox Studio, DataStoreService, Data Store Editor plugin (paid)

## He points to
- Data Store Editor plugin

## Topics
[[data-persistence]]

Back to [[GnomeCode - How to make successful Roblox games]]
