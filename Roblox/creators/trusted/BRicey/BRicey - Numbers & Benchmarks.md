---
title: BRicey - Numbers & Benchmarks
tags: [roblox, bricey]
creator_trust: TRUSTED
creator_score: 8.0
---

> [!note] Trust: TRUSTED (credibility audit score 8.0): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# BRicey: Numbers & Benchmarks

| Date | Topic | Metric | Value | Context | Source |
|---|---|---|---|---|---|
| 2020-09-27 | scripting-and-performance | Raycast direction length | 10 studs in example; 100 studs used in later test | Example ray length used in demo | [2:33](https://youtu.be/4fJBWFz9I-E?t=153) |
| 2020-12-23 | client-server-and-remotes | Remote count in game | 2 (one RemoteFunction, one RemoteEvent) | Entire game routed through only two remotes with the module | [1:44](https://youtu.be/6ZgzabMLkKQ?t=104) |
| 2021-01-04 | ui-ux-design | UI approach | Roact UI elements are instantiated from templates; UI rebuilt on state change | Creator's Roact setup for text label component | [14:42](https://youtu.be/xwaCg7SWUhc?t=882) |
| 2021-01-04 | core-loops-and-game-design | Knockback | Player falls over within 1 second of being hit by a thrown part | Creator's test of thrown part hitting player | [16:51](https://youtu.be/xwaCg7SWUhc?t=1011) |
| 2021-01-17 | scripting-and-performance | Attribute name length limit | 100 characters, no spaces | Stated limit on attribute names in the video | [4:47](https://youtu.be/7BSYIEdo6E4?t=287) |
| 2021-01-17 | scripting-and-performance | Debug wait time example | 1 second vs normal 5 seconds | Script attribute example for fast iteration | [11:44](https://youtu.be/7BSYIEdo6E4?t=704) |
| 2021-01-24 | core-loops-and-game-design | Starting bullet velocity | 1000 | FastCast velocity for gun-realistic speed in demo | [21:57](https://youtu.be/mJZWY3G7wa4?t=1317) |
| 2021-01-24 | combat-and-gameplay-systems | Damage per hit | 50 | Demo damage applied to humanoid on hit | [24:01](https://youtu.be/mJZWY3G7wa4?t=1441) |
| 2021-01-24 | scripting-and-performance | Bullet cleanup delay | 2 seconds | Debris:AddItem lifetime for spent bullets in demo | [24:01](https://youtu.be/mJZWY3G7wa4?t=1441) |
| 2021-03-21 | version-control-and-tooling | Rojo default server port | 34872 (localhost) | Default Rojo server address used to connect the Studio plugin | [10:22](https://youtu.be/ulBM7UdHk_4?t=622) |
| 2021-06-12 | scripting-and-performance | Demo timing | 5 s wait before AddTag, 5 s before RemoveTag | Test script delays used to demonstrate runtime tag toggling | [10:06](https://youtu.be/Vi2FckNJv9w?t=606) |
| 2021-06-29 | code-architecture-and-frameworks | Tycoon script size before components | over 1000 lines (speaker's own project) | Speaker's tycoon module script after a few months of development | [4:00](https://youtu.be/stJtnGGt-1c?t=240) |
| 2022-04-16 | monetisation-gamepasses | Money multiplier gamepass effect | 2x money per collector drop | Example pass in tutorial; copper drop 5 becomes 10 | [1:34](https://youtu.be/TmiU5CY6BW0?t=94) |
| 2022-04-30 | pricing | Example dev product price | 5 Robux | Demo 'More Money' product priced at 5 Robux, grants 1000 coins | [0:35](https://youtu.be/5bI6l6SHBDU?t=35) |
| 2022-05-28 | monetisation-other | Badge creation price | 0 Robux | Speaker says badge purchase should always be zero Robux | [2:26](https://youtu.be/T0xqkYODIl0?t=146) |
| 2022-05-28 | monetisation-other | Badge creation rate note | ~100 per hour | Speaker's uncertain recollection of a charge threshold | [2:26](https://youtu.be/T0xqkYODIl0?t=146) |
| 2022-08-21 | scripting-and-performance | Part move interval in demo | every 10 seconds, 2 studs | Example script used in the object cleanup demonstration | [2:08](https://youtu.be/2Msrw5w5cTs?t=128) |
| 2022-08-21 | scripting-and-performance | Demo cleanup delay | 3 seconds | Object lifetime before destroy is called in the final test | [3:44](https://youtu.be/2Msrw5w5cTs?t=224) |
| 2022-09-23 | common-mistakes | script length | ~1000 lines | single tool script in Chaos The Next Generation, cited as a mistake | [5:28](https://youtu.be/MyK4o2pIpQw?t=328) |
| 2023-04-14 | physics-pathfinding-and-npc-ai | AlignPosition MaxVelocity | 10 (default Infinity) | Suggested cap to keep package from falling off the drone | [9:32](https://youtu.be/jaitqSU2HIA?t=572) |
| 2023-04-14 | scripting-and-performance | Depot spawn loop interval | 3 seconds | task.wait tick used by depot script to spawn packages | [11:04](https://youtu.be/jaitqSU2HIA?t=664) |
| 2023-04-14 | scripting-and-performance | Drone state loop interval | 0.5 seconds | task.wait tick that runs current state; RunService suggested in real games | [17:24](https://youtu.be/jaitqSU2HIA?t=1044) |
| 2023-04-14 | scripting-and-performance | Raycast distance below drop point | 5 studs | Downward raycast from drop point to detect drone underneath | [11:45](https://youtu.be/jaitqSU2HIA?t=705) |
| 2023-04-14 | physics-pathfinding-and-npc-ai | Package detection sphere radius | 1 stud | GetPartBoundsInRadius around drone pivot to find tagged package | [21:47](https://youtu.be/jaitqSU2HIA?t=1307) |
| 2023-06-10 | scripting-and-performance | Servo MaxTorque | 50000 | Example torque value used for hinge servos in the turret model | [9:02](https://youtu.be/BBoJiE4IkSg?t=542) |
| 2023-06-10 | scripting-and-performance | Servo Speed | 5 | Example servo speed set on the yaw and pitch hinges | [9:02](https://youtu.be/BBoJiE4IkSg?t=542) |
| 2024-02-17 | code-architecture-and-frameworks | Spawn pool script length | about 23 lines of code | PlotSpawnPool implementation described by the speaker | [12:57](https://youtu.be/FaEMgVDlaNQ?t=777) |
| 2024-02-17 | scripting-and-performance | Recommended extra spawn points | at least 4 more than max players | Buffer against player reallocation causing spawn errors | [16:18](https://youtu.be/FaEMgVDlaNQ?t=978) |
| 2024-02-17 | building-and-level-design | Base plot part size | 50 x 1 x 50 studs | Concrete base used as plot template | [2:05](https://youtu.be/FaEMgVDlaNQ?t=125) |
| 2024-03-02 | building-and-level-design | Raycast max distance | 1000 studs | Placement ray scaled by 1000 for rendering; validation deferred | [9:51](https://youtu.be/SVBmZ3yIMRo?t=591) |
| 2024-03-02 | thumbnails-icons | Preview transparency | 0.5 | Ghost preview part transparency | [4:06](https://youtu.be/SVBmZ3yIMRo?t=246) |
| 2024-04-14 | data-persistence | Views | 9414 | Video view count at time of upload | [0:00](https://youtu.be/NK8VHcNHJG4?t=0) |
