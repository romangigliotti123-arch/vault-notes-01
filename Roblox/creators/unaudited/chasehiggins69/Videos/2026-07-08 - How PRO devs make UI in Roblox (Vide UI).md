---
title: "How PRO devs make UI in Roblox (Vide UI)"
url: https://youtu.be/p86bt9ROQfk
creator: Chase Higgins
official: false
advice_density: medium
date: 2026-07-08
views: 16959
transcript: auto-captions
confidence: high
tags: [roblox, chasehiggins69, youtube-learn]
creator_trust: INSUFFICIENT
---

> [!note] Trust: UNAUDITED (fewer than 4 checkable claims verified): credibility unknown, treat as unverified, not as bad; confirm before relying. See [[creator-credibility]].

# How PRO devs make UI in Roblox (Vide UI)

[Watch](https://youtu.be/p86bt9ROQfk) | chasehiggins69 | 16,959 views | 2026-07-08

## Summary
Tutorial on using Vide (declarative UI library for Roblox/Luau). Covers Lua parentheses-less call syntax, setting up a Rojo/Wally project with Vide, mounting to PlayerGui, Vide.create, sources (state), effects, component props, Codify plugin export, and UI Labs for live UI editing.

## Tips
- [1:04](https://youtu.be/p86bt9ROQfk?t=64) **[[code-architecture-and-frameworks]]** Use Vide's parentheses-less call style (table/string literal args) only if your team accepts it; StyLua in VS Code will force parentheses anyway.
- [3:26](https://youtu.be/p86bt9ROQfk?t=206) **[[version-control-and-tooling]]** Install Vide via Wally (search on wally.run), then ensure packages are listed in default.project.json before running rojo serve.
- [5:39](https://youtu.be/p86bt9ROQfk?t=339) **[[building-art-and-assets]]** Mount declarative UI to Players.LocalPlayer.PlayerGui from a client script so the root ScreenGui is created on the client.
- [6:23](https://youtu.be/p86bt9ROQfk?t=383) **[[building-art-and-assets]]** Use the Codify plugin to export a Studio-built UI frame into Vide code in one click, then iterate in code.
- [8:17](https://youtu.be/p86bt9ROQfk?t=497) **[[ui-ux-design]]** Bind text properties to sources (state) so only the affected property updates instead of rebuilding the whole element on change.
- [9:11](https://youtu.be/p86bt9ROQfk?t=551) **[[ui-ux-design]]** Use bind.effect to run side effects (prints, animations like Ripple) automatically whenever a source changes, instead of wiring them into click handlers.
- [10:07](https://youtu.be/p86bt9ROQfk?t=607) **[[code-architecture-and-frameworks]]** Define a typed Props table for each component (position, color, increment) and pass values in from the parent app to make components reusable.
- [11:41](https://youtu.be/p86bt9ROQfk?t=701) **[[testing-debugging-and-qa]]** Use UI Labs with a *.story.lua file returning a Vide story table to edit component props live without restarting the game.

## Tools
Vide, Rojo, Wally, Rokit, Codify plugin, UI Labs, StyLua, Ripple

## He points to
- wally.run
- Vide Lua design guidelines document (linked in description)

## Topics
[[building-art-and-assets]] [[code-architecture-and-frameworks]] [[testing-debugging-and-qa]] [[ui-ux-design]] [[version-control-and-tooling]]

Back to [[chasehiggins69 - How to make successful Roblox games]]
