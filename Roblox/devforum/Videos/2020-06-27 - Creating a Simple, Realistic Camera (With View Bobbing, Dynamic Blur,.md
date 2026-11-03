---
title: "Creating a Simple, Realistic Camera (With View Bobbing, Dynamic Blur, & Sprinting)"
url: https://devforum.roblox.com/t/creating-a-simple-realistic-camera-with-view-bobbing-dynamic-blur-sprinting/646943
creator: Roblox DevForum
official: false
advice_density: medium
date: 2020-06-27
views: 243
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Creating a Simple, Realistic Camera (With View Bobbing, Dynamic Blur, & Sprinting)

[Open](https://devforum.roblox.com/t/creating-a-simple-realistic-camera-with-view-bobbing-dynamic-blur-sprinting/646943) | Roblox DevForum | 243 views | 2020-06-27

## Summary
Tutorial building a first-person camera with view bobbing (quadratic Bézier path plus Perlin noise), dynamic blur from camera turn speed, and a sprint system with FOV and walkspeed tweens. Covers the math (lerp, Bézier, Perlin noise) and three LocalScripts.

## Tips
- [page](https://devforum.roblox.com/t/creating-a-simple-realistic-camera-with-view-bobbing-dynamic-blur-sprinting/646943) **[[player-psychology-and-game-feel]]** Keep camera effects subtle; bobbing shouldn't be a 10-stud difference, as extreme motion can make players leave the game.
- [page](https://devforum.roblox.com/t/creating-a-simple-realistic-camera-with-view-bobbing-dynamic-blur-sprinting/646943) **[[ui-ux-design]]** Add a settings menu to toggle each camera effect (bobbing, blur, sprint) on or off, since players have different preferences.
- [page](https://devforum.roblox.com/t/creating-a-simple-realistic-camera-with-view-bobbing-dynamic-blur-sprinting/646943) **[[player-psychology-and-game-feel]]** Camera bobbing is the hardest effect to tune; test with breaks, because over-attending to small bobbing makes it seem more noticeable.
- [page](https://devforum.roblox.com/t/creating-a-simple-realistic-camera-with-view-bobbing-dynamic-blur-sprinting/646943) **[[optimization-and-streaming]]** Use RenderStepped with a modulus counter (e.g. every 5th frame) for camera checks, and avoid math.sqrt by comparing dot products of vectors.
- [page](https://devforum.roblox.com/t/creating-a-simple-realistic-camera-with-view-bobbing-dynamic-blur-sprinting/646943) **[[scripting-and-performance]]** Use TweenInfo reverse and repeat flags instead of separate return tweens; this cut the bobbing script from ~156 lines to ~87.
- [page](https://devforum.roblox.com/t/creating-a-simple-realistic-camera-with-view-bobbing-dynamic-blur-sprinting/646943) **[[building-art-and-assets]]** Disable default footstep sounds and add custom footsteps synced to the bobbing, since default footsteps won't match the camera motion.
- [page](https://devforum.roblox.com/t/creating-a-simple-realistic-camera-with-view-bobbing-dynamic-blur-sprinting/646943) **[[common-mistakes]]** Don't allow sprinting backwards or sideways in first person; check MoveDirection against LookVector dot product and reset FOV/speed when out of range.
- [page](https://devforum.roblox.com/t/creating-a-simple-realistic-camera-with-view-bobbing-dynamic-blur-sprinting/646943) **[[core-loops-and-game-design]]** Best suited to horror, adventure and exploration games where immersion matters; less suited to third-person.

## Numbers
- [page](https://devforum.roblox.com/t/creating-a-simple-realistic-camera-with-view-bobbing-dynamic-blur-sprinting/646943) Blur allowed range before blur starts: **10 degrees (dot ≈ 0.98)** (Camera turn angle under which no blur is applied)
- [page](https://devforum.roblox.com/t/creating-a-simple-realistic-camera-with-view-bobbing-dynamic-blur-sprinting/646943) Blur tween duration: **0.25 s Sine InOut** (Dynamic blur fade in/out tween)
- [page](https://devforum.roblox.com/t/creating-a-simple-realistic-camera-with-view-bobbing-dynamic-blur-sprinting/646943) Blur max Size used in example: **25 (equation tops out below it)** (Blur Size property; kept modest to avoid overdoing it)
- [page](https://devforum.roblox.com/t/creating-a-simple-realistic-camera-with-view-bobbing-dynamic-blur-sprinting/646943) Blur update frequency: **every 5th RenderStepped frame** (Dampener value in modulus check)
- [page](https://devforum.roblox.com/t/creating-a-simple-realistic-camera-with-view-bobbing-dynamic-blur-sprinting/646943) Sprint allowed angle: **45 degrees** (Sprinting cancels if movement is outside this cone from LookVector)
- [page](https://devforum.roblox.com/t/creating-a-simple-realistic-camera-with-view-bobbing-dynamic-blur-sprinting/646943) Sprint FOV change: **70 to 100** (Normal FOV to sprint FOV, tweened over 0.5 s Sine Out)
- [page](https://devforum.roblox.com/t/creating-a-simple-realistic-camera-with-view-bobbing-dynamic-blur-sprinting/646943) Sprint walkspeed change: **+5 over default WalkSpeed** (Author notes slower speeds suit camera bobbing better)
- [page](https://devforum.roblox.com/t/creating-a-simple-realistic-camera-with-view-bobbing-dynamic-blur-sprinting/646943) Bob tween durations: **0.675 s walk, 0.5 s sprint** (Adjust manually to roughly match walk speed)
- [page](https://devforum.roblox.com/t/creating-a-simple-realistic-camera-with-view-bobbing-dynamic-blur-sprinting/646943) Bob camera offset: **0.25 studs** (Offset for point0/point2 of the Bézier bob path)

## Tools
TweenService, RunService.RenderStepped, math.noise (Perlin noise), UserInputService:IsKeyDown, Humanoid.CameraOffset, Quadratic Bézier curve in Luau

## He points to
- Roblox DevHub Bézier curve diagram
- Author's earlier tutorials on trigonometry and vector math

## Quotes
- [page](https://devforum.roblox.com/t/creating-a-simple-realistic-camera-with-view-bobbing-dynamic-blur-sprinting/646943) "The bobbing shouldn't be a 10 stud difference; that can easily cause players to leave your game."
- [page](https://devforum.roblox.com/t/creating-a-simple-realistic-camera-with-view-bobbing-dynamic-blur-sprinting/646943) "Use the dot product instead of magnitude to avoid unnecessary square root calculations, which are expensive."

## Topics
[[building-art-and-assets]] [[common-mistakes]] [[core-loops-and-game-design]] [[optimization-and-streaming]] [[player-psychology-and-game-feel]] [[scripting-and-performance]] [[ui-ux-design]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
