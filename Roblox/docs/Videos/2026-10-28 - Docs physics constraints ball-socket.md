---
title: "Docs: physics / constraints / ball-socket"
url: https://create.roblox.com/docs/physics/constraints/ball-socket.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: physics / constraints / ball-socket

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/physics/constraints/ball-socket.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox engine docs for BallSocketConstraint: how it locks two attachments together while allowing free rotation, and how to restrict tilt (cone via UpperAngle) and twist (TwistLowerAngle/TwistUpperAngle) using LimitsEnabled and TwistLimitsEnabled, plus Restitution and attachment Axis alignment.

## Tips
- [page](https://create.roblox.com/docs/physics/constraints/ball-socket) **[[physics-pathfinding-and-npc-ai]]** Enable LimitsEnabled to expose UpperAngle for tilt limiting within a cone; enable TwistLimitsEnabled to restrict twist via TwistLowerAngle and TwistUpperAngle.
- [page](https://create.roblox.com/docs/physics/constraints/ball-socket) **[[physics-pathfinding-and-npc-ai]]** With LimitsEnabled on, point each attachment's Axis in the same direction so rotation occurs around the intended axis.
- [page](https://create.roblox.com/docs/physics/constraints/ball-socket) **[[physics-pathfinding-and-npc-ai]]** Restitution (exposed when LimitsEnabled is on) sets how elastic the attachments are when they hit tilt or twist limits.

## Numbers
- [page](https://create.roblox.com/docs/physics/constraints/ball-socket) UpperAngle example: **15** (Tilt cone limit example value in docs)
- [page](https://create.roblox.com/docs/physics/constraints/ball-socket) TwistLowerAngle example: **-60** (Twist limit example with TwistUpperAngle set to 0)
- [page](https://create.roblox.com/docs/physics/constraints/ball-socket) TwistUpperAngle example: **0** (Twist limit example paired with TwistLowerAngle -60)

## Tools
BallSocketConstraint, Attachment

## Topics
[[physics-pathfinding-and-npc-ai]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
