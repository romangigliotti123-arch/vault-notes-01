---
title: "Docs: tutorials / curriculums / core / building / create-basic-visual-effects"
url: https://create.roblox.com/docs/tutorials/curriculums/core/building/create-basic-visual-effects.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: tutorials / curriculums / core / building / create-basic-visual-effects

[Open](https://create.roblox.com/docs/tutorials/curriculums/core/building/create-basic-visual-effects.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox Creator Docs tutorial on building two particle-emitter visual effects in Studio: a glowing flare atop the tallest sea stack (invisible anchored part, attachment, ParticleEmitter with NumberSequence Size/Transparency curves, PointLight) and a volumetric dust-mote layer (large invisible part, high-rate emitter with acceleration, rotation, envelopes). Includes Build with Assistant prompts.

## Tips
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/building/create-basic-visual-effects) **[[vfx-and-particles]]** Use Build with Assistant to generate starting particle values, then adjust colors and NumberSequence curves by eye.
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/building/create-basic-visual-effects) **[[vfx-and-particles]]** Put emitters inside an invisible anchored part (Transparency 1) so the particles can be positioned and sized without showing the host part.
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/building/create-basic-visual-effects) **[[vfx-and-particles]]** Use LightEmission 1 for flare-style textures so overlapping particles brighten additively.
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/building/create-basic-visual-effects) **[[vfx-and-particles]]** Use a NumberSequence for Size and Transparency to make particles pulse or fade across their lifetime instead of staying constant.
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/building/create-basic-visual-effects) **[[vfx-and-particles]]** Use a very high Rate in a very large volume to keep ambient dust sparse-looking; disable CanCollide so players walk through it.
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/building/create-basic-visual-effects) **[[vfx-and-particles]]** Use a PointLight for a flare that casts real light on surroundings; use Acceleration with negative Y to mimic gravity.

## Numbers
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/building/create-basic-visual-effects) Flare emitter Rate: **0.45 particles/sec (~one every two seconds)**
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/building/create-basic-visual-effects) Flare emitter Lifetime: **10, 10 (no variation)**
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/building/create-basic-visual-effects) Flare PointLight: **Brightness 2, Range 36**
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/building/create-basic-visual-effects) Dust emitter Rate: **50000 (part is huge so dust still sparse)**
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/building/create-basic-visual-effects) Dust emitter Lifetime: **1 to 10**
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/building/create-basic-visual-effects) Dust volume Size: **645, 355, 275 studs**
- [page](https://create.roblox.com/docs/tutorials/curriculums/core/building/create-basic-visual-effects) Dust particle size peak: **about 0.25**

## Games
- **Island Jump - Final**: Sample game: giant flare on tallest platform makes it a focal point that draws players to climb toward it.

## Tools
Roblox Studio, Build with Assistant, ParticleEmitter, PointLight

## He points to
- Class.ParticleEmitter
- Customizing particles

## Topics
[[vfx-and-particles]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
