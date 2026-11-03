---
title: "Movement System"
url: https://devforum.roblox.com/t/movement-system/2135683
creator: Roblox DevForum
official: false
advice_density: medium
date: 2023-01-12
views: 174
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Movement System

[Open](https://devforum.roblox.com/t/movement-system/2135683) | Roblox DevForum | 174 views | 2023-01-12

## Summary
Outdated DevForum tutorial building a click-to-move unit system in Roblox: premade unit model, RemoteEvents (CreateBeam, MoveUnit), server movement loop, client selection and beam visuals. Author warns the system is outdated and needs significant knowledge to make efficient.

## Tips
- [page](https://devforum.roblox.com/t/movement-system/2135683) **[[client-server-and-remotes]]** Put RemoteEvents in ReplicatedStorage; handle movement on the server (MoveUnit) and visuals on the client (CreateBeam) via OnClientEvent.
- [page](https://devforum.roblox.com/t/movement-system/2135683) **[[scripting-and-performance]]** Use a while loop checking arrival at destination; after the loop, stop the unit and remove its beam, so cleanup always runs.
- [page](https://devforum.roblox.com/t/movement-system/2135683) **[[client-server-and-remotes]]** Validate parameters server-side (player, hitpos, unit) before moving units, since clients can send arbitrary values.
- [page](https://devforum.roblox.com/t/movement-system/2135683) **[[common-mistakes]]** Author warns this tutorial's approach is outdated and the scripts are not final; polish them before using in a real game.
- [page](https://devforum.roblox.com/t/movement-system/2135683) **[[testing-debugging-and-qa]]** Launch the game with the Output window open and check for errors while testing the script.
- [page](https://devforum.roblox.com/t/movement-system/2135683) **[[development-process-and-speed]]** Organize units in a Workspace folder (Units) and use a child Ignore folder for attachments, keeping workspace structure consistent.

## Tools
Roblox Studio, RemoteEvent, Beam, Attachment, PathfindingService-free while-loop movement

## He points to
- https://www.roblox.com/library/12130875696/Unit

## Quotes
- [page](https://devforum.roblox.com/t/movement-system/2135683) "This system is quite outdated, a lot of knowledge is required in order to make this efficient!"

## Topics
[[client-server-and-remotes]] [[common-mistakes]] [[development-process-and-speed]] [[scripting-and-performance]] [[testing-debugging-and-qa]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
