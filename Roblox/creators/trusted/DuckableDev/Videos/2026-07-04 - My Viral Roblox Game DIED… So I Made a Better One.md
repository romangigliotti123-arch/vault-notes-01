---
title: "My Viral Roblox Game DIED… So I Made a Better One"
url: https://youtu.be/eRhFPgj8tc4
creator: Duckable
official: false
advice_density: low
date: 2026-07-04
views: 1211369
transcript: auto-captions
confidence: medium
tags: [roblox, duckabledev, youtube-learn]
creator_trust: TRUSTED
creator_score: 7.9
---

> [!note] Trust: TRUSTED (credibility audit score 7.9): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# My Viral Roblox Game DIED… So I Made a Better One

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Watch](https://youtu.be/eRhFPgj8tc4) | DuckableDev | 1,211,369 views | 2026-07-04

## Summary
Devlog of building Keycap RNG/Tycoon, a keyboard-themed Roblox RNG game inspired by Slime RNG. Covers rolling with a seeded RNG module, inventory, skill tree, rebirth sequence, mutation and shredder updates. Peaks at 569 CCU. Shows a $7,000-for-50% offer declined, and a DMCA threat over similar models.

## Tips
- [1:21](https://youtu.be/eRhFPgj8tc4?t=81) **[[core-loops-and-game-design]]** Copy proven loops from current top games (e.g. Slime RNG) and re-skin them; the creator switched from tycoon to RNG after seeing Slime RNG hit #1.
- [4:04](https://youtu.be/eRhFPgj8tc4?t=244) **[[scripting-and-performance]]** Don't use math.random alone for rolls; players can predict pseudo-random output. Seed from multiple entropy sources (time, IDs) and hash them, server-side.
- [11:33](https://youtu.be/eRhFPgj8tc4?t=693) **[[first-session-onboarding]]** Make key progression moments (rebirth) feel special with a dedicated animation sequence instead of an instant state change.
- [12:14](https://youtu.be/eRhFPgj8tc4?t=734) **[[building-art-and-assets]]** Fill empty maps early; a bare void map is an obvious flaw. Free nature asset packs can populate a map quickly.

## Numbers
- [15:03](https://youtu.be/eRhFPgj8tc4?t=903) Peak active players (first ~12 hours): **320, later 560**
- [26:01](https://youtu.be/eRhFPgj8tc4?t=1561) Final peak concurrent players after update: **569 (goal was 10,000)**
- [15:03](https://youtu.be/eRhFPgj8tc4?t=903) Offer from Preston for 50% of game: **$7,000 (declined)**
- [0:00](https://youtu.be/eRhFPgj8tc4?t=0) Previous game Steal a Duck peak: **thousands of CCU, millions of Robux; dropped to ~1/100 after a bug update**

## Games
- **Keycap RNG (Keycap Tycoon)** [0:40](https://youtu.be/eRhFPgj8tc4?t=40): Creator's keyboard game; started as a tycoon, pivoted to RNG after seeing Slime RNG's success.
- **Slime RNG** [2:42](https://youtu.be/eRhFPgj8tc4?t=162): Top game at the time; its upgrade tree and RNG loop inspired the creator's design.
- **Steal a Duck** [7:29](https://youtu.be/eRhFPgj8tc4?t=449): Creator's prior hit; a bad update cut player count to about 1/100th, a cautionary example.

## Tools
Pixel Forge (plugin for bulk-rendering models), Figma (UI mockups), R&D seeded RNG module (creator's hash-based random module)

## Topics
[[building-art-and-assets]] [[business-and-payouts]] [[common-mistakes]] [[core-loops-and-game-design]] [[first-session-onboarding]] [[mindset-and-strategy]] [[scripting-and-performance]] [[testing-debugging-and-qa]] [[updates-live-ops]]

Back to [[DuckableDev - How to make successful Roblox games]]
