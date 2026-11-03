---
name: safe-area-checker
description: "Check that important Roblox UI stays out of notches, home-bar and rounded-corner areas on phones: read the real insets, test each element's rect, and return nudges. Use before launch and whenever HUD or menu edges move."
category: ui
tags: ui, safe area, notch, insets, screeninsets, gui inset, phone, mobile, corners
kb: Roblox/roblox-kb/ui-ux-design.md, Roblox/roblox-kb/cross-platform-and-console.md
related: mobile-ui-audit, hud-layout-planner, ui-scale-fixer, tooltip-system-builder, gamepad-ui-navigator
---

# safe-area-checker

Phones have cutouts, rounded corners and gesture bars; consoles/TVs have overscan. Anything tappable there is lost. This skill measures instead of guessing: real insets in, per-element overflow and nudges out (`scripts/SafeArea.luau`, Lune-tested).

## When to use
Before launch, after moving edge-pinned UI, when players on one phone report "can't tap X". Not for general sizing (`ui-scale-fixer`) or for deciding what the HUD contains (`hud-layout-planner`).

## Inputs (max 2)
1. Which ScreenGuis / elements (default: everything pinned within 15% of any edge). 2. Devices (default: the emulator's notched phone in landscape and portrait, plus a plain 16:9).

## Procedure
1. Read the insets from the engine, do not assume: `ScreenGui.ScreenInsets` (None, DeviceSafeInsets, CoreUISafeInsets, TopbarSafeInsets) decides how the gui sits relative to them, and `GuiService:GetGuiInset()` returns the top-left and bottom-right core UI insets (vault: keep interactive UI inside safe insets; tuck HUD to device insets deliberately). Note which mode each ScreenGui uses.
2. Decide the mode per gui: interactive HUD and menus use a safe-inset mode; full-bleed art and backgrounds may use `None` with their buttons inset by hand. Stop condition: every gui has a stated mode.
3. Collect rects in a Client playtest (`AbsolutePosition`, `AbsoluteSize`) per emulated device and mark which are `important` (buttons, close, currency, health).
4. Run `SafeArea.fromGuiInset` + `SafeArea.check(rects, viewport, insets, pad)` with `pad` of about 8-12 px for breathing room. Important elements that overflow are blockers.
5. Fix with the issue's `SafeArea.nudge` or by switching the gui's `ScreenInsets`; prefer fixing the parent anchor so siblings move together.
6. Re-check both orientations (`PlayerGui.ScreenOrientation` can change at runtime; listen for it) and screenshot.

## Studio MCP path
`list_roblox_studios` -> `search_game_tree` -> `execute_luau` (Edit) to read each ScreenGui's `ScreenInsets` -> `start_stop_play` + `execute_luau` (Client) to read GuiInset and absolute rects -> `SafeArea.check` -> property fixes -> `screen_capture`. Emulated device choice is manual.

## Fallback
Estimate with the emulator overlay by eye and mark every result `untested`; give the owner the rect list to verify on a real notched phone.

## Evidence
`Roblox/roblox-kb/ui-ux-design.md` (keep interactive UI inside safe insets; tuck HUD to device insets; reserve space for touch controls). `Roblox/roblox-kb/cross-platform-and-console.md` (handle orientation changes at runtime via PlayerGui.ScreenOrientation; mobile-first). Device cutout sizes are not in the vault: read them from the emulator or a device, never from this file.

## Output
```
SAFE AREA <game>  insets L/T/R/B px per device
[BLOCKER] Hud/MenuButton overflow left 30 px -> nudge +30 x
[minor] ...      modes: ScreenGui -> ScreenInsets
```

## Acceptance checks
- [ ] Insets came from the engine or emulator, with the device named.
- [ ] Both orientations were checked or the report says which was not.
- [ ] Every blocker has a nudge or a mode change.
- [ ] Lune test passes (`SafeArea.test.luau`, 4 tests).

## Pitfalls
Hardcoding a notch height. Checking one device. Padding the child when the parent anchor is the problem. Forgetting landscape-left versus landscape-right notch sides.

## Related
`mobile-ui-audit`, `hud-layout-planner`, `ui-scale-fixer`, `tooltip-system-builder`.
