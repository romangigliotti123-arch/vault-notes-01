---
title: "Prompt players to join Communities from in-experience!"
url: https://devforum.roblox.com/t/prompt-players-to-join-communities-from-in-experience/4135599
creator: Roblox DevForum
official: true
advice_density: medium
date: 2025-12-08
views: 965
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Prompt players to join Communities from in-experience!

[Open](https://devforum.roblox.com/t/prompt-players-to-join-communities-from-in-experience/4135599) | Roblox DevForum | 965 views | 2025-12-08

## Summary
Roblox staff announcement of GroupService:PromptJoinAsync, a client-only API that shows a native prompt for players to join a Community without leaving the experience. Covers return values, pcall error handling, reward-abuse caveats, the 60-second IsInGroup cache, and combining with Open Cloud for join-request and role management.

## Tips
- [page](https://devforum.roblox.com/t/prompt-players-to-join-communities-from-in-experience/4135599) **[[community-and-discord]]** Prompt players to join your Community in-experience via GroupService:PromptJoinAsync(groupId) to avoid sending them to a browser.
- [page](https://devforum.roblox.com/t/prompt-players-to-join-communities-from-in-experience/4135599) **[[anti-exploit-and-security]]** Don't attach high rewards to joining a Community; players can join and leave freely to farm join rewards.
- [page](https://devforum.roblox.com/t/prompt-players-to-join-communities-from-in-experience/4135599) **[[client-server-and-remotes]]** Player:IsInGroup/GetRoleInGroup/GetRankInGroup cache for 60s on server and other clients; only the joining client's cache is cleared.
- [page](https://devforum.roblox.com/t/prompt-players-to-join-communities-from-in-experience/4135599) **[[client-server-and-remotes]]** After the prompt, fire a client-to-server signal, then verify membership with GroupService:GetGroupsAsync for an uncached result.
- [page](https://devforum.roblox.com/t/prompt-players-to-join-communities-from-in-experience/4135599) **[[client-server-and-remotes]]** Wrap GroupService:PromptJoinAsync in pcall; the prompt can fail from invalid groupId or network issues.
- [page](https://devforum.roblox.com/t/prompt-players-to-join-communities-from-in-experience/4135599) **[[community-and-discord]]** Manual Approval communities produce a JoinRequestPending result; process requests server-side via Open Cloud through HttpService.
- [page](https://devforum.roblox.com/t/prompt-players-to-join-communities-from-in-experience/4135599) **[[community-and-discord]]** Join Requirements (Verification Level, Account Age) are enforced and shown in the prompt automatically.

## Numbers
- [page](https://devforum.roblox.com/t/prompt-players-to-join-communities-from-in-experience/4135599) Group membership cache duration: **60 seconds (Player:IsInGroup, GetRoleInGroup, GetRankInGroup)**

## Tools
GroupService:PromptJoinAsync, GroupService:GetGroupsAsync, Player:IsInGroup, Open Cloud via HttpService

## He points to
- Official docs on implementing community prompts (Roblox Creator Docs)

## Topics
[[anti-exploit-and-security]] [[client-server-and-remotes]] [[community-and-discord]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
