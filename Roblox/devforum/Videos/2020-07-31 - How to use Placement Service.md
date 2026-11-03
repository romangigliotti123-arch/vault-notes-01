---
title: "How to use Placement Service"
url: https://devforum.roblox.com/t/how-to-use-placement-service/698753
creator: Roblox DevForum
official: false
advice_density: medium
date: 2020-07-31
views: 282
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# How to use Placement Service

[Open](https://devforum.roblox.com/t/how-to-use-placement-service/698753) | Roblox DevForum | 282 views | 2020-07-31

## Summary
Official-style DevForum guide to Placement Service v1.6.2, a client-side placement kit for Roblox tycoons. Covers setup (plot, grid, remotes, server validation script), activate/requestPlacement calls, callbacks/signals, mobile UI handling, and a long list of configurable attributes. Notes the module is outdated and being overhauled.

## Tips
- [page](https://devforum.roblox.com/t/how-to-use-placement-service/698753) **[[building-and-level-design]]** Make plot size a multiple of grid size; otherwise placement emits a warning in the output.
- [page](https://devforum.roblox.com/t/how-to-use-placement-service/698753) **[[anti-exploit-and-security]]** Remove noPlotActivate() unless placement is intentionally plot-free, to prevent exploiters from using it.
- [page](https://devforum.roblox.com/t/how-to-use-placement-service/698753) **[[client-server-and-remotes]]** Validate placement on the server: the module runs client-side, so a server script must check bounds and collisions before placing.
- [page](https://devforum.roblox.com/t/how-to-use-placement-service/698753) **[[common-mistakes]]** Set PrimaryPart on models to a transparent hitbox part; without it collision and placement checks won't work correctly.
- [page](https://devforum.roblox.com/t/how-to-use-placement-service/698753) **[[ui-ux-design]]** On mobile, the module does not handle input; bind your own UI buttons to raise, lower, rotate, terminate and requestPlacement, detected via getPlatform() returning "Mobile".
- [page](https://devforum.roblox.com/t/how-to-use-placement-service/698753) **[[building-and-level-design]]** Set SmartDisplay to false unless grid size is under 5 studs, as the author recommends.
- [page](https://devforum.roblox.com/t/how-to-use-placement-service/698753) **[[scripting-and-performance]]** Leave TargetFPS at 60, as the author recommends.
- [page](https://devforum.roblox.com/t/how-to-use-placement-service/698753) **[[combat-and-gameplay-systems]]** Set CanTouch to false on parts that should be ignored by collision detection.
- [page](https://devforum.roblox.com/t/how-to-use-placement-service/698753) **[[development-process-and-speed]]** Expect breaking changes: the author warns every current feature may be deprecated or modified in later versions.

## Numbers
- [page](https://devforum.roblox.com/t/how-to-use-placement-service/698753) Current version: **1.6.2 (released 2023-05-24)** (Latest module version listed in the changelog)
- [page](https://devforum.roblox.com/t/how-to-use-placement-service/698753) Recommended TargetFPS: **60** (Author's recommended constant FPS target)
- [page](https://devforum.roblox.com/t/how-to-use-placement-service/698753) SmartDisplay recommendation: **Only if grid size < 5 studs** (Otherwise keep SmartDisplay false)
- [page](https://devforum.roblox.com/t/how-to-use-placement-service/698753) Lerp speed range: **0 = no interpolation, 0.9 = major** (LerpSpeed attribute range given by author)
- [page](https://devforum.roblox.com/t/how-to-use-placement-service/698753) Tilt range: **AngleTiltAmplitude 0 (min) to 10 (max)** (Tilt amount when moving)

## Tools
Placement Service (Roblox module v1.6.2), Roblox Studio, Luau

## He points to
- Official Placement Service GitHub repository
- Official Placement Service documentation
- Demo place (linked by author)

## Topics
[[anti-exploit-and-security]] [[building-and-level-design]] [[client-server-and-remotes]] [[combat-and-gameplay-systems]] [[common-mistakes]] [[development-process-and-speed]] [[scripting-and-performance]] [[ui-ux-design]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
