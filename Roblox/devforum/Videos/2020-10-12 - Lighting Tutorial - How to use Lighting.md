---
title: "Lighting Tutorial - How to use Lighting"
url: https://devforum.roblox.com/t/lighting-tutorial-how-to-use-lighting/817013
creator: Roblox DevForum
official: false
advice_density: medium
date: 2020-10-12
views: 85
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Lighting Tutorial - How to use Lighting

[Open](https://devforum.roblox.com/t/lighting-tutorial-how-to-use-lighting/817013) | Roblox DevForum | 85 views | 2020-10-12

## Summary
Beginner tutorial on Roblox Lighting service: key properties (Ambient, Brightness, GlobalShadows, OutdoorAmbient, ClockTime, FogColor, FogEnd) and post-processing effects (Bloom, Blur, ColorCorrection, DepthOfField, SunRays), plus warning that excess lighting effects hurt low-end performance.

## Tips
- [page](https://devforum.roblox.com/t/lighting-tutorial-how-to-use-lighting/817013) **[[scripting-and-performance]]** Access Lighting via game:GetService("Lighting") rather than game.Lighting, the recommended form.
- [page](https://devforum.roblox.com/t/lighting-tutorial-how-to-use-lighting/817013) **[[optimization-and-streaming]]** Excessive lighting settings and effects can hurt performance on low-end devices; use them in moderation.
- [page](https://devforum.roblox.com/t/lighting-tutorial-how-to-use-lighting/817013) **[[building-art-and-assets]]** Match lighting to game style: cartoony sky for cartoony games, dark fog for horror games.
- [page](https://devforum.roblox.com/t/lighting-tutorial-how-to-use-lighting/817013) **[[optimization-and-streaming]]** Keep post-processing effects inside the Lighting service; they only work there and must have Enabled set to true.
- [page](https://devforum.roblox.com/t/lighting-tutorial-how-to-use-lighting/817013) **[[building-art-and-assets]]** For mild background fog, set FogEnd to 1000-2000; default is 100000, and lower values increase fog.
- [page](https://devforum.roblox.com/t/lighting-tutorial-how-to-use-lighting/817013) **[[building-art-and-assets]]** Use a BlurEffect Size of 1 or 2 for a subtle showcase-style blur.
- [page](https://devforum.roblox.com/t/lighting-tutorial-how-to-use-lighting/817013) **[[building-art-and-assets]]** Use ClockTime (24-hour clock) to set sun position; 12 is noon, 24 or 0 is midnight, PM hours are 12 + hour.

## Numbers
- [page](https://devforum.roblox.com/t/lighting-tutorial-how-to-use-lighting/817013) Lighting.Brightness default: **2** (Default Brightness value; higher means brighter world)
- [page](https://devforum.roblox.com/t/lighting-tutorial-how-to-use-lighting/817013) Lighting.FogEnd default: **100000** (Default; mild background fog suggested at 1000-2000)
- [page](https://devforum.roblox.com/t/lighting-tutorial-how-to-use-lighting/817013) BlurEffect Size for showcase look: **1-2** (Values used by showcase games per author)

## Tools
Celestial Body Dragger plugin (by Maximum_ADHD)

## He points to
- Celestial Body Dragger plugin by @Maximum_ADHD

## Topics
[[building-art-and-assets]] [[optimization-and-streaming]] [[scripting-and-performance]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
