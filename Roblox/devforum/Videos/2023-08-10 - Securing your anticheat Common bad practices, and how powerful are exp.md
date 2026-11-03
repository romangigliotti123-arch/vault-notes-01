---
title: "Securing your anticheat: Common bad practices, and how powerful are exploiters (+ Guide on Handshakes)"
url: https://devforum.roblox.com/t/securing-your-anticheat-common-bad-practices-and-how-powerful-are-exploiters-guide-on-handshakes/2519952
creator: Roblox DevForum
official: false
advice_density: high
date: 2023-08-10
views: 110
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Securing your anticheat: Common bad practices, and how powerful are exploiters (+ Guide on Handshakes)

[Open](https://devforum.roblox.com/t/securing-your-anticheat-common-bad-practices-and-how-powerful-are-exploiters-guide-on-handshakes/2519952) | Roblox DevForum | 110 views | 2023-08-10

## Summary
Devforum tutorial by an anticheat developer covering common client anticheat mistakes (FireServer-based ban remotes, client-side physics checks, rawequal detection), how exploiter power depends on executor, game, and skill, and a basic handshake/encryption pattern for server-validated client anticheats.

## Tips
- [page](https://devforum.roblox.com/t/securing-your-anticheat-common-bad-practices-and-how-powerful-are-exploiters-guide-on-handshakes/2519952) **[[anti-exploit-and-security]]** Don't signal tampering with FireServer/InvokeServer to a ban remote; exploiters can hook it and silently drop the call. Use a RemoteFunction the server polls via InvokeClient.
- [page](https://devforum.roblox.com/t/securing-your-anticheat-common-bad-practices-and-how-powerful-are-exploiters-guide-on-handshakes/2519952) **[[anti-exploit-and-security]]** Never run physics/noclip checks on the client; exploiters spoof HumanoidRootPart position (e.g. return Vector3.zero). Do position validation on the server.
- [page](https://devforum.roblox.com/t/securing-your-anticheat-common-bad-practices-and-how-powerful-are-exploiters-guide-on-handshakes/2519952) **[[anti-exploit-and-security]]** Avoid detections based on rawequal, rawget or rawset on the client unless inside a metatable context; exploiters can hook them to return spoofed results.
- [page](https://devforum.roblox.com/t/securing-your-anticheat-common-bad-practices-and-how-powerful-are-exploiters-guide-on-handshakes/2519952) **[[anti-exploit-and-security]]** Add a handshake: server sends a random value, client returns an encrypted response with tamper flag, server verifies and checks for replay; kick on failure or timeout.
- [page](https://devforum.roblox.com/t/securing-your-anticheat-common-bad-practices-and-how-powerful-are-exploiters-guide-on-handshakes/2519952) **[[anti-exploit-and-security]]** Treat exploiter capability as variable: it depends on executor (UNC support, Synapse-only functions), target game mechanics, and whether the user is a consumer or a script developer.
- [page](https://devforum.roblox.com/t/securing-your-anticheat-common-bad-practices-and-how-powerful-are-exploiters-guide-on-handshakes/2519952) **[[anti-exploit-and-security]]** Kick or timeout a client that stops responding to the anticheat remote (e.g. after 60 seconds) since yielding the remote suggests bypass.

## Numbers
- [page](https://devforum.roblox.com/t/securing-your-anticheat-common-bad-practices-and-how-powerful-are-exploiters-guide-on-handshakes/2519952) Roblox game server tickrate: **15 Hz** (Cited as reason devs move noclip checks to client; server workload concern)
- [page](https://devforum.roblox.com/t/securing-your-anticheat-common-bad-practices-and-how-powerful-are-exploiters-guide-on-handshakes/2519952) Noclip check sampling window: **0.5-1 second** (Typical wait between saving old position and raycasting to new position)
- [page](https://devforum.roblox.com/t/securing-your-anticheat-common-bad-practices-and-how-powerful-are-exploiters-guide-on-handshakes/2519952) Client response timeout example: **60 seconds** (Example threshold before kicking unresponsive anticheat client)
- [page](https://devforum.roblox.com/t/securing-your-anticheat-common-bad-practices-and-how-powerful-are-exploiters-guide-on-handshakes/2519952) Handshake interval example: **5 seconds** (Wait between server handshake checks in sample code)

## Games
- **Anomic**: Client-side noclip check there is easily spoofed, so a big game risks flying hackers; move checks to server.
- **Arsenal**: Aimbot and ESP scripts make exploiters powerful in shooters.
- **Pet Simulator X**: Autofarm scripts are the main exploit vector in simulator games.

## Tools
Synapse X (syn.trampoline_call), UNC (Unified Naming Convention), Celery executor, Fluxus, Script-Ware

## He points to
- CodedViolet devforum tutorial on client anticheat base
- HexadecimalLiker devforum anticheat replies

## Quotes
- [page](https://devforum.roblox.com/t/securing-your-anticheat-common-bad-practices-and-how-powerful-are-exploiters-guide-on-handshakes/2519952) "It's a very bad practice as it can just be bypassed by this simple code snippet"
- [page](https://devforum.roblox.com/t/securing-your-anticheat-common-bad-practices-and-how-powerful-are-exploiters-guide-on-handshakes/2519952) "This is very bad especially for a game as big as Anomic since there will be a 99% chance that a hacker will be in the game"

## Topics
[[anti-exploit-and-security]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
