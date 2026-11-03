---
title: "Docs: tutorials / fundamentals / coding-2 / parameters-practice-buttons"
url: https://create.roblox.com/docs/tutorials/fundamentals/coding-2/parameters-practice-buttons.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: tutorials / fundamentals / coding-2 / parameters-practice-buttons

[Open](https://create.roblox.com/docs/tutorials/fundamentals/coding-2/parameters-practice-buttons.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox official docs tutorial: building a button-activated bridge. Covers making a semi-transparent, non-collidable anchored bridge, a floating anchored red button, and a Touched-event script that turns the button green, makes the bridge visible and collidable. Includes troubleshooting and an optional door/gate challenge.

## Tips
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-2/parameters-practice-buttons) **[[core-loops-and-game-design]]** Give players feedback when they touch a button (color change, sound) so they know it is being interacted with.
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-2/parameters-practice-buttons) **[[building-and-level-design]]** Anchor button and bridge parts and keep the button floating, not touching anything, so Touched doesn't fire accidentally.
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-2/parameters-practice-buttons) **[[scripting-and-performance]]** Connect the function with button.Touched:Connect(buttonPressed) outside the function body, not inside it.
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-2/parameters-practice-buttons) **[[scripting-and-performance]]** Use script.Parent to reference the button and workspace.<Name> with the exact Explorer name to avoid 'not a valid member of Workspace' errors.
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-2/parameters-practice-buttons) **[[common-mistakes]]** If a bridge is solid at game start, check that its parts are anchored and not touching terrain or other parts, which can fire Touched early.
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-2/parameters-practice-buttons) **[[building-and-level-design]]** Set bridge Transparency to 0.5 and CanCollide to false initially to show it is inactive; Transparency 0 is fully visible, 1 is invisible.

## Numbers
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-2/parameters-practice-buttons) Transparency: **0.5 (inactive bridge), 0 (active, visible), 1 (invisible)** (Bridge transparency states in the tutorial)
- [page](https://create.roblox.com/docs/tutorials/fundamentals/coding-2/parameters-practice-buttons) Button green color RGB: **Color3.fromRGB(0, 170, 0)** (Pressed-state button color in the sample script)

## Tools
Roblox Studio, Properties window, Explorer, Output window, Luau script

## He points to
- Class.BasePart.Touched event

## Topics
[[building-and-level-design]] [[common-mistakes]] [[core-loops-and-game-design]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
