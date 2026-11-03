---
title: "2 Joint 2 Limb Inverse Kinematics"
url: https://devforum.roblox.com/t/2-joint-2-limb-inverse-kinematics/252399
creator: Roblox DevForum
official: false
advice_density: medium
date: 2019-03-15
views: 262
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# 2 Joint 2 Limb Inverse Kinematics

[Open](https://devforum.roblox.com/t/2-joint-2-limb-inverse-kinematics/252399) | Roblox DevForum | 262 views | 2019-03-15

## Summary
Old (2019, marked outdated 2024) DevForum tutorial on 2-joint 2-limb inverse kinematics for Roblox using the law of cosines. Covers solving joint angles, applying them via C0 offsets or building limb parts, handling unreachable cases by pushing the shoulder back/forward, and a rolled base plane for natural shoulder motion. Includes a full solveIK function and demo file.

## Tips
- [page](https://devforum.roblox.com/t/2-joint-2-limb-inverse-kinematics/252399) **[[physics-pathfinding-and-npc-ai]]** Solve 2-joint IK with the law of cosines: c = distance shoulder-to-goal, then A and C angles from arm lengths a, b and c.
- [page](https://devforum.roblox.com/t/2-joint-2-limb-inverse-kinematics/252399) **[[physics-pathfinding-and-npc-ai]]** Clamp unreachable targets: if distance < |l1-l2|, push shoulder back and fold arm; if distance > l1+l2, push shoulder forward and fully extend.
- [page](https://devforum.roblox.com/t/2-joint-2-limb-inverse-kinematics/252399) **[[physics-pathfinding-and-npc-ai]]** Use a rolled base plane (axis from cross product of Vector3.new(0,0,-1) and goal direction) instead of CFrame.new(shoulder, goal) for natural shoulder/hip rotation.
- [page](https://devforum.roblox.com/t/2-joint-2-limb-inverse-kinematics/252399) **[[building-art-and-assets]]** Apply solved angles either as Motor6D/Weld C0 offsets or by positioning limb parts directly from the base plane CFrame.
- [page](https://devforum.roblox.com/t/2-joint-2-limb-inverse-kinematics/252399) **[[testing-debugging-and-qa]]** Turn off Accurate Play Solo or use Start Server when testing the jointless IK demo, otherwise results may differ.

## Numbers
- [page](https://devforum.roblox.com/t/2-joint-2-limb-inverse-kinematics/252399) Example arm lengths: **upper arm b=1.255, lower arm a=0.735 (tutorial example); demo uses 1.4 and 1.2** (Sample limb lengths used in the tutorial code)

## Games
- **Apocalypse Rising 2**: Author's shipped game; uses push-back/push-forward clamping for unreachable IK targets.

## Tools
Roblox Studio, Luau math library (math.acos, CFrame.fromAxisAngle)

## He points to
- Original DevForum reply thread by LMH_Hutch
- 2 Joint 2 Limb Inverse Kinematics Demo.rbxl

## Topics
[[building-art-and-assets]] [[physics-pathfinding-and-npc-ai]] [[testing-debugging-and-qa]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
