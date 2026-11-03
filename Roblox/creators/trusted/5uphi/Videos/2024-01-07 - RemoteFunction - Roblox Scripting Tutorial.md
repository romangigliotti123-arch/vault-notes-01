---
title: "RemoteFunction - Roblox Scripting Tutorial"
url: https://youtu.be/A14qFAyFYhQ
creator: Suphi Kaner
official: false
advice_density: low
date: 2024-01-07
views: 28742
transcript: auto-captions
confidence: high
tags: [roblox, 5uphi, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.8
---

> [!note] Trust: TRUSTED (credibility audit score 8.8): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# RemoteFunction - Roblox Scripting Tutorial

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Watch](https://youtu.be/A14qFAyFYhQ) | 5uphi | 28,742 views | 2024-01-07

## Summary
Shows why Roblox RemoteFunctions are unsafe: a malicious client that never returns makes InvokeClient yield forever, causing a memory leak. Builds a custom event-based invoke with per-player thread queues and a 5s timeout, then demos Suphi's RemoteFunction module from the Toolbox.

## Tips
- [1:00](https://youtu.be/A14qFAyFYhQ?t=60) **[[client-server-and-remotes]]** Never use RemoteFunction:InvokeClient on untrusted clients; an exploiter that never returns makes the server thread yield forever and leak memory.
- [2:59](https://youtu.be/A14qFAyFYhQ?t=179) **[[client-server-and-remotes]]** Wrap server-to-client requests in a timeout (task.delay, ~5s) that resumes the waiting thread, so unresponsive clients can't hang the server.
- [11:16](https://youtu.be/A14qFAyFYhQ?t=676) **[[anti-exploit-and-security]]** Validate that per-player request data exists before handling client responses, since exploiters can fire remotes you never requested.
- [9:53](https://youtu.be/A14qFAyFYhQ?t=593) **[[scripting-and-performance]]** Clear per-player tables once they are empty so no data lingers and memory doesn't leak.

## Numbers
- [5:46](https://youtu.be/A14qFAyFYhQ?t=346) timeout duration: **5 seconds used in custom invoke example**
- [14:46](https://youtu.be/A14qFAyFYhQ?t=886) test: client wait 2s vs 6s: **2s response succeeds; 6s returns nil**

## Tools
Roblox RemoteFunction, RemoteEvent, task.delay / task.cancel / coroutine.yield/resume, Suphi's RemoteFunction module (Toolbox)

## Topics
[[ai-and-tools]] [[anti-exploit-and-security]] [[client-server-and-remotes]] [[scripting-and-performance]]

Back to [[5uphi - How to make successful Roblox games]]
