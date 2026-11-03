---
title: "Docs: tutorials / use-case-tutorials / lighting / enhance-indoor-environments"
url: https://create.roblox.com/docs/tutorials/use-case-tutorials/lighting/enhance-indoor-environments.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: tutorials / use-case-tutorials / lighting / enhance-indoor-environments

[Open](https://create.roblox.com/docs/tutorials/use-case-tutorials/lighting/enhance-indoor-environments.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox official tutorial on enhancing indoor environments with Realistic lighting: global settings (LightingStyle, EnvironmentDiffuse/SpecularScale, ClockTime, SunRays, Ambient, Skybox, Atmosphere density), local lights (PointLight, SpotLight, SurfaceLight), and balancing via ExposureCompensation and ColorCorrection.

## Tips
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/lighting/enhance-indoor-environments) **[[building-and-level-design]]** Set LightingStyle to Realistic; Soft style hides local light shadows and material detail. Realistic is required for local lights to cast shadows and specular highlights.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/lighting/enhance-indoor-environments) **[[building-and-level-design]]** Surround indoor spaces with Parts at least 1 stud thick (sample uses 2.5 studs) so outdoor light doesn't leak into the room; Realistic detects indoors this way.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/lighting/enhance-indoor-environments) **[[optimization-and-streaming]]** Point lights cost more on low-end devices since they project in every direction; use only as many as needed and combine small nearby sources into one.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/lighting/enhance-indoor-environments) **[[building-and-level-design]]** Set EnvironmentDiffuseScale and EnvironmentSpecularScale to 1 so PBR materials, MaterialVariants and SurfaceAppearance reflect surroundings accurately.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/lighting/enhance-indoor-environments) **[[building-and-level-design]]** Use time of day and sun position to angle sunlight through windows onto key areas, guiding players toward the exit via indirect light cues.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/lighting/enhance-indoor-environments) **[[building-and-level-design]]** Tint Lighting.Ambient warm (e.g. 83,70,57) to match fire and candle sources; ambient colour strongly affects shadowed areas.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/lighting/enhance-indoor-environments) **[[building-and-level-design]]** Raise Atmosphere.Density (sample 0.5) to add haze that carries indirect light and warmth into dark indoor spaces; density 0 looked cold and dark.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/lighting/enhance-indoor-environments) **[[ui-ux-design]]** Use ExposureCompensation rather than Brightness to lift the scene; Brightness washes out shadows into murkiness while exposure brightens highlights more.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/lighting/enhance-indoor-environments) **[[building-and-level-design]]** Add ColorCorrectionEffect with small Contrast (0.05) and Saturation (0.1) values to fix dull, desaturated scenes without losing detail.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/lighting/enhance-indoor-environments) **[[building-and-level-design]]** Choose local light type by source shape: PointLight for omnidirectional (candles, bulbs), SpotLight for directional (lamps, flashlights), SurfaceLight for flat screens and panels.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/lighting/enhance-indoor-environments) **[[building-and-level-design]]** SurfaceLight range and emission scale with parent part size; use it for screens rather than SpotLight, which emits from the part center.

## Numbers
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/lighting/enhance-indoor-environments) Wall part thickness to block outdoor light leak: **at least 1 stud (sample: 2.5 studs)**
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/lighting/enhance-indoor-environments) ClockTime for 3:45 pm sun position: **15.6**
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/lighting/enhance-indoor-environments) Atmosphere.Density (hazy cabin): **0.5 (0 = cold and dark)**
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/lighting/enhance-indoor-environments) Ambient color warm orange: **83, 70, 57 (default 70, 70, 70)**
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/lighting/enhance-indoor-environments) ExposureCompensation: **0.5**
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/lighting/enhance-indoor-environments) ColorCorrection Contrast / Saturation: **0.05 / 0.1**
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/lighting/enhance-indoor-environments) SunRays Intensity / Spread: **0.023 / 0.266**
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/lighting/enhance-indoor-environments) Candle PointLight Brightness / Color: **0.7 / 255,202,156 (shadows on)**
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/lighting/enhance-indoor-environments) Desk SpotLight Angle / Brightness / Range: **140 / 4 / 12**
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/lighting/enhance-indoor-environments) Radio SurfaceLight Brightness / Range: **2 / 4**

## Tools
Roblox Studio, Lighting service, Atmosphere, SunRays, ColorCorrectionEffect, PointLight, SpotLight, SurfaceLight

## He points to
- Skyboxes (Roblox docs)
- Lighting Indoors - Start place file
- Lighting Indoors - Complete place file

## Topics
[[building-and-level-design]] [[optimization-and-streaming]] [[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
