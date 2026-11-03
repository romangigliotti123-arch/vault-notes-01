---
title: "How to write great code and speed up everything"
url: https://devforum.roblox.com/t/how-to-write-great-code-and-speed-up-everything/2666661
creator: Roblox DevForum
official: false
advice_density: high
date: 2023-10-29
views: 113
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# How to write great code and speed up everything

[Open](https://devforum.roblox.com/t/how-to-write-great-code-and-speed-up-everything/2666661) | Roblox DevForum | 113 views | 2023-10-29

## Summary
Hexcede's long guide on writing clean Roblox code: Git branching and rebasing, Rojo and Wally workflow, and architecture patterns (signals, Trove, Observers, Components, Promises). Argues for module-to-module structure over frameworks like Knit, and for avoiding circular dependencies.

## Tips
- [page](https://devforum.roblox.com/t/how-to-write-great-code-and-speed-up-everything/2666661) **[[version-control-and-tooling]]** Use Git with Rojo and Wally; the Luau LSP VS Code extension gives the same typechecking as Studio.
- [page](https://devforum.roblox.com/t/how-to-write-great-code-and-speed-up-everything/2666661) **[[version-control-and-tooling]]** Make each feature its own branch; rebase main into feature branches often and merge features into main, to avoid merge conflicts.
- [page](https://devforum.roblox.com/t/how-to-write-great-code-and-speed-up-everything/2666661) **[[code-architecture-and-frameworks]]** Use signals as the cure for circular dependencies; expose GetXSignal methods so other modules react without the source knowing about them.
- [page](https://devforum.roblox.com/t/how-to-write-great-code-and-speed-up-everything/2666661) **[[code-architecture-and-frameworks]]** Split features by concept and behaviour; keep dependency direction one-way so changes affect only dependents.
- [page](https://devforum.roblox.com/t/how-to-write-great-code-and-speed-up-everything/2666661) **[[code-architecture-and-frameworks]]** Prefer plain module-to-module requires over frameworks; frameworks invert coupling and can weaken type inference (e.g. Knit).
- [page](https://devforum.roblox.com/t/how-to-write-great-code-and-speed-up-everything/2666661) **[[code-architecture-and-frameworks]]** Treat modules as nearly costless when they clarify structure; split when the concept is distinct, keep together when it is not.
- [page](https://devforum.roblox.com/t/how-to-write-great-code-and-speed-up-everything/2666661) **[[data-persistence]]** Use Promises for loading player data; discard or cancel the promise if the player leaves so callbacks never run.
- [page](https://devforum.roblox.com/t/how-to-write-great-code-and-speed-up-everything/2666661) **[[development-process-and-speed]]** Clean code is usually faster and easier to optimise where it matters; avoid over-optimising at the cost of readability.
- [page](https://devforum.roblox.com/t/how-to-write-great-code-and-speed-up-everything/2666661) **[[code-architecture-and-frameworks]]** Use Trove for cleanup: create a trove in the object constructor, connect events into it, and call :Clean() on destroy to avoid leaks.
- [page](https://devforum.roblox.com/t/how-to-write-great-code-and-speed-up-everything/2666661) **[[code-architecture-and-frameworks]]** Use Observers (Observe library) to handle existing and future players, children or attributes, and return cleanup functions from callbacks.
- [page](https://devforum.roblox.com/t/how-to-write-great-code-and-speed-up-everything/2666661) **[[code-architecture-and-frameworks]]** Model objects as components (binder pattern) attached via CollectionService tags, with each component cleaning up its behaviours on removal.
- [page](https://devforum.roblox.com/t/how-to-write-great-code-and-speed-up-everything/2666661) **[[code-architecture-and-frameworks]]** Use Promises for waiting on components and add them to a Trove with AddPromise so waits are cancelled when no longer needed.
- [page](https://devforum.roblox.com/t/how-to-write-great-code-and-speed-up-everything/2666661) **[[luau-language-and-types]]** Use Promise :andThen and :catch as chainable transforms; they return new promises resolving to the callback result, enabling clean sequencing.

## Numbers
- [page](https://devforum.roblox.com/t/how-to-write-great-code-and-speed-up-everything/2666661) Observe library version: **0.1.4 (example used)** (Observe library example referenced in the guide)

## Tools
Git, GitHub Desktop, Rojo, Wally, Luau LSP, Knit, Promise, Trove

## He points to
- Hexcede: How you should secure your game (DevForum)
- Hexcede: Scripting Basics beginner guide (DevForum)
- Hexcede: Garbage Collection and Memory Leaks in Roblox (DevForum)
- Hexcede: Network Optimization (2021) (DevForum)
- Hexolus server-sided anticheat (open source)

## Quotes
- [page](https://devforum.roblox.com/t/how-to-write-great-code-and-speed-up-everything/2666661) "Events are the one true cure to circular dependencies."
- [page](https://devforum.roblox.com/t/how-to-write-great-code-and-speed-up-everything/2666661) "Merge features into main, rebase main into features."

## Topics
[[code-architecture-and-frameworks]] [[data-persistence]] [[development-process-and-speed]] [[luau-language-and-types]] [[version-control-and-tooling]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
