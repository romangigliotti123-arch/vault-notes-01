---
title: "Docs: production / publishing / console-guidelines"
url: https://create.roblox.com/docs/production/publishing/console-guidelines.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: production / publishing / console-guidelines

[Open](https://create.roblox.com/docs/production/publishing/console-guidelines.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs on console development guidelines: designing UI for the 10-foot experience (relative sizing, TV-safe areas, large-screen scaling), controller navigation and minimal input moves, dynamic button icons via InputActionLabel/UserInputService, haptic feedback, progressive disclosure, and audio feedback. Notes that console games need content maturity info.

## Tips
- [page](https://create.roblox.com/docs/production/publishing/console-guidelines) **[[building-art-and-assets]]** Build UI with relative sizes and positions plus UISizeConstraint; develop for lower resolutions first so it scales up to large TVs.
- [page](https://create.roblox.com/docs/production/publishing/console-guidelines) **[[building-art-and-assets]]** Keep important UI inside TV-safe areas, since some TVs crop content at the edges.
- [page](https://create.roblox.com/docs/production/publishing/console-guidelines) **[[building-art-and-assets]]** Use ScrollingFrame to reduce on-screen clutter as UI scales up on large displays.
- [page](https://create.roblox.com/docs/production/publishing/console-guidelines) **[[core-loops-and-game-design]]** Make sure every UI element is reachable with basic D-pad, select and back navigation; console navigation is sequential.
- [page](https://create.roblox.com/docs/production/publishing/console-guidelines) **[[core-loops-and-game-design]]** Keep key actions to only a few button presses; one-button-at-a-time navigation makes extra steps costly with a controller.
- [page](https://create.roblox.com/docs/production/publishing/console-guidelines) **[[common-mistakes]]** Disable the chat window for console games regardless of custom chat setup.
- [page](https://create.roblox.com/docs/production/publishing/console-guidelines) **[[building-art-and-assets]]** Add shortcuts or supplemental buttons for essential in-game actions to speed up console navigation.
- [page](https://create.roblox.com/docs/production/publishing/console-guidelines) **[[building-art-and-assets]]** Show button icons matching the player's device; use InputActionLabel for Input Action System bindings, or GetImageForKeyCode/GetStringForKeyCode otherwise.
- [page](https://create.roblox.com/docs/production/publishing/console-guidelines) **[[building-art-and-assets]]** Use haptic feedback for explosions, collisions, attention events and UI notifications, but avoid overuse since constant vibration annoys players.
- [page](https://create.roblox.com/docs/production/publishing/console-guidelines) **[[core-loops-and-game-design]]** Use progressive disclosure to move advanced or rarely used features to secondary screens; console players go in and out of screens rather than one dense screen.
- [page](https://create.roblox.com/docs/production/publishing/console-guidelines) **[[building-art-and-assets]]** Add sound effects to confirm selections and signal menu traversal for controller-driven UI.
- [page](https://create.roblox.com/docs/production/publishing/console-guidelines) **[[common-mistakes]]** Console games always need content maturity information set up to ensure smooth releases and avoid removal from consoles.

## Numbers
- [page](https://create.roblox.com/docs/production/publishing/console-guidelines) Console player base: **200M+ Xbox and PlayStation players** (Stated as major opportunity for attracting players)
- [page](https://create.roblox.com/docs/production/publishing/console-guidelines) Viewing distance: **8–10 feet** (Typical distance players sit from the TV screen)

## Tools
UISizeConstraint, GuiService.ViewportDisplaySize, ScrollingFrame, InputActionLabel, UserInputService:GetStringForKeyCode, UserInputService:GetImageForKeyCode, HapticEffect

## He points to
- Input Action System displaying bindings docs

## Topics
[[building-art-and-assets]] [[common-mistakes]] [[core-loops-and-game-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
