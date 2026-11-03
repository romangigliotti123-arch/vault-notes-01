---
title: "How to Use Coroutines in Roblox (Studio)"
url: https://youtu.be/nEVaMJpd1Ag
creator: XTB7
official: false
advice_density: low
date: 2023-10-28
views: 1336
transcript: auto-captions
confidence: high
tags: [roblox, xtb7-dev, youtube-learn]
creator_trust: MIXED
creator_score: 7.3
---

> [!note] Trust: MIXED (credibility audit score 7.3): do not rely on this creator alone; confirm a recommendation with a second source. See [[creator-credibility]].

# How to Use Coroutines in Roblox (Studio)

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Watch](https://youtu.be/nEVaMJpd1Ag) | xtb7-dev | 1,336 views | 2023-10-28

## Summary
Beginner tutorial on Luau coroutines in Roblox Studio: creating coroutines with coroutine.create/resume, stopping with close, pausing and returning values with yield, checking status/isyieldable/running, and wrapping functions with coroutine.wrap. Includes a sponsor segment, which is skipped.

## Tips
- [0:51](https://youtu.be/nEVaMJpd1Ag?t=51) **[[luau-language-and-types]]** Use coroutines so a looping function does not block the thread; otherwise a while-true loop in one function prevents other functions from running.
- [2:16](https://youtu.be/nEVaMJpd1Ag?t=136) **[[luau-language-and-types]]** Create a coroutine with coroutine.create(fn), then start it with coroutine.resume(co). Creating alone does nothing.
- [3:18](https://youtu.be/nEVaMJpd1Ag?t=198) **[[luau-language-and-types]]** Stop a coroutine with coroutine.close(co) instead of relying on globals or leaving infinite loops running.
- [4:26](https://youtu.be/nEVaMJpd1Ag?t=266) **[[luau-language-and-types]]** Use coroutine.yield() inside a coroutine to suspend it; it resumes from that point on the next coroutine.resume call.

## Tools
Roblox Studio, Luau, task.wait

## Topics
[[luau-language-and-types]]

Back to [[xtb7-dev - How to make successful Roblox games]]
