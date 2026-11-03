---
title: "Docs: cloud / guides / instance"
url: https://create.roblox.com/docs/cloud/guides/instance.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: cloud / guides / instance

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/cloud/guides/instance.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox Open Cloud docs for Engine Instance APIs (beta): list children, get, update Script/LocalScript/ModuleScript objects from the web via API key with universe-place-instances system. Includes polling pattern and a Potion Shop Google Sheets demo.

## Tips
- [page](https://create.roblox.com/docs/cloud/guides/instance) **[[scripting-and-performance]]** Scripts open in Studio can't be updated via Open Cloud; close the Script Editor tab first, or you get a TypeError.
- [page](https://create.roblox.com/docs/cloud/guides/instance) **[[scripting-and-performance]]** Collaborative session must be enabled for the game before Engine Instance APIs can access it.
- [page](https://create.roblox.com/docs/cloud/guides/instance) **[[anti-exploit-and-security]]** Create API keys with minimal scopes: specify only needed games and read/write permissions, and restrict accepted IP addresses where possible.
- [page](https://create.roblox.com/docs/cloud/guides/instance) **[[scripting-and-performance]]** Keep Open Cloud update request bodies under 200 KB; larger payloads are rejected.

## Numbers
- [page](https://create.roblox.com/docs/cloud/guides/instance) Request body limit: **200 KB** (Open Cloud Update Instance request bodies)
- [page](https://create.roblox.com/docs/cloud/guides/instance) Example poll cadence: **5 s, max 10 retries** (Sample polling loop for Operation results)

## Games
- **Potion Shop (demo)**: Roblox demo place used to show updating ReplicatedStorage ItemList script from Google Sheets via Open Cloud.

## Tools
Roblox Open Cloud Engine Instance APIs (beta), Google Sheets, Google Apps Script, Roblox Studio

## Topics
[[ai-and-tools]] [[anti-exploit-and-security]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
