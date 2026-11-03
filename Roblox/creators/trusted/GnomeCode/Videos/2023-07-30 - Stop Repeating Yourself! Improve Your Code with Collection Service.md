---
title: "Stop Repeating Yourself! Improve Your Code with Collection Service"
url: https://youtu.be/UsPYgIW3rv8
creator: GnomeCode
official: false
advice_density: medium
date: 2023-07-30
views: 90307
transcript: auto-captions
confidence: high
tags: [roblox, gnomecode, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.1
---

> [!note] Trust: TRUSTED (credibility audit score 8.1): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Stop Repeating Yourself! Improve Your Code with Collection Service

[Watch](https://youtu.be/UsPYgIW3rv8) | GnomeCode | 90,307 views | 2023-07-30

## Summary
Tutorial on replacing duplicated per-model door scripts with one server script using CollectionService tags. Shows tagging parts with the Tag Editor plugin, calling CollectionService:GetTagged, looping over tagged models, and editing a single script to update all doors.

## Tips
- [1:22](https://youtu.be/UsPYgIW3rv8?t=82) **[[development-process-and-speed]]** Avoid duplicating scripts into every model; keep one script and update all copies from it, so changes are made once.
- [2:04](https://youtu.be/UsPYgIW3rv8?t=124) **[[scripting-and-performance]]** Use CollectionService tags to find all instances of a type; tag models with a plugin such as Tag Editor instead of hardcoding references.
- [3:26](https://youtu.be/UsPYgIW3rv8?t=206) **[[code-architecture-and-frameworks]]** Call CollectionService:GetTagged('TagName') and loop with for ... do; tag spelling must match exactly.
- [4:48](https://youtu.be/UsPYgIW3rv8?t=288) **[[code-architecture-and-frameworks]]** Pass each tagged model into the handler function instead of relying on script.Parent, so one script drives many objects.

## Numbers
- [5:30](https://youtu.be/UsPYgIW3rv8?t=330) tween duration: **0.1 seconds** (Changed once in the single script; applied to all tagged doors)

## Tools
Roblox Studio, CollectionService, Tag Editor plugin (by Sweetheart Chokes)

## He points to
- Tag Editor plugin by Sweetheart Chokes

## Topics
[[code-architecture-and-frameworks]] [[development-process-and-speed]] [[scripting-and-performance]]

Back to [[GnomeCode - How to make successful Roblox games]]
