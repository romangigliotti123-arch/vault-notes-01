---
name: roblox-npc-pathfinding
description: "Implement Roblox NPCs and enemies with PathfindingService, state machines, network ownership and cheap perception. Use when building enemies, pets, shopkeepers or any moving AI character in Roblox."
---

# Roblox NPC and pathfinding

Code comments: none by default (see roblox-luau-style, Comments).

1. Model: Humanoid-based rig (R15/R6) or a custom anchored mover. For many NPCs prefer a lightweight mover; Humanoids are costly in numbers.
2. Server owns the NPC. Call `rootPart:SetNetworkOwner(nil)` so a nearby player's client does not drive it (and exploiters cannot).
3. State machine: Idle -> Patrol -> Chase -> Attack -> Return (and Dead). One module per behaviour, one `Heartbeat`-free update loop per NPC using `task.wait(0.1-0.25)`; stagger NPC ticks so they do not all run on the same frame.
4. Perception: distance check first (cheap), then angle, then a raycast for line of sight with `RaycastParams` filtering the NPC itself. Use `workspace:GetPartBoundsInRadius` sparingly; or CollectionService tag for targets.
5. Pathfinding: `PathfindingService:CreatePath({AgentRadius, AgentHeight, AgentCanJump, WaypointSpacing, Costs})`; `path:ComputeAsync(from, to)` inside pcall; follow waypoints with `Humanoid:MoveTo` and `MoveToFinished`, handle `Waypoint.Action == Jump`; recompute when the target moves more than a threshold or the path blocks (`path.Blocked`). Add a stuck timer (no progress in 2 s -> repath or teleport back).
6. Combat: attack damage computed on the server; cooldowns; hit validation by distance; no instant-kill from outside range; fair telegraphs.
7. Spawning: cap active NPCs per server, despawn far from players, pool instances, respawn timers, and clean up connections on death.
8. Test: stuck cases (stairs, thin walls, moving platforms), 20+ NPCs frame time in MicroProfiler, player leaves while chased, NPC falls off the map.
