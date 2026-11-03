---
title: "How to add a FPS COUNTER to your Roblox game!"
url: https://youtu.be/zc7vWpLOejE
creator: BubuTheDev
official: false
advice_density: low
date: 2024-09-08
views: 192
transcript: auto-captions
confidence: medium
tags: [roblox, bubuthedev, youtube-learn]
creator_trust: TRUSTED
creator_score: 7.9
---

> [!note] Trust: TRUSTED (credibility audit score 7.9): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# How to add a FPS COUNTER to your Roblox game!

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Watch](https://youtu.be/zc7vWpLOejE) | BubuTheDev | 192 views | 2024-09-08

## Summary
Short tutorial on adding an FPS counter GUI label to a Roblox game using a LocalScript with RunService.RenderStepped-style per-frame counting, updated once per second. Demonstrates testing against the Roblox max frame rate setting.

## Tips
- [0:41](https://youtu.be/zc7vWpLOejE?t=41) **[[scripting-and-performance]]** Count frames in RunService.RenderStepped and update the label once per second (update rate = 1) instead of every frame to keep the readout stable and cheap.
- [2:05](https://youtu.be/zc7vWpLOejE?t=125) **[[optimization-and-streaming]]** Test FPS under different Roblox Settings > Maximum frame rate values (e.g. 120, 144) to verify the counter tracks the cap.
- [2:48](https://youtu.be/zc7vWpLOejE?t=168) **[[ui-ux-design]]** Place the FPS label in a screen corner (right-aligned, slightly down) so it does not block gameplay HUD.

## Numbers
- [1:23](https://youtu.be/zc7vWpLOejE?t=83) update interval: **1 second** (FPS label refresh rate in the tutorial script)
- [2:05](https://youtu.be/zc7vWpLOejE?t=125) example FPS readings: **~200-240 uncapped; 120 and 144 when capped** (Roblox max frame rate setting tests)

## Tools
Roblox Studio, LocalScript, RunService

## Topics
[[optimization-and-streaming]] [[scripting-and-performance]] [[ui-ux-design]]

Back to [[BubuTheDev - How to make successful Roblox games]]
