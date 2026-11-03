---
title: "Docs: environment / post-processing-effects"
url: https://create.roblox.com/docs/environment/post-processing-effects.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: environment / post-processing-effects

[Open](https://create.roblox.com/docs/environment/post-processing-effects.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox official docs page on post-processing effects. Covers adding BloomEffect, BlurEffect, ColorCorrectionEffect, DepthOfFieldEffect, SunRaysEffect, and ColorGradingEffect to Lighting (global, all players) or Camera (per player), plus property descriptions and the Retro tonemapper for pre-2019 look.

## Tips
- [page](https://create.roblox.com/docs/environment/post-processing-effects) **[[building-art-and-assets]]** Add effects to Lighting for global looks (e.g. sun rays) and to Camera for per-player effects (e.g. blur when a UI menu is open).
- [page](https://create.roblox.com/docs/environment/post-processing-effects) **[[ui-ux-design]]** Use BlurEffect on the Camera to blur the 3D world behind open menus so players focus on UI.
- [page](https://create.roblox.com/docs/environment/post-processing-effects) **[[player-psychology-and-game-feel]]** Use ColorCorrectionEffect TintColor to give feedback, e.g. tint screen red when health is low.
- [page](https://create.roblox.com/docs/environment/post-processing-effects) **[[building-and-level-design]]** Use DepthOfFieldEffect to blur distant objects or to focus attention on a specific item, such as in a shop.
- [page](https://create.roblox.com/docs/environment/post-processing-effects) **[[building-and-level-design]]** If effects are missing in Studio, set Editor Quality Level to the highest level under Studio Settings > Rendering.
- [page](https://create.roblox.com/docs/environment/post-processing-effects) **[[building-and-level-design]]** To recreate the pre-2019 Roblox look, use TonemapperPreset.Retro and set all light brightness to a maximum of 1.0.

## Numbers
- [page](https://create.roblox.com/docs/environment/post-processing-effects) Retro tonemapper light brightness max: **1.0** (Maximum light brightness recommended when recreating pre-2019 look)

## Tools
Roblox Studio, Lighting service, Camera object, Explorer window

## He points to
- Lighting.ClockTime
- Lighting.TimeOfDay

## Topics
[[building-and-level-design]] [[building-art-and-assets]] [[player-psychology-and-game-feel]] [[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
