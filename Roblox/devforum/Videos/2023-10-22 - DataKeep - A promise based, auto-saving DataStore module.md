---
title: "DataKeep - A promise based, auto-saving DataStore module"
url: https://devforum.roblox.com/t/datakeep-a-promise-based-auto-saving-datastore-module/2656200
creator: Roblox DevForum
official: false
advice_density: medium
date: 2023-10-22
views: 101
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# DataKeep - A promise based, auto-saving DataStore module

[Open](https://devforum.roblox.com/t/datakeep-a-promise-based-auto-saving-datastore-module/2656200) | Roblox DevForum | 101 views | 2023-10-22

## Summary
Documentation page for DataKeep, a promise-based, auto-saving DataStore module by noahrepublic that mirrors ProfileService's API. Features include session locking, spread-out save calls, and no getter/setter functions. It targets ProfileService issues: connection cleanup, async waiting patterns, code length, and partial type checking.

## Tips
- [page](https://devforum.roblox.com/t/datakeep-a-promise-based-auto-saving-datastore-module/2656200) **[[data-persistence]]** Use a promise-based DataStore wrapper so you know exactly when a profile load or save has finished, instead of awkward async waiting.
- [page](https://devforum.roblox.com/t/datakeep-a-promise-based-auto-saving-datastore-module/2656200) **[[data-persistence]]** Use a DataStore module with session locking so a player's data isn't written by two servers at once.
- [page](https://devforum.roblox.com/t/datakeep-a-promise-based-auto-saving-datastore-module/2656200) **[[data-persistence]]** Spread save calls evenly over time rather than saving all players at once.
- [page](https://devforum.roblox.com/t/datakeep-a-promise-based-auto-saving-datastore-module/2656200) **[[luau-language-and-types]]** Luau cannot type-check Promises, so typed promise APIs only get partial type safety.
- [page](https://devforum.roblox.com/t/datakeep-a-promise-based-auto-saving-datastore-module/2656200) **[[code-architecture-and-frameworks]]** Keep data modules short and readable so contributors can work on them quickly.

## Tools
DataKeep, ProfileService

## He points to
- ProfileService
- Roblox OSS discord DataKeep thread
- DataKeep GitHub repository

## Topics
[[code-architecture-and-frameworks]] [[data-persistence]] [[luau-language-and-types]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
