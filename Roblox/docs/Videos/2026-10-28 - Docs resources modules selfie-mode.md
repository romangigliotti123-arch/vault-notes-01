---
title: "Docs: resources / modules / selfie-mode"
url: https://create.roblox.com/docs/resources/modules/selfie-mode.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: resources / modules / selfie-mode

[Open](https://create.roblox.com/docs/resources/modules/selfie-mode.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Official Roblox docs for the SelfieMode developer module: installing it from the Creator Store, configuring movement and depth-of-field, built-in actions (Depth-of-Field, Lock Gaze, Hide Others, Filter, Pose), and the Luau API for opening, closing, theming and listening to selfie mode.

## Tips
- [page](https://create.roblox.com/docs/resources/modules/selfie-mode) **[[first-session-onboarding]]** Use the SelfieMode module to let players capture clean screenshots without chat or player list, supporting filters, hiding others and posing.
- [page](https://create.roblox.com/docs/resources/modules/selfie-mode) **[[ui-ux-design]]** When using a custom open button, call setHudButtonEnabled(false) first to remove the default camera button, then connect your button to openSelfieMode().
- [page](https://create.roblox.com/docs/resources/modules/selfie-mode) **[[optimization-and-streaming]]** Depth-of-field does not render on mobile and needs graphics quality 8 or higher on non-mobile; lower-quality players are prompted to raise it, so expect the action to be missing on phones.
- [page](https://create.roblox.com/docs/resources/modules/selfie-mode) **[[scripting-and-performance]]** configure, setTheme, openSelfieMode, activateAction and similar functions can only be called from a LocalScript; place the module in ReplicatedStorage and configure it from StarterPlayerScripts.
- [page](https://create.roblox.com/docs/resources/modules/selfie-mode) **[[ui-ux-design]]** Customise look via setTheme (textSize, font, backgroundColor, button and tooltip colours, padding) to match your game's visual style.

## Numbers
- [page](https://create.roblox.com/docs/resources/modules/selfie-mode) Graphics quality required for depth-of-field: **8 or higher on non-mobile devices** (Below this, players are prompted to increase graphics quality)
- [page](https://create.roblox.com/docs/resources/modules/selfie-mode) Default textSize: **16** (Default for setTheme text size)
- [page](https://create.roblox.com/docs/resources/modules/selfie-mode) Default padding: **(0, 12)** (Main UI padding in setTheme defaults)

## Tools
SelfieMode module (Creator Store), Roblox Studio Toolbox, DepthOfFieldEffect

## He points to
- Creator Store: SelfieMode package

## Topics
[[first-session-onboarding]] [[optimization-and-streaming]] [[scripting-and-performance]] [[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
