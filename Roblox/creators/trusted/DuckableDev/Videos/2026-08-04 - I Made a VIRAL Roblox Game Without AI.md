---
title: "I Made a VIRAL Roblox Game Without AI"
url: https://youtu.be/Cc7HT3uNjeQ
creator: Duckable
official: false
advice_density: low
date: 2026-08-04
views: 570179
transcript: auto-captions
confidence: medium
tags: [roblox, duckabledev, youtube-learn]
creator_trust: TRUSTED
creator_score: 7.9
---

> [!note] Trust: TRUSTED (credibility audit score 7.9): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# I Made a VIRAL Roblox Game Without AI

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Watch](https://youtu.be/Cc7HT3uNjeQ) | DuckableDev | 570,179 views | 2026-08-04

## Summary
Creator attempts a 9-day, no-AI challenge to build a smoothie tower tycoon on stream. Covers building plot/tower/dropper/button/merge/blender/crate/customer-queue systems in Luau, struggles with debugging, and reflections on AI use. Mostly devlog and entertainment, with few transferable best practices.

## Tips
- [1:15](https://youtu.be/Cc7HT3uNjeQ?t=75) **[[development-process-and-speed]]** Break the game into discrete 'sauce' milestones (plot, tower, droppers, buttons, merge, blender, customers) and finish each before starting the next.
- [5:41](https://youtu.be/Cc7HT3uNjeQ?t=341) **[[code-architecture-and-frameworks]]** Use inheritance for repeated UI buttons: a base button class with subclasses (spawn, merge) instead of copy-pasting code.
- [6:22](https://youtu.be/Cc7HT3uNjeQ?t=382) **[[code-architecture-and-frameworks]]** Put reusable effects like tween/ripple/color flash into a ModuleScript so any button or system can call them.
- [8:46](https://youtu.be/Cc7HT3uNjeQ?t=526) **[[scripting-and-performance]]** When merge logic fails, check for stale references: deleted droppers may still be indexed by old lookups, causing wrong merge results.

## Numbers
- [0:00](https://youtu.be/Cc7HT3uNjeQ?t=0) Challenge duration: **9 days of streaming** (Building the full game from scratch without AI)
- [19:59](https://youtu.be/Cc7HT3uNjeQ?t=1199) Customer queue debugging: **About 3 hours** (Final customer queue system before players spawned)
- [22:02](https://youtu.be/Cc7HT3uNjeQ?t=1322) Thumbnail CTR claimed: **10%** (Creator's self-made thumbnail, cited as a benchmark)
- [8:46](https://youtu.be/Cc7HT3uNjeQ?t=526) Coding time for an error: **About 8 minutes** (Dropper spawn system issue, described as taking eight minutes to solve)

## Games
- **Pickaxe Tycoon** [0:34](https://youtu.be/Cc7HT3uNjeQ?t=34): Cited as a recent tower tycoon hit; drop-collect-merge loop is the template for the creator's smoothie tycoon.
- **Chicken Farm** [0:34](https://youtu.be/Cc7HT3uNjeQ?t=34): Cited as a recent tower tycoon hit using the same drop-collect-merge loop.
- **Islands** [3:33](https://youtu.be/Cc7HT3uNjeQ?t=213): Creator borrowed the idea of totems that spawn crops around nearby farmland for a dropper design.

## Tools
Roblox Studio, Luau, Claude (AI, used earlier and avoided in challenge), Google search (AI overview used once)

## Topics
[[ai-and-tools]] [[code-architecture-and-frameworks]] [[common-mistakes]] [[core-loops-and-game-design]] [[development-process-and-speed]] [[scripting-and-performance]]

Back to [[DuckableDev - How to make successful Roblox games]]
