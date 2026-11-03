---
title: "Advanced Server-Client Communication"
url: https://youtu.be/Q-xgfPRACcw
creator: ByteBlox
official: false
advice_density: low
date: 2023-10-22
views: 23491
transcript: auto-captions
confidence: high
tags: [roblox, byteblox100, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.1
---

> [!note] Trust: TRUSTED (credibility audit score 8.1): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Advanced Server-Client Communication

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Watch](https://youtu.be/Q-xgfPRACcw) | byteblox100 | 23,491 views | 2023-10-22

## Summary
Beginner tutorial on RemoteFunctions in Roblox: invoking from a LocalScript to the server, handling with OnServerInvoke, passing arguments, returning values, and the fact that invoking yields until a return. Ends with a solo challenge summing three numbers.

## Tips
- [1:05](https://youtu.be/Q-xgfPRACcw?t=65) **[[client-server-and-remotes]]** Use RemoteFunction:InvokeServer from client and catch with OnServerInvoke; the server handler receives the player as the first argument automatically.
- [3:57](https://youtu.be/Q-xgfPRACcw?t=237) **[[client-server-and-remotes]]** Pass values as extra arguments after the invoke call; the server function's parameters after player receive them in order.
- [4:38](https://youtu.be/Q-xgfPRACcw?t=278) **[[client-server-and-remotes]]** RemoteFunctions can return only one value; combine multiple results into one return value (e.g. a table) if needed.
- [6:47](https://youtu.be/Q-xgfPRACcw?t=407) **[[client-server-and-remotes]]** InvokeServer yields the calling script until the server returns, so avoid long waits inside handlers or wrap calls in task.spawn to prevent blocking.

## Tools
Roblox Studio, Luau

## Topics
[[client-server-and-remotes]]

Back to [[byteblox100 - How to make successful Roblox games]]
