---
title: "Docs: players / avatar-inspect-menu"
url: https://create.roblox.com/docs/players/avatar-inspect-menu.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: players / avatar-inspect-menu

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/players/avatar-inspect-menu.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on the Avatar Inspect Menu. Explains the three access points (Players tab View button, clicking name in player list, Avatar Context Menu opt-in), and how to customize it: inspect current in-game outfit via HumanoidDescription, or inspect any UserId via InspectPlayerFromUserId. Covers Avatar Editor Service for catalog access.

## Tips
- [page](https://create.roblox.com/docs/players/avatar-inspect-menu) **[[ui-ux-design]]** Disable the default profile-based inspect menu with GuiService:SetInspectMenuEnabled(false) when the profile outfit may not match the player's current in-game appearance.
- [page](https://create.roblox.com/docs/players/avatar-inspect-menu) **[[ui-ux-design]]** Use GuiService:InspectPlayerFromHumanoidDescription with humanoid:GetAppliedDescription() to show a player's currently equipped items rather than their saved Roblox profile outfit.
- [page](https://create.roblox.com/docs/players/avatar-inspect-menu) **[[social-features-and-virality]]** Use GuiService:InspectPlayerFromUserId(userId) to open inspect for players who are not in the current server, wrapping Players:GetUserIdFromNameAsync in pcall.
- [page](https://create.roblox.com/docs/players/avatar-inspect-menu) **[[client-server-and-remotes]]** Call GuiService inspect functions from a LocalScript, since they open client-side UI for the local player.

## Tools
GuiService, Players:GetUserIdFromNameAsync, Avatar Editor Service

## Topics
[[client-server-and-remotes]] [[social-features-and-virality]] [[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
