---
title: crusherfiredev - Numbers & Benchmarks
tags: [roblox, crusherfiredev]
creator_trust: TRUSTED
creator_score: 8.7
---

> [!note] Trust: TRUSTED (credibility audit score 8.7): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# crusherfiredev: Numbers & Benchmarks

| Date | Topic | Metric | Value | Context | Source |
|---|---|---|---|---|---|
| 2024-01-18 | scripting-and-performance | Server wait before cloning test model | 10 seconds |  | [14:08](https://youtu.be/7tzy1DuPcBQ?t=848) |
| 2024-01-20 | sound-and-music | Volumetric audio release | Dev Forum post July 2022; planned Automatic default update in 2023 not done as of Jan 2024 |  | [1:02](https://youtu.be/2VZ7DQHYPn8?t=62) |
| 2024-01-23 | updates-live-ops | Deferred engine events rollout | Announced Nov 2023; new games default to deferred; default workspace setting switches to deferred Feb 2024 |  | [0:00](https://youtu.be/xz_G2n1Q8-U?t=0) |
| 2024-01-23 | scripting-and-performance | Test frame | Bindable tests fired at frame 100 of Heartbeat count |  | [8:54](https://youtu.be/xz_G2n1Q8-U?t=534) |
| 2024-02-01 | optimization-and-streaming | Average frame time with four 1M-iteration serial loops | 67 ms |  | [14:03](https://youtu.be/MyM3JkHEPmA?t=843) |
| 2024-02-01 | optimization-and-streaming | Frame time after splitting scripts into two Actors | 30-40 ms (from 60-70 ms) |  | [19:23](https://youtu.be/MyM3JkHEPmA?t=1163) |
| 2024-02-01 | optimization-and-streaming | Frame time of 72 serial AI deer vs 72 parallel deer | ~50 ms serial vs ~16 ms parallel |  | [26:54](https://youtu.be/MyM3JkHEPmA?t=1614) |
| 2024-02-01 | optimization-and-streaming | Cost of 100,000-iteration loop per frame in RenderStepped | ~6 ms |  | [5:43](https://youtu.be/MyM3JkHEPmA?t=343) |
| 2024-05-18 | scripting-and-performance | Linear search execution time | 0.032 s for thousands of tagged parts (160-stud radius) |  | [8:13](https://youtu.be/OksI7HpEd6w?t=493) |
| 2024-05-18 | scripting-and-performance | Octree radius search execution time | 0.002 s for same query |  | [8:13](https://youtu.be/OksI7HpEd6w?t=493) |
| 2024-05-18 | scripting-and-performance | Relative slowdown of linear search | ~1,500% slower (reported as 1,2103%, likely transcription error) |  | [8:13](https://youtu.be/OksI7HpEd6w?t=493) |
| 2024-05-18 | scripting-and-performance | Example object count | 5,000 trees; speaker's test used thousands of parts |  | [0:00](https://youtu.be/OksI7HpEd6w?t=0) |
| 2024-10-18 | analytics-metrics | Memory pressure threshold used in demo | 50,000 parts |  | [3:43](https://youtu.be/K6TryCAqFbs?t=223) |
| 2024-10-18 | scripting-and-performance | Reported slowdown adding many parts at once | twice as slow or more (per forum commenter) |  | [19:32](https://youtu.be/K6TryCAqFbs?t=1172) |
| 2025-03-22 | scripting-and-performance | task.delay accuracy | 1 second delay measured ~1.12 s via os.clock | Test of task.delay(1) timing in Studio | [16:26](https://youtu.be/0jAZOpNHqv8?t=986) |
| 2025-03-22 | scripting-and-performance | task.delay(0) resume point | next Heartbeat, frame 94 in same frame as RenderStepped | Micro profiler test result | [20:34](https://youtu.be/0jAZOpNHqv8?t=1234) |
| 2025-04-19 | analytics-metrics | incoming network data threshold | ~50 KB/s | Common standard suggested for deciding whether buffer optimisation is worth it | [0:40](https://youtu.be/M2YKE07cUOc?t=40) |
| 2025-04-19 | scripting-and-performance | packet size: 150 as 64-bit number vs u8 buffer | 9 bytes vs 3 bytes | Packet Profiler measurement, single value | [15:47](https://youtu.be/M2YKE07cUOc?t=947) |
| 2025-04-19 | scripting-and-performance | Color3 packet size | 13 bytes vs 5 bytes | Color3 raw vs serialized into buffer | [19:25](https://youtu.be/M2YKE07cUOc?t=1165) |
| 2025-04-19 | scripting-and-performance | 100 u16 IDs packet size | 900 bytes (array) vs 203 bytes (buffer) | Array of 100 IDs vs 200-byte buffer including overhead | [26:30](https://youtu.be/M2YKE07cUOc?t=1590) |
| 2025-04-19 | scripting-and-performance | Sera enemy dictionary packet size | 53 bytes vs 11 bytes | Dictionary with health, shield, unique ID serialized via Sera | [34:30](https://youtu.be/M2YKE07cUOc?t=2070) |
| 2025-05-24 | code-architecture-and-frameworks | Disco part color change interval | 0.25 seconds | Example loop delay in observer demo | [4:55](https://youtu.be/Nqtpzrkwm1Q?t=295) |
| 2025-05-24 | scripting-and-performance | Throttle delay for bulk sound | 0.01 seconds | Small delay pushes bulk child-added calls to one sound | [13:03](https://youtu.be/Nqtpzrkwm1Q?t=783) |
| 2025-05-24 | matchmaking-and-teleport | Sound load timeout | 5 seconds | Skip sounds that fail to load in music queue | [19:58](https://youtu.be/Nqtpzrkwm1Q?t=1198) |
| 2025-06-14 | luau-language-and-types | Closure memory | ~32 + 28n bytes per closure (n = external upvalues) | Per Lua creators' article; n is number of upvalues used | [5:09](https://youtu.be/oUjrs6Apd7A?t=309) |
| 2025-06-14 | luau-language-and-types | Measured memory increase | +1,644,000 bytes for 10,000 closures with 5 upvalues each | Lua heap snapshot comparison; predicted ~1.72 MB | [23:45](https://youtu.be/oUjrs6Apd7A?t=1425) |
| 2025-06-14 | luau-language-and-types | Upvalue limit | 200 | Max upvalues/local registers per scope before error | [19:51](https://youtu.be/oUjrs6Apd7A?t=1191) |
| 2025-06-14 | luau-language-and-types | Loop closure test | 10 iterations → 10 distinct closures when capturing loop variable | Capturing per-iteration local prevents caching | [9:36](https://youtu.be/oUjrs6Apd7A?t=576) |
| 2025-07-25 | analytics-metrics | Physics parts memory | ~1 MB base template; ~420 MB in his project; 1000 MB is a concern threshold |  | [1:42](https://youtu.be/YWyJHwynM1M?t=102) |
| 2025-07-25 | optimization-and-streaming | Sounds memory | ~500 MB is a sign of too many loaded sounds; his game uses 58 MB after runtime sound creation |  | [9:04](https://youtu.be/YWyJHwynM1M?t=544) |
| 2025-07-25 | building-art-and-assets | Texture memory | 1024x1024 uses 4x graphics memory of 512x512 |  | [14:23](https://youtu.be/YWyJHwynM1M?t=863) |
| 2025-07-25 | optimization-and-streaming | Scene draw count budget | ~500 (Mr. Chicken Rocket recommendation); ~500k triangles |  | [16:05](https://youtu.be/YWyJHwynM1M?t=965) |
| 2025-07-25 | optimization-and-streaming | Mesh render fidelity distances | <250 studs high, 250-500 medium, >500 lowest |  | [25:29](https://youtu.be/YWyJHwynM1M?t=1529) |
| 2025-07-25 | optimization-and-streaming | Incoming network baseline | below 50 KB/s consistently |  | [33:07](https://youtu.be/YWyJHwynM1M?t=1987) |
| 2025-07-25 | optimization-and-streaming | BulkMoveTo timing | ~0.49ms individual vs 0.255ms with FireCFrameChanged (~50% faster) |  | [31:16](https://youtu.be/YWyJHwynM1M?t=1876) |
| 2025-07-25 | optimization-and-streaming | Bandwidth reduction (dev forum case) | 300-350 KB/s down to ~5 KB/s (60x) |  | [36:33](https://youtu.be/YWyJHwynM1M?t=2193) |
| 2025-07-25 | building-art-and-assets | Shipping container draw calls | reduced 50% by reusing mesh IDs |  | [23:34](https://youtu.be/YWyJHwynM1M?t=1414) |
| 2025-08-10 | analytics-metrics | Yield warning interval | loader warns after 10s yield threshold, repeats every 5s | Module loader yield warning behaviour in demo | [9:59](https://youtu.be/dJjZ7ml9bSo?t=599) |
| 2025-08-10 | analytics-metrics | Video views | 31874 | Video view count at upload (2025-08-10) | [31874](https://youtu.be/dJjZ7ml9bSo?t=31874) |
| 2026-10-24 | development-process-and-speed | Refactor time | Weeks by hand vs 1-2 days with AI | Speaker's own older project refactored to new architecture standards | [3:52](https://youtu.be/4n7thZAAF-E?t=232) |
| 2026-10-24 | ui-ux-design | UI build time | Several hours iterative AI work vs 1-2 weeks by hand | Speaker's custom interface; finished in a few days total | [7:06](https://youtu.be/4n7thZAAF-E?t=426) |
