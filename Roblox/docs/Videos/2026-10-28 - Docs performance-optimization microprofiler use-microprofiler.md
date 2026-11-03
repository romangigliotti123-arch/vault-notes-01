---
title: "Docs: performance-optimization / microprofiler / use-microprofiler"
url: https://create.roblox.com/docs/performance-optimization/microprofiler/use-microprofiler.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: performance-optimization / microprofiler / use-microprofiler

[Open](https://create.roblox.com/docs/performance-optimization/microprofiler/use-microprofiler.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Official Roblox docs walkthrough for the MicroProfiler: identifying a consistent per-frame performance cost on worker threads, drilling into the stack to a Raycast call in a LocalScript, adding debug.profilebegin/profileend labels to confirm, then removing the cause to restore frame rate.

## Tips
- [page](https://create.roblox.com/docs/performance-optimization/microprofiler/use-microprofiler) **[[optimization-and-streaming]]** Open the Performance Summary (Ctrl+Shift+F5) to check FPS, and the MicroProfiler (Ctrl+Alt+F6) to see whether frame times are consistent or spiking.
- [page](https://create.roblox.com/docs/performance-optimization/microprofiler/use-microprofiler) **[[optimization-and-streaming]]** Consistent-height frame bars mean a cost running every frame; occasional tall bars mean spikes. Diagnose them differently.
- [page](https://create.roblox.com/docs/performance-optimization/microprofiler/use-microprofiler) **[[optimization-and-streaming]]** Pause the MicroProfiler with Ctrl+P to enter detailed mode, then pan and hover stacked bars from top to bottom to find the root cause.
- [page](https://create.roblox.com/docs/performance-optimization/microprofiler/use-microprofiler) **[[testing-debugging-and-qa]]** Wrap suspect code in debug.profilebegin("Label") and debug.profileend() to create custom MicroProfiler labels and confirm it is the culprit.
- [page](https://create.roblox.com/docs/performance-optimization/microprofiler/use-microprofiler) **[[scripting-and-performance]]** Avoid casting large numbers of raycasts every frame in RunService.Stepped; 1,500 random rays per second caused a major frame rate drop in the example.
- [page](https://create.roblox.com/docs/performance-optimization/microprofiler/use-microprofiler) **[[optimization-and-streaming]]** After fixing, re-check the Performance Summary and MicroProfiler to verify frame rate improvement and reduced frame times.

## Numbers
- [page](https://create.roblox.com/docs/performance-optimization/microprofiler/use-microprofiler) Frame rate target: **60 FPS** (Example game ran below 60 FPS before fix)
- [page](https://create.roblox.com/docs/performance-optimization/microprofiler/use-microprofiler) Raycasts per second in problem code: **1500** (Random-direction raycasts in RunService.Stepped, the root cause in the example)

## Tools
MicroProfiler, Performance Summary overlay, Roblox Studio, debug.profilebegin / debug.profileend

## He points to
- Download the example game and open it via Open from File in Studio

## Topics
[[optimization-and-streaming]] [[scripting-and-performance]] [[testing-debugging-and-qa]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
