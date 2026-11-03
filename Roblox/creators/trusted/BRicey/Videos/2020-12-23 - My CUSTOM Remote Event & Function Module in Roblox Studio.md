---
title: "My CUSTOM Remote Event & Function Module in Roblox  Studio"
url: https://youtu.be/6ZgzabMLkKQ
creator: B Ricey
official: false
advice_density: medium
date: 2020-12-23
views: 10706
transcript: auto-captions
confidence: high
tags: [roblox, bricey, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.0
---

> [!note] Trust: TRUSTED (credibility audit score 8.0): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# My CUSTOM Remote Event & Function Module in Roblox  Studio

[Watch](https://youtu.be/6ZgzabMLkKQ) | BRicey | 10,706 views | 2020-12-23

## Summary
Showcase and explanation of a custom "Remote Messenger" module that replaces many RemoteEvents/RemoteFunctions with a single pair, routed through a string-command listener system. Covers send/listen usage, variadic args, stop-listening, and the security benefit of command keywords. Mostly a rant/showcase rather than a tutorial.

## Tips
- [1:44](https://youtu.be/6ZgzabMLkKQ?t=104) **[[client-server-and-remotes]]** Consolidate all networking into one RemoteEvent and one RemoteFunction behind a wrapper module to avoid cluttered scripts with many remote references.
- [8:23](https://youtu.be/6ZgzabMLkKQ?t=503) **[[anti-exploit-and-security]]** Route client calls through a string-command listener system so only registered commands run on server; unknown or nil commands are ignored. Not impenetrable, but harder to exploit than open remotes.
- [3:09](https://youtu.be/6ZgzabMLkKQ?t=189) **[[code-architecture-and-frameworks]]** Put the shared remote wrapper in ReplicatedStorage so both client and server require the same module.
- [9:07](https://youtu.be/6ZgzabMLkKQ?t=547) **[[client-server-and-remotes]]** Return a listener object from add listener with a stop-listening method so listeners can be disconnected, mirroring signal connections.
- [7:35](https://youtu.be/6ZgzabMLkKQ?t=455) **[[luau-language-and-types]]** Use variadic arguments (...) in wrapper functions to pass any number of parameters through remotes.
- [12:53](https://youtu.be/6ZgzabMLkKQ?t=773) **[[code-architecture-and-frameworks]]** Consider frameworks like Knit (services and controllers) for organising game-wide networking rather than ad hoc wrappers.
- [10:30](https://youtu.be/6ZgzabMLkKQ?t=630) **[[client-server-and-remotes]]** Use a get-from-server call backed by a remote function for values the client needs to read; keep remote functions free of return logic in event-style listeners.

## Numbers
- [1:44](https://youtu.be/6ZgzabMLkKQ?t=104) Remote count in game: **2 (one RemoteFunction, one RemoteEvent)** (Entire game routed through only two remotes with the module)

## Tools
Roblox Studio, Luau, Remote Messenger module (creator's own, linked in description)

## He points to
- Knit framework
- creator's previous video on command-system security

## Topics
[[anti-exploit-and-security]] [[client-server-and-remotes]] [[code-architecture-and-frameworks]] [[luau-language-and-types]]

Back to [[BRicey - How to make successful Roblox games]]
