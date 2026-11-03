---
title: "Docs: education / battle-royale-series / creating-a-gui"
url: https://create.roblox.com/docs/education/battle-royale-series/creating-a-gui.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: education / battle-royale-series / creating-a-gui

[Open](https://create.roblox.com/docs/education/battle-royale-series/creating-a-gui.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox Education Battle Royale lesson: builds a ScreenGUI status label driven by a StringValue in ReplicatedStorage, updated via a DisplayManager module on the server, and shows player count and timer during matches using IntValues.

## Tips
- [page](https://create.roblox.com/docs/education/battle-royale-series/creating-a-gui) **[[client-server-and-remotes]]** Put GUI ScreenGUIs in StarterGUI so all players get a copy at startup; the GUI stays fixed on screen while the camera moves.
- [page](https://create.roblox.com/docs/education/battle-royale-series/creating-a-gui) **[[client-server-and-remotes]]** Local scripts only run on the player's device and can't read ServerStorage; put values the client needs in ReplicatedStorage.
- [page](https://create.roblox.com/docs/education/battle-royale-series/creating-a-gui) **[[client-server-and-remotes]]** Use a server-side module (DisplayManager) as a single entry point so other server scripts can update shared GUI values.
- [page](https://create.roblox.com/docs/education/battle-royale-series/creating-a-gui) **[[scripting-and-performance]]** Drive GUI text with .Changed connections on value objects instead of polling, and call the update function once at the end of the script so late joiners see current state.
- [page](https://create.roblox.com/docs/education/battle-royale-series/creating-a-gui) **[[scripting-and-performance]]** Use task.wait() with no argument in a timer loop for more accurate per-frame updates than a fixed wait.
- [page](https://create.roblox.com/docs/education/battle-royale-series/creating-a-gui) **[[ui-ux-design]]** Test the GUI both with and without the minimum player count to confirm each status message displays correctly.
- [page](https://create.roblox.com/docs/education/battle-royale-series/creating-a-gui) **[[testing-debugging-and-qa]]** If the label shows the default 'Label' text or no message, check the local script calls the update function at the bottom and that the StringValue is in ReplicatedStorage, not ServerStorage.

## Tools
Roblox Studio, Explorer, ScreenGui, TextLabel, LocalScript, ModuleScript, StringValue, IntValue

## Topics
[[client-server-and-remotes]] [[scripting-and-performance]] [[testing-debugging-and-qa]] [[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
