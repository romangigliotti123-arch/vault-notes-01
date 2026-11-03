---
title: PossiblePanda - Mindset & Process
creator: PossiblePanda
tags: [roblox, possiblepanda, theme]
creator_trust: TRUSTED
creator_score: 8.3
---

> [!note] Trust: TRUSTED (credibility audit score 8.3): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# PossiblePanda: Mindset & Process

All PossiblePanda tips on this theme, grouped by topic, oldest first. Cross-creator synthesis: see [[README]] in roblox-kb.

## [[analytics-metrics]]
- 2026-09-20 [5:58](https://youtu.be/KVmPyoOPmRI?t=358) Pass an economy analytics transaction type and item SKU when changing currency so economy flows get logged automatically. ([[2026-09-20 - Scribe Roblox Open Source Showcase 8|Scribe | Roblox Open Source Showcase #8]])

## [[development-process-and-speed]]
- 2025-11-05 [1:05](https://youtu.be/L-2GA_xX-SA?t=65) Install Iris by dropping the release .rbxm into ReplicatedStorage/packages, or add it via Wally to keep it updated. ([[2025-11-05 - Iris Roblox Open Source Showcase 2|Iris | Roblox Open Source Showcase #2]])
- 2025-11-07 [1:08](https://youtu.be/qo0x-Et5NPk?t=68) Install UI Labs from the Roblox marketplace to preview UI components without launching the game, speeding up UI iteration. ([[2025-11-07 - UILabs Roblox Open Source Showcase 3|UILabs | Roblox Open Source Showcase #3]])
- 2025-11-07 [8:11](https://youtu.be/qo0x-Et5NPk?t=491) Group stories into a storybook ModuleScript with name and storyRoots set to script so related components appear together. ([[2025-11-07 - UILabs Roblox Open Source Showcase 3|UILabs | Roblox Open Source Showcase #3]])

## [[common-mistakes]]
- 2025-11-04 [17:57](https://youtu.be/3e406QQHt7o?t=1077) The most common Fusion error is a stray or extra comma, or forgetting to return the instance from the component function. ([[2025-11-04 - Fusion 0.3 Roblox Open Source Showcase 1|Fusion 0.3 | Roblox Open Source Showcase #1]])

## [[testing-debugging-and-qa]]
- 2025-11-05 [3:49](https://youtu.be/L-2GA_xX-SA?t=229) Always call Iris.Init() once and Iris:End() after each window; without End, drawing overlaps and errors pile up. ([[2025-11-05 - Iris Roblox Open Source Showcase 2|Iris | Roblox Open Source Showcase #2]])
- 2025-11-05 [9:21](https://youtu.be/L-2GA_xX-SA?t=561) Iris button events are per-frame booleans: check Iris.Button(...).clicked() inside an if statement rather than connecting an event. ([[2025-11-05 - Iris Roblox Open Source Showcase 2|Iris | Roblox Open Source Showcase #2]])
- 2025-11-05 [11:00](https://youtu.be/L-2GA_xX-SA?t=660) Keep debug menus off by default and toggle with a key like F2 so players don't see them. ([[2025-11-05 - Iris Roblox Open Source Showcase 2|Iris | Roblox Open Source Showcase #2]])
- 2025-11-05 [13:59](https://youtu.be/L-2GA_xX-SA?t=839) Use Iris.State for input values and read them with :get(); passing the state directly returns the wrong value. ([[2025-11-05 - Iris Roblox Open Source Showcase 2|Iris | Roblox Open Source Showcase #2]])
- 2025-11-05 [6:15](https://youtu.be/L-2GA_xX-SA?t=375) Open Iris.ShowDemoWindow to browse every built-in widget before searching the docs. ([[2025-11-05 - Iris Roblox Open Source Showcase 2|Iris | Roblox Open Source Showcase #2]])
- 2026-01-27 [4:31](https://youtu.be/AOAh-4Q9ARw?t=271) Validate data entries with assert on required fields at startup so missing fields error before production rather than mid-game. ([[2026-01-27 - RegistryFactory Roblox Open Source Showcase 7|RegistryFactory | Roblox Open Source Showcase #7]])

Up: [[PossiblePanda - How to make successful Roblox games]]
