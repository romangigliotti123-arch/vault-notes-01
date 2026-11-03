---
title: "Docs: studio / cli"
url: https://create.roblox.com/docs/studio/cli.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: studio / cli

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/studio/cli.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Official Roblox docs for Studio command-line arguments: opening places by ID or version, opening local .rbxl/.rbxlx files, opening scripts at specific lines, running Luau scripts headlessly with output and auto-quit, inserting assets into a baseplate, and dumping the API surface to JSON.

## Tips
- [page](https://create.roblox.com/docs/studio/cli) **[[testing-debugging-and-qa]]** Use --task RunScript with --quitAfterExecution and --outputFile to run smoke tests in CI and capture results to a log file.
- [page](https://create.roblox.com/docs/studio/cli) **[[version-control-and-tooling]]** Studio pipes verbose logs to stdout when launched from the command line, which is more detailed than the Output window; capture it when debugging.
- [page](https://create.roblox.com/docs/studio/cli) **[[version-control-and-tooling]]** Quote file paths containing spaces; arguments are case-insensitive and use a double-dash prefix.
- [page](https://create.roblox.com/docs/studio/cli) **[[testing-debugging-and-qa]]** Use --task EditPlaceRevision with --placeVersion to reopen a previous published version when diagnosing a regression.

## Tools
RobloxStudio.exe / RobloxStudio (command-line arguments)

## Topics
[[development-process-and-speed]] [[scripting-and-performance]] [[testing-debugging-and-qa]] [[version-control-and-tooling]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
