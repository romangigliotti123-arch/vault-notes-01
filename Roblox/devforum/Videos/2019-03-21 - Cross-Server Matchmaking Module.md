---
title: "Cross-Server Matchmaking Module"
url: https://devforum.roblox.com/t/cross-server-matchmaking-module/255142
creator: Roblox DevForum
official: false
advice_density: medium
date: 2019-03-21
views: 171
transcript: web-page
confidence: medium
tags: [roblox, roblox devforum, youtube-learn]
---

# Cross-Server Matchmaking Module

[Open](https://devforum.roblox.com/t/cross-server-matchmaking-module/255142) | Roblox DevForum | 171 views | 2019-03-21

## Summary
Open-source Luau matchmaking module demoing the new MessagingService for cross-server matchmaking. Uses a dedicated matchmaking host server, a queue, and a shared serversActive list; teleports matched players to a match place. Author warns it is untested across multiple servers and not for production.

## Tips
- [page](https://devforum.roblox.com/t/cross-server-matchmaking-module/255142) **[[common-mistakes]]** Do not use this module in production; author states it is untested with multiple servers and is a demo for the new MessagingService.
- [page](https://devforum.roblox.com/t/cross-server-matchmaking-module/255142) **[[matchmaking-and-teleport]]** Use a dedicated matchmaking host server that holds the queue; a re-host loses the queue, so notify players to rejoin.
- [page](https://devforum.roblox.com/t/cross-server-matchmaking-module/255142) **[[matchmaking-and-teleport]]** Avoid auto-queuing players; it sends many queue requests simultaneously. Manual queue requests are the recommended approach.
- [page](https://devforum.roblox.com/t/cross-server-matchmaking-module/255142) **[[data-persistence]]** Keep a serversActive list on all servers so any server can take over hosting if a re-host is needed.
- [page](https://devforum.roblox.com/t/cross-server-matchmaking-module/255142) **[[matchmaking-and-teleport]]** Set matchmakingServerId to the PlaceId of the match place; matchmaking conditions are configurable.
- [page](https://devforum.roblox.com/t/cross-server-matchmaking-module/255142) **[[testing-debugging-and-qa]]** Use a printStatus toggle to switch console logging on or off while debugging matchmaking flow.
- [page](https://devforum.roblox.com/t/cross-server-matchmaking-module/255142) **[[client-server-and-remotes]]** Require the module on the server to initialize it; the two remotes it creates are only needed on the client.

## Tools
MessagingService, TeleportService, DataStoreService, HttpService

## He points to
- MessagingService documentation (Roblox Creator Hub)
- TeleportService documentation (Roblox Creator Hub)
- DataStoreService documentation (Roblox Creator Hub)
- HttpService documentation (Roblox Creator Hub)

## Topics
[[client-server-and-remotes]] [[common-mistakes]] [[data-persistence]] [[matchmaking-and-teleport]] [[testing-debugging-and-qa]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
