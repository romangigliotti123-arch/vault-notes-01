---
title: "Creating A Circular/Radial HP Bar Like Kingdom Hearts"
url: https://devforum.roblox.com/t/creating-a-circularradial-hp-bar-like-kingdom-hearts/420996
creator: Roblox DevForum
official: false
advice_density: medium
date: 2019-12-31
views: 191
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Creating A Circular/Radial HP Bar Like Kingdom Hearts

[Open](https://devforum.roblox.com/t/creating-a-circularradial-hp-bar-like-kingdom-hearts/420996) | Roblox DevForum | 191 views | 2019-12-31

## Summary
Tutorial on building a circular/radial Kingdom Hearts-style HP bar in Roblox using UIGradient with rotation and transparency NumberSequence tricks, plus Luau code that maps health to three corner pieces and a horizontal overflow bar. Notes UIGradient was beta and linear-only at the time.

## Tips
- [page](https://devforum.roblox.com/t/creating-a-circularradial-hp-bar-like-kingdom-hearts/420996) **[[ui-ux-design]]** Build a radial bar from corner pieces: use one 500x500 TopLeft piece rotated via UIGradient for three quarters, mapping health to 1/3 segments.
- [page](https://devforum.roblox.com/t/creating-a-circularradial-hp-bar-like-kingdom-hearts/420996) **[[ui-ux-design]]** Use NumberSequence keypoints 0.001 apart; equal times can be ordered randomly, so offset the fill edge to avoid errors.
- [page](https://devforum.roblox.com/t/creating-a-circularradial-hp-bar-like-kingdom-hearts/420996) **[[ui-ux-design]]** Reposition keypoints when rotating a UIGradient, since rotation skews the edges of the frame; scale keypoints to match the rotation angle.
- [page](https://devforum.roblox.com/t/creating-a-circularradial-hp-bar-like-kingdom-hearts/420996) **[[scripting-and-performance]]** Put the bar math in a function (CurvedBarResize) and reuse it per segment instead of duplicating code for each corner.

## Numbers
- [page](https://devforum.roblox.com/t/creating-a-circularradial-hp-bar-like-kingdom-hearts/420996) Corner image size: **500x500 px; thickness 120 px (0.12 scale in a 1:1 frame)** (Three combined corners form a 1000x1000 image)
- [page](https://devforum.roblox.com/t/creating-a-circularradial-hp-bar-like-kingdom-hearts/420996) Health per corner segment: **circleMaxHealth / 3 (33.333 at max 100)** (Example uses circleMaxHealth = 100)
- [page](https://devforum.roblox.com/t/creating-a-circularradial-hp-bar-like-kingdom-hearts/420996) Keypoint gap: **0.001** (Separation between NumberSequence keypoints to avoid random ordering)
- [page](https://devforum.roblox.com/t/creating-a-circularradial-hp-bar-like-kingdom-hearts/420996) Rotation range per corner: **0 to -90 degrees** (UIGradient rotation mapped from alpha: -90 * (1 - alpha))

## Games
- **Kingdom Hearts Circular/Radial HP Bar (demo place)**: Uncopylocked example place showing the full radial HP bar implementation for reference.

## Tools
Roblox Studio, UIGradient, NumberSequence

## He points to
- UIGradient [LIVE] - #147 by UIScript (DevForum)

## Topics
[[scripting-and-performance]] [[ui-ux-design]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
