---
title: "Roblox Devs, stop misusing :WaitForChild()!"
url: https://youtu.be/7tzy1DuPcBQ
creator: Crusherfire
official: false
advice_density: medium
date: 2024-01-18
views: 178440
transcript: auto-captions
confidence: high
tags: [roblox, crusherfiredev, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.7
---

> [!note] Trust: TRUSTED (credibility audit score 8.7): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Roblox Devs, stop misusing :WaitForChild()!

[Watch](https://youtu.be/7tzy1DuPcBQ) | crusherfiredev | 178,440 views | 2024-01-18

## Summary
Technical Roblox Luau lesson on when WaitForChild is needed. Explains replication, that local script containers (StarterPlayerScripts, StarterGui, StarterPack) already hold replicated content after game.Loaded, and that WaitForChild is only required for runtime-created instances, descendants of workspace models when StreamingEnabled is on, and LocalScripts in ReplicatedFirst accessing outside instances.

## Tips
- [0:41](https://youtu.be/7tzy1DuPcBQ?t=41) **[[scripting-and-performance]]** Don't use WaitForChild on server scripts; you almost never need it there.
- [4:25](https://youtu.be/7tzy1DuPcBQ?t=265) **[[client-server-and-remotes]]** Local scripts in StarterPlayerScripts, StarterGui and StarterPack can directly index ReplicatedStorage and similar instances; the containers only run their scripts after game.Loaded.
- [5:47](https://youtu.be/7tzy1DuPcBQ?t=347) **[[client-server-and-remotes]]** Use WaitForChild for instances created at runtime by the server (e.g. cloned models) and for workspace descendants when StreamingEnabled is on.
- [6:29](https://youtu.be/7tzy1DuPcBQ?t=389) **[[scripting-and-performance]]** Don't write GUI:WaitForChild('Frame') for children of a ScreenGui in StarterGui; index them directly.
- [8:09](https://youtu.be/7tzy1DuPcBQ?t=489) **[[client-server-and-remotes]]** LocalScripts in ReplicatedFirst run before game is loaded; use WaitForChild for anything outside ReplicatedFirst.
- [12:15](https://youtu.be/7tzy1DuPcBQ?t=735) **[[scripting-and-performance]]** Remove 'if not game:IsLoaded() then game.Loaded:Wait()' checks at the top of LocalScripts in StarterPlayerScripts/StarterGui; they are unnecessary.
- [12:55](https://youtu.be/7tzy1DuPcBQ?t=775) **[[client-server-and-remotes]]** Always WaitForChild descendants of a model or part that the server replicates at runtime, since they may not have arrived yet.

## Numbers
- [14:08](https://youtu.be/7tzy1DuPcBQ?t=848) Server wait before cloning test model: **10 seconds**

## Tools
Roblox Studio, View > Network panel (Studio)

## Quotes
- [10:54](https://youtu.be/7tzy1DuPcBQ?t=654) "Only time you need to use WaitForChild is for instances in ReplicatedFirst local scripts or instances created during runtime."

## Topics
[[client-server-and-remotes]] [[scripting-and-performance]]

Back to [[crusherfiredev - How to make successful Roblox games]]
