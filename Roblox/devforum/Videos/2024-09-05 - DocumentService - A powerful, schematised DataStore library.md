---
title: "DocumentService - A powerful, schematised DataStore library"
url: https://devforum.roblox.com/t/documentservice-a-powerful-schematised-datastore-library/3146934
creator: Roblox DevForum
official: false
advice_density: medium
date: 2024-09-05
views: 111
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# DocumentService - A powerful, schematised DataStore library

[Open](https://devforum.roblox.com/t/documentservice-a-powerful-schematised-datastore-library/3146934) | Roblox DevForum | 111 views | 2024-09-05

## Summary
Describes DocumentService, an open-source strictly typed Luau library for saving Roblox DataStore data with optional session locking, migrations, validation, and Result-based error handling. Compares it with ProfileService, Lapis and DataKeep, and covers installation and migration from existing data.

## Tips
- [page](https://devforum.roblox.com/t/documentservice-a-powerful-schematised-datastore-library/3146934) **[[data-persistence]]** Use a schema-validated data library so unsavable data errors before publishing rather than failing silently in production.
- [page](https://devforum.roblox.com/t/documentservice-a-powerful-schematised-datastore-library/3146934) **[[data-persistence]]** Use migrations to change data format over time and mark changes as not backwards compatible, instead of only adding new fields.
- [page](https://devforum.roblox.com/t/documentservice-a-powerful-schematised-datastore-library/3146934) **[[data-persistence]]** Validate data both when saving and when loading to catch manual edits or corruption that would otherwise cause odd side effects.
- [page](https://devforum.roblox.com/t/documentservice-a-powerful-schematised-datastore-library/3146934) **[[data-persistence]]** Implement GlobalUpdates by checking if the player is in the current server and using IsOpenAvailable; otherwise update via MessagingService from the server holding the data.
- [page](https://devforum.roblox.com/t/documentservice-a-powerful-schematised-datastore-library/3146934) **[[data-persistence]]** Use a non-session-locked document for shared data such as groups or houses that need multi-server editing.
- [page](https://devforum.roblox.com/t/documentservice-a-powerful-schematised-datastore-library/3146934) **[[scripting-and-performance]]** Use immutable cached data and autosaves to avoid bugs from commits happening too early or accidental mutations.
- [page](https://devforum.roblox.com/t/documentservice-a-powerful-schematised-datastore-library/3146934) **[[scripting-and-performance]]** Inject a MockDataStore for testing data code without hitting live DataStores.
- [page](https://devforum.roblox.com/t/documentservice-a-powerful-schematised-datastore-library/3146934) **[[data-persistence]]** When migrating an existing game, open documents on keys that already hold data; the library will reuse and reformat existing keys.
- [page](https://devforum.roblox.com/t/documentservice-a-powerful-schematised-datastore-library/3146934) **[[code-architecture-and-frameworks]]** Prefer libraries with no dependencies such as Promise so you can choose your own abstractions.

## Numbers
- [page](https://devforum.roblox.com/t/documentservice-a-powerful-schematised-datastore-library/3146934) ProfileService request wait time: **7 seconds between requests (criticised as outdated)** (Claimed by the author as an unnecessary delay in ProfileService)

## Tools
DocumentService, Wally, MockDataStore, ProfileService, Lapis, DataKeep, MessagingService

## He points to
- Lapis by @nezuo
- DataKeep
- Roblox OSS Discord projects thread
- kineticwallet MockDataStore

## Quotes
- [page](https://devforum.roblox.com/t/documentservice-a-powerful-schematised-datastore-library/3146934) "ProfileService only works with player data, DocumentService works for almost every use case."

## Topics
[[code-architecture-and-frameworks]] [[data-persistence]] [[scripting-and-performance]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
