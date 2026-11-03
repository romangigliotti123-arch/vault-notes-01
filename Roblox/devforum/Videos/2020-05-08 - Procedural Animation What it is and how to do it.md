---
title: "Procedural Animation: What it is and how to do it"
url: https://devforum.roblox.com/t/procedural-animation-what-it-is-and-how-to-do-it/564782
creator: Roblox DevForum
official: false
advice_density: medium
date: 2020-05-08
views: 321
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Procedural Animation: What it is and how to do it

[Open](https://devforum.roblox.com/t/procedural-animation-what-it-is-and-how-to-do-it/564782) | Roblox DevForum | 321 views | 2020-05-08

## Summary
Tutorial on procedural animation in Roblox using CFrames and TweenService instead of animation tracks. Covers history (Black Magic, Strife, script fighters), blending benefits, drawbacks (replication, complexity, tedium), tweening CFrameValues, and a keyframe method with a full R6 example.

## Tips
- [page](https://devforum.roblox.com/t/procedural-animation-what-it-is-and-how-to-do-it/564782) **[[3d-modeling-rigging-and-animation]]** Procedural animation uses CFrames instead of animation tracks; it can replace or augment Roblox's built-in animation system.
- [page](https://devforum.roblox.com/t/procedural-animation-what-it-is-and-how-to-do-it/564782) **[[core-loops-and-game-design]]** Procedural animation blends transitions naturally because code only targets the end pose, not the prior pose, enabling custom easing for blends.
- [page](https://devforum.roblox.com/t/procedural-animation-what-it-is-and-how-to-do-it/564782) **[[scripting-and-performance]]** Tween a CFrameValue and apply its Changed value to the joint's C0; TweenService can only tween values like CFrameValue, not CFrame properties directly.
- [page](https://devforum.roblox.com/t/procedural-animation-what-it-is-and-how-to-do-it/564782) **[[scripting-and-performance]]** Save a base C0 (savedBaseCFrame) at start and multiply offsets by it instead of using the current CFrame to avoid odd drift.
- [page](https://devforum.roblox.com/t/procedural-animation-what-it-is-and-how-to-do-it/564782) **[[scripting-and-performance]]** Reuse one TweenBase by cancelling it, editing goal.Value, and recreating the tween per keyframe rather than creating many tweens.
- [page](https://devforum.roblox.com/t/procedural-animation-what-it-is-and-how-to-do-it/564782) **[[scripting-and-performance]]** Use C0 of a Motor6D so procedural offsets can run alongside regular animation tracks, enabling augmentation such as character tilt.
- [page](https://devforum.roblox.com/t/procedural-animation-what-it-is-and-how-to-do-it/564782) **[[scripting-and-performance]]** CFrame.Angles takes radians; wrap degree values in math.rad().
- [page](https://devforum.roblox.com/t/procedural-animation-what-it-is-and-how-to-do-it/564782) **[[development-process-and-speed]]** Iterate on procedural animations by editing keyframe values and easing in code rather than replaying tracks, since polishing via repeated playtests is tedious.
- [page](https://devforum.roblox.com/t/procedural-animation-what-it-is-and-how-to-do-it/564782) **[[testing-debugging-and-qa]]** Procedural animation drawbacks include replication complexity; the author notes this is not covered and requires a custom approach, so plan server/client replication separately.

## Numbers
- [page](https://devforum.roblox.com/t/procedural-animation-what-it-is-and-how-to-do-it/564782) Animation:Play transition blend time: **Blend length in seconds; 0 gives instant switch with no blending, as used in Black Magic 2**
- [page](https://devforum.roblox.com/t/procedural-animation-what-it-is-and-how-to-do-it/564782) Example TweenInfo: **0.5s Cubic Out for simple keyframe; 1s Circular InOut for second keyframe**

## Games
- **Black Magic 2**: Uses procedural tilt augmentation and instant (0-second) animation switching, a large part of its signature feel.
- **Black Magic 1**: Early example of linear-lerp procedural animation with easing via loops; killed by FilteringEnabled, later revived by nylium.
- **Strife**: Procedural animation reference; revived by nylium and may behave differently now.
- **Phantom Forces**: Uses procedural CFrame-based view model animations.

## Tools
TweenService, CFrameValue, TweenInfo, Motor6D C0

## He points to
- GDC talk by David Rosen on procedural animation
- Roblox API docs for TweenService
- Black Magic 2 (tilt augmentation example)

## Quotes
- [page](https://devforum.roblox.com/t/procedural-animation-what-it-is-and-how-to-do-it/564782) "Procedural animation, in Roblox, is a method of animation that doesn't rely on animation tracks and instead uses CFrames."
- [page](https://devforum.roblox.com/t/procedural-animation-what-it-is-and-how-to-do-it/564782) "Polishing animations by playing them over and over is annoying, playtesting over and over to make small tweaks is maddening."

## Topics
[[3d-modeling-rigging-and-animation]] [[core-loops-and-game-design]] [[development-process-and-speed]] [[scripting-and-performance]] [[testing-debugging-and-qa]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
