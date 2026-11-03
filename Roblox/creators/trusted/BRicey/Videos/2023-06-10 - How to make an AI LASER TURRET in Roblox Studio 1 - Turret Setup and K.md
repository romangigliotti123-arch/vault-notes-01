---
title: "How to make an AI LASER TURRET in Roblox Studio #1 - Turret Setup and Kinematics"
url: https://youtu.be/BBoJiE4IkSg
creator: B Ricey
official: false
advice_density: medium
date: 2023-06-10
views: 17688
transcript: auto-captions
confidence: high
tags: [roblox, bricey, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.0
---

> [!note] Trust: TRUSTED (credibility audit score 8.0): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# How to make an AI LASER TURRET in Roblox Studio #1 - Turret Setup and Kinematics

[Watch](https://youtu.be/BBoJiE4IkSg) | BRicey | 17,688 views | 2023-06-10

## Summary
Part 1 of a two-part series building an AI laser turret in Roblox Studio. Covers model setup (anchored base, pivot alignment, welds), hinge constraints set to servo actuators, a sphere ref part for angle calculation, and scripting yaw/pitch aiming with RunService.Stepped, Vector3 angle and cross products, working in the turret's object space.

## Tips
- [1:37](https://youtu.be/BBoJiE4IkSg?t=97) **[[building-and-level-design]]** Anchor only the base; set all other parts to unanchored so constraints drive movement. Align the gun barrel exactly with the pitch pivot axis to avoid aiming inaccuracies.
- [4:30](https://youtu.be/BBoJiE4IkSg?t=270) **[[scripting-and-performance]]** Use HingeConstraints with ActuatorType Servo, high speed (~5) and very large MaxTorque (~50,000) so the turret moves properly under physics.
- [10:24](https://youtu.be/BBoJiE4IkSg?t=624) **[[scripting-and-performance]]** Create an invisible anchored reference part at the turret's rotation fulcrum; use its CFrame to convert world targets to local space so aiming works in any orientation.
- [12:46](https://youtu.be/BBoJiE4IkSg?t=766) **[[scripting-and-performance]]** Update hinge TargetAngle in RunService.Stepped (runs before physics each frame) so hinges are set before simulation.
- [14:47](https://youtu.be/BBoJiE4IkSg?t=887) **[[scripting-and-performance]]** Flatten the local direction by multiplying by Vector3.new(1,0,1) and use Vector3:Angle with the Y axis for signed 360-degree yaw; convert with math.deg.
- [18:44](https://youtu.be/BBoJiE4IkSg?t=1124) **[[scripting-and-performance]]** If aim is backwards or off by 90 degrees, flip the direction sign, negate the degrees, or swap the Z axis for X axis; debug yaw first, then pitch.
- [19:36](https://youtu.be/BBoJiE4IkSg?t=1176) **[[scripting-and-performance]]** For pitch, get a perpendicular axis via cross product of local Y axis and flat direction, then use Vector3:Angle against the flat direction to set pitch TargetAngle.

## Numbers
- [9:02](https://youtu.be/BBoJiE4IkSg?t=542) Servo MaxTorque: **50000** (Example torque value used for hinge servos in the turret model)
- [9:02](https://youtu.be/BBoJiE4IkSg?t=542) Servo Speed: **5** (Example servo speed set on the yaw and pitch hinges)

## Tools
Roblox Studio, HingeConstraint, RunService.Stepped, CFrame.PointToObjectSpace, Vector3:Angle

## He points to
- Speaker's hinge tutorial video
- Speaker's weld tutorial video
- Speaker's Vector3 angle video
- Speaker's CFrame object-space video
- Part 2 of the series (shooting and AI)

## Topics
[[building-and-level-design]] [[scripting-and-performance]]

Back to [[BRicey - How to make successful Roblox games]]
