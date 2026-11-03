---
title: "Docs: tutorials / use-case-tutorials / vfx / use-particles-for-explosions"
url: https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/use-particles-for-explosions.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: tutorials / use-case-tutorials / vfx / use-particles-for-explosions

[Open](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/use-particles-for-explosions.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
x

## Tips
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/use-particles-for-explosions) **[[vfx-and-particles]]** For a one-time burst, disable the ParticleEmitter's Enabled property and call Emit(amount) from script when needed, so it doesn't emit constantly.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/use-particles-for-explosions) **[[vfx-and-particles]]** Pair short Lifetime (0.2–0.6) with higher Speed (20–40) so burst particles stay visible briefly while still travelling far.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/use-particles-for-explosions) **[[vfx-and-particles]]** Use SpreadAngle 180,180 and Drag around 10 to fire particles in all directions and make them decelerate quickly for explosions.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/use-particles-for-explosions) **[[vfx-and-particles]]** Use a color sequence with multiple keypoints and a number sequence for Transparency rising on a smooth curve to get a gradual fade-out.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/use-particles-for-explosions) **[[vfx-and-particles]]** Test bursts with the Emit() Plugin from the Creator Marketplace by entering a particle count and pressing Emit before scripting.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/use-particles-for-explosions) **[[scripting-and-performance]]** Check for a Humanoid via character:FindFirstChildWhichIsA('Humanoid') in a Touched handler before acting on the touching part.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/use-particles-for-explosions) **[[core-loops-and-game-design]]** Reuse the same burst setup with different textures and counts for other effects, such as sparkles for collectibles or impact bursts for projectiles.

## Numbers
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/use-particles-for-explosions) Lifetime: **0.2, 0.6** (Short particle lifetime range for explosion burst)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/use-particles-for-explosions) Speed: **20, 40** (Compensates for short lifetime)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/use-particles-for-explosions) Drag: **10** (Rate particles lose speed)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/use-particles-for-explosions) SpreadAngle: **180, 180** (Fires particles in all directions)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/use-particles-for-explosions) Emit amount in test and script: **100** (Particles per explosion burst)

## Tools
ParticleEmitter, Emit() Plugin (Creator Marketplace), Roblox Studio, Luau Script

## He points to
- Emit() Plugin Plugin on the Roblox Marketplace
- ParticleEmitter:Emit() API reference

## Topics
[[core-loops-and-game-design]] [[scripting-and-performance]] [[vfx-and-particles]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
