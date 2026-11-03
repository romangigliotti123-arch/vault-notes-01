---
title: "Avoiding wait() and why"
url: https://devforum.roblox.com/t/avoiding-wait-and-why/244015
creator: Roblox DevForum
official: false
advice_density: high
date: 2019-02-23
views: 1241
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Avoiding wait() and why

[Open](https://devforum.roblox.com/t/avoiding-wait-and-why/244015) | Roblox DevForum | 1,241 views | 2019-02-23

## Summary
Kampfkarren argues wait() has no place in production Luau. Explains polling pitfalls (repeat wait() until, while not flag do wait()), replaces them with BindableEvent:Wait(), Instance events like CharacterAdded:Wait(), and RunService Heartbeat/Stepped:Wait(), which are at least 2x faster.

## Tips
- [page](https://devforum.roblox.com/t/avoiding-wait-and-why/244015) **[[luau-language-and-types]]** Never use wait() in production code; treat it as a code smell signalling a design problem.
- [page](https://devforum.roblox.com/t/avoiding-wait-and-why/244015) **[[luau-language-and-types]]** Replace polling loops (repeat wait() until flag) with event-based yielding, e.g. event.Event:Wait(), so code resumes the instant the condition is met.
- [page](https://devforum.roblox.com/t/avoiding-wait-and-why/244015) **[[luau-language-and-types]]** Guard against already-fired events: check the flag first (if not called then event.Event:Wait()) to avoid yielding unnecessarily.
- [page](https://devforum.roblox.com/t/avoiding-wait-and-why/244015) **[[client-server-and-remotes]]** Use player.Character or player.CharacterAdded:Wait() to get the character immediately if present, otherwise wait for it.
- [page](https://devforum.roblox.com/t/avoiding-wait-and-why/244015) **[[luau-language-and-types]]** Yield on Roblox events such as ChildAdded, AncestryChanged, ChildRemoved, CharacterAdded, or RunService.Heartbeat instead of polling.
- [page](https://devforum.roblox.com/t/avoiding-wait-and-why/244015) **[[testing-debugging-and-qa]]** If wait() seems to fix a Roblox bug, use RunService.Heartbeat:Wait() or Stepped:Wait() instead; they are at least 2x faster and worked where wait() did.
- [page](https://devforum.roblox.com/t/avoiding-wait-and-why/244015) **[[optimization-and-streaming]]** wait() can overshoot by seconds and grows worse the more it is called, causing laggy gameplay; avoid it for performance.

## Numbers
- [page](https://devforum.roblox.com/t/avoiding-wait-and-why/244015) Speed comparison: **RunService.Heartbeat:Wait()/Stepped:Wait() at least 2x faster than wait()** (Author's claim for replacing wait() in bug workarounds)
- [page](https://devforum.roblox.com/t/avoiding-wait-and-why/244015) wait() overshoot: **Can last seconds, not microseconds** (Author's description of wait() delay problems)

## He points to
- Kampfkarren Twitter thread (original)

## Quotes
- [page](https://devforum.roblox.com/t/avoiding-wait-and-why/244015) "In my opinion, wait() has no place in production code."
- [page](https://devforum.roblox.com/t/avoiding-wait-and-why/244015) "wait() is code smell, meaning using it is the sign of a design problem."

## Topics
[[client-server-and-remotes]] [[luau-language-and-types]] [[optimization-and-streaming]] [[testing-debugging-and-qa]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
