---
title: "Docs: tutorials / fundamentals / coding-6 / intro-to-module-scripts"
url: https://create.roblox.com/docs/tutorials/fundamentals/coding-6/intro-to-module-scripts.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: tutorials / fundamentals / coding-6 / intro-to-module-scripts

[Open](https://create.roblox.com/docs/tutorials/fundamentals/coding-6/intro-to-module-scripts.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox Creator Docs tutorial explaining ModuleScripts: how to store reusable code in a returned table, add functions/variables with dot syntax, scope with local, and load modules with require() from ServerStorage/ReplicatedStorage. Includes RewardManager example and common error troubleshooting.

## Tips
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-6/intro-to-module-scripts) **[[code-architecture-and-frameworks]]** Put commonly reused code (e.g., coin rewards) in a ModuleScript so changes only need to be made in one place instead of across many scripts.
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-6/intro-to-module-scripts) **[[code-architecture-and-frameworks]]** Use normal Scripts for standalone elements like touching a pickup; use ModuleScripts for logic reused by multiple independent scripts.
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-6/intro-to-module-scripts) **[[scripting-and-performance]]** Place ModuleScripts used by server scripts in ServerScriptService or ServerStorage, and those used by client LocalScripts in ReplicatedStorage.
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-6/intro-to-module-scripts) **[[luau-language-and-types]]** Name module tables in PascalCase (e.g., RewardManager) and regular variables in camelCase.
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-6/intro-to-module-scripts) **[[code-architecture-and-frameworks]]** Always end a ModuleScript with return of the module table; code added after the table is created but outside it can cause errors.
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-6/intro-to-module-scripts) **[[code-architecture-and-frameworks]]** Use the local keyword for module-private variables and functions; omit local only for members that other scripts must access.
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-6/intro-to-module-scripts) **[[testing-debugging-and-qa]]** If you see 'Infinite yield possible' or 'not a valid member', check the require() path and spelling against the actual ModuleScript name.
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-6/intro-to-module-scripts) **[[testing-debugging-and-qa]]** If you see 'attempt to index global', confirm the script loads the module with require(); otherwise it cannot use the module's functions.
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-6/intro-to-module-scripts) **[[code-architecture-and-frameworks]]** Copy exact function/variable names from the module and paste them into calling scripts to avoid spelling mismatches.

## Numbers
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-6/intro-to-module-scripts) Example difficulty multipliers: **easy 0.5, normal 1, hard 2 (base reward 50 coins)** (RewardManager example in the docs)

## Tools
Roblox Studio, ModuleScript, require()

## He points to
- Advanced Module Scripts guide (Roblox Creator Docs)

## Topics
[[code-architecture-and-frameworks]] [[luau-language-and-types]] [[scripting-and-performance]] [[testing-debugging-and-qa]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
