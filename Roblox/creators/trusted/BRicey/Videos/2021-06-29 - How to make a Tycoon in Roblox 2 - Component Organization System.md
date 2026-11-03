---
title: "How to make a Tycoon in Roblox #2 - Component Organization System"
url: https://youtu.be/stJtnGGt-1c
creator: B Ricey
official: false
advice_density: medium
date: 2021-06-29
views: 84830
transcript: manual-subs
confidence: high
tags: [roblox, bricey, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.0
---

> [!note] Trust: TRUSTED (credibility audit score 8.0): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# How to make a Tycoon in Roblox #2 - Component Organization System

[Watch](https://youtu.be/stJtnGGt-1c) | BRicey | 84,830 views | 2021-06-29

## Summary
Part 2 of a Roblox tycoon series: implements the component pattern using CollectionService tags. Covers installing the Tag Editor plugin, tagging a part "Test", building a Components folder of module scripts, a Tycoon:CreateComponent and AddComponents function that reads GetTags() and only creates components whose module exists, and testing with Init().

## Tips
- [3:32](https://youtu.be/stJtnGGt-1c?t=212) **[[building-and-level-design]]** Use the Tag Editor plugin to tag parts; verify tags via World View, which colors tagged instances and shows their tag names on hover.
- [9:53](https://youtu.be/stJtnGGt-1c?t=593) **[[code-architecture-and-frameworks]]** Iterate tags with GetTags() (not GetTagged()) and only create components whose module exists, so stray or third-party tags can't break the game.
- [4:55](https://youtu.be/stJtnGGt-1c?t=295) **[[code-architecture-and-frameworks]]** Give each component module a new() that takes tycoon and instance references, and an Init() that does the setup; keep the tycoon script small by delegating to components.
- [2:50](https://youtu.be/stJtnGGt-1c?t=170) **[[code-architecture-and-frameworks]]** Store a shared Components folder in ServerScriptService and require component modules from it, keeping one module per component type.
- [11:15](https://youtu.be/stJtnGGt-1c?t=675) **[[testing-debugging-and-qa]]** Put the template back in ServerStorage before testing; the test relies on the workspace copy being the one tagged and initialised.

## Numbers
- [4:00](https://youtu.be/stJtnGGt-1c?t=240) Tycoon script size before components: **over 1000 lines (speaker's own project)** (Speaker's tycoon module script after a few months of development)

## Tools
Roblox Studio, CollectionService, Tag Editor plugin, World View plugin, GitHub repository (code samples)

## He points to
- Tag Editor plugin install link (description)
- Video on CollectionService (linked)
- Video on the component pattern/composition (linked)

## Quotes
- [9:53](https://youtu.be/stJtnGGt-1c?t=593) "In a complex game, you might accidentally add another tag that you weren't meaning to... it could break your game."
- [0:00](https://youtu.be/stJtnGGt-1c?t=0) "A tycoon with a module script with over a thousand lines of code, and that was a very painful experience."

## Topics
[[building-and-level-design]] [[code-architecture-and-frameworks]] [[testing-debugging-and-qa]]

Back to [[BRicey - How to make successful Roblox games]]
