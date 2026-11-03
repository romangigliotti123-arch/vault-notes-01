---
title: "Coroutines - When and how to use them"
url: https://devforum.roblox.com/t/coroutines-when-and-how-to-use-them/541683
creator: Roblox DevForum
official: false
advice_density: medium
date: 2020-04-25
views: 294
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Coroutines - When and how to use them

[Open](https://devforum.roblox.com/t/coroutines-when-and-how-to-use-them/541683) | Roblox DevForum | 294 views | 2020-04-25

## Summary
Community tutorial by ReturnedTrue explaining Lua coroutines in Roblox: thread concept, coroutine statuses, create/resume vs wrap, using coroutines to avoid yielding main loops and async class methods, yield-based iterators, error handling, and spawn/FastSpawn alternatives.

## Tips
- [page](https://devforum.roblox.com/t/coroutines-when-and-how-to-use-them/541683) **[[luau-language-and-types]]** Wrap blocking while-loops (e.g. round loops with wait) in coroutine.wrap so code after them still runs; remember to call the wrapped function.
- [page](https://devforum.roblox.com/t/coroutines-when-and-how-to-use-them/541683) **[[luau-language-and-types]]** Prefer coroutine.wrap over create/resume for convenience; it returns a callable function, though it does not return the success boolean.
- [page](https://devforum.roblox.com/t/coroutines-when-and-how-to-use-them/541683) **[[common-mistakes]]** Avoid spawn() due to reported delays (up to 15 seconds); coroutines or task-based alternatives are preferred.
- [page](https://devforum.roblox.com/t/coroutines-when-and-how-to-use-them/541683) **[[common-mistakes]]** Be aware a FastSpawn BindableEvent trick runs in the main thread's error scope; an error in its body will affect the main thread.
- [page](https://devforum.roblox.com/t/coroutines-when-and-how-to-use-them/541683) **[[client-server-and-remotes]]** Coroutines are non-preemptive; a blocking call inside any coroutine or the main thread stalls the whole program, so don't rely on them for true parallelism.
- [page](https://devforum.roblox.com/t/coroutines-when-and-how-to-use-them/541683) **[[scripting-and-performance]]** Errors inside a coroutine do not crash the main thread; check coroutine.resume's returned success value to handle failures.

## Numbers
- [page](https://devforum.roblox.com/t/coroutines-when-and-how-to-use-them/541683) spawn() delay: **up to 15 seconds** (Author's cited horror story for spawn())
- [page](https://devforum.roblox.com/t/coroutines-when-and-how-to-use-them/541683) coroutine status types: **4 (suspended, running, normal, dead)** (Statuses returned by coroutine.status)

## He points to
- PiL Chapter 9
- Roblox Developer Hub coroutine article
- Roblox Developer Hub coroutine API reference

## Topics
[[client-server-and-remotes]] [[common-mistakes]] [[luau-language-and-types]] [[scripting-and-performance]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
