---
title: "Docs: tutorials / use-case-tutorials / lighting / create-flickering-lights"
url: https://create.roblox.com/docs/tutorials/use-case-tutorials/lighting/create-flickering-lights.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: tutorials / use-case-tutorials / lighting / create-flickering-lights

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/tutorials/use-case-tutorials/lighting/create-flickering-lights.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs tutorial on making flickering lights in Studio. Covers adding a NumberSequence attribute (BrightnessCurve) and a number LoopDuration attribute to a banker's lamp model, then a Heartbeat script that evaluates the curve each frame and scales the SpotLight, Beam brightness and bulb color.

## Tips
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/lighting/create-flickering-lights) **[[building-art-and-assets]]** Store flicker parameters as model attributes (BrightnessCurve as NumberSequence, LoopDuration as Number) so you can tune them in Studio without editing script code.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/lighting/create-flickering-lights) **[[scripting-and-performance]]** Read attributes once at script start and cache references to lights and beams rather than looking them up every frame.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/lighting/create-flickering-lights) **[[scripting-and-performance]]** Drive flicker from time() modulo a loop duration inside a Heartbeat connection so the cycle is deterministic and frame-rate independent.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/lighting/create-flickering-lights) **[[building-art-and-assets]]** Keep original brightness and color values in local variables and multiply by a relative 0-1 factor, so the effect scales correctly from the authored values.

## Numbers
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/lighting/create-flickering-lights) LoopDuration example: **1 second** (Sample loop duration attribute set to 1 so the sequence repeats each second.)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/lighting/create-flickering-lights) Example brightness keypoints: **100%, 50%, 75%** (Sample curve: full, half, then three-quarter brightness for successive flickers.)

## Tools
Roblox Studio, Explorer and Properties windows, NumberSequence editor, RunService.Heartbeat

## Topics
[[building-art-and-assets]] [[scripting-and-performance]] [[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
