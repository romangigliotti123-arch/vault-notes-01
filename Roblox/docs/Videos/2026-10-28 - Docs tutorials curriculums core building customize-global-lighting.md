---
title: "Docs: tutorials / curriculums / core / building / customize-global-lighting"
url: https://create.roblox.com/docs/tutorials/curriculums/core/building/customize-global-lighting.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: tutorials / curriculums / core / building / customize-global-lighting

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/tutorials/curriculums/core/building/customize-global-lighting.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox Creator Docs tutorial on customizing global lighting for the Island Jump - Final sample. Covers Lighting service properties (Ambient, OutdoorAmbient, ColorShift_Top, LightingStyle, ShadowSoftness, ClockTime, GeographicLatitude) and Atmosphere Density/Offset, with Assistant prompts and manual steps.

## Tips
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/building/customize-global-lighting) **[[building-art-and-assets]]** Set Lighting.LightingStyle to Realistic instead of the default Soft so local light sources cast precise shadows.
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/building/customize-global-lighting) **[[building-art-and-assets]]** Tint Ambient, OutdoorAmbient and ColorShift_Top together to pull the whole scene toward one palette rather than tuning them separately.
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/building/customize-global-lighting) **[[building-art-and-assets]]** Set ShadowSoftness to 0 for crisp shadow edges when you want dramatic transitions, such as stepping from outside into a tunnel.
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/building/customize-global-lighting) **[[building-art-and-assets]]** Set only one of ClockTime or TimeOfDay; they are linked and changing one updates the other.

## Numbers
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/building/customize-global-lighting) Ambient: **Color3.fromRGB(16,16,16)** (Shaded area light color, Island Jump sample)
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/building/customize-global-lighting) ClockTime: **9** (Mid-morning sun position on 0-24 scale)
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/building/customize-global-lighting) GeographicLatitude: **78** (Rotates world to angle sun for directional shadows)
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/building/customize-global-lighting) ShadowSoftness: **0** (Hard shadow edges)

## Games
- **Island Jump - Final (sample)**: Official sample used to demonstrate cool ocean palette, hard shadows and atmosphere settings.

## Tools
Roblox Studio, Lighting service properties, Atmosphere object, Roblox Assistant

## Topics
[[building-art-and-assets]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
