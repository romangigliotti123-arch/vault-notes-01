---
title: GnomeCode - Numbers & Benchmarks
tags: [roblox, gnomecode]
creator_trust: TRUSTED
creator_score: 8.1
---

> [!note] Trust: TRUSTED (credibility audit score 8.1): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# GnomeCode: Numbers & Benchmarks

| Date | Topic | Metric | Value | Context | Source |
|---|---|---|---|---|---|
| 2020-05-02 | physics-pathfinding-and-npc-ai | AgentHeight | 15 studs | Monster height measured in-world, used for pathfinding agent | [11:04](https://youtu.be/uF-BGGv6otQ?t=664) |
| 2020-05-02 | physics-pathfinding-and-npc-ai | AgentRadius | 4 studs | Half of ~8-stud diameter monster width | [11:04](https://youtu.be/uF-BGGv6otQ?t=664) |
| 2020-05-02 | physics-pathfinding-and-npc-ai | Patrol pause | 2 seconds | Wait between waypoints in patrol example | [14:54](https://youtu.be/uF-BGGv6otQ?t=894) |
| 2020-05-02 | mindset-and-strategy | Subscribers | 1000 | Channel milestone mentioned at start of video | [0:00](https://youtu.be/uF-BGGv6otQ?t=0) |
| 2021-06-14 | retention-d1-d7 | Rejoin cost | Kicked player must reload from website and redo menu and teleport | Illustrates why kicks on death hurt replayability | [10:33](https://youtu.be/0rMO-VHSuGs?t=633) |
| 2021-06-14 | core-loops-and-game-design | Max walk distance | ~10 seconds | Speaker's guideline for distance between points of interest | [20:52](https://youtu.be/0rMO-VHSuGs?t=1252) |
| 2021-07-06 | building-and-level-design | Walk time across oversized map | ~90 seconds | Speaker timed walking the length of an old, mostly empty build | [13:49](https://youtu.be/7vXk_YqxW-c?t=829) |
| 2021-07-06 | building-and-level-design | Window section width and grid increment | 5 studs | Building sized 40.5 studs per side using 5-stud sections plus 0.5 offset | [20:32](https://youtu.be/7vXk_YqxW-c?t=1232) |
| 2021-07-06 | building-and-level-design | Unsnapped building size | 52.082 by 41 by 38 studs | Example of messy decimals from freehand building without increments | [20:32](https://youtu.be/7vXk_YqxW-c?t=1232) |
| 2021-07-06 | building-and-level-design | Increment guide | 10 / 5 / 1 / 0.5 / 0.25 / 0.2 / 0.1 studs | Suggested snapping sizes from big walls down to fine detail | [22:35](https://youtu.be/7vXk_YqxW-c?t=1355) |
| 2021-08-26 | anti-exploit-and-security | Suspicious creator follower count | ~100,000 followers on a linked account (possibly botted) |  | [1:25](https://youtu.be/oHgtXdgJF5U?t=85) |
| 2021-12-14 | building-and-level-design | waypoints | 12 | Numbered waypoints placed at each turn of the example path | [4:29](https://youtu.be/DanjB0cTfw0?t=269) |
| 2022-09-23 | scripting-and-performance | Humanoid:MoveTo timeout | 8 seconds | Humanoid stops walking after eight seconds per the Wiki's MoveTo docs | [18:57](https://youtu.be/aFKaY-PmR08?t=1137) |
| 2022-09-23 | scripting-and-performance | Velocity threshold in demo script | 200 | Demo trampoline script checks root velocity below 200 before applying force | [17:12](https://youtu.be/aFKaY-PmR08?t=1032) |
| 2022-11-26 | vfx-and-particles | Tween duration | 2 seconds | TweenInfo time used in example | [2:03](https://youtu.be/SySp1wTsCkY?t=123) |
| 2022-11-26 | vfx-and-particles | Position offset | move up N studs on Y axis | example sets new position from current position plus Vector3 Y offset | [4:08](https://youtu.be/SySp1wTsCkY?t=248) |
| 2022-11-26 | vfx-and-particles | Size increase | 5 studs in every direction | example size tween increases part.size by 5 | [5:30](https://youtu.be/SySp1wTsCkY?t=330) |
| 2022-12-08 | scripting-and-performance | Custom animate script length | ~228 lines vs ~800+ lines default | Custom animate 2 script vs Roblox default animate script | [2:03](https://youtu.be/PNYtTkMidE8?t=123) |
| 2022-12-08 | building-art-and-assets | Example volume setting | 0.3 (default 0.5) | Volume set for pile and grass footstep sounds | [9:03](https://youtu.be/PNYtTkMidE8?t=543) |
| 2022-12-08 | building-art-and-assets | Footprint decay example | 2 to 5 seconds | Footprint fade-out time configurable per footprint type | [9:03](https://youtu.be/PNYtTkMidE8?t=543) |
| 2022-12-15 | scripting-and-performance | Movement distance in demo | 30 studs up | Example part moved upward by CFrame offset | [0:21](https://youtu.be/R-xurNJtx7M?t=21) |
| 2022-12-15 | scripting-and-performance | Tween duration in demo | 3 seconds | Heartbeat-based lerp duration example | [5:29](https://youtu.be/R-xurNJtx7M?t=329) |
| 2022-12-15 | scripting-and-performance | Heartbeat frame delta | ~0.01 seconds | Approximate deltaTime per frame shown in output | [4:49](https://youtu.be/R-xurNJtx7M?t=289) |
| 2022-12-28 | data-persistence | Retry attempts for DataStore calls | 5 attempts, 3 seconds apart | Used for both saving and loading in the tutorial | [4:11](https://youtu.be/H-cDbjd5-bs?t=251) |
| 2022-12-28 | data-persistence | Shutdown save window | 30 seconds | Time available in BindToClose before server closes | [17:41](https://youtu.be/H-cDbjd5-bs?t=1061) |
| 2022-12-28 | data-persistence | Load timeout before kick | About 15 seconds | Five failed attempts at 3-second waits before kicking | [12:27](https://youtu.be/H-cDbjd5-bs?t=747) |
| 2023-03-11 | building-and-level-design | Breaking up walls | Adding two small parts and resizing can roughly triple the detail level of a wall (speaker's claim) |  | [0:00](https://youtu.be/QRwTkEPPChM?t=0) |
| 2023-04-16 | scripting-and-performance | Walk speed reference | 16 studs/s default; speed check threshold 25 studs/s | Max speed threshold used in speed-hack detection example | [14:57](https://youtu.be/2jvahdJnQRI?t=897) |
| 2023-04-16 | anti-exploit-and-security | Observed fall speed | up to ~36 studs/s when falling | Falling can exceed walk speed, so air time must be handled separately | [14:57](https://youtu.be/2jvahdJnQRI?t=897) |
| 2023-04-16 | anti-exploit-and-security | Max air time before flag | 3 seconds | Fly-hack threshold in the example; customise per game | [21:25](https://youtu.be/2jvahdJnQRI?t=1285) |
| 2023-04-16 | anti-exploit-and-security | Pickup range check | 5 studs | Magnitude distance check for coin pickup | [8:36](https://youtu.be/2jvahdJnQRI?t=516) |
| 2023-05-18 | ads-and-sponsored-experiences | In-game advert price | 2 Robux via PM; earlier 10 ticks | Ro-Ball Arena advert placement, eight players had played it | [22:45](https://youtu.be/TJnV2ycnXZc?t=1365) |
| 2023-05-18 | thumbnails-icons | Thumbnail upload | Required Robux historically | Creator says uploading a thumbnail once cost Robux; he used autosave workaround | [11:40](https://youtu.be/TJnV2ycnXZc?t=700) |
| 2023-05-18 | scripting-and-performance | Repeated script lines | over 1000 lines | Spotlight script with copy-pasted blocks instead of a loop | [18:40](https://youtu.be/TJnV2ycnXZc?t=1120) |
| 2023-07-30 | updates-live-ops | tween duration | 0.1 seconds | Changed once in the single script; applied to all tagged doors | [5:30](https://youtu.be/UsPYgIW3rv8?t=330) |
| 2024-09-19 | development-process-and-speed | Intermission duration | 5 seconds | Example constant in tutorial code | [0:35](https://youtu.be/oEWoyT-GBZY?t=35) |
| 2024-09-19 | development-process-and-speed | Round duration | 10 seconds | Example constant in tutorial code | [1:15](https://youtu.be/oEWoyT-GBZY?t=75) |
| 2024-09-19 | matchmaking-and-teleport | Minimum players to start | 2 | Example value in tutorial; changed to 1 for testing | [5:09](https://youtu.be/oEWoyT-GBZY?t=309) |
| 2024-09-20 | core-loops-and-game-design | Vote stage countdown | 5 seconds | Voting phase length set in the server script | [0:00](https://youtu.be/SUZPuQrKJuU?t=0) |
| 2024-09-20 | core-loops-and-game-design | Map choices in demo | 3 maps | Image buttons for desert, garden, and exosap maps | [0:00](https://youtu.be/SUZPuQrKJuU?t=0) |
| 2024-10-12 | first-session-onboarding | Load-in tolerance | More than 5 seconds (10 max) on desktop risks losing players | Creator's rule of thumb for game jam entries | [3:34](https://youtu.be/H9CbgCe47Mo?t=214) |
| 2024-10-12 | game-ideas-and-genres | Duplicate concept count | At least half a dozen jam games used the alarm-clock wake-up opening | Game jam entries observed by the creator | [4:46](https://youtu.be/H9CbgCe47Mo?t=286) |
| 2024-11-07 | ads-and-sponsored-experiences | Ad budget spent | 400 USD (~114,000 Robux), 1 ad credit = 285 Robux | Visits campaign, lifetime budget, sponsored experience ad type | [1:41](https://youtu.be/g9UbIrR0RbU?t=101) |
| 2024-11-07 | ads-and-sponsored-experiences | Suggested max bid | 0.03-0.05 typical | Creator chose the bottom of the range | [3:05](https://youtu.be/g9UbIrR0RbU?t=185) |
| 2024-11-07 | ads-and-sponsored-experiences | CPM | 0.08 ad credits per 1000 impressions | After first hour or two | [3:20](https://youtu.be/g9UbIrR0RbU?t=200) |
| 2024-11-07 | thumbnails-icons | CTR | ~1% (177k clicks on ~1M impressions in first hours) | Creator's target is about 2% | [3:20](https://youtu.be/g9UbIrR0RbU?t=200) |
| 2024-11-07 | ads-and-sponsored-experiences | Day 2 totals | 4.2M impressions, ~2,000 clicks, 162,000 plays, CTR 0.99% | Day 2 numbers, 351 of 400 credits spent | [6:10](https://youtu.be/g9UbIrR0RbU?t=370) |
| 2024-11-07 | analytics-metrics | Total visits from ads | ~19,000 visits; ~2 cents per play; ~5.7 Robux per new player | Cost efficiency of the whole campaign | [9:04](https://youtu.be/g9UbIrR0RbU?t=544) |
| 2024-11-07 | retention-d1-d7 | Average session length | ~5 min for new ad users vs ~10 min for regulars; 50% of new users left by 5 min | Ad-acquired players versus existing players | [4:44](https://youtu.be/g9UbIrR0RbU?t=284) |
| 2024-11-07 | thumbnails-icons | CTR after icon change | 94% from 97% (creator's figure, likely a relative metric) | Skeleton icon test | [3:20](https://youtu.be/g9UbIrR0RbU?t=200) |
| 2025-02-18 | testing-debugging-and-qa | Artificial replication lag used to reproduce bug | 0.5 seconds |  | [1:32](https://youtu.be/OyPgQgBSIe4?t=92) |
| 2025-02-18 | testing-debugging-and-qa | Coins collected while spamming with lag | 6 |  | [1:32](https://youtu.be/OyPgQgBSIe4?t=92) |
| 2025-02-18 | physics-pathfinding-and-npc-ai | Overhead raycast distance for stand-up check | 3 studs |  | [7:36](https://youtu.be/OyPgQgBSIe4?t=456) |
| 2025-03-08 | analytics-metrics | Players who entered game | 6,000 |  | [4:55](https://youtu.be/u_8p65Bsm2Y?t=295) |
| 2025-03-08 | analytics-metrics | Completion rate | 25.82% (~1,500 players) |  | [4:55](https://youtu.be/u_8p65Bsm2Y?t=295) |
| 2025-03-08 | first-session-onboarding | Lobby join to elevator conversion | ~85% |  | [5:37](https://youtu.be/u_8p65Bsm2Y?t=337) |
| 2025-03-08 | analytics-metrics | Example expected elevator conversion (hypothetical) | ~90% |  | [0:40](https://youtu.be/u_8p65Bsm2Y?t=40) |
| 2025-03-08 | analytics-metrics | Example expected teleport success (hypothetical) | ~99% |  | [1:21](https://youtu.be/u_8p65Bsm2Y?t=81) |
| 2025-03-08 | analytics-metrics | Game approval rating before analysis | 65% |  | [0:00](https://youtu.be/u_8p65Bsm2Y?t=0) |
| 2026-02-10 | code-architecture-and-frameworks | NPC count in demo | 2 NPCs (Joe, Fred) |  | [0:00](https://youtu.be/3D0l-WiEhLI?t=0) |
