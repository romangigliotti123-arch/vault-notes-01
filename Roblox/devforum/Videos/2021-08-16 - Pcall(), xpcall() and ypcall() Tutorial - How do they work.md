---
title: "Pcall(), xpcall() and ypcall() Tutorial - How do they work?"
url: https://devforum.roblox.com/t/pcall-xpcall-and-ypcall-tutorial-how-do-they-work/1417471
creator: Roblox DevForum
official: false
advice_density: low
date: 2021-08-16
views: 145
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Pcall(), xpcall() and ypcall() Tutorial - How do they work?

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://devforum.roblox.com/t/pcall-xpcall-and-ypcall-tutorial-how-do-they-work/1417471) | Roblox DevForum | 145 views | 2021-08-16

## Summary
Tutorial explaining how pcall() and xpcall() work in Luau: pcall returns a success bool and result/error value, commonly used around DataStore GetAsync/SetAsync; xpcall takes an error handler function and does not yield. ypcall() is deprecated since pcall now yields.

## Tips
- [page](https://devforum.roblox.com/t/pcall-xpcall-and-ypcall-tutorial-how-do-they-work/1417471) **[[scripting-and-performance]]** Wrap DataStore GetAsync/SetAsync calls in pcall() since they are network calls that can error.
- [page](https://devforum.roblox.com/t/pcall-xpcall-and-ypcall-tutorial-how-do-they-work/1417471) **[[scripting-and-performance]]** Check the first pcall return value (bool) before using the second value; on false, the second value holds the error message.
- [page](https://devforum.roblox.com/t/pcall-xpcall-and-ypcall-tutorial-how-do-they-work/1417471) **[[luau-language-and-types]]** Do not use ypcall(); it is deprecated because pcall() now yields too.
- [page](https://devforum.roblox.com/t/pcall-xpcall-and-ypcall-tutorial-how-do-they-work/1417471) **[[luau-language-and-types]]** Use xpcall() with a custom error handler function when you need to react to errors; the handler runs only on failure.

## Numbers
- [page](https://devforum.roblox.com/t/pcall-xpcall-and-ypcall-tutorial-how-do-they-work/1417471) ypcall status: **deprecated** (pcall now yields like ypcall did, so ypcall is redundant)

## Tools
pcall, xpcall, warn

## Topics
[[luau-language-and-types]] [[scripting-and-performance]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
