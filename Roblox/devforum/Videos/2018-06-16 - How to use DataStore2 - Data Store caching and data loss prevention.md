---
title: "How to use DataStore2 - Data Store caching and data loss prevention"
url: https://devforum.roblox.com/t/how-to-use-datastore2-data-store-caching-and-data-loss-prevention/136317
creator: Roblox DevForum
official: false
advice_density: medium
date: 2018-06-16
views: 5574
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# How to use DataStore2 - Data Store caching and data loss prevention

[Open](https://devforum.roblox.com/t/how-to-use-datastore2-data-store-caching-and-data-loss-prevention/136317) | Roblox DevForum | 5,574 views | 2018-06-16

## Summary
Documentation/announcement page for DataStore2, an open-source Roblox module (by Kampfkarren) that wraps berezaa's save method to prevent data loss, cache data, and verify before saving. Covers download from GitHub releases, news thread, docs site, and a basic coin-store example using Get, OnUpdate, Increment and Combine.

## Tips
- [page](https://devforum.roblox.com/t/how-to-use-datastore2-data-store-caching-and-data-loss-prevention/136317) **[[data-persistence]]** Use DataStore2 (open source, berezaa's method) for saving: it caches, verifies data before saving, and has had no reported data loss per the author.
- [page](https://devforum.roblox.com/t/how-to-use-datastore2-data-store-caching-and-data-loss-prevention/136317) **[[data-persistence]]** Always call DataStore2.Combine("DATA", key) for every key you use, so keys share one DataStore; the docs' Gotchas page explains why.
- [page](https://devforum.roblox.com/t/how-to-use-datastore2-data-store-caching-and-data-loss-prevention/136317) **[[data-persistence]]** Pass a default to coinStore:Get(100) so new players start with a value instead of nil.
- [page](https://devforum.roblox.com/t/how-to-use-datastore2-data-store-caching-and-data-loss-prevention/136317) **[[client-server-and-remotes]]** Keep purchase logic on the server: validate the product name against a shared table, check balance with Get, then deduct with Increment(-price).
- [page](https://devforum.roblox.com/t/how-to-use-datastore2-data-store-caching-and-data-loss-prevention/136317) **[[client-server-and-remotes]]** Use coinStore:OnUpdate(callback) to push fresh values to the client via RemoteEvent whenever the store changes.

## Numbers
- [page](https://devforum.roblox.com/t/how-to-use-datastore2-data-store-caching-and-data-loss-prevention/136317) Visits: **120 million** (Author's game using DataStore2)
- [page](https://devforum.roblox.com/t/how-to-use-datastore2-data-store-caching-and-data-loss-prevention/136317) Concurrent players: **3,000-8,000 typical; peak 12,000** (Author's game using DataStore2)
- [page](https://devforum.roblox.com/t/how-to-use-datastore2-data-store-caching-and-data-loss-prevention/136317) Visits: **3 million; consistent CCU above 1,000; peak 5.8k** (Fairy World by AlreadyPro, uses DataStore2)
- [page](https://devforum.roblox.com/t/how-to-use-datastore2-data-store-caching-and-data-loss-prevention/136317) Visits: **350 million; tens of thousands CCU** (Dungeon Quest by vCaffy, uses DataStore2)
- [page](https://devforum.roblox.com/t/how-to-use-datastore2-data-store-caching-and-data-loss-prevention/136317) Reported data loss cases: **0** (Author says no data loss reported to date (2018))

## Games
- **Fairy World**: Uses DataStore2; featured by Roblox with peak 5.8k players.
- **Dungeon Quest**: Uses DataStore2 at 350M visits with tens of thousands of players.

## Tools
DataStore2, GitHub releases (rbxmx file), Roblox Studio

## He points to
- DataStore2 documentation site
- DataStore2 GitHub releases page
- DataStore2 News/Changelog DevForum thread

## Topics
[[client-server-and-remotes]] [[data-persistence]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
