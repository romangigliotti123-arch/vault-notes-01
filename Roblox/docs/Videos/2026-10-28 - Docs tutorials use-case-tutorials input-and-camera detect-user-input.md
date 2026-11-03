---
title: "Docs: tutorials / use-case-tutorials / input-and-camera / detect-user-input"
url: https://create.roblox.com/docs/tutorials/use-case-tutorials/input-and-camera/detect-user-input.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: tutorials / use-case-tutorials / input-and-camera / detect-user-input

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/tutorials/use-case-tutorials/input-and-camera/detect-user-input.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs tutorial showing how to bind a reload action to the R key using ContextActionService in a Blaster tool. Covers BindAction on Equipped, UnbindAction on Unequipped, and filtering on Enum.UserInputState.Begin. Purely technical; no monetisation or growth advice.

## Tips
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/input-and-camera/detect-user-input) **[[client-server-and-remotes]]** Check inputState == Enum.UserInputState.Begin in input handlers; the callback fires on every state change, so without the check a single press triggers multiple times.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/input-and-camera/detect-user-input) **[[combat-and-gameplay-systems]]** Bind tool input actions on Equipped and UnbindAction on Unequipped so keys only work while the tool is held.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/input-and-camera/detect-user-input) **[[ui-ux-design]]** Pass true as the third BindAction argument to auto-create a touchscreen button for mobile players.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/input-and-camera/detect-user-input) **[[cross-platform-and-console]]** Use ContextActionService with KeyCodes rather than raw input checks; the same binding can cover keyboard and controller buttons.

## Numbers
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/input-and-camera/detect-user-input) reload visual duration: **2 seconds (task.wait(2))** (Example reload feedback: texture swap for 2 seconds in tutorial)

## Tools
ContextActionService, Toolbox Inventory, Roblox Studio LocalScript

## Topics
[[client-server-and-remotes]] [[combat-and-gameplay-systems]] [[cross-platform-and-console]] [[scripting-and-performance]] [[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
