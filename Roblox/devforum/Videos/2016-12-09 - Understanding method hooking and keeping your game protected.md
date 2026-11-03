---
title: "Understanding method hooking and keeping your game protected"
url: https://devforum.roblox.com/t/understanding-method-hooking-and-keeping-your-game-protected/31442
creator: Roblox DevForum
official: false
advice_density: high
date: 2016-12-09
views: 377
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Understanding method hooking and keeping your game protected

[Open](https://devforum.roblox.com/t/understanding-method-hooking-and-keeping-your-game-protected/31442) | Roblox DevForum | 377 views | 2016-12-09

## Summary
Developer post on how script injectors exploit Roblox games: stealing assets and code via client-side storage, method hooking (metatable __index detour) to spoof remotes, quick detour checks, and why server-authoritative state design is the real defense. Notes that client-side fixes can be bypassed.

## Tips
- [page](https://devforum.roblox.com/t/understanding-method-hooking-and-keeping-your-game-protected/31442) **[[building-art-and-assets]]** Store models and maps in ServerStorage rather than ReplicatedStorage to reduce asset leaks; clone client-needed assets, delete originals, and hold references to clones.
- [page](https://devforum.roblox.com/t/understanding-method-hooking-and-keeping-your-game-protected/31442) **[[scripting-and-performance]]** Place main code in ModuleScripts, require them, then delete the modules; code keeps running while the requiring script exists. Obfuscation adds further protection but is not absolute.
- [page](https://devforum.roblox.com/t/understanding-method-hooking-and-keeping-your-game-protected/31442) **[[anti-exploit-and-security]]** Assume the client can be hooked or spoofed. Never implement security fully on the client; any client-only solution will eventually be bypassed.
- [page](https://devforum.roblox.com/t/understanding-method-hooking-and-keeping-your-game-protected/31442) **[[anti-exploit-and-security]]** Cache remote methods via a local reference (e.g. local FireServer = Instance.new("RemoteEvent").FireServer) to avoid calling hooked __index results. Only a partial mitigation; resets can undo it.
- [page](https://devforum.roblox.com/t/understanding-method-hooking-and-keeping-your-game-protected/31442) **[[anti-exploit-and-security]]** Compare a cached method to the current one (e.g. RemoteEvent.FireServer) to detect detours. Avoid obvious responses since exploiters can adapt; it is easy to bypass.
- [page](https://devforum.roblox.com/t/understanding-method-hooking-and-keeping-your-game-protected/31442) **[[client-server-and-remotes]]** Use server-authoritative state: the server must validate every state-changing action (item exists, player in range, inventory space) before applying it.
- [page](https://devforum.roblox.com/t/understanding-method-hooking-and-keeping-your-game-protected/31442) **[[client-server-and-remotes]]** Let the client predict locally for responsiveness, keep a server-side authoritative copy of player state, and send corrections when client and server disagree.
- [page](https://devforum.roblox.com/t/understanding-method-hooking-and-keeping-your-game-protected/31442) **[[client-server-and-remotes]]** Avoid trusting remote arguments; a single generic remote dispatching by string is easy to reverse-engineer and abuse by spoofing arguments.
- [page](https://devforum.roblox.com/t/understanding-method-hooking-and-keeping-your-game-protected/31442) **[[anti-exploit-and-security]]** Treat any asset or code visible on the client as potentially exposed; exploiters can save instances to disk and read module source.

## Numbers
- [page](https://devforum.roblox.com/t/understanding-method-hooking-and-keeping-your-game-protected/31442) Client-side code reading: **Modules can be deleted after require; bytecode still decompilable but less readable** (Author's stated protection level for module-based code hiding)
- [page](https://devforum.roblox.com/t/understanding-method-hooking-and-keeping-your-game-protected/31442) Ping example: **250 ping** (Latency example used to justify client-side prediction)

## Games
- **Gunshooter: Online**: Hypothetical example: single generic RemoteEvent with string-dispatched events let an exploiter hook FireServer and instakill; shows the risk of trusting client args.

## Tools
Script injectors (exploit tools), setmetatable / getrawmetatable-style metatable hooking

## He points to
- Roblox DevForum: claylittlehorse, 'Understanding method hooking and keeping your game protected' (Aug 2018 revision)

## Quotes
- [page](https://devforum.roblox.com/t/understanding-method-hooking-and-keeping-your-game-protected/31442) "The solution is not keeping exploiters from method hooking. The client can not be trusted, and any solution that is implemented fully on the client can, and will eventually be bypassed."
- [page](https://devforum.roblox.com/t/understanding-method-hooking-and-keeping-your-game-protected/31442) "We need to allow the client to have a state that is parallel to, not reliant on, the server."

## Topics
[[anti-exploit-and-security]] [[building-art-and-assets]] [[client-server-and-remotes]] [[scripting-and-performance]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
