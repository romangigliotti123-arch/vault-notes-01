---
title: "Creating an Intelligent Delivery Drone with Finite State Machines #1 - Roblox Studio"
url: https://youtu.be/jaitqSU2HIA
creator: B Ricey
official: false
advice_density: medium
date: 2023-04-14
views: 13447
transcript: auto-captions
confidence: high
tags: [roblox, bricey, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.0
---

> [!note] Trust: TRUSTED (credibility audit score 8.0): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Creating an Intelligent Delivery Drone with Finite State Machines #1 - Roblox Studio

[Watch](https://youtu.be/jaitqSU2HIA) | BRicey | 13,447 views | 2023-04-14

## Summary
Part 1 of a Roblox tutorial building an autonomous delivery drone using a finite state machine (FSM). Covers modelling states (returning, delivering, dropping, avoiding), AlignPosition movement with one attachment, a depot script that raycasts and spawns packages, and a state table driven by a current-state variable. Wall avoidance and dropping are deferred to part 2.

## Tips
- [0:43](https://youtu.be/jaitqSU2HIA?t=43) **[[common-mistakes]]** Don't scale AI behaviour with isolated if-statements; model behaviours as explicit states and transitions in a diagram first.
- [9:32](https://youtu.be/jaitqSU2HIA?t=572) **[[scripting-and-performance]]** Set AlignPosition MaxVelocity to a finite value (e.g. 10); default is Infinity, which flings attached objects off.
- [11:04](https://youtu.be/jaitqSU2HIA?t=664) **[[scripting-and-performance]]** Use a task.wait loop for infrequent spawn checks; for time-critical logic prefer RunService events instead.
- [18:45](https://youtu.be/jaitqSU2HIA?t=1125) **[[luau-language-and-types]]** Store state functions in a table and assign the function reference (no parentheses) to current_state; call it each tick as current_state().
- [24:30](https://youtu.be/jaitqSU2HIA?t=1470) **[[scripting-and-performance]]** Set the Model PrimaryPart before calling GetPivot, or GetPivot will error.
- [24:45](https://youtu.be/jaitqSU2HIA?t=1485) **[[building-and-level-design]]** Keep the pickup detection sphere smaller than the drone's flat surface, or the depot cannot drop parts onto it.
- [14:12](https://youtu.be/jaitqSU2HIA?t=852) **[[scripting-and-performance]]** Tag packages with an attribute (e.g. Target) rather than relying on names to identify them.

## Numbers
- [9:32](https://youtu.be/jaitqSU2HIA?t=572) AlignPosition MaxVelocity: **10 (default Infinity)** (Suggested cap to keep package from falling off the drone)
- [11:04](https://youtu.be/jaitqSU2HIA?t=664) Depot spawn loop interval: **3 seconds** (task.wait tick used by depot script to spawn packages)
- [17:24](https://youtu.be/jaitqSU2HIA?t=1044) Drone state loop interval: **0.5 seconds** (task.wait tick that runs current state; RunService suggested in real games)
- [11:45](https://youtu.be/jaitqSU2HIA?t=705) Raycast distance below drop point: **5 studs** (Downward raycast from drop point to detect drone underneath)
- [21:47](https://youtu.be/jaitqSU2HIA?t=1307) Package detection sphere radius: **1 stud** (GetPartBoundsInRadius around drone pivot to find tagged package)

## Tools
Roblox Studio, AlignPosition, AlignOrientation, Attachments, Luau tables, workspace:Raycast, GetPartBoundsInRadius

## He points to
- Creator's earlier video on AlignPosition
- Creator's video on Luau tables

## Topics
[[building-and-level-design]] [[common-mistakes]] [[luau-language-and-types]] [[scripting-and-performance]]

Back to [[BRicey - How to make successful Roblox games]]
