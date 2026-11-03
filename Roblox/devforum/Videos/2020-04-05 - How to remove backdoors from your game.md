---
title: "How to remove backdoors from your game"
url: https://devforum.roblox.com/t/how-to-remove-backdoors-from-your-game/511548
creator: Roblox DevForum
official: false
advice_density: high
date: 2020-04-05
views: 225
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# How to remove backdoors from your game

[Open](https://devforum.roblox.com/t/how-to-remove-backdoors-from-your-game/511548) | Roblox DevForum | 225 views | 2020-04-05

## Summary
Devforum guide on detecting and removing backdoors in Roblox games. Covers fake/botted plugins, free-model placeholders, and a list of suspicious script strings to search with Ctrl+Shift+F. Explains backdoors give exploiters server-side access, distinct from server-access remotes.

## Tips
- [page](https://devforum.roblox.com/t/how-to-remove-backdoors-from-your-game/511548) **[[anti-exploit-and-security]]** Check plugins before installing: fake or botted plugins are a common backdoor source. Look at creator username, join date, and creation date, not just sales counts.
- [page](https://devforum.roblox.com/t/how-to-remove-backdoors-from-your-game/511548) **[[anti-exploit-and-security]]** Treat free models as placeholders only. Check the creator (bot-like name or new account), and after inserting, delete any scripts inside the model (tools excepted). Replace with your own assets.
- [page](https://devforum.roblox.com/t/how-to-remove-backdoors-from-your-game/511548) **[[anti-exploit-and-security]]** Use Ctrl+Shift+F in Studio to search for backdoor strings: math., require, luraph, synapse, string., I, loadstring, getfenv, setfenv, IsStudio. Follow any found ModuleScript ID to its source.
- [page](https://devforum.roblox.com/t/how-to-remove-backdoors-from-your-game/511548) **[[anti-exploit-and-security]]** Look for a ':run'-style function call after a suspicious module, which typically activates the backdoor.
- [page](https://devforum.roblox.com/t/how-to-remove-backdoors-from-your-game/511548) **[[anti-exploit-and-security]]** Distinguish backdoors from server-side access remotes: both grant server-level effects but stem from different properties, so audit remotes separately.

## Tools
Roblox Studio Ctrl+Shift+F script search

## He points to
- Sudden_Demise DevForum post

## Topics
[[anti-exploit-and-security]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
