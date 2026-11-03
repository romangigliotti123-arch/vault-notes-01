---
title: "Introducing the Ban API and Alt Account Detection"
url: https://devforum.roblox.com/t/introducing-the-ban-api-and-alt-account-detection/3039740
creator: Roblox DevForum
official: true
advice_density: medium
date: 2024-06-25
views: 3805
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Introducing the Ban API and Alt Account Detection

[Open](https://devforum.roblox.com/t/introducing-the-ban-api-and-alt-account-detection/3039740) | Roblox DevForum | 3,805 views | 2024-06-25

## Summary
Roblox staff announcement of the Ban API (launched June 2024) with real-time alt account detection, CreatorHub Ban Management Dashboard (Aug 2024), and a Jan 2025 clarification that the dashboard only shows universe-level bans. Covers ban limits, alt detection defaults, unban behaviour, subscription cancellation after 14-day bans, and the Kick API comparison.

## Tips
- [page](https://devforum.roblox.com/t/introducing-the-ban-api-and-alt-account-detection/3039740) **[[community-and-discord]]** Build your own appeals process; Roblox won't handle appeals for API bans. You decide whether to unban when a player appeals, and customer support redirects those contacts to you.
- [page](https://devforum.roblox.com/t/introducing-the-ban-api-and-alt-account-detection/3039740) **[[common-mistakes]]** Write experience rules that follow Community Standards and apply them fairly. Rules excluding users by protected traits violate policy, and arbitrary targeting is not allowed.
- [page](https://devforum.roblox.com/t/introducing-the-ban-api-and-alt-account-detection/3039740) **[[anti-exploit-and-security]]** Use Ban API instead of Kick API for moderation; Kick is only temporary and has no ban history, while Ban API supports durations, alt detection and history.
- [page](https://devforum.roblox.com/t/introducing-the-ban-api-and-alt-account-detection/3039740) **[[anti-exploit-and-security]]** Keep suspected alt detection on (default) to auto-ban alts of banned users in real time, or disable it if false positives are a concern.
- [page](https://devforum.roblox.com/t/introducing-the-ban-api-and-alt-account-detection/3039740) **[[anti-exploit-and-security]]** Ban by user ID, not username. Unbanning an original account also unbans its suspected alts; unbanning an alt only unbans that alt.
- [page](https://devforum.roblox.com/t/introducing-the-ban-api-and-alt-account-detection/3039740) **[[anti-exploit-and-security]]** Ban up to 50 user IDs per batch in CreatorHub. Set permanent or custom duration and write both public (shown to player) and private reasons.
- [page](https://devforum.roblox.com/t/introducing-the-ban-api-and-alt-account-detection/3039740) **[[data-persistence]]** Keep your own ban database if you need cross-experience or bulk lists. The API only exposes per-experience data and per-user moderation history.
- [page](https://devforum.roblox.com/t/introducing-the-ban-api-and-alt-account-detection/3039740) **[[monetisation-other]]** Permanent or over-14-day bans auto-cancel the player's experience subscription without refund. Factor this into subscription-based offers.
- [page](https://devforum.roblox.com/t/introducing-the-ban-api-and-alt-account-detection/3039740) **[[roblox-platform-changes]]** Jan 2025: CreatorHub dashboard shows only universe-level bans. Query place-level bans with ListUserRestrictions via the place-level OpenCloud resource paths.

## Numbers
- [page](https://devforum.roblox.com/t/introducing-the-ban-api-and-alt-account-detection/3039740) Max bans per batch: **50 user IDs at a time** (CreatorHub Ban Management Dashboard limit)
- [page](https://devforum.roblox.com/t/introducing-the-ban-api-and-alt-account-detection/3039740) Subscription auto-cancel threshold: **Ban longer than 14 days** (Experience subscription, no refund)
- [page](https://devforum.roblox.com/t/introducing-the-ban-api-and-alt-account-detection/3039740) Alt detection default: **On by default** (Suspected alt auto-ban setting)

## Tools
Ban API (Engine: Players:BanAsync), OpenCloud UpdateUserRestriction / ListUserRestrictions, CreatorHub Ban Management Dashboard

## He points to
- Engine Ban API docs
- OpenCloud Ban API docs
- Ban API Guidelines

## Topics
[[anti-exploit-and-security]] [[common-mistakes]] [[community-and-discord]] [[data-persistence]] [[monetisation-other]] [[roblox-platform-changes]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
