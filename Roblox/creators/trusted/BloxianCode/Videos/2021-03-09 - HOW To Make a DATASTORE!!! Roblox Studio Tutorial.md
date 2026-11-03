---
title: "HOW To Make a DATASTORE!!! Roblox Studio Tutorial"
url: https://youtu.be/aBFH7KGIpnc
creator: BloxianCode
official: false
advice_density: low
date: 2021-03-09
views: 7280
transcript: auto-captions
confidence: medium
tags: [roblox, bloxiancode, youtube-learn]
creator_trust: TRUSTED
creator_score: 7.7
---

> [!note] Trust: TRUSTED (credibility audit score 7.7): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# HOW To Make a DATASTORE!!! Roblox Studio Tutorial

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Watch](https://youtu.be/aBFH7KGIpnc) | BloxianCode | 7,280 views | 2021-03-09

## Summary
Beginner tutorial on saving player coins with DataStoreService in Roblox Studio. Covers creating a leaderstats folder and coins value, loading saved data on PlayerAdded inside a pcall, and assigning the loaded value. Short and code-walkthrough focused; no monetisation or growth advice.

## Tips
- [0:28](https://youtu.be/aBFH7KGIpnc?t=28) **[[data-persistence]]** Never change the DataStore name after release; changing it makes all existing player data unreachable and lost.
- [2:06](https://youtu.be/aBFH7KGIpnc?t=126) **[[data-persistence]]** Wrap DataStore GetAsync calls in pcall so a failed request does not halt the script.
- [1:52](https://youtu.be/aBFH7KGIpnc?t=112) **[[data-persistence]]** Load player data inside a PlayerAdded handler so saved values can be applied when the player joins.

## Tools
Roblox Studio, DataStoreService, leaderstats folder

## Topics
[[data-persistence]]

Back to [[BloxianCode - How to make successful Roblox games]]
