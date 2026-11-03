---
title: "Network ownership for beginners - How to handle physics on the client"
url: https://devforum.roblox.com/t/network-ownership-for-beginners-how-to-handle-physics-on-the-client/947029
creator: Roblox DevForum
official: false
advice_density: medium
date: 2020-12-27
views: 189
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Network ownership for beginners - How to handle physics on the client

[Open](https://devforum.roblox.com/t/network-ownership-for-beginners-how-to-handle-physics-on-the-client/947029) | Roblox DevForum | 189 views | 2020-12-27

## Summary
Explains network ownership in Roblox: the BasePart network owner handles physics and replicates movement to the server. Shows that client-side moves don't replicate by default, and that SetNetworkOwner(player) lets a client's movement replicate, offloading physics from the server. Uses a cannonball example and notes anchored parts can't have network ownership set.

## Tips
- [page](https://devforum.roblox.com/t/network-ownership-for-beginners-how-to-handle-physics-on-the-client/947029) **[[client-server-and-remotes]]** Set network ownership to a player with BasePart:SetNetworkOwner(player) so client-side moves replicate to the server. Only works on unanchored parts.
- [page](https://devforum.roblox.com/t/network-ownership-for-beginners-how-to-handle-physics-on-the-client/947029) **[[scripting-and-performance]]** Hand physics of many short-lived, frequently spawned parts (e.g. cannonballs) to the firing player so the server doesn't simulate every one, avoiding lag under spam.
- [page](https://devforum.roblox.com/t/network-ownership-for-beginners-how-to-handle-physics-on-the-client/947029) **[[client-server-and-remotes]]** Setting network owner on a part does not replicate client moves by default; a client-only move stays local and the server sees nothing unless ownership is assigned.
- [page](https://devforum.roblox.com/t/network-ownership-for-beginners-how-to-handle-physics-on-the-client/947029) **[[anti-exploit-and-security]]** Client-owned physics trusts the client; validate important results server-side when handing ownership to players.

## Tools
BasePart:SetNetworkOwner

## Topics
[[anti-exploit-and-security]] [[client-server-and-remotes]] [[scripting-and-performance]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
