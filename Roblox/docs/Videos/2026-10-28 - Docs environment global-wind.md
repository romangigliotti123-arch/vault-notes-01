---
title: "Docs: environment / global-wind"
url: https://create.roblox.com/docs/environment/global-wind.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: environment / global-wind

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/environment/global-wind.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on Workspace.GlobalWind: setting the global wind vector in Studio, the Reduce Motion effect on grass, particle wind influence via WindAffectsDrag and Drag, the Wind Direction widget, and a Luau sample for scripted gusts using math.sin.

## Tips
- [page](https://create.roblox.com/docs/environment/global-wind) **[[building-art-and-assets]]** Set Workspace.GlobalWind in Studio's Properties window (X, Y, Z) to control direction and strength for grass and clouds.
- [page](https://create.roblox.com/docs/environment/global-wind) **[[building-art-and-assets]]** Use the Wind Direction widget (View menu) to tune Speed, Yaw and Pitch visually with a wind sock model.
- [page](https://create.roblox.com/docs/environment/global-wind) **[[vfx-and-particles]]** For rain-like particles to follow wind, enable ParticleEmitter.WindAffectsDrag and set Drag greater than 0.
- [page](https://create.roblox.com/docs/environment/global-wind) **[[vfx-and-particles]]** Fire and Smoke instances follow the wind vector by default; no extra setup needed.

## Numbers
- [page](https://create.roblox.com/docs/environment/global-wind) Sample gust cycle delay: **5 s max between gusts; 3.5 s per gust cycle; 100 intervals** (Example values in the scripted GlobalWind sample)
- [page](https://create.roblox.com/docs/environment/global-wind) Sample wind vectors: **baseWind (5,0,2); gust (25,0,10)** (Example values in the scripted GlobalWind sample)

## Tools
Roblox Studio Properties window, Roblox Studio Wind Direction widget, Luau script (math.sin, task.wait)

## Topics
[[building-art-and-assets]] [[scripting-and-performance]] [[ui-ux-design]] [[vfx-and-particles]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
