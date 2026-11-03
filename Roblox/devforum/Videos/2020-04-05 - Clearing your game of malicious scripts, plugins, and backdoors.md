---
title: "Clearing your game of malicious scripts, plugins, and backdoors"
url: https://devforum.roblox.com/t/clearing-your-game-of-malicious-scripts-plugins-and-backdoors/511830
creator: Roblox DevForum
official: false
advice_density: high
date: 2020-04-05
views: 118
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Clearing your game of malicious scripts, plugins, and backdoors

[Open](https://devforum.roblox.com/t/clearing-your-game-of-malicious-scripts-plugins-and-backdoors/511830) | Roblox DevForum | 118 views | 2020-04-05

## Summary
Guide for cleaning a Roblox game infected with malicious scripts, plugins, or backdoors: audit plugins, scan for rogue scripts (print LuaSourceContainer descendants, anti-virus plugins, Find in All Scripts, hidden classes like CSGDictionaryService), and prevent reinfection. Covers July 2020 security settings and plugin HTTP permissions.

## Tips
- [page](https://devforum.roblox.com/t/clearing-your-game-of-malicious-scripts-plugins-and-backdoors/511830) **[[ugc-and-avatar-economy]]** Disable third-party sales and cross-game teleports in Game Settings > Security if you don't need them, but still clean the infection fully.
- [page](https://devforum.roblox.com/t/clearing-your-game-of-malicious-scripts-plugins-and-backdoors/511830) **[[anti-exploit-and-security]]** Remove any plugin you don't recognize, and check that creator names match exactly since display names can be impersonated.
- [page](https://devforum.roblox.com/t/clearing-your-game-of-malicious-scripts-plugins-and-backdoors/511830) **[[anti-exploit-and-security]]** Verify plugin source code before installing unless the plugin was purchased with Robux; many free plugins can inject malicious code.
- [page](https://devforum.roblox.com/t/clearing-your-game-of-malicious-scripts-plugins-and-backdoors/511830) **[[anti-exploit-and-security]]** Scan for rogue scripts by printing GetFullName() of all LuaSourceContainer descendants across every service you can, including CSGDictionaryService.
- [page](https://devforum.roblox.com/t/clearing-your-game-of-malicious-scripts-plugins-and-backdoors/511830) **[[anti-exploit-and-security]]** Enable 'Show Hidden Objects in Explorer' in Studio settings to find scripts hidden in services like CSGDictionaryService; anything besides MeshData there is suspicious.
- [page](https://devforum.roblox.com/t/clearing-your-game-of-malicious-scripts-plugins-and-backdoors/511830) **[[anti-exploit-and-security]]** Search all scripts (Ctrl/Cmd+Shift+F) for MarketplaceService, string.reverse, string.byte, require, and getfenv to locate backdoor code.
- [page](https://devforum.roblox.com/t/clearing-your-game-of-malicious-scripts-plugins-and-backdoors/511830) **[[anti-exploit-and-security]]** Limit free models and check inserted models for scripts before keeping them.
- [page](https://devforum.roblox.com/t/clearing-your-game-of-malicious-scripts-plugins-and-backdoors/511830) **[[common-mistakes]]** Don't just disable the Security toggles and stop; you must still remove the malicious content from the game.
- [page](https://devforum.roblox.com/t/clearing-your-game-of-malicious-scripts-plugins-and-backdoors/511830) **[[team-and-budget]]** In Team Create, make every collaborator follow the same plugin and script hygiene rules, since one person's bad plugin affects everyone.
- [page](https://devforum.roblox.com/t/clearing-your-game-of-malicious-scripts-plugins-and-backdoors/511830) **[[anti-exploit-and-security]]** Only use scripts from trusted sources; the DevForum is safer because public posts are visible to everyone and bad actors get caught quickly.

## Tools
Roblox Studio Manage Plugins window, DataModel:GetObjects() in command bar, Venom, GameTree, Kronos, Hidden Backdoor/Infection Script Detector

## He points to
- How to inspect the source of plugins (Community Tutorials, DevForum)

## Topics
[[anti-exploit-and-security]] [[common-mistakes]] [[team-and-budget]] [[ugc-and-avatar-economy]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
