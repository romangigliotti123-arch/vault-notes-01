---
title: "how to DEBUG the PROPER way - ROBLOX Studio"
url: https://youtu.be/vj55DK8aH3s
creator: Crusherfire
official: false
advice_density: medium
date: 2024-04-28
views: 11750
transcript: auto-captions
confidence: high
tags: [roblox, crusherfiredev, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.7
---

> [!note] Trust: TRUSTED (credibility audit score 8.7): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# how to DEBUG the PROPER way - ROBLOX Studio

[Watch](https://youtu.be/vj55DK8aH3s) | crusherfiredev | 11,750 views | 2024-04-28

## Summary
Tutorial on debugging Luau code in Roblox Studio: print statements vs breakpoints, breakpoint settings (conditions, log messages, continue execution), step into/over/out, Watch window, Call Stack window, and Script Analysis window for linter warnings.

## Tips
- [0:00](https://youtu.be/vj55DK8aH3s?t=0) **[[testing-debugging-and-qa]]** Use print statements for quick checks, but switch to breakpoints when you need to inspect state mid-playtest without stopping and editing code.
- [1:21](https://youtu.be/vj55DK8aH3s?t=81) **[[testing-debugging-and-qa]]** Click the red dot in the gutter next to a line number to add a breakpoint; right-click it to disable, delete, or edit.
- [3:24](https://youtu.be/vj55DK8aH3s?t=204) **[[testing-debugging-and-qa]]** Edit a breakpoint to 'log message' with continue execution enabled to print values without pausing the game.
- [4:05](https://youtu.be/vj55DK8aH3s?t=245) **[[testing-debugging-and-qa]]** Add a boolean condition to a breakpoint so it only pauses when a specific state occurs, e.g. table key equals 20.
- [5:26](https://youtu.be/vj55DK8aH3s?t=326) **[[testing-debugging-and-qa]]** Edit or add breakpoints while paused mid-debug; changes take effect as you continue stepping.
- [6:47](https://youtu.be/vj55DK8aH3s?t=407) **[[testing-debugging-and-qa]]** Disabled breakpoints appear hollow; create them up front and enable later from the View > Breakpoints window.
- [8:08](https://youtu.be/vj55DK8aH3s?t=488) **[[testing-debugging-and-qa]]** Use Step Over to skip a function's internals, Step Into to enter it, and Step Out to finish the current scope and return to the caller.
- [10:09](https://youtu.be/vj55DK8aH3s?t=609) **[[testing-debugging-and-qa]]** Use the Watch window to inspect variable values, filter by local/upvalue/global scope, and add expressions like A + B that update as you step.
- [11:50](https://youtu.be/vj55DK8aH3s?t=710) **[[testing-debugging-and-qa]]** Check the Call Stack window to verify function execution order when functions run in an unexpected sequence.
- [13:53](https://youtu.be/vj55DK8aH3s?t=833) **[[testing-debugging-and-qa]]** Watch the Script Analysis window for linter warnings and errors across all scripts, catching type mismatches and syntax errors before playtesting.

## Tools
Roblox Studio debugger, Breakpoints window (View tab), Watch window (View tab), Call Stack window (View tab), Script Analysis window (linter)

## Topics
[[testing-debugging-and-qa]]

Back to [[crusherfiredev - How to make successful Roblox games]]
