---
title: "Docs: ui / on-screen-containers"
url: https://create.roblox.com/docs/ui/on-screen-containers.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: ui / on-screen-containers

[Open](https://create.roblox.com/docs/ui/on-screen-containers.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs on ScreenGui containers: placing ScreenGuis in StarterGui, toggling Enabled, DisplayOrder layering, ScreenInsets safe-area modes, ResetOnSpawn behaviour, and disabling default CoreGui elements and touch controls.

## Tips
- [page](https://create.roblox.com/docs/ui/on-screen-containers) **[[ui-ux-design]]** Keep ScreenGuis with interactive elements on CoreUISafeInsets (the default); it keeps UI clear of top bar buttons and cutouts.
- [page](https://create.roblox.com/docs/ui/on-screen-containers) **[[ui-ux-design]]** Use ScreenInsets None only for non-interactive background content, since notches and cutouts can hide it.
- [page](https://create.roblox.com/docs/ui/on-screen-containers) **[[ui-ux-design]]** Use DisplayOrder to layer multiple ScreenGuis, giving modal menus a higher value than the underlying interface.
- [page](https://create.roblox.com/docs/ui/on-screen-containers) **[[ui-ux-design]]** Toggle ScreenGui.Enabled rather than destroying screens; disabled screens stop rendering and processing input.
- [page](https://create.roblox.com/docs/ui/on-screen-containers) **[[client-server-and-remotes]]** Control UI from a LocalScript by accessing PlayerGui and using WaitForChild on screen names before setting Enabled.
- [page](https://create.roblox.com/docs/ui/on-screen-containers) **[[ui-ux-design]]** Set ResetOnSpawn to false on ScreenGuis placed directly in StarterGui so they persist across respawns and keep state.
- [page](https://create.roblox.com/docs/ui/on-screen-containers) **[[ui-ux-design]]** Disable default CoreGui elements (Health, Backpack, PlayerList) via StarterGui:SetCoreGuiEnabled when replacing them with custom UI.
- [page](https://create.roblox.com/docs/ui/on-screen-containers) **[[cross-platform-and-console]]** Set GuiService.TouchControlsEnabled to false in a client script to hide the default virtual thumbstick and jump button on touch devices.

## Tools
Roblox Studio Properties window, Visualization Options (GUI overlay toggle)

## He points to
- In-game UI Containers (Roblox docs)
- Display Order (Roblox docs)

## Topics
[[client-server-and-remotes]] [[cross-platform-and-console]] [[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
