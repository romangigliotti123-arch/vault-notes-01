---
title: "Docs: ui / ui-drag-detectors"
url: https://create.roblox.com/docs/ui/ui-drag-detectors.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: ui / ui-drag-detectors

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/ui/ui-drag-detectors.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox official docs page on UIDragDetector: how to make any GuiObject draggable without code, drag styles (TranslateLine, TranslatePlane, Rotate, Scriptable), drag/response styles, axis, bounds, rotation and speed limits, and scripting via drag events, property signals and constraint functions.

## Tips
- [page](https://create.roblox.com/docs/ui/ui-drag-detectors) **[[ui-ux-design]]** Add a UIDragDetector as a direct child of any GuiObject to make it draggable across all input types with no code.
- [page](https://create.roblox.com/docs/ui/ui-drag-detectors) **[[ui-ux-design]]** UIDragDetectors don't work in Studio while Select, Move, Scale or Rotate tools are active; switch to another tool to test drag.
- [page](https://create.roblox.com/docs/ui/ui-drag-detectors) **[[ui-ux-design]]** Use ResponseStyle CustomOffset or CustomScale when you want drag events without the UI moving, then apply your own logic.
- [page](https://create.roblox.com/docs/ui/ui-drag-detectors) **[[ui-ux-design]]** Set BoundingUI to a container so drag stays inside it; with Scale-based TranslateLine this limits a slider to the container width without extra scripting.

## Numbers
- [page](https://create.roblox.com/docs/ui/ui-drag-detectors) Speed example: **SelectionModeDragSpeed {0.1,10},{0.1,20} in 800x600 ScreenGui gives XX speeds 90/100 and YY speeds 70/80 (e.g. 80+10 and 80+20 for XX)** (Docs example for UIDragSpeedAxisMapping; illustrates scale vs offset combination)
- [page](https://create.roblox.com/docs/ui/ui-drag-detectors) Default MinDragTranslation / MaxDragTranslation: **{0,0},{0,0} (no clamping unless Max > Min)** (Translation limits default)
- [page](https://create.roblox.com/docs/ui/ui-drag-detectors) Default DragAxis: **(1, 0)** (Axis used by TranslateLine)

## Tools
UIDragDetector, Roblox Studio

## Topics
[[scripting-and-performance]] [[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
