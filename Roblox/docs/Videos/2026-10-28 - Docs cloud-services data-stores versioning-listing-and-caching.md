---
title: "Docs: cloud-services / data-stores / versioning-listing-and-caching"
url: https://create.roblox.com/docs/cloud-services/data-stores/versioning-listing-and-caching.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: cloud-services / data-stores / versioning-listing-and-caching

[Open](https://create.roblox.com/docs/cloud-services/data-stores/versioning-listing-and-caching.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs on data store versioning (versions kept per first write each UTC hour, 30-day expiry, ListVersionsAsync/GetVersionAsync/RemoveVersionAsync, daily snapshots before risky updates), key listing by prefix, scopes and AllScopes, and caching behaviour (4-second GetAsync cache, UseCache=false for verification reads), plus serialization rules.

## Tips
- [page](https://create.roblox.com/docs/cloud-services/data-stores/versioning-listing-and-caching) **[[data-persistence]]** Take a Snapshot Data Stores Open Cloud snapshot once a day and before publishing any update that changes data storage logic, so corrupted writes can be rolled back.
- [page](https://create.roblox.com/docs/cloud-services/data-stores/versioning-listing-and-caching) **[[data-persistence]]** Use ListVersionsAsync and GetVersionAsync to restore a player's data to the version closest to a reported time, then SetAsync it back with metadata.
- [page](https://create.roblox.com/docs/cloud-services/data-stores/versioning-listing-and-caching) **[[data-persistence]]** Don't rely on scopes for new games; use key prefixes with ListKeysAsync to organise keys instead.
- [page](https://create.roblox.com/docs/cloud-services/data-stores/versioning-listing-and-caching) **[[data-persistence]]** Verify writes with GetAsync using DataStoreGetOptions.UseCache = false, since the default 4-second cache can return stale data.
- [page](https://create.roblox.com/docs/cloud-services/data-stores/versioning-listing-and-caching) **[[scripting-and-performance]]** Keep GetAsync caching on by default for reads; cached reads don't count toward server and throughput limits, but bypassing it always does.
- [page](https://create.roblox.com/docs/cloud-services/data-stores/versioning-listing-and-caching) **[[data-persistence]]** Don't store inf, -inf or nan in data stores; they break JSON and come back as tagged objects via Open Cloud.
- [page](https://create.roblox.com/docs/cloud-services/data-stores/versioning-listing-and-caching) **[[common-mistakes]]** Don't assume a data store instance's cache is shared; separate instances (different scope or AllScopes) each keep their own cache and can diverge.
- [page](https://create.roblox.com/docs/cloud-services/data-stores/versioning-listing-and-caching) **[[common-mistakes]]** Unsupported types may save silently as nil; debug with HttpService:JSONEncode to preview what gets stored.
- [page](https://create.roblox.com/docs/cloud-services/data-stores/versioning-listing-and-caching) **[[data-persistence]]** When a write errors, decide between retry, refund or other correction based on backend state, not cached state.
- [page](https://create.roblox.com/docs/cloud-services/data-stores/versioning-listing-and-caching) **[[data-persistence]]** Remember RemoveVersionAsync leaves a tombstone; older versions remain retrievable via ListVersionsAsync and GetVersionAsync.

## Numbers
- [page](https://create.roblox.com/docs/cloud-services/data-stores/versioning-listing-and-caching) Versioned backup creation: **first write to each key per UTC hour** (Later same-hour writes overwrite previous data)
- [page](https://create.roblox.com/docs/cloud-services/data-stores/versioning-listing-and-caching) Versioned backup expiry: **30 days after overwritten** (Latest version never expires)
- [page](https://create.roblox.com/docs/cloud-services/data-stores/versioning-listing-and-caching) GetAsync default cache duration: **4 seconds** (Cached reads don't count toward server or throughput limits)
- [page](https://create.roblox.com/docs/cloud-services/data-stores/versioning-listing-and-caching) Snapshot frequency: **once per day** (Snapshot Data Stores Open Cloud API, taken before risky updates)

## Tools
DataStoreService, ListVersionsAsync, GetVersionAsync, RemoveVersionAsync, Snapshot Data Stores Open Cloud API, HttpService.JSONEncode

## He points to
- Snapshot Data Stores Open Cloud API
- Non-finite numbers (Open Cloud docs)

## Topics
[[common-mistakes]] [[data-persistence]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
