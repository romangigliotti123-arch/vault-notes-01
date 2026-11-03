---
title: "Background Sound for Regions (GetPartBoundsInBox)"
url: https://youtu.be/c1jFXwmRtzI
creator: SimTek Game Development
official: false
advice_density: low
date: 2022-12-25
views: 3982
transcript: auto-captions
confidence: high
tags: [roblox, simtekgamedevelopment, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.2
---

> [!note] Trust: TRUSTED (credibility audit score 8.2): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Background Sound for Regions (GetPartBoundsInBox)

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Watch](https://youtu.be/c1jFXwmRtzI) | SimTekGameDevelopment | 3,982 views | 2022-12-25

## Summary
Tutorial on replacing Region3 with Workspace:GetPartBoundsInBox to detect when a player's character is inside colored region parts, then play a matching zone sound client-side and show the zone name in a GUI label. Covers sound setup, region parts, LocalScript logic and stopping sounds when leaving zones.

## Tips
- [2:06](https://youtu.be/c1jFXwmRtzI?t=126) **[[building-and-level-design]]** Use invisible-or-translucent Parts as zone triggers, grouped in a Regions folder, and name each region the same as its matching sound for simpler code.
- [8:28](https://youtu.be/c1jFXwmRtzI?t=508) **[[scripting-and-performance]]** Use Workspace:GetPartBoundsInBox instead of the deprecated Region3 API to find parts inside a box; pass nil for OverlapParams since they gave no optimisation benefit here.
- [9:50](https://youtu.be/c1jFXwmRtzI?t=590) **[[scripting-and-performance]]** Detect a player inside a region by checking if a part's parent name matches the player's character name, then break the loop early once found.
- [5:39](https://youtu.be/c1jFXwmRtzI?t=339) **[[sound-and-music]]** Run zone-based ambient audio from a LocalScript so each client hears only its own zone sounds.

## Tools
Roblox Studio, Toolbox audio

## Topics
[[building-and-level-design]] [[scripting-and-performance]] [[sound-and-music]]

Back to [[SimTekGameDevelopment - How to make successful Roblox games]]
