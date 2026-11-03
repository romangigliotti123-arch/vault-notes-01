---
title: "Docs: ui / 9-slice"
url: https://create.roblox.com/docs/ui/9-slice.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: ui / 9-slice

[Open](https://create.roblox.com/docs/ui/9-slice.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on UI 9-slice scaling. Explains splitting an image into nine sub-images so corners stay fixed, edges stretch in one axis, and the center stretches in both. Covers opening Studio's 9-Slice Editor (ScaleType = Slice, SliceCenter) and setting offsets, noting offsets differ from SliceCenter values.

## Tips
- [page](https://create.roblox.com/docs/ui/9-slice) **[[ui-ux-design]]** Set ScaleType to Slice and use Studio's 9-Slice Editor (SliceCenter ... button) to define borders visually instead of typing values.
- [page](https://create.roblox.com/docs/ui/9-slice) **[[ui-ux-design]]** Use 9-slice for borders and corners on UI elements that must render at varying sizes or hold unknown-length localized text without distortion.
- [page](https://create.roblox.com/docs/ui/9-slice) **[[ui-ux-design]]** Enter exact offset values in the editor's side fields for better precision than dragging the red dragger lines.
- [page](https://create.roblox.com/docs/ui/9-slice) **[[ui-ux-design]]** Remember editor offsets are pixel distances from image edges to draggers, not the UI object's SliceCenter values; don't copy them directly.

## Numbers
- [page](https://create.roblox.com/docs/ui/9-slice) Sub-image scaling rules: **Corners (1,3,7,9): none; edges 2,8: horizontal; edges 4,6: vertical; center 5: both** (9-slice divides one image into nine sub-images)
- [page](https://create.roblox.com/docs/ui/9-slice) Example result size: **500×200 ImageLabel** (Example used in docs to show slice result)

## Tools
Roblox Studio 9-Slice Editor

## He points to
- Enum.ScaleType
- Class.ImageLabel
- Class.ImageButton

## Topics
[[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
