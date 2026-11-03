---
title: "How to Use ProfileService in Roblox Studio! | Best Way to Save and Manage Player Data in Roblox!"
url: https://youtu.be/vr1fae2qROM
creator: Amora
official: false
advice_density: medium
date: 2023-08-03
views: 27448
transcript: auto-captions
confidence: high
tags: [roblox, amorascripting, youtube-learn]
creator_trust: MIXED
creator_score: 7.2
---

> [!note] Trust: MIXED (credibility audit score 7.2): do not rely on this creator alone; confirm a recommendation with a second source. See [[creator-credibility]].

# How to Use ProfileService in Roblox Studio! | Best Way to Save and Manage Player Data in Roblox!

[Watch](https://youtu.be/vr1fae2qROM) | AmoraScripting | 27,448 views | 2023-08-03

## Summary
Tutorial on using ProfileService (a Roblox data-saving module) in Studio: installing the module, building a DataManager with profile loading, session-locked release, reconcile for template updates, leaderstats binding, updating cash from a proximity prompt, and using Profile:Mock() for testing without saving.

## Tips
- [0:00](https://youtu.be/vr1fae2qROM?t=0) **[[data-persistence]]** Use ProfileService for player data: it handles session locking automatically and scales to large player counts.
- [3:50](https://youtu.be/vr1fae2qROM?t=230) **[[data-persistence]]** Store a template table of default values (e.g. cash = 0) and load profiles against it so new keys are added to profile data.
- [5:46](https://youtu.be/vr1fae2qROM?t=346) **[[data-persistence]]** Call profile:AddUserId and profile:Reconcile after loading so the profile is tied to the player and missing template keys are filled in.
- [6:27](https://youtu.be/vr1fae2qROM?t=387) **[[data-persistence]]** Listen to profile:ListenToRelease and kick the player if the profile is released, to avoid data loss from duplicate sessions.
- [6:27](https://youtu.be/vr1fae2qROM?t=387) **[[data-persistence]]** Only keep the profile in a table if the player is still a descendant of Players; otherwise release the profile and kick.
- [7:52](https://youtu.be/vr1fae2qROM?t=472) **[[data-persistence]]** On PlayerRemoving, release the player's profile so the session lock is cleared and data is saved.
- [8:33](https://youtu.be/vr1fae2qROM?t=513) **[[scripting-and-performance]]** Handle players already in the server by looping over Players:GetPlayers() with task.spawn(playerAdded) alongside the PlayerAdded connection.
- [9:23](https://youtu.be/vr1fae2qROM?t=563) **[[common-mistakes]]** Enable Game Settings > Security > Studio Access to API Services, or Studio cannot access DataStores and saving will fail.
- [10:20](https://youtu.be/vr1fae2qROM?t=620) **[[client-server-and-remotes]]** Modify player data only on the server, e.g. from a ProximityPrompt Triggered handler, never trusting client values.
- [11:01](https://youtu.be/vr1fae2qROM?t=661) **[[data-persistence]]** Always check that the profile exists before changing data; return early if it is nil.
- [11:43](https://youtu.be/vr1fae2qROM?t=703) **[[data-persistence]]** Change profile.Data values, then mirror them to leaderstats values; the profile autosaves without extra calls.
- [12:23](https://youtu.be/vr1fae2qROM?t=743) **[[testing-debugging-and-qa]]** Append :Mock() to the ProfileStore:LoadProfileAsync setup to test without saving; remove it before publishing to keep real saves.
- [3:09](https://youtu.be/vr1fae2qROM?t=189) **[[code-architecture-and-frameworks]]** Organize data code as a modules folder in ServerScriptService with separate DataManager, Template and LeaderStats modules.
- [2:26](https://youtu.be/vr1fae2qROM?t=146) **[[common-mistakes]]** Name the leaderstats folder exactly 'leaderstats' in lowercase, or the leaderboard will not display it.

## Numbers
- [0:00](https://youtu.be/vr1fae2qROM?t=0) Data key name: **"_data_store" used as ProfileStore name in the example**
- [9:39](https://youtu.be/vr1fae2qROM?t=579) Example cash increment: **+20 cash per proximity prompt trigger; prompt duration set to 0.2s**

## Tools
ProfileService, Roblox Studio, Roblox Toolbox

## He points to
- ProfileService module (linked in video description)

## Topics
[[client-server-and-remotes]] [[code-architecture-and-frameworks]] [[common-mistakes]] [[data-persistence]] [[scripting-and-performance]] [[testing-debugging-and-qa]]

Back to [[AmoraScripting - How to make successful Roblox games]]
