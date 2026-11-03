---
title: "Replica - Server to client state replication (Module)"
url: https://devforum.roblox.com/t/replica-server-to-client-state-replication-module/3216980
creator: Roblox DevForum
official: false
advice_density: medium
date: 2024-10-16
views: 568
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Replica - Server to client state replication (Module)

[Open](https://devforum.roblox.com/t/replica-server-to-client-state-replication-module/3216980) | Roblox DevForum | 568 views | 2024-10-16

## Summary
Documentation page for Replica, a successor to ReplicaService by loleris: a server-to-client state replication module. Covers creating replicas server-side, subscribing players, Set/OnSet listeners, and differences from ReplicaService (renamed members, no Replication/Parent constructor args, Maid:Add cleanup).

## Tips
- [page](https://devforum.roblox.com/t/replica-server-to-client-state-replication-module/3216980) **[[data-persistence]]** Use ProfileStore (DataStore wrapper) for player data persistence; Replica is for replicating state, not saving it.
- [page](https://devforum.roblox.com/t/replica-server-to-client-state-replication-module/3216980) **[[client-server-and-remotes]]** Create and modify replicas only on the server; clients receive them via Replica.OnNew and listen with OnSet.
- [page](https://devforum.roblox.com/t/replica-server-to-client-state-replication-module/3216980) **[[client-server-and-remotes]]** Call Replica.RequestData() once client-side so replicas are received; new replicas are not replicated until Replicate() or Subscribe(player) is called.
- [page](https://devforum.roblox.com/t/replica-server-to-client-state-replication-module/3216980) **[[client-server-and-remotes]]** Use Replica:BindToInstance() for Roblox streaming support so replicas tie to instances that stream in and out.
- [page](https://devforum.roblox.com/t/replica-server-to-client-state-replication-module/3216980) **[[common-mistakes]]** Don't rely on the old ReplicaService names; Replica renamed members (use Replica.Maid:Add instead of AddCleanupTask, SetParent after construction instead of Parent arg).
- [page](https://devforum.roblox.com/t/replica-server-to-client-state-replication-module/3216980) **[[client-server-and-remotes]]** For advanced high-efficiency custom replication, consider Sera, a bare-bones schematized serialization library.

## Tools
Replica, ReplicaService, ProfileStore, Sera

## He points to
- Replica GitHub repo
- Replica wiki
- ProfileStore
- Sera

## Topics
[[client-server-and-remotes]] [[common-mistakes]] [[data-persistence]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
