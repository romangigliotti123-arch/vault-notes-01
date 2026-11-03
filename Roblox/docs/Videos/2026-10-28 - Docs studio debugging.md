---
title: "Docs: studio / debugging"
url: https://create.roblox.com/docs/studio/debugging.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: studio / debugging

[Open](https://create.roblox.com/docs/studio/debugging.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox Studio docs on debugging: breakpoint types (standard, conditional, logpoint, temporary), enabling/disabling/editing, stepping workflow, and monitoring windows (Breakpoints, Call Stack, Watch), plus Command Bar, Developer Console (F9), and platform log file locations.

## Tips
- [page](https://create.roblox.com/docs/studio/debugging) **[[testing-debugging-and-qa]]** Use breakpoints as the primary tool for debugging functions; they let you pause and inspect variables, watch values and view the call stack.
- [page](https://create.roblox.com/docs/studio/debugging) **[[testing-debugging-and-qa]]** Use conditional breakpoints (e.g. var == 10) to pause only when a specific variable value occurs, especially inside loops.
- [page](https://create.roblox.com/docs/studio/debugging) **[[testing-debugging-and-qa]]** Use logpoints to print variable values to the Output window without pausing the script.
- [page](https://create.roblox.com/docs/studio/debugging) **[[testing-debugging-and-qa]]** Use temporary breakpoints for quick checks; they remove themselves after the first playtest session.
- [page](https://create.roblox.com/docs/studio/debugging) **[[testing-debugging-and-qa]]** Disable breakpoints instead of deleting them to keep their conditions and log messages; deleting removes them permanently.
- [page](https://create.roblox.com/docs/studio/debugging) **[[testing-debugging-and-qa]]** Use Step Into (F11), Step Over (F10) and Step Out (Shift+F11) to move through code line by line while paused.
- [page](https://create.roblox.com/docs/studio/debugging) **[[testing-debugging-and-qa]]** Use the Watch window's My Watches tab to track arbitrary expressions instead of adding print statements.
- [page](https://create.roblox.com/docs/studio/debugging) **[[testing-debugging-and-qa]]** Press F9 or type /console in chat during a test to open the Developer Console for client/server output, memory and network stats.
- [page](https://create.roblox.com/docs/studio/debugging) **[[testing-debugging-and-qa]]** Use the Command Bar to run Luau commands while the game is running for quick inspection.
- [page](https://create.roblox.com/docs/studio/debugging) **[[testing-debugging-and-qa]]** Check platform log files (%LOCALAPPDATA%\Roblox\logs on Windows, ~/Library/Logs/Roblox on Mac) to see script prints and errors; same XXXXX value means same Studio session.

## Numbers
- [page](https://create.roblox.com/docs/studio/debugging) Conditional breakpoint example: **var == 10** (Example condition; breakpoint activates only when true)
- [page](https://create.roblox.com/docs/studio/debugging) Step Into shortcut: **F11** (Moves into function on current line)
- [page](https://create.roblox.com/docs/studio/debugging) Step Over shortcut: **F10** (Moves to next line without entering functions)
- [page](https://create.roblox.com/docs/studio/debugging) Step Out shortcut: **Shift+F11** (Exits current function to next line after call)
- [page](https://create.roblox.com/docs/studio/debugging) Developer Console shortcut: **F9 or /console** (Opens console during playtest)

## Tools
Roblox Studio Script Editor debugger, Breakpoints window, Call Stack window, Watch window, Command Bar, Developer Console

## He points to
- Roblox Studio debugging docs

## Topics
[[testing-debugging-and-qa]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
