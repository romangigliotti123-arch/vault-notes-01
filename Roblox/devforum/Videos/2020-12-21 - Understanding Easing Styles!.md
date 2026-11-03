---
title: "Understanding Easing Styles!"
url: https://devforum.roblox.com/t/understanding-easing-styles/937281
creator: Roblox DevForum
official: false
advice_density: low
date: 2020-12-21
views: 235
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Understanding Easing Styles!

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://devforum.roblox.com/t/understanding-easing-styles/937281) | Roblox DevForum | 235 views | 2020-12-21

## Summary
Developer Hub-style tutorial explaining each TweenService EasingStyle (Back, Bounce, Circular, Elastic, Exponential, Linear, Sine, and the interpolated Cubic/Quad/Quart/Quint) with visual behaviour descriptions, using a grey block and red target part for comparison. EasingDirection is left at default (In).

## Tips
- [page](https://devforum.roblox.com/t/understanding-easing-styles/937281) **[[core-loops-and-game-design]]** Pick easing by feel: Back overshoots then settles, Bounce drops and rebounds lower, Elastic overshoots several times. Use these for juicy UI and object motion.
- [page](https://devforum.roblox.com/t/understanding-easing-styles/937281) **[[scripting-and-performance]]** Elastic can make objects pass through targets if too fast; slow the tween duration (author raised it from 1s to 2-3s) to avoid overshooting through colliders.
- [page](https://devforum.roblox.com/t/understanding-easing-styles/937281) **[[player-psychology-and-game-feel]]** Use Exponential or Circular for fast-start, slow-stop motion; Linear feels mechanical. Quint/Quart start faster than Quad/Cubic for more snappy starts.

## Numbers
- [page](https://devforum.roblox.com/t/understanding-easing-styles/937281) Tween duration used in demo: **3 seconds** (Each EasingStyle demo tween length; original Back demo was 1 second)
- [page](https://devforum.roblox.com/t/understanding-easing-styles/937281) Interpolation order by start speed: **Quad < Cubic < Quart < Quint** (Higher degree starts faster and ends with a stronger ease)

## Tools
TweenService, TweenInfo, Enum.EasingStyle

## Topics
[[core-loops-and-game-design]] [[player-psychology-and-game-feel]] [[scripting-and-performance]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
