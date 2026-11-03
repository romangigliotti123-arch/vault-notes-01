---
title: "Organizing your Game with Tags and CollectionService - Roblox Studio"
url: https://youtu.be/Vi2FckNJv9w
creator: B Ricey
official: false
advice_density: medium
date: 2021-06-12
views: 36237
transcript: manual-subs
confidence: high
tags: [roblox, bricey, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.0
---

> [!note] Trust: TRUSTED (credibility audit score 8.0): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Organizing your Game with Tags and CollectionService - Roblox Studio

[Watch](https://youtu.be/Vi2FckNJv9w) | BRicey | 36,237 views | 2021-06-12

## Summary
Tutorial on organizing a Roblox combat game's landmine logic with CollectionService tags. Shows a per-part Touched script, then refactors it into one centralized server script that handles all tagged parts, adds/removes behaviour via GetInstanceAddedSignal/RemovedSignal, and toggles tags at runtime. Mentions Knit's component system.

## Tips
- [0:00](https://youtu.be/Vi2FckNJv9w?t=0) **[[common-mistakes]]** Avoid putting a separate copy of a script inside every part; editing behaviour then means editing each copy. Centralize logic instead.
- [4:02](https://youtu.be/Vi2FckNJv9w?t=242) **[[code-architecture-and-frameworks]]** Use CollectionService tags to apply one script's logic to many parts; change the code once in ServerScriptService and every tagged instance updates.
- [5:12](https://youtu.be/Vi2FckNJv9w?t=312) **[[code-architecture-and-frameworks]]** Wrap per-object setup in a function like makeLandmine(part), then loop over CollectionService:GetTagged(tag) at startup to apply it to all existing instances.
- [6:39](https://youtu.be/Vi2FckNJv9w?t=399) **[[code-architecture-and-frameworks]]** Connect CollectionService:GetInstanceAddedSignal(tag) so instances tagged at runtime get the behaviour automatically, without extra code.
- [8:06](https://youtu.be/Vi2FckNJv9w?t=486) **[[luau-language-and-types]]** Store event connections in a table keyed by the instance, then call connections[instance]:Disconnect() to turn behaviour off for that instance; check existence first.
- [8:49](https://youtu.be/Vi2FckNJv9w?t=529) **[[code-architecture-and-frameworks]]** Handle GetInstanceRemovedSignal to undo behaviour when a tag is removed, so toggling a tag (e.g. defusing) cleanly switches behaviour off.
- [10:06](https://youtu.be/Vi2FckNJv9w?t=606) **[[code-architecture-and-frameworks]]** Use CollectionService:AddTag and RemoveTag from any script to enable or disable tagged behaviour globally at runtime.
- [12:12](https://youtu.be/Vi2FckNJv9w?t=732) **[[code-architecture-and-frameworks]]** Instances can carry multiple tags, letting you combine behaviours; duplicate a tagged part to add more instances without adding scripts.
- [12:12](https://youtu.be/Vi2FckNJv9w?t=732) **[[code-architecture-and-frameworks]]** Tag-based component systems such as Knit's component system use these tag add/remove signals to attach and detach components.
- [2:11](https://youtu.be/Vi2FckNJv9w?t=131) **[[code-architecture-and-frameworks]]** When checking a hit's character, use hit:FindFirstAncestor to find the Model and check for a Humanoid, so NPCs and zombies work, not only Players.

## Numbers
- [10:06](https://youtu.be/Vi2FckNJv9w?t=606) Demo timing: **5 s wait before AddTag, 5 s before RemoveTag** (Test script delays used to demonstrate runtime tag toggling)

## Tools
CollectionService, Tag Window / Tag Editor plugin (Studio), Knit component system

## He points to
- Knit framework component system
- Tag Editor plugin (linked in description)
- CollectionService API documentation

## Quotes
- [2:53](https://youtu.be/Vi2FckNJv9w?t=173) "CollectionService is basically a way to centralize your scripts for a situation like this and keep all of your code in one spot that you can change on the fly."

## Topics
[[code-architecture-and-frameworks]] [[common-mistakes]] [[luau-language-and-types]]

Back to [[BRicey - How to make successful Roblox games]]
