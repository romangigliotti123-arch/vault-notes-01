---
title: "Docs: effects / particle-emitters"
url: https://create.roblox.com/docs/effects/particle-emitters.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: effects / particle-emitters

[Open](https://create.roblox.com/docs/effects/particle-emitters.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on ParticleEmitter: parenting (Attachment vs BasePart), customizing texture, color, size, transparency, lifetime, speed, rate, orientation, shape, flipbooks, and a rain simulation recipe with performance limits.

## Tips
- [page](https://create.roblox.com/docs/effects/particle-emitters) **[[vfx-and-particles]]** Keep particle Rate as low as possible; a single emitter maxes at 400/s (100/s on mobile). Use size and other properties for visual impact instead.
- [page](https://create.roblox.com/docs/effects/particle-emitters) **[[optimization-and-streaming]]** Large particles cost GPU fill-rate; overlapping transparent layers cost overdraw. Limit both for performance.
- [page](https://create.roblox.com/docs/effects/particle-emitters) **[[vfx-and-particles]]** Fade particles in/out using a Transparency NumberSequence to avoid popping and get a more realistic effect.
- [page](https://create.roblox.com/docs/effects/particle-emitters) **[[vfx-and-particles]]** Use PNG textures with transparent backgrounds; for grayscale textures without alpha, set LightEmission to 1 to hide dark regions.
- [page](https://create.roblox.com/docs/effects/particle-emitters) **[[vfx-and-particles]]** Test particles at both lowest and highest Editor Quality Level, since visuals vary by player graphics settings.
- [page](https://create.roblox.com/docs/effects/particle-emitters) **[[vfx-and-particles]]** Lifetime is capped at 20 seconds; higher values are silently clamped.
- [page](https://create.roblox.com/docs/effects/particle-emitters) **[[vfx-and-particles]]** Changing Speed does not affect active particles; use Acceleration, Drag or VelocityInheritance to alter live particle speed.
- [page](https://create.roblox.com/docs/effects/particle-emitters) **[[optimization-and-streaming]]** Flipbook textures cost memory; clients disable flipbooks when low on memory (common on older phones). Reuse textures and use smaller resolutions.
- [page](https://create.roblox.com/docs/effects/particle-emitters) **[[vfx-and-particles]]** Don't parent Sphere or Cylinder emitter shapes to an Attachment; they only render correctly on a BasePart.
- [page](https://create.roblox.com/docs/effects/particle-emitters) **[[vfx-and-particles]]** For rain, use a transparent anchored Part, EmissionDirection Bottom, positive Squash (e.g. 3) for streaks, and a grid of emitter parts for large areas.
- [page](https://create.roblox.com/docs/effects/particle-emitters) **[[optimization-and-streaming]]** On rain with flickering distant particles, lower emitter height and Lifetime, decrease Rate, or cover a smaller area with fewer emitter parts.

## Numbers
- [page](https://create.roblox.com/docs/effects/particle-emitters) Max particle rate per emitter: **400/s desktop, 100/s mobile**
- [page](https://create.roblox.com/docs/effects/particle-emitters) Max particle lifetime: **20 seconds**
- [page](https://create.roblox.com/docs/effects/particle-emitters) Max flipbook framerate: **30 FPS**
- [page](https://create.roblox.com/docs/effects/particle-emitters) Flipbook layouts: **2x2 (4 frames), 4x4 (16), 8x8 (64), or custom**
- [page](https://create.roblox.com/docs/effects/particle-emitters) Transparency range: **0 (opaque) to 1 (clear)**
- [page](https://create.roblox.com/docs/effects/particle-emitters) LightEmission range: **0 normal blend, 1 additive**
- [page](https://create.roblox.com/docs/effects/particle-emitters) Example rain squash value: **3**

## Games
- **The Mystery of Duvall Drive**: Hand-built example using emitters for rain, mist, splashes, and water dripping from awnings.

## Tools
Roblox Studio, Toolbox / Inventory / Creator Store, Studio Settings (Editor Quality Level)

## He points to
- The Mystery of Duvall Drive (hand-built rain/mist example)
- weather-island project (scripted storms, rain/mist spawning, roof detection)

## Topics
[[optimization-and-streaming]] [[vfx-and-particles]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
