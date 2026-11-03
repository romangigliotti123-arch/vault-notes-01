---
title: "Docs: ui / text-filtering"
url: https://create.roblox.com/docs/ui/text-filtering.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: ui / text-filtering

[Open](https://create.roblox.com/docs/ui/text-filtering.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on text filtering. Explains that developers must filter any displayed user-generated or external text, which Roblox enforces (games without filtering get removed). Covers TextService:FilterStringAsync and the broadcast/user result methods, with client-to-server TextBox example and warning against per-character filtering.

## Tips
- [page](https://create.roblox.com/docs/ui/text-filtering) **[[common-mistakes]]** Games that display user text without filtering can be removed by Roblox until filtering is added.
- [page](https://create.roblox.com/docs/ui/text-filtering) **[[anti-exploit-and-security]]** Filter text on the server with TextService:FilterStringAsync, not on the client, before showing it to others.
- [page](https://create.roblox.com/docs/ui/text-filtering) **[[client-server-and-remotes]]** Send submitted TextBox input to the server via RemoteEvent on FocusLost with enterPressed, then filter there.
- [page](https://create.roblox.com/docs/ui/text-filtering) **[[common-mistakes]]** Do not filter per character while typing; filtered output only shows to the typing user. Filter after submit.
- [page](https://create.roblox.com/docs/ui/text-filtering) **[[scripting-and-performance]]** Wrap FilterStringAsync and GetNonChatStringForBroadcastAsync in pcall and handle failures.
- [page](https://create.roblox.com/docs/ui/text-filtering) **[[ui-ux-design]]** Use GetNonChatStringForUserAsync when showing filtered text to one specific user, since it depends on that user's age.
- [page](https://create.roblox.com/docs/ui/text-filtering) **[[data-persistence]]** Filter text loaded from DataStores (e.g. pet names) before displaying, since stored text may contain inappropriate words.
- [page](https://create.roblox.com/docs/ui/text-filtering) **[[anti-exploit-and-security]]** Filter text from external web servers and random-character generators too, since you don't control their content.

## Tools
TextService, TextFilterResult, RemoteEvent, TextBox

## Topics
[[anti-exploit-and-security]] [[client-server-and-remotes]] [[common-mistakes]] [[data-persistence]] [[scripting-and-performance]] [[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
