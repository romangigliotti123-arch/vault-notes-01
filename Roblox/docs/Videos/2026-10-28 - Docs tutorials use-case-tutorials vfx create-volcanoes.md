---
title: "Docs: tutorials / use-case-tutorials / vfx / create-volcanoes"
url: https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/create-volcanoes.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: tutorials / use-case-tutorials / vfx / create-volcanoes

[Open](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/create-volcanoes.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Official Roblox docs tutorial on building a volcanic eruption with lighting and ParticleEmitter VFX. Covers breaking a reference into components (surface ripples, embers, lava splashes, lava flow, smoke plume), local lights (PointLight), global lighting (Bloom, ColorCorrection, Clouds), and specific ParticleEmitter property values. Truncated before the lava flow and smoke plume sections.

## Tips
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/create-volcanoes) **[[building-art-and-assets]]** Break a real-world reference into distinct components, each with its own visual and behavioural traits, before choosing which VFX objects to use for each.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/create-volcanoes) **[[vfx-and-particles]]** Use local lights (PointLight in invisible parts) around the lava so it reads as the only light source; particle brightness alone cannot light the surroundings.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/create-volcanoes) **[[vfx-and-particles]]** Set LightEmission to 1 and LightInfluence to 0 on glowing particles so they stay bright regardless of environment lighting.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/create-volcanoes) **[[building-art-and-assets]]** Make emitter host parts invisible (Transparency 1) and attach ParticleEmitters to them to control emission area without visible geometry.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/create-volcanoes) **[[optimization-and-streaming]]** Flipbooks cost memory; clients disable them when memory is low, which is likely on older mobile phones. Use fewer animated effects or smaller textures.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/create-volcanoes) **[[vfx-and-particles]]** Use two emitters with flipbooks of slightly different properties (speed, size, squash) to hide animation repetition; one emitter repeats visibly.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/create-volcanoes) **[[vfx-and-particles]]** Reuse the same particle texture across gameplay areas (e.g. volcano and waterfall) to save memory and improve performance on low-end devices.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/create-volcanoes) **[[vfx-and-particles]]** Use NumberSequence Envelope (window of variation) and ColorSequence keypoints to make particles change size, color and opacity over their lifetime.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/create-volcanoes) **[[vfx-and-particles]]** Enable Bloom with threshold around 0.85 so Beam lava textures glow; desaturate with ColorCorrection for a darker night mood.

## Numbers
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/create-volcanoes) PointLight caldera brightness / range: **15 / 60** (Caldera local light, dark orange color 255,85,0)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/create-volcanoes) PointLight magma/outflow brightness / range: **2 / 50** (Crevice and outflow local lights)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/create-volcanoes) Bloom Intensity / Size / Threshold: **0.75 / 80 / 0.85** (Global lighting bloom for glowing beams)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/create-volcanoes) ClockTime / ExposureCompensation: **4.3 / -1** (Night setup; exposure about half of moonlight)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/create-volcanoes) Surface ripples emitter Rate / Lifetime: **12 per second / 5-8 s** (Foam ripples on caldera surface)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/create-volcanoes) Embers Speed / Lifetime / Acceleration: **5-8 studs/s / 1-5 s / (0,10,0)** (Embers rising from caldera)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/create-volcanoes) Flipbook layout / frames: **Grid8x8 / 64 frames** (Lava splash flipbook animation, Oneshot mode)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/create-volcanoes) SplashFill Rate / Lifetime / Speed: **8 / 1.5 s / 12-20 studs/s** (Caldera fill splashes with gravity -25 acceleration)

## Games
- **Volcano Island - Complete**: Reference place file showing final volcano; used to demonstrate lighting and VFX setup.

## Tools
Roblox Studio, ParticleEmitter, Beam, PointLight, SpotLight, SurfaceLight, Lighting service (Bloom, ColorCorrection, Clouds), Asset Manager

## He points to
- Volcano Island - Start .rbxl
- Volcano Island - Complete .rbxl
- Creating Waterfalls tutorial
- Asset Manager docs

## Topics
[[building-art-and-assets]] [[optimization-and-streaming]] [[vfx-and-particles]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
