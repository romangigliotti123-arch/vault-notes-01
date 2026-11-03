---
title: "Docs: environment / lighting"
url: https://create.roblox.com/docs/environment/lighting.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: environment / lighting

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/environment/lighting.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox Creator Docs page on global lighting via the Lighting service. Covers five property categories (Color, Intensity, Shadows, Appearance, Environment) and what each property controls, with example value sets for Ambient, OutdoorAmbient, Brightness, LightingStyle, ClockTime and related settings.

## Tips
- [page](https://create.roblox.com/docs/environment/lighting) **[[building-art-and-assets]]** Use OutdoorAmbient for time-of-day color shifts outdoors; Ambient tints the whole game, including indoor areas, so it cannot mimic sunlight alone.
- [page](https://create.roblox.com/docs/environment/lighting) **[[building-art-and-assets]]** Set LightingStyle to Realistic for the most advanced shadows and lighting; use Soft for a flat, retro Roblox look.
- [page](https://create.roblox.com/docs/environment/lighting) **[[optimization-and-streaming]]** Set PrioritizeLightingQuality to true if shadows and shaders drive the artistic feel; set false to prioritize view distance.
- [page](https://create.roblox.com/docs/environment/lighting) **[[building-art-and-assets]]** Set ShadowSoftness only when LightingStyle is Realistic; it has no effect with Soft.

## Numbers
- [page](https://create.roblox.com/docs/environment/lighting) ShadowSoftness range: **0 (hard) to 1 (soft)** (Only valid when LightingStyle is Realistic)
- [page](https://create.roblox.com/docs/environment/lighting) ClockTime range: **0 to 24 hours** (TimeOfDay uses a 24-hour string; e.g. 6.3 = 06:18:00)
- [page](https://create.roblox.com/docs/environment/lighting) Brightness example values: **0.5, 1.5, 3.75** (Higher values increase contrast between lit areas and shadows)
- [page](https://create.roblox.com/docs/environment/lighting) ExposureCompensation example values: **0, -1, 1.25** (Negative = under-exposed, positive = over-exposed)

## Tools
Roblox Studio Lighting service

## Topics
[[building-art-and-assets]] [[optimization-and-streaming]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
