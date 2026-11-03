---
title: "Datastore - Save Your Leaderboard!"
url: https://youtu.be/10uZXhWd_Aw
creator: SimTek Game Development
official: false
advice_density: medium
date: 2025-05-17
views: 8294
transcript: auto-captions
confidence: high
tags: [roblox, simtekgamedevelopment, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.2
---

> [!note] Trust: TRUSTED (credibility audit score 8.2): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Datastore - Save Your Leaderboard!

[Watch](https://youtu.be/10uZXhWd_Aw) | SimTekGameDevelopment | 8,294 views | 2025-05-17

## Summary
Tutorial on building a general leaderboard system in Roblox Studio: leaderstats folder on player join, pickups that increment stats by name, DataStoreService save/load with pcall, kick on failed load, periodic autosave loop, save on PlayerRemoving, and clearing test data. Includes Studio API access setting.

## Tips
- [1:44](https://youtu.be/10uZXhWd_Aw?t=104) **[[data-persistence]]** Name the leaderboard folder exactly 'leaderstats' (lowercase l) or Roblox won't display it in the player list corner.
- [8:08](https://youtu.be/10uZXhWd_Aw?t=488) **[[data-persistence]]** Make pickup part names match leaderstat names exactly; the pickup script uses its name to know which stat to increment.
- [9:38](https://youtu.be/10uZXhWd_Aw?t=578) **[[data-persistence]]** Enable 'Studio Access to API Services' in Game Settings > Security or DataStore calls will fail in Studio; this is commonly missed.
- [13:05](https://youtu.be/10uZXhWd_Aw?t=785) **[[data-persistence]]** Autosave player data every ~60 seconds in a spawned loop, not every few seconds, because DataStore calls are taxing on the game.
- [15:08](https://youtu.be/10uZXhWd_Aw?t=908) **[[data-persistence]]** Wrap DataStore GetAsync/SetAsync in pcall; on load failure kick the player instead of saving, so a failed load never overwrites their history.
- [15:49](https://youtu.be/10uZXhWd_Aw?t=949) **[[data-persistence]]** Use WaitForChild on leaderstats when loading data, since another script may add the leaderboard after PlayerAdded fires.
- [16:30](https://youtu.be/10uZXhWd_Aw?t=990) **[[data-persistence]]** Write loaded values by stat name via a generic loop over data, so one save/load script works for any integer or number leaderboard.
- [22:40](https://youtu.be/10uZXhWd_Aw?t=1360) **[[data-persistence]]** Save data on PlayerRemoving as well as periodically; the periodic loop covers crashes and failed exit saves.
- [25:28](https://youtu.be/10uZXhWd_Aw?t=1528) **[[data-persistence]]** To reset test data, temporarily call SetAsync with an empty value for the player key, run once, then comment the line out.
- [1:02](https://youtu.be/10uZXhWd_Aw?t=62) **[[core-loops-and-game-design]]** Build a generic pickup script driven by part name so new resources (wood, grass, stone) are added by duplicating a part and renaming it.

## Numbers
- [0:00](https://youtu.be/10uZXhWd_Aw?t=0) Autosave interval: **60 seconds recommended (30 max)** (Periodic save loop for player leaderstats)

## Tools
Roblox Studio, Luau, DataStoreService

## Topics
[[core-loops-and-game-design]] [[data-persistence]]

Back to [[SimTekGameDevelopment - How to make successful Roblox games]]
