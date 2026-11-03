---
title: "Docs: ui / grid-table-layouts"
url: https://create.roblox.com/docs/ui/grid-table-layouts.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: ui / grid-table-layouts

[Open](https://create.roblox.com/docs/ui/grid-table-layouts.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on Grid and Table layouts. Explains UIGridLayout (uniform cells, FillDirection, FillDirectionMaxCells, LayoutOrder/SortOrder) and UITableLayout (row/column cell sizing, FillEmptySpaceRows/Columns, UISizeConstraint behaviour), plus warnings that these layouts override Position/Size of siblings.

## Tips
- [page](https://create.roblox.com/docs/ui/grid-table-layouts) **[[ui-ux-design]]** Use UIGridLayout for equal-sized tiles such as shop inventories; use UITableLayout when items need to sort into related rows and columns.
- [page](https://create.roblox.com/docs/ui/grid-table-layouts) **[[ui-ux-design]]** Once UIGridLayout or UITableLayout is inserted, setting Position or Size on sibling objects in properties or scripts will not have normal effect; the layout controls them.
- [page](https://create.roblox.com/docs/ui/grid-table-layouts) **[[ui-ux-design]]** Use FillDirectionMaxCells on UIGridLayout to cap cells per row or column for finer control.
- [page](https://create.roblox.com/docs/ui/grid-table-layouts) **[[ui-ux-design]]** Set UIGridStyleLayout.SortOrder to Enum.SortOrder.Name to order grid items alphabetically; default is LayoutOrder.
- [page](https://create.roblox.com/docs/ui/grid-table-layouts) **[[ui-ux-design]]** Add UISizeConstraint MinSize larger than CellSize to let a grid object span multiple cells.
- [page](https://create.roblox.com/docs/ui/grid-table-layouts) **[[ui-ux-design]]** In UITableLayout, a header cell's UISizeConstraint MinSize sets the width or height of the entire column or row it belongs to.
- [page](https://create.roblox.com/docs/ui/grid-table-layouts) **[[ui-ux-design]]** Enable UITableLayout FillEmptySpaceColumns or FillEmptySpaceRows if cell sizes should not be dictated by child GuiObject sizes.

## Numbers
- [page](https://create.roblox.com/docs/ui/grid-table-layouts) Example table cell size: **UDim2.new(0.25,0,0.1,0) creates 25% width x 10% height cell** (TextLabel size in UITableLayout example from docs)

## Tools
UIGridLayout, UITableLayout, UISizeConstraint

## He points to
- Roblox docs: UIListLayout

## Topics
[[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
