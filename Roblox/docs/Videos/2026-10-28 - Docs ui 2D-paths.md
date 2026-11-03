---
title: "Docs: ui / 2D-paths"
url: https://create.roblox.com/docs/ui/2D-paths.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: ui / 2D-paths

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/ui/2D-paths.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox Creator Docs page on the Path2D instance for 2D splines and curved lines in ScreenGui/SurfaceGui. Covers creating paths, editing control points and tangents, visual properties, Luau scripting examples for arranging UI along a path and tweening along it, and the cubic Bézier generation math.

## Tips
- [page](https://create.roblox.com/docs/ui/2D-paths) **[[ui-ux-design]]** Path2D must sit under a ScreenGui or SurfaceGui; it does not need to be a direct child of that container.
- [page](https://create.roblox.com/docs/ui/2D-paths) **[[ui-ux-design]]** Path2D control point positions are relative to the parent container, so nesting the path in a Frame changes its effective position.
- [page](https://create.roblox.com/docs/ui/2D-paths) **[[ui-ux-design]]** Use GetPositionOnCurveArcLength(t) rather than raw parameter t to get evenly spaced positions along the curve.
- [page](https://create.roblox.com/docs/ui/2D-paths) **[[ui-ux-design]]** Tween a NumberValue from 0 to 1 and drive GuiObject.Position from its Changed event to animate UI along a path.

## Numbers
- [page](https://create.roblox.com/docs/ui/2D-paths) Thickness: **Path line thickness in pixels (example values 2 and 10)** (Path2D visual property, sets line width)
- [page](https://create.roblox.com/docs/ui/2D-paths) Example tween duration: **4 seconds, Cubic InOut, repeat count 2 with reverse** (Scripted path animation example)

## Tools
Path2D, TweenService, Roblox Studio viewport path tooling widget

## Topics
[[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
