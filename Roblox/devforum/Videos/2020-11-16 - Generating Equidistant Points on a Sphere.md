---
title: "Generating Equidistant Points on a Sphere"
url: https://devforum.roblox.com/t/generating-equidistant-points-on-a-sphere/874144
creator: Roblox DevForum
official: false
advice_density: medium
date: 2020-11-16
views: 163
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Generating Equidistant Points on a Sphere

[Open](https://devforum.roblox.com/t/generating-equidistant-points-on-a-sphere/874144) | Roblox DevForum | 163 views | 2020-11-16

## Summary
Tutorial on generating evenly spaced points on a unit sphere in Luau using the golden angle spiral (Fibonacci sphere) method, with a 2D circle warm-up. Covers the code, parameter tweaks, and an application to Boids-style raycast vision and visual effects.

## Tips
- [page](https://devforum.roblox.com/t/generating-equidistant-points-on-a-sphere/874144) **[[scripting-and-performance]]** Use a golden-angle spiral (azimuth increment = 2π × golden ratio, incline = acos(1 - 2·i/n)) to get evenly distributed points on a sphere instead of random sampling, which avoids clumps and line artifacts.
- [page](https://devforum.roblox.com/t/generating-equidistant-points-on-a-sphere/874144) **[[scripting-and-performance]]** Precompute sphere points once and store them in a table (self._points) so they can be reused without recalculating each frame.
- [page](https://devforum.roblox.com/t/generating-equidistant-points-on-a-sphere/874144) **[[scripting-and-performance]]** Use Vector3 tables for sphere directions when doing raycasts for vision cones; limiting the number of rays simulates a limited field of view and keeps cost low.
- [page](https://devforum.roblox.com/t/generating-equidistant-points-on-a-sphere/874144) **[[vfx-and-particles]]** Spherical point distributions work well for spell effects in RPGs; animate points slowly or attach a trail to one point and move it through the sequence.
- [page](https://devforum.roblox.com/t/generating-equidistant-points-on-a-sphere/874144) **[[genre-mechanics]]** Combine sphere point generation with raycasting to build basic character or NPC vision for AI and obstacle avoidance.

## Numbers
- [page](https://devforum.roblox.com/t/generating-equidistant-points-on-a-sphere/874144) Golden angle: **approx. 2.39 radians** (Angle subtended by small arc in golden ratio construction)
- [page](https://devforum.roblox.com/t/generating-equidistant-points-on-a-sphere/874144) Example point counts: **100 (circle), 400 (sphere)** (Counts used in the tutorial's demos)
- [page](https://devforum.roblox.com/t/generating-equidistant-points-on-a-sphere/874144) Multiplier: **10** (Scale factor applied to unit-sphere coordinates in demo)

## Tools
Roblox Studio, Luau

## He points to
- Brilliant.org: Inverse Transform Sampling
- Wikipedia: Boids (Craig Reynolds, 1986)

## Topics
[[genre-mechanics]] [[scripting-and-performance]] [[vfx-and-particles]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
