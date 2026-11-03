---
title: "Roblox Script Organization Explained"
url: https://youtu.be/28z_064N-lc
creator: Crusherfire
official: false
advice_density: medium
date: 2024-02-11
views: 80328
transcript: auto-captions
confidence: high
tags: [roblox, crusherfiredev, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.7
---

> [!note] Trust: TRUSTED (credibility audit score 8.7): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Roblox Script Organization Explained

[Watch](https://youtu.be/28z_064N-lc) | crusherfiredev | 80,328 views | 2024-02-11

## Summary
Explains how to organize scripts and instances in a Roblox project: which services hold server scripts, local scripts, and shared modules, naming scripts by single purpose, folder structuring, and a modular require-based architecture example.

## Tips
- [0:33](https://youtu.be/28z_064N-lc?t=33) **[[code-architecture-and-frameworks]]** Store server scripts in ServerScriptService; share modules between server scripts via ServerScriptService or ServerStorage. Don't put server scripts in StarterPlayerScripts.
- [1:14](https://youtu.be/28z_064N-lc?t=74) **[[code-architecture-and-frameworks]]** Use folders inside ServerScriptService and ReplicatedStorage to categorize scripts; folders keep large projects navigable.
- [1:56](https://youtu.be/28z_064N-lc?t=116) **[[code-architecture-and-frameworks]]** Put character-only local scripts (health regen, stamina) in StarterCharacterScripts; they re-clone on every respawn.
- [2:36](https://youtu.be/28z_064N-lc?t=156) **[[code-architecture-and-frameworks]]** Put modules shared between client and server in ReplicatedStorage; use ServerStorage for objects only the server should access.
- [3:51](https://youtu.be/28z_064N-lc?t=231) **[[code-architecture-and-frameworks]]** Give each script exactly one purpose and name it after that purpose (e.g. LeaderboardHandler). Split scripts that do multiple unrelated jobs.
- [5:06](https://youtu.be/28z_064N-lc?t=306) **[[code-architecture-and-frameworks]]** Use ReplicatedFirst only for assets needed immediately, such as a loading screen; otherwise use ReplicatedStorage since it's rarely needed.
- [8:39](https://youtu.be/28z_064N-lc?t=519) **[[code-architecture-and-frameworks]]** Consider a modular approach: one server bootstrap script and one client bootstrap script that require all module handlers/services, rather than many independent scripts.
- [10:01](https://youtu.be/28z_064N-lc?t=601) **[[code-architecture-and-frameworks]]** Add subfolders to categorize services once a project grows; a single flat folder becomes cluttered quickly.
- [11:24](https://youtu.be/28z_064N-lc?t=684) **[[code-architecture-and-frameworks]]** Use CollectionService tags to find all instances of a type (e.g. hot tubs) and wire each one up with a class module.
- [11:24](https://youtu.be/28z_064N-lc?t=684) **[[code-architecture-and-frameworks]]** Keep a shared Utilities module folder (signals, Trove, camera shaker) and a folder of custom enums for client-server communication.
- [12:40](https://youtu.be/28z_064N-lc?t=760) **[[common-mistakes]]** Don't store local scripts in ServerScriptService or server scripts in StarterPlayerScripts; these are misuses of the services.

## Tools
Trove (module by Suphi Kaner / 'snik'), CollectionService

## He points to
- Trove module by snik

## Topics
[[code-architecture-and-frameworks]] [[common-mistakes]]

Back to [[crusherfiredev - How to make successful Roblox games]]
