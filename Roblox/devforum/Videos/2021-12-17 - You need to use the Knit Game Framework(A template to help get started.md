---
title: "You need to use the Knit Game Framework(A template to help get started using Knit)"
url: https://devforum.roblox.com/t/you-need-to-use-the-knit-game-frameworka-template-to-help-get-started-using-knit/1592333
creator: Roblox DevForum
official: false
advice_density: medium
date: 2021-12-17
views: 298
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# You need to use the Knit Game Framework(A template to help get started using Knit)

[Open](https://devforum.roblox.com/t/you-need-to-use-the-knit-game-frameworka-template-to-help-get-started-using-knit/1592333) | Roblox DevForum | 298 views | 2021-12-17

## Summary
Documentation page for Knit, a lightweight Roblox framework that abstracts RemoteEvents/Functions and structures code into Services (server), Controllers (client) and Components bound via CollectionService tags. Includes setup Runtime scripts, example service/controller code, a ProfileService-based DataService example, and a list of recommended utility plugins.

## Tips
- [page](https://devforum.roblox.com/t/you-need-to-use-the-knit-game-frameworka-template-to-help-get-started-using-knit/1592333) **[[code-architecture-and-frameworks]]** Use Knit's Service (server) and Controller (client) paradigm to split one-script games into modules that scale better, though one script is viable for performance.
- [page](https://devforum.roblox.com/t/you-need-to-use-the-knit-game-frameworka-template-to-help-get-started-using-knit/1592333) **[[client-server-and-remotes]]** Define client-exposed functions and signals in a service's Client table; Knit creates the RemoteEvents in the background so you don't call RemoteEvents directly.
- [page](https://devforum.roblox.com/t/you-need-to-use-the-knit-game-frameworka-template-to-help-get-started-using-knit/1592333) **[[code-architecture-and-frameworks]]** Put Knit.AddServices and Knit.AddControllers in separate Runtime scripts, then call Knit.Start() on each side; this bootstrapping is configurable unlike Aero.
- [page](https://devforum.roblox.com/t/you-need-to-use-the-knit-game-frameworka-template-to-help-get-started-using-knit/1592333) **[[code-architecture-and-frameworks]]** Use Component.Auto with CollectionService tags to bind classes to instances, with Init, Deinit and update hooks, and clean up connections via Trove.
- [page](https://devforum.roblox.com/t/you-need-to-use-the-knit-game-frameworka-template-to-help-get-started-using-knit/1592333) **[[data-persistence]]** Load profiles with ProfileService on PlayerAdded, handle players already in-game via task.spawn, release profiles on PlayerRemoving, and kick players whose profile is released.
- [page](https://devforum.roblox.com/t/you-need-to-use-the-knit-game-frameworka-template-to-help-get-started-using-knit/1592333) **[[data-persistence]]** Replicate saved data to the client with ReplicaService, using a class token and Replication set to All, so clients read state without custom remotes.
- [page](https://devforum.roblox.com/t/you-need-to-use-the-knit-game-frameworka-template-to-help-get-started-using-knit/1592333) **[[development-process-and-speed]]** Use Rojo to bring professional software engineering tooling into Roblox development.

## Tools
Knit, Rojo, ProfileService, ReplicaService, Trove, Promise, Tag Editor plugin, DataStore Editor plugin

## He points to
- Knit GitHub module
- Rojo (rojo.space)
- Aero Game Framework
- SwapUI, Instance Serializer, InCommand, Studio Levels, Tool Grip Editor, Get Object Path, Easy Crop, Archimedes Two, Weld Plugin (Roblox plugins listed)

## Topics
[[client-server-and-remotes]] [[code-architecture-and-frameworks]] [[data-persistence]] [[development-process-and-speed]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
