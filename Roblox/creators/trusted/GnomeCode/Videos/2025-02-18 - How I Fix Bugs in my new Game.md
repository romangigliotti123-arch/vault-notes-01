---
title: "How I Fix Bugs in my new Game"
url: https://youtu.be/OyPgQgBSIe4
creator: GnomeCode
official: false
advice_density: medium
date: 2025-02-18
views: 19590
transcript: auto-captions
confidence: high
tags: [roblox, gnomecode, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.1
---

> [!note] Trust: TRUSTED (credibility audit score 8.1): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# How I Fix Bugs in my new Game

[Watch](https://youtu.be/OyPgQgBSIe4) | GnomeCode | 19,590 views | 2025-02-18

## Summary
Devlog walkthrough of fixing player-reported bugs in the newly launched Roblox game Gnome Hotel. Covers reproducing bugs with artificial replication lag, debouncing ProximityPrompts, raycast-based stand-up checks for crawling, a LocalPlayer-side fix for mobile crouch buttons via LastInputTypeChanged, and anchoring welded props.

## Tips
- [0:52](https://youtu.be/OyPgQgBSIe4?t=52) **[[testing-debugging-and-qa]]** Reproduce race-condition bugs by adding artificial replication lag in Studio settings (e.g. 0.5s) to expose double-pickup exploits.
- [2:13](https://youtu.be/OyPgQgBSIe4?t=133) **[[client-server-and-remotes]]** Disable a ProximityPrompt immediately on trigger and return early if disabled, so rapid spamming can't grant multiple pickups.
- [4:19](https://youtu.be/OyPgQgBSIe4?t=259) **[[common-mistakes]]** Scattering teleport logic across many functions causes mistakes; centralise all teleport-to-room logic in one function so it resets state (e.g. walk speed) consistently.
- [6:56](https://youtu.be/OyPgQgBSIe4?t=416) **[[physics-pathfinding-and-npc-ai]]** Before letting a character stand from crawl, raycast up ~3 studs from head and root; block standing while anything is overhead to prevent clipping through the floor.
- [9:05](https://youtu.be/OyPgQgBSIe4?t=545) **[[physics-pathfinding-and-npc-ai]]** Disable collisions on closet doors that cause physics fling; use an invisible barrier part to block movement instead.
- [9:45](https://youtu.be/OyPgQgBSIe4?t=585) **[[combat-and-gameplay-systems]]** Gate actions like crouch and jump with a character attribute (e.g. Hiding) checked in the crouch logic, since setting walk speed to zero doesn't block crouching.
- [10:28](https://youtu.be/OyPgQgBSIe4?t=628) **[[ui-ux-design]]** Don't rely on a one-time UserInputService.TouchEnabled check; hook LastInputTypeChanged to show/hide the mobile crouch button dynamically as the input type changes.
- [11:47](https://youtu.be/OyPgQgBSIe4?t=707) **[[building-and-level-design]]** Anchor props that are welded to surfaces at build time, or they can behave unexpectedly in live play.
- [3:12](https://youtu.be/OyPgQgBSIe4?t=192) **[[building-and-level-design]]** Missing assets found by players can be scattered one per room; audit every room systematically rather than fixing a single report.

## Numbers
- [1:32](https://youtu.be/OyPgQgBSIe4?t=92) Artificial replication lag used to reproduce bug: **0.5 seconds**
- [1:32](https://youtu.be/OyPgQgBSIe4?t=92) Coins collected while spamming with lag: **6**
- [7:36](https://youtu.be/OyPgQgBSIe4?t=456) Overhead raycast distance for stand-up check: **3 studs**

## Games
- **Gnome Hotel** [0:00](https://youtu.be/OyPgQgBSIe4?t=0): Newly launched demo; player bug reports via Discord drove the fix list. Fixes were small logic and physics patches.

## Tools
Roblox Studio

## Quotes
- [0:00](https://youtu.be/OyPgQgBSIe4?t=0) "thanks to everyone who's checked out the game so far... there's actually been quite a bit of enthusiasm for this thing"
- [8:59](https://youtu.be/OyPgQgBSIe4?t=539) "sometimes fixing the bugs is as much about finding how to recreate them"

## Topics
[[building-and-level-design]] [[client-server-and-remotes]] [[combat-and-gameplay-systems]] [[common-mistakes]] [[physics-pathfinding-and-npc-ai]] [[testing-debugging-and-qa]] [[ui-ux-design]]

Back to [[GnomeCode - How to make successful Roblox games]]
