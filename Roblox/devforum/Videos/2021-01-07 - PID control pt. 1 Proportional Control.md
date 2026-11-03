---
title: "PID control pt. 1: Proportional Control"
url: https://devforum.roblox.com/t/pid-control-pt-1-proportional-control/968881
creator: Roblox DevForum
official: false
advice_density: medium
date: 2021-01-07
views: 138
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# PID control pt. 1: Proportional Control

[Open](https://devforum.roblox.com/t/pid-control-pt-1-proportional-control/968881) | Roblox DevForum | 138 views | 2021-01-07

## Summary
Part 1 of a PID control tutorial series for Roblox. Explains feedback loops, set point/process value/controller output terms, and the proportional controller formula CO = kP * e (e = SP - PV). Shows a rolling-ball example with a VectorForce and a GUI cursor-following demo, and notes P-only limits (overshoot and oscillation without dampening).

## Tips
- [page](https://devforum.roblox.com/t/pid-control-pt-1-proportional-control/968881) **[[core-loops-and-game-design]]** Use a P controller (CO = kP * error) to drive physics velocity smoothly instead of setting velocity directly; force falls to 0 as you approach target speed.
- [page](https://devforum.roblox.com/t/pid-control-pt-1-proportional-control/968881) **[[physics-pathfinding-and-npc-ai]]** For a rolling ball, apply VectorForce = kP * (desiredVelocity - currentVelocity) each frame; example uses kP=300 and top speed 30.
- [page](https://devforum.roblox.com/t/pid-control-pt-1-proportional-control/968881) **[[physics-pathfinding-and-npc-ai]]** P-only control overshoots and oscillates without dampening; add a D term (part 2) or rely on friction. Setting kP to 3000 on the ball example makes it yeet off.
- [page](https://devforum.roblox.com/t/pid-control-pt-1-proportional-control/968881) **[[scripting-and-performance]]** Write the controller as a generic function taking kP, set point and process value; it only needs subtraction and multiplication, so it works for numbers, Vector2, Vector3.

## Numbers
- [page](https://devforum.roblox.com/t/pid-control-pt-1-proportional-control/968881) kP (rolling ball example): **300** (Rolling ball P controller with top speed 30 studs/s)
- [page](https://devforum.roblox.com/t/pid-control-pt-1-proportional-control/968881) Top speed (rolling ball example): **30 studs/s** (Set point magnitude used in the P controller demo)
- [page](https://devforum.roblox.com/t/pid-control-pt-1-proportional-control/968881) Overshoot-prone kP: **3000** (Value the author says makes the ball overshoot without enough dampening)
- [page](https://devforum.roblox.com/t/pid-control-pt-1-proportional-control/968881) Initial constant force (before P control): **300 units** (Constant VectorForce teaser that felt sluggish and never stopped)

## Tools
Roblox Studio, Luau, RunService.RenderStepped, VectorForce

## He points to
- MatLab PID video (youtube wkfEZmsQqiA)
- Brian Douglas PID video series (youtube UR0hOmjaHp0)
- Wikipedia: Proportional-integral-derivative controller
- Wikipedia: Control loop
- BPS.Space DIY PID rocket videos

## Topics
[[core-loops-and-game-design]] [[physics-pathfinding-and-npc-ai]] [[scripting-and-performance]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
