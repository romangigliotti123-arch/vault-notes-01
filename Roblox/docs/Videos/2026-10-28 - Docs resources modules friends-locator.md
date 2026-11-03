---
title: "Docs: resources / modules / friends-locator"
url: https://create.roblox.com/docs/resources/modules/friends-locator.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: resources / modules / friends-locator

[Open](https://create.roblox.com/docs/resources/modules/friends-locator.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox developer docs for the FriendsLocator package module: installing it from the Creator Store, testing it in Studio with a multi-client simulation, customizing click behavior, replacing the default locator UI, and the configure/clicked/visibilityChanged API.

## Tips
- [page](https://create.roblox.com/docs/resources/modules/friends-locator) **[[testing-debugging-and-qa]]** Test FriendsLocator in Studio with a multi-client simulation (2 clients); solo playtests show no friends.
- [page](https://create.roblox.com/docs/resources/modules/friends-locator) **[[testing-debugging-and-qa]]** Set showAllPlayers = RunService:IsStudio() so locators display for all players in Studio only, not in published places.
- [page](https://create.roblox.com/docs/resources/modules/friends-locator) **[[optimization-and-streaming]]** If clicking a locator causes streaming pauses under StreamingEnabled, call RequestStreamAroundAsync at the target position in the clicked handler.
- [page](https://create.roblox.com/docs/resources/modules/friends-locator) **[[ui-ux-design]]** To replace the default locator UI, build a disabled ScreenGui with a FriendLocator frame; optionally name children Portrait and DisplayName so the module fills them.
- [page](https://create.roblox.com/docs/resources/modules/friends-locator) **[[social-features-and-virality]]** Set teleportToFriend = false and handle FriendsLocator.clicked yourself to customize what happens when a friend icon is clicked.

## Numbers
- [page](https://create.roblox.com/docs/resources/modules/friends-locator) thresholdDistance default: **100 studs (friends closer than this show no icon)** (FriendsLocator configure default)
- [page](https://create.roblox.com/docs/resources/modules/friends-locator) maxLocators default: **10 icons** (Maximum locator icons shown at once)
- [page](https://create.roblox.com/docs/resources/modules/friends-locator) Multi-client test setup: **2 clients + 1 server (3 Studio instances)** (Multi-client simulation needed for friend testing)

## Tools
FriendsLocator (Creator Store package), Roblox Studio multi-client simulation, RunService:IsStudio()

## He points to
- Creator Store Packages category

## Topics
[[optimization-and-streaming]] [[social-features-and-virality]] [[testing-debugging-and-qa]] [[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
