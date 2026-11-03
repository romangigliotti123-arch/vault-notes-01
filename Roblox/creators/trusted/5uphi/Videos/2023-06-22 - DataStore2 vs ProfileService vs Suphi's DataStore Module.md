---
title: "DataStore2 vs ProfileService vs Suphi's DataStore Module"
url: https://youtu.be/ARPfIt16sXI
creator: Suphi Kaner
official: false
advice_density: high
date: 2023-06-22
views: 19642
transcript: auto-captions
confidence: high
tags: [roblox, 5uphi, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.8
---

> [!note] Trust: TRUSTED (credibility audit score 8.8): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# DataStore2 vs ProfileService vs Suphi's DataStore Module

[Watch](https://youtu.be/ARPfIt16sXI) | 5uphi | 19,642 views | 2023-06-22

## Summary
Source-code walkthrough comparing three Roblox DataStore wrappers: DataStore2 (save methods, Promise, cloning, validation), ProfileService (session locking via UpdateAsync active session plus OS time timeout) and Suphi's DataStore module (MemoryStore locks, per-session settings, task manager, compression). Explains trade-offs of each.

## Tips
- [0:13](https://youtu.be/ARPfIt16sXI?t=13) **[[data-persistence]]** Use a session-locking module (ProfileService or Suphi's) so two servers cannot overwrite the same player's data.
- [5:05](https://youtu.be/ARPfIt16sXI?t=305) **[[data-persistence]]** Use UpdateAsync only when reading the previous value to modify it (e.g. adding coins); passing a fixed value to UpdateAsync gains nothing and wastes budget.
- [10:36](https://youtu.be/ARPfIt16sXI?t=636) **[[data-persistence]]** Don't build ordered-backup versioning yourself; Roblox keeps previous DataStore versions for up to 30 days.
- [11:59](https://youtu.be/ARPfIt16sXI?t=719) **[[data-persistence]]** Avoid the ordered-backup save pattern: it has two points of failure and uses extra get/sorted-get budget.
- [24:02](https://youtu.be/ARPfIt16sXI?t=1442) **[[data-persistence]]** Don't rely on os.time() for lock expiry across servers; server clocks can drift, so a 30-minute timeout is unreliable.
- [39:18](https://youtu.be/ARPfIt16sXI?t=2358) **[[data-persistence]]** Store session locks in MemoryStore with an expiration via UpdateAsync; it avoids OS time and uses less DataStore budget.
- [40:41](https://youtu.be/ARPfIt16sXI?t=2441) **[[data-persistence]]** Make save and lock intervals configurable per session so important sessions save more often and others use fewer requests.
- [45:35](https://youtu.be/ARPfIt16sXI?t=2735) **[[data-persistence]]** Keep lock timeouts short (about 3 attempts, 30s apart) so players are not blocked for 30 minutes after a server crash.
- [36:32](https://youtu.be/ARPfIt16sXI?t=2192) **[[optimization-and-streaming]]** Avoid deep-cloning data on every get/set; clone only on reconcile or explicit clone to reduce CPU cost.
- [37:14](https://youtu.be/ARPfIt16sXI?t=2234) **[[scripting-and-performance]]** Schedule timers with task.delay and cancel them with task.cancel; use os.clock for drift-free intervals.
- [28:17](https://youtu.be/ARPfIt16sXI?t=1697) **[[code-architecture-and-frameworks]]** Use a custom signal module rather than BindableEvents when signal behavior may change (Workspace setting deferred vs immediate) so the module does not break.
- [27:36](https://youtu.be/ARPfIt16sXI?t=1656) **[[code-architecture-and-frameworks]]** Sandbox module properties with a proxy so invalid values (e.g. lock interval below 10) raise clear errors.
- [31:43](https://youtu.be/ARPfIt16sXI?t=1903) **[[code-architecture-and-frameworks]]** Batch concurrent open/close requests through a task queue so overlapping calls wait on the same operation.
- [15:36](https://youtu.be/ARPfIt16sXI?t=936) **[[data-persistence]]** Session locking means only one server holds a DataStore key open at a time; understand this before choosing a wrapper.
- [14:04](https://youtu.be/ARPfIt16sXI?t=844) **[[client-server-and-remotes]]** Key data wrappers by Player object, not raw userId, so one player's data is open in only one server.
- [5:05](https://youtu.be/ARPfIt16sXI?t=305) **[[common-mistakes]]** Misconception: UpdateAsync is not inherently more secure than SetAsync; it only helps when you read and modify the previous value.

## Numbers
- [4:22](https://youtu.be/ARPfIt16sXI?t=262) ProfileService session lock timeout: **30 minutes (OS-time based, auto-save 30s)** (ProfileService assumes lock dead after 30 min; OS time unreliable)
- [39:18](https://youtu.be/ARPfIt16sXI?t=2358) Suphi lock default: **lock interval 60s, 5 attempts, ~5 min expiry** (MemoryStore lock expiration with 30s buffer)
- [13:23](https://youtu.be/ARPfIt16sXI?t=803) DataStore budget per player: **10 sets, 10 gets, 2 sorted gets** (Ordered-backup save uses 2 sets per save and a sorted get per load)
- [11:18](https://youtu.be/ARPfIt16sXI?t=678) Roblox DataStore version retention: **up to 30 days** (Built-in versioning keeps previous values)
- [11:59](https://youtu.be/ARPfIt16sXI?t=719) Old per-key write limit: **once per 6 seconds (removed)** (Roblox reportedly removed the six-second write limit)
- [45:35](https://youtu.be/ARPfIt16sXI?t=2735) Lowest suggested lock settings: **3 attempts, 30s between attempts** (Suphi's advice for minimum lock timeout)

## Tools
DataStore2, ProfileService, Suphi's DataStore module, MemoryStore, Promise module

## He points to
- Suphi's DataStore module

## Topics
[[client-server-and-remotes]] [[code-architecture-and-frameworks]] [[common-mistakes]] [[data-persistence]] [[optimization-and-streaming]] [[scripting-and-performance]]

Back to [[5uphi - How to make successful Roblox games]]
