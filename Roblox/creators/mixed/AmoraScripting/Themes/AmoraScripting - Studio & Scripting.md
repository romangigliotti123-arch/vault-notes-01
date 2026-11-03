---
title: AmoraScripting - Studio & Scripting
creator: AmoraScripting
tags: [roblox, amorascripting, theme]
creator_trust: MIXED
creator_score: 7.2
---

> [!note] Trust: MIXED (credibility audit score 7.2): do not rely on this creator alone; confirm a recommendation with a second source. See [[creator-credibility]].

# AmoraScripting: Studio & Scripting

All AmoraScripting tips on this theme, grouped by topic, oldest first. Cross-creator synthesis: see [[README]] in roblox-kb.

## [[scripting-and-performance]]
- 2023-07-31 [2:15](https://youtu.be/KPK86YQ6t-Y?t=135) Set a Script's Run Context to Client so it runs inside a part; regular LocalScripts only run in specific containers like backpack, character, PlayerGui, or PlayerScripts. ([[2023-07-31 - How to Make Area Music in Roblox Studio in 2023! Music by Region Roblo|How to Make Area Music in Roblox Studio in 2023! |]])
- 2023-07-31 [3:57](https://youtu.be/KPK86YQ6t-Y?t=237) Compute Region3 corners from part.Position ± part.Size/2 instead of placing manual corner parts. ([[2023-07-31 - How to Make Area Music in Roblox Studio in 2023! Music by Region Roblo|How to Make Area Music in Roblox Studio in 2023! |]])
- 2023-07-31 [6:21](https://youtu.be/KPK86YQ6t-Y?t=381) Use OverlapParams with FilterType Include and the character as the filter descendant so only the player's own parts are detected. ([[2023-07-31 - How to Make Area Music in Roblox Studio in 2023! Music by Region Roblo|How to Make Area Music in Roblox Studio in 2023! |]])
- 2023-07-31 [7:44](https://youtu.be/KPK86YQ6t-Y?t=464) Use workspace:GetPartBoundsInBox instead of the deprecated FindPartsInRegion3. ([[2023-07-31 - How to Make Area Music in Roblox Studio in 2023! Music by Region Roblo|How to Make Area Music in Roblox Studio in 2023! |]])
- 2023-07-31 [5:39](https://youtu.be/KPK86YQ6t-Y?t=339) Reset the inRegion flag each frame before the check so music stops if the player leaves the zone. ([[2023-07-31 - How to Make Area Music in Roblox Studio in 2023! Music by Region Roblo|How to Make Area Music in Roblox Studio in 2023! |]])
- 2023-08-03 [8:33](https://youtu.be/vr1fae2qROM?t=513) Handle players already in the server by looping over Players:GetPlayers() with task.spawn(playerAdded) alongside the PlayerAdded connection. ([[2023-08-03 - How to Use ProfileService in Roblox Studio! Best Way to Save and Manag|How to Use ProfileService in Roblox Studio! | Best]])

## [[code-architecture-and-frameworks]]
- 2023-08-03 [3:09](https://youtu.be/vr1fae2qROM?t=189) Organize data code as a modules folder in ServerScriptService with separate DataManager, Template and LeaderStats modules. ([[2023-08-03 - How to Use ProfileService in Roblox Studio! Best Way to Save and Manag|How to Use ProfileService in Roblox Studio! | Best]])

## [[client-server-and-remotes]]
- 2023-08-03 [10:20](https://youtu.be/vr1fae2qROM?t=620) Modify player data only on the server, e.g. from a ProximityPrompt Triggered handler, never trusting client values. ([[2023-08-03 - How to Use ProfileService in Roblox Studio! Best Way to Save and Manag|How to Use ProfileService in Roblox Studio! | Best]])

## [[data-persistence]]
- 2023-08-03 [0:00](https://youtu.be/vr1fae2qROM?t=0) Use ProfileService for player data: it handles session locking automatically and scales to large player counts. ([[2023-08-03 - How to Use ProfileService in Roblox Studio! Best Way to Save and Manag|How to Use ProfileService in Roblox Studio! | Best]])
- 2023-08-03 [3:50](https://youtu.be/vr1fae2qROM?t=230) Store a template table of default values (e.g. cash = 0) and load profiles against it so new keys are added to profile data. ([[2023-08-03 - How to Use ProfileService in Roblox Studio! Best Way to Save and Manag|How to Use ProfileService in Roblox Studio! | Best]])
- 2023-08-03 [5:46](https://youtu.be/vr1fae2qROM?t=346) Call profile:AddUserId and profile:Reconcile after loading so the profile is tied to the player and missing template keys are filled in. ([[2023-08-03 - How to Use ProfileService in Roblox Studio! Best Way to Save and Manag|How to Use ProfileService in Roblox Studio! | Best]])
- 2023-08-03 [6:27](https://youtu.be/vr1fae2qROM?t=387) Listen to profile:ListenToRelease and kick the player if the profile is released, to avoid data loss from duplicate sessions. ([[2023-08-03 - How to Use ProfileService in Roblox Studio! Best Way to Save and Manag|How to Use ProfileService in Roblox Studio! | Best]])
- 2023-08-03 [6:27](https://youtu.be/vr1fae2qROM?t=387) Only keep the profile in a table if the player is still a descendant of Players; otherwise release the profile and kick. ([[2023-08-03 - How to Use ProfileService in Roblox Studio! Best Way to Save and Manag|How to Use ProfileService in Roblox Studio! | Best]])
- 2023-08-03 [7:52](https://youtu.be/vr1fae2qROM?t=472) On PlayerRemoving, release the player's profile so the session lock is cleared and data is saved. ([[2023-08-03 - How to Use ProfileService in Roblox Studio! Best Way to Save and Manag|How to Use ProfileService in Roblox Studio! | Best]])
- 2023-08-03 [11:01](https://youtu.be/vr1fae2qROM?t=661) Always check that the profile exists before changing data; return early if it is nil. ([[2023-08-03 - How to Use ProfileService in Roblox Studio! Best Way to Save and Manag|How to Use ProfileService in Roblox Studio! | Best]])
- 2023-08-03 [11:43](https://youtu.be/vr1fae2qROM?t=703) Change profile.Data values, then mirror them to leaderstats values; the profile autosaves without extra calls. ([[2023-08-03 - How to Use ProfileService in Roblox Studio! Best Way to Save and Manag|How to Use ProfileService in Roblox Studio! | Best]])

## [[building-and-level-design]]
- 2023-07-31 [0:36](https://youtu.be/KPK86YQ6t-Y?t=36) Make zone parts Anchored, CanCollide false, Transparency 1, and tall enough that players can't escape above them. ([[2023-07-31 - How to Make Area Music in Roblox Studio in 2023! Music by Region Roblo|How to Make Area Music in Roblox Studio in 2023! |]])

Up: [[AmoraScripting - How to make successful Roblox games]]
