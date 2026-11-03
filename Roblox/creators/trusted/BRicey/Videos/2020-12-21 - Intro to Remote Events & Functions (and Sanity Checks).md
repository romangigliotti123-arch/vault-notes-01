---
title: "Intro to Remote Events & Functions (and Sanity Checks)"
url: https://youtu.be/Zh-Jd4xEc2g
creator: B Ricey
official: false
advice_density: medium
date: 2020-12-21
views: 17341
transcript: auto-captions
confidence: high
tags: [roblox, bricey, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.0
---

> [!note] Trust: TRUSTED (credibility audit score 8.0): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Intro to Remote Events & Functions (and Sanity Checks)

[Watch](https://youtu.be/Zh-Jd4xEc2g) | BRicey | 17,341 views | 2020-12-21

## Summary
Beginner tutorial on RemoteEvents and RemoteFunctions for server-client communication in Roblox. Covers where to place them (ReplicatedStorage), FireServer/OnServerEvent (player is always the first argument), FireClient, InvokeServer/OnServerInvoke for returning values, and server-side sanity checks against exploiters.

## Tips
- [4:00](https://youtu.be/Zh-Jd4xEc2g?t=240) **[[client-server-and-remotes]]** Put RemoteEvents and RemoteFunctions in ReplicatedStorage; it is the best spot since both client and server can see it.
- [5:22](https://youtu.be/Zh-Jd4xEc2g?t=322) **[[client-server-and-remotes]]** OnServerEvent callbacks always receive the player as the first parameter, before any sent arguments; forgetting this shifts all values.
- [8:05](https://youtu.be/Zh-Jd4xEc2g?t=485) **[[client-server-and-remotes]]** Use RemoteEvents for one-way signals and RemoteFunctions when the client needs a returned value; RemoteFunction.OnServerInvoke should return a value.
- [10:47](https://youtu.be/Zh-Jd4xEc2g?t=647) **[[client-server-and-remotes]]** Return a success boolean from a RemoteFunction so the client immediately knows whether a transaction, such as a purchase, succeeded.
- [11:20](https://youtu.be/Zh-Jd4xEc2g?t=680) **[[anti-exploit-and-security]]** Run sanity checks on the server, e.g. verify money >= cost before subtracting, so values never go negative or get exploited.
- [14:06](https://youtu.be/Zh-Jd4xEc2g?t=846) **[[anti-exploit-and-security]]** Never trust the client. Exploiters can fire any unprotected RemoteEvent with arbitrary values, such as adding millions of currency.
- [14:48](https://youtu.be/Zh-Jd4xEc2g?t=888) **[[anti-exploit-and-security]]** Write defensive code that catches invalid input before it takes effect; use warn statements for debugging failed checks.
- [0:36](https://youtu.be/Zh-Jd4xEc2g?t=36) **[[client-server-and-remotes]]** Since FilteringEnabled, clients cannot change what the server sees, so all client-to-server state changes must go through remotes.

## Tools
Roblox Studio

## Topics
[[anti-exploit-and-security]] [[client-server-and-remotes]]

Back to [[BRicey - How to make successful Roblox games]]
