---
title: "Docs: studio / network-simulator"
url: https://create.roblox.com/docs/studio/network-simulator.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: studio / network-simulator

[Open](https://create.roblox.com/docs/studio/network-simulator.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on Network Simulator, a Studio beta tool that adds per-direction latency, jitter and packet loss to playtests. Covers presets, custom and saved configs, script properties, and a workflow for testing network-sensitive features and diagnosing results.

## Tips
- [page](https://create.roblox.com/docs/studio/network-simulator) **[[playtesting-and-feedback]]** Run a baseline on Ideal Fiber, then repeat the same journey on Home Wi-Fi or Standard Mobile (4G/LTE) and Bad Connection (3G) to isolate network-caused problems.
- [page](https://create.roblox.com/docs/studio/network-simulator) **[[testing-debugging-and-qa]]** Change only inbound or outbound values to find which direction (client-to-server requests vs server-to-client replication) causes the problem.
- [page](https://create.roblox.com/docs/studio/network-simulator) **[[client-server-and-remotes]]** Give immediate local feedback while waiting for server confirmation so players don't perceive server-authoritative actions as stuck.
- [page](https://create.roblox.com/docs/studio/network-simulator) **[[anti-exploit-and-security]]** Make repeated input idempotent so the same action cannot submit more than once when the connection is slow.
- [page](https://create.roblox.com/docs/studio/network-simulator) **[[first-session-onboarding]]** Distinguish slow work from failure in loading and progress states, and offer a safe retry path on timeouts.
- [page](https://create.roblox.com/docs/studio/network-simulator) **[[optimization-and-streaming]]** Use MicroProfiler network capture to tell whether a delay is replication, physics or other network data, and separate it from frame-time problems.
- [page](https://create.roblox.com/docs/studio/network-simulator) **[[testing-debugging-and-qa]]** Apply each network condition before starting an interaction; changing latency mid-run can affect congestion control and muddy comparisons.
- [page](https://create.roblox.com/docs/studio/network-simulator) **[[testing-debugging-and-qa]]** Repeat baseline and impaired runs with the same scenario and observation method rather than trusting a single poor-connection run.
- [page](https://create.roblox.com/docs/studio/network-simulator) **[[client-server-and-remotes]]** Ensure unreliable updates can be skipped without leaving stale state on screen, and recover cleanly when the connection improves.
- [page](https://create.roblox.com/docs/studio/network-simulator) **[[client-server-and-remotes]]** Ping is round-trip: added inbound and outbound latency both count, so 10 ms each adds about 20 ms to RTT.
- [page](https://create.roblox.com/docs/studio/network-simulator) **[[testing-debugging-and-qa]]** Set all six values to 0 as a custom config for a true zero-delay comparison, since Ideal Fiber still adds 8 ms per direction.
- [page](https://create.roblox.com/docs/studio/network-simulator) **[[testing-debugging-and-qa]]** In Team Tests, configured values stack on top of real geographic latency and packet loss, so account for existing conditions.

## Numbers
- [page](https://create.roblox.com/docs/studio/network-simulator) Ideal Fiber preset: **8 ms latency / 0 ms jitter / 0.00% loss per direction**
- [page](https://create.roblox.com/docs/studio/network-simulator) Home Wi-Fi preset: **Inbound 30/12/0.20%; Outbound 30/15/0.30%**
- [page](https://create.roblox.com/docs/studio/network-simulator) Standard Mobile 4G/LTE preset: **Inbound 45/20/0.40%; Outbound 55/30/0.50%**
- [page](https://create.roblox.com/docs/studio/network-simulator) Bad Connection 3G preset: **Inbound 150/70/0.50%; Outbound 180/90/0.50%**
- [page](https://create.roblox.com/docs/studio/network-simulator) Custom latency and jitter range: **0–1000 ms, 0.1 ms precision**
- [page](https://create.roblox.com/docs/studio/network-simulator) Custom packet loss range: **0.00–0.50%, 0.01% precision**

## Tools
Network Simulator (Studio beta, File > Beta Features > New Device Simulator), Studio Device Simulator, Developer Console, MicroProfiler network capture, NetworkSettings properties (script/plugin control)

## He points to
- Studio Settings Network tab

## Topics
[[anti-exploit-and-security]] [[client-server-and-remotes]] [[first-session-onboarding]] [[optimization-and-streaming]] [[playtesting-and-feedback]] [[testing-debugging-and-qa]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
