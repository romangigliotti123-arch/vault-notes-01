---
title: "Docs: tutorials / use-case-tutorials / lighting / enhance-outdoor-environments"
url: https://create.roblox.com/docs/tutorials/use-case-tutorials/lighting/enhance-outdoor-environments.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: tutorials / use-case-tutorials / lighting / enhance-outdoor-environments

[Open](https://create.roblox.com/docs/tutorials/use-case-tutorials/lighting/enhance-outdoor-environments.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Official Roblox docs tutorial on using Realistic lighting style for an evening campfire outdoor scene: enabling Realistic lighting, PBR metal reflections via EnvironmentDiffuseScale/SpecularScale, sun ClockTime, ambient colors, skybox guidance, Atmosphere density/haze/color, and PointLight range, shadows and color.

## Tips
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/lighting/enhance-outdoor-environments) **[[building-art-and-assets]]** Switch Lighting.LightingStyle to Realistic so local light sources (PointLight, SpotLight, SurfaceLight) cast accurate shadows; Soft is the default.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/lighting/enhance-outdoor-environments) **[[building-art-and-assets]]** Set Lighting.EnvironmentDiffuseScale and EnvironmentSpecularScale to 1 so PBR materials, MaterialVariants and SurfaceAppearance show real metal reflections.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/lighting/enhance-outdoor-environments) **[[building-and-level-design]]** Move the sun near the skyline with ClockTime (e.g. 17 for ~5pm) instead of the default midday position to match the scene's time of day.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/lighting/enhance-outdoor-environments) **[[building-and-level-design]]** Use a tinted Ambient and OutdoorAmbient (e.g. purple 156,136,176 for evening) rather than default gray to match the sky mood.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/lighting/enhance-outdoor-environments) **[[building-and-level-design]]** Make a skybox's lower hemisphere similar to terrain colour and darker than the upper hemisphere to improve reflections and realism.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/lighting/enhance-outdoor-environments) **[[building-and-level-design]]** Skip clouds in the skybox and add dynamic clouds instead, since they can supplement the skybox without baking them in.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/lighting/enhance-outdoor-environments) **[[optimization-and-streaming]]** Enable PointLight shadows only where they significantly add to the scene, because extra shadows can hurt performance on low-end devices.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/lighting/enhance-outdoor-environments) **[[building-and-level-design]]** Set Atmosphere Color close to the average colour of environment objects; raise Haze to add depth and affect fresnel-heavy metal surfaces.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/lighting/enhance-outdoor-environments) **[[building-and-level-design]]** Increase PointLight Range (example 48) and Brightness (example 2) with a warm colour (255,179,73) so a campfire lights nearby trees and rocks.

## Numbers
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/lighting/enhance-outdoor-environments) ClockTime: **17** (Sun position for ~5pm evening scene)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/lighting/enhance-outdoor-environments) Atmosphere.Density: **0.272 (example 0.391 shown)** (Air particle density for evening scene)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/lighting/enhance-outdoor-environments) Atmosphere.Haze: **1** (Haze setting used in tutorial)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/lighting/enhance-outdoor-environments) PointLight Range: **48** (Campfire light range in tutorial)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/lighting/enhance-outdoor-environments) PointLight Brightness: **2** (Campfire light brightness in tutorial)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/lighting/enhance-outdoor-environments) Ambient / OutdoorAmbient: **156,136,176 (default 70,70,70)** (Purple evening ambient colour in tutorial)

## Tools
Roblox Studio

## He points to
- Lighting Outdoors - Start .rbxl
- Lighting Outdoors - Complete .rbxl
- Skyboxes documentation

## Topics
[[building-and-level-design]] [[building-art-and-assets]] [[optimization-and-streaming]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
