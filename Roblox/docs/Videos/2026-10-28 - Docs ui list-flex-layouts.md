---
title: "Docs: ui / list-flex-layouts"
url: https://create.roblox.com/docs/ui/list-flex-layouts.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: ui / list-flex-layouts

[Open](https://create.roblox.com/docs/ui/list-flex-layouts.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on UIListLayout: fill direction, sort order via LayoutOrder/Name, alignment, wrapping, padding, and flex layouts (HorizontalFlex/VerticalFlex, ItemLineAlignment, UIFlexItem for individual items). Covers performance caveats of flex.

## Tips
- [page](https://create.roblox.com/docs/ui/list-flex-layouts) **[[building-and-level-design]]** Once a UIListLayout is inserted, Position, Rotation and Size of sibling UI objects are overridden or influenced; setting them in Properties or scripts won't work normally.
- [page](https://create.roblox.com/docs/ui/list-flex-layouts) **[[ui-ux-design]]** To reverse order in a list, negate LayoutOrder values (0,1,2,3 becomes 0,-1,-2,-3) for right-to-left horizontal lists.
- [page](https://create.roblox.com/docs/ui/list-flex-layouts) **[[ui-ux-design]]** Use UIListLayout.HorizontalFlex for tab bars so tabs fill width equally and auto-adjust when tab count changes, with no fixed widths.
- [page](https://create.roblox.com/docs/ui/list-flex-layouts) **[[ui-ux-design]]** Use ItemLineAlignment = Stretch to make inconsistently sized tiles fill their row for a more cohesive layout.
- [page](https://create.roblox.com/docs/ui/list-flex-layouts) **[[ui-ux-design]]** Use Padding for space between list items; use UIPadding for space around the list's outer bounds.
- [page](https://create.roblox.com/docs/ui/list-flex-layouts) **[[optimization-and-streaming]]** Only apply flex when needed; it adds a slight performance cost over non-flex, especially on resize or when dynamically adding/removing flex items.
- [page](https://create.roblox.com/docs/ui/list-flex-layouts) **[[ui-ux-design]]** Prefer a UIGridLayout when items must strictly align to a consistent cell size in both X and Y; flex allows variable item counts per line.
- [page](https://create.roblox.com/docs/ui/list-flex-layouts) **[[ui-ux-design]]** For a single flexible element (e.g. slider bar between fixed labels), add a UIFlexItem child and set FlexMode to Fill, Grow, Shrink or Custom.

## Tools
UIListLayout, UIFlexItem, UIPadding, UIGridLayout

## He points to
- Roblox Creator Docs: UIListLayout

## Topics
[[building-and-level-design]] [[optimization-and-streaming]] [[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
