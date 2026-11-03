---
title: "How to make a cross-server matchmaking system | Full Tutorial"
url: https://devforum.roblox.com/t/how-to-make-a-cross-server-matchmaking-system-full-tutorial/2707983
creator: Roblox DevForum
official: false
advice_density: medium
date: 2023-11-19
views: 77
transcript: web-page
confidence: medium
tags: [roblox, roblox devforum, youtube-learn]
---

# How to make a cross-server matchmaking system | Full Tutorial

[Open](https://devforum.roblox.com/t/how-to-make-a-cross-server-matchmaking-system-full-tutorial/2707983) | Roblox DevForum | 77 views | 2023-11-19

## Summary
Tutorial on building a cross-server matchmaking queue in Roblox using MemoryStoreService sorted maps for the queue, a DataStore-based host election per game mode, MessagingService to notify servers, and ReserveServer/TeleportToPrivateServer to move matched players into a private server.

## Tips
- [page](https://devforum.roblox.com/t/how-to-make-a-cross-server-matchmaking-system-full-tutorial/2707983) **[[matchmaking-and-teleport]]** Only one server should confirm queue matches; elect a host server per game mode via a DataStore key so 100 servers don't all try to teleport the same players.
- [page](https://devforum.roblox.com/t/how-to-make-a-cross-server-matchmaking-system-full-tutorial/2707983) **[[matchmaking-and-teleport]]** Use MemoryStoreService sorted maps for cross-server queues; read in Descending order so the oldest-queued players are matched first.
- [page](https://devforum.roblox.com/t/how-to-make-a-cross-server-matchmaking-system-full-tutorial/2707983) **[[matchmaking-and-teleport]]** Use MessagingService to tell other servers when host data changes and to send teleport instructions for players not in the host server.
- [page](https://devforum.roblox.com/t/how-to-make-a-cross-server-matchmaking-system-full-tutorial/2707983) **[[matchmaking-and-teleport]]** Use TeleportService:ReserveServer then TeleportToPrivateServer to move matched groups into a fresh server; check players are still in the game before teleporting.
- [page](https://devforum.roblox.com/t/how-to-make-a-cross-server-matchmaking-system-full-tutorial/2707983) **[[client-server-and-remotes]]** Fire the UI show/hide from server to client via RemoteEvent with a boolean, so the server controls queue state and can cancel the UI on error.
- [page](https://devforum.roblox.com/t/how-to-make-a-cross-server-matchmaking-system-full-tutorial/2707983) **[[common-mistakes]]** Don't call SetAsync on a shared key from many servers without care; the author suggests UpdateAsync for safer host-data writes.
- [page](https://devforum.roblox.com/t/how-to-make-a-cross-server-matchmaking-system-full-tutorial/2707983) **[[data-persistence]]** Initialize the host DataStore key once (SetAsync with an empty table) before the queue system reads it, or GetAsync will return nil.
- [page](https://devforum.roblox.com/t/how-to-make-a-cross-server-matchmaking-system-full-tutorial/2707983) **[[scripting-and-performance]]** Prevent duplicate queue entries by setting and checking a player attribute (e.g. IsInQueue) before adding them to the queue.
- [page](https://devforum.roblox.com/t/how-to-make-a-cross-server-matchmaking-system-full-tutorial/2707983) **[[matchmaking-and-teleport]]** Remove players from the MemoryStore queue on PlayerRemoving so departed players are not matched into a round.

## Numbers
- [page](https://devforum.roblox.com/t/how-to-make-a-cross-server-matchmaking-system-full-tutorial/2707983) Players per match: **5 (example numberofplayersperround in script)**
- [page](https://devforum.roblox.com/t/how-to-make-a-cross-server-matchmaking-system-full-tutorial/2707983) Servers in example: **100 servers would all attempt teleport without a host**

## Tools
MemoryStoreService, DataStoreService, MessagingService, TeleportService, RemoteEvent, BindableEvent, ProximityPrompt, ClickDetector

## He points to
- buymeacoffee.com (creator support link, omitted)

## Topics
[[client-server-and-remotes]] [[common-mistakes]] [[data-persistence]] [[matchmaking-and-teleport]] [[scripting-and-performance]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
