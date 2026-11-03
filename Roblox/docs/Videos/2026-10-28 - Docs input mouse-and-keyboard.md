---
title: "Docs: input / mouse-and-keyboard"
url: https://create.roblox.com/docs/input/mouse-and-keyboard.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: input / mouse-and-keyboard

[Open](https://create.roblox.com/docs/input/mouse-and-keyboard.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox developer docs on mouse and keyboard input: Input Action System for actions and bindings, UserInputService events (InputBegan/InputEnded/IsKeyDown), PreferredInput detection for cross-platform UI, and code for customizing, hiding, and locking the mouse icon.

## Tips
- [page](https://create.roblox.com/docs/input/mouse-and-keyboard) **[[ui-ux-design]]** Support mouse/keyboard: a large percentage of Roblox sessions are on PC/laptop, so design inputs for it from the start.
- [page](https://create.roblox.com/docs/input/mouse-and-keyboard) **[[cross-platform-and-console]]** Use the Input Action System to define actions (jump, sprint, shoot) and bind multiple hardware inputs to each, instead of hardcoding keys.
- [page](https://create.roblox.com/docs/input/mouse-and-keyboard) **[[cross-platform-and-console]]** Check UserInputService.PreferredInput to adapt on-screen buttons and menus; a connected gamepad can become the primary input even on PC.
- [page](https://create.roblox.com/docs/input/mouse-and-keyboard) **[[client-server-and-remotes]]** In InputBegan/InputEnded handlers, return early when processedEvent is true so you don't react to input another script already handled.
- [page](https://create.roblox.com/docs/input/mouse-and-keyboard) **[[ui-ux-design]]** Customize the mouse icon via UserInputService.MouseIcon to match UI style, and swap it temporarily (e.g. when hovering buttons).
- [page](https://create.roblox.com/docs/input/mouse-and-keyboard) **[[ui-ux-design]]** Lock the mouse with MouseBehavior LockCurrentPosition or LockCenter for camera control; reset to Enum.MouseBehavior.Default to unlock.
- [page](https://create.roblox.com/docs/input/mouse-and-keyboard) **[[cross-platform-and-console]]** While the mouse is locked, read InputChanged with UserInputType MouseMovement and use Delta for movement, since position no longer changes.

## Tools
Input Action System, UserInputService

## He points to
- Input type detection (Roblox docs)

## Topics
[[client-server-and-remotes]] [[cross-platform-and-console]] [[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
