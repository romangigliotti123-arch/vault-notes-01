---
title: "Docs: input / micro-gamepad"
url: https://create.roblox.com/docs/input/micro-gamepad.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: input / micro-gamepad

[Open](https://create.roblox.com/docs/input/micro-gamepad.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on micro gamepad input (TV remotes). Explains detecting micro gamepads via Gamepad1 thumbstick support, mapping TV remote keycodes to legacy gamepad events, binding with IAS or ContextActionService, TV-focused UI guidance, and testing with Android TV Device Emulator and Controller Emulator.

## Tips
- [page](https://create.roblox.com/docs/input/micro-gamepad) **[[cross-platform-and-console]]** Detect micro gamepads by checking Gamepad1 is connected and supports neither Thumbstick1 nor Thumbstick2; Enum.PreferredInput.MicroGamepad is not yet set.
- [page](https://create.roblox.com/docs/input/micro-gamepad) **[[cross-platform-and-console]]** Do not identify TV remotes by legacy keycodes alone; full gamepads send the same codes. Check ButtonCenter support on Gamepad1 as well.
- [page](https://create.roblox.com/docs/input/micro-gamepad) **[[cross-platform-and-console]]** Bind TV remote buttons via legacy codes: ButtonCenter maps to ButtonA, ButtonBack maps to ButtonB, D-pad keys map to DPad directions.
- [page](https://create.roblox.com/docs/input/micro-gamepad) **[[cross-platform-and-console]]** Use separate input contexts for navigation and gameplay so one legacy button does not fire both actions at once.
- [page](https://create.roblox.com/docs/input/micro-gamepad) **[[ui-ux-design]]** For TV UI, show a visible focus state, make every control reachable with the four directions, and use large controls with clear spacing for 10-foot viewing.
- [page](https://create.roblox.com/docs/input/micro-gamepad) **[[ui-ux-design]]** Use center for primary action and back consistently for close/cancel; preserve focus when opening and closing menus.
- [page](https://create.roblox.com/docs/input/micro-gamepad) **[[cross-platform-and-console]]** Test with a physical TV remote when possible; otherwise use Studio Device Emulator (Android TV, 1920x1080) with the Controller Emulator TV Remote.
- [page](https://create.roblox.com/docs/input/micro-gamepad) **[[common-mistakes]]** In ContextActionService handlers, return Pass for unhandled input states and Sink once the input is handled so other bound actions still run.

## Numbers
- [page](https://create.roblox.com/docs/input/micro-gamepad) Android TV emulator viewport: **1920x1080** (Device Emulator viewport when Android TV is selected in Studio)
- [page](https://create.roblox.com/docs/input/micro-gamepad) Micro gamepad input slots: **Gamepad1-Gamepad8** (Slots used by micro gamepads like TV remotes)

## Tools
Input Action System (InputContext, InputAction, InputBinding), ContextActionService, Device Emulator, Controller Emulator

## He points to
- Legacy gamepad control schema (Roblox docs)
- Controller emulation (Roblox docs)

## Topics
[[common-mistakes]] [[cross-platform-and-console]] [[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
