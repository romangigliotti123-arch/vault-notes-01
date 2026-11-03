---
title: "Docs: players / avatar-context-menu"
url: https://create.roblox.com/docs/players/avatar-context-menu.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: players / avatar-context-menu

[Open](https://create.roblox.com/docs/players/avatar-context-menu.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs page on the Avatar Context Menu (ACM): enabling it via StarterGui:SetCore, opening/closing it for a player, adding and removing default or custom options, and theming its appearance with AvatarContextMenuTheme parameters.

## Tips
- [page](https://create.roblox.com/docs/players/avatar-context-menu) **[[client-server-and-remotes]]** Enable the ACM with StarterGui:SetCore("AvatarContextMenuEnabled", true) in a LocalScript, ideally in StarterPlayerScripts. Use it only where clicking other users has no predefined behavior.
- [page](https://create.roblox.com/docs/players/avatar-context-menu) **[[ui-ux-design]]** Customize ACM look via SetCore("AvatarContextMenuTheme", table) using colors, transparency, Font, and TextScale to match your game's UI.
- [page](https://create.roblox.com/docs/players/avatar-context-menu) **[[combat-and-gameplay-systems]]** Add game-specific actions (e.g. trade, add-to-party) with SetCore("AddAvatarContextMenuOption", {name, BindableEvent}); forward to server via RemoteFunction if needed.
- [page](https://create.roblox.com/docs/players/avatar-context-menu) **[[common-mistakes]]** ACM cannot be edited while open. Re-verify an action is still valid when selected, e.g. both users still in the same area, since options may have been removed.

## Tools
StarterGui:SetCore, StarterGui:GetCore, BindableEvent

## He points to
- Roblox Creator Docs: Avatar Context Menu

## Topics
[[client-server-and-remotes]] [[combat-and-gameplay-systems]] [[common-mistakes]] [[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
