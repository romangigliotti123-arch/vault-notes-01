---
title: "Docs: players / loading-screens"
url: https://create.roblox.com/docs/players/loading-screens.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: players / loading-screens

[Open](https://create.roblox.com/docs/players/loading-screens.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Official Roblox docs on custom loading screens for initial game join. Covers replacing the default loading screen via ReplicatedFirst:RemoveDefaultLoadingScreen(), building a ScreenGui in a LocalScript or referencing one in ReplicatedFirst, enforcing a minimum display time, and adding TweenService animations. Teleport loading screens are out of scope.

## Tips
- [page](https://create.roblox.com/docs/players/loading-screens) **[[first-session-onboarding]]** Put the loading screen ScreenGui in ReplicatedFirst so it replicates before anything else and is the first thing players see.
- [page](https://create.roblox.com/docs/players/loading-screens) **[[first-session-onboarding]]** Design the loading screen in StarterGui to preview it, then move it to ReplicatedFirst once satisfied.
- [page](https://create.roblox.com/docs/players/loading-screens) **[[ui-ux-design]]** Set IgnoreGuiInset = true on the loading ScreenGui so it fills the full screen.
- [page](https://create.roblox.com/docs/players/loading-screens) **[[ui-ux-design]]** Animate loading elements with TweenService (fade-in, looping rotation) to show that loading is progressing.
- [page](https://create.roblox.com/docs/players/loading-screens) **[[scripting-and-performance]]** Call ReplicatedFirst:RemoveDefaultLoadingScreen() before showing your custom screen, otherwise the default screen still appears.
- [page](https://create.roblox.com/docs/players/loading-screens) **[[scripting-and-performance]]** Wait for game.Loaded (if not game:IsLoaded()) before destroying the custom loading screen so it does not close before the game is ready.

## Numbers
- [page](https://create.roblox.com/docs/players/loading-screens) Minimum loading screen display time in sample code: **5 seconds (task.wait(5))**
- [page](https://create.roblox.com/docs/players/loading-screens) Sample ImageLabel loading ring size: **256x256 pixels**
- [page](https://create.roblox.com/docs/players/loading-screens) Sample tween rotation duration per loop: **4 seconds, linear, infinite repeat to 360 degrees**

## Tools
ReplicatedFirst, ScreenGui, LocalScript, TweenService, RemoveDefaultLoadingScreen

## He points to
- Teleport between places (Roblox docs)

## Topics
[[first-session-onboarding]] [[scripting-and-performance]] [[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
