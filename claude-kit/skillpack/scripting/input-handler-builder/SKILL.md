---
name: input-handler-builder
description: "Build one client input layer: named actions bound once to keyboard, gamepad and touch through ContextActionService, rebindable, throttled, released cleanly, whose handlers only request things from the server. Use when input code is scattered across scripts or mobile and gamepad are afterthoughts."
category: scripting
tags: input, contextactionservice, keyboard, gamepad, touch, mobile, bindaction, rebind, inputaction, controls
kb: Roblox/roblox-kb/ui-ux-design.md, Roblox/roblox-kb/client-server-and-remotes.md, Roblox/roblox-kb/cross-platform-and-console.md, Roblox/roblox-kb/anti-exploit-and-security.md
related: remote-guard-builder, cooldown-manager-builder, mobile-ui-audit, tween-helper-builder, proximity-prompt-wiring
---

# input-handler-builder

Input belongs in one place: a table of action names, each bound to every device, each handler asking the server for something. `scripts/InputMap.luau` wraps `ContextActionService` so game code sees phases (`"Begin"`, `"End"`), never raw input objects.

## When to use
A game with more than two actions, any gamepad or mobile target, or rebinding. Not for: UI buttons (wire them to `Activated`, which covers mouse, touch and gamepad), or a game that uses engine Server Authority (see step 6).

## Inputs (max 2)
1. The actions and their keys (default: design doc). 2. Devices (default keyboard and mouse, gamepad, touch).

## Procedure
1. Table of actions: name, keyboard, gamepad, whether it needs an on-screen touch button, whether holding matters (Begin and End) and what it asks the server.
2. Build the map once at client start: `InputMap.new(ContextActionService :: any, { sink = Enum.ContextActionResult.Sink, pass = Enum.ContextActionResult.Pass })`. Bind: `map:Bind("Dash", { inputs = { Enum.KeyCode.LeftShift, Enum.KeyCode.ButtonB }, touchButton = true, title = "Dash", throttle = 0.4 }, handler)`.
3. Handlers are small: `if phase == "Begin" then dashRemote:FireServer() end`. They send an intent (an action name and ids), never a result (position, damage). The server validates (`remote-guard-builder`) and rate-limits (`cooldown-manager-builder`); the client throttle is a courtesy against held keys only.
4. Prediction: run the visual immediately on the client and let the server confirm or correct; never apply authoritative state locally.
5. Touch: pass the touch-button flag so the engine creates the button; keep custom mobile UI out of the default thumbstick and jump areas (see `mobile-ui-audit`). Detect the device by the preferred input type rather than `TouchEnabled` (true on touch laptops).
6. Engine Server Authority: when the game sets `AuthorityMode` to Server, the vault says use InputActions, not `InputBegan`, for any input affecting the core simulation, and poll `GetState()` on the simulation bind rather than using `Changed`, `Pressed` or `Released`. This skill's map is then used only for non-simulation actions (UI toggles, emotes). Live-check the current docs.
7. Rebinding: `map:Rebind("Dash", { Enum.KeyCode.Q })`; persist the player's choice with the PlayerData system (settings table) and apply at startup.
8. Cleanup: `map:UnbindAll()` when the character or the mode (menu, vehicle) changes; bind per mode with distinct priorities so menus sink gameplay input.
9. Test: `lune run ../skillpack/scripting/input-handler-builder/scripts/tests/InputMap.test.luau` from the kit `systems` folder (fake ContextActionService).

## Studio MCP path
`list_roblox_studios` -> `script_grep` for `InputBegan|UserInputService|BindAction` -> `multi_edit` -> `start_stop_play` -> `user_keyboard_input` / `user_mouse_input` to press keys and `get_console_output` to watch the intents; `screen_capture` for touch buttons (device emulator, manual).

## Fallback
Lune tests for the map; real device behaviour (gamepad, touch buttons) is `untested` without hardware or the emulator.

## Evidence
`Roblox/roblox-kb/ui-ux-design.md`: use the `BindAction` touch-button argument; wire buttons to `Activated`; detect input with the preferred input type, not `TouchEnabled`; reserve default touch control zones; bind every input for every device. `Roblox/roblox-kb/client-server-and-remotes.md`: under Server Authority, InputAction is the only client data the server trusts; poll `GetState()` on the simulation bind; predict locally then reconcile (official Creator Docs 2026-10).

## Output
`InputMap.luau`, the action table, the handlers, the rebind persistence note, the test line.

## Acceptance checks
- [ ] Executed: Lune test quoted (`6 passed, 0 failed`).
- [ ] Every action works on keyboard, gamepad and touch (or the gap is listed).
- [ ] Handlers only send intents; no authoritative state is changed on the client.
- [ ] Menus and modes unbind or out-prioritise gameplay input.
- [ ] Device behaviour checked, or marked untested.

## Pitfalls
Returning `Pass` from a handler so the camera also reacts. Binding in `Heartbeat`. Using `InputBegan` plus `gameProcessedEvent` hacks instead of one map. Hard-coding keys in several scripts. Letting a held key spam the remote (throttle and server limit).

## Related
`remote-guard-builder`, `cooldown-manager-builder`, `mobile-ui-audit`, `proximity-prompt-wiring`.
