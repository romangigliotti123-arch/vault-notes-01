---
title: "Docs: projects / cross-platform"
url: https://create.roblox.com/docs/projects/cross-platform.md
creator: Roblox Creator Docs
official: true
advice_density: high
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: projects / cross-platform

[Open](https://create.roblox.com/docs/projects/cross-platform.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs on cross-platform development: design UI and input so one game works on mobile, PC, console and gamepad. Covers the Input Action System, primary-input detection, assistive hints, Scale-based layout, ViewportDisplaySize adaptation, layout containers, and accessibility/legibility.

## Tips
- [page](https://create.roblox.com/docs/projects/cross-platform) **[[cross-platform-and-console]]** Use the Input Action System to define actions (jump, sprint, shoot) and bind multiple hardware inputs to each, instead of handling raw device inputs.
- [page](https://create.roblox.com/docs/projects/cross-platform) **[[cross-platform-and-console]]** Respond to the primary input type (UserInputService.PreferredInput), not just device capability. Touch stays a backup when a gamepad is connected.
- [page](https://create.roblox.com/docs/projects/cross-platform) **[[ui-ux-design]]** Show input-specific hints (1-5 for keyboard, gamepad button glyphs) based on the current primary input. Use InputActionLabel for no-code hints that update automatically.
- [page](https://create.roblox.com/docs/projects/cross-platform) **[[ui-ux-design]]** Position and size UI with UDim.Scale plus AnchorPoint rather than pixel offsets, since pixel sizes vary widely across devices and densities.
- [page](https://create.roblox.com/docs/projects/cross-platform) **[[ui-ux-design]]** Use ViewportDisplaySize (Small/Medium/Large) and Style Queries to adapt layout; a 75% width container that fits a phone would be huge on a 4K TV.
- [page](https://create.roblox.com/docs/projects/cross-platform) **[[ui-ux-design]]** Use UIListLayout and flex for containers so children reflow when siblings are added or removed.
- [page](https://create.roblox.com/docs/projects/cross-platform) **[[ui-ux-design]]** Keep all controls unobscured by device cutouts and Roblox UI, and add text size constraints so text stays legible on small and TV screens.
- [page](https://create.roblox.com/docs/projects/cross-platform) **[[ui-ux-design]]** Don't rely on color alone to signal an action or outcome; ensure sufficient contrast.
- [page](https://create.roblox.com/docs/projects/cross-platform) **[[testing-debugging-and-qa]]** Test with the built-in Device Emulator and Controller Emulator in Studio before release.
- [page](https://create.roblox.com/docs/projects/cross-platform) **[[cross-platform-and-console]]** After the game is cross-platform, add haptics on mobile/gamepad, touch swipe/pinch gestures, and accelerometer/gyroscope where it fits.

## Numbers
- [page](https://create.roblox.com/docs/projects/cross-platform) ViewportDisplaySize categories: **Small: most tablet/mobile/handheld; Medium: most laptops/monitors; Large: most TVs or larger** (Roblox categorises viewport size internally; use instead of pixel prediction)
- [page](https://create.roblox.com/docs/projects/cross-platform) Example width: **75% width container** (Scale-based width example; would render huge on 4K TVs without adaptation)

## Games
- **Interactivity Showcase**: Pre-made Roblox game demonstrating the cross-platform design concepts in this guide.

## Tools
Input Action System, InputActionLabel, UserInputService, GuiService.ViewportDisplaySize, UI Style Editor / Style Queries, UIListLayout, Device Emulator, Controller Emulator

## He points to
- Adaptive design guide
- Accessibility guidelines
- Displaying bindings docs

## Topics
[[cross-platform-and-console]] [[testing-debugging-and-qa]] [[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
