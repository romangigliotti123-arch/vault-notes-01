---
title: "Linked List / Signals - Roblox Scripting Tutorial"
url: https://youtu.be/DTEraIOfoS0
creator: Suphi Kaner
official: false
advice_density: low
date: 2024-08-06
views: 21058
transcript: auto-captions
confidence: high
tags: [roblox, 5uphi, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.8
---

> [!note] Trust: TRUSTED (credibility audit score 8.8): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Linked List / Signals - Roblox Scripting Tutorial

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Watch](https://youtu.be/DTEraIOfoS0) | 5uphi | 21,058 views | 2024-08-06

## Summary
Teaches linked lists in Luau and builds event-system classes (BindableEvent wrapper, dictionary, array, singly then doubly linked list) to compare iteration safety during connect/disconnect/fire. Covers task.defer vs spawn, thread recycling, and a linked list module from the Toolbox.

## Tips
- [15:43](https://youtu.be/DTEraIOfoS0?t=943) **[[code-architecture-and-frameworks]]** Pick array vs linked list by features, not performance; array performance only matters at roughly 5,000+ items with front inserts/removes.
- [21:52](https://youtu.be/DTEraIOfoS0?t=1312) **[[scripting-and-performance]]** Roblox signals now defer by default; mirror that in custom event classes with task.defer, since spawn/direct calls break when connecting or disconnecting mid-fire.
- [35:07](https://youtu.be/DTEraIOfoS0?t=2107) **[[luau-language-and-types]]** Never insert into a dictionary (pairs/next) while iterating it; removal is tolerable but insertion corrupts iteration order.
- [44:14](https://youtu.be/DTEraIOfoS0?t=2654) **[[luau-language-and-types]]** Array event: iterate in reverse when connecting during fire so new items are not called; avoid removing items mid-iteration with table.remove or later entries get skipped.

## Numbers
- [11:14](https://youtu.be/DTEraIOfoS0?t=674) table.remove shift cost: **around 500 items after target before linked list matches** (Creator's personal benchmark for table.remove vs link update)
- [14:39](https://youtu.be/DTEraIOfoS0?t=879) Array size threshold for performance concern: **5,000+ items** (Only when removing or inserting at the front of the list)
- [1:23:19](https://youtu.be/DTEraIOfoS0?t=4999) Thread recycling: **Pool stays short with spawn; slightly larger with defer** (Creator's description of cached thread array size)

## Tools
Roblox Studio, Toolbox, Luau, table library

## Topics
[[code-architecture-and-frameworks]] [[luau-language-and-types]] [[scripting-and-performance]] [[testing-debugging-and-qa]]

Back to [[5uphi - How to make successful Roblox games]]
