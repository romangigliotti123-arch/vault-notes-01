---
title: "Docs: tutorials / use-case-tutorials / vfx / custom-particle-effects"
url: https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/custom-particle-effects.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: tutorials / use-case-tutorials / vfx / custom-particle-effects

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/custom-particle-effects.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Official Roblox docs tutorial on building a multicolored volcano smoke effect with ParticleEmitter: texture choice, transparency/size/color sequences, acceleration vs speed, and rate tuning.

## Tips
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/custom-particle-effects) **[[vfx-and-particles]]** Make particle textures grayscale so the Color property fully controls final tint; use a transparent background and blurred edges for a polished look.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/custom-particle-effects) **[[vfx-and-particles]]** Animate Transparency with a sequence, dragging the end keypoint to 1, so particles fade out over their lifetime instead of popping off.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/custom-particle-effects) **[[vfx-and-particles]]** Use a Size sequence (e.g. 3 to 10) so particles grow and overlap, which makes smoke read as a cloud rather than separate sprites.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/custom-particle-effects) **[[vfx-and-particles]]** Use a multi-keypoint Color sequence (orange to dark grey to white) to show a lifecycle change across each particle's life.

## Numbers
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/custom-particle-effects) Size sequence start: **3** (Smoke particle starting size in volcano tutorial)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/custom-particle-effects) Size sequence end: **10** (Smoke particle ending size in volcano tutorial)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/custom-particle-effects) Acceleration: **2, 2, 0** (Drift effect for wind-blown smoke)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/custom-particle-effects) Rate: **40** (Thickened smoke after acceleration spreads it out)

## Tools
Roblox Studio ParticleEmitter

## Topics
[[vfx-and-particles]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
