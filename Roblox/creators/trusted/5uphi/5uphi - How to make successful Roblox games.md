---
title: 5uphi - How to make successful Roblox games
tags: [roblox, 5uphi, playbook]
videos: 25
generated: 2026-10-29
credibility: trusted
credibility_score: 8.8
creator_trust: TRUSTED
creator_score: 8.8
---

> [!note] Trust: TRUSTED (credibility audit score 8.8): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# 5uphi - How to make successful Roblox games

5uphi's channel is technical Roblox scripting, not a growth or business playbook. Core advice: keep the server authoritative and validate every client-sent value (types, NaN, ranges, distance, speed). Move visual-only motion such as NPCs, tweens and doors to the client to cut replicated traffic. Structure code with a global module loader, two-phase initialize/initiate and metatable classes. Keep DataStore saves small and session-safe, compressing data to fit the 4M-character key limit. Measure with MicroProfiler and Stats > Network before optimising. Discovery, pricing and monetisation advice is largely absent from these videos.

**Style:** Dense, code-first tutorials that benchmark claims live in Studio and show numbers. Suits developers who already script and want performance, networking and architecture depth. Less useful for beginners wanting design or business guidance; the creator often publishes free Toolbox modules (Suphi's DataStore, RemoteFunction, Packet, Global Framework) alongside the videos.

## Playbook
1. **Pick a mechanic you can prototype and measure** [[game-ideas-and-genres]]: The creator gives no genre or market-validation advice. Their demos centre on mechanics: drivable cars (FVOowr2DXbM), NPC wandering and pathfinding (JyMxrcqEzu8), apple collecting with NPC selling (UAdE8-AfuMo), and doors (ZPviBfpPloE). Choose a core mechanic and judge it by benchmarks rather than audience research.
2. **Decide replication and ownership before building** [[client-server-and-remotes]]: Decide which state the server owns and which is visual only. Replicate server-to-client by default (Ng1uYpFcpOA). Use client-driven visuals for NPCs and doors (JyMxrcqEzu8, BRYp2-rdpXQ). Anchor or nil-own NPC physics parts so exploiters cannot move them (hr_8svt1n1E).
3. **Set up a modular code architecture** [[code-architecture-and-frameworks]]: Auto-require every ModuleScript into one global table in ServerScriptService (YsXijBUUmmM). Run an initialize pass then an initiate pass so cross-module calls are safe. Build classes with metatables, putting shared methods on __index (bk8UVm-gxBs). Split systems (leaderstats, data, shop) into separate scripts (YsXijBUUmmM).
4. **Build physics gameplay and client-side NPCs with benchmarks** [[physics-pathfinding-and-npc-ai]]: Prefer physics-driven parts over CFrame updates (thfUspopuGE). For cars, tune mass, spring suspension and wheel friction, use constraint limits and motor-driven rear wheels (FVOowr2DXbM). Keep NPCs client-side with server-sent wander targets and distance culling (100 studs test, 500 final), using PathfindingService with ComputeAsync in pcall and a teleport fallback (JyMxrcqEzu8).
5. **Harden remotes, throttle data and use typed networking** [[anti-exploit-and-security]]: Assume every RemoteEvent argument is forged. Check typeof, NaN (value ~= value), reject amounts <= 0 and floor values. Validate pickups server-side: distance 10 studs, parent ~= nil, and speed check of WalkSpeed + 5 (SFAwwmb8G6o). Throttle camera remotes by dot product 0.99 and 0.1 s minimum (8fV-XOOj6O4). Prefer Packet for typed, batched packets (WoIElUdj64A).
6. **Design the save system around size limits** [[data-persistence]]: Measure JSON size with HttpService:JSONEncode against the 4,000,000-character key limit before optimising. Round to integers, flatten arrays, drop brackets, base-90 encode and table.concat with commas (ws3-gfJXw_U). Use Suphi's DataStore module or ProfileService for session locking (ARPfIt16sXI).
7. **Build animation and motion with the cheapest option** [[3d-modeling-rigging-and-animation]]: Choose AnimationTrack keyframes for doors and repeated motion: lowest CPU and near-zero network during playback (ZPviBfpPloE). Keep keyframe rotations under 180 degrees per key and add buffer keyframes past markers (AkF-4x7qfzM). Use TweenService only when you can keep it client-side.
8. **Handle streaming and large worlds** [[optimization-and-streaming]]: Enable StreamingEnabled and choose StreamingIntegrityMode, a minimum radius, and StreamOutBehavior (d8pqcfxqmek). Opportunistic stream-out distance is target + target/2 + 64 studs. Use ModelStreamingMode atomic for models that must load whole.
9. **Test with lag and profiling before launch** [[testing-debugging-and-qa]]: Simulate lag with Studio Settings > Network incoming replication lag and sudden ping changes (hr_8svt1n1E, AkF-4x7qfzM). Test event code with task.spawn first to expose iteration bugs (DTEraIOfoS0). Multiply Studio network numbers by player count for real estimates (Ng1uYpFcpOA).
10. **Gate monetisation on successful saves** [[monetisation-devproducts]]: For developer products, call DataStore:save() before granting the item. On failure, deduct the grant and return NotProcessedYet so it cannot be obtained free. Route ProcessReceipt through a table keyed by product ID so adding products means adding one function (UAdE8-AfuMo).
11. **Prepare the release build and tooling** [[version-control-and-tooling]]: Use the Global Framework plugin with the 'Global types' attribute to regenerate shared typed modules, and keep the 'local globals' marker intact (SVLFkdeh6c8). Use Global Library from the Toolbox as a starting point without forcing a style (SVLFkdeh6c8).
12. **Growth: no evidence in these videos** [[mindset-and-strategy]]: None of the 25 videos cover discovery, thumbnails, advertising, social or community growth. The 2022-07-13 benchmark video is explicitly low on business advice. Growth is best treated as outside this creator's coverage; rely on other sources for discovery and marketing.
13. **Live ops: use DataStore Queue for cross-server events** [[data-persistence]]: Use DataStore:Queue for cross-server messages (default expiry 7 days, max 45). ProcessQueue re-fires about every 30 s until values are removed, and failed saves re-queue (ykWkDov_x-8). Keep server-only logic in start stage loops, not initialize (YsXijBUUmmM).
14. **Re-verify platform assumptions regularly** [[roblox-platform-changes]]: Some advice is platform-dependent: the six-second write limit was reportedly removed (ARPfIt16sXI); parallel script execution order may change (BbIPalpAfaI); identical functions are now raw-equal in memory (scripting-and-performance tips). Recheck these when Roblox updates.

## Key numbers
- DataStore key limit: 4,000,000 characters; compression raised capacity from about 70k parts to about 297k parts (ws3-gfJXw_U)
- Physics vs CFrame: about 4 ms vs 8 ms at 1,000 parts (thfUspopuGE)
- Incoming data, 100 parts: physics ~40 KB/s vs CFrame ~271 KB/s (thfUspopuGE)
- Camera look-vector throttle: ~1.8 KB/s down to ~0.4-0.5 KB/s fast rotation; dot 0.99, minimum 0.1 s (8fV-XOOj6O4)
- Server-side tween: ~1.66 KB/s incoming vs 0.16 KB/s idle; client tween stays ~0.16 KB/s (ZJnMimf9n5Y)
- Door benchmark, 60 doors: animation ~16 ms CPU vs tween ~60 ms; tween ~1,800 KB/s received while moving (ZPviBfpPloE)
- Motor6D Transform ~25 ms vs BulkMoveTo ~28 ms average CPU (BRYp2-rdpXQ)
- NPC display distance: 100 studs test, 500 studs final (JyMxrcqEzu8)
- Exploit checks: pickup distance 10 studs; max speed WalkSpeed + 5 (SFAwwmb8G6o)
- Car tuning: body mass ~82 at density 0.3; suspension stiffness 3500, damping 200, free length 2.8 (FVOowr2DXbM)
- Motor torque: drive 5000; rear handbrake 2000 when unpowered (FVOowr2DXbM)
- DataStore autosave every 30 s; open retry 6 s; locked retry 5 s, increasing (UAdE8-AfuMo, ykWkDov_x-8)
- ProfileService assumes dead session lock after 30 minutes (ARPfIt16sXI)
- Queue default expiry 7 days (max 45); ProcessQueue re-fires about every 30 s (ykWkDov_x-8)
- Animation rotation: 1440 deg/s split into 2 x 72 deg steps; keep each key under 180 deg (AkF-4x7qfzM)

## Common mistakes
- Trusting client touched events or client-sent amounts; negative, decimal or NaN values pass type checks (SFAwwmb8G6o)
- Assuming anchoring stops touched-event spoofing; it does not (SFAwwmb8G6o)
- Leaving NPC humanoids or physics parts client-owned, letting exploiters set states like Dead for all players (hr_8svt1n1E)
- Calling RemoteFunction InvokeClient without a timeout; a silent client yields forever and leaks memory (A14qFAyFYhQ)
- Replicating server-side tweens every frame, which raises incoming network use (ZJnMimf9n5Y)
- Not disconnecting seat.Changed when the driver exits, so handlers stack on re-entry (FVOowr2DXbM)
- Using task.defer and hiding iteration bugs in event systems; test with task.spawn first (DTEraIOfoS0)
- Comparing animation marker times as strings to numbers, which breaks logic silently (AkF-4x7qfzM)
- Putting infinite loops in initialize or initiate stages, which block later stages (YsXijBUUmmM)
- Believing UpdateAsync is inherently more secure than SetAsync; it helps only when you read and modify the previous value (ARPfIt16sXI)

## Launch checklist
- [ ] Confirm DataStore save size is under 4,000,000 characters using JSONEncode length (ws3-gfJXw_U)
- [ ] Call DataStore:save() before granting any developer product; deduct and return NotProcessedYet on failure (UAdE8-AfuMo)
- [ ] Wrap ComputeAsync in pcall and check status == Success, with teleport fallback (JyMxrcqEzu8)
- [ ] Validate every remote argument with typeof, NaN checks, and amount > 0 with floor (SFAwwmb8G6o)
- [ ] Enforce server-side pickup distance (10 studs) and speed check (WalkSpeed + 5) (SFAwwmb8G6o)
- [ ] Call SetNetworkOwner(nil) on unanchored NPC and physics parts not controlled by players (hr_8svt1n1E)
- [ ] Replace raw RemoteEvents and RemoteFunctions with Packet or a timeout-wrapped invoke (WoIElUdj64A, A14qFAyFYhQ)
- [ ] Throttle camera or high-frequency remotes by dot product and minimum interval (8fV-XOOj6O4)
- [ ] Test with Studio incoming replication lag and sudden ping changes (AkF-4x7qfzM)
- [ ] Profile with MicroProfiler and Stats > Network; multiply Studio numbers by player count (BbIPalpAfaI, Ng1uYpFcpOA)
- [ ] Set StreamingEnabled integrity mode and minimum radius; pause outside loaded area if needed (d8pqcfxqmek)
- [ ] Ensure terrain is loaded at NPC start and target before spawning (JyMxrcqEzu8)
- [ ] Disconnect seat and driver connections on exit to prevent handler stacking (FVOowr2DXbM)
- [ ] Verify ProcessReceipt routes through a table keyed by product ID (UAdE8-AfuMo)
- [ ] Use task.spawn in tests to surface event-system iteration bugs (DTEraIOfoS0)
- [ ] Recheck platform-dependent claims: write limits, parallel order, raw-equal functions (ARPfIt16sXI, BbIPalpAfaI)

## How the advice changed over time
- Newest guidance on remotes: Packet (WoIElUdj64A, 2025-03) supersedes earlier RemoteEvent/RemoteFunction use; A14qFAyFYhQ (2024-01) warned against RemoteFunctions and used a custom invoke or Suphi's module.
- Save locking changed: ARPfIt16sXI (2023-06) describes ProfileService's 30-minute lock timeout, while SVLFkdeh6c8 (2024-11) uses a 5-second load delay after join instead of a session lock.
- Door movement changed: ZJnMimf9n5Y (2023-02) moved tweens to the client; ZPviBfpPloE (2024-10) found tweens worst on CPU and network and favoured Animator keyframes; BRYp2-rdpXQ (2025-03), the newest, favours client-only Motor6D Transform.
- Type checking: eRVDL7xlN8g (2023-08) prefers strict mode over non-strict because strict infers types with less manual work.
- NPC ownership: JyMxrcqEzu8 (2021-11) built client-owned NPCs; hr_8svt1n1E (2023-02) adds anchoring or nil network owner and disabling Dead to block exploiters.
- Write limit: ARPfIt16sXI (2023-06) reports Roblox removed the six-second per-key write limit that earlier guidance assumed.

## Theme notes
- [[5uphi - Monetisation|Monetisation]]
- [[5uphi - Game Ideas|Game Ideas]]
- [[5uphi - Studio & Scripting|Studio & Scripting]]
- [[5uphi - Mindset & Process|Mindset & Process]]
- 5uphi - Games Mentioned
- [[5uphi - Numbers & Benchmarks]]
- [[5uphi - Tools & Resources]]
- Cross-creator knowledge base: [[README]]

## All videos (oldest first)
- [[2021-11-10 - Pathfinding, Client VS Server, Unlimited Humanoids - Roblox Scripting|Pathfinding, Client VS Server, Unlimited Humanoids]] (73,466 views, 2021-11-10): Client-side NPCs with server-sent wander targets, distance culling, and PathfindingService to run hundreds smoothly.
- [[2021-12-10 - Metatables - Roblox Scripting Tutorial|Metatables - Roblox Scripting Tutorial]] (35,368 views, 2021-12-10): Luau metatables explained: __index defaults, __call, __add, __eq, __tostring, and shared methods on a Vector2-like type.
- [[2021-12-15 - How To Structure Your Project And Organize Your Scripts - Roblox Scrip|How To Structure Your Project And Organize Your Sc]] (55,863 views, 2021-12-15): Auto-require ModuleScripts into a global table, then initialize and initiate in order to avoid load-order errors.
- [[2021-12-28 - Stop Hackers Exploiters - Roblox Scripting Tutorial|Stop Hackers / Exploiters - Roblox Scripting Tutor]] (66,047 views, 2021-12-28): Defends remotes and touched events against exploiters with type, NaN, range, distance, and speed checks.
- [[2022-03-01 - Compress Optimize Datastore - Roblox Scripting Tutorial|Compress / Optimize Datastore  - Roblox Scripting ]] (24,120 views, 2022-03-01): Compress DataStore saves with rounding, base-90 encoding, and table.concat to fit far more parts per key.
- [[2022-04-14 - Cars With Suspension - Roblox Scripting Tutorial|Cars With Suspension - Roblox Scripting Tutorial]] (114,089 views, 2022-04-14): Builds a drivable suspension car with constraints, motor-driven rear wheels, seat-driven controls, and proximity-prompt entry.
- [[2022-06-19 - Multi Thread, Parallel Scripts, MicroProfiler - Roblox Scripting Tutor|Multi Thread, Parallel Scripts,  MicroProfiler  - ]] (46,461 views, 2022-06-19): MicroProfiler and parallel Luau with Actors and ConnectParallel; threads run in series within one actor.
- [[2022-07-13 - Physics vs CFrame - Roblox Scripting Performance Benchmark|Physics vs CFrame - Roblox Scripting Performance B]] (19,743 views, 2022-07-13): Benchmark: physics-driven parts halve frame cost versus CFrame updates and send far less data.
- [[2023-02-13 - Inverse Kinematics, HingeConstraint - Roblox Scripting Tutorial|Inverse Kinematics, HingeConstraint - Roblox Scrip]] (86,961 views, 2023-02-13): IKControl head look-at and hinge steering-wheel hands, with a throttled camera RemoteEvent to cut bandwidth.
- [[2023-02-17 - Replication, Client-Server Model - Roblox Scripting Tutorial|Replication, Client-Server Model - Roblox Scriptin]] (22,428 views, 2023-02-17): Explains replication with a text-file analogy, then tests which properties, scripts, and states sync each way.
- [[2023-02-21 - Stop exploiters setting humanoid states - Roblox Scripting Tutorial|Stop exploiters setting humanoid states - Roblox S]] (26,121 views, 2023-02-21): Shows exploiters setting NPC humanoid state, plus fixes: anchoring, nil network owner, and disabling Dead state.
- [[2023-02-27 - Optimizing Tweens - Roblox Scripting Tutorial|Optimizing Tweens - Roblox Scripting Tutorial]] (45,512 views, 2023-02-27): Server tweens cost bandwidth every frame; moving tweens to a client RemoteEvent module keeps traffic near idle.
- [[2023-03-29 - Content Streaming - Roblox Scripting Tutorial|Content Streaming - Roblox Scripting Tutorial]] (27,079 views, 2023-03-29): StreamingEnabled explained: integrity modes, replication focus, stream-out behaviour, model streaming, and imposter LOD.
- [[2023-06-15 - Suphi's DataStore Module Basics - Roblox Scripting Tutorial|Suphi's DataStore Module Basics - Roblox Scripting]] (27,707 views, 2023-06-15): Suphi's DataStore module basics: open, save, destroy lifecycle, templates, and a small apples-and-coins demo.
- [[2023-06-16 - Suphi's DataStore Module Advanced - Roblox Scripting Tutorial|Suphi's DataStore Module Advanced - Roblox Scripti]] (7,968 views, 2023-06-16): Suphi's DataStore advanced: Hidden, New, and Find modes, cross-server Queue system, and compression options explained.
- [[2023-06-22 - DataStore2 vs ProfileService vs Suphi's DataStore Module|DataStore2 vs ProfileService vs Suphi's DataStore ]] (19,642 views, 2023-06-22): Compares DataStore2, ProfileService, and Suphi's module on locking, cloning, compression, and trade-offs.
- [[2023-08-01 - Luau Type Checking - Roblox Scripting Tutorial|Luau Type Checking - Roblox Scripting Tutorial]] (24,728 views, 2023-08-01): Luau type checking: strict mode infers types from values, so it needs less annotation than non-strict.
- [[2023-08-29 - Curves & Tweening - Roblox Scripting Tutorial|Curves & Tweening - Roblox Scripting Tutorial]] (56,411 views, 2023-08-29): Arc-length curve tweening for paths, streamed atomically, with clients synced via GetServerTimeNow at no network cost.
- [[2024-01-07 - RemoteFunction - Roblox Scripting Tutorial|RemoteFunction - Roblox Scripting Tutorial]] (28,742 views, 2024-01-07): Why RemoteFunctions leak: a silent client hangs InvokeClient forever; custom invoke adds a 5-second timeout.
- [[2024-08-06 - Linked List Signals - Roblox Scripting Tutorial|Linked List / Signals - Roblox Scripting Tutorial]] (21,058 views, 2024-08-06): Linked lists and event systems compared for connect, disconnect, and fire safety, plus task.defer versus task.spawn.
- [[2024-10-10 - Animation Controller - Roblox Scripting Tutorial|Animation Controller - Roblox Scripting Tutorial]] (21,032 views, 2024-10-10): Door benchmark: Animator keyframes used the least CPU and near-zero network; tweens were worst on both.
- [[2024-10-13 - Animation Controller Synchronization - Roblox Scripting Tutorial|Animation Controller Synchronization - Roblox Scri]] (11,203 views, 2024-10-13): Animation Editor sync: late clients lag rather than skip, paused and stopped cost the same, plus attribute-driven doors.
- [[2024-11-28 - Global Framework - Roblox (Library, Plugin, Scripting)|Global Framework - Roblox (Library, Plugin, Script]] (16,382 views, 2024-11-28): Global Framework: shared typed modules via a plugin, initialize and start stages, and a coin-and-level demo game.
- [[2025-03-09 - Motor6D Transform - Roblox Scripting Tutorial|Motor6D Transform - Roblox Scripting Tutorial]] (16,475 views, 2025-03-09): Motor6D Transform doesn't replicate, so client-only door animation works and slightly beats BulkMoveTo on CPU.
- [[2025-03-26 - Packet - Networking library - Roblox|Packet - Networking library - Roblox]] (51,766 views, 2025-03-26): Packet replaces RemoteEvents and RemoteFunctions with typed, batched packets that send fewer bytes.
