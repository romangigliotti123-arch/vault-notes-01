---
title: "All about Entity Component System"
url: https://devforum.roblox.com/t/all-about-entity-component-system/1664447
creator: Roblox DevForum
official: false
advice_density: low
date: 2022-02-12
views: 193
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# All about Entity Component System

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://devforum.roblox.com/t/all-about-entity-component-system/1664447) | Roblox DevForum | 193 views | 2022-02-12

## Summary
Ukendio's developer-forum guide to Entity Component System (ECS) for Roblox, using the Matter library. Contrasts ECS with OOP inheritance (diamond problem, composition via components), then walks through a Matter example: world, components, spawning entities, querying, useDeltaTime, useEvent, and loop scheduling. Mentions Jecs as a faster alternative.

## Tips
- [page](https://devforum.roblox.com/t/all-about-entity-component-system/1664447) **[[code-architecture-and-frameworks]]** Prefer composition over deep inheritance: model behaviour as data components added to entities, so new behaviours (e.g. Fly, Float) combine without conflicting class hierarchies.
- [page](https://devforum.roblox.com/t/all-about-entity-component-system/1664447) **[[code-architecture-and-frameworks]]** In ECS, components hold pure data with no behaviour; systems hold self-contained logic that query specific component sets.
- [page](https://devforum.roblox.com/t/all-about-entity-component-system/1664447) **[[luau-language-and-types]]** Use Matter.useDeltaTime() when moving entities per frame so speed is frame-rate independent (speed * deltaTime, not speed per frame).
- [page](https://devforum.roblox.com/t/all-about-entity-component-system/1664447) **[[scripting-and-performance]]** Run ECS systems through Matter.Loop bound to a signal such as RunService.Heartbeat, scheduling all systems in one place.

## Numbers
- [page](https://devforum.roblox.com/t/all-about-entity-component-system/1664447) Example arrow speed: **50 studs per second (multiplied by delta time)** (Matter arrow example moves a Velocity speed value each frame)
- [page](https://devforum.roblox.com/t/all-about-entity-component-system/1664447) Example damage on contact: **5 damage per Touched hit** (Arrow hurts players via Humanoid:TakeDamage(5))

## Games
- **Overwatch**: Cited as an outer-industry game using ECS in some form.
- **Minecraft**: Cited as an outer-industry game using ECS in some form.
- **Hearthstone**: Cited as an outer-industry game using ECS in some form.

## Tools
Matter, Jecs, Anatta, Stitch

## Topics
[[code-architecture-and-frameworks]] [[luau-language-and-types]] [[scripting-and-performance]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
