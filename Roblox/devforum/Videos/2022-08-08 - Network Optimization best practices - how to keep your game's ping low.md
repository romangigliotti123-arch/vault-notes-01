---
title: "Network Optimization best practices - how to keep your game's ping low!"
url: https://devforum.roblox.com/t/network-optimization-best-practices-how-to-keep-your-games-ping-low/1913475
creator: Roblox DevForum
official: false
advice_density: high
date: 2022-08-08
views: 275
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Network Optimization best practices - how to keep your game's ping low!

[Open](https://devforum.roblox.com/t/network-optimization-best-practices-how-to-keep-your-games-ping-low/1913475) | Roblox DevForum | 275 views | 2022-08-08

## Summary
Roblox DevForum-style guide on reducing network bandwidth and ping: byte costs of remote data types, sending minimal data, converting dictionaries to arrays, packing data, a SerDes layer separating remote logic from game logic, and CFrame/Color3/Vector3int16 size tricks.

## Tips
- [page](https://devforum.roblox.com/t/network-optimization-best-practices-how-to-keep-your-games-ping-low/1913475) **[[scripting-and-performance]]** Send only the fields the client needs (e.g. item name and class), not full tables with history or damage data.
- [page](https://devforum.roblox.com/t/network-optimization-best-practices-how-to-keep-your-games-ping-low/1913475) **[[client-server-and-remotes]]** Create all VFX on the client; send a short string like 'SpawnParticle' instead of replicating server-created particles and their properties.
- [page](https://devforum.roblox.com/t/network-optimization-best-practices-how-to-keep-your-games-ping-low/1913475) **[[client-server-and-remotes]]** Convert dictionaries to arrays for remote payloads to avoid per-key string overhead; hardcode field order in a shared PackFormat module.
- [page](https://devforum.roblox.com/t/network-optimization-best-practices-how-to-keep-your-games-ping-low/1913475) **[[client-server-and-remotes]]** Pack frequently sent data compactly; e.g. GenerateGUID(false) hex strings can pack two characters per byte, halving size. Do not use packed strings in DataStores (invalid UTF-8 risk).
- [page](https://devforum.roblox.com/t/network-optimization-best-practices-how-to-keep-your-games-ping-low/1913475) **[[client-server-and-remotes]]** Put all remote connections and serialization/deserialization in one SerDes module so game scripts receive already-deserialized values.
- [page](https://devforum.roblox.com/t/network-optimization-best-practices-how-to-keep-your-games-ping-low/1913475) **[[optimization-and-streaming]]** Do not use math.floor to shrink numbers; all numbers are sent as 8-byte Float64 regardless.
- [page](https://devforum.roblox.com/t/network-optimization-best-practices-how-to-keep-your-games-ping-low/1913475) **[[optimization-and-streaming]]** For colours limited to 0-255, send three Int8s packed into a string (about 5 bytes) instead of a Color3 (12 bytes).
- [page](https://devforum.roblox.com/t/network-optimization-best-practices-how-to-keep-your-games-ping-low/1913475) **[[optimization-and-streaming]]** Use Vector3int16 for integer-only position data when decimals can be discarded; it is half the size of Vector3.
- [page](https://devforum.roblox.com/t/network-optimization-best-practices-how-to-keep-your-games-ping-low/1913475) **[[optimization-and-streaming]]** Use axis-aligned CFrames (rotations that are multiples of 90 degrees) where possible; they send only a 1-byte rotation ID instead of full rotation data.

## Numbers
- [page](https://devforum.roblox.com/t/network-optimization-best-practices-how-to-keep-your-games-ping-low/1913475) Remote overhead: **9 bytes per remote call (e.g. FireServer)** (Fixed cost per Remote:FireServer() call)
- [page](https://devforum.roblox.com/t/network-optimization-best-practices-how-to-keep-your-games-ping-low/1913475) Type overhead: **1 byte per value sent** (Every data type adds one byte for its type)
- [page](https://devforum.roblox.com/t/network-optimization-best-practices-how-to-keep-your-games-ping-low/1913475) String size: **#String + 2 bytes** (e.g. "1234" = 6 bytes plus 1 type byte)
- [page](https://devforum.roblox.com/t/network-optimization-best-practices-how-to-keep-your-games-ping-low/1913475) Number size: **8 bytes (Float64) + 1 type byte** (All numbers sent via remotes, math.floor does not help)
- [page](https://devforum.roblox.com/t/network-optimization-best-practices-how-to-keep-your-games-ping-low/1913475) Vector3 size: **12 bytes (three Float32) + 1 type byte** (Vector3 sent through a remote)
- [page](https://devforum.roblox.com/t/network-optimization-best-practices-how-to-keep-your-games-ping-low/1913475) Color3 size: **12 bytes (three Float32)** (Packed as Int8s in string: about 5 bytes)
- [page](https://devforum.roblox.com/t/network-optimization-best-practices-how-to-keep-your-games-ping-low/1913475) Instance size: **4 bytes** (Instances sent through remotes are cheaper than a 3-char string or a number)
- [page](https://devforum.roblox.com/t/network-optimization-best-practices-how-to-keep-your-games-ping-low/1913475) GUID string size: **36 characters, 38 bytes; packed hex halves it** (HttpService:GenerateGUID(false))
- [page](https://devforum.roblox.com/t/network-optimization-best-practices-how-to-keep-your-games-ping-low/1913475) CFrame axis-aligned rotation: **24 special cases, 1-byte rotation ID** (Rotations that are multiples of 90 degrees send no rotation data)
- [page](https://devforum.roblox.com/t/network-optimization-best-practices-how-to-keep-your-games-ping-low/1913475) Unit definition: **1 KB = 1000 bytes** (Stated as baseline for bandwidth thinking)

## Tools
Packet Profiler (author's plugin, measures remote packet bandwidth), HttpService:GenerateGUID

## He points to
- Packet Profiler plugin by PysephDEV

## Quotes
- [page](https://devforum.roblox.com/t/network-optimization-best-practices-how-to-keep-your-games-ping-low/1913475) "The absolutely best way to optimize your game's netcode while keeping the rest of your code readable and logical is to separate your remote logic from your game logic."
- [page](https://devforum.roblox.com/t/network-optimization-best-practices-how-to-keep-your-games-ping-low/1913475) "Arrays don't take any extra size for their indices, only values!"

## Topics
[[client-server-and-remotes]] [[optimization-and-streaming]] [[scripting-and-performance]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
