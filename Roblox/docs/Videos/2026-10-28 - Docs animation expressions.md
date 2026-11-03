---
title: "Docs: animation / expressions"
url: https://create.roblox.com/docs/animation/expressions.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: animation / expressions

[Open](https://create.roblox.com/docs/animation/expressions.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Docs page on Animation Graph Editor expressions: short Luau-like formulas that read graph parameters and drive node properties or state machine transitions. Covers a Blend1DNode speed-blend example, the supported syntax (arithmetic, logic, if-then-else, math library, vector, CFrame, Color3, string concat), unsupported functions, and multi-line local-variable expressions.

## Tips
- [page](https://create.roblox.com/docs/animation/expressions) **[[3d-modeling-rigging-and-animation]]** Normalise movement speed into 0-1 with math.clamp(MovementSpeed / MaxSpeed, 0, 1) before feeding a Blend1DNode so it blends idle to run cleanly.
- [page](https://create.roblox.com/docs/animation/expressions) **[[3d-modeling-rigging-and-animation]]** Keep parameter transformations inside the graph as expressions, close to the nodes they drive, rather than scattering the math across gameplay scripts.
- [page](https://create.roblox.com/docs/animation/expressions) **[[3d-modeling-rigging-and-animation]]** Push parameters from gameplay code each frame with AnimationTrack:SetParameter (e.g. inside RunService.Stepped); expressions re-evaluate as values change.
- [page](https://create.roblox.com/docs/animation/expressions) **[[3d-modeling-rigging-and-animation]]** Click outside the expression box after editing to refresh and apply it in the Graph Editor.
- [page](https://create.roblox.com/docs/animation/expressions) **[[3d-modeling-rigging-and-animation]]** Break complex formulas into multi-line expressions with local variables and return to keep named, readable steps.
- [page](https://create.roblox.com/docs/animation/expressions) **[[common-mistakes]]** Remember Luau truthiness in and/or: only false and nil are falsy, so 0 and empty strings count as true in conditions like IsGrounded and GroundSpeed or AirSpeed.
- [page](https://create.roblox.com/docs/animation/expressions) **[[3d-modeling-rigging-and-animation]]** Do not rely on Library.math.frexp, math.noise or math.randomseed in graph expressions; they are unsupported. math.modf returns only the integer portion.
- [page](https://create.roblox.com/docs/animation/expressions) **[[3d-modeling-rigging-and-animation]]** Inside an if or else body in a multi-line expression, use only return or a standalone expression; nested if and local declarations are not allowed.

## Numbers
- [page](https://create.roblox.com/docs/animation/expressions) Blend1DNode position range: **0 to 1 (idle at 0, run at 1 in the example)** (Output range the example expression clamps to for blending idle and run)
- [page](https://create.roblox.com/docs/animation/expressions) Integer division: **10 // 3 = 3 (rounds down)** (Floor-division operator supported in graph expressions)

## Tools
Animation Graph Editor, Blend1DNode, AnimationTrack:SetParameter, Humanoid (MoveDirection, WalkSpeed), RunService.Stepped, Library.math

## He points to
- API integration (parameter workflow, linked from the docs page)
- Animation Graph Editor documentation (prerequisite)

## Quotes
- [page](https://create.roblox.com/docs/animation/expressions) "Only false and nil are considered false."

## Topics
[[3d-modeling-rigging-and-animation]] [[common-mistakes]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
