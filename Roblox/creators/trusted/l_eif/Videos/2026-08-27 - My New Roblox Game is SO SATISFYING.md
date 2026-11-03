---
title: "My New Roblox Game is SO SATISFYING"
url: https://youtu.be/UhpaVrb5Imo
creator: Leif
official: false
advice_density: low
date: 2026-08-27
views: 72326
transcript: auto-captions
confidence: high
tags: [roblox, l_eif, youtube-learn]
creator_trust: TRUSTED
creator_score: 7.9
---

> [!note] Trust: TRUSTED (credibility audit score 7.9): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# My New Roblox Game is SO SATISFYING

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Watch](https://youtu.be/UhpaVrb5Imo) | l_eif | 72,326 views | 2026-08-27

## Summary
Devlog building a satisfying clicker: a spring-animated Blender button, coin/loot spawning with Bezier arcs, spatial-hash coin merging, combo UI, inventory with Clash Royale-style per-item upgrades, XP/leveling, equipping followers, and a per-button upgrade tree. Mostly build progress, little advice.

## Tips
- [3:35](https://youtu.be/UhpaVrb5Imo?t=215) **[[scripting-and-performance]]** Use a spatial hash grid to find nearby objects to merge instead of comparing every object's position to every other each frame; the speaker calls the brute-force way very inefficient.
- [0:41](https://youtu.be/UhpaVrb5Imo?t=41) **[[building-art-and-assets]]** Model a bottom-stroke with inverted normals in Blender to get a cheap black outline effect that reads well in game.
- [1:24](https://youtu.be/UhpaVrb5Imo?t=84) **[[building-art-and-assets]]** Use a depth-fade mesh with alpha fades to make a hole or pit look endless with little geometry.
- [1:38](https://youtu.be/UhpaVrb5Imo?t=98) **[[building-art-and-assets]]** Attach a spring to a clicked button (Ripple library) so spam clicks keep pushing it, making the press feel springy and satisfying.

## Numbers
- [6:45](https://youtu.be/UhpaVrb5Imo?t=405) Upgrade cost gating: **50 fish for first upgrade, 200 for next, 200 of an item per upgrade (planned)** (Clash Royale-style duplicate-based upgrade concept, not yet live)
- [4:17](https://youtu.be/UhpaVrb5Imo?t=257) Combo threshold and timeout: **Starts at 10+ rapid clicks; expires after 1 second without clicking** (Combo UI with flame GIF; loot scales with combo)
- [13:36](https://youtu.be/UhpaVrb5Imo?t=816) Impact freeze frame: **About 0.1 second** (Brief hit-stop on impact)

## Games
- **Unnamed clicker (in development)** [0:00](https://youtu.be/UhpaVrb5Imo?t=0): Inspired by a Loop Cap Twitter clip; the speaker says they won't copy it one-to-one and will add their own ideas.
- **Slime Rancher** [3:07](https://youtu.be/UhpaVrb5Imo?t=187): Used as a visual reference for an icon design in the middle of a coin icon.

## Tools
Blender, Roblox Studio, Ripple (spring animation library), Figma

## On screen
Contact sheet shows inventory UI with light-themed item cards, upgrade/equip buttons, item info popup (Fish Common, Apple Rare), a currency counter climbing from 0 to 9.00K, a coin/XP HUD, and a loot-box reveal (Cooler Thing, Something, Big Red). Item tags show rarity and level.

## Topics
[[building-art-and-assets]] [[core-loops-and-game-design]] [[scripting-and-performance]]

Back to [[l_eif - How to make successful Roblox games]]
