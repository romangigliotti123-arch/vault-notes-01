---
title: "Docs: effects / light-sources"
url: https://create.roblox.com/docs/effects/light-sources.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: effects / light-sources

[Open](https://create.roblox.com/docs/effects/light-sources.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on local light sources: PointLight, SpotLight, and SurfaceLight, their key properties (Range, Face, Angle, Color, Brightness, Shadows), and the Show Light Guides Studio setting for previewing light cones.

## Tips
- [page](https://create.roblox.com/docs/effects/light-sources) **[[building-art-and-assets]]** Insert PointLights into an Attachment rather than a BasePart, since Attachment is recommended for point-specific light emission.
- [page](https://create.roblox.com/docs/effects/light-sources) **[[building-art-and-assets]]** Use local light sources (PointLight, SpotLight, SurfaceLight) instead of relying only on global Lighting for immersive, mood-driven environments.
- [page](https://create.roblox.com/docs/effects/light-sources) **[[building-and-level-design]]** Enable Studio Settings > Show Light Guides to visualise light color and field of effect, such as a SpotLight's cone from its apex.
- [page](https://create.roblox.com/docs/effects/light-sources) **[[building-art-and-assets]]** Brightness is capped by Range: raising Brightness does not light a larger area, so adjust Range to change coverage.
- [page](https://create.roblox.com/docs/effects/light-sources) **[[building-art-and-assets]]** Match light type to source: PointLight for omnidirectional sources like bulbs and torches, SpotLight for directional sources like streetlamps and flashlights, SurfaceLight for screens and signs.

## Numbers
- [page](https://create.roblox.com/docs/effects/light-sources) SpotLight Angle maximum: **180 (full half sphere from apex)** (SpotLight Angle property, defined from cone apex)
- [page](https://create.roblox.com/docs/effects/light-sources) SurfaceLight Angle range: **0 (outward from surface) to 180 (perpendicular)** (SurfaceLight Angle property emission spread)
- [page](https://create.roblox.com/docs/effects/light-sources) Range units: **studs** (PointLight and other light Range measured radially in studs)

## Tools
Roblox Studio, Lighting service, PointLight, SpotLight, SurfaceLight

## He points to
- Roblox docs: Appearance (LightingStyle)

## Topics
[[building-and-level-design]] [[building-art-and-assets]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
