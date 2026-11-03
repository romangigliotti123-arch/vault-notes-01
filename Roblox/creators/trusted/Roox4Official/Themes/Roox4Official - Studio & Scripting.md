---
title: Roox4Official - Studio & Scripting
creator: Roox4Official
tags: [roblox, roox4official, theme]
creator_trust: TRUSTED
creator_score: 8.1
---

> [!note] Trust: TRUSTED (credibility audit score 8.1): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Roox4Official: Studio & Scripting

All Roox4Official tips on this theme, grouped by topic, oldest first. Cross-creator synthesis: see [[README]] in roblox-kb.

## [[scripting-and-performance]]
- 2023-04-15 [3:15](https://youtu.be/Pbrvfdn9UN8?t=195) When PathfindingService fails on stairs, add custom waypoints for that section and have enemies follow them instead of default path waypoints. ([[2023-04-15 - I Accidentally Made My Game Difficult Roblox Shooter Devlog 3|I Accidentally Made My Game Difficult | Roblox Sho]])
- 2024-06-19 [2:44](https://youtu.be/DPpAsjUr278?t=164) Set IK target parts to CanCollide, CanTouch and CanQuery off and Massless on; weld raycast parts to HumanoidRootPart and keep them unanchored. ([[2024-06-19 - How To EASILY Make Procedural Animations In Roblox|How To EASILY Make Procedural Animations In Roblox]])
- 2024-06-19 [4:35](https://youtu.be/DPpAsjUr278?t=275) Use a raycast params filter of Exclude with the whole model so leg raycasts don't hit the character itself. ([[2024-06-19 - How To EASILY Make Procedural Animations In Roblox|How To EASILY Make Procedural Animations In Roblox]])
- 2024-07-25 [2:42](https://youtu.be/OYfrdTxNdjA?t=162) When offsetting viewmodels/cframes, check whether offsets are in object space or world space; mixing them broke the scope alignment until made relative to the camera. ([[2024-07-25 - Making INSANE Enemies For Our Roblox FPS Game|Making INSANE Enemies For Our Roblox FPS Game]])
- 2024-11-01 [1:20](https://youtu.be/LC8AV8Yy6Z4?t=80) Humanoid can override applied forces (rocket jump momentum bled away mid-air). If physics-driven movement matters, build a custom character controller instead. ([[2024-11-01 - I Tried Remaking My First Game, 9 Years Later|I Tried Remaking My First Game, 9 Years Later]])
- 2024-12-06 [6:14](https://youtu.be/_E1stqb2fNw?t=374) Raycasts have a 15,000-stud max range; at extreme distances, chain multiple raycasts to hit nearby targets. ([[2024-12-06 - I Tried Pushing Roblox To It's Absolute Limits|I Tried Pushing Roblox To It's Absolute Limits]])
- 2025-06-19 [0:42](https://youtu.be/vBZMscweRDk?t=42) Don't replicate every projectile as a physical part over the network; network bandwidth becomes the bottleneck. Simulate them with math instead. ([[2025-06-19 - These Weird Optimizations Made Our Game Run 10x FASTER!|These Weird Optimizations Made Our Game Run 10x FA]])
- 2025-06-19 [2:46](https://youtu.be/vBZMscweRDk?t=166) Make bullets purely visual on clients and have the server simulate them from start position, direction and velocity; this reduces each object to a few numbers. ([[2025-06-19 - These Weird Optimizations Made Our Game Run 10x FASTER!|These Weird Optimizations Made Our Game Run 10x FA]])
- 2025-06-19 [3:29](https://youtu.be/vBZMscweRDk?t=209) For non-linear projectiles like grenades, use a closed-form ballistic equation to compute position at any time instead of simulating physics objects. ([[2025-06-19 - These Weird Optimizations Made Our Game Run 10x FASTER!|These Weird Optimizations Made Our Game Run 10x FA]])
- 2025-06-19 [5:34](https://youtu.be/vBZMscweRDk?t=334) Avoid rotating turrets with CFrame updates, animation rigs or mechanical constraints; they were too expensive at scale. ([[2025-06-19 - These Weird Optimizations Made Our Game Run 10x FASTER!|These Weird Optimizations Made Our Game Run 10x FA]])

## [[building-art-and-assets]]
- 2024-06-19 [0:15](https://youtu.be/DPpAsjUr278?t=15) Name all parts uniquely, put animated parts in one folder, and set CanCollide to false on them so they don't interfere with other physics. ([[2024-06-19 - How To EASILY Make Procedural Animations In Roblox|How To EASILY Make Procedural Animations In Roblox]])

## [[client-server-and-remotes]]
- 2025-06-19 [6:14](https://youtu.be/vBZMscweRDk?t=374) Running turret logic on clients saves performance but makes server aim estimates inaccurate and desynced; avoid this trade-off if possible. ([[2025-06-19 - These Weird Optimizations Made Our Game Run 10x FASTER!|These Weird Optimizations Made Our Game Run 10x FA]])

## [[physics-pathfinding-and-npc-ai]]
- 2024-06-19 [3:26](https://youtu.be/DPpAsjUr278?t=206) Configure each IK control with EndEffector (last leg part), Target (matching IK target part) and ChainRoot (first leg part). ([[2024-06-19 - How To EASILY Make Procedural Animations In Roblox|How To EASILY Make Procedural Animations In Roblox]])
- 2024-06-19 [4:07](https://youtu.be/DPpAsjUr278?t=247) Add a pole attachment per leg on HumanoidRootPart, oriented in the direction the knee should bend (e.g. outward and slightly up). ([[2024-06-19 - How To EASILY Make Procedural Animations In Roblox|How To EASILY Make Procedural Animations In Roblox]])
- 2024-06-19 [5:50](https://youtu.be/DPpAsjUr278?t=350) Add an AlignOrientation on HumanoidRootPart with a large MaxTorque, targeting the move target, so the body tilts up/down on terrain instead of only turning left/right. ([[2024-06-19 - How To EASILY Make Procedural Animations In Roblox|How To EASILY Make Procedural Animations In Roblox]])
- 2024-07-25 [2:51](https://youtu.be/OYfrdTxNdjA?t=171) Custom spring math for enemy suspension lost numerical precision on small, fast enemies; using engine-native constraints (real Springs on wheels) fixed it. ([[2024-07-25 - Making INSANE Enemies For Our Roblox FPS Game|Making INSANE Enemies For Our Roblox FPS Game]])
- 2024-07-25 [6:22](https://youtu.be/OYfrdTxNdjA?t=382) Use AlignPosition and AlignOrientation constraints plus a simple target-facing function to rotate turrets smoothly. ([[2024-07-25 - Making INSANE Enemies For Our Roblox FPS Game|Making INSANE Enemies For Our Roblox FPS Game]])
- 2024-12-06 [0:40](https://youtu.be/_E1stqb2fNw?t=40) Server-side teleports beyond about 1,000,000 studs snap back to 1M; client-created parts can still exist farther, but this is an unsupported edge case. ([[2024-12-06 - I Tried Pushing Roblox To It's Absolute Limits|I Tried Pushing Roblox To It's Absolute Limits]])
- 2025-06-19 [6:56](https://youtu.be/vBZMscweRDk?t=416) Use IK control in Look At mode to rotate a part toward a target on the server; the speaker reports it runs with no performance issues. ([[2025-06-19 - These Weird Optimizations Made Our Game Run 10x FASTER!|These Weird Optimizations Made Our Game Run 10x FA]])
- 2025-09-01 [0:50](https://youtu.be/WNqGLvkf7hQ?t=50) Avoid Humanoids for physics-driven NPCs; they are rigid, stay upright, and stop abruptly under applied forces. Use simple parts with custom movement instead. ([[2025-09-01 - Adding INSANE Physics To Our Roblox Game|Adding INSANE Physics To Our Roblox Game]])
- 2025-09-01 [4:06](https://youtu.be/WNqGLvkf7hQ?t=246) Custom suspension needs only spring force from Hooke's law (F=-kx) plus damping; without damping the object bounces forever and never stops. ([[2025-09-01 - Adding INSANE Physics To Our Roblox Game|Adding INSANE Physics To Our Roblox Game]])
- 2025-09-01 [5:31](https://youtu.be/WNqGLvkf7hQ?t=331) Add sliding friction on wheels by computing lateral velocity change opposite to steer direction and applying mass times acceleration as force. ([[2025-09-01 - Adding INSANE Physics To Our Roblox Game|Adding INSANE Physics To Our Roblox Game]])

## [[combat-and-gameplay-systems]]
- 2024-07-25 [8:17](https://youtu.be/OYfrdTxNdjA?t=497) Use raycasts to keep a laser beam's endpoint attached to the ground, and make weak points reachable only at close range to create risk/reward. ([[2024-07-25 - Making INSANE Enemies For Our Roblox FPS Game|Making INSANE Enemies For Our Roblox FPS Game]])
- 2024-07-25 [0:22](https://youtu.be/OYfrdTxNdjA?t=22) Balance weapons by role: shotgun can't break weak points, sniper can, so each weapon has a distinct purpose. ([[2024-07-25 - Making INSANE Enemies For Our Roblox FPS Game|Making INSANE Enemies For Our Roblox FPS Game]])

## [[building-and-level-design]]
- 2023-04-15 [4:39](https://youtu.be/Pbrvfdn9UN8?t=279) Use crude placeholder blocks for buildings during prototyping and swap in real models later. ([[2023-04-15 - I Accidentally Made My Game Difficult Roblox Shooter Devlog 3|I Accidentally Made My Game Difficult | Roblox Sho]])
- 2024-07-25 [4:55](https://youtu.be/OYfrdTxNdjA?t=295) Automate attaching parts/wheels to many enemies with a module instead of manual assignment. ([[2024-07-25 - Making INSANE Enemies For Our Roblox FPS Game|Making INSANE Enemies For Our Roblox FPS Game]])
- 2024-11-01 [3:07](https://youtu.be/LC8AV8Yy6Z4?t=187) For destructible walls, build them from many smaller blocks rather than one part so projectiles can carve holes. ([[2024-11-01 - I Tried Remaking My First Game, 9 Years Later|I Tried Remaking My First Game, 9 Years Later]])
- 2024-12-06 [3:26](https://youtu.be/_E1stqb2fNw?t=206) Scale up objects when working far from origin; the creator found larger parts glitch less than small ones, making the game more playable. ([[2024-12-06 - I Tried Pushing Roblox To It's Absolute Limits|I Tried Pushing Roblox To It's Absolute Limits]])
- 2024-12-06 [6:14](https://youtu.be/_E1stqb2fNw?t=374) Parts have a maximum size limit; building large walls may require stacking many parts instead of resizing one. ([[2024-12-06 - I Tried Pushing Roblox To It's Absolute Limits|I Tried Pushing Roblox To It's Absolute Limits]])

## [[3d-modeling-rigging-and-animation]]
- 2024-06-19 [0:58](https://youtu.be/DPpAsjUr278?t=58) Rig parts in Studio with the free Rig Edit plugin: select parent then child part and press Create Joints, then move joint pivots to the rotation point. ([[2024-06-19 - How To EASILY Make Procedural Animations In Roblox|How To EASILY Make Procedural Animations In Roblox]])
- 2024-06-19 [2:21](https://youtu.be/DPpAsjUr278?t=141) Lower Rig Edit step value gives more precise joint movement; tune it per model and test joints in the animation editor before continuing. ([[2024-06-19 - How To EASILY Make Procedural Animations In Roblox|How To EASILY Make Procedural Animations In Roblox]])

## [[optimization-and-streaming]]
- 2025-09-01 [7:31](https://youtu.be/WNqGLvkf7hQ?t=451) Per-wheel raycast and force logic running every frame for each vehicle clogs network bandwidth; check the performance stats network panel when adding many physics actors. ([[2025-09-01 - Adding INSANE Physics To Our Roblox Game|Adding INSANE Physics To Our Roblox Game]])
- 2025-09-01 [9:34](https://youtu.be/WNqGLvkf7hQ?t=574) Replace four per-wheel raycasts with one center raycast plus a line orientation constraint and linear velocity; cut iterations from four per frame to one and ran about 10x better. ([[2025-09-01 - Adding INSANE Physics To Our Roblox Game|Adding INSANE Physics To Our Roblox Game]])

Up: [[Roox4Official - How to make successful Roblox games]]
