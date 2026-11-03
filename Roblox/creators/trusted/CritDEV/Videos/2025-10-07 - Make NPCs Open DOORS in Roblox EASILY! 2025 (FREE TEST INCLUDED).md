---
title: "Make NPCs Open DOORS in Roblox EASILY! 2025 (FREE TEST INCLUDED)"
url: https://youtu.be/nEvM3aYY2pY
creator: Crit
official: false
advice_density: medium
date: 2025-10-07
views: 2306
transcript: auto-captions
confidence: medium
tags: [roblox, critdev, youtube-learn]
creator_trust: TRUSTED
creator_score: 7.8
---

> [!note] Trust: TRUSTED (credibility audit score 7.8): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Make NPCs Open DOORS in Roblox EASILY! 2025 (FREE TEST INCLUDED)

[Watch](https://youtu.be/nEvM3aYY2pY) | CritDEV | 2,306 views | 2025-10-07

## Summary
Tutorial on making Roblox NPCs open doors using the free Forbidden pathfinding library. Covers setting up door folders, PathfindingLink parts with labels, overriding PathfindingLinkReached to open doors and move the NPC through, and using collision groups so NPCs don't block each other or doors.

## Tips
- [0:36](https://youtu.be/nEvM3aYY2pY?t=36) **[[building-and-level-design]]** Name each door's folder to match the PathfindingLink label (e.g. 'door one') so the script can find the matching door model.
- [4:00](https://youtu.be/nEvM3aYY2pY?t=240) **[[scripting-and-performance]]** Build door traversal with two anchored, non-collidable parts on each side of the door, each with an Attachment, linked by a PathfindingLink.
- [6:01](https://youtu.be/nEvM3aYY2pY?t=361) **[[scripting-and-performance]]** Return true from PathfindingLinkReached (or it stalls the Forbidden movement loop); fall back to a warning and return true so the AI can self-recover.
- [7:26](https://youtu.be/nEvM3aYY2pY?t=446) **[[scripting-and-performance]]** Open the door by setting its open BoolValue to true; the door's own script detects the change, so no door logic needs editing.
- [8:07](https://youtu.be/nEvM3aYY2pY?t=487) **[[scripting-and-performance]]** Use humanoid:MoveTo(waypoint.Position) and wait for MoveToFinished before finishing the link, so the NPC walks through the opened door.
- [10:51](https://youtu.be/nEvM3aYY2pY?t=651) **[[scripting-and-performance]]** Set collision groups: doors don't collide with NPCs, and NPCs don't collide with each other, to prevent NPCs getting stuck and improve pathing performance.
- [9:29](https://youtu.be/nEvM3aYY2pY?t=569) **[[testing-debugging-and-qa]]** Config.Tracking and a hardcoded player lookup are for testing only; remove before release.
- [10:11](https://youtu.be/nEvM3aYY2pY?t=611) **[[physics-pathfinding-and-npc-ai]]** Expect NPCs to get stuck if a player closes a door on them; rely on Forbidden's unstuck logic and collision group setup to mitigate.

## Numbers
- [1:17](https://youtu.be/nEvM3aYY2pY?t=77) Integration time: **~30 minutes** (Time to integrate a random marketplace door with Forbidden)

## Tools
Forbidden pathfinding library (Forbidden V2), Roblox PathfindingService / PathfindingLink, Collision Groups

## He points to
- Forbidden Discord (free models and library)

## Topics
[[building-and-level-design]] [[physics-pathfinding-and-npc-ai]] [[scripting-and-performance]] [[testing-debugging-and-qa]]

Back to [[CritDEV - How to make successful Roblox games]]
