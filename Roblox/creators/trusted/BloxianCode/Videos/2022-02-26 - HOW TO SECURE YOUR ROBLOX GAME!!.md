---
title: "HOW TO SECURE YOUR ROBLOX GAME!!"
url: https://youtu.be/SN7MyJFOQkU
creator: BloxianCode
official: false
advice_density: medium
date: 2022-02-26
views: 1777
transcript: auto-captions
confidence: medium
tags: [roblox, bloxiancode, youtube-learn]
creator_trust: TRUSTED
creator_score: 7.7
---

> [!note] Trust: TRUSTED (credibility audit score 7.7): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# HOW TO SECURE YOUR ROBLOX GAME!!

[Watch](https://youtu.be/SN7MyJFOQkU) | BloxianCode | 1,777 views | 2022-02-26

## Summary
Beginner security primer for Roblox games: client vs server split, RemoteEvents as the main exploit surface, validating on the server, and choosing between silently undoing exploits (passive) or kicking/banning exploiters (aggressive). Thin on specifics; no code shown.

## Tips
- [0:40](https://youtu.be/SN7MyJFOQkU?t=40) **[[anti-exploit-and-security]]** Assume every game can be hacked; aim to make exploiting hard enough to deter most people rather than promising perfect security.
- [0:47](https://youtu.be/SN7MyJFOQkU?t=47) **[[anti-exploit-and-security]]** Treat the client as untrusted: local scripts can be modified or bypassed, so never rely on client-side checks alone for gameplay-critical logic.
- [2:11](https://youtu.be/SN7MyJFOQkU?t=131) **[[client-server-and-remotes]]** Secure RemoteEvents on both client and server; RemoteEvents are the main way exploiters reach server code, so validate every incoming argument on the server.
- [2:45](https://youtu.be/SN7MyJFOQkU?t=165) **[[anti-exploit-and-security]]** Double-check critical actions like killing a player on both client and server, but make the server the authoritative check.
- [3:27](https://youtu.be/SN7MyJFOQkU?t=207) **[[anti-exploit-and-security]]** Choose a response policy: passive (silently undo the exploit's effect) or aggressive (kick or ban the exploiter); the speaker notes aggressive use needs a reliable way to undo bans.

## Games
- **Arsenal** [3:27](https://youtu.be/SN7MyJFOQkU?t=207): Kicks or bans players caught exploiting, an aggressive anti-cheat approach.
- **Meep City** [0:00](https://youtu.be/SN7MyJFOQkU?t=0): Cited as a well-known example of a big game that was hacked.

## He points to
- Roblox DevForum (source of the passive vs aggressive anti-cheat idea)

## Quotes
- [0:00](https://youtu.be/SN7MyJFOQkU?t=0) "everything on the internet can get hacked but although this is true we can still make it really hard to prevent our games to get hacked"
- [2:45](https://youtu.be/SN7MyJFOQkU?t=165) "client side is all not always safe and can be avoided by exploiters"

## Topics
[[anti-exploit-and-security]] [[client-server-and-remotes]]

Back to [[BloxianCode - How to make successful Roblox games]]
