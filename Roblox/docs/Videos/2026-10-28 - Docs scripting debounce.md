---
title: "Docs: scripting / debounce"
url: https://create.roblox.com/docs/scripting/debounce.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: scripting / debounce

[Open](https://create.roblox.com/docs/scripting/debounce.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on debounce patterns in Luau. Covers debouncing Touched damage traps with an attribute and task.wait cooldown, preventing sound overlap by checking Sound.IsPlaying on Touched and Activated, and cooldown-based pickups that refresh after a delay with transparency feedback.

## Tips
- [page](https://create.roblox.com/docs/scripting/debounce) **[[scripting-and-performance]]** Debounce Touched events: Touched fires multiple times in quick succession from subtle physical contacts. Guard damage with a state flag so one contact deals damage once.
- [page](https://create.roblox.com/docs/scripting/debounce) **[[scripting-and-performance]]** Store debounce state in an instance attribute (e.g. SetAttribute('Touched', true)) and reset it after a cooldown with task.wait.
- [page](https://create.roblox.com/docs/scripting/debounce) **[[scripting-and-performance]]** Before calling Sound:Play() on Touched or Activated, check `not sound.IsPlaying` to avoid overlapping restarts of the same sound.
- [page](https://create.roblox.com/docs/scripting/debounce) **[[scripting-and-performance]]** For reusable pickups, use a CoolingDown attribute and a cooldown timer, and show the cooldown state visually, e.g. lowering Transparency to 0.75 while cooling down.
- [page](https://create.roblox.com/docs/scripting/debounce) **[[genre-mechanics]]** Apply the same cooldown pattern to weapon limits, such as a rocket launcher reload time, to cap how often players can fire.

## Numbers
- [page](https://create.roblox.com/docs/scripting/debounce) Trap damage: **10 damage per debounced contact, 1 s reset (RESET_TIME = 1)**
- [page](https://create.roblox.com/docs/scripting/debounce) Pickup heal: **+25 health, 5 s COOLDOWN_TIME, transparency 0.75 during cooldown**

## Tools
Luau, Roblox Studio, Instance attributes, task.wait

## He points to
- Roblox Creator Docs: Debounce patterns

## Topics
[[genre-mechanics]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
