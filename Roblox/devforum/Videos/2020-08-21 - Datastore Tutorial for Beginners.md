---
title: "Datastore Tutorial for Beginners"
url: https://devforum.roblox.com/t/datastore-tutorial-for-beginners/733973
creator: Roblox DevForum
official: false
advice_density: medium
date: 2020-08-21
views: 932
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Datastore Tutorial for Beginners

[Open](https://devforum.roblox.com/t/datastore-tutorial-for-beginners/733973) | Roblox DevForum | 932 views | 2020-08-21

## Summary
Beginner tutorial on Roblox DataStoreService: enabling API services, saving a per-player table keyed by UserId with SetAsync inside pcall, loading with GetAsync on PlayerAdded, saving on PlayerRemoving, and using BindToClose so Studio stop and server shutdowns still save. Also covers manually editing saved data with a plugin.

## Tips
- [page](https://devforum.roblox.com/t/datastore-tutorial-for-beginners/733973) **[[data-persistence]]** Enable 'Studio access to API services' in Game Settings > Security before using DataStoreService, or saves will fail in Studio.
- [page](https://devforum.roblox.com/t/datastore-tutorial-for-beginners/733973) **[[data-persistence]]** Wrap GetAsync and SetAsync in pcall so an error does not stop the script; check success and warn(err) on failure.
- [page](https://devforum.roblox.com/t/datastore-tutorial-for-beginners/733973) **[[data-persistence]]** Key datastore entries by player.UserId; new players return nil from GetAsync, so fall back to default values.
- [page](https://devforum.roblox.com/t/datastore-tutorial-for-beginners/733973) **[[data-persistence]]** Save on PlayerRemoving and also in game:BindToClose, since Studio stop and server shutdowns skip the time needed to save otherwise.
- [page](https://devforum.roblox.com/t/datastore-tutorial-for-beginners/733973) **[[data-persistence]]** Changing the DataStore name creates a brand-new empty store; keep the name fixed once players have data.
- [page](https://devforum.roblox.com/t/datastore-tutorial-for-beginners/733973) **[[data-persistence]]** Store values as an array table (e.g. {Money, Coins}) and read by index; reordering indices later breaks existing saves.
- [page](https://devforum.roblox.com/t/datastore-tutorial-for-beginners/733973) **[[scripting-and-performance]]** Put datastore code in a server Script, not a LocalScript.

## Tools
DataStoreService, pcall, BindToClose, Datastore editing plugin (manual edit by UserId)

## Topics
[[data-persistence]] [[scripting-and-performance]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
