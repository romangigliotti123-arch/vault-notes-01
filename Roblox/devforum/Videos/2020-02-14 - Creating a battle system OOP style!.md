---
title: "Creating a battle system: OOP style!"
url: https://devforum.roblox.com/t/creating-a-battle-system-oop-style/457584
creator: Roblox DevForum
official: false
advice_density: medium
date: 2020-02-14
views: 163
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Creating a battle system: OOP style!

[Open](https://devforum.roblox.com/t/creating-a-battle-system-oop-style/457584) | Roblox DevForum | 163 views | 2020-02-14

## Summary
Step-by-step OOP tutorial for a Pokemon-style turn-based battle system in Roblox. Covers required instances, DataStore2 player stats, creature/move/NPC data tables, a BattleCreator class using ValueBases, server-side turn handling via RemoteEvents, and client UI tweening.

## Tips
- [page](https://devforum.roblox.com/t/creating-a-battle-system-oop-style/457584) **[[code-architecture-and-frameworks]]** Use a class with .new and : methods (BattleCreator) holding per-battle state, so each battle is a self-contained object you can destroy cleanly.
- [page](https://devforum.roblox.com/t/creating-a-battle-system-oop-style/457584) **[[data-persistence]]** Use DataStore2 for player saves; it provides caching and backups, which the author says prevented problems for him.
- [page](https://devforum.roblox.com/t/creating-a-battle-system-oop-style/457584) **[[client-server-and-remotes]]** Keep battle logic on the server and only fire player choices via a RemoteEvent; validate that the fired player matches and use a debounce to block repeat actions.
- [page](https://devforum.roblox.com/t/creating-a-battle-system-oop-style/457584) **[[client-server-and-remotes]]** Store battle state in ValueBases (IntValue, NumberValue, ObjectValue) inside a Folder so both server and client can read and react via Changed.
- [page](https://devforum.roblox.com/t/creating-a-battle-system-oop-style/457584) **[[client-server-and-remotes]]** Parent the battle area to ReplicatedStorage, then move it to Workspace on the client so other players cannot see it.
- [page](https://devforum.roblox.com/t/creating-a-battle-system-oop-style/457584) **[[scripting-and-performance]]** Clamp health with math.clamp between 0 and MaxHealth so values cannot go negative or exceed max after heal/attack.
- [page](https://devforum.roblox.com/t/creating-a-battle-system-oop-style/457584) **[[scripting-and-performance]]** Disconnect event connections and destroy the battle area when a battle ends to avoid leaked connections.
- [page](https://devforum.roblox.com/t/creating-a-battle-system-oop-style/457584) **[[ui-ux-design]]** Tween UI frames on and off screen using TweenService with predefined On/Off UDim2 positions for battle transitions.
- [page](https://devforum.roblox.com/t/creating-a-battle-system-oop-style/457584) **[[building-art-and-assets]]** Set PrimaryPart on creature and character models and clone them with Archivable enabled, so they can be positioned and copied per battle.
- [page](https://devforum.roblox.com/t/creating-a-battle-system-oop-style/457584) **[[combat-and-gameplay-systems]]** Define creature, move and NPC data in separate ModuleScripts (moves as {amount, type} pairs) so balance changes need no logic edits.
- [page](https://devforum.roblox.com/t/creating-a-battle-system-oop-style/457584) **[[combat-and-gameplay-systems]]** Use a simple NPC AI: heal if the attack would kill the NPC's creature, otherwise attack. Easy to extend later.
- [page](https://devforum.roblox.com/t/creating-a-battle-system-oop-style/457584) **[[matchmaking-and-teleport]]** Use GetPlayerFromCharacter instead of searching Players by name when you have a character and need its Player.

## Numbers
- [page](https://devforum.roblox.com/t/creating-a-battle-system-oop-style/457584) Battle structure: **One move per player turn; two options (Attack, Heal)** (Tutorial's Pokemon-style turn system)
- [page](https://devforum.roblox.com/t/creating-a-battle-system-oop-style/457584) Battle start delay: **2 seconds after CharacterAppearanceLoaded** (Wait before creating battle so player is ready)
- [page](https://devforum.roblox.com/t/creating-a-battle-system-oop-style/457584) Turn pacing delay: **1 second wait before letting player choose again** (Allows tween out to finish)
- [page](https://devforum.roblox.com/t/creating-a-battle-system-oop-style/457584) Example creature health: **Cheese Monster 100 HP, Bean Lord 150 HP** (Sample creature stats in tutorial)
- [page](https://devforum.roblox.com/t/creating-a-battle-system-oop-style/457584) Example move values: **Cheese Attack 20, Eat Cheese 10, Beans 30, Eat Beans 20** (Sample move amounts in tutorial)

## Tools
DataStore2, TweenService, RemoteEvent, RemoteFunction, BindableEvent, BindableFunction

## He points to
- All about Object Oriented Programming (community tutorial)
- BattleSystemTutorial.rbxl place file (uncopylocked resource)

## Topics
[[building-art-and-assets]] [[client-server-and-remotes]] [[code-architecture-and-frameworks]] [[combat-and-gameplay-systems]] [[data-persistence]] [[matchmaking-and-teleport]] [[scripting-and-performance]] [[ui-ux-design]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
