---
title: "Cars With Suspension - Roblox Scripting Tutorial"
url: https://youtu.be/FVOowr2DXbM
creator: Suphi Kaner
official: false
advice_density: high
date: 2022-04-14
views: 114089
transcript: auto-captions
confidence: high
tags: [roblox, 5uphi, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.8
---

> [!note] Trust: TRUSTED (credibility audit score 8.8): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Cars With Suspension - Roblox Scripting Tutorial

[Watch](https://youtu.be/FVOowr2DXbM) | 5uphi | 114,089 views | 2022-04-14

## Summary
Scripting tutorial building a drivable car in Roblox: mesh body with mass tuning, cylindrical constraints for wheels with limits, spring suspension, collision groups, network ownership to the seated driver, motor-driven rear wheels, throttle/steer via seat float properties, tweened steering, and proximity-prompt entry/exit.

## Tips
- [2:47](https://youtu.be/FVOowr2DXbM?t=167) **[[building-and-level-design]]** Set body mass near 80 by lowering custom density (0.7 to 0.3 gave ~82 mass); the speaker says this works well as a starting point.
- [7:41](https://youtu.be/FVOowr2DXbM?t=461) **[[combat-and-gameplay-systems]]** Put wheels and body in separate collision groups and disable collision between them so wheels don't push into the chassis.
- [10:26](https://youtu.be/FVOowr2DXbM?t=626) **[[physics-pathfinding-and-npc-ai]]** Add upper and lower limits to cylindrical constraints; leave headroom (upper -1) so springs don't bottom out or invert.
- [14:04](https://youtu.be/FVOowr2DXbM?t=844) **[[physics-pathfinding-and-npc-ai]]** Starting spring values: damping 200, free length 2.8, stiffness 3500. Tune per car. Rear free length 3.2 when rear is heavier.
- [14:46](https://youtu.be/FVOowr2DXbM?t=886) **[[physics-pathfinding-and-npc-ai]]** Wheels: density 2, elasticity 0.2 to reduce bounce, friction 1.5 for grip; friction affects drift/slide.
- [19:33](https://youtu.be/FVOowr2DXbM?t=1173) **[[physics-pathfinding-and-npc-ai]]** Drive with cylindrical constraint angular actuator set to motor; angularVelocity sign controls direction, max torque controls force.
- [20:55](https://youtu.be/FVOowr2DXbM?t=1255) **[[physics-pathfinding-and-npc-ai]]** Use only rear motors for RWD; a rear max torque of 2000 acts as a handbrake when unpowered.
- [22:58](https://youtu.be/FVOowr2DXbM?t=1378) **[[client-server-and-remotes]]** Set seat part network owner to the driver on Seated to get responsive local control; warn that clients can then exploit, so clamp speed server-side.
- [27:11](https://youtu.be/FVOowr2DXbM?t=1631) **[[physics-pathfinding-and-npc-ai]]** Filter seated events by a unique seat name so the car script only runs for car seats.
- [33:28](https://youtu.be/FVOowr2DXbM?t=2008) **[[scripting-and-performance]]** Disconnect the seat.Changed connection when the driver exits, or handlers stack (each event fires once more per re-entry).
- [31:24](https://youtu.be/FVOowr2DXbM?t=1884) **[[cross-platform-and-console]]** Read SteerFloat and ThrottleFloat rather than raw keys: they give finer control for mobile D-pad and gamepad input.
- [39:42](https://youtu.be/FVOowr2DXbM?t=2382) **[[physics-pathfinding-and-npc-ai]]** motorMaxTorque cannot be negative; wrap throttle in math.abs and default to engine-brake torque when throttle is zero.
- [44:38](https://youtu.be/FVOowr2DXbM?t=2678) **[[physics-pathfinding-and-npc-ai]]** Cap top speed by computing angularVelocity = maxSpeed / wheel radius (Size.Y / 2) and multiplying by math.sign(throttle).
- [50:14](https://youtu.be/FVOowr2DXbM?t=3014) **[[ui-ux-design]]** Tween wheel orientation (about 0.4 s) instead of setting it instantly so steering looks smooth rather than snapping.
- [54:21](https://youtu.be/FVOowr2DXbM?t=3261) **[[physics-pathfinding-and-npc-ai]]** Place the seat low and centred, transparent with CanCollide/CanQuery/CanTouch off, to lower the centre of mass and reduce flipping.
- [55:01](https://youtu.be/FVOowr2DXbM?t=3301) **[[ui-ux-design]]** Use a ProximityPrompt on the seat with RequiresLineOfSight off, and disable it while occupied (watch Occupant changes).
- [59:54](https://youtu.be/FVOowr2DXbM?t=3594) **[[ui-ux-design]]** On exit, teleport the player to the highest Y-axis attachment on the seat so they don't land under a flipped car or fall into gaps.
- [1:06:53](https://youtu.be/FVOowr2DXbM?t=4013) **[[scripting-and-performance]]** Structure car logic as: sit script (prompt), network owner server script, and drive local script connected to Seated; rename scripts by role.

## Numbers
- [2:47](https://youtu.be/FVOowr2DXbM?t=167) Body mass: **~82 (density 0.3, from 192 at 0.7)** (Target car body mass used in the video)
- [14:04](https://youtu.be/FVOowr2DXbM?t=844) Spring stiffness / damping / free length: **3500 / 200 / 2.8 (rear free length 3.2)** (Starting suspension tuning values)
- [14:46](https://youtu.be/FVOowr2DXbM?t=886) Wheel density / elasticity / friction: **2 / 0.2 / 1.5** (Custom physical properties for wheels)
- [29:17](https://youtu.be/FVOowr2DXbM?t=1757) Rear handbrake motor max torque: **2000** (Unpowered rear wheels act as handbrake)
- [39:01](https://youtu.be/FVOowr2DXbM?t=2341) Drive motor max torque: **5000 (50000 shows wheelies)** (Seat Torque value used for drive)
- [46:05](https://youtu.be/FVOowr2DXbM?t=2765) Max speed demo: **25 studs/s, then 40 after change** (Speed cap computed from MaxSpeed / wheel radius)
- [50:14](https://youtu.be/FVOowr2DXbM?t=3014) Steering tween time: **0.4 s (from 1 s)** (Tween of front attachment orientation)
- [48:51](https://youtu.be/FVOowr2DXbM?t=2931) Turn speed: **30 degrees (default steer scale)** (Steer multiplier; 90 looked wrong)

## Tools
Roblox Studio, Toolbox, Collision Groups, Luau

## He points to
- Speaker's channel video 'Stop hackers/exploiters' (character speed-limit script)

## Topics
[[building-and-level-design]] [[client-server-and-remotes]] [[combat-and-gameplay-systems]] [[cross-platform-and-console]] [[physics-pathfinding-and-npc-ai]] [[scripting-and-performance]] [[ui-ux-design]]

Back to [[5uphi - How to make successful Roblox games]]
