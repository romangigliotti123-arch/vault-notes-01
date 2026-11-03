---
title: "Docs: physics / sleep-system"
url: https://create.roblox.com/docs/physics/sleep-system.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: physics / sleep-system

[Open](https://create.roblox.com/docs/physics/sleep-system.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox engine docs on the physics sleep system: assembly states (awake, sleeping, sleep-checking), velocity/acceleration thresholds, actuated joints that delay sleep, and the events that wake assemblies, plus a debug visualization toggle.

## Tips
- [page](https://create.roblox.com/docs/physics/sleep-system) **[[physics-pathfinding-and-npc-ai]]** If a slow-moving assembly falls asleep unexpectedly, it's usually moving below the sleep thresholds; wake it via impulses or constraint property changes.
- [page](https://create.roblox.com/docs/physics/sleep-system) **[[physics-pathfinding-and-npc-ai]]** Use actuated joints (Motor/Servo hinges, AlignPosition with RigidityEnabled=false, etc.) for slow controlled motion; they use a stricter sleep threshold so they don't fall asleep prematurely.
- [page](https://create.roblox.com/docs/physics/sleep-system) **[[optimization-and-streaming]]** Large mechanisms with many assemblies and constraints are costly to simulate; the sleep system skips non-moving assemblies, so keep static parts anchored or let them settle.
- [page](https://create.roblox.com/docs/physics/sleep-system) **[[optimization-and-streaming]]** Use Workspace 'Awake parts' visualization during playtesting to see which assemblies are awake (red), sleep-checking (orange), or sleeping (un-outlined).
- [page](https://create.roblox.com/docs/physics/sleep-system) **[[physics-pathfinding-and-npc-ai]]** Changing BasePart physics properties (Anchored, CanCollide, velocities, Massless, etc.), applying impulses, or changing Workspace Gravity/wind wakes the whole assembly.
- [page](https://create.roblox.com/docs/physics/sleep-system) **[[physics-pathfinding-and-npc-ai]]** Larger assemblies rotate at lower angular velocity before falling asleep, because rotational velocity scales with the bounding sphere radius.

## Numbers
- [page](https://create.roblox.com/docs/physics/sleep-system) Linear velocity sleep threshold: **0.33 studs/s** (Awake to sleeping when below this and rotational velocity is also below threshold)
- [page](https://create.roblox.com/docs/physics/sleep-system) Rotational velocity sleep threshold: **0.42 studs/s** (Awake to sleeping threshold for rotational velocity)
- [page](https://create.roblox.com/docs/physics/sleep-system) Linear acceleration sleep threshold: **0.24 studs/s²** (Above this, assembly is considered accelerating and won't sleep)
- [page](https://create.roblox.com/docs/physics/sleep-system) Rotational acceleration sleep threshold: **0.24 studs/s²** (Above this, assembly is considered accelerating and won't sleep)
- [page](https://create.roblox.com/docs/physics/sleep-system) Neighbor linear velocity wake threshold: **0.48 studs/s** (Sleep-checking assembly wakes if neighbor exceeds this)
- [page](https://create.roblox.com/docs/physics/sleep-system) Neighbor rotational velocity wake threshold: **0.59 studs/s** (Sleep-checking assembly wakes if neighbor exceeds this)
- [page](https://create.roblox.com/docs/physics/sleep-system) Wake linear acceleration threshold: **16.9 studs/s²** (Sleep-checking assembly wakes above this linear acceleration)
- [page](https://create.roblox.com/docs/physics/sleep-system) Wake rotational acceleration threshold: **16.9 studs/s²** (Sleep-checking assembly wakes above this rotational acceleration)
- [page](https://create.roblox.com/docs/physics/sleep-system) Collision wake speed: **1 studs/s** (Assembly wakes when colliding with an assembly moving faster than this)

## Tools
Roblox Studio Visualization Options (Awake parts)

## He points to
- Roblox docs: Sleep system

## Topics
[[optimization-and-streaming]] [[physics-pathfinding-and-npc-ai]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
