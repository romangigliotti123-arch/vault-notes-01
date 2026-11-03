---
title: "DON’T do this mistake in your Roblox games!"
url: https://youtu.be/oYQ5jIZKE8s
creator: BubuTheDev
official: false
advice_density: low
date: 2024-09-06
views: 213
transcript: auto-captions
confidence: medium
tags: [roblox, bubuthedev, youtube-learn]
creator_trust: TRUSTED
creator_score: 7.9
---

> [!note] Trust: TRUSTED (credibility audit score 7.9): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# DON’T do this mistake in your Roblox games!

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Watch](https://youtu.be/oYQ5jIZKE8s) | BubuTheDev | 213 views | 2024-09-06

## Summary
Short Roblox tutorial showing how to add a fade-out death effect: a server script that, on character death, tweens every BasePart (except Head) to transparency 1, fading face decal and accessories' handles, after a 0.25s delay. Mostly entertainment/tutorial, little strategy.

## Tips
- [0:00](https://youtu.be/oYQ5jIZKE8s?t=0) **[[vfx-and-particles]]** Use TweenService with TweenInfo on Humanoid.Died to fade character parts on death instead of the default instant reset, for a smoother feel.
- [2:45](https://youtu.be/oYQ5jIZKE8s?t=165) **[[scripting-and-performance]]** Add a short wait (about 0.25s) before the death fade so it doesn't play instantly on death.
- [0:00](https://youtu.be/oYQ5jIZKE8s?t=0) **[[scripting-and-performance]]** Cache a service-level local for character debugging: store Humanoid via character:FindFirstChildOfClass('Humanoid') and check it exists before connecting Died.

## Numbers
- [0:00](https://youtu.be/oYQ5jIZKE8s?t=0) Death fade delay: **0.25 s** (Wait before fade so it doesn't play immediately on death)

## Tools
Roblox Studio, Luau, TweenService

## Topics
[[scripting-and-performance]] [[vfx-and-particles]]

Back to [[BubuTheDev - How to make successful Roblox games]]
