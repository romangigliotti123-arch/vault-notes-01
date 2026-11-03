---
title: "Docs: ui / scrolling-frames"
url: https://create.roblox.com/docs/ui/scrolling-frames.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: ui / scrolling-frames

[Open](https://create.roblox.com/docs/ui/scrolling-frames.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox API docs page on ScrollingFrame: canvas size rules that trigger scrolling, CanvasPosition, scroll bar insets and asset images, clipping behavior (including rotation and rounded corners), and disabling elastic scrolling.

## Tips
- [page](https://create.roblox.com/docs/ui/scrolling-frames) **[[ui-ux-design]]** Use Enum.AutomaticSize Y or XY on ScrollingFrame.AutomaticCanvasSize so scrolling appears automatically when child content overflows Size.
- [page](https://create.roblox.com/docs/ui/scrolling-frames) **[[ui-ux-design]]** CanvasPosition does nothing unless scroll bars are visible; ensure canvas exceeds frame size before setting it.
- [page](https://create.roblox.com/docs/ui/scrolling-frames) **[[ui-ux-design]]** Set VerticalScrollBarInset to Always or ScrollBar so the canvas meets the scroll bar edge-to-edge instead of hiding content under it.
- [page](https://create.roblox.com/docs/ui/scrolling-frames) **[[ui-ux-design]]** Horizontal scroll bars can only sit below the canvas; only vertical bars can switch to left or right via VerticalScrollBarPosition.
- [page](https://create.roblox.com/docs/ui/scrolling-frames) **[[ui-ux-design]]** Set StarterGui.ClipsDescendantsSupportsRotation to true if rotated descendants must be clipped by their container.
- [page](https://create.roblox.com/docs/ui/scrolling-frames) **[[ui-ux-design]]** Clipping by a rotated container or by UICorner is unsupported; use CanvasGroup for rotated or rounded clipping.
- [page](https://create.roblox.com/docs/ui/scrolling-frames) **[[ui-ux-design]]** Set ElasticBehavior to Never on touch devices if the canvas must never scroll past its limits.
- [page](https://create.roblox.com/docs/ui/scrolling-frames) **[[ui-ux-design]]** ScrollingFrame suits displaying lots of information in a confined space and pairs well with list and grid layouts.

## Tools
ScrollingFrame, UIListLayout, UIGridLayout, CanvasGroup, UICorner

## He points to
- Roblox API docs: ScrollingFrame.CanvasSize
- Roblox API docs: ScrollingFrame.ElasticBehavior

## Topics
[[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
