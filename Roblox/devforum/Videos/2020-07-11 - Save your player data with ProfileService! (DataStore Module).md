---
title: "Save your player data with ProfileService! (DataStore Module)"
url: https://devforum.roblox.com/t/save-your-player-data-with-profileservice-datastore-module/667805
creator: Roblox DevForum
official: false
advice_density: medium
date: 2020-07-11
views: 3632
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Save your player data with ProfileService! (DataStore Module)

[Open](https://devforum.roblox.com/t/save-your-player-data-with-profileservice-datastore-module/667805) | Roblox DevForum | 3,632 views | 2020-07-11

## Summary
Documentation page for ProfileService, a stand-alone ModuleScript by loleris (Madwork) for loading and auto-saving DataStore profiles. Covers session-locking, auto-save, template reconciliation, GDPR UserId tagging, and sample code. Notes the module is stable but superseded by ProfileStore for new projects.

## Tips
- [page](https://devforum.roblox.com/t/save-your-player-data-with-profileservice-datastore-module/667805) **[[development-process-and-speed]]** For new projects, use ProfileStore instead of ProfileService; ProfileService is stable but no longer supported.
- [page](https://devforum.roblox.com/t/save-your-player-data-with-profileservice-datastore-module/667805) **[[data-persistence]]** Load each profile once per server and read/write it locally; auto-save periodically and save once on release, avoiding DataStore calls on every change.
- [page](https://devforum.roblox.com/t/save-your-player-data-with-profileservice-datastore-module/667805) **[[data-persistence]]** Always session-lock profiles (via LoadProfileAsync) to prevent multi-server edits that cause item loss or duplication exploits.
- [page](https://devforum.roblox.com/t/save-your-player-data-with-profileservice-datastore-module/667805) **[[data-persistence]]** Use a ProfileTemplate for defaults, and call Reconcile() to fill missing keys; updating the template does not add missing values to existing profiles otherwise.
- [page](https://devforum.roblox.com/t/save-your-player-data-with-profileservice-datastore-module/667805) **[[data-persistence]]** Handle nil profiles from LoadProfileAsync by kicking the player, and release the profile if the player left before loading finished.
- [page](https://devforum.roblox.com/t/save-your-player-data-with-profileservice-datastore-module/667805) **[[data-persistence]]** Call profile:AddUserId(player.UserId) for GDPR compliance when loading profiles.
- [page](https://devforum.roblox.com/t/save-your-player-data-with-profileservice-datastore-module/667805) **[[data-persistence]]** Use ListenToRelease to clear the local cache and kick the player if the profile was loaded on another server.
- [page](https://devforum.roblox.com/t/save-your-player-data-with-profileservice-datastore-module/667805) **[[client-server-and-remotes]]** ProfileService is server-side only; replicate Profile.Data to clients with a replication module such as ReplicaService.
- [page](https://devforum.roblox.com/t/save-your-player-data-with-profileservice-datastore-module/667805) **[[development-process-and-speed]]** Use task.spawn for players already in server when the script starts, and Players.PlayerAdded/PlayerRemoving connections for the rest.

## Numbers
- [page](https://devforum.roblox.com/t/save-your-player-data-with-profileservice-datastore-module/667805) Bug fix turnaround: **~2-3 days with a decent report** (Stated by module author for ProfileService bugs)
- [page](https://devforum.roblox.com/t/save-your-player-data-with-profileservice-datastore-module/667805) Scalability target: **100+ player servers** (Author says it is built for large servers with DataStore calls spread across auto-save loop)

## Tools
ProfileService, ProfileStore, ReplicaService, Madwork, Roblox Luau task library

## He points to
- ProfileService wiki
- ProfileService on GitHub
- Roblox library (ProfileService)
- M_nzter ProfileService tutorial
- CheekySquid ProfileService in 10 minutes
- okeanskiy ProfileService playlist

## Quotes
- [page](https://devforum.roblox.com/t/save-your-player-data-with-profileservice-datastore-module/667805) "Session-locking is essential to keeping your data protected from multiple server editing - this is a potential cause of item loss or item duplication loopholes."
- [page](https://devforum.roblox.com/t/save-your-player-data-with-profileservice-datastore-module/667805) "ProfileService is server-side only - you'll need replication code to pass Profile.Data to clients."

## Topics
[[client-server-and-remotes]] [[data-persistence]] [[development-process-and-speed]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
