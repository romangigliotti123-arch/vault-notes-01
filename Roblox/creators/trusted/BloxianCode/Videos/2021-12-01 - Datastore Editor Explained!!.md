---
title: "Datastore Editor Explained!!"
url: https://youtu.be/Z1OjuaBCAXU
creator: BloxianCode
official: false
advice_density: medium
date: 2021-12-01
views: 19002
transcript: auto-captions
confidence: high
tags: [roblox, bloxiancode, youtube-learn]
creator_trust: TRUSTED
creator_score: 7.7
---

> [!note] Trust: TRUSTED (credibility audit score 7.7): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Datastore Editor Explained!!

[Watch](https://youtu.be/Z1OjuaBCAXU) | BloxianCode | 19,002 views | 2021-12-01

## Summary
Tutorial on using the DataStore Editor plugin (by Sligny) in Roblox Studio: enabling API access, finding the DataStore name and player user-ID keys, viewing/editing/saving values (strings, numbers, booleans, tables), import/export, deleting keys, and OrderedDataStore basics.

## Tips
- [0:00](https://youtu.be/Z1OjuaBCAXU?t=0) **[[data-persistence]]** Enable Game Settings > Security > 'Enable Studio Access to API Services' before using DataStores in Studio, then save.
- [0:00](https://youtu.be/Z1OjuaBCAXU?t=0) **[[data-persistence]]** Publish the game or set it to Roblox so DataStore access works as expected during testing.
- [2:42](https://youtu.be/Z1OjuaBCAXU?t=162) **[[data-persistence]]** Use player UserId as the DataStore key so each player's data is unique.
- [6:10](https://youtu.be/Z1OjuaBCAXU?t=370) **[[data-persistence]]** Always click the save icon in DataStore Editor after editing; otherwise changes are not written and errors can occur.
- [8:13](https://youtu.be/Z1OjuaBCAXU?t=493) **[[data-persistence]]** Deleting a key in DataStore Editor cannot be undone; confirm carefully before deleting.
- [8:55](https://youtu.be/Z1OjuaBCAXU?t=535) **[[testing-debugging-and-qa]]** Edit a player's saved value in the plugin, then play-test to confirm the in-game value matches the edit and persists after leaving.
- [11:38](https://youtu.be/Z1OjuaBCAXU?t=698) **[[data-persistence]]** OrderedDataStores store ranked lists (e.g. leaderboards); the editor can sort them ascending or descending.

## Numbers
- [8:55](https://youtu.be/Z1OjuaBCAXU?t=535) Test edit example: **Cash changed from 30 to 25, then 55 after earning** (Demonstration values in Studio play-test)

## Tools
DataStore Editor plugin (by Sligny), Roblox Studio Output/Command bar

## He points to
- Sligny (DataStore Editor plugin author)

## Topics
[[data-persistence]] [[testing-debugging-and-qa]]

Back to [[BloxianCode - How to make successful Roblox games]]
