---
title: "Docs: characters / name-health-display"
url: https://create.roblox.com/docs/characters/name-health-display.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: characters / name-health-display

[Open](https://create.roblox.com/docs/characters/name-health-display.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on character name and health display. Covers Humanoid DisplayDistanceType (Viewer/Subject/None), HealthDisplayType (AlwaysOn/DisplayWhenDamaged/AlwaysOff), NameOcclusion modes, scripting examples for per-player name/health settings, and overriding DisplayName via TextService-filtered client input.

## Tips
- [page](https://create.roblox.com/docs/characters/name-health-display) **[[ui-ux-design]]** Set DisplayDistanceType to Subject when you need per-character control; Viewer is the lowest priority and ignored for humanoids set to Subject or None.
- [page](https://create.roblox.com/docs/characters/name-health-display) **[[ui-ux-design]]** Use DisplayWhenDamaged health display to show health bars only on damaged characters, reducing HUD clutter.
- [page](https://create.roblox.com/docs/characters/name-health-display) **[[common-mistakes]]** Name/health display requires the Humanoid to sit inside a Model with a BasePart named Head, both at the same hierarchy level; otherwise nothing shows.
- [page](https://create.roblox.com/docs/characters/name-health-display) **[[common-mistakes]]** Occlusion does not occur if the occluding part has Transparency above 0.99, or when hidden behind another character model.
- [page](https://create.roblox.com/docs/characters/name-health-display) **[[client-server-and-remotes]]** Assign custom player names on the server, never on the client; pass input via RemoteEvent and filter with TextService:FilterStringAsync before setting Humanoid.DisplayName.
- [page](https://create.roblox.com/docs/characters/name-health-display) **[[ui-ux-design]]** Team-colored names appear automatically in the team's TeamColor, which helps distinguish teammates from opponents.
- [page](https://create.roblox.com/docs/characters/name-health-display) **[[ui-ux-design]]** Use EnemyOcclusion so names are hidden only behind walls from opposing team members, keeping teammates' names visible.

## Numbers
- [page](https://create.roblox.com/docs/characters/name-health-display) Occlusion transparency threshold: **Occlusion skipped when occluder Transparency > 0.99** (Warning on NameOcclusion behaviour)
- [page](https://create.roblox.com/docs/characters/name-health-display) Example NameDisplayDistance: **20 studs** (Sample script setting name display range)
- [page](https://create.roblox.com/docs/characters/name-health-display) Example HealthDisplayDistance: **15 studs** (Sample script setting health bar range)

## Tools
Humanoid, TextService, RemoteEvent, Players

## He points to
- Roblox Creator Docs: Humanoid properties

## Topics
[[client-server-and-remotes]] [[common-mistakes]] [[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
