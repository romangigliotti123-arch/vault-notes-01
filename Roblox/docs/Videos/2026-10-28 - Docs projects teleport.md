---
title: "Docs: projects / teleport"
url: https://create.roblox.com/docs/projects/teleport.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: projects / teleport

[Open](https://create.roblox.com/docs/projects/teleport.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs on teleporting players between places using TeleportService: TeleportAsync usage, secure teleport access settings, migrating off client-side Teleport, custom teleport GUIs, TeleportOptions (servers, reserved/VIP servers, teleport data), and handling failed teleports with retries.

## Tips
- [page](https://create.roblox.com/docs/projects/teleport) **[[matchmaking-and-teleport]]** Call TeleportService:TeleportAsync() only from server scripts; client Teleport() is deprecated and should not be used for new work.
- [page](https://create.roblox.com/docs/projects/teleport) **[[anti-exploit-and-security]]** Set Access Control for Places to Secure Within Universe Only if progression gates areas or a test place must stay hidden; many games don't need secure teleports.
- [page](https://create.roblox.com/docs/projects/teleport) **[[matchmaking-and-teleport]]** Migrate legacy client teleports: move logic to server scripts via RemoteEvents, ProximityPrompts, ClickDetectors or Touched, then switch access control to Secure.
- [page](https://create.roblox.com/docs/projects/teleport) **[[data-persistence]]** Teleporting discards local player data; persist secure data like currency and inventory with DataStores or MemoryStores, not teleport data.
- [page](https://create.roblox.com/docs/projects/teleport) **[[anti-exploit-and-security]]** Never pass secure data via TeleportOptions:SetTeleportData(); it is visible to the client and unencrypted.
- [page](https://create.roblox.com/docs/projects/teleport) **[[matchmaking-and-teleport]]** Use HttpService:GenerateGUID(false) for ReservedServerId; the first teleport with a new ID creates the server, reusing the ID routes players to it.
- [page](https://create.roblox.com/docs/projects/teleport) **[[matchmaking-and-teleport]]** Wrap TeleportAsync in pcall and retry on failure, especially for reserved servers; handle TeleportInitFailed for teleports that fail after a successful call.
- [page](https://create.roblox.com/docs/projects/teleport) **[[matchmaking-and-teleport]]** Handle Enum.TeleportResult.Flooded with a ~15 second wait before retrying, and Failure with a short ~1 second retry delay; treat other results as invalid teleports.
- [page](https://create.roblox.com/docs/projects/teleport) **[[matchmaking-and-teleport]]** Without a specified server, TeleportAsync places users in a public server matched on the first user in the list's information.
- [page](https://create.roblox.com/docs/projects/teleport) **[[ui-ux-design]]** Use TeleportService:SetTeleportGui() on the client to replace the default loading screen; scripts inside the ScreenGui do not run.
- [page](https://create.roblox.com/docs/projects/teleport) **[[matchmaking-and-teleport]]** Teleport testing requires publishing the game and testing in the Roblox client; TeleportService does not work in Studio playtesting.
- [page](https://create.roblox.com/docs/projects/teleport) **[[matchmaking-and-teleport]]** Use Player:GetJoinData().TeleportData on arrival to read teleport data; use TeleportService:GetLocalPlayerTeleportData() for client-only access.

## Numbers
- [page](https://create.roblox.com/docs/projects/teleport) SafeTeleport attempt limit: **5 attempts, 1s retry delay** (Example retry wrapper in docs)
- [page](https://create.roblox.com/docs/projects/teleport) Flood delay: **15 seconds** (Wait before retrying after Enum.TeleportResult.Flooded in example)

## Tools
TeleportService, TeleportOptions, HttpService:GenerateGUID, Players:GetJoinData, ProximityPrompt, ClickDetector, DataStores, MemoryStores

## He points to
- Teleport to private servers (Roblox docs)
- Configure secure teleportation (Roblox docs)

## Topics
[[anti-exploit-and-security]] [[data-persistence]] [[matchmaking-and-teleport]] [[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
