---
title: "Docs: tutorials / use-case-tutorials / ui / interactive-ui"
url: https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/interactive-ui.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: tutorials / use-case-tutorials / ui / interactive-ui

[Open](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/interactive-ui.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Official Roblox docs tutorial on building an interactive settings UI in the HUD: gear button at top-center, a settings menu with two UIDragDetector volume sliders (Effects and Background), and reusable StatefulObjectController and SliderController ModuleScripts that handle tweened open/close state and slider-to-SoundGroup volume binding.

## Tips
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/interactive-ui) **[[ui-ux-design]]** Use UIAspectRatioConstraint plus UISizeConstraint (e.g. MaxSize inf, 44) so buttons scale with screen height but cap pixel size on phones.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/interactive-ui) **[[ui-ux-design]]** Enable the Device Emulator (phone such as iPhone X or Galaxy A51, Fit to Window) to verify UI fits small screens before publishing.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/interactive-ui) **[[ui-ux-design]]** Set LayoutOrder on siblings and keep layout targets as siblings of UIListLayout, not children, or the layout will not position them correctly.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/interactive-ui) **[[ui-ux-design]]** Give a settings menu a single parent Frame so it can be managed as one stateful object that toggles open or closed.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/interactive-ui) **[[ui-ux-design]]** Pair every toggle button with an explicit close button inside the menu so players have two ways to dismiss it.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/interactive-ui) **[[ui-ux-design]]** Use a 0-duration TweenInfo for instant state changes such as hiding a menu, and cancel running tweens before starting a new state to avoid conflicts.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/interactive-ui) **[[ui-ux-design]]** Reuse tweens by creating them once per state in a hydrate function rather than creating new tweens on every state change.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/interactive-ui) **[[scripting-and-performance]]** Put shared UI controller modules in ReplicatedStorage so both client and server-side scripts can require them.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/interactive-ui) **[[scripting-and-performance]]** Wrap UI callbacks in pcall so an error in one callback logs a warning instead of breaking the slider.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/interactive-ui) **[[sound-and-music]]** Group sounds into SoundGroups (e.g. Effects, Background) in SoundService and control volume via the group's Volume property.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/interactive-ui) **[[ui-ux-design]]** Use UIDragDetector with TranslateLine and BoundingUI linked to the track frame to build draggable sliders; sync the handle position and fill size in one setValue function.

## Numbers
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/interactive-ui) Settings button size: **10% of screen height, MaxSize 44 px height** (Gear ImageButton at top-center, aspect-ratio constrained)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/interactive-ui) Settings menu size: **75% width/height, MaxSize 800 px wide, MinSize 350 px wide** (Parent SettingsMenu frame, aspect ratio 2.5:1)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/interactive-ui) Slider track max height: **30 px** (SliderFrame UISizeConstraint MaxSize inf, 30)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/interactive-ui) Open/close tween duration: **0.5 s** (Settings button rotates 45 degrees with Exponential easing; menu uses Bounce)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/interactive-ui) Slider default initial value: **0.5** (Used when the SoundGroup volume is not found)

## Tools
Roblox Studio, Device Emulator, TweenService, UIDragDetector, UIListLayout, UIAspectRatioConstraint, UISizeConstraint, SoundGroup

## He points to
- UI Fundamentals - HUD Meter template
- UI Fundamentals - Interactivity template

## Topics
[[scripting-and-performance]] [[sound-and-music]] [[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
