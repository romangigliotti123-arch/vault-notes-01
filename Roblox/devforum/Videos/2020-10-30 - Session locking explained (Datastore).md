---
title: "Session locking explained (Datastore)"
url: https://devforum.roblox.com/t/session-locking-explained-datastore/846799
creator: Roblox DevForum
official: false
advice_density: high
date: 2020-10-30
views: 104
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Session locking explained (Datastore)

[Open](https://devforum.roblox.com/t/session-locking-explained-datastore/846799) | Roblox DevForum | 104 views | 2020-10-30

## Summary
Explains session locking for Roblox DataStores: using UpdateAsync with a JobId session tag to prevent data regression and item duplication, plus lease expiry, force-load, and when to use ProfileStore/ProfileService instead of a custom system.

## Tips
- [page](https://devforum.roblox.com/t/session-locking-explained-datastore/846799) **[[monetisation-other]]** Use session locking to prevent data regression and item duplication, e.g. via trading exploits where players rejoin before saves complete.
- [page](https://devforum.roblox.com/t/session-locking-explained-datastore/846799) **[[data-persistence]]** Use only UpdateAsync for session-locked saves; SetAsync and GetAsync cause more network errors and caching issues.
- [page](https://devforum.roblox.com/t/session-locking-explained-datastore/846799) **[[data-persistence]]** Store game.JobId as a session tag in the data; only load if the session is nil or matches the current server.
- [page](https://devforum.roblox.com/t/session-locking-explained-datastore/846799) **[[data-persistence]]** On save, release the session by setting SessionJobId to nil, and only if the stored session matches your JobId.
- [page](https://devforum.roblox.com/t/session-locking-explained-datastore/846799) **[[data-persistence]]** Implement leases: treat a session older than your autosave interval (e.g. 30 min) as dead to avoid permanently locked data.
- [page](https://devforum.roblox.com/t/session-locking-explained-datastore/846799) **[[data-persistence]]** Use os.time() for session timestamps and comparisons, not tick() or os.clock(); DataStore metadata can also record last update time.
- [page](https://devforum.roblox.com/t/session-locking-explained-datastore/846799) **[[data-persistence]]** Check that loaded data is a table; treat other types as corrupted.
- [page](https://devforum.roblox.com/t/session-locking-explained-datastore/846799) **[[data-persistence]]** Avoid MessagingService for session handoff; delivery can fail and loading/saving data is too critical.
- [page](https://devforum.roblox.com/t/session-locking-explained-datastore/846799) **[[data-persistence]]** Unless you have unique needs, use ProfileStore/ProfileService rather than building your own session locking system.
- [page](https://devforum.roblox.com/t/session-locking-explained-datastore/846799) **[[data-persistence]]** Optionally queue session load/save operations so a save finishes before a rapid rejoin load runs.

## Numbers
- [page](https://devforum.roblox.com/t/session-locking-explained-datastore/846799) GetAsync cache duration: **4 seconds** (GetAsync caches data and may return stale values)
- [page](https://devforum.roblox.com/t/session-locking-explained-datastore/846799) ProfileService dead-session threshold: **30 minutes** (Session considered dead; matches 30-minute autosave interval)
- [page](https://devforum.roblox.com/t/session-locking-explained-datastore/846799) Network error ratio, GetAsync+SetAsync vs UpdateAsync: **2x** (Separate get and set calls prone to twice as many network errors)

## Tools
DataStore UpdateAsync, ProfileService, ProfileStore, DataStore2, MessagingService

## He points to
- Preventing item duplication via trading (DevForum)

## Topics
[[data-persistence]] [[monetisation-other]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
