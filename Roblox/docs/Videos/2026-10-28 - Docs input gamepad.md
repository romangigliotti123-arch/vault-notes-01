---
title: "Docs: input / gamepad"
url: https://create.roblox.com/docs/input/gamepad.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: input / gamepad

[Open](https://create.roblox.com/docs/input/gamepad.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox developer docs on gamepad support: Input Action System actions and bindings, PreferredInput detection, common controller binding conventions, HapticEffect rumble feedback, and testing with Controller Emulator in Studio.

## Tips
- [page](https://create.roblox.com/docs/input/gamepad) **[[cross-platform-and-console]]** Detect the player's PreferredInput type and respond to it so on-screen buttons and menus adapt across devices; a PC player may connect a gamepad and want it as primary.
- [page](https://create.roblox.com/docs/input/gamepad) **[[cross-platform-and-console]]** Use common gamepad conventions: ButtonA for confirm/jump, ButtonB for cancel/dodge/sprint, Thumbstick1 movement, Thumbstick2 camera, R2/L2 primary actions like shooting.
- [page](https://create.roblox.com/docs/input/gamepad) **[[ui-ux-design]]** Map secondary actions (reload, targeting, inventory, minimap) to ButtonL1, ButtonR1, ButtonX, or ButtonY for consistency with other games.
- [page](https://create.roblox.com/docs/input/gamepad) **[[cross-platform-and-console]]** Define gameplay inputs as Input Action System actions with bindings for multiple hardware inputs rather than hardcoding individual keys.
- [page](https://create.roblox.com/docs/input/gamepad) **[[sound-and-music]]** Add HapticEffect instances (e.g. GameplayCollision, GameplayExplosion, UIClick) and call Play() to add rumble feedback on PlayStation, Xbox, and Quest Touch controllers.
- [page](https://create.roblox.com/docs/input/gamepad) **[[testing-debugging-and-qa]]** Test gamepad support frequently with a connected controller or Studio's Controller Emulator, which lights up controls as input arrives to verify UserInputService handlers and bindings.
- [page](https://create.roblox.com/docs/input/gamepad) **[[cross-platform-and-console]]** Listen to GamepadConnected/GamepadDisconnected or check GamepadEnabled as alternative detection methods if PreferredInput is not sufficient.

## Tools
Input Action System, UserInputService, HapticEffect, Controller Emulator (Studio)

## He points to
- Input type detection docs
- UserInputService.GamepadEnabled
- UserInputService.GamepadConnected / GamepadDisconnected

## Topics
[[cross-platform-and-console]] [[sound-and-music]] [[testing-debugging-and-qa]] [[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
