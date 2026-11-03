---
title: Roox4Official - Numbers & Benchmarks
tags: [roblox, roox4official]
creator_trust: TRUSTED
creator_score: 8.1
---

> [!note] Trust: TRUSTED (credibility audit score 8.1): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Roox4Official: Numbers & Benchmarks

| Date | Topic | Metric | Value | Context | Source |
|---|---|---|---|---|---|
| 2023-04-15 | scripting-and-performance | Debugging time on enemy stair pathfinding | about 20 + 50 minutes |  | [3:15](https://youtu.be/Pbrvfdn9UN8?t=195) |
| 2023-04-15 | 3d-modeling-rigging-and-animation | Blender enemy model time | about 2 hours |  | [6:19](https://youtu.be/Pbrvfdn9UN8?t=379) |
| 2023-04-15 | scripting-and-performance | Time to get enemy aiming at player working | about 50 minutes |  | [7:01](https://youtu.be/Pbrvfdn9UN8?t=421) |
| 2024-06-19 | physics-pathfinding-and-npc-ai | IK controls | one per leg (example model had 4) | Creator's example model used four legs | [2:44](https://youtu.be/DPpAsjUr278?t=164) |
| 2024-06-19 | 3d-modeling-rigging-and-animation | Rig Edit step value | 25 recommended starting point | Suggested initial setting in the Rig Edit plugin | [0:58](https://youtu.be/DPpAsjUr278?t=58) |
| 2024-07-25 | scripting-and-performance | Enemy suspension | 4 invisible springs per enemy | Custom spring calc broke on small enemies due to precision loss | [3:32](https://youtu.be/OYfrdTxNdjA?t=212) |
| 2024-07-25 | combat-and-gameplay-systems | Laser damage | 5 damage per hit | Titan enemy laser beam damage per tick | [8:17](https://youtu.be/OYfrdTxNdjA?t=497) |
| 2024-07-25 | development-process-and-speed | Suspension rework time | a few days | Time spent fixing enemy suspension system | [5:37](https://youtu.be/OYfrdTxNdjA?t=337) |
| 2024-11-01 | analytics-metrics | Video views | 1968242 | Views of this remake devlog video at time of extraction | [0:00](https://youtu.be/LC8AV8Yy6Z4?t=0) |
| 2024-11-01 | scripting-and-performance | Offline block-welding algorithm freeze | ~5 seconds | Freezes developer's computer while running the welding algorithm | [3:48](https://youtu.be/LC8AV8Yy6Z4?t=228) |
| 2024-12-06 | optimization-and-streaming | Teleport cap | 1,000,000 studs | Server teleports beyond this snap back to 1M studs | [0:40](https://youtu.be/_E1stqb2fNw?t=40) |
| 2024-12-06 | optimization-and-streaming | Max reached via client-created parts | 20,000,000 studs | Game barely playable; camera stutter, movement issues | [2:45](https://youtu.be/_E1stqb2fNw?t=165) |
| 2024-12-06 | building-and-level-design | Playable distance after scaling up | 2,000,000,000 studs | Game looked decent at 500M-1B; 5B killed player instantly | [4:09](https://youtu.be/_E1stqb2fNw?t=249) |
| 2024-12-06 | building-and-level-design | Max scale factor observed | 1,000x | Creator concluded scaling only worked to about 1,000 | [4:52](https://youtu.be/_E1stqb2fNw?t=292) |
| 2024-12-06 | scripting-and-performance | Raycast max distance | 15,000 studs | Needed ~10 consecutive raycasts to hit a nearby enemy at 2B studs | [6:14](https://youtu.be/_E1stqb2fNw?t=374) |
| 2025-06-19 | optimization-and-streaming | projectiles fired per second | ~1,400 at 60 FPS | Physics-based FPS demo with networked, simulated bullets | [0:00](https://youtu.be/vBZMscweRDk?t=0) |
| 2025-06-19 | optimization-and-streaming | FPS before fix | ~15 | Original approach replicated each bullet as physical object | [1:24](https://youtu.be/vBZMscweRDk?t=84) |
| 2025-06-19 | optimization-and-streaming | Striderbot grenades thrown | 4 per second | Enemy throws four grenades every second; 2-3 Striderbots at once | [4:11](https://youtu.be/vBZMscweRDk?t=251) |
| 2025-06-19 | optimization-and-streaming | Turret share of network bandwidth | about half of available | Turret rotation replication before IK fix | [5:34](https://youtu.be/vBZMscweRDk?t=334) |
| 2025-09-01 | optimization-and-streaming | Performance improvement from single-raycast approach | ~10x better than four-wheel version | Single center raycast plus orientation constraint versus four per-wheel raycasts | [7:31](https://youtu.be/WNqGLvkf7hQ?t=451) |
| 2025-09-01 | optimization-and-streaming | Per-frame iterations of car logic | 4 reduced to 1 | Per enemy: four wheel loops reduced to one center raycast | [7:31](https://youtu.be/WNqGLvkf7hQ?t=451) |
