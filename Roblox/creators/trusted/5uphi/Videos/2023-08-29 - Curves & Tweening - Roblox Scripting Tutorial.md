---
title: "Curves & Tweening - Roblox Scripting Tutorial"
url: https://youtu.be/OAZvYqbzOWI
creator: Suphi Kaner
official: false
advice_density: medium
date: 2023-08-29
views: 56411
transcript: auto-captions
confidence: high
tags: [roblox, 5uphi, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.8
---

> [!note] Trust: TRUSTED (credibility audit score 8.8): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Curves & Tweening - Roblox Scripting Tutorial

[Watch](https://youtu.be/OAZvYqbzOWI) | 5uphi | 56,411 views | 2023-08-29

## Summary
Technical Roblox scripting tutorial: uses FloatCurve/Vector3Curve to define path shapes, tweens parts along curves by arc length with speed control, streams path models atomically, and syncs movement across clients via workspace:GetServerTimeNow() with no network traffic. Includes a metatable-based Path class.

## Tips
- [9:49](https://youtu.be/OAZvYqbzOWI?t=589) **[[scripting-and-performance]]** Sync cosmetic movement across clients by computing position from workspace:GetServerTimeNow() instead of local time; network traffic stays near zero.
- [27:01](https://youtu.be/OAZvYqbzOWI?t=1621) **[[scripting-and-performance]]** Parameterise path movement by arc length (magnitude between points divided by speed) so constant speed doesn't depend on point spacing.
- [30:48](https://youtu.be/OAZvYqbzOWI?t=1848) **[[optimization-and-streaming]]** Set a model's StreamingMode to Atomic when its parts must be read together, so all parts stream in and out at the same time.
- [36:22](https://youtu.be/OAZvYqbzOWI?t=2182) **[[scripting-and-performance]]** Destroy client-side instances when a streamed model is removed, otherwise re-streaming creates duplicates.
- [33:37](https://youtu.be/OAZvYqbzOWI?t=2017) **[[scripting-and-performance]]** When listening for streamed-in models, loop existing children and call the handler once before connecting ChildAdded so nothing is missed.
- [13:25](https://youtu.be/OAZvYqbzOWI?t=805) **[[code-architecture-and-frameworks]]** Build classes with a module whose __index is itself and a new() that sets a metatable on self; shared methods stay in one table to save memory.
- [11:58](https://youtu.be/OAZvYqbzOWI?t=718) **[[building-art-and-assets]]** Use a Trail between two attachments on a part to draw path visuals with Face Camera, light emission and width/transparency sequences.
- [42:29](https://youtu.be/OAZvYqbzOWI?t=2549) **[[core-loops-and-game-design]]** Apply TweenService:GetValue to a normalised alpha to add easing (bounce, exponential) to any looping path movement.
- [4:39](https://youtu.be/OAZvYqbzOWI?t=279) **[[scripting-and-performance]]** Use FloatCurve keys with tangents to shape smooth motion; leave tangents unset to let Roblox auto-calculate them.

## Numbers
- [0:25](https://youtu.be/OAZvYqbzOWI?t=25) Path movement network traffic: **near zero** (Synced path movement between clients via GetServerTimeNow, per video's network stats)
- [31:29](https://youtu.be/OAZvYqbzOWI?t=1889) Streaming Target Radius (test setting): **128** (Lowered for testing content streaming; WalkSpeed set to 20)
- [29:05](https://youtu.be/OAZvYqbzOWI?t=1745) Example path speed: **10 studs/second** (Speed parameter divides arc length; example uses 10 and 2)

## Tools
Roblox Studio, FloatCurve, Vector3Curve, TweenService:GetValue, RunService.Heartbeat, workspace:GetServerTimeNow

## He points to
- Author's channel videos on content streaming, metatables, and modulus operator (not named exactly)

## Topics
[[building-art-and-assets]] [[code-architecture-and-frameworks]] [[core-loops-and-game-design]] [[optimization-and-streaming]] [[scripting-and-performance]]

Back to [[5uphi - How to make successful Roblox games]]
