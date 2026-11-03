---
title: "Docs: studio / controller-emulator"
url: https://create.roblox.com/docs/studio/controller-emulator.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: studio / controller-emulator

[Open](https://create.roblox.com/docs/studio/controller-emulator.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Official Roblox Studio docs for Controller Emulator, a widget that emulates gamepads, PS4/PS5/Xbox controllers, handhelds, TV remotes and Quest VR devices. Covers opening it, sending device/keyboard/VR-pose input, remapping keys per device, and pairing with Device Simulator.

## Tips
- [page](https://create.roblox.com/docs/studio/controller-emulator) **[[first-session-onboarding]]** Test a gamepad-first control scheme by simulating a console and driving the experience entirely from the emulated pad; anything unreachable is a gap in gamepad navigation.
- [page](https://create.roblox.com/docs/studio/controller-emulator) **[[ui-ux-design]]** Confirm your UI is fully navigable on a TV remote using directional pad, center button and back button.
- [page](https://create.roblox.com/docs/studio/controller-emulator) **[[playtesting-and-feedback]]** Watch the device picture during play; if a control doesn't highlight, the problem is upstream of your input handling.
- [page](https://create.roblox.com/docs/studio/controller-emulator) **[[testing-debugging-and-qa]]** Test analog thresholds by dragging triggers and thumbsticks slowly to find where dead zones and activation thresholds actually fire.
- [page](https://create.roblox.com/docs/studio/controller-emulator) **[[cross-platform-and-console]]** Test VR interactions one hand at a time by disabling the headset and one controller, to check reach, grab volumes and whether interactions depend on gaze.
- [page](https://create.roblox.com/docs/studio/controller-emulator) **[[cross-platform-and-console]]** Use Reset Positions during a playtest to recover quickly from a VR pose you cannot recover by hand.
- [page](https://create.roblox.com/docs/studio/controller-emulator) **[[testing-debugging-and-qa]]** Use keyboard input for timing-sensitive tests; it is faster than clicking the device picture.
- [page](https://create.roblox.com/docs/studio/controller-emulator) **[[cross-platform-and-console]]** Check code branching on Enum.GamepadType, since the experience sees the emulated controller type as it would with the real device.

## Numbers
- [page](https://create.roblox.com/docs/studio/controller-emulator) Translation sensitivity range: **1 to 10** (Scales how far enabled VR parts travel per keypress)

## Tools
Controller Emulator, Device Simulator, Roblox Studio

## He points to
- Device Simulator documentation

## Topics
[[cross-platform-and-console]] [[first-session-onboarding]] [[playtesting-and-feedback]] [[testing-debugging-and-qa]] [[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
