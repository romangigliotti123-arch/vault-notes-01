---
title: "Suphi's DataStore Module Advanced - Roblox Scripting Tutorial"
url: https://youtu.be/ykWkDov_x-8
creator: Suphi Kaner
official: false
advice_density: medium
date: 2023-06-16
views: 7968
transcript: auto-captions
confidence: high
tags: [roblox, 5uphi, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.8
---

> [!note] Trust: TRUSTED (credibility audit score 8.8): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Suphi's DataStore Module Advanced - Roblox Scripting Tutorial

[Watch](https://youtu.be/ykWkDov_x-8) | 5uphi | 7,968 views | 2023-06-16

## Summary
Advanced walkthrough of Suphi's DataStore module: Hidden vs New vs Find for server emulation and player-joins-mid-open edge cases, the Queue system for cross-server messaging (queue, process, remove, re-queue on save failure), and compression options (level, decimals, safety) with the usage function.

## Tips
- [2:20](https://youtu.be/ykWkDov_x-8?t=140) **[[data-persistence]]** Use DataStore.Hidden when opening a player's store on a server where they may not be; New returns a shared object that can be destroyed mid-use, causing nil errors.
- [6:29](https://youtu.be/ykWkDov_x-8?t=389) **[[data-persistence]]** Use Find first to reuse an already-open store on this server, otherwise create Hidden; then destroy only if the store is hidden to avoid leaks.
- [9:34](https://youtu.be/ykWkDov_x-8?t=574) **[[data-persistence]]** Queue data via DataStore:Queue(value, expirySeconds, priority) from any state; default expiry is 7 days, max 45 days. Use it to message the server that holds a locked store.
- [11:41](https://youtu.be/ykWkDov_x-8?t=701) **[[data-persistence]]** Queue processing needs the store open and at least one ProcessQueue connection; otherwise the queue stays dormant. Call remove(id) after processing or values re-fire every 30s.
- [16:30](https://youtu.be/ykWkDov_x-8?t=990) **[[data-persistence]]** Handle Open responses explicitly: success sets value, locked queues a message to the owning server, error means Roblox issues and fall back to queueing.
- [21:24](https://youtu.be/ykWkDov_x-8?t=1284) **[[data-persistence]]** Queue processing tradeoff: remove-then-save can lose coins if save fails; save-then-remove can double-grant. Pick based on how critical the reward is.
- [28:20](https://youtu.be/ykWkDov_x-8?t=1700) **[[data-persistence]]** Check DataStore:Usage() to monitor character count and percent of the 4MB limit before the store fills up.
- [31:04](https://youtu.be/ykWkDov_x-8?t=1864) **[[data-persistence]]** Enable compression only as a last resort; it costs CPU on every save. Enable by setting metadata.compress after opening and save the value in compressed form.
- [35:58](https://youtu.be/ykWkDov_x-8?t=2158) **[[anti-exploit-and-security]]** Keep compression safety=true when storing strings from RemoteEvents, since clients can send the delete character that breaks compressed strings.
- [34:34](https://youtu.be/ykWkDov_x-8?t=2074) **[[data-persistence]]** Compression level 1 supports mixed arrays; decimals default 3 truncates extra decimals, so raise it only if precision matters (costs characters).

## Numbers
- [9:34](https://youtu.be/ykWkDov_x-8?t=574) Queue default expiry: **7 days (max 45 days)** (DataStore:Queue default expiration time)
- [14:26](https://youtu.be/ykWkDov_x-8?t=866) Queue re-fire interval: **30 seconds** (ProcessQueue fires repeatedly until values are removed)
- [5:46](https://youtu.be/ykWkDov_x-8?t=346) Locked retry interval: **5 seconds, increasing (5, 6, ...)** (Retry loop when DataStore open returns locked)
- [30:23](https://youtu.be/ykWkDov_x-8?t=1823) Compression test size: **76 chars reduced to 58 chars** (Example table with default compression)
- [35:15](https://youtu.be/ykWkDov_x-8?t=2115) Default compression decimals: **3** (Decimals setting; default keeps 3 decimal places)

## Tools
Suphi's DataStore Module

## He points to
- Suphi's DataStore module basics video (prerequisite)

## Topics
[[anti-exploit-and-security]] [[data-persistence]]

Back to [[5uphi - How to make successful Roblox games]]
