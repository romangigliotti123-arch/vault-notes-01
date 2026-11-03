---
name: gamepad-ui-navigator
description: "Make Roblox menus fully usable with a controller or TV remote: plan the focus graph, wire Selectable/NextSelection links, show focus, and audit for traps and unreachable buttons. Use for any menu that must work on console, handheld or Android TV."
category: ui
tags: ui, gamepad, controller, console, tv remote, focus, selection, navigation, guiservice, accessibility
kb: Roblox/roblox-kb/ui-ux-design.md, Roblox/roblox-kb/cross-platform-and-console.md
related: input-handler-builder, button-feedback-designer, menu-flow-mapper, tooltip-system-builder, shop-ui-planner, accessibility-checker
---

# gamepad-ui-navigator

A touch-and-mouse menu is often a dead end on a controller. The official guidance is to support gamepad and TV with focus and bind every input for every device (vault). This skill plans and verifies the focus graph; `scripts/FocusNav.luau` models directional choice so the graph is tested before wiring.

## When to use
Console/TV/handheld support, or any menu pressed with a pad. Not for gameplay actions (`input-handler-builder`) or for sizes on phones (`mobile-ui-audit`).

## Inputs (max 2)
1. Which screens (default: every screen from `menu-flow-mapper` or all ScreenGuis). 2. Whether a TV remote is a target (default yes: remote-first players navigate only with a D-pad).

## Procedure
1. For each screen mark the focusable controls (`Selectable = true`) and the default control to focus on open (`GuiService.SelectedObject`). Decorative frames are not selectable.
2. Run `FocusNav.audit(items, startId, backId)` on the controls' rects. Stop condition: `unreachable` empty, `noExit` empty, `noBack` false.
3. Where geometry gives a wrong neighbour (a list beside a side bar), set explicit links: `NextSelectionUp/Down/Left/Right`. Wrap lists only on purpose.
4. Focus visibility: provide a clear selection visual (a `SelectionImageObject` or your own highlight driven by `GuiService:GetPropertyChangedSignal("SelectedObject")`), distinct from hover; never rely on colour alone.
5. Open/close: when a screen opens, set `SelectedObject` to its default; when it closes, restore the previous selection. Back/B closes the top layer (menu stack with two dismissals, vault). Trap focus inside a modal.
6. Input mapping: detect the active input with `UserInputService.PreferredInput` (not `TouchEnabled`), show the matching prompts (A/B glyphs vs keys), and bind actions for every device through the pack's `input-handler-builder`. Do not let rebinding steal reserved inputs.
7. Test with a real pad or the emulator's gamepad; walk every screen using only the D-pad and A/B.

## Studio MCP path
`list_roblox_studios` -> `search_game_tree` -> `execute_luau` (Edit) to set `Selectable`/`NextSelection*` -> `start_stop_play` -> `user_keyboard_input` to approximate D-pad keys where supported -> `screen_capture` to confirm the focus visual. Real controller input is manual: `untested` otherwise.

## Fallback
Run `FocusNav.audit` on rects exported from the layout; give the owner a checklist to walk with a controller.

## Evidence
`Roblox/roblox-kb/ui-ux-design.md` (support gamepad and TV with focus and bind every input for every device; menus as one stateful object with two dismissals and a stack; keep reserved and default inputs out of rebinds; detect input with PreferredInput, not TouchEnabled). `Roblox/roblox-kb/cross-platform-and-console.md` (map every control per input type up front; Android TV pilot: about 88% of those users use only a remote - official docs, 2026-10, live-check).

## Output
```
GAMEPAD NAV <screen>   start: <id>  back: <id>
unreachable: [] noExit: [] noBack: false
explicit links added: A.Right -> B ...
```

## Acceptance checks
- [ ] Audit returns no unreachable controls, no dead ends and a reachable back control for each screen.
- [ ] Each screen sets a default selection and restores the previous one on close.
- [ ] Focus is visible without colour alone.
- [ ] A D-pad-only walkthrough succeeded, or the report says `untested`.
- [ ] Lune test passes (`FocusNav.test.luau`, 6 tests).

## Pitfalls
Letting focus leave a modal. Selectable decorations that swallow focus. Forgetting to move focus on open (the pad "sees nothing"). Showing keyboard hints to pad users.

## Related
`input-handler-builder`, `button-feedback-designer`, `menu-flow-mapper`, `tooltip-system-builder`, `accessibility-checker`.
