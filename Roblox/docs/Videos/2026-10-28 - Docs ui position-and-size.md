---
title: "Docs: ui / position-and-size"
url: https://create.roblox.com/docs/ui/position-and-size.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: ui / position-and-size

[Open](https://create.roblox.com/docs/ui/position-and-size.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox Creator Docs page on positioning and sizing UI objects: UDim2 Position/Size (Scale vs Offset), AnchorPoint, ZIndex, layout containers (UIListLayout, UIGridLayout, UITableLayout, UIPageLayout), and cross-platform mobile guidance (reserved zones, thumb zones, context-based UI).

## Tips
- [page](https://create.roblox.com/docs/ui/position-and-size) **[[ui-ux-design]]** Avoid placing important info or virtual buttons in the bottom-left and bottom-right corners, where default mobile controls sit.
- [page](https://create.roblox.com/docs/ui/position-and-size) **[[ui-ux-design]]** Keep frequently used buttons within easy thumb reach; comfortable reach differs between phones and tablets, so test both.
- [page](https://create.roblox.com/docs/ui/position-and-size) **[[ui-ux-design]]** Position custom buttons relative to the default jump button rather than using fixed screen coordinates, for reliable placement across devices.
- [page](https://create.roblox.com/docs/ui/position-and-size) **[[cross-platform-and-console]]** Design for all platforms you support (mobile, PC, console) rather than optimizing for one and neglecting others, since players switch devices.
- [page](https://create.roblox.com/docs/ui/position-and-size) **[[ui-ux-design]]** Show only vital info during active gameplay on mobile; use ProximityPrompts for context actions like opening doors instead of persistent buttons.
- [page](https://create.roblox.com/docs/ui/position-and-size) **[[ui-ux-design]]** Use Scale for responsive positioning and Offset for fixed pixel values; mix both in UDim2 as needed.
- [page](https://create.roblox.com/docs/ui/position-and-size) **[[ui-ux-design]]** Set AnchorPoint to (0.5, 0.5) when you want position and size changes to scale outward from the object's center.
- [page](https://create.roblox.com/docs/ui/position-and-size) **[[ui-ux-design]]** Use layout objects (UIListLayout, UIGridLayout, UITableLayout, UIPageLayout) to organize GuiObjects; they override manual position and size of children.

## Numbers
- [page](https://create.roblox.com/docs/ui/position-and-size) Button position example: **40% from top edge** (Reachable on a phone, almost unreachable on a tablet)
- [page](https://create.roblox.com/docs/ui/position-and-size) Custom button offset example: **20 px left of jump button** (Code sample placing placeholder button relative to JumpButton)
- [page](https://create.roblox.com/docs/ui/position-and-size) Custom button size scale in sample: **0.8x jump button size** (Code sample sizing)
- [page](https://create.roblox.com/docs/ui/position-and-size) Studio input inference: **0.5 -> {0.5,0},{0.5,0}; 20 -> {0,20},{0,20}** (Single numbers inferred as Scale or Offset)

## Tools
Roblox Studio Properties window, UIListLayout, UIGridLayout, UITableLayout, UIPageLayout, ProximityPrompt

## He points to
- Class.GuiObject
- Class.ScreenGui
- Datatype.UDim2

## Topics
[[cross-platform-and-console]] [[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
