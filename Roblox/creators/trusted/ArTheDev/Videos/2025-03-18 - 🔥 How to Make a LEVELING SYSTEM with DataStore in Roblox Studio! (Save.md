---
title: "🔥 How to Make a LEVELING SYSTEM with DataStore in Roblox Studio! (Save XP & Levels)"
url: https://youtu.be/V7PdX03D_hM
creator: ArTheDev
official: false
advice_density: low
date: 2025-03-18
views: 5136
transcript: auto-captions
confidence: high
tags: [roblox, arthedev, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.5
---

> [!note] Trust: TRUSTED (credibility audit score 8.5): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# 🔥 How to Make a LEVELING SYSTEM with DataStore in Roblox Studio! (Save XP & Levels)

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Watch](https://youtu.be/V7PdX03D_hM) | ArTheDev | 5,136 views | 2025-03-18

## Summary
Tutorial on building a leveling system in Roblox Studio with DataStoreService persistence. Covers a server script that loads/saves level, XP and max XP keyed by UserId, leaderstats display, and a client script that updates a level label and tweens an XP bar. Mostly a code walkthrough with no monetisation or growth advice.

## Tips
- [1:44](https://youtu.be/V7PdX03D_hM?t=104) **[[first-session-onboarding]]** Build the XP bar as a child of the background frame and use scale (0-1) sizing so progress math stays relative to the background.
- [2:44](https://youtu.be/V7PdX03D_hM?t=164) **[[data-persistence]]** Enable Game Settings > Security > 'Enable Studio Access to API Services' or DataStore calls will fail in Studio.
- [3:26](https://youtu.be/V7PdX03D_hM?t=206) **[[data-persistence]]** Key DataStore entries by player.UserId, not Name or DisplayName, since names can change.
- [3:26](https://youtu.be/V7PdX03D_hM?t=206) **[[data-persistence]]** Wrap DataStore GetAsync and SetAsync in pcall and check success before using returned data.

## Numbers
- [0:42](https://youtu.be/V7PdX03D_hM?t=42) XP requirement increase per level: **+5 XP in the example, scaled per level** (Demo example; XP requirement rises each level)
- [14:20](https://youtu.be/V7PdX03D_hM?t=860) Tween duration for XP bar: **2 seconds** (Default TweenInfo duration in the example)

## Tools
Roblox Studio, DataStoreService, TweenService, leaderstats

## Topics
[[client-server-and-remotes]] [[core-loops-and-game-design]] [[data-persistence]] [[first-session-onboarding]] [[ui-ux-design]]

Back to [[ArTheDev - How to make successful Roblox games]]
