---
title: "Making Your Game More Satisfying | Roblox Studio"
url: https://youtu.be/qMdRT1xf9GM
creator: Stewiepfing
official: false
advice_density: low
date: 2024-04-23
views: 5830
transcript: auto-captions
confidence: high
tags: [roblox, stewiepfing, youtube-learn]
creator_trust: TRUSTED
creator_score: 7.7
---

> [!note] Trust: TRUSTED (credibility audit score 7.7): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Making Your Game More Satisfying | Roblox Studio

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Watch](https://youtu.be/qMdRT1xf9GM) | stewiepfing | 5,830 views | 2024-04-23

## Summary
Tutorial building a currency-orb popup effect in Roblox Studio: an orb part with a BillboardGui/ImageLabel gold icon, a ModuleScript that clones orbs and launches them with LinearVelocity at random X/Z force, and a LocalScript that triggers the burst. Customizable force ranges, orb count, and a stagger wait.

## Tips
- [2:39](https://youtu.be/qMdRT1xf9GM?t=159) **[[building-art-and-assets]]** Use your own custom currency icon rather than default toolbox icons; the creator says custom is better.
- [9:24](https://youtu.be/qMdRT1xf9GM?t=564) **[[core-loops-and-game-design]]** Stagger orb spawns with a short task.wait (~0.15s) so currency pops out one at a time instead of all at once, which looks better.
- [8:42](https://youtu.be/qMdRT1xf9GM?t=522) **[[core-loops-and-game-design]]** Make collected-feedback orbs non-collidable and anchored after they settle so players can't get stuck touching them.
- [10:50](https://youtu.be/qMdRT1xf9GM?t=650) **[[scripting-and-performance]]** Spawn popup orbs on the client with a LocalScript so only the player sees them; setting the count too high can crash the game.

## Numbers
- [8:42](https://youtu.be/qMdRT1xf9GM?t=522) Wait before destroying attachment/linear velocity: **2 seconds** (Orb physics force applied then removed)
- [9:24](https://youtu.be/qMdRT1xf9GM?t=564) Stagger wait between orbs: **0.15 seconds** (Creates one-at-a-time popup effect)
- [10:50](https://youtu.be/qMdRT1xf9GM?t=650) Orb count in test: **3 then 5** (Demo amounts; higher counts may crash game)
- [10:50](https://youtu.be/qMdRT1xf9GM?t=650) Random X/Z force range: **-10 to 10 (final), -55 to 55 (initial)** (LinearVelocity Max Force 250)

## Games
- **Pet Simulator** [0:22](https://youtu.be/qMdRT1xf9GM?t=22): Referenced as an example of orb-style currency pickups that the creator's naming style mirrors.

## Tools
Roblox Studio, BillboardGui, LinearVelocity, ModuleScript

## Topics
[[building-art-and-assets]] [[core-loops-and-game-design]] [[scripting-and-performance]]

Back to [[stewiepfing - How to make successful Roblox games]]
