---
title: "Introducing Luau buffer type [Beta]"
url: https://devforum.roblox.com/t/introducing-luau-buffer-type-beta/2724894
creator: Roblox DevForum
official: false
advice_density: medium
date: 2023-11-30
views: 883
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Introducing Luau buffer type [Beta]

[Open](https://devforum.roblox.com/t/introducing-luau-buffer-type-beta/2724894) | Roblox DevForum | 883 views | 2023-11-30

## Summary
Roblox DevForum announcement introducing the Luau 'buffer' type and buffer library (Beta, Nov 2023), covering creation, read/write functions, network replication with compression, and limitations such as DataStore and attribute support.

## Tips
- [page](https://devforum.roblox.com/t/introducing-luau-buffer-type-beta/2724894) **[[optimization-and-streaming]]** Group many small buffers into one large buffer before sending, so on-the-wire compression can work more effectively.
- [page](https://devforum.roblox.com/t/introducing-luau-buffer-type-beta/2724894) **[[client-server-and-remotes]]** Keep buffers sent over remote events under 50 MB; network replication limits are smaller than max buffer size.
- [page](https://devforum.roblox.com/t/introducing-luau-buffer-type-beta/2724894) **[[scripting-and-performance]]** Use buffers instead of string.unpack or large number arrays for compact binary data; buffers are faster to read and cheaper for GC.
- [page](https://devforum.roblox.com/t/introducing-luau-buffer-type-beta/2724894) **[[luau-language-and-types]]** Buffers are not auto-resizable; estimate an upper bound, compute exact size in a prior pass, or resize adaptively with buffer.create/buffer.copy.
- [page](https://devforum.roblox.com/t/introducing-luau-buffer-type-beta/2724894) **[[client-server-and-remotes]]** Buffers cannot be stored in attributes but can be passed via BindableEvent/RemoteEvent; passing copies data, not reference identity.
- [page](https://devforum.roblox.com/t/introducing-luau-buffer-type-beta/2724894) **[[data-persistence]]** Do not store buffer.tostring output in DataStores; it often contains non-UTF8 bytes. Later updates added DataStore support.
- [page](https://devforum.roblox.com/t/introducing-luau-buffer-type-beta/2724894) **[[scripting-and-performance]]** Use 0-based offsets with buffer read/write functions, and scale floats to integers (e.g. degrees*100 in i16) to save bytes.

## Numbers
- [page](https://devforum.roblox.com/t/introducing-luau-buffer-type-beta/2724894) Max network buffer size: **under 50 MB for remote events** (Recommended limit for buffers sent over remote events)
- [page](https://devforum.roblox.com/t/introducing-luau-buffer-type-beta/2724894) Example packing: **18 bytes per object (12 for f32 position, 6 for i16 orientation)** (Transform replication example from the announcement)

## Tools
Roblox Studio Beta Features (Luau Buffer Type), Luau buffer library

## He points to
- Roblox Creator Hub buffer documentation
- Luau website buffer documentation
- Luau GitHub RFC for buffer type

## Topics
[[client-server-and-remotes]] [[data-persistence]] [[luau-language-and-types]] [[optimization-and-streaming]] [[scripting-and-performance]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
