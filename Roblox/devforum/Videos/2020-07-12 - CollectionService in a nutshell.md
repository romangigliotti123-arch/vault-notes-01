---
title: "CollectionService in a nutshell"
url: https://devforum.roblox.com/t/collectionservice-in-a-nutshell/668984
creator: Roblox DevForum
official: false
advice_density: medium
date: 2020-07-12
views: 242
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# CollectionService in a nutshell

[Open](https://devforum.roblox.com/t/collectionservice-in-a-nutshell/668984) | Roblox DevForum | 242 views | 2020-07-12

## Summary
Devforum tutorial explaining CollectionService basics (AddTag, GetTags, GetTagged, RemoveTag, HasTag, added/removed signals), using tags to apply one script to many parts, the Tag Editor Plugin for tagging in Studio, and replication/persistence FAQs.

## Tips
- [page](https://devforum.roblox.com/t/collectionservice-in-a-nutshell/668984) **[[scripting-and-performance]]** Use CollectionService tags to drive one script over many instances instead of duplicating scripts; fixing one script fixes all tagged parts (e.g. 300 killing bricks).
- [page](https://devforum.roblox.com/t/collectionservice-in-a-nutshell/668984) **[[building-art-and-assets]]** Install the Tag Editor Plugin (by Sweetheartichoke) to create tags and apply them to selected parts in Studio without scripting; use World View to verify tagged parts.
- [page](https://devforum.roblox.com/t/collectionservice-in-a-nutshell/668984) **[[client-server-and-remotes]]** Tags replicate server-to-client only; client-added tags do not replicate to server or other clients. Add tags that matter for gameplay on the server.
- [page](https://devforum.roblox.com/t/collectionservice-in-a-nutshell/668984) **[[data-persistence]]** Do not manage DataStoreService values with tags; use dictionaries or arrays on the server for that data.
- [page](https://devforum.roblox.com/t/collectionservice-in-a-nutshell/668984) **[[testing-debugging-and-qa]]** Tags added in Studio via the command bar persist across sessions, but there is no guarantee they persist forever, especially if tagged instances are modified.
- [page](https://devforum.roblox.com/t/collectionservice-in-a-nutshell/668984) **[[scripting-and-performance]]** Use GetInstanceAddedSignal and GetInstanceRemovedSignal to react to instances gaining or losing a tag at runtime.

## Numbers
- [page](https://devforum.roblox.com/t/collectionservice-in-a-nutshell/668984) Example scale: **3 parts in example; author notes 300 or 500 parts as the real-world case** (Single tagged-part script example, roughly 25 lines of code)

## Tools
CollectionService, Tag Editor Plugin

## He points to
- Tag Editor Plugin by @Sweetheartichoke (DevForum)

## Topics
[[building-art-and-assets]] [[client-server-and-remotes]] [[data-persistence]] [[scripting-and-performance]] [[testing-debugging-and-qa]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
