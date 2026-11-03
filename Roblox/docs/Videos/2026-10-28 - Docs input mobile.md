---
title: "Docs: input / mobile"
url: https://create.roblox.com/docs/input/mobile.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: input / mobile

[Open](https://create.roblox.com/docs/input/mobile.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on mobile input: Input Action System for cross-platform actions, PreferredInput detection, screen orientation modes and runtime orientation control, touch gestures, accelerometer/gyroscope, and haptic feedback via HapticEffect.

## Tips
- [page](https://create.roblox.com/docs/input/mobile) **[[cross-platform-and-console]]** Design for mobile first: the majority of Roblox sessions are played on mobile devices, so consider orientation and touch from the start.
- [page](https://create.roblox.com/docs/input/mobile) **[[cross-platform-and-console]]** Use the Input Action System to define actions (jump, sprint, shoot) and bind multiple hardware inputs to each, rather than hardcoding per-device input.
- [page](https://create.roblox.com/docs/input/mobile) **[[cross-platform-and-console]]** Check UserInputService.PreferredInput to decide which UI to show; switch to on-screen buttons only when touch is primary, and keep touch as a backup when a gamepad is connected.
- [page](https://create.roblox.com/docs/input/mobile) **[[ui-ux-design]]** Set StarterGui.ScreenOrientation (default LandscapeSensor) in Studio properties; lock to Portrait only when the experience needs it, e.g. a minigame.
- [page](https://create.roblox.com/docs/input/mobile) **[[cross-platform-and-console]]** Change orientation at runtime via PlayerGui.ScreenOrientation and listen to PlayerGui:GetPropertyChangedSignal("ScreenOrientation") to respond to changes.
- [page](https://create.roblox.com/docs/input/mobile) **[[player-psychology-and-game-feel]]** Add haptic feedback (HapticEffect with types like GameplayCollision, GameplayExplosion, UIClick) to enhance feel beyond visuals and audio; supported on most modern iPhone, Pixel and Samsung Galaxy devices.
- [page](https://create.roblox.com/docs/input/mobile) **[[cross-platform-and-console]]** Use touch gestures (TouchSwipe, TouchPinch) and accelerometer/gyroscope only where the device supports them, checking AccelerometerEnabled and GyroscopeEnabled first.

## Numbers
- [page](https://create.roblox.com/docs/input/mobile) Share of Roblox sessions on mobile: **Majority** (Docs state most Roblox sessions are played on mobile devices)
- [page](https://create.roblox.com/docs/input/mobile) Orientation modes: **5 (2 sensor, 3 locked)** (No portrait-upside-down mode included)

## Tools
Input Action System, UserInputService, HapticEffect, PlayerGui.ScreenOrientation, StarterGui.ScreenOrientation

## He points to
- Input type detection docs page

## Topics
[[cross-platform-and-console]] [[player-psychology-and-game-feel]] [[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
