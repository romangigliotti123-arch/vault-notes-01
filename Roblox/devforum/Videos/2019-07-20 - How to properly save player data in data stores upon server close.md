---
title: "How to properly save player data in data stores upon server close"
url: https://devforum.roblox.com/t/how-to-properly-save-player-data-in-data-stores-upon-server-close/313218
creator: Roblox DevForum
official: false
advice_density: high
date: 2019-07-20
views: 295
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# How to properly save player data in data stores upon server close

[Open](https://devforum.roblox.com/t/how-to-properly-save-player-data-in-data-stores-upon-server-close/313218) | Roblox DevForum | 295 views | 2019-07-20

## Summary
DevForum tutorial explaining why PlayerRemoving-only saves fail when servers shut down (last player leaves, manual shutdown, network error). Proposes game:BindToClose to save remaining players, notes the 30-second shared time limit across all bound functions, and recommends running saves concurrently with coroutine.wrap rather than sequentially.

## Tips
- [page](https://devforum.roblox.com/t/how-to-properly-save-player-data-in-data-stores-upon-server-close/313218) **[[data-persistence]]** Don't rely only on PlayerRemoving for saving; the event may never fire or finish when the server shuts down (last player leaves, manual shutdown, network error).
- [page](https://devforum.roblox.com/t/how-to-properly-save-player-data-in-data-stores-upon-server-close/313218) **[[data-persistence]]** Use game:BindToClose to save all remaining players' data when the server shuts down, in addition to saving on PlayerRemoving.
- [page](https://devforum.roblox.com/t/how-to-properly-save-player-data-in-data-stores-upon-server-close/313218) **[[data-persistence]]** Save players concurrently inside BindToClose using coroutine.wrap(save)(player) so DataStore web requests don't run one after another.
- [page](https://devforum.roblox.com/t/how-to-properly-save-player-data-in-data-stores-upon-server-close/313218) **[[data-persistence]]** All BindToClose functions share a single 30-second budget combined, not 30 seconds each; the server shuts down when it expires regardless of unfinished saves.
- [page](https://devforum.roblox.com/t/how-to-properly-save-player-data-in-data-stores-upon-server-close/313218) **[[luau-language-and-types]]** Don't use wait(n) inside BindToClose to stall for time; it buys no extra time. Do meaningful save work instead.

## Numbers
- [page](https://devforum.roblox.com/t/how-to-properly-save-player-data-in-data-stores-upon-server-close/313218) BindToClose time limit: **30 seconds total for all bound functions** (Shared budget; server shuts down when it expires even if saves are unfinished)
- [page](https://devforum.roblox.com/t/how-to-properly-save-player-data-in-data-stores-upon-server-close/313218) DataStore web request duration: **about 0.5 to 1 second** (Author's experience; scales badly with many players per server)

## Tools
DataStoreService, BindToClose, coroutine.wrap

## Topics
[[data-persistence]] [[luau-language-and-types]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
