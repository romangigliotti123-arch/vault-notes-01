---
title: "Docs: studio / build-studio-widgets"
url: https://create.roblox.com/docs/studio/build-studio-widgets.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: studio / build-studio-widgets

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/studio/build-studio-widgets.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on building Studio plugin widgets: creating DockWidgetPluginGui objects with the required constructor parameter order, customizing widget UI, syncing colors to the Studio theme, setting mouse cursors, gathering input (UserInputService does not work), and implementing drag-and-drop between widgets.

## Tips
- [page](https://create.roblox.com/docs/studio/build-studio-widgets) **[[ai-and-tools]]** Call CreateDockWidgetPluginGui only from the command bar or a plugin script; it cannot be called from regular scripts.
- [page](https://create.roblox.com/docs/studio/build-studio-widgets) **[[ai-and-tools]]** Use the Studio GitHub GUI kit for checkboxes, radio buttons and inputs so widgets match Studio's look and support dark theme.
- [page](https://create.roblox.com/docs/studio/build-studio-widgets) **[[ai-and-tools]]** Sync widget colors with settings().Studio.Theme:GetColor() and reconnect on Studio.ThemeChanged so widgets follow the user's theme.
- [page](https://create.roblox.com/docs/studio/build-studio-widgets) **[[ai-and-tools]]** Parent every widget GuiObject to the DockWidgetPluginGui, as you would parent in-game GUI to a ScreenGui.

## Numbers
- [page](https://create.roblox.com/docs/studio/build-studio-widgets) DockWidgetPluginGuiInfo parameter count: **7 ordered parameters (InitialDockState, InitialEnabled, InitialEnabledShouldOverrideRestore, FloatingXSize, FloatingYSize, MinWidth, MinHeight)**
- [page](https://create.roblox.com/docs/studio/build-studio-widgets) Example floating widget size: **200x300 px default, 150x150 px minimum**

## Tools
Roblox Studio plugin API, DockWidgetPluginGui, Plugin:StartDrag(), Studio GUI GitHub repo

## Topics
[[ai-and-tools]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
