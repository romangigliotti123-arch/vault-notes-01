---
title: "Docs: performance-optimization / test-on-hardware"
url: https://create.roblox.com/docs/performance-optimization/test-on-hardware.md
creator: Roblox Creator Docs
official: true
advice_density: high
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: performance-optimization / test-on-hardware

[Open](https://create.roblox.com/docs/performance-optimization/test-on-hardware.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on testing games on real hardware. Covers why emulation misses memory, frame rate, thermal throttling and input latency; the player device mix (Android ~65%, RAM tiers, Passmark benchmarks); on-device profiling tools; thermal, network, UX, loading and audio checks.

## Tips
- [page](https://create.roblox.com/docs/performance-optimization/test-on-hardware) **[[testing-debugging-and-qa]]** Test on real devices; Studio emulation misses memory pressure, thermal throttling and touch latency. Studio runs on a far stronger machine than most players use.
- [page](https://create.roblox.com/docs/performance-optimization/test-on-hardware) **[[testing-debugging-and-qa]]** Pick at least one low-end baseline device matching your target player demographic; testing only on a dev PC covers the minority of your audience.
- [page](https://create.roblox.com/docs/performance-optimization/test-on-hardware) **[[testing-debugging-and-qa]]** Use a range of Android devices across performance levels and manufacturers rather than one flagship phone.
- [page](https://create.roblox.com/docs/performance-optimization/test-on-hardware) **[[optimization-and-streaming]]** Use MicroProfiler (Ctrl+Alt+F6 / Cmd+Opt+F6) and Developer Console (F9, Memory tab) on device to get real frame times and memory readings.
- [page](https://create.roblox.com/docs/performance-optimization/test-on-hardware) **[[optimization-and-streaming]]** Enable Performance Stats in settings to view FPS, memory and ping overlay during on-device tests.
- [page](https://create.roblox.com/docs/performance-optimization/test-on-hardware) **[[optimization-and-streaming]]** Run a 10–15 minute mobile session and watch for steady FPS decline, which indicates thermal throttling; then cut sustained GPU/CPU load in hot paths.
- [page](https://create.roblox.com/docs/performance-optimization/test-on-hardware) **[[optimization-and-streaming]]** Confirm network behaviour over cellular or constrained Wi-Fi; simulation in Studio is only for quick iteration.
- [page](https://create.roblox.com/docs/performance-optimization/test-on-hardware) **[[analytics-metrics]]** Use the Performance Dashboard to track FPS, memory and crash rates by device category after publish; a crash spike after an update suggests a low-end memory regression.
- [page](https://create.roblox.com/docs/performance-optimization/test-on-hardware) **[[ui-ux-design]]** Test touch targets, gesture conflicts and thumbstick/button reach on real phone screens, not emulated resolutions.
- [page](https://create.roblox.com/docs/performance-optimization/test-on-hardware) **[[ui-ux-design]]** Check text size, icon clarity and contrast on your lowest-supported device at arm's-length viewing distance.
- [page](https://create.roblox.com/docs/performance-optimization/test-on-hardware) **[[cross-platform-and-console]]** Verify the UI responds correctly when players switch input type mid-session, such as connecting a Bluetooth controller or switching trackpad to mouse.
- [page](https://create.roblox.com/docs/performance-optimization/test-on-hardware) **[[optimization-and-streaming]]** Time the full join-to-gameplay flow on the baseline device; if loads exceed a few seconds, consider instance streaming and check for pop-in during movement.
- [page](https://create.roblox.com/docs/performance-optimization/test-on-hardware) **[[sound-and-music]]** Test audio on both device speakers and headphones; phone speakers can make SFX and voice muddy or inaudible.
- [page](https://create.roblox.com/docs/performance-optimization/test-on-hardware) **[[cross-platform-and-console]]** Multi-input devices (handheld gamepads with touchscreens, phones with USB-C gamepad adapters) cover touch and gamepad testing on one device.

## Numbers
- [page](https://create.roblox.com/docs/performance-optimization/test-on-hardware) Android share of player base: **~65% of a typical game's players** (General device statistics across Roblox user base)
- [page](https://create.roblox.com/docs/performance-optimization/test-on-hardware) Android RAM distribution: **~60% have 2–4 GB; ~35% 4–8 GB; ~5% over 8 GB** (Android players in typical game)
- [page](https://create.roblox.com/docs/performance-optimization/test-on-hardware) Passmark score of player devices: **>50% score 10,000–20,000** (Share of Roblox player base on Passmark benchmarks)
- [page](https://create.roblox.com/docs/performance-optimization/test-on-hardware) Extended mobile thermal test length: **10–15 minutes of active gameplay** (Session length to detect thermal throttling)

## Tools
Studio device emulator, MicroProfiler, Developer Console, Performance Stats overlay, Performance Dashboard

## He points to
- Identify performance issues
- Design for performance
- Cross-platform development
- Adaptive design

## Topics
[[analytics-metrics]] [[cross-platform-and-console]] [[optimization-and-streaming]] [[sound-and-music]] [[testing-debugging-and-qa]] [[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
