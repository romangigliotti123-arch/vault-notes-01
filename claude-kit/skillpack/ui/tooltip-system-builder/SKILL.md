---
name: tooltip-system-builder
description: "Build a tooltip system that works on touch, mouse and controller: long-press on phones, hover delay on desktop, focus on pads, placement that flips and stays inside safe insets, one tooltip at a time. Use when item, button or stat explanations are hover-only."
category: ui
tags: ui, tooltip, hover, long press, touch, mobile, placement, safe area, gamepad, help text
kb: Roblox/roblox-kb/ui-ux-design.md, Roblox/roblox-kb/cross-platform-and-console.md, Roblox/roblox-kb/first-session-onboarding.md
related: gamepad-ui-navigator, safe-area-checker, inventory-ui-planner, button-feedback-designer, shop-ui-planner, accessibility-checker
---

# tooltip-system-builder

Hover does not exist on phones, so hover-only tooltips hide information from most Roblox players. This skill makes one tooltip service that every screen registers with; placement and show rules are `scripts/TooltipPlacement.luau` (Lune-tested).

## When to use
Item/stat/ability explanations, disabled-button reasons, or any "what does this do" text. Not for tutorials (`first-minute-designer`) or toasts (`notification-system-planner`).

## Inputs (max 2)
1. Which elements need tips (default: inventory items, shop cards, disabled buttons, HUD icons). 2. Tip content source (default: a table keyed by id, translatable).

## Procedure
1. One service, one tooltip frame (top `DisplayOrder`, `Active = false` so it never eats input), one visible at a time. Register `target -> content` rather than writing per-element scripts.
2. Trigger by input kind (detect with `UserInputService.PreferredInput`, not `TouchEnabled`): mouse hover after `HOVER_DELAY`, touch long-press after `LONG_PRESS` and dismiss on release or tap elsewhere, gamepad on focus change. `TooltipPlacement.shouldShow(kind, held, dismissed)`.
3. Place with `TooltipPlacement.place(anchorRect, tipSize, viewport, insets, gap)`: tries above, below, right, left, clamps inside the safe insets, pins on tiny viewports. Re-place on orientation change.
4. Critical information must not live only in a tooltip: touch players may never long-press. Put essentials (price, owned, why disabled) on the element itself; tooltips add detail.
5. Content: short (two lines), localised, text width with `AutomaticSize` and a max width; a stroke or solid background for contrast.
6. Teardown: hide when the target hides, the screen closes, or the camera/input mode changes; disconnect connections when a screen is destroyed.

## Studio MCP path
`list_roblox_studios` -> `search_game_tree` -> `multi_edit` to add the service module and register targets -> `start_stop_play` -> `user_mouse_input` to hover -> `screen_capture` -> `get_console_output`. Touch long-press and controller focus need a device or the emulator: `untested` otherwise.

## Fallback
Deliver the module and registry; owner verifies on a phone.

## Evidence
`Roblox/roblox-kb/ui-ux-design.md` (detect input with PreferredInput, not TouchEnabled; keep interactive UI inside safe insets; layer UI with ZIndex/DisplayOrder; keep text legible). `Roblox/roblox-kb/cross-platform-and-console.md` (touch as a first-class input; mobile-first, most sessions on mobile; map every control per input type). `Roblox/roblox-kb/first-session-onboarding.md` (explain why, not only what). Delay values are heuristics.

## Output
```
TOOLTIP SERVICE  triggers: mouse hover 0.3 s / touch hold 0.4 s / pad focus
targets: N registered   placement: above>below>right>left, clamped to insets
```

## Acceptance checks
- [ ] Every registered tip is reachable on touch (long-press) and pad (focus).
- [ ] No essential information exists only in a tooltip.
- [ ] Placement never leaves safe insets (tested in Lune with an inset case).
- [ ] The tooltip frame does not intercept input.
- [ ] Lune test passes (`TooltipPlacement.test.luau`, 6 tests).

## Pitfalls
Tooltips on MouseEnter only. Tips under the finger (place above the touch point). Multiple tooltips stuck on screen after fast input changes. Fixed-width text that clips when translated.

## Related
`gamepad-ui-navigator`, `safe-area-checker`, `inventory-ui-planner`, `button-feedback-designer`, `shop-ui-planner`.
