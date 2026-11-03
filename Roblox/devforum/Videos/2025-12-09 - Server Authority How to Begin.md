---
title: "Server Authority: How to Begin?"
url: https://devforum.roblox.com/t/server-authority-how-to-begin/4139185
creator: Roblox DevForum
official: false
advice_density: medium
date: 2025-12-09
views: 152
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Server Authority: How to Begin?

[Open](https://devforum.roblox.com/t/server-authority-how-to-begin/4139185) | Roblox DevForum | 152 views | 2025-12-09

## Summary
Beginner tutorial on Roblox Server Authority (AuthorityMode) and Rollback Netcode: why clients lose network ownership, how prediction/misprediction/rollback work, and how to start with InputActions, RunService:BindToSimulation, SetPredictionMode, and a shared ModuleScript simulation architecture.

## Tips
- [page](https://devforum.roblox.com/t/server-authority-how-to-begin/4139185) **[[client-server-and-remotes]]** Enable Server Authority via Workspace > Server Authority > AuthorityMode = Server; this disables certain other workspace properties automatically.
- [page](https://devforum.roblox.com/t/server-authority-how-to-begin/4139185) **[[client-server-and-remotes]]** With Server Authority, clients no longer own instances; only their inputs are trusted. Keep replicated client data to a minimum.
- [page](https://devforum.roblox.com/t/server-authority-how-to-begin/4139185) **[[anti-exploit-and-security]]** Use InputActions for all inputs affecting core simulation; validate them server-side and enforce min/max ranges on numbers, as with remotes.
- [page](https://devforum.roblox.com/t/server-authority-how-to-begin/4139185) **[[client-server-and-remotes]]** Put core game logic in RunService:BindToSimulation so it runs on both client and server, including during rollback.
- [page](https://devforum.roblox.com/t/server-authority-how-to-begin/4139185) **[[client-server-and-remotes]]** Place shared simulation code in a ModuleScript in ReplicatedStorage, required and run by both server and client scripts.
- [page](https://devforum.roblox.com/t/server-authority-how-to-begin/4139185) **[[optimization-and-streaming]]** Use SetPredictionMode On only for critical instances; overuse hurts low-end devices. Automatic (default) is suitable for most BaseParts.
- [page](https://devforum.roblox.com/t/server-authority-how-to-begin/4139185) **[[optimization-and-streaming]]** Use SetPredictionMode Off for instances that don't need client prediction; they are then server-owned with no client prediction.
- [page](https://devforum.roblox.com/t/server-authority-how-to-begin/4139185) **[[physics-pathfinding-and-npc-ai]]** Use RunService:GetPredictionStatus to debug which vehicle/physics instances are predicted when some are and some aren't.
- [page](https://devforum.roblox.com/t/server-authority-how-to-begin/4139185) **[[common-mistakes]]** Don't expect zero mispredictions; design so corrections are small and imperceptible, since mispredictions are normal.

## Numbers
- [page](https://devforum.roblox.com/t/server-authority-how-to-begin/4139185) Frame rate for example simulation: **60Hz (default BindToSimulation frequency)**
- [page](https://devforum.roblox.com/t/server-authority-how-to-begin/4139185) Example latency to frames ahead: **100ms latency ≈ 6 frames at 60Hz (16.67ms/frame)**

## Tools
RunService:BindToSimulation, RunService:SetPredictionMode, RunService:GetPredictionStatus, Input Action System (IAS)

## He points to
- Roblox Server Authority Best Practices community tutorial (TenebrisNoctua)
- Roblox documentation on Input Action System
- Articles on Rollback Netcode concepts

## Topics
[[anti-exploit-and-security]] [[client-server-and-remotes]] [[common-mistakes]] [[optimization-and-streaming]] [[physics-pathfinding-and-npc-ai]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
