---
title: "Roblox API Tutorial"
url: https://youtu.be/V65oLE0Wbuc
creator: SimTek Game Development
official: false
advice_density: medium
date: 2024-02-10
views: 18532
transcript: auto-captions
confidence: medium
tags: [roblox, simtekgamedevelopment, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.2
---

> [!note] Trust: TRUSTED (credibility audit score 8.2): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Roblox API Tutorial

[Watch](https://youtu.be/V65oLE0Wbuc) | SimTekGameDevelopment | 18,532 views | 2024-02-10

## Summary
Tutorial on using Roblox's public games and game-pass APIs (Swagger docs, curl testing) to list a user's games and passes and sell another creator's passes via a stand. Covers HttpService setup, the HTTP-blocked-in-Studio problem, and why proxies are needed, with a warning about third-party proxies.

## Tips
- [2:55](https://youtu.be/V65oLE0Wbuc?t=175) **[[trend-research-and-validation]]** Use Roblox's public games API docs (Swagger UI) to explore endpoints before writing code; test requests manually first.
- [6:02](https://youtu.be/V65oLE0Wbuc?t=362) **[[scripting-and-performance]]** Enable 'Allow HTTP Requests' in Game Settings > Security before using HttpService; Studio blocks external calls otherwise.
- [9:18](https://youtu.be/V65oLE0Wbuc?t=558) **[[scripting-and-performance]]** HttpService cannot call Roblox API domains directly from Studio; test endpoints with curl to confirm data is reachable.
- [11:27](https://youtu.be/V65oLE0Wbuc?t=687) **[[anti-exploit-and-security]]** Route Roblox API calls through a proxy you wrote or fully trust; avoid unknown public proxies, which can log or alter data.
- [16:16](https://youtu.be/V65oLE0Wbuc?t=976) **[[monetisation-gamepasses]]** Passing a game-pass owner's ID is unnecessary: the marketplace pays the pass owner automatically on purchase.
- [17:39](https://youtu.be/V65oLE0Wbuc?t=1059) **[[scripting-and-performance]]** Public proxies may go down or get shut down; do not rely on them in production games.

## Numbers
- [0:00](https://youtu.be/V65oLE0Wbuc?t=0) Example game-pass purchase: **10 Robux donation pass** (Demo purchase of another creator's pass through a stand)
- [5:00](https://youtu.be/V65oLE0Wbuc?t=300) Passes returned by query: **2 (limit set to 2)** (Games API V1 game-passes call with limit parameter)

## Games
- **Please Donate** [2:45](https://youtu.be/V65oLE0Wbuc?t=165): Lets creators set up a stand that sells other creators' game passes by querying the user's public games and their passes via API.

## Tools
Roblox Swagger UI (games API v1/v2), curl, HttpService, Python with requests (for external proxy testing), Notepad

## He points to
- Roblox games API Swagger UI (URL in video description)
- RoProxy (third-party proxy mentioned, not endorsed)

## Topics
[[anti-exploit-and-security]] [[monetisation-gamepasses]] [[scripting-and-performance]] [[trend-research-and-validation]]

Back to [[SimTekGameDevelopment - How to make successful Roblox games]]
