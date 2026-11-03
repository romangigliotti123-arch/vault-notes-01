---
title: "PATHFIND and TRACK PLAYERS with NPCs in 2026"
url: https://youtu.be/hqWLpWsWF00
creator: Crit
official: false
advice_density: medium
date: 2025-07-25
views: 16136
transcript: auto-captions
confidence: medium
tags: [roblox, critdev, youtube-learn]
creator_trust: TRUSTED
creator_score: 7.8
---

> [!note] Trust: TRUSTED (credibility audit score 7.8): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# PATHFIND and TRACK PLAYERS with NPCs in 2026

[Watch](https://youtu.be/hqWLpWsWF00) | CritDEV | 16,136 views | 2025-07-25

## Summary
Walkthrough of Forbidden V2, a Roblox pathfinding/tracking module for NPCs. Covers inserting the module, setting up a test rig, config options (restore defaults, visualize, anti-lag network ownership, direct-move timers, target offsets), and a tracking-closest-player example. Mostly a tool tutorial with few business lessons.

## Tips
- [0:37](https://youtu.be/hqWLpWsWF00?t=37) **[[physics-pathfinding-and-npc-ai]]** Use a pathfinding module like Forbidden rather than raw PathfindingService; the raw API is hard and tracking moving targets needs custom code.
- [1:19](https://youtu.be/hqWLpWsWF00?t=79) **[[physics-pathfinding-and-npc-ai]]** Make sure the NPC has a Humanoid, a Head, and a HumanoidRootPart (or at least a PrimaryPart) so the module can drive it.
- [2:15](https://youtu.be/hqWLpWsWF00?t=135) **[[physics-pathfinding-and-npc-ai]]** Call restoreDefaults on the module config before changing settings, since config values persist between calls.
- [3:37](https://youtu.be/hqWLpWsWF00?t=217) **[[physics-pathfinding-and-npc-ai]]** Always insert the anti-lag script so the server keeps network ownership of NPC parts; without it parts stutter and explode near players.
- [4:21](https://youtu.be/hqWLpWsWF00?t=261) **[[physics-pathfinding-and-npc-ai]]** Tune the direct-move switch timer in config (e.g. 1 second instead of default) to make NPC chase feel more responsive.
- [5:49](https://youtu.be/hqWLpWsWF00?t=349) **[[physics-pathfinding-and-npc-ai]]** Run NPC pathfinding on the server; it is not suitable if the logic must run on the client because of ping and replication.
- [7:41](https://youtu.be/hqWLpWsWF00?t=461) **[[physics-pathfinding-and-npc-ai]]** Use config target offset (e.g. 3 studs) so the NPC stops at a distance from the player instead of colliding with them.

## Numbers
- [6:59](https://youtu.be/hqWLpWsWF00?t=419) Anti-lag effect: **Claimed about 10x smoother NPC movement with anti-lag enabled** (Speaker's own demonstration with network-ownership script)
- [0:00](https://youtu.be/hqWLpWsWF00?t=0) Video series size: **Around 20 videos on Forbidden V1 being remade as V2** (Speaker says the channel has about 20 prior videos)

## Tools
Forbidden V2 (pathfinding module), Roblox PathfindingService, Roblox Studio

## He points to
- Forbidden Discord server (link in video description)

## Quotes
- [0:00](https://youtu.be/hqWLpWsWF00?t=0) "The Roblox Pathfinding service API is way too hard to use. 99% of people are going to use it for two things."

## Topics
[[physics-pathfinding-and-npc-ai]]

Back to [[CritDEV - How to make successful Roblox games]]
