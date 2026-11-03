---
title: "How you should secure your game - A beginner guide for secure networking and developing anticheats"
url: https://devforum.roblox.com/t/how-you-should-secure-your-game-a-beginner-guide-for-secure-networking-and-developing-anticheats/351775
creator: Roblox DevForum
official: false
advice_density: high
date: 2019-09-18
views: 734
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# How you should secure your game - A beginner guide for secure networking and developing anticheats

[Open](https://devforum.roblox.com/t/how-you-should-secure-your-game-a-beginner-guide-for-secure-networking-and-developing-anticheats/351775) | Roblox DevForum | 734 views | 2019-09-18

## Summary
Hexcede's beginner guide to Roblox security: why client-side checks fail (bytecode, decompilers, exploiters), client-predicts/server-verifies networking, limiting remote traffic, and passive vs aggressive anticheats with honeypots and false-positive caution.

## Tips
- [page](https://devforum.roblox.com/t/how-you-should-secure-your-game-a-beginner-guide-for-secure-networking-and-developing-anticheats/351775) **[[anti-exploit-and-security]]** Never trust the client: exploiters can read and change any LocalScript/ModuleScript and all remote traffic. Put validation and authority on the server.
- [page](https://devforum.roblox.com/t/how-you-should-secure-your-game-a-beginner-guide-for-secure-networking-and-developing-anticheats/351775) **[[client-server-and-remotes]]** Let the client predict and act immediately, then ask the server to perform the action. The server verifies and clamps the request before applying it.
- [page](https://devforum.roblox.com/t/how-you-should-secure-your-game-a-beginner-guide-for-secure-networking-and-developing-anticheats/351775) **[[client-server-and-remotes]]** Share the same validation code between client and server (e.g. team check and range check) so the server can mirror what the client should do.
- [page](https://devforum.roblox.com/t/how-you-should-secure-your-game-a-beginner-guide-for-secure-networking-and-developing-anticheats/351775) **[[client-server-and-remotes]]** Be ready to resync the client when the server rejects an action, such as removing an item the player never had. This is correct behavior.
- [page](https://devforum.roblox.com/t/how-you-should-secure-your-game-a-beginner-guide-for-secure-networking-and-developing-anticheats/351775) **[[anti-exploit-and-security]]** Keep server-only logic in ServerScriptService/ServerStorage modules; their bytecode is never sent to the client and cannot be decompiled.
- [page](https://devforum.roblox.com/t/how-you-should-secure-your-game-a-beginner-guide-for-secure-networking-and-developing-anticheats/351775) **[[client-server-and-remotes]]** Limit remote traffic to about one basic remote per frame. Sending large tables every frame can grow ping to several seconds.
- [page](https://devforum.roblox.com/t/how-you-should-secure-your-game-a-beginner-guide-for-secure-networking-and-developing-anticheats/351775) **[[client-server-and-remotes]]** Send a full table once, then send only changed properties individually when a value changes, using a __newindex proxy, instead of resending on Heartbeat.
- [page](https://devforum.roblox.com/t/how-you-should-secure-your-game-a-beginner-guide-for-secure-networking-and-developing-anticheats/351775) **[[anti-exploit-and-security]]** Prefer passive anticheats that correct illegal state (reset position, clamp velocity) over kicking; they are more accurate and better for UX.
- [page](https://devforum.roblox.com/t/how-you-should-secure-your-game-a-beginner-guide-for-secure-networking-and-developing-anticheats/351775) **[[anti-exploit-and-security]]** Use a generous leeway (e.g. 2 studs) on speed/noclip checks; low leeway causes rubber-banding during lag.
- [page](https://devforum.roblox.com/t/how-you-should-secure-your-game-a-beginner-guide-for-secure-networking-and-developing-anticheats/351775) **[[anti-exploit-and-security]]** Avoid permanent bans as a main response: exploiters usually just make an alternate account. Soft penalties like disabling purchases or interactions work better.
- [page](https://devforum.roblox.com/t/how-you-should-secure-your-game-a-beginner-guide-for-secure-networking-and-developing-anticheats/351775) **[[anti-exploit-and-security]]** Use honeypot remotes (e.g. a fake AddMoney remote). Any firing of a remote that legitimate code never uses identifies an exploiter.
- [page](https://devforum.roblox.com/t/how-you-should-secure-your-game-a-beginner-guide-for-secure-networking-and-developing-anticheats/351775) **[[anti-exploit-and-security]]** Guard against false positives even at the cost of anticheat strength; never punish a player on an uncertain detection.
- [page](https://devforum.roblox.com/t/how-you-should-secure-your-game-a-beginner-guide-for-secure-networking-and-developing-anticheats/351775) **[[anti-exploit-and-security]]** Disguise soft punishments as glitches, e.g. give a cheater a fake 'Invalid Item', to make cheating annoying without outright banning.

## Numbers
- [page](https://devforum.roblox.com/t/how-you-should-secure-your-game-a-beginner-guide-for-secure-networking-and-developing-anticheats/351775) Leeway for speed/noclip checks: **2 studs** (Example passive anticheat tolerance before correcting player position)
- [page](https://devforum.roblox.com/t/how-you-should-secure-your-game-a-beginner-guide-for-secure-networking-and-developing-anticheats/351775) Remote calls per frame: **~1 basic remote per frame** (Guideline for ping-safe remote traffic)

## Games
- **Hexolus**: Author's game where he implemented and open-sourced a server-sided anticheat.

## Tools
Roblox Studio, LocalScript/ModuleScript/ServerScriptService

## He points to
- Hexolus Server-sided Anticheat (open-source repo, linked by author)

## Quotes
- [page](https://devforum.roblox.com/t/how-you-should-secure-your-game-a-beginner-guide-for-secure-networking-and-developing-anticheats/351775) "Never trust the client!"
- [page](https://devforum.roblox.com/t/how-you-should-secure-your-game-a-beginner-guide-for-secure-networking-and-developing-anticheats/351775) "Permanently banning a player is a huge risk for not a lot of effect."

## Topics
[[anti-exploit-and-security]] [[client-server-and-remotes]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
