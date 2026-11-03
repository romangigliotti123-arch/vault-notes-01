---
title: "How to script with REMOTE EVENTS in ROBLOX STUDIO!"
url: https://youtu.be/0oL3YX4sCb8
creator: PineappleDev
official: false
advice_density: low
date: 2024-02-06
views: 865
transcript: auto-captions
confidence: high
tags: [roblox, pineappledevv, youtube-learn]
creator_trust: TRUSTED
creator_score: 7.7
---

> [!note] Trust: TRUSTED (credibility audit score 7.7): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# How to script with REMOTE EVENTS in ROBLOX STUDIO!

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Watch](https://youtu.be/0oL3YX4sCb8) | pineappledevv | 865 views | 2024-02-06

## Summary
Beginner tutorial on Roblox RemoteEvents: firing from a LocalScript to the server (FireServer, OnServerEvent) and from the server to all clients (FireAllClients, OnClientEvent). Uses a keypress as the trigger and a string payload. Explains that the server's first argument is always the player.

## Tips
- [0:20](https://youtu.be/0oL3YX4sCb8?t=20) **[[client-server-and-remotes]]** Place RemoteEvents in ReplicatedStorage so both client and server scripts can reference them.
- [1:44](https://youtu.be/0oL3YX4sCb8?t=104) **[[client-server-and-remotes]]** FireServer accepts up to about 16 arguments, including strings, booleans, numbers and tables.
- [2:31](https://youtu.be/0oL3YX4sCb8?t=151) **[[client-server-and-remotes]]** On the server, OnServerEvent always passes the firing player as the first argument, before any custom arguments.
- [4:28](https://youtu.be/0oL3YX4sCb8?t=268) **[[client-server-and-remotes]]** Use FireClient to target one player and FireAllClients to broadcast to everyone; OnClientEvent receives only the server's arguments, not a player.

## Numbers
- [1:44](https://youtu.be/0oL3YX4sCb8?t=104) max FireServer arguments: **16** (Stated as roughly up to 16 variables passed in one call)

## Tools
Roblox Studio, RemoteEvent, LocalScript, Server Script

## Topics
[[client-server-and-remotes]]

Back to [[pineappledevv - How to make successful Roblox games]]
