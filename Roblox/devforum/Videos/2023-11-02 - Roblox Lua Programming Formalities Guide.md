---
title: "Roblox Lua Programming Formalities Guide"
url: https://devforum.roblox.com/t/roblox-lua-programming-formalities-guide/2672585
creator: Roblox DevForum
official: false
advice_density: high
date: 2023-11-02
views: 60
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Roblox Lua Programming Formalities Guide

[Open](https://devforum.roblox.com/t/roblox-lua-programming-formalities-guide/2672585) | Roblox DevForum | 60 views | 2023-11-02

## Summary
Opinionated programming style guide for Roblox projects covering decomposition, information hiding, function documentation, Explorer organization, module placement, MarketplaceService ProcessReceipt routing, ProfileService-based DataManager, naming conventions, section layout, and a UIVisibilityManager for overlapping UI. Explicitly not a professional standard.

## Tips
- [page](https://devforum.roblox.com/t/roblox-lua-programming-formalities-guide/2672585) **[[development-process-and-speed]]** Decompose problems into small tasks, then subtasks; each subtask becomes its own function to enable reuse and easier future changes.
- [page](https://devforum.roblox.com/t/roblox-lua-programming-formalities-guide/2672585) **[[code-architecture-and-frameworks]]** Document functions with pre-conditions, post-conditions, return values, side effects and whether they yield, so others can use them without reading internals.
- [page](https://devforum.roblox.com/t/roblox-lua-programming-formalities-guide/2672585) **[[testing-debugging-and-qa]]** Test functions individually with inputs whose correct output you know, include error-prone inputs, and ensure every line runs at least once; retest prior inputs after each fix.
- [page](https://devforum.roblox.com/t/roblox-lua-programming-formalities-guide/2672585) **[[code-architecture-and-frameworks]]** Keep ReplicatedFirst for loading screen only; put assets in ReplicatedStorage subfolders by system (Assets, Inventory, PetsStorage, Modules).
- [page](https://devforum.roblox.com/t/roblox-lua-programming-formalities-guide/2672585) **[[code-architecture-and-frameworks]]** Place a module with its single consumer script if only one script uses it; use ServerStorage/ServerScriptService for server-only modules and ReplicatedStorage for shared ones. Keep one copy per module.
- [page](https://devforum.roblox.com/t/roblox-lua-programming-formalities-guide/2672585) **[[code-architecture-and-frameworks]]** Keep a Common Functions module for shared helpers and global constants, and a Notes module (block comments only) for todos and bugs.
- [page](https://devforum.roblox.com/t/roblox-lua-programming-formalities-guide/2672585) **[[monetisation-devproducts]]** Store all gamepass and product IDs in one ReplicatedStorage module grouped by category so clients and server scripts share one source.
- [page](https://devforum.roblox.com/t/roblox-lua-programming-formalities-guide/2672585) **[[anti-exploit-and-security]]** Use a single MarketplaceService.ProcessReceipt handler that classifies the product ID and routes to a per-category module, since only one ProcessReceipt callback can exist.
- [page](https://devforum.roblox.com/t/roblox-lua-programming-formalities-guide/2672585) **[[data-persistence]]** Load player data via ProfileService in a DataManager module, expose it through a dictionary for server scripts, and have clients request data via remotes rather than reading it directly.
- [page](https://devforum.roblox.com/t/roblox-lua-programming-formalities-guide/2672585) **[[data-persistence]]** Save purchase receipts (PurchaseId) in a PurchaseLog within player data to guard against duplicate processing.
- [page](https://devforum.roblox.com/t/roblox-lua-programming-formalities-guide/2672585) **[[ui-ux-design]]** Route all UI open/close through a single visibility manager keyed by screen position so overlapping frames close automatically; distinguish temporary frames from default HUD frames.
- [page](https://devforum.roblox.com/t/roblox-lua-programming-formalities-guide/2672585) **[[common-mistakes]]** Do not put scripts directly under StarterGui; wrap local scripts in a ScreenGui.
- [page](https://devforum.roblox.com/t/roblox-lua-programming-formalities-guide/2672585) **[[code-architecture-and-frameworks]]** Keep scripts roughly under ~1000 lines and sections under ~100 lines; avoid folders of many ~50-line scripts that are hard to navigate.
- [page](https://devforum.roblox.com/t/roblox-lua-programming-formalities-guide/2672585) **[[luau-language-and-types]]** Name objects PascalCase, primitives and functions camelCase, constants UPPERCASE, use underscore for unused loop variables, and avoid 3-4 character or vague names like data or connection.
- [page](https://devforum.roblox.com/t/roblox-lua-programming-formalities-guide/2672585) **[[code-architecture-and-frameworks]]** Use a fixed top-of-script layout: services, modules, instances, then remaining variables; split long scripts into commented sections with clear titles.
- [page](https://devforum.roblox.com/t/roblox-lua-programming-formalities-guide/2672585) **[[ai-and-tools]]** Use the open-source modules BridgeNet2, TopbarPlus, ProfileService and similar rather than rebuilding them; keep only one copy in the project.

## Numbers
- [page](https://devforum.roblox.com/t/roblox-lua-programming-formalities-guide/2672585) Author experience: **4 years Roblox development, team of 8 programmers** (Author's stated background for the guide)
- [page](https://devforum.roblox.com/t/roblox-lua-programming-formalities-guide/2672585) Script length guideline: **Under ~1000 lines per script** (Split larger scripts into modules)
- [page](https://devforum.roblox.com/t/roblox-lua-programming-formalities-guide/2672585) Section length guideline: **Not 100+ lines per section** (Commented section breaks in scripts)

## Tools
ProfileService, BridgeNet2, TopbarPlus, MarketplaceService, Roblox Studio Explorer

## He points to
- Lua Style Guide
- MadLife Code Guidebook

## Quotes
- [page](https://devforum.roblox.com/t/roblox-lua-programming-formalities-guide/2672585) "This is NOT a professional standard guide. It is entirely possible that any information here may not be 100% factually correct."
- [page](https://devforum.roblox.com/t/roblox-lua-programming-formalities-guide/2672585) "Copying 1 for 1 from this guide may not be completely applicable to your development needs."

## Topics
[[ai-and-tools]] [[anti-exploit-and-security]] [[code-architecture-and-frameworks]] [[common-mistakes]] [[data-persistence]] [[development-process-and-speed]] [[luau-language-and-types]] [[monetisation-devproducts]] [[testing-debugging-and-qa]] [[ui-ux-design]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
