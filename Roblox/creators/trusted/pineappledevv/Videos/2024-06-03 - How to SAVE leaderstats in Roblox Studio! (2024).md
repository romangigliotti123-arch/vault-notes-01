---
title: "How to SAVE leaderstats in Roblox Studio! (2024)"
url: https://youtu.be/BOMfj0bSjf0
creator: PineappleDev
official: false
advice_density: medium
date: 2024-06-03
views: 4699
transcript: auto-captions
confidence: high
tags: [roblox, pineappledevv, youtube-learn]
creator_trust: TRUSTED
creator_score: 7.7
---

> [!note] Trust: TRUSTED (credibility audit score 7.7): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# How to SAVE leaderstats in Roblox Studio! (2024)

[Watch](https://youtu.be/BOMfj0bSjf0) | pineappledevv | 4,699 views | 2024-06-03

## Summary
Tutorial on saving leaderstats in Roblox Studio using a ModuleScript in ReplicatedStorage with DataStoreService. Covers saving values from a player's leaderstats folder by UserId, loading on join via a callback, autosave, saving on leave, and enabling Studio API access. Includes a fix to pass the result (not success) to the callback.

## Tips
- [0:13](https://youtu.be/BOMfj0bSjf0?t=13) **[[data-persistence]]** Put the save/load logic in a ModuleScript in ReplicatedStorage and require it from a server Script so the logic is reusable.
- [0:55](https://youtu.be/BOMfj0bSjf0?t=55) **[[data-persistence]]** DataStore keys must be strings; convert UserId with tostring() before calling GetAsync/SetAsync, since numbers are rejected.
- [2:19](https://youtu.be/BOMfj0bSjf0?t=139) **[[data-persistence]]** Wrap DataStore SetAsync/GetAsync in pcall and warn on failure so save errors are visible instead of silent.
- [4:31](https://youtu.be/BOMfj0bSjf0?t=271) **[[data-persistence]]** Load player data on PlayerAdded and save on PlayerRemoving; add an autosave loop in between to limit data loss on crashes.
- [6:34](https://youtu.be/BOMfj0bSjf0?t=394) **[[data-persistence]]** Enable Studio Access to API Services in Game Settings > Security before testing DataStore saves in Studio.
- [3:43](https://youtu.be/BOMfj0bSjf0?t=223) **[[data-persistence]]** Use a callback pattern when loading data so the server continues while the async DataStore read completes.
- [5:12](https://youtu.be/BOMfj0bSjf0?t=312) **[[scripting-and-performance]]** Check that the data table value exists before assigning it to a leaderstat value to avoid nil errors for new players.
- [0:00](https://youtu.be/BOMfj0bSjf0?t=0) **[[common-mistakes]]** This simple script lacks session locking and retries; for production games use a library like ProfileStore to avoid data loss.

## Tools
Roblox Studio, DataStoreService, ModuleScript, Script

## Topics
[[common-mistakes]] [[data-persistence]] [[scripting-and-performance]]

Back to [[pineappledevv - How to make successful Roblox games]]
