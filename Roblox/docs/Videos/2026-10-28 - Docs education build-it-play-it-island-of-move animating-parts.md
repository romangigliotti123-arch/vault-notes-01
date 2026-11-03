---
title: "Docs: education / build-it-play-it-island-of-move / animating-parts"
url: https://create.roblox.com/docs/education/build-it-play-it-island-of-move/animating-parts.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: education / build-it-play-it-island-of-move / animating-parts

[Open](https://create.roblox.com/docs/education/build-it-play-it-island-of-move/animating-parts.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on animating parts with TweenService. Covers a click-to-press button tween (TweenMove script with ClickDetector), changing tween direction via CFrame offsets, adjusting TWEEN_TIME and TWEEN_MOVE_DISTANCE, and tweening rotation, scale, and color, including a MeshPart workaround.

## Tips
- [page](https://create.roblox.com/docs/education/build-it-play-it-island-of-move/animating-parts) **[[core-loops-and-game-design]]** Animate objects on interaction (press, hit, pet, pickup) to give players immediate feedback that their action did something.
- [page](https://create.roblox.com/docs/education/build-it-play-it-island-of-move/animating-parts) **[[client-server-and-remotes]]** Guard tweens with an inTween flag so a tweening object cannot be re-triggered mid-animation.
- [page](https://create.roblox.com/docs/education/build-it-play-it-island-of-move/animating-parts) **[[building-art-and-assets]]** For fully textured MeshParts, use a SpecialMesh and tween VertexColor, since the MeshPart texture overrides tinted Color.
- [page](https://create.roblox.com/docs/education/build-it-play-it-island-of-move/animating-parts) **[[building-art-and-assets]]** If a model has many parts, tween one part (e.g. the button) and parent the tween script to it rather than the whole model.
- [page](https://create.roblox.com/docs/education/build-it-play-it-island-of-move/animating-parts) **[[scripting-and-performance]]** Use TweenService with TweenInfo and Completed:Connect for state changes instead of manual per-frame loops.
- [page](https://create.roblox.com/docs/education/build-it-play-it-island-of-move/animating-parts) **[[player-psychology-and-game-feel]]** Use Exponential easing for pickups shrinking on touch and Quad for button presses to make motion feel distinct.

## Numbers
- [page](https://create.roblox.com/docs/education/build-it-play-it-island-of-move/animating-parts) TWEEN_TIME example (button): **0.15 s** (Button press tween duration in the TweenMove sample script)
- [page](https://create.roblox.com/docs/education/build-it-play-it-island-of-move/animating-parts) TWEEN_MOVE_DISTANCE example (button): **1.5 studs** (Button press distance in the TweenMove sample script)
- [page](https://create.roblox.com/docs/education/build-it-play-it-island-of-move/animating-parts) TWEEN_TIME example (rotation): **0.25 s** (Rotate-and-bounce creature tween with reverse and repeat count 1)
- [page](https://create.roblox.com/docs/education/build-it-play-it-island-of-move/animating-parts) TWEEN_ROT_ANGLES example: **-45 degrees** (Creature rotation tween angle; move distance 3 studs)
- [page](https://create.roblox.com/docs/education/build-it-play-it-island-of-move/animating-parts) Scale tween TWEEN_TIME example: **1 s** (Pickup shrink to Vector3.zero with Exponential easing)
- [page](https://create.roblox.com/docs/education/build-it-play-it-island-of-move/animating-parts) Color tween TWEEN_TIME example: **0.2 s** (Hit flash to RGB(255,0,50); destroyed after 3 hits)

## Tools
TweenService, TweenInfo, ClickDetector, SpecialMesh

## He points to
- Class.TweenService API page

## Topics
[[building-art-and-assets]] [[client-server-and-remotes]] [[core-loops-and-game-design]] [[player-psychology-and-game-feel]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
