---
title: "Docs: input / input-action-system"
url: https://create.roblox.com/docs/input/input-action-system.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: input / input-action-system

[Open](https://create.roblox.com/docs/input/input-action-system.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on the Input Action System: contexts (PlayContext/NavContext, priority, sink), action types (Bool, Direction1D/2D/3D, ViewportPosition), per-platform bindings, Pressed/Released/StateChanged events, polling GetState for analog input, runtime context switching, and InputActionLabel (beta) for displaying bindings.

## Tips
- [page](https://create.roblox.com/docs/input/input-action-system) **[[client-server-and-remotes]]** Create a top-level PlayContext in ReplicatedStorage/Inputs even if you only use one context; it keeps the input system modular for later menus.
- [page](https://create.roblox.com/docs/input/input-action-system) **[[ui-ux-design]]** Give every InputAction a binding for gamepad, keyboard/mouse, and touch so the game works cross-platform.
- [page](https://create.roblox.com/docs/input/input-action-system) **[[cross-platform-and-console]]** Only override Roblox default controls (movement, camera, reserved keys) in specific cases; players already know them.
- [page](https://create.roblox.com/docs/input/input-action-system) **[[combat-and-gameplay-systems]]** Set Priority to 2000 and enable Sink on a menu context so its bound inputs are consumed before default PlayerScripts handle them.
- [page](https://create.roblox.com/docs/input/input-action-system) **[[physics-pathfinding-and-npc-ai]]** For continuous analog input like camera rotation, poll InputAction:GetState() each frame and multiply by dt; StateChanged fires only once for a held thumbstick.
- [page](https://create.roblox.com/docs/input/input-action-system) **[[ui-ux-design]]** Use InputActionLabel (beta) for on-screen control hints; it updates automatically on device switch or rebinding, with no scripting.
- [page](https://create.roblox.com/docs/input/input-action-system) **[[ui-ux-design]]** Use InputAction.PreferredBinding to build custom binding hints when you need full control over UI.
- [page](https://create.roblox.com/docs/input/input-action-system) **[[testing-debugging-and-qa]]** Test gamepad input in Studio with the Controller Emulator before release.
- [page](https://create.roblox.com/docs/input/input-action-system) **[[client-server-and-remotes]]** Switch contexts by firing a BindableEvent from a LocalScript (e.g. ContextEvent:Fire("PlayContext", true)) rather than toggling contexts directly from many scripts.
- [page](https://create.roblox.com/docs/input/input-action-system) **[[combat-and-gameplay-systems]]** Choose action type by input shape: Bool for jump/shoot/sprint, Direction1D for throttle/zoom, Direction2D for camera or movement, Direction3D for flight, ViewportPosition for cursors or raycast selection.

## Numbers
- [page](https://create.roblox.com/docs/input/input-action-system) Sprint walk speed multiplier: **2x default WalkSpeed** (Example sprint script doubles humanoid.WalkSpeed on Pressed)
- [page](https://create.roblox.com/docs/input/input-action-system) Mouse delta scale for camera rotation: **0.01** (Converts MouseDelta pixels to rotation range in camera binding)
- [page](https://create.roblox.com/docs/input/input-action-system) Recommended PlayContext priority: **2000** (Priority used so Sink blocks inputs before default PlayerScripts contexts)
- [page](https://create.roblox.com/docs/input/input-action-system) Camera rotation sensitivity example: **1.5 radians per second at full input** (CAMERA_SENSITIVITY constant in OnInput example script)

## Tools
Input Action System (Studio), InputContext, InputAction, InputBinding, InputActionLabel (beta), Controller Emulator

## He points to
- Roblox Controller Emulator
- File > Beta Features > InputActionLabel

## Topics
[[client-server-and-remotes]] [[combat-and-gameplay-systems]] [[cross-platform-and-console]] [[physics-pathfinding-and-npc-ai]] [[testing-debugging-and-qa]] [[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
