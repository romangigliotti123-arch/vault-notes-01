---
title: "Dungeon Generation: A Procedural Generation Guide"
url: https://devforum.roblox.com/t/dungeon-generation-a-procedural-generation-guide/342413
creator: Roblox DevForum
official: false
advice_density: medium
date: 2019-09-01
views: 417
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Dungeon Generation: A Procedural Generation Guide

[Open](https://devforum.roblox.com/t/dungeon-generation-a-procedural-generation-guide/342413) | Roblox DevForum | 417 views | 2019-09-01

## Summary
Official-style DevForum/docs guide by iiau (Nyapaw) on procedural 2D dungeon generation in Luau. Covers top-down algorithm design, OOP Cell/Maze/Room/House classes, room placement by brute force, Recursive Backtracker maze fill, door carving, flood-fill pathfinding to connect rooms, and pruning dead cells. Code on GitHub.

## Tips
- [page](https://devforum.roblox.com/t/dungeon-generation-a-procedural-generation-guide/342413) **[[game-ideas-and-genres]]** Design the algorithm top-down on paper before scripting; an algorithm you can't explain can't be implemented. Aim for implementable, understandable, trustable.
- [page](https://devforum.roblox.com/t/dungeon-generation-a-procedural-generation-guide/342413) **[[code-architecture-and-frameworks]]** Split procedural generation into OOP classes (Cell, Maze, Room, House, Dungeon) with a Settings module holding tunable constants.
- [page](https://devforum.roblox.com/t/dungeon-generation-a-procedural-generation-guide/342413) **[[building-and-level-design]]** Use Recursive Backtracker rather than Hunt and Kill for filling maze space; Hunt and Kill can leave blocked-off unreachable areas around rooms.
- [page](https://devforum.roblox.com/t/dungeon-generation-a-procedural-generation-guide/342413) **[[building-and-level-design]]** Require at least 2 rooms before placing doors; set a minimum spacing (ROOM_BORDER_LENIANCY) between rooms and cap brute-force attempts (MAX_ROOM_TRIES).
- [page](https://devforum.roblox.com/t/dungeon-generation-a-procedural-generation-guide/342413) **[[building-and-level-design]]** Connect rooms with a flood fill from each door to the nearest door of another room; close off doors that fail to find a path.
- [page](https://devforum.roblox.com/t/dungeon-generation-a-procedural-generation-guide/342413) **[[building-and-level-design]]** After pathing, remove non-path, non-room cells and rebuild walls only between them and adjacent path cells; reuse tables instead of creating new ones to save memory.

## Numbers
- [page](https://devforum.roblox.com/t/dungeon-generation-a-procedural-generation-guide/342413) Settings defaults: **MAX_ROOM_TRIES 300, MAX_ROOMS 3, room size 3x3 to 8x8** (Example constants from the Settings module in the guide)
- [page](https://devforum.roblox.com/t/dungeon-generation-a-procedural-generation-guide/342413) Border retries: **ROOM_BORDER_RETRIES 10, ROOM_BORDER_LENIANCY 3** (Retries for room openings; minimum spacing between rooms)
- [page](https://devforum.roblox.com/t/dungeon-generation-a-procedural-generation-guide/342413) Doorways per room: **2** (Brute-force door count per room in the example; adjustable in loop)
- [page](https://devforum.roblox.com/t/dungeon-generation-a-procedural-generation-guide/342413) Stress test size: **6400 cells** (Bonus massive dungeon shown at end of guide)

## Tools
Luau, GitHub (Nyapaw/Roblox repo), Roblox Studio

## He points to
- github.com/Nyapaw/Roblox
- RDC 2019 keynote on procedural generation (Crazyman32)
- DevForum: All about OOP community tutorial (2014)

## Topics
[[building-and-level-design]] [[code-architecture-and-frameworks]] [[game-ideas-and-genres]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
