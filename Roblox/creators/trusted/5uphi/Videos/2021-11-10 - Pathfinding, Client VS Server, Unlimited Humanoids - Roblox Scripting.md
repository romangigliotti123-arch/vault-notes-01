---
title: "Pathfinding, Client VS Server, Unlimited Humanoids - Roblox Scripting Tutorial"
url: https://youtu.be/JyMxrcqEzu8
creator: Suphi Kaner
official: false
advice_density: medium
date: 2021-11-10
views: 73466
transcript: auto-captions
confidence: high
tags: [roblox, 5uphi, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.8
---

> [!note] Trust: TRUSTED (credibility audit score 8.8): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Pathfinding, Client VS Server, Unlimited Humanoids - Roblox Scripting Tutorial

[Watch](https://youtu.be/JyMxrcqEzu8) | 5uphi | 73,466 views | 2021-11-10

## Summary
Explains Roblox client-server model and network ownership, then builds a mostly client-side NPC system: server computes random wander targets and sends positions via attributes, clients clone and animate humanoid NPCs, cull by distance, and use PathfindingService with terrain-loaded checks.

## Tips
- [1:20](https://youtu.be/JyMxrcqEzu8?t=80) **[[client-server-and-remotes]]** Unanchored server parts are physics-owned by the nearest client, which sends positions back to the server; the server blindly accepts them.
- [3:56](https://youtu.be/JyMxrcqEzu8?t=236) **[[anti-exploit-and-security]]** Call SetNetworkOwner(nil) on unanchored NPC/physics parts so the server keeps ownership; otherwise exploiters can move them for all players.
- [4:39](https://youtu.be/JyMxrcqEzu8?t=279) **[[optimization-and-streaming]]** Moving server-replicated parts and NPCs is very laggy at scale (200 NPCs, 300 parts); run visual-only movement on the client to keep network usage near zero.
- [16:13](https://youtu.be/JyMxrcqEzu8?t=973) **[[3d-modeling-rigging-and-animation]]** Use the Build Rig plugin to generate a block rig, set Anchored false, and store the model in ReplicatedStorage keyed by folder name so clients know which model to clone.
- [21:12](https://youtu.be/JyMxrcqEzu8?t=1272) **[[building-art-and-assets]]** Copy Idle and Run animations from an existing character and load them via Animator; set Idle to Core-priority and Run to Movement priority.
- [25:58](https://youtu.be/JyMxrcqEzu8?t=1558) **[[optimization-and-streaming]]** Only move and animate NPCs within a set distance of the camera focus (test value 100 studs, final 500); park others in ReplicatedStorage.
- [28:48](https://youtu.be/JyMxrcqEzu8?t=1728) **[[optimization-and-streaming]]** Pass a waypoint list computed by PathfindingService into Humanoid:MoveTo one at a time, advancing on MoveTo Finished; teleport on failure.
- [29:57](https://youtu.be/JyMxrcqEzu8?t=1797) **[[scripting-and-performance]]** Set AgentRadius, AgentHeight, AgentCanJump and Costs (e.g. Water = 20) in CreatePath; enable the Pathfinding Modifiers beta feature to use Costs.
- [43:17](https://youtu.be/JyMxrcqEzu8?t=2597) **[[scripting-and-performance]]** Wrap ComputeAsync in pcall and check status == Success; otherwise fall back to teleporting the NPC to the target.
- [46:46](https://youtu.be/JyMxrcqEzu8?t=2806) **[[optimization-and-streaming]]** Check terrain is loaded at both the NPC's current and target positions before placing it in the world, to avoid spawning NPCs before terrain streams in.
- [12:48](https://youtu.be/JyMxrcqEzu8?t=768) **[[building-and-level-design]]** Define NPC wander zones as anchored parts; pick random offsets within part size and convert with CFrame:PointToWorldSpace.

## Numbers
- [4:39](https://youtu.be/JyMxrcqEzu8?t=279) NPC count in server vs client benchmark: **200 NPCs and 300 parts per script; server-run laggy, client-run smooth** (Demo comparing server-run and client-run movement)
- [25:58](https://youtu.be/JyMxrcqEzu8?t=1558) NPC display distance: **100 studs test, 500 studs final** (Distance from camera focus before NPC is shown and animated)
- [29:57](https://youtu.be/JyMxrcqEzu8?t=1797) Pathfinding agent settings: **AgentRadius 2, AgentHeight 5, WaypointSpacing 4, Water cost 20** (CreatePath configuration in video)
- [14:51](https://youtu.be/JyMxrcqEzu8?t=891) Server update interval: **5 seconds** (Wait between server position updates per folder)
- [2:34](https://youtu.be/JyMxrcqEzu8?t=154) Network ownership radius: **Starts small, grows as player stays in game** (Radius around character that grants ownership of unanchored parts)

## Tools
Roblox Studio, Build Rig plugin, PathfindingService, Animator, Luau, RunService, TweenService

## He points to
- Infinite terrain plugin (author's own, mentioned)

## Topics
[[3d-modeling-rigging-and-animation]] [[anti-exploit-and-security]] [[building-and-level-design]] [[building-art-and-assets]] [[client-server-and-remotes]] [[optimization-and-streaming]] [[scripting-and-performance]]

Back to [[5uphi - How to make successful Roblox games]]
