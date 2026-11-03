---
title: "Docs: physics / constraints / rope"
url: https://create.roblox.com/docs/physics/constraints/rope.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: physics / constraints / rope

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/physics/constraints/rope.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox engine docs for the RopeConstraint: a length-limited constraint between two attachments that can slacken, with restitution at the limit, and an optional winch mode driven by WinchTarget, WinchSpeed, WinchResponsiveness and WinchForce. Notes that negative WinchSpeed is clamped to 0, not reversed.

## Tips
- [page](https://create.roblox.com/docs/physics/constraints/rope) **[[physics-pathfinding-and-npc-ai]]** Use WinchSpeed as a positive value only; a negative value reverts to 0 rather than reversing the winch direction.
- [page](https://create.roblox.com/docs/physics/constraints/rope) **[[physics-pathfinding-and-npc-ai]]** To reel a rope in or out, enable WinchEnabled and set WinchTarget to the desired rope length in studs.
- [page](https://create.roblox.com/docs/physics/constraints/rope) **[[physics-pathfinding-and-npc-ai]]** RopeConstraint only limits maximum separation; attachments may move closer and rotate freely, so use it for slack-tolerant ropes.
- [page](https://create.roblox.com/docs/physics/constraints/rope) **[[physics-pathfinding-and-npc-ai]]** Tune Restitution to control bounce at the rope's length limit; it sets elasticity when the separation limit is reached.

## Tools
Roblox Studio RopeConstraint

## Topics
[[physics-pathfinding-and-npc-ai]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
