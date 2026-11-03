---
title: "How to Make Area Music in Roblox Studio in 2023! | Music by Region | Roblox Studio Tutorial"
url: https://youtu.be/KPK86YQ6t-Y
creator: Amora
official: false
advice_density: medium
date: 2023-07-31
views: 16690
transcript: auto-captions
confidence: high
tags: [roblox, amorascripting, youtube-learn]
creator_trust: MIXED
creator_score: 7.2
---

> [!note] Trust: MIXED (credibility audit score 7.2): do not rely on this creator alone; confirm a recommendation with a second source. See [[creator-credibility]].

# How to Make Area Music in Roblox Studio in 2023! | Music by Region | Roblox Studio Tutorial

[Watch](https://youtu.be/KPK86YQ6t-Y) | AmoraScripting | 16,690 views | 2023-07-31

## Summary
Tutorial on building region-based area music in Roblox Studio: invisible anchored parts define zones, a client-side script builds a Region3 from part position and size, uses GetPartBoundsInBox with a character-only OverlapParams filter, and plays or stops a Sound on RenderStepped depending on whether the player is inside.

## Tips
- [0:36](https://youtu.be/KPK86YQ6t-Y?t=36) **[[building-and-level-design]]** Make zone parts Anchored, CanCollide false, Transparency 1, and tall enough that players can't escape above them.
- [2:15](https://youtu.be/KPK86YQ6t-Y?t=135) **[[scripting-and-performance]]** Set a Script's Run Context to Client so it runs inside a part; regular LocalScripts only run in specific containers like backpack, character, PlayerGui, or PlayerScripts.
- [3:57](https://youtu.be/KPK86YQ6t-Y?t=237) **[[scripting-and-performance]]** Compute Region3 corners from part.Position ± part.Size/2 instead of placing manual corner parts.
- [6:21](https://youtu.be/KPK86YQ6t-Y?t=381) **[[scripting-and-performance]]** Use OverlapParams with FilterType Include and the character as the filter descendant so only the player's own parts are detected.
- [7:44](https://youtu.be/KPK86YQ6t-Y?t=464) **[[scripting-and-performance]]** Use workspace:GetPartBoundsInBox instead of the deprecated FindPartsInRegion3.
- [5:39](https://youtu.be/KPK86YQ6t-Y?t=339) **[[scripting-and-performance]]** Reset the inRegion flag each frame before the check so music stops if the player leaves the zone.
- [8:29](https://youtu.be/KPK86YQ6t-Y?t=509) **[[core-loops-and-game-design]]** Check music.IsPlaying before calling Play to avoid restarting the track every frame.

## Tools
Roblox Studio, Luau

## Topics
[[building-and-level-design]] [[core-loops-and-game-design]] [[scripting-and-performance]]

Back to [[AmoraScripting - How to make successful Roblox games]]
