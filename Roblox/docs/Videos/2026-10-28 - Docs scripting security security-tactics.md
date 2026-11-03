---
title: "Docs: scripting / security / security-tactics"
url: https://create.roblox.com/docs/scripting/security/security-tactics.md
creator: Roblox Creator Docs
official: true
advice_density: high
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: scripting / security / security-tactics

[Open](https://create.roblox.com/docs/scripting/security/security-tactics.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox official security docs: core principles for building cheat-resistant games. Never trust the client; server is source of truth; distinguish server authority (engine feature for movement/physics); threat-model features early; keep logic in ServerScriptService; Device Trust API gives a trust level you act on.

## Tips
- [page](https://create.roblox.com/docs/scripting/security/security-tactics) **[[anti-exploit-and-security]]** Assume every client-sent value is manipulated. Validate all critical actions server-side, since client-side checks will eventually be bypassed by exploiters.
- [page](https://create.roblox.com/docs/scripting/security/security-tactics) **[[anti-exploit-and-security]]** Server should validate price, player money, and distance before approving a purchase, then subtract currency on the server itself.
- [page](https://create.roblox.com/docs/scripting/security/security-tactics) **[[client-server-and-remotes]]** Treat RemoteEvent/RemoteFunction arguments (besides the Player) as arbitrary. Validate types, ranges and call rate on the server.
- [page](https://create.roblox.com/docs/scripting/security/security-tactics) **[[anti-exploit-and-security]]** Keep logic and data in ServerScriptService from day one. Never put them in ReplicatedStorage or Workspace where exploiters can decompile them.
- [page](https://create.roblox.com/docs/scripting/security/security-tactics) **[[anti-exploit-and-security]]** Threat-model every feature: how it could be exploited, worst-case value, behavior at 1,000+ calls/sec, maximum sensible rate, and worst-case resource use.
- [page](https://create.roblox.com/docs/scripting/security/security-tactics) **[[anti-exploit-and-security]]** Expose the minimum internal state needed by a feature to the client.
- [page](https://create.roblox.com/docs/scripting/security/security-tactics) **[[client-server-and-remotes]]** Use engine server authority for competitive games (shooters, racing, sports, combat) so clients send only inputs and the server handles position and physics.
- [page](https://create.roblox.com/docs/scripting/security/security-tactics) **[[anti-exploit-and-security]]** Device Trust API is optional. Act on the trust level yourself (separate places, limit trading, or reject), and still validate server-side because trusted devices can exploit weak validation.
- [page](https://create.roblox.com/docs/scripting/security/security-tactics) **[[physics-pathfinding-and-npc-ai]]** Clients can take network ownership of their character and unanchored parts, so don't rely on client-reported physics or position for gameplay decisions.

## Numbers
- [page](https://create.roblox.com/docs/scripting/security/security-tactics) Feature stress threshold: **1,000+ calls per second** (Docs suggest testing features at this rate and defining a max rate)

## Games
- **Bloxy Cola (example item only)**: Used as a purchase example: server must verify true price, player money and distance before approving.

## Tools
Device Trust API

## He points to
- Network Ownership, Movement Validation, and Physics Exploits
- Access Control and Confidentiality

## Topics
[[anti-exploit-and-security]] [[client-server-and-remotes]] [[physics-pathfinding-and-npc-ai]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
