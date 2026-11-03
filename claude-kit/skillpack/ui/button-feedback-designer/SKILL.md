---
name: button-feedback-designer
description: "Define and implement every state of a Roblox button (idle, hover, pressed, disabled, loading, owned) with short tweens, sound and a touch-safe activation rule, using a tested state machine. Use when buttons feel dead, double-fire, or look the same when disabled."
category: ui
tags: ui, button, feedback, hover, press, disabled, loading, activated, touch, sound, states
kb: Roblox/roblox-kb/ui-ux-design.md, Roblox/roblox-kb/first-session-onboarding.md, Roblox/roblox-kb/cross-platform-and-console.md
related: ui-animation-planner, shop-ui-planner, gamepad-ui-navigator, accessibility-checker, ui-kit-consistency-checker
---

# button-feedback-designer

Players trust a button that answers instantly. This skill specifies a style per state and the event rules that decide when a click counts; `scripts/ButtonState.luau` is the Lune-tested state machine.

## When to use
Designing the button kit, fixing "tap does nothing" or "fires twice", or making purchase buttons clear. Not for the animation budget (`ui-animation-planner`) or full-screen flow.

## Inputs (max 2)
1. Which button types exist (default: primary, secondary, close, purchase). 2. Whether sound is wanted (default yes, one short click and one error).

## Procedure
1. List states: `idle`, `hover` (mouse/pad focus only; touch has none), `pressed`, `disabled`, `loading` (waiting for the server), `owned`. Check with `ButtonState.missingStyles(styles)`; stop condition: empty.
2. Give each state at least two visible differences (colour plus size or icon), never colour alone. Primary and secondary buttons differ in weight (vault).
3. Wire events to the machine: MouseEnter/Leave -> `enter`/`leave`; InputBegan/Ended -> `down`/`up`; use `Activated` as the single activation event so mouse, touch and gamepad all work (vault: wire every button to Activated), and handlers live in LocalScripts. For touch, `tap` models down+up without hover.
4. Activation rule: fires only on release over the same button; leaving cancels. While `loading`/`disabled`/`owned` nothing fires, so double taps cannot double purchase. The server still validates every request.
5. Timings: press response under 0.1 s, hover 0.12 s (see `ui-animation-planner`); play a click sound on activation and a distinct soft sound on a refused press.
6. Disabled must explain itself (tooltip or label: "Need 50 coins"), see `tooltip-system-builder`.

## Studio MCP path
`list_roblox_studios` -> `search_game_tree` -> `execute_luau` (Edit) to apply a style table to each button -> `multi_edit` for the controller script -> `start_stop_play` -> `user_mouse_input` to click -> `get_console_output` -> `screen_capture` of hover/press if the tool can hold state (otherwise `untested`).

## Fallback
Provide the state table and the event wiring snippet; hand-test with mouse, touch emulator and pad.

## Evidence
`Roblox/roblox-kb/ui-ux-design.md` (wire every button to Activated; put button handlers in LocalScripts; give hover and press feedback with short tweens and sound; hide or swap buy buttons once owned; do not rely on colour alone). `Roblox/roblox-kb/first-session-onboarding.md` (immediate feedback for every action). `Roblox/roblox-kb/cross-platform-and-console.md` (touch is first-class; mobile-first).

## Output
```
BUTTON STATES <kit>
type | idle | hover | pressed | disabled | loading | owned   (property deltas)
events: Activated-only; cancel on leave; locked states inert
```

## Acceptance checks
- [ ] `missingStyles` returns empty for every button type.
- [ ] Tap, click and pad all route through `Activated`.
- [ ] No state fires while locked; double tap does not double-send (tested in the Lune file).
- [ ] Disabled shows why.
- [ ] Lune test passes (`ButtonState.test.luau`, 7 tests).

## Pitfalls
Using MouseButton1Click only (touch/pad miss). Hover-dependent info on phones. Re-enabling a button before the server answered. Same look for disabled and idle.

## Related
`ui-animation-planner`, `shop-ui-planner`, `gamepad-ui-navigator`, `accessibility-checker`, `ui-kit-consistency-checker`.
