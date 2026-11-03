---
title: "Roblox How to use Atmosphere (Create Custom Lighting Zones) - Game Development Tutorial #10"
url: https://youtu.be/UYnn9JF8qCc
creator: Emancyphur
official: false
advice_density: medium
date: 2022-07-25
views: 42659
transcript: manual-subs
confidence: high
tags: [roblox, emancyphur, youtube-learn]
creator_trust: TRUSTED
creator_score: 7.6
---

> [!note] Trust: TRUSTED (credibility audit score 7.6): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Roblox How to use Atmosphere (Create Custom Lighting Zones) - Game Development Tutorial #10

[Watch](https://youtu.be/UYnn9JF8qCc) | Emancyphur | 42,659 views | 2022-07-25

## Summary
Tutorial on adding Atmosphere to Roblox Studio Lighting and using ForeverHD's ZonePlus module to create invisible zones that tween Atmosphere properties per area for entering/exiting players, via LocalScript with Attributes.

## Tips
- [0:00](https://youtu.be/UYnn9JF8qCc?t=0) **[[building-art-and-assets]]** Add a Skybox to Lighting before adding Atmosphere, otherwise Atmosphere won't work.
- [5:13](https://youtu.be/UYnn9JF8qCc?t=313) **[[building-and-level-design]]** For zone parts: Transparency 1, CanCollide off, Anchored on so players walk through invisibly and parts don't fall into the void.
- [5:54](https://youtu.be/UYnn9JF8qCc?t=354) **[[building-and-level-design]]** Store Atmosphere values as Attributes on zone containers, named exactly like Atmosphere properties, so a LocalScript can read them.
- [6:37](https://youtu.be/UYnn9JF8qCc?t=397) **[[building-and-level-design]]** Tune Atmosphere values in Lighting first, then copy the combination into zone Attributes once it looks right.
- [9:28](https://youtu.be/UYnn9JF8qCc?t=568) **[[scripting-and-performance]]** Bind zones to a group 'EnterOnlyOneZoneAtATime' to stop overlapping zones from fighting over Atmosphere changes.
- [10:52](https://youtu.be/UYnn9JF8qCc?t=652) **[[scripting-and-performance]]** Clean up zone connections on removal and disconnect/nil them so removed zones stop listening.
- [3:30](https://youtu.be/UYnn9JF8qCc?t=210) **[[scripting-and-performance]]** Run Atmosphere zone changes in a LocalScript for per-player visuals; server changes affect everyone.

## Numbers
- [0:47](https://youtu.be/UYnn9JF8qCc?t=47) Atmosphere Density: **0 to 1 scale** (Higher density reduces visibility of distant objects)
- [1:15](https://youtu.be/UYnn9JF8qCc?t=75) Atmosphere Haze: **0 to 10 scale** (Foggy mist, starts at horizon then covers sky)
- [1:51](https://youtu.be/UYnn9JF8qCc?t=111) Atmosphere Glare: **0 to 10 scale** (Needs Haze and Lighting Brightness above 0)

## Tools
Roblox Studio, ZonePlus module (ForeverHD), TweenService, Toolbox

## He points to
- ForeverHD ZonePlus module
- Video description Resources section

## Topics
[[building-and-level-design]] [[building-art-and-assets]] [[scripting-and-performance]]

Back to [[Emancyphur - How to make successful Roblox games]]
