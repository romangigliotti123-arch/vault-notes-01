---
title: "ProfileService Tutorial!"
url: https://devforum.roblox.com/t/profileservice-tutorial/1926732
creator: Roblox DevForum
official: false
advice_density: high
date: 2022-08-17
views: 158
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# ProfileService Tutorial!

[Open](https://devforum.roblox.com/t/profileservice-tutorial/1926732) | Roblox DevForum | 158 views | 2022-08-17

## Summary
Tutorial on saving Roblox player data with ProfileService: why to use a proven module instead of a custom DataStore, a full annotated server script (profile template, load/release, GDPR AddUserId, Reconcile, ListenToRelease, Cache sharing), migrating from an old DataStore, and a note that DataStore2 works fine too.

## Tips
- [page](https://devforum.roblox.com/t/profileservice-tutorial/1926732) **[[data-persistence]]** Don't write your own DataStore module unless you have proper security; use a proven one like ProfileService or DataStore2.
- [page](https://devforum.roblox.com/t/profileservice-tutorial/1926732) **[[data-persistence]]** Define all default fields in ProfileTemplate; updating the template won't add missing values to existing player profiles.
- [page](https://devforum.roblox.com/t/profileservice-tutorial/1926732) **[[data-persistence]]** Call profile:Reconcile() after loading to fill in template fields missing from older saves.
- [page](https://devforum.roblox.com/t/profileservice-tutorial/1926732) **[[data-persistence]]** Call profile:Release() in PlayerRemoving and kick players in ListenToRelease, since the profile may be loaded on another server.
- [page](https://devforum.roblox.com/t/profileservice-tutorial/1926732) **[[data-persistence]]** Kick the player if LoadProfileAsync returns nil, which usually means another server is loading the same profile.
- [page](https://devforum.roblox.com/t/profileservice-tutorial/1926732) **[[data-persistence]]** Call profile:AddUserId(player.UserId) for GDPR compliance.
- [page](https://devforum.roblox.com/t/profileservice-tutorial/1926732) **[[data-persistence]]** Handle players who leave before their profile finishes loading by releasing the profile immediately.
- [page](https://devforum.roblox.com/t/profileservice-tutorial/1926732) **[[data-persistence]]** When migrating from an old DataStore, load the old data for joining players into their profile, then delete the old record; remove the old code later.
- [page](https://devforum.roblox.com/t/profileservice-tutorial/1926732) **[[data-persistence]]** If you already use DataStore2 and it works, there is no need to switch to ProfileService.
- [page](https://devforum.roblox.com/t/profileservice-tutorial/1926732) **[[scripting-and-performance]]** Load data for players already in the server with task.spawn, in case they joined before the script ran.
- [page](https://devforum.roblox.com/t/profileservice-tutorial/1926732) **[[code-architecture-and-frameworks]]** Share loaded profile data with other scripts through a Cache module keyed by UserId, rather than requiring the profile directly.

## Tools
ProfileService, DataStore2, Roblox DataStore

## He points to
- Save your player data with ProfileService! (DataStore Module) - DevForum Community Resources

## Topics
[[code-architecture-and-frameworks]] [[data-persistence]] [[scripting-and-performance]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
