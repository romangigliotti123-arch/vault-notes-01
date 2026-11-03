---
title: "Iris | Roblox Open Source Showcase #2"
url: https://youtu.be/L-2GA_xX-SA
creator: Possible Panda
official: false
advice_density: low
date: 2025-11-05
views: 8156
transcript: auto-captions
confidence: high
tags: [roblox, possiblepanda, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.3
---

> [!note] Trust: TRUSTED (credibility audit score 8.3): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Iris | Roblox Open Source Showcase #2

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Watch](https://youtu.be/L-2GA_xX-SA) | PossiblePanda | 8,156 views | 2025-11-05

## Summary
Tutorial on Iris, an immediate-mode GUI debugging library for Roblox (a Roblox-internal-style tool). Covers installing via GitHub releases or Wally, setting up Iris.Connect/Init/End, creating windows, text, buttons, input text with states, toggling the debug menu with F2, and showing live FPS.

## Tips
- [1:05](https://youtu.be/L-2GA_xX-SA?t=65) **[[development-process-and-speed]]** Install Iris by dropping the release .rbxm into ReplicatedStorage/packages, or add it via Wally to keep it updated.
- [3:49](https://youtu.be/L-2GA_xX-SA?t=229) **[[testing-debugging-and-qa]]** Always call Iris.Init() once and Iris:End() after each window; without End, drawing overlaps and errors pile up.
- [9:21](https://youtu.be/L-2GA_xX-SA?t=561) **[[testing-debugging-and-qa]]** Iris button events are per-frame booleans: check Iris.Button(...).clicked() inside an if statement rather than connecting an event.
- [11:00](https://youtu.be/L-2GA_xX-SA?t=660) **[[testing-debugging-and-qa]]** Keep debug menus off by default and toggle with a key like F2 so players don't see them.

## Tools
Iris (immediate mode GUI library), Wally, Roblox Studio, UserInputService

## Topics
[[development-process-and-speed]] [[testing-debugging-and-qa]]

Back to [[PossiblePanda - How to make successful Roblox games]]
