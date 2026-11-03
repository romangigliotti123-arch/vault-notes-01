---
title: "How to use a Maid class on Roblox to manage state"
url: https://devforum.roblox.com/t/how-to-use-a-maid-class-on-roblox-to-manage-state/340061
creator: Roblox DevForum
official: false
advice_density: medium
date: 2019-08-28
views: 227
transcript: web-page
confidence: medium
tags: [roblox, roblox devforum, youtube-learn]
---

# How to use a Maid class on Roblox to manage state

[Open](https://devforum.roblox.com/t/how-to-use-a-maid-class-on-roblox-to-manage-state/340061) | Roblox DevForum | 227 views | 2019-08-28

## Summary
Quenty's DevForum/Medium article introducing the Maid class for managing state and cleaning up events/objects in Roblox. Explains Maid as a helper for encapsulating state and deconstructors, used heavily in Jailbreak to avoid memory leaks. Points to the NevermoreEngine source for Maid.lua.

## Tips
- [page](https://devforum.roblox.com/t/how-to-use-a-maid-class-on-roblox-to-manage-state/340061) **[[code-architecture-and-frameworks]]** Use a Maid class to collect events, connections and instances, then clean them all up in one call to avoid memory leaks and simplify teardown.
- [page](https://devforum.roblox.com/t/how-to-use-a-maid-class-on-roblox-to-manage-state/340061) **[[scripting-and-performance]]** Disconnect signals and destroy objects when state changes or objects are removed; a Maid centralises this cleanup so nothing is forgotten.
- [page](https://devforum.roblox.com/t/how-to-use-a-maid-class-on-roblox-to-manage-state/340061) **[[luau-language-and-types]]** Maid.isMaid checks ClassName == 'Maid' on a table, a simple duck-typing pattern for identifying custom classes.

## Games
- **Jailbreak**: Uses Maid extensively to clean up events and objects and avoid memory leaks.

## Tools
Maid class (NevermoreEngine)

## He points to
- https://medium.com/roblox-development/how-to-use-a-maid-class-on-roblox-to-manage-state-651bf74de98b
- github.com/Quenty/NevermoreEngine

## Quotes
- [page](https://devforum.roblox.com/t/how-to-use-a-maid-class-on-roblox-to-manage-state/340061) "It vastly simplifies the cleaning up of events/objects, and gives me confidence that I will avoid memory leaks."

## Topics
[[code-architecture-and-frameworks]] [[luau-language-and-types]] [[scripting-and-performance]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
