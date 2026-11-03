---
title: "Dragging objects with the mouse"
url: https://devforum.roblox.com/t/dragging-objects-with-the-mouse/403766
creator: Roblox DevForum
official: false
advice_density: medium
date: 2019-12-08
views: 831
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Dragging objects with the mouse

[Open](https://devforum.roblox.com/t/dragging-objects-with-the-mouse/403766) | Roblox DevForum | 831 views | 2019-12-08

## Summary
DevForum tutorial on dragging parts with the mouse in Roblox. Explains why naive mouse.Hit dragging sticks to the ground or vanishes in empty space, then uses vector math (subtraction, .Unit, scalar limit, addition) to clamp drag distance relative to the character's head. Recommends SetNetworkOwnership for smooth multiplayer dragging. Notes that Drag Detectors are now the easier solution.

## Tips
- [page](https://devforum.roblox.com/t/dragging-objects-with-the-mouse/403766) **[[client-server-and-remotes]]** Pass network ownership of dragged parts to the client with SetNetworkOwnership() to make dragging smooth and work in multiplayer.
- [page](https://devforum.roblox.com/t/dragging-objects-with-the-mouse/403766) **[[building-and-level-design]]** Clamp drag distance relative to the character's Head, not the camera, so zooming out doesn't send the part far away.
- [page](https://devforum.roblox.com/t/dragging-objects-with-the-mouse/403766) **[[combat-and-gameplay-systems]]** Use Drag Detectors instead of hand-rolled mouse dragging; they replicate automatically and give good control.
- [page](https://devforum.roblox.com/t/dragging-objects-with-the-mouse/403766) **[[scripting-and-performance]]** Set mouse.TargetFilter to the dragged target so mouse.Hit ignores it, and only move the part while Button1 is held.
- [page](https://devforum.roblox.com/t/dragging-objects-with-the-mouse/403766) **[[physics-pathfinding-and-npc-ai]]** Use AlignPosition rather than setting Position each frame for smoother physically-driven dragging.

## Numbers
- [page](https://devforum.roblox.com/t/dragging-objects-with-the-mouse/403766) mouse.Hit.Position.Magnitude when hovering empty space: **~9986 studs**
- [page](https://devforum.roblox.com/t/dragging-objects-with-the-mouse/403766) Example drag distance limit: **20 studs from head**

## Games
- **Lumber Tycoon**: Cited as the reference example of players dragging objects around with the mouse.

## Tools
Roblox Studio, mouse object (Mouse.Hit, Mouse.Target, TargetFilter), BasePart:SetNetworkOwnership(), AlignPosition, Drag Detectors

## He points to
- BenSBk advanced dragging system (uncopylocked)
- dragging.rbxl and even_better_dragging.rbxl example files by starmaq

## Topics
[[building-and-level-design]] [[client-server-and-remotes]] [[combat-and-gameplay-systems]] [[physics-pathfinding-and-npc-ai]] [[scripting-and-performance]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
