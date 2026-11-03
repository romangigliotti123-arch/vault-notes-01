---
title: "Docs: ui / size-modifiers"
url: https://create.roblox.com/docs/ui/size-modifiers.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: ui / size-modifiers

[Open](https://create.roblox.com/docs/ui/size-modifiers.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox developer docs on UI size modifiers and constraints: UIScale for proportional scaling, AutomaticSize for auto-resizing to content, and UISizeConstraint, UITextSizeConstraint, and UIAspectRatioConstraint for bounding size, text size, and aspect ratio.

## Tips
- [page](https://create.roblox.com/docs/ui/size-modifiers) **[[ui-ux-design]]** Use UIScale to zoom in while designing detailed UI in Studio; it scales children and UIStroke/UICorner proportionally.
- [page](https://create.roblox.com/docs/ui/size-modifiers) **[[ui-ux-design]]** Tween UIScale to animate a button, e.g. slightly enlarge on mouse hover.
- [page](https://create.roblox.com/docs/ui/size-modifiers) **[[ui-ux-design]]** Use AutomaticSize so labels expand for long localized text across many languages.
- [page](https://create.roblox.com/docs/ui/size-modifiers) **[[ui-ux-design]]** Set a GuiObject's Size to 0 along an axis with AutomaticSize if it should shrink to fit children; a nonzero Size sets a minimum.
- [page](https://create.roblox.com/docs/ui/size-modifiers) **[[ui-ux-design]]** Use TextWrapped with AutomaticSize Y or XY so text labels grow vertically when wrapping.
- [page](https://create.roblox.com/docs/ui/size-modifiers) **[[ui-ux-design]]** Use ScrollingFrame.AutomaticCanvasSize instead of AutomaticSize for scrolling containers.
- [page](https://create.roblox.com/docs/ui/size-modifiers) **[[ui-ux-design]]** Keep UITextSizeConstraint MinTextSize at 9 or higher; lower values are hard for many viewers to read.
- [page](https://create.roblox.com/docs/ui/size-modifiers) **[[ui-ux-design]]** Use UIAspectRatioConstraint with AspectRatio 1 on square ImageLabels such as avatar thumbnails to prevent stretching.
- [page](https://create.roblox.com/docs/ui/size-modifiers) **[[ui-ux-design]]** A UISizeConstraint or UIAspectRatioConstraint overrides UIListLayout sizing on the same object; avoid combining them unintentionally.
- [page](https://create.roblox.com/docs/ui/size-modifiers) **[[ui-ux-design]]** Constraints must be direct children of the GuiObject they constrain.

## Numbers
- [page](https://create.roblox.com/docs/ui/size-modifiers) UITextSizeConstraint.MinTextSize minimum: **9** (Docs warn against values lower than 9 for readability)
- [page](https://create.roblox.com/docs/ui/size-modifiers) UISizeConstraint example range: **200x200 to 400x400 px** (Example MinSize (200,200) and MaxSize (400,400))
- [page](https://create.roblox.com/docs/ui/size-modifiers) UITextSizeConstraint example range: **50 to 80 px** (Example MinTextSize 50, MaxTextSize 80)
- [page](https://create.roblox.com/docs/ui/size-modifiers) UIAspectRatioConstraint examples: **2 (2:1), 0.5 (0.5:1), 1 (1:1 default)** (AspectRatio is width-to-height)

## Tools
UIScale, AutomaticSize, UISizeConstraint, UITextSizeConstraint, UIAspectRatioConstraint, UIListLayout, TextScaled

## Topics
[[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
