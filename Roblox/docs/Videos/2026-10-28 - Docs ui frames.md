---
title: "Docs: ui / frames"
url: https://create.roblox.com/docs/ui/frames.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: ui / frames

[Open](https://create.roblox.com/docs/ui/frames.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on Frames: basic GuiObject containers for layouts and visual UI elements. Covers ClipsDescendants clipping behaviour (including rotated and rounded-corner limits, with CanvasGroup as the alternative) and AutomaticSize for content-driven frame sizing.

## Tips
- [page](https://create.roblox.com/docs/ui/frames) **[[ui-ux-design]]** Use Frames as containers for responsive list and flex layouts so child items adapt when the frame's size changes.
- [page](https://create.roblox.com/docs/ui/frames) **[[ui-ux-design]]** Make a thin, long Frame to serve as a visual separator line between UI elements.
- [page](https://create.roblox.com/docs/ui/frames) **[[ui-ux-design]]** Clipping is on by default for GuiObject containers; set ClipsDescendants to false only when children must render outside the bounds.
- [page](https://create.roblox.com/docs/ui/frames) **[[ui-ux-design]]** Set StarterGui.ClipsDescendantsSupportsRotation to true if clipping must work on rotated descendants (non-zero Rotation) inside a container.
- [page](https://create.roblox.com/docs/ui/frames) **[[ui-ux-design]]** Clipping by a rotated container or by UICorner rounded corners is not supported; use CanvasGroup when you need clipping on rotated or rounded containers.
- [page](https://create.roblox.com/docs/ui/frames) **[[ui-ux-design]]** For auto-sized frames, set Size to the minimum width and/or height, then set AutomaticSize to X, Y, or XY so the frame grows with its content.

## Tools
Roblox Studio, Frame, ScrollingFrame, ViewportFrame, VideoFrame, CanvasGroup, UICorner

## He points to
- Class.CanvasGroup
- Class.GuiObject.ClipsDescendants
- Class.StarterGui.ClipsDescendantsSupportsRotation
- Class.Frame.AutomaticSize
- Class.GuiObject.Rotation
- Class.UICorner

## Topics
[[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
