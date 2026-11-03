---
title: 5uphi - Numbers & Benchmarks
tags: [roblox, 5uphi]
creator_trust: TRUSTED
creator_score: 8.8
---

> [!note] Trust: TRUSTED (credibility audit score 8.8): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# 5uphi: Numbers & Benchmarks

| Date | Topic | Metric | Value | Context | Source |
|---|---|---|---|---|---|
| 2021-11-10 | optimization-and-streaming | NPC count in server vs client benchmark | 200 NPCs and 300 parts per script; server-run laggy, client-run smooth | Demo comparing server-run and client-run movement | [4:39](https://youtu.be/JyMxrcqEzu8?t=279) |
| 2021-11-10 | optimization-and-streaming | NPC display distance | 100 studs test, 500 studs final | Distance from camera focus before NPC is shown and animated | [25:58](https://youtu.be/JyMxrcqEzu8?t=1558) |
| 2021-11-10 | scripting-and-performance | Pathfinding agent settings | AgentRadius 2, AgentHeight 5, WaypointSpacing 4, Water cost 20 | CreatePath configuration in video | [29:57](https://youtu.be/JyMxrcqEzu8?t=1797) |
| 2021-11-10 | scripting-and-performance | Server update interval | 5 seconds | Wait between server position updates per folder | [14:51](https://youtu.be/JyMxrcqEzu8?t=891) |
| 2021-11-10 | client-server-and-remotes | Network ownership radius | Starts small, grows as player stays in game | Radius around character that grants ownership of unanchored parts | [2:34](https://youtu.be/JyMxrcqEzu8?t=154) |
| 2021-12-10 | scripting-and-performance | Vector2 magnitude example result | 42 for (23,36) using sqrt(x*x+y*y) as written | Example calculation in tutorial, not a benchmark | [9:53](https://youtu.be/bk8UVm-gxBs?t=593) |
| 2021-12-28 | anti-exploit-and-security | Max speed allowed for character speed check | WalkSpeed + 5 margin (example 16 + 5 = 21) | Margin prevents false positives from laggy clients | [19:22](https://youtu.be/SFAwwmb8G6o?t=1162) |
| 2021-12-28 | anti-exploit-and-security | Pickup distance check threshold | 10 studs | Server rejects pickups where distance exceeds 10 | [15:13](https://youtu.be/SFAwwmb8G6o?t=913) |
| 2021-12-28 | anti-exploit-and-security | Demo speed limit exceeded example | speed 40 walk rejected vs 21 max | Hacker walkspeed 40 blocked until speed drops below 21 | [26:55](https://youtu.be/SFAwwmb8G6o?t=1615) |
| 2022-03-01 | data-persistence | DataStore key character limit | 4,000,000 characters |  | [0:00](https://youtu.be/ws3-gfJXw_U?t=0) |
| 2022-03-01 | data-persistence | Parts storable, naive JSON of x/y/z tables | ~70,000 |  | [4:41](https://youtu.be/ws3-gfJXw_U?t=281) |
| 2022-03-01 | data-persistence | Parts storable after integer rounding | ~176,000 |  | [8:29](https://youtu.be/ws3-gfJXw_U?t=509) |
| 2022-03-01 | data-persistence | Parts storable after removing brackets | ~193,000 |  | [13:20](https://youtu.be/ws3-gfJXw_U?t=800) |
| 2022-03-01 | data-persistence | Parts storable after base-90 encoding and removing quotes | ~297,000 |  | [37:30](https://youtu.be/ws3-gfJXw_U?t=2250) |
| 2022-03-01 | data-persistence | Value range: base 10 vs base 16, 3 characters | 1,000 vs 4,096 |  | [18:47](https://youtu.be/ws3-gfJXw_U?t=1127) |
| 2022-03-01 | data-persistence | Base 90 value range, 4 characters | 65,610,000 |  | [19:28](https://youtu.be/ws3-gfJXw_U?t=1168) |
| 2022-04-14 | physics-pathfinding-and-npc-ai | Body mass | ~82 (density 0.3, from 192 at 0.7) | Target car body mass used in the video | [2:47](https://youtu.be/FVOowr2DXbM?t=167) |
| 2022-04-14 | physics-pathfinding-and-npc-ai | Spring stiffness / damping / free length | 3500 / 200 / 2.8 (rear free length 3.2) | Starting suspension tuning values | [14:04](https://youtu.be/FVOowr2DXbM?t=844) |
| 2022-04-14 | physics-pathfinding-and-npc-ai | Wheel density / elasticity / friction | 2 / 0.2 / 1.5 | Custom physical properties for wheels | [14:46](https://youtu.be/FVOowr2DXbM?t=886) |
| 2022-04-14 | physics-pathfinding-and-npc-ai | Rear handbrake motor max torque | 2000 | Unpowered rear wheels act as handbrake | [29:17](https://youtu.be/FVOowr2DXbM?t=1757) |
| 2022-04-14 | physics-pathfinding-and-npc-ai | Drive motor max torque | 5000 (50000 shows wheelies) | Seat Torque value used for drive | [39:01](https://youtu.be/FVOowr2DXbM?t=2341) |
| 2022-04-14 | physics-pathfinding-and-npc-ai | Max speed demo | 25 studs/s, then 40 after change | Speed cap computed from MaxSpeed / wheel radius | [46:05](https://youtu.be/FVOowr2DXbM?t=2765) |
| 2022-04-14 | ui-ux-design | Steering tween time | 0.4 s (from 1 s) | Tween of front attachment orientation | [50:14](https://youtu.be/FVOowr2DXbM?t=3014) |
| 2022-04-14 | physics-pathfinding-and-npc-ai | Turn speed | 30 degrees (default steer scale) | Steer multiplier; 90 looked wrong | [48:51](https://youtu.be/FVOowr2DXbM?t=2931) |
| 2022-07-13 | scripting-and-performance | Script cost, CFrame vs physics | ~8 ms vs ~4 ms (about 50% faster physics), 1,000 parts | Heartbeat CFrame loop vs physics step, benchmark in Studio | [0:41](https://youtu.be/thfUspopuGE?t=41) |
| 2022-07-13 | scripting-and-performance | Frame budget | At 3,000 parts per side, CFrame movement could not finish in one frame | Author's own machine | [4:11](https://youtu.be/thfUspopuGE?t=251) |
| 2022-07-13 | optimization-and-streaming | Incoming server-to-client data, 100 parts | Physics ~40 KB/s vs CFrame ~271 KB/s | Network stats, single client | [9:23](https://youtu.be/thfUspopuGE?t=563) |
| 2022-07-13 | optimization-and-streaming | Incoming data at 200 parts | Physics ~50 KB/s vs CFrame ~542 KB/s | Physics only rose ~10 KB/s when doubling parts | [11:26](https://youtu.be/thfUspopuGE?t=686) |
| 2022-07-13 | optimization-and-streaming | Outgoing client-to-server, CFrame 100 parts | 66 KB/s (physics ~1 KB/s) | Single client | [10:04](https://youtu.be/thfUspopuGE?t=604) |
| 2022-07-13 | optimization-and-streaming | 720p YouTube recommended bitrate | 5 Mbps ≈ 625 KB/s | Author compares to 200-part CFrame data rate | [13:36](https://youtu.be/thfUspopuGE?t=816) |
| 2023-02-13 | scripting-and-performance | Outgoing network (unoptimised) | ~0.2 KB/s idle, ~1.8 KB/s while rotating camera | Naive camera-CFrame RemoteEvent firing, before throttling | [27:59](https://youtu.be/8fV-XOOj6O4?t=1679) |
| 2023-02-13 | scripting-and-performance | Outgoing network (optimised) | ~0.4-0.5 KB/s fast rotation, ~30-40 B/s slow rotation | After dot-product plus time throttling of look vector | [41:58](https://youtu.be/8fV-XOOj6O4?t=2518) |
| 2023-02-13 | scripting-and-performance | Dot-product threshold | 0.99 (~8 degree change); 0.5 sends every ~90 degrees | Look-vector send threshold, minimum 0 to avoid never sending | [30:45](https://youtu.be/8fV-XOOj6O4?t=1845) |
| 2023-02-13 | scripting-and-performance | Minimum send interval | 0.1 s (test used 0.5 s) | Time throttle for camera look-vector RemoteEvent | [35:46](https://youtu.be/8fV-XOOj6O4?t=2146) |
| 2023-02-17 | analytics-metrics | Outgoing network traffic (idle, server to client) | ~0.16 KB/s | Overall outgoing KB/s with one static part in workspace via Stats > Network | [2:45](https://youtu.be/Ng1uYpFcpOA?t=165) |
| 2023-02-17 | analytics-metrics | Outgoing network traffic while moving a part quickly | ~1.5 KB/s | Server moving an anchored=false part left and right | [6:49](https://youtu.be/Ng1uYpFcpOA?t=409) |
| 2023-02-17 | analytics-metrics | Outgoing network traffic when client owns and moves part | 0.18 to 0.8 KB/s | Bob's overall outgoing KB/s while moving network-owned part | [8:56](https://youtu.be/Ng1uYpFcpOA?t=536) |
| 2023-02-21 | anti-exploit-and-security | Damage per click in demo | 20 | Click detector deducts 20 humanoid health per click on dummy head | [2:36](https://youtu.be/hr_8svt1n1E?t=156) |
| 2023-02-27 | scripting-and-performance | Incoming network (server tween) | ~1.66 KB/s while tweening vs ~0.16 KB/s idle | Measured in View > Network Stats with server-side tween running | [0:40](https://youtu.be/ZJnMimf9n5Y?t=40) |
| 2023-02-27 | scripting-and-performance | Incoming network (client tween) | stays ~0.16 KB/s while tweening | Same part tweened locally via RemoteEvent | [9:42](https://youtu.be/ZJnMimf9n5Y?t=582) |
| 2023-02-27 | scripting-and-performance | Tween duration formula | (delay + time) × (repeatCount + 1) | Example: 0+3 = 3 seconds for one non-repeating tween | [15:59](https://youtu.be/ZJnMimf9n5Y?t=959) |
| 2023-03-29 | optimization-and-streaming | Part spacing in test world | 64 studs | Anchored parts spaced 64 studs apart in demo folder | [0:22](https://youtu.be/d8pqcfxqmek?t=22) |
| 2023-03-29 | optimization-and-streaming | Incoming network KB/s, replicated moving parts without streaming | 0.15 to 1.5 KB/s | Moving many parts without streaming raises incoming data | [1:05](https://youtu.be/d8pqcfxqmek?t=65) |
| 2023-03-29 | optimization-and-streaming | Opportunistic stream-out distance formula | TargetRadius + TargetRadius/2 + 64 studs | Target 128 gives 256 studs; target 512 gives 832 studs | [14:15](https://youtu.be/d8pqcfxqmek?t=855) |
| 2023-03-29 | optimization-and-streaming | Example radii used for MinRadius integrity test | 256 studs | Min and target radius set to 256 for pause test | [5:45](https://youtu.be/d8pqcfxqmek?t=345) |
| 2023-06-15 | data-persistence | DataStore autosave interval | 30 seconds | Open DataStore saves automatically every 30 seconds | [8:23](https://youtu.be/UAdE8-AfuMo?t=503) |
| 2023-06-15 | data-persistence | Open retry wait | 6 seconds | Wait between failed open attempts in retry loop | [22:27](https://youtu.be/UAdE8-AfuMo?t=1347) |
| 2023-06-15 | scripting-and-performance | Apple spawn interval | 3 seconds | Demo spawn loop for collectible apples | [36:39](https://youtu.be/UAdE8-AfuMo?t=2199) |
| 2023-06-15 | monetisation-devproducts | Test product price | 100 Robux | Demo coin developer product | [48:20](https://youtu.be/UAdE8-AfuMo?t=2900) |
| 2023-06-16 | data-persistence | Queue default expiry | 7 days (max 45 days) | DataStore:Queue default expiration time | [9:34](https://youtu.be/ykWkDov_x-8?t=574) |
| 2023-06-16 | data-persistence | Queue re-fire interval | 30 seconds | ProcessQueue fires repeatedly until values are removed | [14:26](https://youtu.be/ykWkDov_x-8?t=866) |
| 2023-06-16 | data-persistence | Locked retry interval | 5 seconds, increasing (5, 6, ...) | Retry loop when DataStore open returns locked | [5:46](https://youtu.be/ykWkDov_x-8?t=346) |
| 2023-06-16 | data-persistence | Compression test size | 76 chars reduced to 58 chars | Example table with default compression | [30:23](https://youtu.be/ykWkDov_x-8?t=1823) |
| 2023-06-16 | data-persistence | Default compression decimals | 3 | Decimals setting; default keeps 3 decimal places | [35:15](https://youtu.be/ykWkDov_x-8?t=2115) |
| 2023-06-22 | data-persistence | ProfileService session lock timeout | 30 minutes (OS-time based, auto-save 30s) | ProfileService assumes lock dead after 30 min; OS time unreliable | [4:22](https://youtu.be/ARPfIt16sXI?t=262) |
| 2023-06-22 | data-persistence | Suphi lock default | lock interval 60s, 5 attempts, ~5 min expiry | MemoryStore lock expiration with 30s buffer | [39:18](https://youtu.be/ARPfIt16sXI?t=2358) |
| 2023-06-22 | data-persistence | DataStore budget per player | 10 sets, 10 gets, 2 sorted gets | Ordered-backup save uses 2 sets per save and a sorted get per load | [13:23](https://youtu.be/ARPfIt16sXI?t=803) |
| 2023-06-22 | data-persistence | Roblox DataStore version retention | up to 30 days | Built-in versioning keeps previous values | [11:18](https://youtu.be/ARPfIt16sXI?t=678) |
| 2023-06-22 | data-persistence | Old per-key write limit | once per 6 seconds (removed) | Roblox reportedly removed the six-second write limit | [11:59](https://youtu.be/ARPfIt16sXI?t=719) |
| 2023-06-22 | data-persistence | Lowest suggested lock settings | 3 attempts, 30s between attempts | Suphi's advice for minimum lock timeout | [45:35](https://youtu.be/ARPfIt16sXI?t=2735) |
| 2023-08-29 | scripting-and-performance | Path movement network traffic | near zero | Synced path movement between clients via GetServerTimeNow, per video's network stats | [0:25](https://youtu.be/OAZvYqbzOWI?t=25) |
| 2023-08-29 | optimization-and-streaming | Streaming Target Radius (test setting) | 128 | Lowered for testing content streaming; WalkSpeed set to 20 | [31:29](https://youtu.be/OAZvYqbzOWI?t=1889) |
| 2023-08-29 | scripting-and-performance | Example path speed | 10 studs/second | Speed parameter divides arc length; example uses 10 and 2 | [29:05](https://youtu.be/OAZvYqbzOWI?t=1745) |
| 2024-01-07 | client-server-and-remotes | timeout duration | 5 seconds used in custom invoke example |  | [5:46](https://youtu.be/A14qFAyFYhQ?t=346) |
| 2024-01-07 | client-server-and-remotes | test: client wait 2s vs 6s | 2s response succeeds; 6s returns nil |  | [14:46](https://youtu.be/A14qFAyFYhQ?t=886) |
| 2024-08-06 | scripting-and-performance | table.remove shift cost | around 500 items after target before linked list matches | Creator's personal benchmark for table.remove vs link update | [11:14](https://youtu.be/DTEraIOfoS0?t=674) |
| 2024-08-06 | scripting-and-performance | Array size threshold for performance concern | 5,000+ items | Only when removing or inserting at the front of the list | [14:39](https://youtu.be/DTEraIOfoS0?t=879) |
| 2024-08-06 | scripting-and-performance | Thread recycling | Pool stays short with spawn; slightly larger with defer | Creator's description of cached thread array size | [1:23:19](https://youtu.be/DTEraIOfoS0?t=4999) |
| 2024-10-10 | optimization-and-streaming | CPU usage (animation door, moving) | ~16 ms (idle ~5) | 60 cloned doors in test, animation playback | [18:23](https://youtu.be/ZPviBfpPloE?t=1103) |
| 2024-10-10 | optimization-and-streaming | CPU usage (tween door, moving) | ~60 ms (idle ~5) | 60 doors in test, tweened | [20:29](https://youtu.be/ZPviBfpPloE?t=1229) |
| 2024-10-10 | optimization-and-streaming | Received network data (tween door) | ~1,800 KB/s while moving | Tween replicates property changes constantly | [21:10](https://youtu.be/ZPviBfpPloE?t=1270) |
| 2024-10-10 | optimization-and-streaming | Received network data (animation door) | ~100 KB spike at start, ~0 while playing | Only play state replicates | [19:47](https://youtu.be/ZPviBfpPloE?t=1187) |
| 2024-10-10 | optimization-and-streaming | CPU and network (physics door) | ~32 ms CPU, ~41 KB/s | Hinge servo, angular speed 0.3 throttled; 3.3 fixes opening | [21:54](https://youtu.be/ZPviBfpPloE?t=1314) |
| 2024-10-10 | building-and-level-design | Tween rotation angle | -112.5 degrees | Slab orientation read from keyframe; used for door opening | [14:00](https://youtu.be/ZPviBfpPloE?t=840) |
| 2024-10-10 | scripting-and-performance | Loop timing | 10 s open, 10 s close | Door demo loop with wait intervals | [10:30](https://youtu.be/ZPviBfpPloE?t=630) |
| 2024-10-10 | building-and-level-design | Attachment offsets | 0.5 frame, 3.5 slab | Pivot at frame edge for hinge and Motor6D | [15:22](https://youtu.be/ZPviBfpPloE?t=922) |
| 2024-10-13 | building-art-and-assets | Rotation keyframe spin | 360° in 1 s, playback speed 0.25 for slower spin | Spinning part test with looping animation | [4:12](https://youtu.be/AkF-4x7qfzM?t=252) |
| 2024-10-13 | building-art-and-assets | Rotation steps | 1440° per second split into 10 steps of 144°, applied as 2×72° | Part spiralling around center four times per rotation | [7:45](https://youtu.be/AkF-4x7qfzM?t=465) |
| 2024-10-13 | scripting-and-performance | Playback speed formula | speed = 1 / seconds per cycle (e.g. 10 s = 0.1) | Adjusting AnimationTrack speed for timing | [11:23](https://youtu.be/AkF-4x7qfzM?t=683) |
| 2024-10-13 | client-server-and-remotes | Late-joiner sync | Late joiners sync to same position as others when paused or playing | Tested in local server with one client | [14:28](https://youtu.be/AkF-4x7qfzM?t=868) |
| 2024-10-13 | scripting-and-performance | CPU cost | ~6 ms, same for paused and stopped tracks | Test loop of cloned models in Studio | [18:57](https://youtu.be/AkF-4x7qfzM?t=1137) |
| 2024-10-13 | testing-debugging-and-qa | Simulated incoming replication lag | 1 s (door opens 1 s later on client) | Studio Settings network test | [22:44](https://youtu.be/AkF-4x7qfzM?t=1364) |
| 2024-10-13 | building-art-and-assets | Keyframe times used for door markers | Marker times 0, 0.4, 0.5, 0.8, 0.1, 0.9 | Buffered start and end markers for bidirectional door | [29:42](https://youtu.be/AkF-4x7qfzM?t=1782) |
| 2024-11-28 | scripting-and-performance | Thread recycling speedup | ~2x vs creating new Freds per defer (speaker claim) |  | [46:24](https://youtu.be/SVLFkdeh6c8?t=2784) |
| 2024-11-28 | analytics-metrics | Plugin analysis time per large script | ~0.06s (500-line script); module update ~0.005s |  | [23:21](https://youtu.be/SVLFkdeh6c8?t=1401) |
| 2024-11-28 | data-persistence | Demo save interval | 30 seconds (tested at 5s) |  | [1:27:23](https://youtu.be/SVLFkdeh6c8?t=5243) |
| 2024-11-28 | data-persistence | Load delay after join instead of session lock | 5 seconds |  | [1:39:08](https://youtu.be/SVLFkdeh6c8?t=5948) |
| 2024-11-28 | combat-and-gameplay-systems | Item respawn timer | 5-10s first, 10-15s after collection |  | [2:14:55](https://youtu.be/SVLFkdeh6c8?t=8095) |
| 2025-03-09 | scripting-and-performance | average CPU time | BulkMoveTo ~28 ms vs Motor6D ~25 ms | Author's benchmark on client, moving many parts per frame | [17:12](https://youtu.be/BRYp2-rdpXQ?t=1032) |
| 2025-03-09 | core-loops-and-game-design | tween duration | 1 second, Elastic easing, Out direction | Door open/close tween settings in the example | [8:56](https://youtu.be/BRYp2-rdpXQ?t=536) |
| 2025-03-26 | scripting-and-performance | Default response timeout | 10 seconds | Packet remote invoke default; configurable via responseTimeout | [1:09:37](https://youtu.be/WoIElUdj64A?t=4177) |
| 2025-03-26 | anti-exploit-and-security | Inbound buffer size limit | 16,000 bytes | Packet discards client buffers above this to prevent server crash | [48:51](https://youtu.be/WoIElUdj64A?t=2931) |
| 2025-03-26 | scripting-and-performance | Unreliable remote event limit | 1,000 bytes | Reason batching unreliable events is discouraged | [49:42](https://youtu.be/WoIElUdj64A?t=2982) |
| 2025-03-26 | scripting-and-performance | 1000 events per frame bytes | Roblox 14 KB vs Packet 1 KB | Packet Profiler benchmark with batching | [59:50](https://youtu.be/WoIElUdj64A?t=3590) |
| 2025-03-26 | scripting-and-performance | Number byte cost | Roblox 9 bytes vs Packet F16 8 bytes, U8 1 byte | Per number sent; Packet overhead is 3 bytes per buffer | [1:01:55](https://youtu.be/WoIElUdj64A?t=3715) |
| 2025-03-26 | scripting-and-performance | CFrame byte cost | Roblox 20 bytes vs Packet 18 bytes (largest) and 12 bytes (smallest) | Single CFrame per fire; array of 4 gives 96 vs 91 vs smaller | [1:04:42](https://youtu.be/WoIElUdj64A?t=3882) |
| 2025-03-26 | scripting-and-performance | String byte cost | 1 byte length prefix plus characters; U8 max 255 chars | Use U16 length prefix for up to 65,535 characters | [27:41](https://youtu.be/WoIElUdj64A?t=1661) |
