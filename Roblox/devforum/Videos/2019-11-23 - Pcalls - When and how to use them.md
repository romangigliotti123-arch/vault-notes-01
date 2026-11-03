---
title: "Pcalls - When and how to use them"
url: https://devforum.roblox.com/t/pcalls-when-and-how-to-use-them/393687
creator: Roblox DevForum
official: false
advice_density: medium
date: 2019-11-23
views: 659
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Pcalls - When and how to use them

[Open](https://devforum.roblox.com/t/pcalls-when-and-how-to-use-them/393687) | Roblox DevForum | 659 views | 2019-11-23

## Summary
Community tutorial on Lua pcalls for Roblox: basic syntax, wrapping DataStore Get/Set/Update/Increment with retry loops (while/repeat, 7s wait), pcalling StarterGui SetCore until registered, xpcall with error handlers, debug.traceback, and ypcall being obsolete.

## Tips
- [page](https://devforum.roblox.com/t/pcalls-when-and-how-to-use-them/393687) **[[scripting-and-performance]]** Pass the method as pcall(DataStore.GetAsync, DataStore, "key") rather than wrapping in an anonymous function; avoids creating a closure each call.
- [page](https://devforum.roblox.com/t/pcalls-when-and-how-to-use-them/393687) **[[data-persistence]]** Wrap every DataStore call (GetAsync, SetAsync, UpdateAsync, IncrementAsync) in pcall and check success, since failures can cause data loss.
- [page](https://devforum.roblox.com/t/pcalls-when-and-how-to-use-them/393687) **[[data-persistence]]** Retry failed DataStore calls in a while-not-success loop with a wait(7) cooldown between attempts to respect DataStore limits.
- [page](https://devforum.roblox.com/t/pcalls-when-and-how-to-use-them/393687) **[[data-persistence]]** Do not declare success/response as local inside the retry loop; the loop condition must see the same variable the pcall assigns.
- [page](https://devforum.roblox.com/t/pcalls-when-and-how-to-use-them/393687) **[[scripting-and-performance]]** Pcall StarterGui:SetCore in a retry loop with wait(1), since SetCores aren't registered until CoreScripts initialise.
- [page](https://devforum.roblox.com/t/pcalls-when-and-how-to-use-them/393687) **[[scripting-and-performance]]** Do not use ypcall; pcall can yield in modern Luau, so ypcall gives no benefit.
- [page](https://devforum.roblox.com/t/pcalls-when-and-how-to-use-them/393687) **[[scripting-and-performance]]** Do not yield (wait) inside xpcall; it cannot yield. Use xpcall with debug.traceback as handler to get stack traces on errors.
- [page](https://devforum.roblox.com/t/pcalls-when-and-how-to-use-them/393687) **[[client-server-and-remotes]]** Pcall web API calls such as GetUserThumbnailAsync, since they fetch from external websites and can fail.

## Numbers
- [page](https://devforum.roblox.com/t/pcalls-when-and-how-to-use-them/393687) DataStore retry cooldown: **7 seconds between retries (per tutorial example)** (wait(7) in DataStore retry loop)
- [page](https://devforum.roblox.com/t/pcalls-when-and-how-to-use-them/393687) SetCore retry interval: **wait(1) between attempts** (StarterGui SetCore retry loop)

## Tools
pcall, xpcall, debug.traceback, DataStoreService

## He points to
- Programming in Lua: 8.4
- Lua Globals - Roblox Creator Hub
- debug - Roblox Creator Hub

## Topics
[[client-server-and-remotes]] [[data-persistence]] [[scripting-and-performance]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
