---
title: LastLevelStudios - Studio & Scripting
creator: LastLevelStudios
tags: [roblox, lastlevelstudios, theme]
creator_trust: MIXED
creator_score: 5.5
---

> [!note] Trust: MIXED (credibility audit score 5.5): do not rely on this creator alone; confirm a recommendation with a second source. See [[creator-credibility]].

# LastLevelStudios: Studio & Scripting

All LastLevelStudios tips on this theme, grouped by topic, oldest first. Cross-creator synthesis: see [[README]] in roblox-kb.

## [[scripting-and-performance]]
- 2020-03-01 [23:08](https://youtu.be/4fz4fpJLUSQ?t=1388) Use a command framework like Commander so argument parsing (e.g. converting names to Player objects) is handled before your command code runs. ([[2020-03-01 - evaera - Adopt Me!, Roblox Discord Bots - Beyond The Blox S1E12|evaera - Adopt Me!, Roblox Discord Bots - Beyond T]])
- 2020-03-23 [19:14](https://youtu.be/n0ODJH9EgWc?t=1154) Build utilities that solve a wide-audience problem (e.g. rotated region checks) rather than one-off effects; they get reused across many projects. ([[2020-03-23 - EgoMoose - Bloxy Nominee, Roblox Wiki - Beyond The Blox S1E13|EgoMoose - Bloxy Nominee, Roblox Wiki - Beyond The]])
- 2020-08-17 [21:38](https://youtu.be/0RRGneqSZRY?t=1298) When initially processing hundreds of thousands of parts, yield periodically using a time budget rather than after every part, or the load takes unacceptably long. ([[2020-08-17 - SCR's Part Streaming System - BTS² 02|SCR's Part Streaming System - BTS² #02]])
- 2020-08-24 [4:29](https://youtu.be/uYIE3IVmKY8?t=269) Treat track as blocks with entry and exit sensors; track trains in an in-block table, adding on enter and removing on exit or despawn, instead of GetTouchingParts. ([[2020-08-24 - SCR's Signalling System - BTS² 03|SCR's Signalling System - BTS² #03]])
- 2020-08-24 [30:33](https://youtu.be/uYIE3IVmKY8?t=1833) Avoid per-object background loops; use one centralised table/manager for hundreds of entities and yield to keep the server near 60 fps. ([[2020-08-24 - SCR's Signalling System - BTS² 03|SCR's Signalling System - BTS² #03]])
- 2021-12-09 [16:19](https://youtu.be/v_TGu45AD_g?t=979) Roblox's default VR GUI behaves oddly; building a custom GUI system was easier than working around it. ([[2021-12-09 - GregTame - Pioneering Roblox VR into the Future (Virtual Reality) - Be|GregTame - Pioneering Roblox VR into the Future (V]])

## [[code-architecture-and-frameworks]]
- 2020-03-01 [23:08](https://youtu.be/4fz4fpJLUSQ?t=1388) Write code for reuse across games from the start; game-specific code wastes time when you need it again. ([[2020-03-01 - evaera - Adopt Me!, Roblox Discord Bots - Beyond The Blox S1E12|evaera - Adopt Me!, Roblox Discord Bots - Beyond T]])
- 2020-08-24 [11:17](https://youtu.be/uYIE3IVmKY8?t=677) Auto-derive aspect count from topology: if no signal ahead can show yellow, drop double-yellow and use a three-aspect signal. ([[2020-08-24 - SCR's Signalling System - BTS² 03|SCR's Signalling System - BTS² #03]])
- 2020-08-24 [19:49](https://youtu.be/uYIE3IVmKY8?t=1189) Check the most dangerous downstream signal first and return immediately; keep looping over lesser signals so a red ahead overrides a yellow. ([[2020-08-24 - SCR's Signalling System - BTS² 03|SCR's Signalling System - BTS² #03]])
- 2021-08-27 [7:54](https://youtu.be/3djSOjdGaE8?t=474) His early code was copy-pasted with no loops, functions, or modules; refactoring for FilteringEnabled was painful. Use functions, loops and modules from the start. ([[2021-08-27 - thebenster - Roblox Security, Make a Cake - Beyond The Blox S2E4|thebenster - Roblox Security, Make a Cake - Beyond]])

## [[client-server-and-remotes]]
- 2019-09-13 [28:14](https://youtu.be/h4W8yHxmxns?t=1694) Ship new features behind a server-side flag defaulting off; enable gradually (1%→5%→10%→50%→100%) while watching crash rates, and turn off instantly if they spike. ([[2019-09-13 - spotco - Former Roblox Employee, Robeats Creator - Beyond The Blox S1E|spotco - Former Roblox Employee, Robeats Creator -]])
- 2020-08-17 [41:25](https://youtu.be/0RRGneqSZRY?t=2485) Let the server do the heavy one-time work of indexing and moving parts into storage, and have clients fetch chunk data via a RemoteFunction to avoid freezing low-end clients. ([[2020-08-17 - SCR's Part Streaming System - BTS² 02|SCR's Part Streaming System - BTS² #02]])
- 2020-08-24 [24:36](https://youtu.be/uYIE3IVmKY8?t=1476) Keep occupancy authority on the server; use event-based enter/exit reports plus a periodic safety loop that forces exit for players too far from any sensor. ([[2020-08-24 - SCR's Signalling System - BTS² 03|SCR's Signalling System - BTS² #03]])

## [[anti-exploit-and-security]]
- 2020-08-24 [28:20](https://youtu.be/uYIE3IVmKY8?t=1700) Validate manual control requests server-side: check permissions, rank, VIP server, desk ownership, and reject invalid states or double control. ([[2020-08-24 - SCR's Signalling System - BTS² 03|SCR's Signalling System - BTS² #03]])
- 2021-08-27 [22:39](https://youtu.be/3djSOjdGaE8?t=1359) Attackers used social engineering to port the phone number and bypass SMS 2FA. Remove phone numbers from dev and key accounts where possible. ([[2021-08-27 - thebenster - Roblox Security, Make a Cake - Beyond The Blox S2E4|thebenster - Roblox Security, Make a Cake - Beyond]])
- 2021-08-27 [24:02](https://youtu.be/3djSOjdGaE8?t=1442) Use authenticator apps or hardware security keys for 2FA, and add a PIN to your carrier account to block unauthorized number transfers. ([[2021-08-27 - thebenster - Roblox Security, Make a Cake - Beyond The Blox S2E4|thebenster - Roblox Security, Make a Cake - Beyond]])
- 2021-08-27 [26:47](https://youtu.be/3djSOjdGaE8?t=1607) Protect critical accounts, especially email, with security keys plus 2FA, and use unique emails per service so one breach does not cascade. ([[2021-08-27 - thebenster - Roblox Security, Make a Cake - Beyond The Blox S2E4|thebenster - Roblox Security, Make a Cake - Beyond]])
- 2021-08-27 [25:25](https://youtu.be/3djSOjdGaE8?t=1525) Developer accounts should support stronger 2FA (authenticator apps or security keys); he said Roblox was working on it, not yet available. ([[2021-08-27 - thebenster - Roblox Security, Make a Cake - Beyond The Blox S2E4|thebenster - Roblox Security, Make a Cake - Beyond]])

## [[data-persistence]]
- 2020-02-07 [36:15](https://youtu.be/HU4JJOft4Pw?t=2175) DataStores have no limit on how many you can use, which allows large per-player data volumes; learn them early since they are simple once understood. ([[2020-02-07 - boatbomber - Lua Learning on Roblox - Beyond The Blox S1E10|boatbomber - Lua Learning on Roblox - Beyond The B]])

## [[physics-pathfinding-and-npc-ai]]
- 2020-08-24 [3:48](https://youtu.be/uYIE3IVmKY8?t=228) Put trains in a separate collision group from scenery and use CFrame/BodyMovers with raycasts for sensors to cut physics collision checks. ([[2020-08-24 - SCR's Signalling System - BTS² 03|SCR's Signalling System - BTS² #03]])

## [[building-and-level-design]]
- 2020-08-17 [3:48](https://youtu.be/0RRGneqSZRY?t=228) Split the map into fixed-size chunks (SCR uses 1024 studs) and key each by x/y/z index; avoid making chunks 2048 since that forces three loaded chunks per direction. ([[2020-08-17 - SCR's Part Streaming System - BTS² 02|SCR's Part Streaming System - BTS² #02]])
- 2020-08-17 [1:08:32](https://youtu.be/0RRGneqSZRY?t=4112) Split very long parts to match chunk size for backward compatibility, but note that automatically splitting unions is tricky. ([[2020-08-17 - SCR's Part Streaming System - BTS² 02|SCR's Part Streaming System - BTS² #02]])
- 2020-08-24 [1:20](https://youtu.be/uYIE3IVmKY8?t=80) Use sensor parts (not unioned track bricks) for signal triggers so moving track means moving one part; object values pointing at unions break when you rebuild. ([[2020-08-24 - SCR's Signalling System - BTS² 03|SCR's Signalling System - BTS² #03]])
- 2020-08-24 [5:10](https://youtu.be/uYIE3IVmKY8?t=310) Write a Studio plugin to create and configure signal entry/exit points and advanced signals; hand-editing object values is error-prone. ([[2020-08-24 - SCR's Signalling System - BTS² 03|SCR's Signalling System - BTS² #03]])

## [[3d-modeling-rigging-and-animation]]
- 2021-12-09 [27:34](https://youtu.be/v_TGu45AD_g?t=1654) Mocap pipeline: Kinect via NI Mate into Blender, convert empties to bones, clean up (~2/3 of animation work saved), export FBX to Roblox. ([[2021-12-09 - GregTame - Pioneering Roblox VR into the Future (Virtual Reality) - Be|GregTame - Pioneering Roblox VR into the Future (V]])

## [[vfx-and-particles]]
- 2025-11-05 [6:46](https://youtu.be/KNHngRRMPVI?t=406) Use emissive mask texture for glow areas, emissive strength (0 to ~40 suggested) for intensity, and emissive tint for colour; replaces old export-twice neon hacks. ([[2025-11-05 - Will emissive maps finally put an end to lighting hacks — Beyond The B|Will emissive maps finally put an end to lighting ]])

## [[ui-ux-design]]
- 2019-10-11 [7:23](https://youtu.be/vY0om5O-Oh8?t=443) Design UI for mobile and console from the start; retrofitting Xbox selection onto a GUI-heavy game can require a separate selection layer. ([[2019-10-11 - iGottic - Common Roblox Developer Mistakes - Beyond The Blox S1E6|iGottic - Common Roblox Developer Mistakes - Beyon]])
- 2020-02-07 [20:08](https://youtu.be/HU4JJOft4Pw?t=1208) Use a scrolling-frame smoothing module for long-text UIs; default Roblox scrolling frames teleport and make reading annoying. ([[2020-02-07 - boatbomber - Lua Learning on Roblox - Beyond The Blox S1E10|boatbomber - Lua Learning on Roblox - Beyond The B]])

## [[optimization-and-streaming]]
- 2019-10-11 [5:20](https://youtu.be/vY0om5O-Oh8?t=320) Review memory and optimization regularly, not just at launch; server memory overuse causes freezing and lag, especially on mobile and console. ([[2019-10-11 - iGottic - Common Roblox Developer Mistakes - Beyond The Blox S1E6|iGottic - Common Roblox Developer Mistakes - Beyon]])
- 2020-08-17 [5:51](https://youtu.be/0RRGneqSZRY?t=351) Move out-of-range parts into a storage folder instead of destroying and recreating them; Lua-side destroy/create is too costly, so reparenting is the cheaper option. ([[2020-08-17 - SCR's Part Streaming System - BTS² 02|SCR's Part Streaming System - BTS² #02]])
- 2020-08-17 [7:24](https://youtu.be/0RRGneqSZRY?t=444) Separate flagging chunks needing state change from the actual reparenting, then process a priority queue ordered by distance to the player's focus. ([[2020-08-17 - SCR's Part Streaming System - BTS² 02|SCR's Part Streaming System - BTS² #02]])
- 2020-08-17 [8:05](https://youtu.be/0RRGneqSZRY?t=485) Load in the chunk ahead of the player before unloading chunks behind, so the player never arrives in empty space. ([[2020-08-17 - SCR's Part Streaming System - BTS² 02|SCR's Part Streaming System - BTS² #02]])
- 2020-08-17 [10:41](https://youtu.be/0RRGneqSZRY?t=641) Auto-throttle streaming by measured frame time rather than a part-count limit, since parts have very different render costs. ([[2020-08-17 - SCR's Part Streaming System - BTS² 02|SCR's Part Streaming System - BTS² #02]])
- 2020-08-17 [11:22](https://youtu.be/0RRGneqSZRY?t=682) When frames drop, skip the streaming step for that frame instead of letting overrun time compound into the next frame. ([[2020-08-17 - SCR's Part Streaming System - BTS² 02|SCR's Part Streaming System - BTS² #02]])
- 2020-08-17 [26:27](https://youtu.be/0RRGneqSZRY?t=1587) Pause streaming only after repeated critical frame drops (below ~5 FPS); single blips shouldn't trigger it, and abrupt toggling causes oscillating lag spikes. ([[2020-08-17 - SCR's Part Streaming System - BTS² 02|SCR's Part Streaming System - BTS² #02]])
- 2020-08-17 [39:23](https://youtu.be/0RRGneqSZRY?t=2363) Enforce a minimum reparent count per cycle (SCR uses 50) so low-end devices still make progress through the queue. ([[2020-08-17 - SCR's Part Streaming System - BTS² 02|SCR's Part Streaming System - BTS² #02]])
- 2020-08-17 [49:41](https://youtu.be/0RRGneqSZRY?t=2981) Weight priority chunks by halving their distance magnitude when sorting, so nearby regular chunks can still outrank distant priority chunks. ([[2020-08-17 - SCR's Part Streaming System - BTS² 02|SCR's Part Streaming System - BTS² #02]])
- 2020-08-17 [54:17](https://youtu.be/0RRGneqSZRY?t=3257) Keep the draw-distance setting near default; pushing it to max can cause throttling and a negative cycle of chunks not loading when needed. ([[2020-08-17 - SCR's Part Streaming System - BTS² 02|SCR's Part Streaming System - BTS² #02]])
- 2020-08-17 [56:20](https://youtu.be/0RRGneqSZRY?t=3380) When training, focus streaming on the front of the vehicle so rails and scenery load ahead of travel, and unload from the rear. ([[2020-08-17 - SCR's Part Streaming System - BTS² 02|SCR's Part Streaming System - BTS² #02]])
- 2020-08-17 [1:10:35](https://youtu.be/0RRGneqSZRY?t=4235) Exempt critical parts like terrain, spawns, and sensors from streaming so they always exist, and keep base plates as priority loads. ([[2020-08-17 - SCR's Part Streaming System - BTS² 02|SCR's Part Streaming System - BTS² #02]])
- 2020-08-17 [30:30](https://youtu.be/0RRGneqSZRY?t=1830) Expose a throttle slider in settings so players on different hardware can tune streaming aggressiveness; SCR's testers saw FPS roughly double after the rewrite. ([[2020-08-17 - SCR's Part Streaming System - BTS² 02|SCR's Part Streaming System - BTS² #02]])
- 2021-12-09 [28:16](https://youtu.be/v_TGu45AD_g?t=1696) 60fps mocap FBX files reach 200-300 KB each; load animations on demand so they don't eat the memory budget, accepting brief pauses on slow connections. ([[2021-12-09 - GregTame - Pioneering Roblox VR into the Future (Virtual Reality) - Be|GregTame - Pioneering Roblox VR into the Future (V]])
- 2022-01-07 [30:01](https://youtu.be/v8S5puPQEw4?t=1801) Design for low-end mobile first: enable streaming and program with it on from the start, even if you later turn it off. ([[2022-01-07 - Quenty - Whatever Floats Your Boat, Roblox Intern, Open Source Tools -|Quenty - Whatever Floats Your Boat, Roblox Intern,]])
- 2022-01-07 [30:42](https://youtu.be/v8S5puPQEw4?t=1842) Minimise textures and polygons; texture memory scales quadratically, and mobile crashes are almost always memory-related. ([[2022-01-07 - Quenty - Whatever Floats Your Boat, Roblox Intern, Open Source Tools -|Quenty - Whatever Floats Your Boat, Roblox Intern,]])
- 2022-01-07 [30:42](https://youtu.be/v8S5puPQEw4?t=1842) When diagnosing mobile crashes, check memory usage first rather than other causes. ([[2022-01-07 - Quenty - Whatever Floats Your Boat, Roblox Intern, Open Source Tools -|Quenty - Whatever Floats Your Boat, Roblox Intern,]])
- 2025-11-05 [11:16](https://youtu.be/KNHngRRMPVI?t=676) Use SLIM (Studio Beta) for large worlds: Roblox auto-generates lower-fidelity variants by distance; verify with a Highlight in Workspace to see which geometry is SLIM. ([[2025-11-05 - Will emissive maps finally put an end to lighting hacks — Beyond The B|Will emissive maps finally put an end to lighting ]])
- 2025-11-05 [12:42](https://youtu.be/KNHngRRMPVI?t=762) SLIM has known issues (Z-fighting, corroded metal material, UV map problems); test these on your assets before relying on it in production. ([[2025-11-05 - Will emissive maps finally put an end to lighting hacks — Beyond The B|Will emissive maps finally put an end to lighting ]])

## [[version-control-and-tooling]]
- 2020-03-01 [25:51](https://youtu.be/4fz4fpJLUSQ?t=1551) Use Rojo to write code in a normal editor (VS Code) and sync to Studio, enabling Git and external tooling. ([[2020-03-01 - evaera - Adopt Me!, Roblox Discord Bots - Beyond The Blox S1E12|evaera - Adopt Me!, Roblox Discord Bots - Beyond T]])

## [[cross-platform-and-console]]
- 2019-10-11 [6:43](https://youtu.be/vY0om5O-Oh8?t=403) Add Xbox or mobile support once the game has about 10 concurrent players; these audiences can be larger than PC. ([[2019-10-11 - iGottic - Common Roblox Developer Mistakes - Beyond The Blox S1E6|iGottic - Common Roblox Developer Mistakes - Beyon]])
- 2019-10-11 [10:46](https://youtu.be/vY0om5O-Oh8?t=646) Use generic default input activation rather than many keyboard- or mouse-specific actions to ease porting. ([[2019-10-11 - iGottic - Common Roblox Developer Mistakes - Beyond The Blox S1E6|iGottic - Common Roblox Developer Mistakes - Beyon]])

Up: [[LastLevelStudios - How to make successful Roblox games]]
