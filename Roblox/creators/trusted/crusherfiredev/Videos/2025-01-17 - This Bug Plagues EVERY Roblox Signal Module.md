---
title: "This Bug Plagues EVERY Roblox Signal Module..."
url: https://youtu.be/yevAvHU3ewo
creator: Crusherfire
official: false
advice_density: low
date: 2025-01-17
views: 9561
transcript: auto-captions
confidence: high
tags: [roblox, crusherfiredev, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.7
---

> [!note] Trust: TRUSTED (credibility audit score 8.7): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# This Bug Plagues EVERY Roblox Signal Module...

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Watch](https://youtu.be/yevAvHU3ewo) | crusherfiredev | 9,561 views | 2025-01-17

## Summary
Debugging a Roblox signal-module error "cannot spawn nonsuspended coroutine with arguments". Shows it occurs when a thread yielded on a signal's Wait is cancelled before the signal fires, then the signal's Fire passes arguments to the dead thread. Affects Lemon, Good, and Fast Signal. Fix: check coroutine.status == "suspended" before task.spawn.

## Tips
- [4:18](https://youtu.be/yevAvHU3ewo?t=258) **[[scripting-and-performance]]** In signal modules, check coroutine.status(thread) == "suspended" before task.spawn; otherwise a cancelled waiting thread throws 'cannot spawn nonsuspended coroutine with arguments'.
- [1:34](https://youtu.be/yevAvHU3ewo?t=94) **[[testing-debugging-and-qa]]** Reproduce signal errors by cancelling a waiting thread with task.cancel before the signal fires, then firing with arguments; the stack trace points only at the signal module.
- [0:00](https://youtu.be/yevAvHU3ewo?t=0) **[[testing-debugging-and-qa]]** Use breakpoints to identify which specific signal is firing when a stack trace from a signal module is unhelpful.

## Tools
Roblox Studio, Lemon Signal, Good Signal, Fast Signal

## Topics
[[scripting-and-performance]] [[testing-debugging-and-qa]]

Back to [[crusherfiredev - How to make successful Roblox games]]
