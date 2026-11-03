---
title: "Docs: tutorials / fundamentals / coding-6 / coding-concept-abstraction"
url: https://create.roblox.com/docs/tutorials/fundamentals/coding-6/coding-concept-abstraction.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: tutorials / fundamentals / coding-6 / coding-concept-abstraction

[Open](https://create.roblox.com/docs/tutorials/fundamentals/coding-6/coding-concept-abstraction.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page explaining abstraction in coding: hide unnecessary detail behind reusable functions. Uses an in-game backpack shop example to show how copied code with small changes should be replaced by one function that looks up name, price and capacity in a table.

## Tips
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-6/coding-concept-abstraction) **[[code-architecture-and-frameworks]]** Abstract code that is reused with small changes each time; identify what stays the same and what differs, then pull out only the differing values.
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-6/coding-concept-abstraction) **[[code-architecture-and-frameworks]]** Replace copy-pasted per-item scripts with one function that searches a table for unique data, so updates happen in one place.
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-6/coding-concept-abstraction) **[[code-architecture-and-frameworks]]** Plan abstractions before scaling: adding 20 more items, per-item capacity differences, or a sitewide sale is painful with duplicated scripts and easy with one abstraction.
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-6/coding-concept-abstraction) **[[code-architecture-and-frameworks]]** Expose only the variables that change (e.g., a settings script with unique values) and hide the rest in a module, keeping beginners focused.
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-6/coding-concept-abstraction) **[[combat-and-gameplay-systems]]** Good abstraction candidates in games include trap parts with different harm values, random power-up award functions, and character classes.

## Numbers
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-6/coding-concept-abstraction) Shop example pricing: **Yellow Backpack 10 Robux; Violet Backpack 25 Robux** (Illustrative duplicated backpack scripts with different name and price)
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-6/coding-concept-abstraction) Holiday sale example: **25% off all backpacks** (Example of a sitewide discount that is easy to apply with one abstraction)

## Games
- **Galactic Speedway**: Settings script holds only the driftspeeder's unique variables; the rest is hidden so new coders stay focused.
- **Story Game Creator Challenge**: Students call getInput() from a StoryMaker module to create questions without viewing the module's code.

## Tools
Roblox Studio, Luau ModuleScripts

## He points to
- Roblox Creator Docs: Coding concept - abstraction

## Topics
[[code-architecture-and-frameworks]] [[combat-and-gameplay-systems]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
