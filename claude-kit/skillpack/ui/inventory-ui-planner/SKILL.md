---
name: inventory-ui-planner
description: "Plan a grid inventory UI with filters, search, sorting, paging, single and multi-select and selection reconciliation, driven by a tested view model; includes phone sizes and controller focus. Use when building or reworking an item, pet or cosmetic inventory screen."
category: ui
tags: ui, inventory, grid, filter, sort, search, selection, paging, pets, items, mobile
kb: Roblox/roblox-kb/ui-ux-design.md, Roblox/roblox-kb/cross-platform-and-console.md, Roblox/roblox-kb/first-session-onboarding.md
related: shop-ui-planner, gamepad-ui-navigator, tooltip-system-builder, button-feedback-designer, ui-scale-fixer, datastore-schema-builder
---

# inventory-ui-planner

An inventory is a view over data the server owns. This skill separates the two: a pure view model (`scripts/InventoryView.luau`, Lune-tested) filters, sorts, pages and tracks selection, and the UI renders its output.

## When to use
Items/pets/cosmetics lists, equip or sell screens. Not for storing the data (`datastore-schema-builder`, kit PlayerData) or for purchasing (`shop-ui-planner`).

## Inputs (max 2)
1. The item fields players care about (default: name, category, rarity, quantity, acquired time). 2. Typical item count (default: up to a few hundred).

## Procedure
1. Layout: a grid (`UIGridLayout`) inside a scroll frame with automatic canvas size, cell size from Scale plus `UIAspectRatioConstraint` so cells stay square on every device (vault: pick the right grid; make scroll containers scale and clip). Cells hold icon, quantity badge, rarity border plus a non-colour cue.
2. Controls: category tabs, a search box, a sort selector (name, rarity, quantity, newest), optional min-rarity filter. Keep the control row tall enough for 44 px+ touch targets.
3. View model: call `InventoryView.view(items, query)` whenever the data or query changes; render only the returned page (or virtualise the visible rows for big lists) by cloning a hidden template per row and reusing frames (vault: clone hidden templates).
4. Selection: `toggle` for single or multi-select (long-press or a select-mode button on touch, ctrl/shift on desktop), `reconcile` after any data change so sold/traded items disappear from the selection.
5. Detail and actions: a side or bottom panel with stats and Equip/Sell; destructive actions (sell, delete) confirm and are server-validated. Tooltips on touch use long-press (`tooltip-system-builder`).
6. Empty and loading states: say "no items match" with a clear-filters button; never show a blank grid.
7. Controller: `Selectable` cells with explicit `NextSelection` wrap rules (`gamepad-ui-navigator`).

## Studio MCP path
`list_roblox_studios` -> `search_game_tree` -> `execute_luau` (Edit) to build the template and layout -> `multi_edit` for the controller using InventoryView -> `start_stop_play` -> `screen_capture` at phone and desktop sizes -> `get_console_output`.

## Fallback
Provide the module and layout spec; the owner checks rendering. All rendering claims `untested` without a run.

## Evidence
`Roblox/roblox-kb/ui-ux-design.md` (pick the right grid or table layout; make scrolling containers scale and clip correctly; clone hidden templates per row or item; use LayoutOrder, not renames). `Roblox/roblox-kb/cross-platform-and-console.md` (mobile-first; touch is first-class). `Roblox/roblox-kb/first-session-onboarding.md` (gate features and UI behind progression: hide the inventory tabs the player has not unlocked).

## Output
```
INVENTORY UI <game>  fields: ...  cell: scale + aspect 1:1
queries: filters/sort/page   selection: single|multi   states: empty, loading, error
```

## Acceptance checks
- [ ] Cells are square and 44 px+ on the smallest emulated phone.
- [ ] Zero-quantity items never render; selection is reconciled after data changes.
- [ ] Destructive actions confirm and are server-validated.
- [ ] Empty state exists.
- [ ] Lune test passes (`InventoryView.test.luau`, 6 tests).

## Pitfalls
Rebuilding all cells on each keystroke. Selection ids that outlive the item. Sorting by display strings. Colour-only rarity.

## Related
`shop-ui-planner`, `gamepad-ui-navigator`, `tooltip-system-builder`, `button-feedback-designer`, `ui-scale-fixer`.
