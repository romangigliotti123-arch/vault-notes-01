---
title: "Modeling a projectile's motion"
url: https://devforum.roblox.com/t/modeling-a-projectiles-motion/176677
creator: Roblox DevForum
official: false
advice_density: low
date: 2018-09-07
views: 1193
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Modeling a projectile's motion

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://devforum.roblox.com/t/modeling-a-projectiles-motion/176677) | Roblox DevForum | 1,193 views | 2018-09-07

## Summary
EgoMoose's guide derives projectile motion equations (position as a function of time, v0 and x0), applies them to basketball aiming, jump height/power, and draws projectile arcs using cubic Bezier Beams. Code-heavy technical tutorial for Roblox scripting.

## Tips
- [page](https://devforum.roblox.com/t/modeling-a-projectiles-motion/176677) **[[scripting-and-performance]]** Use x(t) = 0.5*g*t^2 + v0*t + x0 to compute launch velocity v0 = (target - x0 - 0.5*g*t^2)/t for a chosen flight time t.
- [page](https://devforum.roblox.com/t/modeling-a-projectiles-motion/176677) **[[core-loops-and-game-design]]** Set Velocity on a cloned physics part for collision-accurate projectiles; use CFrame stepping on RenderStepped if collisions don't matter.
- [page](https://devforum.roblox.com/t/modeling-a-projectiles-motion/176677) **[[physics-pathfinding-and-npc-ai]]** Humanoid.JumpPower acts as initial velocity: jump height h = JumpPower^2/(2*g), airtime = 2*JumpPower/g; JumpPower = sqrt(2*g*h) for a target height.
- [page](https://devforum.roblox.com/t/modeling-a-projectiles-motion/176677) **[[vfx-and-particles]]** Draw projectile arc previews with a Beam using two Attachments; cubic Bezier points derive from x0, v0 and flight time, and CurveSize0/1 set handle lengths.

## Numbers
- [page](https://devforum.roblox.com/t/modeling-a-projectiles-motion/176677) Example jump height: **10 studs (JumpPower = sqrt(2*g*10))** (Example used to set jump height via JumpPower)
- [page](https://devforum.roblox.com/t/modeling-a-projectiles-motion/176677) Example flight time: **t = 1 second** (Basketball throw example uses t = 1)

## Tools
Beam, Attachment, RunService.RenderStepped, Humanoid.JumpPower

## Topics
[[core-loops-and-game-design]] [[physics-pathfinding-and-npc-ai]] [[scripting-and-performance]] [[ui-ux-design]] [[vfx-and-particles]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
