---
title: "Docs: education / build-it-play-it-island-of-move / adding-animations"
url: https://create.roblox.com/docs/education/build-it-play-it-island-of-move/adding-animations.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: education / build-it-play-it-island-of-move / adding-animations

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/education/build-it-play-it-island-of-move/adding-animations.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs tutorial on adding script-triggered animations: a TouchPartFolder of parts fires a LocalScript that calls a ModuleScript to load, play, and yield on an exported animation via its asset ID. Covers project setup, the code, and next-step links to the Animation overview and tween lessons.

## Tips
- [page](https://create.roblox.com/docs/education/build-it-play-it-island-of-move/adding-animations) **[[building-art-and-assets]]** Set animation priority to Action and Looped to false for one-shot celebration animations so they override idle/walk animations.
- [page](https://create.roblox.com/docs/education/build-it-play-it-island-of-move/adding-animations) **[[client-server-and-remotes]]** Trigger animations from events like Touched, purchases or level completion; the tutorial's approach is a LocalScript calling a ModuleScript.
- [page](https://create.roblox.com/docs/education/build-it-play-it-island-of-move/adding-animations) **[[optimization-and-streaming]]** Guard touch handlers with a canTouch flag so a part cannot re-trigger the animation while it is already playing.
- [page](https://create.roblox.com/docs/education/build-it-play-it-island-of-move/adding-animations) **[[3d-modeling-rigging-and-animation]]** Find an exported animation's asset ID in the Create page Animations section by copying the ID from the URL.

## Numbers
- [page](https://create.roblox.com/docs/education/build-it-play-it-island-of-move/adding-animations) Fade-in time for animation: **0.3 seconds** (ANIMATION_FADE passed to Play() in PlayerAnimationFeedback)

## Tools
Roblox Studio, Luau LocalScript and ModuleScript, Roblox Create page Animations section

## Topics
[[3d-modeling-rigging-and-animation]] [[building-art-and-assets]] [[client-server-and-remotes]] [[optimization-and-streaming]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
