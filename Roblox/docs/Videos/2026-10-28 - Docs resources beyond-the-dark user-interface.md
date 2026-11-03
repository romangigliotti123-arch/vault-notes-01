---
title: "Docs: resources / beyond-the-dark / user-interface"
url: https://create.roblox.com/docs/resources/beyond-the-dark/user-interface.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: resources / beyond-the-dark / user-interface

[Open](https://create.roblox.com/docs/resources/beyond-the-dark/user-interface.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox developer docs case study (Beyond the Dark) on building an interactive diegetic map UI in 3D space using SurfaceGuis, ProximityPrompt activation, parallax via stacked ScreenGuis, glow via LightInfluence/Brightness, and a TweenService-based UITween module.

## Tips
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/user-interface) **[[ui-ux-design]]** Build diegetic UI inside the 3D world (SurfaceGui on parts) rather than screen overlays to keep players immersed in the world.
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/user-interface) **[[ui-ux-design]]** Mock UI in an external app first, then export pieces as .png and import into Studio to iterate on look quickly.
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/user-interface) **[[ui-ux-design]]** Non-interactive SurfaceGuis can sit directly on a part; interactive ones must live in StarterGui with Adornee set to the target part so button events work.
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/user-interface) **[[ui-ux-design]]** Fake parallax by stacking three ScreenGuis on three parts at different X values.
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/user-interface) **[[ui-ux-design]]** Set SurfaceGui.LightInfluence below 1 to enable Brightness, then raise Brightness to create a glow effect.
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/user-interface) **[[building-art-and-assets]]** Use a ProximityPrompt attached to a 3D model as a simple way to let players toggle world-embedded UI.
- [page](https://create.roblox.com/docs/resources/beyond-the-dark/user-interface) **[[vfx-and-particles]]** Centralise tween helpers in a shared ModuleScript (TweenService wrappers for fade, size, move, blur) and sequence them with delays for polished UI transitions.

## Games
- **Beyond the Dark**: Diegetic in-world space station map UI built from SurfaceGuis, ProximityPrompt toggle, and tweened reveal.

## Tools
Roblox Studio, SurfaceGui, ProximityPrompt, TweenService, ScreenGui, ReplicatedStorage ModuleScript

## Topics
[[building-art-and-assets]] [[ui-ux-design]] [[vfx-and-particles]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
