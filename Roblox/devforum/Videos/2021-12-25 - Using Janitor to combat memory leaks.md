---
title: "Using Janitor to combat memory leaks"
url: https://devforum.roblox.com/t/using-janitor-to-combat-memory-leaks/1601710
creator: Roblox DevForum
official: false
advice_density: medium
date: 2021-12-25
views: 100
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Using Janitor to combat memory leaks

[Open](https://devforum.roblox.com/t/using-janitor-to-combat-memory-leaks/1601710) | Roblox DevForum | 100 views | 2021-12-25

## Summary
Developer guide to the Janitor library for Roblox (by LucasMZ_RBX): tracking connections, instances, custom objects and functions for cleanup, Cleanup vs Destroy, LinkToInstance, indexed removal, and usage pattern inside classes to prevent memory leaks.

## Tips
- [page](https://devforum.roblox.com/t/using-janitor-to-combat-memory-leaks/1601710) **[[data-persistence]]** Use Janitor per player, per instance, or per script/tool to group everything that must be cleaned together.
- [page](https://devforum.roblox.com/t/using-janitor-to-combat-memory-leaks/1601710) **[[scripting-and-performance]]** Store RBXScriptConnections in a Janitor and disconnect them when no longer needed to avoid leaks and stray threads.
- [page](https://devforum.roblox.com/t/using-janitor-to-combat-memory-leaks/1601710) **[[scripting-and-performance]]** Always pass the cleanup method name explicitly when adding Instances or custom objects (e.g. "Destroy", "DisconnectAll") for consistent habits.
- [page](https://devforum.roblox.com/t/using-janitor-to-combat-memory-leaks/1601710) **[[code-architecture-and-frameworks]]** Give each class a _janitor member; add signals, connections and instances to it, and call Destroy in the class's Destroy method, setting it to nil afterward.
- [page](https://devforum.roblox.com/t/using-janitor-to-combat-memory-leaks/1601710) **[[scripting-and-performance]]** Use janitor:LinkToInstance(instance) so the Janitor cleans up automatically when that instance is destroyed.
- [page](https://devforum.roblox.com/t/using-janitor-to-combat-memory-leaks/1601710) **[[code-architecture-and-frameworks]]** Pass an index as the third argument to :Add so you can later prematurely clean one item with :Remove(index).
- [page](https://devforum.roblox.com/t/using-janitor-to-combat-memory-leaks/1601710) **[[code-architecture-and-frameworks]]** Use :Cleanup to reuse a Janitor, and :Destroy when the object is finished, since Destroy makes it unusable.
- [page](https://devforum.roblox.com/t/using-janitor-to-combat-memory-leaks/1601710) **[[code-architecture-and-frameworks]]** Use Janitor's returned object from :Add when constructing inline, e.g. local obj = janitor:Add(Obj.new(), "Destroy").

## Tools
Janitor

## He points to
- Maid
- GoodSignal
- FastSignal
- Janitor documentation

## Topics
[[code-architecture-and-frameworks]] [[data-persistence]] [[scripting-and-performance]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
