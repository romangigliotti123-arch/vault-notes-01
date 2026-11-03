---
title: "Docs: physics / network-ownership"
url: https://create.roblox.com/docs/physics/network-ownership.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: physics / network-ownership

[Open](https://create.roblox.com/docs/physics/network-ownership.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs on network ownership: distributed physics where server or clients own unanchored BaseParts. Covers automatic proximity-based ownership, assembly rules, SetNetworkOwner for vehicles, ownership visualization, and exploit risks with client-owned parts and Touched events.

## Tips
- [page](https://create.roblox.com/docs/physics/network-ownership) **[[client-server-and-remotes]]** Anchored BaseParts are always server-owned and cannot be manually reassigned; plan physics mechanisms around unanchored parts only.
- [page](https://create.roblox.com/docs/physics/network-ownership) **[[physics-pathfinding-and-npc-ai]]** Set vehicle ownership to the driver via server-side SetNetworkOwner on VehicleSeat Occupant changes, and reset with SetNetworkOwnershipAuto when vacated, so driver input is not delayed by passengers.
- [page](https://create.roblox.com/docs/physics/network-ownership) **[[physics-pathfinding-and-npc-ai]]** Assign ownership of loose parts sitting on a vehicle to the same client that drives it, for smooth behaviour.
- [page](https://create.roblox.com/docs/physics/network-ownership) **[[physics-pathfinding-and-npc-ai]]** Use SetNetworkOwner(nil) for gameplay-critical server-controlled parts sparingly; overuse can cause jittery physics for clients.
- [page](https://create.roblox.com/docs/physics/network-ownership) **[[anti-exploit-and-security]]** Validate all physics-driven data from clients, since clients owning a part can teleport it, pass through walls or fly it.
- [page](https://create.roblox.com/docs/physics/network-ownership) **[[anti-exploit-and-security]]** Do not trust client-fired Touched events; a client can fire Touched on owned parts, so re-check hits server-side (e.g., sword damage across the map).
- [page](https://create.roblox.com/docs/physics/network-ownership) **[[optimization-and-streaming]]** Client-owned parts offload physics from the server; use network ownership to free server time for other tasks.
- [page](https://create.roblox.com/docs/physics/network-ownership) **[[testing-debugging-and-qa]]** Enable Network owners visualization in Studio's 3D viewport options during playtesting to see which client owns each part (green = yours, red = buffer zone, black = no physics).

## Numbers
- [page](https://create.roblox.com/docs/physics/network-ownership) ownership buffer zone color: **rgb(160,0,0) red indicates buffer zone where client simulates a part still owned by another**
- [page](https://create.roblox.com/docs/physics/network-ownership) ownership visualization colors: **green rgb(30,100,50) owned by you; white/grey rgb(220,220,220)/rgb(140,140,140) server or other; black rgb(0,0,0) unowned, no physics**

## Tools
Studio network owners visualization, BasePart:SetNetworkOwner(), BasePart:SetNetworkOwnershipAuto()

## He points to
- Security Tactics and Cheat Mitigation (Roblox docs)

## Topics
[[anti-exploit-and-security]] [[client-server-and-remotes]] [[optimization-and-streaming]] [[physics-pathfinding-and-npc-ai]] [[testing-debugging-and-qa]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
