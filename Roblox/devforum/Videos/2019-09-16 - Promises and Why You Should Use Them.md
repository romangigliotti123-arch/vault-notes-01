---
title: "Promises and Why You Should Use Them"
url: https://devforum.roblox.com/t/promises-and-why-you-should-use-them/350825
creator: Roblox DevForum
official: false
advice_density: medium
date: 2019-09-16
views: 727
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Promises and Why You Should Use Them

[Open](https://devforum.roblox.com/t/promises-and-why-you-should-use-them/350825) | Roblox DevForum | 727 views | 2019-09-16

## Summary
Evaera's introduction to Promises for Roblox Lua: why coroutine yielding causes bugs, how Promise.new/andThen/catch/await/all/race work, cancellation via onCancel, propagation, and promisify for existing yielding functions.

## Tips
- [page](https://devforum.roblox.com/t/promises-and-why-you-should-use-them/350825) **[[code-architecture-and-frameworks]]** Wrap yielding functions in Promises so callers know the call is async; calling a Promise-returning function never yields, making yield bugs and race conditions easier to avoid.
- [page](https://devforum.roblox.com/t/promises-and-why-you-should-use-them/350825) **[[client-server-and-remotes]]** Use Promise.promisify to turn existing yielding functions (e.g. GetAsync-style APIs) into Promise-returning ones without rewriting them.
- [page](https://devforum.roblox.com/t/promises-and-why-you-should-use-them/350825) **[[common-mistakes]]** Always attach a catch to Promise chains; the library warns in the console when a chain errors without a catch handler.
- [page](https://devforum.roblox.com/t/promises-and-why-you-should-use-them/350825) **[[luau-language-and-types]]** Use Promise.all to run independent async operations concurrently instead of sequentially when waiting is wasteful.
- [page](https://devforum.roblox.com/t/promises-and-why-you-should-use-them/350825) **[[luau-language-and-types]]** Use promise:cancel() with an onCancel hook (e.g. cancelling tweens) to stop work when a menu closes, an ability is interrupted, or a cutscene is skipped.
- [page](https://devforum.roblox.com/t/promises-and-why-you-should-use-them/350825) **[[code-architecture-and-frameworks]]** Use finally for cleanup that must run whether a Promise resolves, rejects, or is cancelled.
- [page](https://devforum.roblox.com/t/promises-and-why-you-should-use-them/350825) **[[code-architecture-and-frameworks]]** Centralise async logic in one Promise library so all async APIs behave consistently and compose; ad-hoc pcall/success-flag patterns diverge and cause usage mistakes.

## Tools
Promise library (evaera / LPGhatguy, Roblox Lua), NevermoreEngine Promise implementation (no cancellation), HttpService:GetAsync, TweenService

## He points to
- NevermoreEngine

## Topics
[[client-server-and-remotes]] [[code-architecture-and-frameworks]] [[common-mistakes]] [[luau-language-and-types]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
