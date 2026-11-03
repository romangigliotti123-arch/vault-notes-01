---
title: BloxianCode - Studio & Scripting
creator: BloxianCode
tags: [roblox, bloxiancode, theme]
creator_trust: TRUSTED
creator_score: 7.7
---

> [!note] Trust: TRUSTED (credibility audit score 7.7): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# BloxianCode: Studio & Scripting

All BloxianCode tips on this theme, grouped by topic, oldest first. Cross-creator synthesis: see [[README]] in roblox-kb.

## [[client-server-and-remotes]]
- 2022-02-26 [2:11](https://youtu.be/SN7MyJFOQkU?t=131) Secure RemoteEvents on both client and server; RemoteEvents are the main way exploiters reach server code, so validate every incoming argument on the server. ([[2022-02-26 - HOW TO SECURE YOUR ROBLOX GAME!!|HOW TO SECURE YOUR ROBLOX GAME!!]])

## [[anti-exploit-and-security]]
- 2022-02-26 [0:40](https://youtu.be/SN7MyJFOQkU?t=40) Assume every game can be hacked; aim to make exploiting hard enough to deter most people rather than promising perfect security. ([[2022-02-26 - HOW TO SECURE YOUR ROBLOX GAME!!|HOW TO SECURE YOUR ROBLOX GAME!!]])
- 2022-02-26 [0:47](https://youtu.be/SN7MyJFOQkU?t=47) Treat the client as untrusted: local scripts can be modified or bypassed, so never rely on client-side checks alone for gameplay-critical logic. ([[2022-02-26 - HOW TO SECURE YOUR ROBLOX GAME!!|HOW TO SECURE YOUR ROBLOX GAME!!]])
- 2022-02-26 [2:45](https://youtu.be/SN7MyJFOQkU?t=165) Double-check critical actions like killing a player on both client and server, but make the server the authoritative check. ([[2022-02-26 - HOW TO SECURE YOUR ROBLOX GAME!!|HOW TO SECURE YOUR ROBLOX GAME!!]])
- 2022-02-26 [3:27](https://youtu.be/SN7MyJFOQkU?t=207) Choose a response policy: passive (silently undo the exploit's effect) or aggressive (kick or ban the exploiter); the speaker notes aggressive use needs a reliable way to undo bans. ([[2022-02-26 - HOW TO SECURE YOUR ROBLOX GAME!!|HOW TO SECURE YOUR ROBLOX GAME!!]])

## [[data-persistence]]
- 2021-03-09 [0:28](https://youtu.be/aBFH7KGIpnc?t=28) Never change the DataStore name after release; changing it makes all existing player data unreachable and lost. ([[2021-03-09 - HOW To Make a DATASTORE!!! Roblox Studio Tutorial|HOW To Make a DATASTORE!!! Roblox Studio Tutorial]])
- 2021-03-09 [2:06](https://youtu.be/aBFH7KGIpnc?t=126) Wrap DataStore GetAsync calls in pcall so a failed request does not halt the script. ([[2021-03-09 - HOW To Make a DATASTORE!!! Roblox Studio Tutorial|HOW To Make a DATASTORE!!! Roblox Studio Tutorial]])
- 2021-03-09 [1:52](https://youtu.be/aBFH7KGIpnc?t=112) Load player data inside a PlayerAdded handler so saved values can be applied when the player joins. ([[2021-03-09 - HOW To Make a DATASTORE!!! Roblox Studio Tutorial|HOW To Make a DATASTORE!!! Roblox Studio Tutorial]])
- 2021-12-01 [0:00](https://youtu.be/Z1OjuaBCAXU?t=0) Enable Game Settings > Security > 'Enable Studio Access to API Services' before using DataStores in Studio, then save. ([[2021-12-01 - Datastore Editor Explained!!|Datastore Editor Explained!!]])
- 2021-12-01 [0:00](https://youtu.be/Z1OjuaBCAXU?t=0) Publish the game or set it to Roblox so DataStore access works as expected during testing. ([[2021-12-01 - Datastore Editor Explained!!|Datastore Editor Explained!!]])
- 2021-12-01 [2:42](https://youtu.be/Z1OjuaBCAXU?t=162) Use player UserId as the DataStore key so each player's data is unique. ([[2021-12-01 - Datastore Editor Explained!!|Datastore Editor Explained!!]])
- 2021-12-01 [6:10](https://youtu.be/Z1OjuaBCAXU?t=370) Always click the save icon in DataStore Editor after editing; otherwise changes are not written and errors can occur. ([[2021-12-01 - Datastore Editor Explained!!|Datastore Editor Explained!!]])
- 2021-12-01 [8:13](https://youtu.be/Z1OjuaBCAXU?t=493) Deleting a key in DataStore Editor cannot be undone; confirm carefully before deleting. ([[2021-12-01 - Datastore Editor Explained!!|Datastore Editor Explained!!]])
- 2021-12-01 [11:38](https://youtu.be/Z1OjuaBCAXU?t=698) OrderedDataStores store ranked lists (e.g. leaderboards); the editor can sort them ascending or descending. ([[2021-12-01 - Datastore Editor Explained!!|Datastore Editor Explained!!]])

## [[version-control-and-tooling]]
- 2024-04-20 [0:24](https://youtu.be/TmSZl5CcIKE?t=24) Use GitHub Desktop to set up a repo for your Studio project so every change is tracked and can be rolled back. ([[2024-04-20 - BEGINNER HOW TO CONNECT ROBLOX STUDIO to GITHUB!!|[BEGINNER] HOW TO CONNECT ROBLOX STUDIO to GITHUB!]])
- 2024-04-20 [2:47](https://youtu.be/TmSZl5CcIKE?t=167) Open the synced project folder in VS Code alongside Roblox Studio to edit scripts while keeping the project under Git. ([[2024-04-20 - BEGINNER HOW TO CONNECT ROBLOX STUDIO to GITHUB!!|[BEGINNER] HOW TO CONNECT ROBLOX STUDIO to GITHUB!]])
- 2024-04-20 [3:53](https://youtu.be/TmSZl5CcIKE?t=233) Commit and push changes via GitHub Desktop to save a snapshot of your game to GitHub. ([[2024-04-20 - BEGINNER HOW TO CONNECT ROBLOX STUDIO to GITHUB!!|[BEGINNER] HOW TO CONNECT ROBLOX STUDIO to GITHUB!]])
- 2024-04-20 [5:54](https://youtu.be/TmSZl5CcIKE?t=354) Check file history on GitHub to review past changes and recover earlier versions of files. ([[2024-04-20 - BEGINNER HOW TO CONNECT ROBLOX STUDIO to GITHUB!!|[BEGINNER] HOW TO CONNECT ROBLOX STUDIO to GITHUB!]])

Up: [[BloxianCode - How to make successful Roblox games]]
