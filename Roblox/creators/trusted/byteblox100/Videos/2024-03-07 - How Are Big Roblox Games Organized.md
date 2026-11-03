---
title: "How Are Big Roblox Games Organized?"
url: https://youtu.be/j-yWdoJqV_c
creator: ByteBlox
official: false
advice_density: medium
date: 2024-03-07
views: 18577
transcript: auto-captions
confidence: high
tags: [roblox, byteblox100, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.1
---

> [!note] Trust: TRUSTED (credibility audit score 8.1): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# How Are Big Roblox Games Organized?

[Watch](https://youtu.be/j-yWdoJqV_c) | byteblox100 | 18,577 views | 2024-03-07

## Summary
Beginner tutorial on Roblox CollectionService and tags. Covers how tags work on any instance, the TagAdded and TagRemoved events, and the GetTagged, GetTags and GetAllTags functions. Demonstrates adding tags via script and shows that tag names are unique across the game, so one tag can be shared by many instances.

## Tips
- [0:24](https://youtu.be/j-yWdoJqV_c?t=24) **[[code-architecture-and-frameworks]]** Use tags to label instances by role (e.g. 'weapon') and check the tag in script instead of relying on names or hierarchy.
- [2:08](https://youtu.be/j-yWdoJqV_c?t=128) **[[code-architecture-and-frameworks]]** Alias game:GetService('CollectionService') to a short local variable such as CS to keep code concise.
- [2:50](https://youtu.be/j-yWdoJqV_c?t=170) **[[code-architecture-and-frameworks]]** Use CollectionService TagAdded/TagRemoved signals to react when tags change; per-instance tags alone cannot be watched for changes.
- [3:36](https://youtu.be/j-yWdoJqV_c?t=216) **[[code-architecture-and-frameworks]]** Use CS:GetTagged(tag) to fetch every instance carrying a tag, rather than searching the workspace manually.
- [4:59](https://youtu.be/j-yWdoJqV_c?t=299) **[[code-architecture-and-frameworks]]** Expect tag names to be global: tags are unique strings, so many instances can share one tag without creating duplicates.
- [8:14](https://youtu.be/j-yWdoJqV_c?t=494) **[[code-architecture-and-frameworks]]** Give instances several tags (a shared category tag plus a specific tag) to group them in different ways.
- [9:37](https://youtu.be/j-yWdoJqV_c?t=577) **[[code-architecture-and-frameworks]]** GetAllTags only returns tags you created; Roblox's built-in tags such as RigEdit are excluded.

## Numbers
- [9:37](https://youtu.be/j-yWdoJqV_c?t=577) Built-in CollectionService tags: **1 (RigEdit), as of March 4, 2024** (Roblox ships with only one default tag at the time)

## Tools
Roblox Studio, CollectionService, Luau

## Topics
[[code-architecture-and-frameworks]]

Back to [[byteblox100 - How to make successful Roblox games]]
