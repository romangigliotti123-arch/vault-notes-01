---
title: CritDEV - Studio & Scripting
creator: CritDEV
tags: [roblox, critdev, theme]
creator_trust: TRUSTED
creator_score: 7.8
---

> [!note] Trust: TRUSTED (credibility audit score 7.8): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# CritDEV: Studio & Scripting

All CritDEV tips on this theme, grouped by topic, oldest first. Cross-creator synthesis: see [[README]] in roblox-kb.

## [[scripting-and-performance]]
- 2025-10-07 [4:00](https://youtu.be/nEvM3aYY2pY?t=240) Build door traversal with two anchored, non-collidable parts on each side of the door, each with an Attachment, linked by a PathfindingLink. ([[2025-10-07 - Make NPCs Open DOORS in Roblox EASILY! 2025 (FREE TEST INCLUDED)|Make NPCs Open DOORS in Roblox EASILY! 2025 (FREE ]])
- 2025-10-07 [6:01](https://youtu.be/nEvM3aYY2pY?t=361) Return true from PathfindingLinkReached (or it stalls the Forbidden movement loop); fall back to a warning and return true so the AI can self-recover. ([[2025-10-07 - Make NPCs Open DOORS in Roblox EASILY! 2025 (FREE TEST INCLUDED)|Make NPCs Open DOORS in Roblox EASILY! 2025 (FREE ]])
- 2025-10-07 [7:26](https://youtu.be/nEvM3aYY2pY?t=446) Open the door by setting its open BoolValue to true; the door's own script detects the change, so no door logic needs editing. ([[2025-10-07 - Make NPCs Open DOORS in Roblox EASILY! 2025 (FREE TEST INCLUDED)|Make NPCs Open DOORS in Roblox EASILY! 2025 (FREE ]])
- 2025-10-07 [8:07](https://youtu.be/nEvM3aYY2pY?t=487) Use humanoid:MoveTo(waypoint.Position) and wait for MoveToFinished before finishing the link, so the NPC walks through the opened door. ([[2025-10-07 - Make NPCs Open DOORS in Roblox EASILY! 2025 (FREE TEST INCLUDED)|Make NPCs Open DOORS in Roblox EASILY! 2025 (FREE ]])
- 2025-10-07 [10:51](https://youtu.be/nEvM3aYY2pY?t=651) Set collision groups: doors don't collide with NPCs, and NPCs don't collide with each other, to prevent NPCs getting stuck and improve pathing performance. ([[2025-10-07 - Make NPCs Open DOORS in Roblox EASILY! 2025 (FREE TEST INCLUDED)|Make NPCs Open DOORS in Roblox EASILY! 2025 (FREE ]])

## [[code-architecture-and-frameworks]]
- 2025-08-18 [4:09](https://youtu.be/Om2vAKMW1Pw?t=249) Put each custom link handler in its own module script and dispatch from a single manager keyed by link label to keep the NPC script clean. ([[2025-08-18 - The ULTIMATE Guide to Pathfinding Links|The ULTIMATE Guide to Pathfinding Links]])

## [[physics-pathfinding-and-npc-ai]]
- 2025-07-25 [0:37](https://youtu.be/hqWLpWsWF00?t=37) Use a pathfinding module like Forbidden rather than raw PathfindingService; the raw API is hard and tracking moving targets needs custom code. ([[2025-07-25 - PATHFIND and TRACK PLAYERS with NPCs in 2026|PATHFIND and TRACK PLAYERS with NPCs in 2026]])
- 2025-07-25 [1:19](https://youtu.be/hqWLpWsWF00?t=79) Make sure the NPC has a Humanoid, a Head, and a HumanoidRootPart (or at least a PrimaryPart) so the module can drive it. ([[2025-07-25 - PATHFIND and TRACK PLAYERS with NPCs in 2026|PATHFIND and TRACK PLAYERS with NPCs in 2026]])
- 2025-07-25 [2:15](https://youtu.be/hqWLpWsWF00?t=135) Call restoreDefaults on the module config before changing settings, since config values persist between calls. ([[2025-07-25 - PATHFIND and TRACK PLAYERS with NPCs in 2026|PATHFIND and TRACK PLAYERS with NPCs in 2026]])
- 2025-07-25 [3:37](https://youtu.be/hqWLpWsWF00?t=217) Always insert the anti-lag script so the server keeps network ownership of NPC parts; without it parts stutter and explode near players. ([[2025-07-25 - PATHFIND and TRACK PLAYERS with NPCs in 2026|PATHFIND and TRACK PLAYERS with NPCs in 2026]])
- 2025-07-25 [4:21](https://youtu.be/hqWLpWsWF00?t=261) Tune the direct-move switch timer in config (e.g. 1 second instead of default) to make NPC chase feel more responsive. ([[2025-07-25 - PATHFIND and TRACK PLAYERS with NPCs in 2026|PATHFIND and TRACK PLAYERS with NPCs in 2026]])
- 2025-07-25 [5:49](https://youtu.be/hqWLpWsWF00?t=349) Run NPC pathfinding on the server; it is not suitable if the logic must run on the client because of ping and replication. ([[2025-07-25 - PATHFIND and TRACK PLAYERS with NPCs in 2026|PATHFIND and TRACK PLAYERS with NPCs in 2026]])
- 2025-07-25 [7:41](https://youtu.be/hqWLpWsWF00?t=461) Use config target offset (e.g. 3 studs) so the NPC stops at a distance from the player instead of colliding with them. ([[2025-07-25 - PATHFIND and TRACK PLAYERS with NPCs in 2026|PATHFIND and TRACK PLAYERS with NPCs in 2026]])
- 2025-08-18 [0:00](https://youtu.be/Om2vAKMW1Pw?t=0) Use PathfindingLinks when default pathing handles stairs poorly or when a route is otherwise unpathable (e.g. a wall you want NPCs to teleport over). ([[2025-08-18 - The ULTIMATE Guide to Pathfinding Links|The ULTIMATE Guide to Pathfinding Links]])
- 2025-08-18 [0:37](https://youtu.be/Om2vAKMW1Pw?t=37) Create a PathfindingLink with two attachments placed in two parts, enable Bidirectional unless one-way is intended, and set a Label to identify its behaviour. ([[2025-08-18 - The ULTIMATE Guide to Pathfinding Links|The ULTIMATE Guide to Pathfinding Links]])
- 2025-08-18 [2:11](https://youtu.be/Om2vAKMW1Pw?t=131) Assign the link-reached handler without parentheses (hooks.PathfindingLinkReached = fn) so the function is set, not called. ([[2025-08-18 - The ULTIMATE Guide to Pathfinding Links|The ULTIMATE Guide to Pathfinding Links]])
- 2025-08-18 [3:32](https://youtu.be/Om2vAKMW1Pw?t=212) Always return true from the PathfindingLinkReached handler after custom movement, otherwise pathfinding will not continue. ([[2025-08-18 - The ULTIMATE Guide to Pathfinding Links|The ULTIMATE Guide to Pathfinding Links]])
- 2025-08-18 [4:51](https://youtu.be/Om2vAKMW1Pw?t=291) Reset the NPC config to default before changing it, since it may have been altered elsewhere; enable visualization while debugging to see waypoints. ([[2025-08-18 - The ULTIMATE Guide to Pathfinding Links|The ULTIMATE Guide to Pathfinding Links]])
- 2025-10-07 [10:11](https://youtu.be/nEvM3aYY2pY?t=611) Expect NPCs to get stuck if a player closes a door on them; rely on Forbidden's unstuck logic and collision group setup to mitigate. ([[2025-10-07 - Make NPCs Open DOORS in Roblox EASILY! 2025 (FREE TEST INCLUDED)|Make NPCs Open DOORS in Roblox EASILY! 2025 (FREE ]])

## [[building-and-level-design]]
- 2025-10-07 [0:36](https://youtu.be/nEvM3aYY2pY?t=36) Name each door's folder to match the PathfindingLink label (e.g. 'door one') so the script can find the matching door model. ([[2025-10-07 - Make NPCs Open DOORS in Roblox EASILY! 2025 (FREE TEST INCLUDED)|Make NPCs Open DOORS in Roblox EASILY! 2025 (FREE ]])

Up: [[CritDEV - How to make successful Roblox games]]
