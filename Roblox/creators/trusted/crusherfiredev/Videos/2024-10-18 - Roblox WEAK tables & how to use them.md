---
title: "Roblox WEAK tables & how to use them"
url: https://youtu.be/K6TryCAqFbs
creator: Crusherfire
official: false
advice_density: medium
date: 2024-10-18
views: 14738
transcript: auto-captions
confidence: high
tags: [roblox, crusherfiredev, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.7
---

> [!note] Trust: TRUSTED (credibility audit score 8.7): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Roblox WEAK tables & how to use them

[Watch](https://youtu.be/K6TryCAqFbs) | crusherfiredev | 14,738 views | 2024-10-18

## Summary
Explains Luau weak tables (__mode K, V, KV), how weak keys enable auto-cleaning caches (ephemeron tables), and why Roblox instances behave differently: instances are not weakly held as documented, so workarounds like Parent-change listeners and holding references via Destroying/DescendantAdded are shown.

## Tips
- [0:35](https://youtu.be/K6TryCAqFbs?t=35) **[[scripting-and-performance]]** Use weak-key tables (__mode='k') as caches keyed by objects; entries are auto-removed when the key object is no longer strongly referenced, avoiding manual cleanup and leaks.
- [5:33](https://youtu.be/K6TryCAqFbs?t=333) **[[scripting-and-performance]]** Don't store the weak key inside the table's values under a strong reference; a value referencing its own key keeps it alive. Use __mode='kv' to avoid this.
- [6:54](https://youtu.be/K6TryCAqFbs?t=414) **[[scripting-and-performance]]** For per-entity caches (e.g. AI raycast params), key by the entity so cache entries are collected when the entity is destroyed.
- [10:22](https://youtu.be/K6TryCAqFbs?t=622) **[[scripting-and-performance]]** Don't rely on weak tables to weakly hold Roblox Instances; the docs say instances are never weak, and behavior is inconsistent. Test before depending on it.
- [13:44](https://youtu.be/K6TryCAqFbs?t=824) **[[scripting-and-performance]]** Workaround for instances: hold a strong reference in a table, and release it when the part's Parent changes to nil, disconnecting the connection.
- [18:23](https://youtu.be/K6TryCAqFbs?t=1103) **[[scripting-and-performance]]** A closure must reference the object (e.g. in a Destroying listener) to keep it alive; otherwise it may be collected even when the weak table should hold it.
- [19:32](https://youtu.be/K6TryCAqFbs?t=1172) **[[scripting-and-performance]]** DescendantAdded on game is a possible way to track instances globally, but it adds a script execution per instance; be cautious on mobile with large batches.

## Numbers
- [3:43](https://youtu.be/K6TryCAqFbs?t=223) Memory pressure threshold used in demo: **50,000 parts**
- [19:32](https://youtu.be/K6TryCAqFbs?t=1172) Reported slowdown adding many parts at once: **twice as slow or more (per forum commenter)**

## Games
- **Paths of Peril** [6:54](https://youtu.be/K6TryCAqFbs?t=414): Caches AI raycast parameters in a weak-key table so entries clear automatically when AI objects are destroyed.
- **Salty Gun Labs** [9:42](https://youtu.be/K6TryCAqFbs?t=582): Uses a weak-key connections cache for GUI button objects so destroyed buttons are cleaned up without manual removal.

## Tools
Roblox Studio, Luau metatables (setmetatable, __mode)

## He points to
- Roblox developer forum thread on weak tables and instances (2018 post)
- Roblox documentation: metatables, __mode

## Topics
[[scripting-and-performance]]

Back to [[crusherfiredev - How to make successful Roblox games]]
