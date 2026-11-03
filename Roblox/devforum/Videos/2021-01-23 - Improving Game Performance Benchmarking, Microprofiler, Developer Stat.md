---
title: "Improving Game Performance: Benchmarking, Microprofiler, Developer Stats, and Developer Console"
url: https://devforum.roblox.com/t/improving-game-performance-benchmarking-microprofiler-developer-stats-and-developer-console/1002074
creator: Roblox DevForum
official: false
advice_density: high
date: 2021-01-23
views: 214
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Improving Game Performance: Benchmarking, Microprofiler, Developer Stats, and Developer Console

[Open](https://devforum.roblox.com/t/improving-game-performance-benchmarking-microprofiler-developer-stats-and-developer-console/1002074) | Roblox DevForum | 214 views | 2021-01-23

## Summary
Guide by TechSpectrum on benchmarking Roblox game performance across devices using Developer Stats, Developer Console and Microprofiler, using the FPS shooter Polybattle as the example. Covers test setup pitfalls, recommended test devices, optimization tips, and target ms/MB figures.

## Tips
- [page](https://devforum.roblox.com/t/improving-game-performance-benchmarking-microprofiler-developer-stats-and-developer-console/1002074) **[[testing-debugging-and-qa]]** Test on the same map and server across all devices, e.g. follow one alt account on multiple devices at once, so results are comparable.
- [page](https://devforum.roblox.com/t/improving-game-performance-benchmarking-microprofiler-developer-stats-and-developer-console/1002074) **[[testing-debugging-and-qa]]** Stress test with Graphics Mode Manual, Graphics Quality 10 and Performance Stats On on every device; Automatic mode gives misleading results.
- [page](https://devforum.roblox.com/t/improving-game-performance-benchmarking-microprofiler-developer-stats-and-developer-console/1002074) **[[testing-debugging-and-qa]]** Test with background apps running, since real players rarely close everything else; also test without them to isolate causes.
- [page](https://devforum.roblox.com/t/improving-game-performance-benchmarking-microprofiler-developer-stats-and-developer-console/1002074) **[[testing-debugging-and-qa]]** Do not trust Studio or emulator performance numbers; Studio has overhead and emulation does not match real phone CPU/GPU. Use emulation only for compatibility and UI layout.
- [page](https://devforum.roblox.com/t/improving-game-performance-benchmarking-microprofiler-developer-stats-and-developer-console/1002074) **[[testing-debugging-and-qa]]** Test in different map locations, since streaming and content distribution make some areas lower-performing.
- [page](https://devforum.roblox.com/t/improving-game-performance-benchmarking-microprofiler-developer-stats-and-developer-console/1002074) **[[testing-debugging-and-qa]]** Save mobile profiler dumps and microprofiler captures so the team can inspect performance problems later.
- [page](https://devforum.roblox.com/t/improving-game-performance-benchmarking-microprofiler-developer-stats-and-developer-console/1002074) **[[optimization-and-streaming]]** Enable Streaming Enabled and code for its limitations; the author says this is the path to top performance for low-end users.
- [page](https://devforum.roblox.com/t/improving-game-performance-benchmarking-microprofiler-developer-stats-and-developer-console/1002074) **[[optimization-and-streaming]]** Disable ShadowCast on parts except key buildings that need shadows to reduce shadows the client renders.
- [page](https://devforum.roblox.com/t/improving-game-performance-benchmarking-microprofiler-developer-stats-and-developer-console/1002074) **[[optimization-and-streaming]]** Reduce mesh count and polycount; Roblox does not compress meshes, so a 1 MB mesh costs 1 MB in memory.
- [page](https://devforum.roblox.com/t/improving-game-performance-benchmarking-microprofiler-developer-stats-and-developer-console/1002074) **[[optimization-and-streaming]]** Compress audio to OGG; it has the lowest memory cost of supported formats. Limit how much audio plays at once.
- [page](https://devforum.roblox.com/t/improving-game-performance-benchmarking-microprofiler-developer-stats-and-developer-console/1002074) **[[optimization-and-streaming]]** Shrink textures (e.g. 1024x1024 to 512x512) and use JPEG instead of PNG; many uncompressed textures can exceed 200 MB.
- [page](https://devforum.roblox.com/t/improving-game-performance-benchmarking-microprofiler-developer-stats-and-developer-console/1002074) **[[optimization-and-streaming]]** Set Mesh RenderFidelity to Performance on anything not key to the experience, such as distant islands.
- [page](https://devforum.roblox.com/t/improving-game-performance-benchmarking-microprofiler-developer-stats-and-developer-console/1002074) **[[optimization-and-streaming]]** Set Mesh CollisionFidelity to Box for complex meshes like crates to cut physics collision work.
- [page](https://devforum.roblox.com/t/improving-game-performance-benchmarking-microprofiler-developer-stats-and-developer-console/1002074) **[[optimization-and-streaming]]** Disable CanCollide on parts that are touched but do not need collision, so they are not physics-checked.
- [page](https://devforum.roblox.com/t/improving-game-performance-benchmarking-microprofiler-developer-stats-and-developer-console/1002074) **[[optimization-and-streaming]]** Avoid unnecessary lighting effects such as blur; they cost performance and players on quality 10 see them.
- [page](https://devforum.roblox.com/t/improving-game-performance-benchmarking-microprofiler-developer-stats-and-developer-console/1002074) **[[client-server-and-remotes]]** Run heavy animations on the client rather than the server to free server Task Scheduler time.
- [page](https://devforum.roblox.com/t/improving-game-performance-benchmarking-microprofiler-developer-stats-and-developer-console/1002074) **[[client-server-and-remotes]]** Avoid sending large packets through RemoteEvents and RemoteFunctions; keep Sent and Received under 5-10 ms (Roblox suggests 50 as a ceiling).
- [page](https://devforum.roblox.com/t/improving-game-performance-benchmarking-microprofiler-developer-stats-and-developer-console/1002074) **[[analytics-metrics]]** Use Developer Stats targets: Memory 400-600 MB realistic, CPU and GPU frame time ideally 15-20 ms, not the 33 ms ceiling.
- [page](https://devforum.roblox.com/t/improving-game-performance-benchmarking-microprofiler-developer-stats-and-developer-console/1002074) **[[analytics-metrics]]** Diagnose network with Sent and Received stats; ping depends on the player's connection, so investigate high ping only after those are fine.
- [page](https://devforum.roblox.com/t/improving-game-performance-benchmarking-microprofiler-developer-stats-and-developer-console/1002074) **[[scripting-and-performance]]** Use the Microprofiler at peak spikes, zoom in, and identify which tasks consume time in each frame.
- [page](https://devforum.roblox.com/t/improving-game-performance-benchmarking-microprofiler-developer-stats-and-developer-console/1002074) **[[optimization-and-streaming]]** Use the Developer Console memory view to find which client-side parts of the place use the most memory, such as overly many textures.
- [page](https://devforum.roblox.com/t/improving-game-performance-benchmarking-microprofiler-developer-stats-and-developer-console/1002074) **[[optimization-and-streaming]]** Mobile RAM varies widely; a 2 GB iPhone 8 showed 700-800 MB memory use vs 300-400 MB on a 4 GB Galaxy S9, so design memory budgets for the low end.
- [page](https://devforum.roblox.com/t/improving-game-performance-benchmarking-microprofiler-developer-stats-and-developer-console/1002074) **[[testing-debugging-and-qa]]** Build a test device set spanning low to high end (e.g. Galaxy S9, iPhone 8, iPad 9.7, Xbox One S, a 4-8 GB home PC) to cover the player base.

## Numbers
- [page](https://devforum.roblox.com/t/improving-game-performance-benchmarking-microprofiler-developer-stats-and-developer-console/1002074) Memory target: **400-600 MB realistic (official 200 MB unreachable)** (Developer Stats memory guidance for performance tests)
- [page](https://devforum.roblox.com/t/improving-game-performance-benchmarking-microprofiler-developer-stats-and-developer-console/1002074) CPU frame target: **15-20 ms (ceiling 33 ms)** (Developer Stats CPU; Polybattle mobile averages 15-18 ms)
- [page](https://devforum.roblox.com/t/improving-game-performance-benchmarking-microprofiler-developer-stats-and-developer-console/1002074) GPU frame target: **15-20 ms (ceiling 33 ms)** (Developer Stats GPU guidance)
- [page](https://devforum.roblox.com/t/improving-game-performance-benchmarking-microprofiler-developer-stats-and-developer-console/1002074) Sent/Received network time: **under 5-10 ms (Roblox recommends 50)** (Developer Stats network guidance)
- [page](https://devforum.roblox.com/t/improving-game-performance-benchmarking-microprofiler-developer-stats-and-developer-console/1002074) Texture memory overrun: **over 200 MB if many textures uncompressed** (Warning on stacking textures)
- [page](https://devforum.roblox.com/t/improving-game-performance-benchmarking-microprofiler-developer-stats-and-developer-console/1002074) Galaxy S9 memory (4 GB RAM): **300-400 MB playing Polybattle** (Developer Stats memory example)
- [page](https://devforum.roblox.com/t/improving-game-performance-benchmarking-microprofiler-developer-stats-and-developer-console/1002074) iPhone 8 memory (2 GB RAM): **700-800 MB playing Polybattle** (Developer Stats memory example)
- [page](https://devforum.roblox.com/t/improving-game-performance-benchmarking-microprofiler-developer-stats-and-developer-console/1002074) Graphics quality for tests: **10 (manual mode)** (Standard setting for stress-test comparisons)

## Games
- **Polybattle**: Gamefam FPS with vehicles; author uses it as benchmark, averaging 15-18 ms CPU on mobile and low Sent/Received times despite shooting and vehicles.

## Tools
Developer Stats, Developer Console, Microprofiler, Mobile memory profiler, Roblox Studio emulator

## He points to
- https://developer.roblox.com/en-us/articles/Improving-Performance
- https://developer.roblox.com/en-us/articles/Developer-Console
- https://developer.roblox.com/en-us/articles/MicroProfiler
- Gavin's microprofiler cheat sheet

## Topics
[[analytics-metrics]] [[client-server-and-remotes]] [[optimization-and-streaming]] [[scripting-and-performance]] [[testing-debugging-and-qa]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
