---
title: "Docs: resources / modules / spawn-with-friends"
url: https://create.roblox.com/docs/resources/modules/spawn-with-friends.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: resources / modules / spawn-with-friends

[Open](https://create.roblox.com/docs/resources/modules/spawn-with-friends.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page for the SpawnWithFriends developer module, which auto-spawns players near a friend already in the game, or teleports on command. Covers installation from the Creator Store, blocking restricted spawn areas with tagged invisible parts plus a validator, and the configure, teleportToRandomFriend and setTeleportationValidator APIs.

## Tips
- [page](https://create.roblox.com/docs/resources/modules/spawn-with-friends) **[[matchmaking-and-teleport]]** Install SpawnWithFriends from Creator Store Packages and move the model into ReplicatedStorage; it starts running automatically when the game runs.
- [page](https://create.roblox.com/docs/resources/modules/spawn-with-friends) **[[matchmaking-and-teleport]]** Fill restricted areas (VIP rooms, access-only spaces) with invisible anchored parts with CanCollide, CanTouch and CanQuery disabled, tagged RestrictedSpawnArea, so players don't spawn there.
- [page](https://create.roblox.com/docs/resources/modules/spawn-with-friends) **[[matchmaking-and-teleport]]** Use setTeleportationValidator to add custom pre-teleport checks, e.g. only teleport players on the same Team, by returning false to abort.
- [page](https://create.roblox.com/docs/resources/modules/spawn-with-friends) **[[matchmaking-and-teleport]]** Set teleportToFriendOnRespawn to false if friend teleports should happen only on demand via teleportToRandomFriend instead of on every respawn.
- [page](https://create.roblox.com/docs/resources/modules/spawn-with-friends) **[[matchmaking-and-teleport]]** Spawn-with-friends works better in games with large open spaces, since the module checks there is enough room before spawning to avoid placing characters inside geometry.
- [page](https://create.roblox.com/docs/resources/modules/spawn-with-friends) **[[matchmaking-and-teleport]]** Enable showLogs while debugging to see module log messages in the Output window; it is off by default.
- [page](https://create.roblox.com/docs/resources/modules/spawn-with-friends) **[[client-server-and-remotes]]** Call configure and setTeleportationValidator only from a server Script, since the docs restrict both to Script context.

## Numbers
- [page](https://create.roblox.com/docs/resources/modules/spawn-with-friends) teleportDistance: **5 studs (default spacing between players)**
- [page](https://create.roblox.com/docs/resources/modules/spawn-with-friends) maxCharacterVelocity: **48 (default; faster characters, e.g. in vehicles, are not candidates)**

## Tools
SpawnWithFriends module (Creator Store package), CollectionService

## He points to
- Creator Store Packages

## Topics
[[client-server-and-remotes]] [[matchmaking-and-teleport]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
