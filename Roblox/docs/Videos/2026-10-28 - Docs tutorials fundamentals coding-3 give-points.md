---
title: "Docs: tutorials / fundamentals / coding-3 / give-points"
url: https://create.roblox.com/docs/tutorials/fundamentals/coding-3/give-points.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: tutorials / fundamentals / coding-3 / give-points

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/tutorials/fundamentals/coding-3/give-points.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs tutorial building a color-changing PointPart that awards or subtracts leaderstats points on touch (blue small, green large, red lose), then destroys itself and shows a particle effect. Covers Players service, Touched events, while-true color loop, if/elseif/else, and ParticleEmitter feedback.

## Tips
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-3/give-points) **[[first-session-onboarding]]** Give players immediate visible feedback on interactions (particles, sounds, shakes) so they notice rewards without checking the leaderboard.
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-3/give-points) **[[core-loops-and-game-design]]** Store repeated values like colors and point amounts in variables at the top of the script so they are easy to reuse and tune.
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-3/give-points) **[[scripting-and-performance]]** Put while-true loops at the bottom of a script; code below an infinite loop never runs.
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-3/give-points) **[[scripting-and-performance]]** Use player:WaitForChild on leaderstats and child values rather than assuming they exist when the Touched event fires.

## Numbers
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-3/give-points) Point values: **smallPoints 10, largePoints 50, losePoints 100** (Tutorial example values for blue, green, red parts)
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-3/give-points) Color loop timings: **blue 4s, green 3s, red 2s waits** (Final script while-true loop wait durations)
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-3/give-points) Particle lifetime: **1 second** (ParticleEmitter destroyed after task.wait(1))

## Tools
Roblox Studio, Luau, ServerScriptService, ParticleEmitter

## Topics
[[client-server-and-remotes]] [[core-loops-and-game-design]] [[data-persistence]] [[first-session-onboarding]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
