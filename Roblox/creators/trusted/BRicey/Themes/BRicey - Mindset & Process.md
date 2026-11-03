---
title: BRicey - Mindset & Process
creator: BRicey
tags: [roblox, bricey, theme]
creator_trust: TRUSTED
creator_score: 8.0
---

> [!note] Trust: TRUSTED (credibility audit score 8.0): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# BRicey: Mindset & Process

All BRicey tips on this theme, grouped by topic, oldest first. Cross-creator synthesis: see [[README]] in roblox-kb.

## [[development-process-and-speed]]
- 2021-01-17 [1:14](https://youtu.be/7BSYIEdo6E4?t=74) Attributes were in beta in Jan 2021; enable them under File > Beta Features before use. ([[2021-01-17 - How to use Attributes to create CUSTOM properties in Roblox Studio|How to use Attributes to create CUSTOM properties ]])
- 2021-01-17 [15:47](https://youtu.be/7BSYIEdo6E4?t=947) Run one-off setup such as JSON-encoding table attributes from the command bar so values are baked in before runtime. ([[2021-01-17 - How to use Attributes to create CUSTOM properties in Roblox Studio|How to use Attributes to create CUSTOM properties ]])
- 2022-09-23 [3:26](https://youtu.be/MyK4o2pIpQw?t=206) Only build what you need now (YAGNI); don't architect the full game upfront since ideas change during development. ([[2022-09-23 - How to Organize & Style your Code in Roblox Development (and when to u|How to Organize & Style your Code in Roblox Develo]])
- 2022-09-23 [4:06](https://youtu.be/MyK4o2pIpQw?t=246) Refactor freely; it costs less time than guessing a perfect structure up front. Fail fast like SpaceX rather than designing like NASA SLS. ([[2022-09-23 - How to Organize & Style your Code in Roblox Development (and when to u|How to Organize & Style your Code in Roblox Develo]])
- 2022-09-23 [17:05](https://youtu.be/MyK4o2pIpQw?t=1025) Release a game that mostly works and players enjoy; a perfect codebase that never ships earns nothing. ([[2022-09-23 - How to Organize & Style your Code in Roblox Development (and when to u|How to Organize & Style your Code in Roblox Develo]])
- 2024-02-17 [2:48](https://youtu.be/FaEMgVDlaNQ?t=168) Keep the server script thin and push logic into single-purpose ModuleScripts (PlotManager, PlotSpawnPool, ClientPlacer) for readability and expandability. ([[2024-02-17 - How to create a Plot Placement System in Roblox 1 - Plots & Players|How to create a Plot Placement System in Roblox #1]])
- 2024-02-17 [21:52](https://youtu.be/FaEMgVDlaNQ?t=1312) Create and destroy a fresh client object on each toggle for a clean state instead of managing persistent flags. ([[2024-02-17 - How to create a Plot Placement System in Roblox 1 - Plots & Players|How to create a Plot Placement System in Roblox #1]])
- 2024-03-02 [22:17](https://youtu.be/SVBmZ3yIMRo?t=1337) Always clean up in the destroy path (unbind render step and input actions) or the build tool leaks behaviour after toggling off. ([[2024-03-02 - How to create a Plot Placement System in Roblox 2 - Placing stuff!|How to create a Plot Placement System in Roblox #2]])

## [[common-mistakes]]
- 2021-06-12 [0:00](https://youtu.be/Vi2FckNJv9w?t=0) Avoid putting a separate copy of a script inside every part; editing behaviour then means editing each copy. Centralize logic instead. ([[2021-06-12 - Organizing your Game with Tags and CollectionService - Roblox Studio|Organizing your Game with Tags and CollectionServi]])
- 2022-04-16 [11:11](https://youtu.be/TmiU5CY6BW0?t=671) A gamepass you created is auto-owned by you, so testing shows an 'already own' prompt; test with a separate account or expect that message. ([[2022-04-16 - How to make a Tycoon in Roblox 11 - Gamepasses|How to make a Tycoon in Roblox #11 - Gamepasses]])
- 2022-05-28 [10:07](https://youtu.be/T0xqkYODIl0?t=607) Assert that the badge ID attribute exists on each tagged part so a forgotten attribute gives a clear error instead of a confusing one. ([[2022-05-28 - How to use Badges in Roblox! (Plus some scripting tips)|How to use Badges in Roblox! (Plus some scripting ]])
- 2022-09-23 [16:33](https://youtu.be/MyK4o2pIpQw?t=993) Comment why you are doing something, not what the code does; skip comments when a solo codebase is self-explanatory. ([[2022-09-23 - How to Organize & Style your Code in Roblox Development (and when to u|How to Organize & Style your Code in Roblox Develo]])
- 2023-04-14 [0:43](https://youtu.be/jaitqSU2HIA?t=43) Don't scale AI behaviour with isolated if-statements; model behaviours as explicit states and transitions in a diagram first. ([[2023-04-14 - Creating an Intelligent Delivery Drone with Finite State Machines 1 -|Creating an Intelligent Delivery Drone with Finite]])

## [[mindset-and-strategy]]
- 2021-01-04 [18:42](https://youtu.be/xwaCg7SWUhc?t=1122) Consider that grinding out a big rework without progress clips may be less engaging for viewers; ask audience which they prefer. ([[2021-01-04 - Using Knit & Roact to COMPLETELY Rework my Roblox Game! - Tallest Towe|Using Knit & Roact to COMPLETELY Rework my Roblox ]])
- 2022-09-23 [19:19](https://youtu.be/MyK4o2pIpQw?t=1159) Over-complicating wastes time without improving productivity; find the simplest way to build the game and ship it. ([[2022-09-23 - How to Organize & Style your Code in Roblox Development (and when to u|How to Organize & Style your Code in Roblox Develo]])

## [[testing-debugging-and-qa]]
- 2021-06-29 [11:15](https://youtu.be/stJtnGGt-1c?t=675) Put the template back in ServerStorage before testing; the test relies on the workspace copy being the one tagged and initialised. ([[2021-06-29 - How to make a Tycoon in Roblox 2 - Component Organization System|How to make a Tycoon in Roblox #2 - Component Orga]])
- 2021-08-09 [22:20](https://youtu.be/TgZI48DTNqE?t=1340) Disable Studio API access after testing DataStores to keep Studio from lagging, and test in a published build for accurate save behaviour. ([[2021-08-09 - How to make a Tycoon in Roblox 8 - Saving Player Data READ PINNED COMM|How to make a Tycoon in Roblox #8 - Saving Player ]])
- 2022-04-30 [4:11](https://youtu.be/5bI6l6SHBDU?t=251) Studio test purchases do not charge Robux, so test the flow freely in Studio before release. ([[2022-04-30 - How to make a Tycoon in Roblox Studio 12 - Dev Products|How to make a Tycoon in Roblox Studio #12 - Dev Pr]])
- 2022-06-19 [11:31](https://youtu.be/TeMGAqzZrDc?t=691) Add a catch block at the end of a promise chain to warn or log errors with a clean stack, and optionally send them to AnalyticsService. ([[2022-06-19 - How to use Promises (and why you should) in Roblox Development|How to use Promises (and why you should) in Roblox]])

Up: [[BRicey - How to make successful Roblox games]]
