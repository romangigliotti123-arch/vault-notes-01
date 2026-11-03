---
title: "Data storing/presenting using ProfileService and ReplicaService!"
url: https://devforum.roblox.com/t/data-storingpresenting-using-profileservice-and-replicaservice/1464984
creator: Roblox DevForum
official: false
advice_density: medium
date: 2021-09-12
views: 119
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Data storing/presenting using ProfileService and ReplicaService!

[Open](https://devforum.roblox.com/t/data-storingpresenting-using-profileservice-and-replicaservice/1464984) | Roblox DevForum | 119 views | 2021-09-12

## Summary
Devforum tutorial on using ProfileService (session-locked saving via ProfileStore, LoadProfileAsync with ForceLoad, Release, BindToClose) plus ReplicaService to replicate server-side player data to clients, with a click-to-add-cash example and a client LocalScript setup.

## Tips
- [page](https://devforum.roblox.com/t/data-storingpresenting-using-profileservice-and-replicaservice/1464984) **[[data-persistence]]** Use ProfileService instead of raw DataStoreService for saving; its session locking prevents item loss and duplication from race conditions between servers.
- [page](https://devforum.roblox.com/t/data-storingpresenting-using-profileservice-and-replicaservice/1464984) **[[data-persistence]]** Pass a template table to GetProfileStore so new players get default values (e.g. Cash = 100) and schema stays consistent.
- [page](https://devforum.roblox.com/t/data-storingpresenting-using-profileservice-and-replicaservice/1464984) **[[data-persistence]]** Call Profile:ListenToRelease to clean up your local profile table, and check player:IsDescendantOf(Players) after loading before storing the profile.
- [page](https://devforum.roblox.com/t/data-storingpresenting-using-profileservice-and-replicaservice/1464984) **[[data-persistence]]** If LoadProfileAsync returns nil, kick the player with a rejoin message rather than leaving them in a broken state.
- [page](https://devforum.roblox.com/t/data-storingpresenting-using-profileservice-and-replicaservice/1464984) **[[data-persistence]]** Release profiles in PlayerRemoving and also in game:BindToClose, since PlayerRemoving may not fire when the server shuts down quickly.
- [page](https://devforum.roblox.com/t/data-storingpresenting-using-profileservice-and-replicaservice/1464984) **[[client-server-and-remotes]]** Server-side profile data is not visible to clients; replicate it with ReplicaService replicas, using Replication = player to limit a replica to one player.
- [page](https://devforum.roblox.com/t/data-storingpresenting-using-profileservice-and-replicaservice/1464984) **[[client-server-and-remotes]]** Update replicated state with Replica:SetValue alongside saved data changes so client UI stays in sync with the server data.
- [page](https://devforum.roblox.com/t/data-storingpresenting-using-profileservice-and-replicaservice/1464984) **[[anti-exploit-and-security]]** Validate on the server before changing data: check the value type matches the existing type and only modify server-side profile data.
- [page](https://devforum.roblox.com/t/data-storingpresenting-using-profileservice-and-replicaservice/1464984) **[[common-mistakes]]** Don't assign to DataReplicas[player] after nil-ing it; the destroy call in ListenToRelease in the tutorial code is wrong and should be replica:Destroy() before clearing the reference.

## Numbers
- [page](https://devforum.roblox.com/t/data-storingpresenting-using-profileservice-and-replicaservice/1464984) Starting cash default: **100** (Template value for Cash in the ProfileStore example)
- [page](https://devforum.roblox.com/t/data-storingpresenting-using-profileservice-and-replicaservice/1464984) Click increment: **+1 per click** (Demo part adds 1 Cash per MouseClick)

## Tools
ProfileService, ReplicaService, DataStoreService, Roblox Studio

## He points to
- ProfileService API page (loleris)
- ReplicaService API page (loleris)
- DataStore 2.0
- LuckyDataStore

## Topics
[[anti-exploit-and-security]] [[client-server-and-remotes]] [[common-mistakes]] [[data-persistence]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
