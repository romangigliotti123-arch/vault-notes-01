---
title: "Docs: environment / skybox"
url: https://create.roblox.com/docs/environment/skybox.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: environment / skybox

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/environment/skybox.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on Skyboxes: building a Sky object from six seamless face textures (SkyboxBk/Dn/Ft/Lf/Rt/Up), customizing celestial bodies (sun, moon, stars), and animating SkyboxOrientation with a Heartbeat script. Notes limits of orientation rotation (reflections, celestial bodies, ViewportFrames, dynamic clouds not affected).

## Tips
- [page](https://create.roblox.com/docs/environment/skybox) **[[building-art-and-assets]]** Make each skybox face seamless along all edges of neighbouring faces when folded into a cube, or the panorama will show visible seams.
- [page](https://create.roblox.com/docs/environment/skybox) **[[building-art-and-assets]]** Import custom skybox images into Roblox before assigning them to a Sky object's face properties.
- [page](https://create.roblox.com/docs/environment/skybox) **[[optimization-and-streaming]]** SkyboxOrientation is a low-cost feature that works across all platforms and quality levels, so animating it is cheap.
- [page](https://create.roblox.com/docs/environment/skybox) **[[scripting-and-performance]]** Wrap SkyboxOrientation Y in modulo 360 for long-running spin animations to avoid floating-point precision loss over time.

## Numbers
- [page](https://create.roblox.com/docs/environment/skybox) SkyboxOrientation animation example rate: **5 degrees per second, fixed 30 degree X tilt** (Example Heartbeat script spinning Y axis)

## Tools
Roblox Studio Explorer and Properties windows, Lighting.Sky object

## Topics
[[building-art-and-assets]] [[optimization-and-streaming]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
