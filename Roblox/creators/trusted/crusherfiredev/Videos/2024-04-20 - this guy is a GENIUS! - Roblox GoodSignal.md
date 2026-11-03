---
title: "this guy is a GENIUS! - Roblox GoodSignal"
url: https://youtu.be/wgdyFcGdGnk
creator: Crusherfire
official: false
advice_density: low
date: 2024-04-20
views: 33791
transcript: auto-captions
confidence: high
tags: [roblox, crusherfiredev, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.7
---

> [!note] Trust: TRUSTED (credibility audit score 8.7): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# this guy is a GENIUS! - Roblox GoodSignal

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Watch](https://youtu.be/wgdyFcGdGnk) | crusherfiredev | 33,791 views | 2024-04-20

## Summary
Shows the GoodSignal module by Stant for creating custom RBXScriptSignal-like events on custom OOP classes. Demonstrates Fire with varargs, Once, connection disconnect, a destroying signal for custom objects, and a level-change signal example.

## Tips
- [0:41](https://youtu.be/wgdyFcGdGnk?t=41) **[[code-architecture-and-frameworks]]** Use custom signals on your own classes to make code event-driven, mimicking instance events like Destroying or AncestryChanged.
- [5:28](https://youtu.be/wgdyFcGdGnk?t=328) **[[luau-language-and-types]]** Fire a Destroying-style signal before clearing a custom object's table so listeners can clean up connections and references.
- [6:09](https://youtu.be/wgdyFcGdGnk?t=369) **[[luau-language-and-types]]** Yielding inside a signal handler lets the thread pause and resume later; GoodSignal caches runner coroutines so yielding costs little.
- [7:08](https://youtu.be/wgdyFcGdGnk?t=428) **[[code-architecture-and-frameworks]]** Fire a LevelChanged-style signal with the old value after updating state so other scripts can react to changes in custom objects.

## Tools
GoodSignal (by Stant), require-autocomplete plugin

## Topics
[[code-architecture-and-frameworks]] [[luau-language-and-types]]

Back to [[crusherfiredev - How to make successful Roblox games]]
