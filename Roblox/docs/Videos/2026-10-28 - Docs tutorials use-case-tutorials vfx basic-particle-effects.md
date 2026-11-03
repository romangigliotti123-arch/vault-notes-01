---
title: "Docs: tutorials / use-case-tutorials / vfx / basic-particle-effects"
url: https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/basic-particle-effects.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: tutorials / use-case-tutorials / vfx / basic-particle-effects

[Open](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/basic-particle-effects.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Docs tutorial on making a sparkle effect with a ParticleEmitter on a neon MeshPart. Covers emitter placement, EmissionDirection, and key properties (Color, Lifetime, Rate, Speed, SpreadAngle, Size, LightEmission, Transparency, Drag), plus optional PointLight glow.

## Tips
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/basic-particle-effects) **[[building-art-and-assets]]** Set ParticleEmitter Lifetime to a short Min,Max range (e.g. 0.5, 1) for sparkles; the default 5-10s is too long for that effect.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/basic-particle-effects) **[[vfx-and-particles]]** Lower ParticleEmitter Rate (default 20/s) to around 7 for sparkle effects to avoid visual clutter.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/basic-particle-effects) **[[vfx-and-particles]]** Use a speed range (e.g. 2, 3 studs/s) for slow, gentle particle motion rather than a single fast value.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/basic-particle-effects) **[[vfx-and-particles]]** Use SpreadAngle 180, 180 to emit particles in all directions around a part; 180, 0 gives a flat circle on the X axis.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/basic-particle-effects) **[[vfx-and-particles]]** Particles emit from one face set by EmissionDirection (default Top) and from the part's volume; resize the part to widen the emission area.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/basic-particle-effects) **[[vfx-and-particles]]** For sparkles, use Size 0.3, LightEmission 1, Transparency 0.5, Drag 1.5, and optionally add a PointLight for a glow.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/basic-particle-effects) **[[vfx-and-particles]]** Prefer ParticleEmitter over pre-made Fire/Smoke objects when you need customization; Fire and Smoke are less configurable.

## Numbers
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/basic-particle-effects) Default ParticleEmitter Lifetime: **5 to 10 seconds**
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/basic-particle-effects) Default ParticleEmitter Rate: **20 particles/s**
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/basic-particle-effects) Tutorial sparkle Rate: **7 particles/s**
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/basic-particle-effects) Tutorial sparkle Lifetime: **0.5 to 1 s**
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/basic-particle-effects) Tutorial sparkle Speed: **2 to 3 studs/s**
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/basic-particle-effects) Tutorial sparkle Size / Transparency / Drag: **0.3 / 0.5 / 1.5**

## Tools
Roblox Studio, ParticleEmitter, PointLight

## He points to
- Lighting with Props course

## Topics
[[building-art-and-assets]] [[vfx-and-particles]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
