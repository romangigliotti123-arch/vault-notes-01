---
title: "Docs: input"
url: https://create.roblox.com/docs/input.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: input

[Open](https://create.roblox.com/docs/input.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox official docs page on the Input system. Covers cross-platform input via the Input Action System, detecting the primary input type with UserInputService.PreferredInput (and why it beats TouchEnabled/GetLastInputType), a LocalScript template, and the default Roblox control bindings, including reserved inputs that cannot be overridden.

## Tips
- [page](https://create.roblox.com/docs/input) **[[ui-ux-design]]** Detect the primary input with UserInputService.PreferredInput, not TouchEnabled; TouchEnabled is true on touch-screen laptops, so it is not a reliable mobile check.
- [page](https://create.roblox.com/docs/input) **[[cross-platform-and-console]]** Build controls with the Input Action System (actions plus multiple bindings) so one action works across touch, keyboard, gamepad and VR.
- [page](https://create.roblox.com/docs/input) **[[ui-ux-design]]** Connect to UserInputService:GetPropertyChangedSignal('PreferredInput') to swap UI layouts when the player switches devices mid-session.
- [page](https://create.roblox.com/docs/input) **[[ui-ux-design]]** Avoid GetLastInputType for layout decisions; it flickers between MouseMovement and Keyboard, and between Touch and Gamepad, causing UI to flicker. Use it only for advanced control schemes.
- [page](https://create.roblox.com/docs/input) **[[ui-ux-design]]** Override Roblox default bindings only in specific cases; players already know the default movement, camera and interaction controls.
- [page](https://create.roblox.com/docs/input) **[[ui-ux-design]]** Do not try to rebind reserved inputs (Esc menu, F9 console, F11, F12, PrintScreen); they always keep their built-in purpose.
- [page](https://create.roblox.com/docs/input) **[[ui-ux-design]]** Disable the backpack, player list or chat features before reusing their keys (Tab, backtick, /), since those actions are reserved until the feature is disabled.

## Numbers
- [page](https://create.roblox.com/docs/input) PreferredInput values: **Touch, Gamepad, KeyboardAndMouse** (Enum.PreferredInput values returned by UserInputService)
- [page](https://create.roblox.com/docs/input) Mobile with Bluetooth keyboard and mouse: **PreferredInput = KeyboardAndMouse** (Switches to KeyboardAndMouse once a peripheral is connected and used)
- [page](https://create.roblox.com/docs/input) Xbox/PlayStation with keyboard and mouse: **PreferredInput = KeyboardAndMouse** (Depends on the most recently used device)

## Tools
Input Action System, UserInputService.PreferredInput, UserInputService:GetLastInputType(), LocalScript

## He points to
- Roblox Creator Docs: Input

## Topics
[[cross-platform-and-console]] [[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
