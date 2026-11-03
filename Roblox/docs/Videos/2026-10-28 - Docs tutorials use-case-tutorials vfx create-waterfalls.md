---
title: "Docs: tutorials / use-case-tutorials / vfx / create-waterfalls"
url: https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/create-waterfalls.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: tutorials / use-case-tutorials / vfx / create-waterfalls

[Open](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/create-waterfalls.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs tutorial on building a waterfall with VFX: breaking a waterfall into components (cascades, splashes, white water, foam, mist) and recreating each with Beam and ParticleEmitter objects, using the Waterfall Island sample place as reference.

## Tips
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/create-waterfalls) **[[building-art-and-assets]]** Break a real-world reference (e.g. Snoqualmie Falls) into distinct components before building; each component maps to specific VFX objects.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/create-waterfalls) **[[vfx-and-particles]]** Use multiple Beams at varying speeds and lengths for cascades; this creates parallax and depth from a flat 2D texture.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/create-waterfalls) **[[vfx-and-particles]]** Set Beam TextureMode to Wrap so the texture tiles along the beam length, which looks more like flowing water.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/create-waterfalls) **[[vfx-and-particles]]** Emit splash dense and droplet particles at the same time but at different rates to emulate aerosolized water.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/create-waterfalls) **[[vfx-and-particles]]** Use NumberSequence Envelope values to add variation windows so particle size and transparency are not uniform.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/create-waterfalls) **[[vfx-and-particles]]** Set LightInfluence low (0-0.1) on water, splash, foam and mist particles so environmental light does not dull them; add LightEmission for brightness.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/create-waterfalls) **[[vfx-and-particles]]** Use Orientation VelocityPerpendicular with slow low-speed emission for foam ripples that spread across the pool surface.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/create-waterfalls) **[[vfx-and-particles]]** Hide helper block parts by setting Transparency to 1 rather than deleting them; they anchor emitters and beams.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/create-waterfalls) **[[vfx-and-particles]]** Use ZOffset (about 2) to push textures slightly off the surface they sit on to avoid z-fighting.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/create-waterfalls) **[[vfx-and-particles]]** Enable FaceCamera on beams and rainbow particles so they stay visible from any player angle.

## Numbers
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/create-waterfalls) Beam Width0/Width1: **Main drop outflow 60 to 20; fast drop 5 to 10; slow drop Width1 20** (Cascade beam widths from Waterfall Island tutorial)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/create-waterfalls) Beam TextureSpeed / TextureLength: **Outflow 0.4 / 64; FastDrop 1.3 / 2; SlowDrop 1 / 1.5** (Cascade texture flow settings)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/create-waterfalls) Dense splash Rate / Lifetime: **30 particles/s; 0.25-0.35 s** (SplashDense emitter)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/create-waterfalls) Droplet splash Rate / Lifetime: **20 particles/s; 0.15-0.6 s** (SplashDroplets emitter)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/create-waterfalls) Gentle white water Rate / Lifetime / Gravity: **12 particles/s; 1.25-1.5 s; Acceleration Y -35** (GentleWW emitter)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/create-waterfalls) Turbulent white water Rate / Lifetime: **20 particles/s; 0.25-0.5 s** (TurbulentWW emitter)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/create-waterfalls) Foam ripples Rate / Lifetime / Size: **5 particles/s; 0.5-0.7 s; size 5 to 20 studs** (FoamRipples emitter, size set via Command Bar)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/create-waterfalls) Base mist Rate / Lifetime / Size: **20 particles/s; 0.5-1 s; size 8 to 10 studs** (BaseMist emitter)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/create-waterfalls) Splash Speed / Acceleration: **20-35 studs/s; Acceleration Y -40** (Dense splash particle movement)

## Games
- **Waterfall Island**: Sample place file referenced by the tutorial; demonstrates all five waterfall components built with Beams and ParticleEmitters.

## Tools
Roblox Studio, Explorer, Properties window, Command Bar, Beam, ParticleEmitter, Asset Manager

## He points to
- Waterfall Island .rbxl sample place
- Snoqualmie Falls (Washington state) as real-world reference

## Topics
[[building-art-and-assets]] [[vfx-and-particles]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
