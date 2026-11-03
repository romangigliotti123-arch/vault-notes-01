---
title: "Master the TeleportService: Roblox Studio Scripting Tutorial"
url: https://youtu.be/o0S_8fFCsfA
creator: XTB7
official: false
advice_density: medium
date: 2023-10-30
views: 977
transcript: auto-captions
confidence: high
tags: [roblox, xtb7-dev, youtube-learn]
creator_trust: MIXED
creator_score: 7.3
---

> [!note] Trust: MIXED (credibility audit score 7.3): do not rely on this creator alone; confirm a recommendation with a second source. See [[creator-credibility]].

# Master the TeleportService: Roblox Studio Scripting Tutorial

[Watch](https://youtu.be/o0S_8fFCsfA) | xtb7-dev | 977 views | 2023-10-30

## Summary
Tutorial on Roblox TeleportService in Luau: TeleportAsync usage with TeleportOptions (ReservedServer, reserved server access codes, server instance IDs, mutually exclusive), client-side arrival handling via PlayerArrivedFromTeleport, teleport settings, GetPlayerPlaceInstanceAsync, and TeleportInitFailed. Wrap async calls in pcall.

## Tips
- [0:00](https://youtu.be/o0S_8fFCsfA?t=0) **[[matchmaking-and-teleport]]** Wrap every asynchronous call (TeleportAsync, ReserveServer, GetPlayerPlaceInstanceAsync) in pcall so failures are handled.
- [0:17](https://youtu.be/o0S_8fFCsfA?t=17) **[[matchmaking-and-teleport]]** Use TeleportAsync; older teleport functions are deprecated.
- [1:21](https://youtu.be/o0S_8fFCsfA?t=81) **[[matchmaking-and-teleport]]** Use a reserved server access code for matchmaking; the server is not joinable from outside, so friends cannot follow players in.
- [1:21](https://youtu.be/o0S_8fFCsfA?t=81) **[[matchmaking-and-teleport]]** Use a server instance (job) ID to let friends join each other's servers; the target server need not be reserved.
- [2:05](https://youtu.be/o0S_8fFCsfA?t=125) **[[matchmaking-and-teleport]]** Set only one of ShouldReserveServer, ReservedServerAccessCode, or ServerInstanceId in TeleportOptions; they are mutually exclusive or an error is thrown.
- [3:20](https://youtu.be/o0S_8fFCsfA?t=200) **[[matchmaking-and-teleport]]** Put the TeleportService PlayerArrivedFromTeleport handler in a script in ReplicatedFirst so it loads early and works reliably.
- [3:20](https://youtu.be/o0S_8fFCsfA?t=200) **[[matchmaking-and-teleport]]** Use TeleportService:GetArrivingTeleportGui() on the client to access the custom loading GUI set via TeleportGui.
- [4:31](https://youtu.be/o0S_8fFCsfA?t=271) **[[scripting-and-performance]]** Do not store sensitive data (e.g. currency) in teleport settings; they are client-accessible and can be manipulated by exploiters. Validate on the server.
- [5:24](https://youtu.be/o0S_8fFCsfA?t=324) **[[matchmaking-and-teleport]]** Use GetPlayerPlaceInstanceAsync(userId) to get a player's place ID and job ID, then pass the job ID as ServerInstanceId to let others join them.
- [5:46](https://youtu.be/o0S_8fFCsfA?t=346) **[[matchmaking-and-teleport]]** Handle teleport failures with pcall rather than the TeleportInitFailed event, which the speaker personally avoids.

## Numbers
- [2:47](https://youtu.be/o0S_8fFCsfA?t=167) Honeygain affiliate reward: **$5 (sponsored, promotional; not a game metric)**

## Tools
Roblox Studio, TeleportService

## Topics
[[matchmaking-and-teleport]] [[scripting-and-performance]]

Back to [[xtb7-dev - How to make successful Roblox games]]
