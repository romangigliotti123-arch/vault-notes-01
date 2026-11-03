---
title: "How to use Cos and Sin"
url: https://devforum.roblox.com/t/how-to-use-cos-and-sin/1659301
creator: Roblox DevForum
official: false
advice_density: low
date: 2022-02-07
views: 135
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# How to use Cos and Sin

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://devforum.roblox.com/t/how-to-use-cos-and-sin/1659301) | Roblox DevForum | 135 views | 2022-02-07

## Summary
Tutorial on using math.cos/math.sin (and acos/asin) in Roblox. Explains the unit-circle basics, radians, and two examples: placing parts in a circle with radius scaling, and a smooth floating-part effect using sin over Heartbeat alpha.

## Tips
- [page](https://devforum.roblox.com/t/how-to-use-cos-and-sin/1659301) **[[scripting-and-performance]]** Roblox cos and sin take radians, not degrees; convert degrees with math.pi*2 / 360 scaling before calling them.
- [page](https://devforum.roblox.com/t/how-to-use-cos-and-sin/1659301) **[[building-and-level-design]]** To place parts in a ring, loop i=1..N and use angle i*(2*pi/N), then multiply cos/sin by the desired radius (cos/sin only give unit-circle values).
- [page](https://devforum.roblox.com/t/how-to-use-cos-and-sin/1659301) **[[vfx-and-particles]]** For smooth bobbing or floating motion, drive sin(alpha) with alpha += delta in Heartbeat; a full cycle takes 2*pi seconds at rate 1 per second.
- [page](https://devforum.roblox.com/t/how-to-use-cos-and-sin/1659301) **[[scripting-and-performance]]** Use math.acos and math.asin to recover an angle in radians from a value between -1 and 1.

## Numbers
- [page](https://devforum.roblox.com/t/how-to-use-cos-and-sin/1659301) cos(pi): **-1** (Unit-circle value at pi radians)
- [page](https://devforum.roblox.com/t/how-to-use-cos-and-sin/1659301) cos(pi*0.75): **-0.707** (Example value from the tutorial)
- [page](https://devforum.roblox.com/t/how-to-use-cos-and-sin/1659301) sin(pi*2): **0** (Start of circle on the right)
- [page](https://devforum.roblox.com/t/how-to-use-cos-and-sin/1659301) ring part count and radius: **7 parts, radius 5 studs** (Example circle layout)

## Tools
math.cos, math.sin, math.acos, math.asin

## Topics
[[building-and-level-design]] [[scripting-and-performance]] [[vfx-and-particles]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
