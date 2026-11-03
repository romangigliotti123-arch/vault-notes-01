---
id: "roblox-brain/roblox-npc-ai"
type: skill
category: "src-roblox-brain"
source: "roblox-brain"
license: "MIT"
repo_path: "sources/roblox-brain/skills/gameplay/roblox-npc-ai/SKILL.md"
description: "Use when creating or fixing Roblox NPCs, bots or enemies: pathfinding, state machines, line of sight, spawns, AI update loops."
orig_name: "roblox-npc-ai"
orig_when_to_use: "Also when NPCs get stuck, walk through walls, chase wrongly, lag the server, or bots need to fill empty servers."
orig_last_reviewed: "2026-10-14"
alternatives: ["roblox-skills-el4cteo: roblox-skills-el4cteo/roblox-npc-ai"]
tags: [lib/skill, cat/src-roblox-brain, src/roblox-brain]
---

# roblox-brain/roblox-npc-ai

> Use when creating or fixing Roblox NPCs, bots or enemies: pathfinding, state machines, line of sight, spawns, AI update loops.

Type: skill | Category: [[categories/cat-src-roblox-brain|src-roblox-brain]] | Source: [[sources/src-roblox-brain|roblox-brain]] | License: MIT
Repo file: `sources/roblox-brain/skills/gameplay/roblox-npc-ai/SKILL.md` (extra files, if any, sit beside it in the repo)

---
# Roblox NPC & AI

## When to Load

Load for NPCs/enemies: pathfinding, state machines, LOS/FOV detection, spawns, AI loops, or physics ownership.

## Quick Reference

### PathfindingService

```luau
local path = PathfindingService:CreatePath({
    AgentRadius = 2, AgentHeight = 5, AgentCanJump = true,
    Costs = { Water = 20, DangerZone = math.huge },
})
path:ComputeAsync(npcPos, targetPos)
if path.Status ~= Enum.PathStatus.Success then return end
for _, wp in path:GetWaypoints() do
    if wp.Action == Enum.PathWaypointAction.Jump then humanoid.Jump = true end
    humanoid:MoveTo(wp.Position)
    if not humanoid.MoveToFinished:Wait() then return end
end
```

- Recompute on blocked with a bounded retry or cancellation policy.
- In Studio, test `Workspace.PathfindingUseImprovedSearch` on representative maps before rollout; it is not scriptable.
- Avoid long requests and repeated recomputation. Moving collidable geometry can trigger navigation-mesh work.
- Region modifiers: anchored part + `PathfindingModifier` Label → Costs
- `PassThrough = true` for doors; `PathfindingLink` for disconnected navmesh
- `math.huge` cost = non-traversable

### State Machine

`idle → patrol → chase → attack → flee → dead`
- idle/patrol → chase (player detected) → attack (in range) → idle (lost)
- any → flee (health low) → idle (safe); any → dead (health ≤ 0)
- Transitions own movement changes, target cleanup, and cancellation

### Detection (distance → FOV → LOS)

1. **Distance** `(a-b).Magnitude`: cheapest, always first
2. **FOV** `forward:Dot(toTarget)` cosine; use a configured cone for your game, not a universal angle
3. **LOS** `workspace:Raycast`: expensive, last
- If the design includes hearing or proximity detection, make it a separate configured signal rather than a universal FOV bypass.

### Network Ownership
- Classic projects may use `SetNetworkOwner(nil)` for physics-sensitive NPCs, but it is not complete security. In Server Authority projects, configure the authority model instead of treating network ownership as the security boundary.

### Update Loop

- Throttle and stagger AI based on NPC count, path cost, and profiler evidence, not a universal tick rate. Keep NPC decisions and movement server-side; client code may handle presentation.

For spawners, lifecycle cleanup, timeout handling, and performance budgets, load `references/full.md`.

---

## Alternatives (same name, not shown in this vault)

This note is the best of 2 items called `roblox-npc-ai`. The others stay in the claude-library repo (open the repo file if this one does not fit):

- `roblox-skills-el4cteo`: roblox-skills-el4cteo/roblox-npc-ai - NPCs and enemy AI - PathfindingService (CreatePath, ComputeAsync, costs, modifiers, links, blocked paths), chase/follow loops, state machin... (repo file `sources/roblox-skills-el4cteo/skills/roblox-npc-ai/SKILL.md`)

