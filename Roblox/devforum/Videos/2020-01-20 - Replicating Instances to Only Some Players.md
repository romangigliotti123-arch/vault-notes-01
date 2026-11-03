---
title: "Replicating Instances to Only Some Players"
url: https://devforum.roblox.com/t/replicating-instances-to-only-some-players/438374
creator: Roblox DevForum
official: false
advice_density: medium
date: 2020-01-20
views: 83
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Replicating Instances to Only Some Players

[Open](https://devforum.roblox.com/t/replicating-instances-to-only-some-players/438374) | Roblox DevForum | 83 views | 2020-01-20

## Summary
Technique for replicating a Model to only one specific player: the server parents clones into a ScreenGui in that player's PlayerGui (which doesn't replicate to other players), the client waits until all descendants arrive, clones it, acks via RemoteEvent, and the server destroys its clone. Includes a ChunkSender/ChunkReceiver module architecture. Aimed at memory savings on mobile.

## Tips
- [page](https://devforum.roblox.com/t/replicating-instances-to-only-some-players/438374) **[[scripting-and-performance]]** Replicate instances to only the players who need them (e.g. a player's interior) instead of ReplicatedStorage, to save bandwidth, CPU and memory, especially on mobile.
- [page](https://devforum.roblox.com/t/replicating-instances-to-only-some-players/438374) **[[client-server-and-remotes]]** Use a ScreenGui in Player.PlayerGui with ResetOnSpawn = false as a per-player replication target; it replicates only to that player. Other Instance types get destroyed on death.
- [page](https://devforum.roblox.com/t/replicating-instances-to-only-some-players/438374) **[[client-server-and-remotes]]** Name the replicated Model with its expected descendant count; the client waits on DescendantAdded until that many descendants have arrived before using it.
- [page](https://devforum.roblox.com/t/replicating-instances-to-only-some-players/438374) **[[client-server-and-remotes]]** Have the client fire a RemoteEvent back to the server once a replicated chunk is fully loaded, since replication completion is not guaranteed when the instance appears.
- [page](https://devforum.roblox.com/t/replicating-instances-to-only-some-players/438374) **[[client-server-and-remotes]]** Connect ChildAdded listeners before replications can arrive, and also process existing children via GetChildren(), since ChildAdded misses children added earlier.
- [page](https://devforum.roblox.com/t/replicating-instances-to-only-some-players/438374) **[[anti-exploit-and-security]]** Validate remote inputs on the server (typeof check for Instance) and only accept completion callbacks for objects the server actually sent to that player.
- [page](https://devforum.roblox.com/t/replicating-instances-to-only-some-players/438374) **[[data-persistence]]** Clear per-player pending replication data on PlayerRemoving to free references for garbage collection.
- [page](https://devforum.roblox.com/t/replicating-instances-to-only-some-players/438374) **[[scripting-and-performance]]** Store instances as table keys to prevent garbage collection while they are held in a pending state, rather than parenting them early.
- [page](https://devforum.roblox.com/t/replicating-instances-to-only-some-players/438374) **[[common-mistakes]]** Don't use StreamingEnabled as a first resort for per-player content; advanced developers who know their game's mechanics can optimise better than its general-purpose defaults.
- [page](https://devforum.roblox.com/t/replicating-instances-to-only-some-players/438374) **[[building-and-level-design]]** For smooth terrain, use Terrain:ReadVoxels and WriteVoxels; the Instance replication technique does not apply to terrain.
- [page](https://devforum.roblox.com/t/replicating-instances-to-only-some-players/438374) **[[client-server-and-remotes]]** Do not rely on reparenting a replicated instance on the client to unload it on the server; destroy the server-side object instead, and clone client-side so the server-owned copy is not moved.

## Tools
RemoteEvent, ScreenGui, ModuleScript, PlayerGui

## He points to
- Replicate items to individual client (DevForum feature request by @Crazyman32)

## Topics
[[anti-exploit-and-security]] [[building-and-level-design]] [[client-server-and-remotes]] [[common-mistakes]] [[data-persistence]] [[scripting-and-performance]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
