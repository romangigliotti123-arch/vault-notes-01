---
title: "Roblox TweenService - How To Tween Parts"
url: https://youtu.be/SySp1wTsCkY
creator: GnomeCode
official: false
advice_density: low
date: 2022-11-26
views: 96574
transcript: auto-captions
confidence: high
tags: [roblox, gnomecode, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.1
---

> [!note] Trust: TRUSTED (credibility audit score 8.1): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Roblox TweenService - How To Tween Parts

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Watch](https://youtu.be/SySp1wTsCkY) | GnomeCode | 96,574 views | 2022-11-26

## Summary
Tutorial on TweenService in Luau: anchor a part, build a TweenInfo (time, EasingStyle, EasingDirection, RepeatCount, Reverses), create a tween with a property table, and call Play. Shows tweening position, size and color together. No business or monetisation content.

## Tips
- [2:03](https://youtu.be/SySp1wTsCkY?t=123) **[[vfx-and-particles]]** Use TweenInfo with RepeatCount -1 for infinite repeats and Reverses true to bob a part back and forth.
- [4:49](https://youtu.be/SySp1wTsCkY?t=289) **[[vfx-and-particles]]** Switch EasingDirection from Out to InOut for smoother motion in both directions when tweens look snappy on return.
- [5:30](https://youtu.be/SySp1wTsCkY?t=330) **[[vfx-and-particles]]** Put several properties (Position, Size, Color3) in one tween's property table to animate them together with one Play call.
- [2:46](https://youtu.be/SySp1wTsCkY?t=166) **[[luau-language-and-types]]** Break long TweenInfo and property-table constructors across multiple lines for readability.

## Numbers
- [2:03](https://youtu.be/SySp1wTsCkY?t=123) Tween duration: **2 seconds** (TweenInfo time used in example)
- [4:08](https://youtu.be/SySp1wTsCkY?t=248) Position offset: **move up N studs on Y axis** (example sets new position from current position plus Vector3 Y offset)
- [5:30](https://youtu.be/SySp1wTsCkY?t=330) Size increase: **5 studs in every direction** (example size tween increases part.size by 5)

## Tools
Roblox Studio, TweenService, TweenInfo, Explorer

## Topics
[[luau-language-and-types]] [[vfx-and-particles]]

Back to [[GnomeCode - How to make successful Roblox games]]
