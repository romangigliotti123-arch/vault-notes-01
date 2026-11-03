---
title: "Programming Patterns YOU'RE NOT USING!"
url: https://youtu.be/Nqtpzrkwm1Q
creator: Crusherfire
official: false
advice_density: medium
date: 2025-05-24
views: 24988
transcript: auto-captions
confidence: high
tags: [roblox, crusherfiredev, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.7
---

> [!note] Trust: TRUSTED (credibility audit score 8.7): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Programming Patterns YOU'RE NOT USING!

[Watch](https://youtu.be/Nqtpzrkwm1Q) | crusherfiredev | 24,988 views | 2025-05-24

## Summary
Covers five scripting patterns the creator uses: observers (Sleitnick's observer pack plus custom children/descendants/attributes observers) with Trove cleanup, runtime type checking with the T library, a throttle function using os.clock, and a waitWithTimeout wrapper for RBXScriptSignals. Includes a server-authoritative music example.

## Tips
- [2:13](https://youtu.be/Nqtpzrkwm1Q?t=133) **[[code-architecture-and-frameworks]]** Use observers (tag, attribute, children, descendants) instead of manual event wiring; each observer returns a cleanup function you can add to a Trove.
- [4:15](https://youtu.be/Nqtpzrkwm1Q?t=255) **[[code-architecture-and-frameworks]]** Nest observers: e.g. observe a tag, then observe an attribute on each tagged instance, with a value guard to only react to valid values.
- [3:34](https://youtu.be/Nqtpzrkwm1Q?t=214) **[[code-architecture-and-frameworks]]** Put all per-instance connections and loops into a Trove and call clean() when the tag or instance is removed to avoid leaks.
- [8:20](https://youtu.be/Nqtpzrkwm1Q?t=500) **[[code-architecture-and-frameworks]]** Add the observer's cleanup function to a main Trove so disconnecting the whole system tears down all observers.
- [8:52](https://youtu.be/Nqtpzrkwm1Q?t=532) **[[scripting-and-performance]]** Use the T runtime type-checking library (recommended in Roblox docs) to validate values instead of repeated type() comparisons, especially for remote arguments.
- [10:56](https://youtu.be/Nqtpzrkwm1Q?t=656) **[[scripting-and-performance]]** Build T.interface schemas for complex tables and nest interfaces or tuples to validate data passed through RemoteEvents at runtime.
- [13:03](https://youtu.be/Nqtpzrkwm1Q?t=783) **[[scripting-and-performance]]** Wrap sound or effect triggers in a throttle(id, delay, fn) helper so bulk child-added events play only once within the delay window.
- [16:34](https://youtu.be/Nqtpzrkwm1Q?t=994) **[[scripting-and-performance]]** Implement waitWithTimeout with a coroutine plus task.delay race so yields on RBXScriptSignals can time out instead of hanging forever.
- [19:17](https://youtu.be/Nqtpzrkwm1Q?t=1157) **[[matchmaking-and-teleport]]** For server-authoritative audio, have the server wait on Sound.Loaded with a 5-second timeout and skip queue entries that fail to load.

## Numbers
- [4:55](https://youtu.be/Nqtpzrkwm1Q?t=295) Disco part color change interval: **0.25 seconds** (Example loop delay in observer demo)
- [13:03](https://youtu.be/Nqtpzrkwm1Q?t=783) Throttle delay for bulk sound: **0.01 seconds** (Small delay pushes bulk child-added calls to one sound)
- [19:58](https://youtu.be/Nqtpzrkwm1Q?t=1198) Sound load timeout: **5 seconds** (Skip sounds that fail to load in music queue)

## Tools
Sleitnick observer module, Sleitnick Trove, T runtime type-checking library, Roblox Studio

## He points to
- Sleitnick observer video (linked in description)
- T library (linked from Roblox documentation)
- Trove module by Sleitnick

## Topics
[[code-architecture-and-frameworks]] [[matchmaking-and-teleport]] [[scripting-and-performance]]

Back to [[crusherfiredev - How to make successful Roblox games]]
