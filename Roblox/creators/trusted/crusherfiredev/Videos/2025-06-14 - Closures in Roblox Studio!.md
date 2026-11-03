---
title: "Closures in Roblox Studio!"
url: https://youtu.be/oUjrs6Apd7A
creator: Crusherfire
official: false
advice_density: low
date: 2025-06-14
views: 10182
transcript: auto-captions
confidence: high
tags: [roblox, crusherfiredev, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.7
---

> [!note] Trust: TRUSTED (credibility audit score 8.7): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Closures in Roblox Studio!

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Watch](https://youtu.be/oUjrs6Apd7A) | crusherfiredev | 10,182 views | 2025-06-14

## Summary
Explains Luau closures (captured upvalues, upvalue cells, ~32+28n bytes memory cost), Luau's closure caching rules (cached when no upvalues or only module-scope immutable ones, or pure), and how to avoid closures in signal connections using variadic arguments (Lemon Signal, Future, task.spawn). Argues micro-optimizing closures is usually unnecessary; make it work first.

## Tips
- [14:24](https://youtu.be/oUjrs6Apd7A?t=864) **[[luau-language-and-types]]** Avoid capturing per-instance locals in lambdas in hot paths; pass values as arguments (task.spawn, Future.new) so Luau can cache the function instead of allocating a closure.
- [16:37](https://youtu.be/oUjrs6Apd7A?t=997) **[[code-architecture-and-frameworks]]** Use a signal library supporting variadic connection args (e.g. Lemon Signal) to pass extra values to handlers without creating closures.
- [11:53](https://youtu.be/oUjrs6Apd7A?t=713) **[[luau-language-and-types]]** Keep functions pure where practical: rely only on inputs, not outer locals, so the compiler can cache them.
- [8:55](https://youtu.be/oUjrs6Apd7A?t=535) **[[luau-language-and-types]]** Declare shared values at module/script scope; closures accessing only immutable module-scope upvalues are cached by Luau.

## Numbers
- [5:09](https://youtu.be/oUjrs6Apd7A?t=309) Closure memory: **~32 + 28n bytes per closure (n = external upvalues)** (Per Lua creators' article; n is number of upvalues used)
- [23:45](https://youtu.be/oUjrs6Apd7A?t=1425) Measured memory increase: **+1,644,000 bytes for 10,000 closures with 5 upvalues each** (Lua heap snapshot comparison; predicted ~1.72 MB)
- [19:51](https://youtu.be/oUjrs6Apd7A?t=1191) Upvalue limit: **200** (Max upvalues/local registers per scope before error)
- [9:36](https://youtu.be/oUjrs6Apd7A?t=576) Loop closure test: **10 iterations → 10 distinct closures when capturing loop variable** (Capturing per-iteration local prevents caching)

## Tools
Roblox Studio, Lemon Signal, Future, Roblox Studio Lua heap snapshot (F9 console)

## Topics
[[code-architecture-and-frameworks]] [[development-process-and-speed]] [[luau-language-and-types]]

Back to [[crusherfiredev - How to make successful Roblox games]]
