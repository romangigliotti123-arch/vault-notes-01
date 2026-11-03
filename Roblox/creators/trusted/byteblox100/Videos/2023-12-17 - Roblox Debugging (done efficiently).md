---
title: "Roblox Debugging (done efficiently)"
url: https://youtu.be/9YwYDuIuih4
creator: ByteBlox
official: false
advice_density: medium
date: 2023-12-17
views: 13576
transcript: auto-captions
confidence: medium
tags: [roblox, byteblox100, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.1
---

> [!note] Trust: TRUSTED (credibility audit score 8.1): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Roblox Debugging (done efficiently)

[Watch](https://youtu.be/9YwYDuIuih4) | byteblox100 | 13,576 views | 2023-12-17

## Summary
Tutorial on Roblox Studio's breakpoint debugger as a replacement for print-statement debugging. Covers placing breakpoints, step into/over/out, editing breakpoints (condition, log message, continue execution, remove on hit, trigger-at client/server/edit), and log points.

## Tips
- [0:00](https://youtu.be/9YwYDuIuih4?t=0) **[[scripting-and-performance]]** Use breakpoints instead of print statements for debugging; prints only show what you anticipated and require editing code to change what you check.
- [2:30](https://youtu.be/9YwYDuIuih4?t=150) **[[testing-debugging-and-qa]]** Click the gutter next to a line to set a breakpoint; the game enters debug mode and halts there so you can inspect state.
- [4:21](https://youtu.be/9YwYDuIuih4?t=261) **[[testing-debugging-and-qa]]** Step Into runs the next line that does something; Step Over runs a function without entering it; Step Out runs to the end of the current function.
- [9:18](https://youtu.be/9YwYDuIuih4?t=558) **[[testing-debugging-and-qa]]** Add a condition to a breakpoint (e.g. testVar == 100) so it only halts when that condition is true, avoiding manual stopping in long runs.
- [10:33](https://youtu.be/9YwYDuIuih4?t=633) **[[testing-debugging-and-qa]]** Use a log message on a breakpoint (a log point) to print variable values without halting; enable Continue Execution to keep the script running.
- [14:10](https://youtu.be/9YwYDuIuih4?t=850) **[[testing-debugging-and-qa]]** Enable Remove Breakpoint on Hit when debugging loops so the breakpoint deletes itself after the first hit.
- [14:58](https://youtu.be/9YwYDuIuih4?t=898) **[[testing-debugging-and-qa]]** Set Trigger At to client, server, or edit so breakpoints in shared ModuleScripts only fire in the context you're debugging.
- [0:41](https://youtu.be/9YwYDuIuih4?t=41) **[[development-process-and-speed]]** Learn debugging early: the speaker argues being able to fix errors is what keeps beginners motivated to keep learning.

## Tools
Roblox Studio debugger (breakpoints, step into/over/out, log points)

## Topics
[[development-process-and-speed]] [[scripting-and-performance]] [[testing-debugging-and-qa]]

Back to [[byteblox100 - How to make successful Roblox games]]
