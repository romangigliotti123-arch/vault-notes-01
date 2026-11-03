---
title: "Docs: projects / client-server"
url: https://create.roblox.com/docs/projects/client-server.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: projects / client-server

[Open](https://create.roblox.com/docs/projects/client-server.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on the client-server runtime model: server authority, edit-to-runtime data model copy, replication of data/physics/chat, client-to-server and server-to-client patterns, physics assembly ownership, and chat filtering. Includes latency simulation guidance for Studio testing.

## Tips
- [page](https://create.roblox.com/docs/projects/client-server) **[[client-server-and-remotes]]** Treat the server as the ultimate authority for game state; clients receive replicated copies and keep everything in sync through the server.
- [page](https://create.roblox.com/docs/projects/client-server) **[[client-server-and-remotes]]** Use Client to Server replication for player input, e.g. a key press to drink a potion, then have the server apply the effect to all players.
- [page](https://create.roblox.com/docs/projects/client-server) **[[client-server-and-remotes]]** Use Server to Client replication for player-specific data such as populating a joining player's inventory.
- [page](https://create.roblox.com/docs/projects/client-server) **[[optimization-and-streaming]]** With StreamingEnabled on, the server only sends content near each client initially; design scripts and assets with this partial loading in mind.
- [page](https://create.roblox.com/docs/projects/client-server) **[[client-server-and-remotes]]** Let the server filter chat messages (profanity, length) before replicating them to other clients.
- [page](https://create.roblox.com/docs/projects/client-server) **[[testing-debugging-and-qa]]** Studio playtests default to zero latency; enable Network Simulation with 50-150 ms inbound and outbound delay to approximate real player conditions.
- [page](https://create.roblox.com/docs/projects/client-server) **[[physics-pathfinding-and-npc-ai]]** Assemblies are simulated by one owner (client or server) and other clients receive position updates; ownership is usually automatic but can be set manually for responsiveness.
- [page](https://create.roblox.com/docs/projects/client-server) **[[optimization-and-streaming]]** Group parts into assemblies where possible, since the physics engine treats an assembly as one rigid body.

## Numbers
- [page](https://create.roblox.com/docs/projects/client-server) Typical player network latency: **100–300 ms** (Most players on Roblox game between these latencies)
- [page](https://create.roblox.com/docs/projects/client-server) Recommended simulated latency in Studio: **50–150 ms inbound and outbound** (Minimum delay for Network Simulation in Studio Settings)

## Tools
Roblox Studio, Studio Settings Network Simulation

## He points to
- Roblox Creator Docs: client-server runtime

## Topics
[[client-server-and-remotes]] [[optimization-and-streaming]] [[physics-pathfinding-and-npc-ai]] [[testing-debugging-and-qa]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
