---
title: "If you’re a new Roblox dev, watch this"
url: https://youtu.be/cWfsm8rwgDg
creator: ByteBlox
official: false
advice_density: low
date: 2024-04-05
views: 30112
transcript: auto-captions
confidence: high
tags: [roblox, byteblox100, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.1
---

> [!note] Trust: TRUSTED (credibility audit score 8.1): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# If you’re a new Roblox dev, watch this

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Watch](https://youtu.be/cWfsm8rwgDg) | byteblox100 | 30,112 views | 2024-04-05

## Summary
Beginner-oriented Luau fundamentals walkthrough: multithreading (task.spawn vs wait), enums, ModuleScripts, events vs functions, connections, GUI (ScreenGui, scale vs offset, LocalScripts for buttons, StarterGui vs PlayerGui), services, TweenService, hierarchy/descendants, loops, and server vs client. No game-specific business advice.

## Tips
- [1:02](https://youtu.be/cWfsm8rwgDg?t=62) **[[luau-language-and-types]]** Use task.spawn(fn) to run a function on its own thread so a wait() inside it doesn't block the other calls in a loop.
- [8:05](https://youtu.be/cWfsm8rwgDg?t=485) **[[code-architecture-and-frameworks]]** ModuleScripts never run alone; they return a table of variables/functions that other scripts access via require(module).
- [10:19](https://youtu.be/cWfsm8rwgDg?t=619) **[[luau-language-and-types]]** Use events (e.g. Part.Touched:Connect) to react when something happens, and functions (e.g. :WaitForChild) to act on an object now.
- [16:42](https://youtu.be/cWfsm8rwgDg?t=1002) **[[luau-language-and-types]]** Store a connection in a variable and call :Disconnect() to stop listening; otherwise the event stays connected.

## Tools
Roblox Studio, Luau

## Topics
[[client-server-and-remotes]] [[code-architecture-and-frameworks]] [[luau-language-and-types]] [[scripting-and-performance]] [[ui-ux-design]]

Back to [[byteblox100 - How to make successful Roblox games]]
