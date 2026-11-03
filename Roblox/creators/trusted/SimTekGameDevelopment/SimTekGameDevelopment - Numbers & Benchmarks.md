---
title: SimTekGameDevelopment - Numbers & Benchmarks
tags: [roblox, simtekgamedevelopment]
creator_trust: TRUSTED
creator_score: 8.2
---

> [!note] Trust: TRUSTED (credibility audit score 8.2): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# SimTekGameDevelopment: Numbers & Benchmarks

| Date | Topic | Metric | Value | Context | Source |
|---|---|---|---|---|---|
| 2020-12-11 | ui-ux-design | Bag frame size | 220 px wide, roughly 110 px scaled down in the tutorial | Initial bag frame sizing, tuned by eye | [1:08](https://youtu.be/8QUJ_Qc6JTs?t=68) |
| 2020-12-11 | ui-ux-design | UIGridLayout CellSize | Scale X 0.4, offset Y 0.2 (set via relative sizing) | Slot grid sizing relative to parent frame | [2:30](https://youtu.be/8QUJ_Qc6JTs?t=150) |
| 2020-12-29 | data-persistence | Save loop interval | 10 seconds for testing, ~60 seconds suggested for live game | Periodic save loop interval | [6:14](https://youtu.be/bFoHE1qWe64?t=374) |
| 2021-02-15 | analytics-metrics | Test spawn count | 4 zombies used for testing | Test setup; not a performance benchmark | [9:42](https://youtu.be/_ANWj69QDms?t=582) |
| 2021-07-04 | scripting-and-performance | Jump obstacle height | ~3.5 studs cleared by pathfinding jump in speaker's test (wall 11.5 studs high was not cleared) | Speaker's own test with Roblox pathfinding jump | [18:13](https://youtu.be/lJktfRT2pbg?t=1093) |
| 2021-07-18 | scripting-and-performance | Response payload | JSON with fact string and length field | Cat fact API response shape observed in the print output | [6:46](https://youtu.be/NsnoDX2dEY8?t=406) |
| 2022-12-04 | combat-and-gameplay-systems | raycast range | 300 studs | Max shot distance in the example script | [2:06](https://youtu.be/BiaMIbrzo0Q?t=126) |
| 2022-12-04 | combat-and-gameplay-systems | accessory depth | ~3 accessories | Speaker estimates max accessories stacked on one hit point | [8:10](https://youtu.be/BiaMIbrzo0Q?t=490) |
| 2022-12-10 | scripting-and-performance | Pickups placed | 500 clones at random X/Z in a ±500 stud area | Tutorial example spawning loop | [2:03](https://youtu.be/mrmB0hQGCXE?t=123) |
| 2022-12-10 | scripting-and-performance | Raycast origin height | 300 studs above; map max height 256 studs | Ray starts above highest terrain point | [5:34](https://youtu.be/mrmB0hQGCXE?t=334) |
| 2022-12-10 | scripting-and-performance | Raycast length | from Y=300 down to Y=-100 | Stop point 100 studs below origin | [6:16](https://youtu.be/mrmB0hQGCXE?t=376) |
| 2022-12-10 | building-and-level-design | Pickup offset above ground | 3 studs | Added to raycast hit Y | [7:40](https://youtu.be/mrmB0hQGCXE?t=460) |
| 2023-01-07 | first-session-onboarding | Wait before firing messages | 5 seconds after PlayerAdded | Test delay so player sees the world before messages fire | [2:07](https://youtu.be/zmTsh66uxsI?t=127) |
| 2023-01-07 | scripting-and-performance | Queue poll interval | 1 second | Client loop checks queue every second | [6:42](https://youtu.be/zmTsh66uxsI?t=402) |
| 2023-01-07 | ui-ux-design | Tween duration and delay | 1s tween, 2s delay | Label slides off screen after a 2 second read delay | [13:28](https://youtu.be/zmTsh66uxsI?t=808) |
| 2023-01-28 | physics-pathfinding-and-npc-ai | Animate script length | about 800 lines copied | Default Animate script copied from player to NPC | [1:50](https://youtu.be/tjwI4b2ZRZk?t=110) |
| 2023-02-03 | physics-pathfinding-and-npc-ai | VectorForce magnitude | 10000 (example, tune as needed) | Multiplier applied to normalized direction for knockback force | [5:28](https://youtu.be/-sQHMwuVAu4?t=328) |
| 2023-02-03 | physics-pathfinding-and-npc-ai | AngularVelocity magnitude | random between -30 and 30 per axis | Scalar multiplier on vector for spin | [10:15](https://youtu.be/-sQHMwuVAu4?t=615) |
| 2023-02-03 | physics-pathfinding-and-npc-ai | Constraint lifetime | 0.2 seconds | Debris time-to-live for force, angular velocity and attachment | [11:37](https://youtu.be/-sQHMwuVAu4?t=697) |
| 2023-02-03 | physics-pathfinding-and-npc-ai | PlatformStand reset delay | 2 seconds | Time before re-enabling movement after knockback | [11:37](https://youtu.be/-sQHMwuVAu4?t=697) |
| 2023-08-18 | business-and-payouts | Creator share of gamepass Robux sales | 70% | Speaker says Roblox takes 70 percent of the sale price | [2:46](https://youtu.be/U22nZqDmTXI?t=166) |
| 2023-08-18 | pricing | Test gamepass price | 1 Robux | Speaker uses 1 Robux to minimise cost during testing | [4:48](https://youtu.be/U22nZqDmTXI?t=288) |
| 2023-08-18 | combat-and-gameplay-systems | Speed gamepass WalkSpeed boost | +16 WalkSpeed | Demo grants a walk speed increase on purchase | [5:28](https://youtu.be/U22nZqDmTXI?t=328) |
| 2023-09-22 | physics-pathfinding-and-npc-ai | Debris time to live | 10 seconds | Cleanup TTL used for all spawned balls in demo | [8:58](https://youtu.be/ArNJwChSU8Q?t=538) |
| 2023-09-22 | physics-pathfinding-and-npc-ai | Spawn count | 5 balls per type | Loop spawns five balls with one-second waits | [8:58](https://youtu.be/ArNJwChSU8Q?t=538) |
| 2023-09-22 | physics-pathfinding-and-npc-ai | Default LinearVelocity speed in demo | 1 stud/s before speed increase | Unscaled look vector magnitude is one | [8:17](https://youtu.be/ArNJwChSU8Q?t=497) |
| 2023-09-30 | physics-pathfinding-and-npc-ai | Elevator speed | 10 studs per second; floor spacing 10 studs | LinearVelocity set to 10 studs/s, each floor placed 10 studs apart | [1:55](https://youtu.be/6sgx1elbhwU?t=115) |
| 2023-09-30 | physics-pathfinding-and-npc-ai | LinearVelocity MaxForce | math.huge | Used for the elevator floor's LinearVelocity constraint | [4:53](https://youtu.be/6sgx1elbhwU?t=293) |
| 2023-12-30 | scripting-and-performance | Scan angle | ±30° on X, Y, Z in intro demo | Example rig scan range shown at start | [0:00](https://youtu.be/eDTbzVDm1aY?t=0) |
| 2023-12-30 | scripting-and-performance | Sweep step | 5 degrees, horizontal ±45°, vertical ±15° | Cone scan loop ranges used in the video | [23:58](https://youtu.be/eDTbzVDm1aY?t=1438) |
| 2023-12-30 | scripting-and-performance | Default raycast range | 30 studs | Range used in example raycast | [10:46](https://youtu.be/eDTbzVDm1aY?t=646) |
| 2024-02-10 | monetisation-gamepasses | Example game-pass purchase | 10 Robux donation pass | Demo purchase of another creator's pass through a stand | [0:00](https://youtu.be/V65oLE0Wbuc?t=0) |
| 2024-02-10 | monetisation-gamepasses | Passes returned by query | 2 (limit set to 2) | Games API V1 game-passes call with limit parameter | [5:00](https://youtu.be/V65oLE0Wbuc?t=300) |
| 2024-02-19 | luau-language-and-types | Merged example result | Food 19, gold 13, points 300 after adding two player tables |  | [5:48](https://youtu.be/q-kUXooTRd8?t=348) |
| 2024-10-12 | common-mistakes | cooldown | 300 seconds | Suggested production debounce, matching World of Warcraft standard; 5s used only for testing | [6:01](https://youtu.be/i2_7zT36Jeg?t=361) |
| 2024-11-02 | core-loops-and-game-design | WalkSpeed boost | 16 normal to 50 with speed pellet | Speed pellet sets Humanoid.WalkSpeed to 50 | [4:09](https://youtu.be/zimfV0QYV2w?t=249) |
| 2024-11-02 | scripting-and-performance | Knockback speed threshold | 20 studs/s | Linear velocity magnitude check before applying forces | [10:49](https://youtu.be/zimfV0QYV2w?t=649) |
| 2024-11-02 | scripting-and-performance | Force duration | 0.1 seconds | VectorForce and AngularVelocity destroyed via Debris after 0.1s | [18:10](https://youtu.be/zimfV0QYV2w?t=1090) |
| 2024-11-02 | scripting-and-performance | Wall buffer size | ~3/10 stud enlargement | Invisible buffer part slightly larger than wall, approximate | [14:45](https://youtu.be/zimfV0QYV2w?t=885) |
| 2024-11-02 | scripting-and-performance | Demo force values | VectorForce 10000, AngularVelocity 50 | Stronger knockback values used at end of demo | [26:54](https://youtu.be/zimfV0QYV2w?t=1614) |
| 2025-05-17 | data-persistence | Autosave interval | 60 seconds recommended (30 max) | Periodic save loop for player leaderstats | [0:00](https://youtu.be/10uZXhWd_Aw?t=0) |
| 2025-06-24 | core-loops-and-game-design | NPC states in example FSM | 3 (idle, greet, follow) |  | [0:00](https://youtu.be/4tGM1Ac5fcI?t=0) |
| 2025-06-24 | core-loops-and-game-design | Greet state delay | 2 seconds |  | [13:48](https://youtu.be/4tGM1Ac5fcI?t=828) |
| 2025-06-24 | scripting-and-performance | Original decide-action loop interval | every 3 seconds |  | [14:31](https://youtu.be/4tGM1Ac5fcI?t=871) |
| 2025-06-24 | core-loops-and-game-design | Friend score increase per chat | +1 per talk |  | [17:57](https://youtu.be/4tGM1Ac5fcI?t=1077) |
| 2025-07-07 | scripting-and-performance | attack interval | 0.2 seconds between shots | rapid-fire loop for defensive NPC pistol, suggested config value | [44:45](https://youtu.be/DcLba0yVLHs?t=2685) |
| 2025-07-07 | core-loops-and-game-design | cooldown duration | about 2 seconds | time in cooldown state before returning to idle | [49:34](https://youtu.be/DcLba0yVLHs?t=2974) |
| 2025-07-07 | combat-and-gameplay-systems | creator tag lifetime | 2 seconds | kill credit window after damage in sword and pistol scripts | [19:20](https://youtu.be/DcLba0yVLHs?t=1160) |
| 2025-07-07 | core-loops-and-game-design | friend score penalty | -5 shown in test; -10 suggested | applied when player shoots the NPC | [30:17](https://youtu.be/DcLba0yVLHs?t=1817) |
| 2025-07-28 | scripting-and-performance | Walk speed wander / investigate / chase | 3 / 6 / fastest studs per second (chase value not stated) | Config walk speeds for zombie states | [1:20](https://youtu.be/9rzgsXFPTjY?t=80) |
| 2025-07-28 | scripting-and-performance | Investigate sight-based distance | 30 studs | Distance before investigate reverts to wander | [1:10:46](https://youtu.be/9rzgsXFPTjY?t=4246) |
| 2025-07-28 | scripting-and-performance | Max sight ray cast distance | 45 studs | Config vision max sight used by can-see raycast | [1:18:20](https://youtu.be/9rzgsXFPTjY?t=4700) |
| 2025-07-28 | scripting-and-performance | Ray cast distance in code | 50 studs | Initial ray cast length before config change | [43:59](https://youtu.be/9rzgsXFPTjY?t=2639) |
| 2025-07-28 | scripting-and-performance | Decision loop wait | 0.5 seconds | task.wait interval for NPC decide-action loop | [32:17](https://youtu.be/9rzgsXFPTjY?t=1937) |
| 2025-07-28 | scripting-and-performance | Respawn delay after death | 5 seconds | task.delay before cloning zombie again | [32:17](https://youtu.be/9rzgsXFPTjY?t=1937) |
| 2025-07-28 | scripting-and-performance | Wander delay range | 2 to 6 seconds | Random min and max delay between wander moves | [49:27](https://youtu.be/9rzgsXFPTjY?t=2967) |
| 2025-07-28 | building-art-and-assets | Animation keyframe timing | 30 frames per second, 15-frame walk cycle | Animation Editor default frame rate for wander animation | [4:09](https://youtu.be/9rzgsXFPTjY?t=249) |
