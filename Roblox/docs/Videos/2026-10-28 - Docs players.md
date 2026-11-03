---
title: "Docs: players"
url: https://create.roblox.com/docs/players.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: players

[Open](https://create.roblox.com/docs/players.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Official Roblox docs on the Player object: lifecycle events (PlayerAdded, CharacterAdded/Removing, PlayerRemoving), the four player containers (Backpack, StarterGear, PlayerGui, PlayerScripts), gear permissions and safety, and ban tools including device blocking and ban guidelines.

## Tips
- [page](https://create.roblox.com/docs/players) **[[data-persistence]]** Load player data in Players.PlayerAdded and save it in Players.PlayerRemoving, wrapping DataStore calls in pcall and warning on failure.
- [page](https://create.roblox.com/docs/players) **[[client-server-and-remotes]]** Use PlayerScripts for client scripts not tied to character lifecycle (chat, input); server Scripts cannot run inside PlayerScripts.
- [page](https://create.roblox.com/docs/players) **[[combat-and-gameplay-systems]]** Test games after adding gear; gear can include Scripts that let players access restricted map areas or damage others without retaliation.
- [page](https://create.roblox.com/docs/players) **[[ui-ux-design]]** Disable default inventory GUI with StarterGui:SetCoreGuiEnabled in a LocalScript before adding your own inventory UI.
- [page](https://create.roblox.com/docs/players) **[[ui-ux-design]]** Set StarterGui.ResetPlayerGuiOnSpawn deliberately; when true, PlayerGui is cleared and replaced from StarterGui on every respawn.
- [page](https://create.roblox.com/docs/players) **[[combat-and-gameplay-systems]]** Set Players.CharacterAutoLoads to false and call Player:LoadCharacterAsync() when you need manual spawn control; StarterGui won't copy until then.
- [page](https://create.roblox.com/docs/players) **[[age-ratings-moderation-and-tos]]** State game rules clearly where all users can see them, apply them fairly, and ensure rules comply with Community Standards.
- [page](https://create.roblox.com/docs/players) **[[age-ratings-moderation-and-tos]]** Ban messages may point to off-platform contact by brand or platform name, but must not include usernames, handles, or direct links.
- [page](https://create.roblox.com/docs/players) **[[anti-exploit-and-security]]** Use BanAsync with ApplyDeviceBlock true to block the user's desktop device for 24 hours; this does not apply to mobile or console.
- [page](https://create.roblox.com/docs/players) **[[anti-exploit-and-security]]** Note that device blocks do not propagate to other accounts on the device, and calling the unban API immediately lifts the device block.

## Numbers
- [page](https://create.roblox.com/docs/players) Device block duration: **24 hours** (Applied via BanAsync ApplyDeviceBlock, desktop only (Windows and macOS))

## Tools
Players service, Player object, DataStoreService, StarterGui, StarterGear, Creator Hub Bans dashboard, Open Cloud bans and blocks API

## He points to
- Users and scoped user IDs
- In-game tools
- Disable default UI
- Open Cloud bans and blocks

## Topics
[[age-ratings-moderation-and-tos]] [[anti-exploit-and-security]] [[client-server-and-remotes]] [[combat-and-gameplay-systems]] [[data-persistence]] [[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
