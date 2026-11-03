---
title: "We FINALLY added a MAP to our Roblox Game..."
url: https://youtu.be/tSWHABNX2bU
creator: JustDucksey
official: false
advice_density: low
date: 2025-05-12
views: 5876
transcript: auto-captions
confidence: medium
tags: [roblox, justducksey, youtube-learn]
creator_trust: TRUSTED
creator_score: 7.8
---

> [!note] Trust: TRUSTED (credibility audit score 7.8): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# We FINALLY added a MAP to our Roblox Game...

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Watch](https://youtu.be/tSWHABNX2bU) | JustDucksey | 5,876 views | 2025-05-12

## Summary
Devlog showing a Roblox car-building game adding props (lamps, signs, rocks, cacti, bushes), a wind-shake module with flying debris and distance culling, a gas pump refuel mechanic, a chisel tool and paint tool for car customization, and an admin tool for testing. Mostly entertainment and progress update with little actionable advice.

## Tips
- [1:23](https://youtu.be/tSWHABNX2bU?t=83) **[[scripting-and-performance]]** Stop animating distant objects: freeze wind-shake on far props using a configurable range; the creator says a test with many objects stayed performant.
- [1:23](https://youtu.be/tSWHABNX2bU?t=83) **[[optimization-and-streaming]]** Auto-remove debris that flew off after about 30 seconds to prevent lag from accumulating physics objects.
- [3:26](https://youtu.be/tSWHABNX2bU?t=206) **[[optimization-and-streaming]]** Gate wind-driven object flight by wind speed threshold (around 200 wind) with a random chance, so only strong gusts launch props.

## Numbers
- [3:26](https://youtu.be/tSWHABNX2bU?t=206) Wind speed threshold: **~200 for objects to start flying off** (Custom wind shake module tested at 100, 200, 400 wind)
- [1:23](https://youtu.be/tSWHABNX2bU?t=83) Debris removal time: **~30 seconds** (Flown-off objects disappear after about 30 seconds to prevent lag)

## Tools
Custom wind shake module, Chisel tool, Paint tool (HSV picker), Eyedropper tool

## Topics
[[optimization-and-streaming]] [[scripting-and-performance]]

Back to [[JustDucksey - How to make successful Roblox games]]
