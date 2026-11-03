---
title: "Docs: cloud-services / data-stores / data-stores-manager"
url: https://create.roblox.com/docs/cloud-services/data-stores/data-stores-manager.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: cloud-services / data-stores / data-stores-manager

[Open](https://create.roblox.com/docs/cloud-services/data-stores/data-stores-manager.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Creator Hub documentation for the Data Stores Manager: viewing data stores, keys, versions and storage usage, reverting and comparing versions, and marking data stores or keys for deletion with a restore cooldown.

## Tips
- [page](https://create.roblox.com/docs/cloud-services/data-stores/data-stores-manager) **[[data-persistence]]** Check Total Size vs Storage Limit in the Data Stores Manager Summary; overage populates Est. Monthly Costs, so monitor it before it grows.
- [page](https://create.roblox.com/docs/cloud-services/data-stores/data-stores-manager) **[[data-persistence]]** Keep data stores under 100 per game; above 100, size and key counts are no longer shown in the Data Stores list.
- [page](https://create.roblox.com/docs/cloud-services/data-stores/data-stores-manager) **[[data-persistence]]** Use key prefixes that start with the scope name when searching, so you can filter keys efficiently in the manager.
- [page](https://create.roblox.com/docs/cloud-services/data-stores/data-stores-manager) **[[data-persistence]]** Mark a data store or key for deletion instead of deleting immediately; a cooldown lets you undo it with Restore.
- [page](https://create.roblox.com/docs/cloud-services/data-stores/data-stores-manager) **[[data-persistence]]** Deleting a data store makes it immediately inaccessible; reads and writes to it fail during the deletion schedule.
- [page](https://create.roblox.com/docs/cloud-services/data-stores/data-stores-manager) **[[data-persistence]]** Use version history Compare versions and Revert to recover bad data; reverting writes a new version rather than deleting history.
- [page](https://create.roblox.com/docs/cloud-services/data-stores/data-stores-manager) **[[data-persistence]]** Restore deleted keys via UpdateAsync or UpdateDataStoreEntry (Open Cloud); restore data stores via Restore or UndeleteDataStore.
- [page](https://create.roblox.com/docs/cloud-services/data-stores/data-stores-manager) **[[anti-exploit-and-security]]** Grant group members only the minimum Data Stores Manager permission needed (view, delete keys, delete stores, or full access).

## Numbers
- [page](https://create.roblox.com/docs/cloud-services/data-stores/data-stores-manager) Data stores per game before size/key counts unavailable: **100+** (Above 100 data stores, Data Stores list omits size and key counts)
- [page](https://create.roblox.com/docs/cloud-services/data-stores/data-stores-manager) Total Size: **Sum of bytes of all existing keys** (Compared against Storage Limit, based on game lifetime user count)

## Tools
Data Stores Manager (Creator Hub), Open Cloud API, Engine API

## He points to
- Limits (Roblox docs)
- Best practices (Roblox docs)

## Topics
[[anti-exploit-and-security]] [[data-persistence]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
