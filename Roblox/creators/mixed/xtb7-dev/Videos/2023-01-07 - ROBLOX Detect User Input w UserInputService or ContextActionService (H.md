---
title: "ROBLOX: Detect User Input w/ UserInputService or ContextActionService (How to)"
url: https://youtu.be/DIz1Nk7YOUo
creator: XTB7
official: false
advice_density: medium
date: 2023-01-07
views: 1907
transcript: manual-subs
confidence: high
tags: [roblox, xtb7-dev, youtube-learn]
creator_trust: MIXED
creator_score: 7.3
---

> [!note] Trust: MIXED (credibility audit score 7.3): do not rely on this creator alone; confirm a recommendation with a second source. See [[creator-credibility]].

# ROBLOX: Detect User Input w/ UserInputService or ContextActionService (How to)

[Watch](https://youtu.be/DIz1Nk7YOUo) | xtb7-dev | 1,907 views | 2023-01-07

## Summary
Tutorial on detecting player input in Roblox using UserInputService (InputBegan, key checks) and ContextActionService (BindAction/UnbindAction, action names, input states). Demonstrates binding multiple actions to one function and unbinding after a count. Argues ContextActionService is better for context-specific input because its handler code doesn't run on every input.

## Tips
- [0:28](https://youtu.be/DIz1Nk7YOUo?t=28) **[[scripting-and-performance]]** Put input-handling code in a LocalScript (e.g. StarterPlayerScripts); UserInputService and ContextActionService only work on the client.
- [1:08](https://youtu.be/DIz1Nk7YOUo?t=68) **[[scripting-and-performance]]** Use UserInputService.InputBegan with the gameProcessed boolean to ignore inputs already handled by the game, such as UI clicks.
- [4:20](https://youtu.be/DIz1Nk7YOUo?t=260) **[[scripting-and-performance]]** Name ContextActionService actions descriptively (e.g. 'change part colour'), not after the key used to trigger them.
- [5:01](https://youtu.be/DIz1Nk7YOUo?t=301) **[[ui-ux-design]]** Set the BindAction createTouchButton argument to true when you need a mobile touch button for the action; false otherwise.
- [5:43](https://youtu.be/DIz1Nk7YOUo?t=343) **[[scripting-and-performance]]** BindAction accepts multiple KeyCodes or UserInputTypes, so one action can respond to several inputs.
- [6:25](https://youtu.be/DIz1Nk7YOUo?t=385) **[[scripting-and-performance]]** ContextActionService fires on Begin, Change and End states; check inputState == Enum.UserInputState.Begin to act once per press.
- [7:07](https://youtu.be/DIz1Nk7YOUo?t=427) **[[code-architecture-and-frameworks]]** Bind several actions to the same handler function and branch on actionName with if/elseif to keep one shared handler.
- [9:19](https://youtu.be/DIz1Nk7YOUo?t=559) **[[scripting-and-performance]]** Call ContextActionService:UnbindAction(name) to stop an action once it is no longer needed; unbound actions cost nothing when inputs occur.
- [12:24](https://youtu.be/DIz1Nk7YOUo?t=744) **[[scripting-and-performance]]** Prefer ContextActionService over UserInputService for input only valid in certain states; UserInputService handler runs on every InputBegan, hurting performance as logic grows.

## Numbers
- [5:43](https://youtu.be/DIz1Nk7YOUo?t=343) Action firing count with default binding: **Fired twice per key press (begin and end states) before Begin check** (ContextActionService without inputState filter fires on every input state)
- [8:35](https://youtu.be/DIz1Nk7YOUo?t=515) Example unbind threshold: **10 uses before UnbindAction** (Demo counter in ContextActionService example)

## Tools
UserInputService, ContextActionService, Roblox Creator Documentation

## He points to
- Roblox Creator Documentation

## Topics
[[code-architecture-and-frameworks]] [[scripting-and-performance]] [[ui-ux-design]]

Back to [[xtb7-dev - How to make successful Roblox games]]
