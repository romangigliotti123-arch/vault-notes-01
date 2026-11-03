---
title: "Introducing ReflectionService: Programmatic Access to Engine API Information"
url: https://devforum.roblox.com/t/introducing-reflectionservice-programmatic-access-to-engine-api-information/4078522
creator: Roblox DevForum
official: false
advice_density: low
date: 2025-11-18
views: 617
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Introducing ReflectionService: Programmatic Access to Engine API Information

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://devforum.roblox.com/t/introducing-reflectionservice-programmatic-access-to-engine-api-information/4078522) | Roblox DevForum | 617 views | 2025-11-18

## Summary
Announces ReflectionService, a Luau service for programmatically inspecting the engine API (classes, properties, methods, events) filtered by SecurityCapabilities. Covers GetClass, GetClasses, GetPropertiesOfClass, and a Feb 2026 update adding GetMethodsOfClass, GetEventsOfClass, Owner and Serialized fields. Includes a plugin example that instantiates every creatable class.

## Tips
- [page](https://devforum.roblox.com/t/introducing-reflectionservice-programmatic-access-to-engine-api-information/4078522) **[[ai-and-tools]]** Use ReflectionService to build API inspection plugins that analyze new engine API releases, or Studio plugins that change instance classes faster.
- [page](https://devforum.roblox.com/t/introducing-reflectionservice-programmatic-access-to-engine-api-information/4078522) **[[scripting-and-performance]]** Pass a Security filter to GetClasses to query as a specific context; default output depends on the calling script's SecurityCapabilities (Plugin, ModuleScript, or regular script).
- [page](https://devforum.roblox.com/t/introducing-reflectionservice-programmatic-access-to-engine-api-information/4078522) **[[version-control-and-tooling]]** Use GetPropertiesOfClass to check whether a property is serialized (saved/loaded) and its security level before building tooling around it.

## Numbers
- [page](https://devforum.roblox.com/t/introducing-reflectionservice-programmatic-access-to-engine-api-information/4078522) Update date: **February 12, 2026 (GetMethodsOfClass, GetEventsOfClass, Owner, Serialized added)**

## Tools
ReflectionService, SecurityCapabilities, ChangeHistoryService, Plugin toolbar API

## Topics
[[ai-and-tools]] [[scripting-and-performance]] [[version-control-and-tooling]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
