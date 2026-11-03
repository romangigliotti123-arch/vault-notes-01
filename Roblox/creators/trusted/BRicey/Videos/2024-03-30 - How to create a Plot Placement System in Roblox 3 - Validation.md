---
title: "How to create a Plot Placement System in Roblox #3 - Validation"
url: https://youtu.be/1XJRZ1x2x4g
creator: B Ricey
official: false
advice_density: medium
date: 2024-03-30
views: 9547
transcript: auto-captions
confidence: high
tags: [roblox, bricey, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.0
---

> [!note] Trust: TRUSTED (credibility audit score 8.0): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# How to create a Plot Placement System in Roblox #3 - Validation

[Watch](https://youtu.be/1XJRZ1x2x4g) | BRicey | 9,547 views | 2024-03-30

## Summary
Part 3 of a Roblox plot placement series. Builds a PlacementValidator module (shared in ReplicatedStorage) with a within-bounds check using a bounding-box corner algorithm in plot local space, plus a GetPartBoundsInBox overlap check. Client uses results for blue/red preview; server re-validates in the place method.

## Tips
- [0:26](https://youtu.be/1XJRZ1x2x4g?t=26) **[[core-loops-and-game-design]]** Validate placement with a bounding box: transform the object's four corner points into plot local space and check abs(x) and abs(z) against half plot size, instead of full mesh collision.
- [3:17](https://youtu.be/1XJRZ1x2x4g?t=197) **[[code-architecture-and-frameworks]]** Put pure validator functions in ReplicatedStorage so both client (preview feedback) and server (authoritative check) use the same logic.
- [10:32](https://youtu.be/1XJRZ1x2x4g?t=632) **[[ui-ux-design]]** Show a per-frame preview: tint the placement outline blue when valid and red when invalid so players know before placing.
- [14:20](https://youtu.be/1XJRZ1x2x4g?t=860) **[[scripting-and-performance]]** Use OverlapParams with an include filter on plot objects and workspace:GetPartBoundsInBox to detect collisions, ignoring players and debris.
- [19:51](https://youtu.be/1XJRZ1x2x4g?t=1191) **[[anti-exploit-and-security]]** Always re-run placement validation on the server; the client preview alone is not secure because exploiters can bypass it.
- [19:51](https://youtu.be/1XJRZ1x2x4g?t=1191) **[[code-architecture-and-frameworks]]** Use guard clauses with early returns in place methods to keep validation readable and avoid deep indentation.

## Tools
Roblox Studio, Luau, OverlapParams, workspace:GetPartBoundsInBox

## Topics
[[anti-exploit-and-security]] [[code-architecture-and-frameworks]] [[core-loops-and-game-design]] [[scripting-and-performance]] [[ui-ux-design]]

Back to [[BRicey - How to make successful Roblox games]]
