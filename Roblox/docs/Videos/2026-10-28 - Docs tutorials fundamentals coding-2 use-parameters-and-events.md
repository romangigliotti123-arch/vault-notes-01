---
title: "Docs: tutorials / fundamentals / coding-2 / use-parameters-and-events"
url: https://create.roblox.com/docs/tutorials/fundamentals/coding-2/use-parameters-and-events.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: tutorials / fundamentals / coding-2 / use-parameters-and-events

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/tutorials/fundamentals/coding-2/use-parameters-and-events.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox Creator Docs lesson on parameters and events. Shows how to write a function with a parameter, connect it to a part's Touched event, and build a trap that destroys whatever touches it. Explains the difference between parameters (passing outside information into a function) and events (signals fired when something happens).

## Tips
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-2/use-parameters-and-events) **[[common-mistakes]]** Anchor the trap part and keep it from touching anything when placed; otherwise it may fire too early or fall and destroy things unintentionally.
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-2/use-parameters-and-events) **[[luau-language-and-types]]** Use a parameter to pass information a function cannot otherwise see (out-of-scope values) instead of hardcoding it.
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-2/use-parameters-and-events) **[[scripting-and-performance]]** Connect functions to events with Event:Connect(functionName) so they run each time the event fires, e.g. trap.Touched:Connect(onTouch).
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-2/use-parameters-and-events) **[[testing-debugging-and-qa]]** When an event handler does nothing, check the Output window for a test print, verify the print is inside the function, and confirm event names are capitalized correctly (Touched).

## Tools
Roblox Studio, Explorer, Output window

## Topics
[[common-mistakes]] [[luau-language-and-types]] [[scripting-and-performance]] [[testing-debugging-and-qa]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
