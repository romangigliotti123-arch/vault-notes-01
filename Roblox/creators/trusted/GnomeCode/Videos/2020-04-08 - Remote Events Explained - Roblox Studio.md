---
title: "Remote Events Explained - Roblox Studio"
url: https://youtu.be/3wkPekjQvKg
creator: GnomeCode
official: false
advice_density: medium
date: 2020-04-08
views: 63278
transcript: auto-captions
confidence: high
tags: [roblox, gnomecode, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.1
---

> [!note] Trust: TRUSTED (credibility audit score 8.1): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Remote Events Explained - Roblox Studio

[Watch](https://youtu.be/3wkPekjQvKg) | GnomeCode | 63,278 views | 2020-04-08

## Summary
Tutorial on Roblox RemoteEvents explaining filtering enabled and the three communication directions: client-to-server, server-to-client (one player), and server-to-all-clients, with code walkthroughs in Roblox Studio.

## Tips
- [0:00](https://youtu.be/3wkPekjQvKg?t=0) **[[client-server-and-remotes]]** Never rely on client-made changes to replicate; with FilteringEnabled the server rejects them. Send a RemoteEvent to the server and make the change there.
- [4:05](https://youtu.be/3wkPekjQvKg?t=245) **[[client-server-and-remotes]]** Create RemoteEvents in ReplicatedStorage so both client and server can access them. Create them in Studio rather than in scripts so they're easy to find.
- [5:31](https://youtu.be/3wkPekjQvKg?t=331) **[[client-server-and-remotes]]** Client sends with FireServer; server listens with OnServerEvent:Connect. Use WaitForChild on the client before indexing the event to avoid nil errors.
- [10:05](https://youtu.be/3wkPekjQvKg?t=605) **[[client-server-and-remotes]]** Use FireClient(player, ...) to reveal something to a single player, and always specify the target player. Server-side changes to a single client's view (e.g. a door) are only visible to that client.
- [11:55](https://youtu.be/3wkPekjQvKg?t=715) **[[client-server-and-remotes]]** Use FireAllClients(data) to broadcast to every client. Pass only needed data such as player.Name, not the whole Player object.
- [10:05](https://youtu.be/3wkPekjQvKg?t=605) **[[anti-exploit-and-security]]** Gate sensitive actions like admin-only features with a server-side check (e.g. comparing UserId) before firing to the client; client-side checks alone are not secure.

## Tools
Roblox Studio, RemoteEvent, FilteringEnabled

## Topics
[[anti-exploit-and-security]] [[client-server-and-remotes]]

Back to [[GnomeCode - How to make successful Roblox games]]
