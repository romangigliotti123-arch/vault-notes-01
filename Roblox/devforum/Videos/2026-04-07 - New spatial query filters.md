---
title: "New spatial query filters"
url: https://devforum.roblox.com/t/new-spatial-query-filters/4563575
creator: Roblox DevForum
official: false
advice_density: medium
date: 2026-04-07
views: 480
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# New spatial query filters

[Open](https://devforum.roblox.com/t/new-spatial-query-filters/4563575) | Roblox DevForum | 480 views | 2026-04-07

## Summary
Roblox Physics Team announces new spatial query filter APIs (ExcludeInstances/IncludeInstances) for RaycastParams and OverlapParams, replacing FilterDescendantsInstances. Explains include/exclude semantics, priority rules, and performance gains from log(n) lookups; old API will eventually be deprecated.

## Tips
- [page](https://devforum.roblox.com/t/new-spatial-query-filters/4563575) **[[scripting-and-performance]]** Use RaycastParams.ExcludeInstances/IncludeInstances instead of FilterDescendantsInstances; new APIs are much faster, especially with large filter lists.
- [page](https://devforum.roblox.com/t/new-spatial-query-filters/4563575) **[[scripting-and-performance]]** Set IncludeInstances = nil for most permissive filter and {} for include-nothing; they are opposites, don't confuse them.
- [page](https://devforum.roblox.com/t/new-spatial-query-filters/4563575) **[[scripting-and-performance]]** If an instance is in both exclude and include lists, exclusion wins; design lists so they don't overlap unintentionally.
- [page](https://devforum.roblox.com/t/new-spatial-query-filters/4563575) **[[scripting-and-performance]]** Repeatedly updating filter lists (e.g., adding parts dynamically) is cheap in the new APIs thanks to tuned reflection code.
- [page](https://devforum.roblox.com/t/new-spatial-query-filters/4563575) **[[common-mistakes]]** Old FilterDescendantsInstances will eventually trigger a script analysis warning; migrate before deprecation rather than relying on it.
- [page](https://devforum.roblox.com/t/new-spatial-query-filters/4563575) **[[combat-and-gameplay-systems]]** Whitelist-with-exceptions (include a folder, exclude specific children) avoids needing multiple raycasts per query.

## Tools
RaycastParams, OverlapParams, FilterDescendantsInstances

## Topics
[[combat-and-gameplay-systems]] [[common-mistakes]] [[scripting-and-performance]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
