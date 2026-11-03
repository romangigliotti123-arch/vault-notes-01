---
title: "Using GameAnalytics (Retention and Monetisation) (Ez mode)"
url: https://devforum.roblox.com/t/using-gameanalytics-retention-and-monetisation-ez-mode/41083
creator: Roblox DevForum
official: false
advice_density: medium
date: 2017-06-27
views: 357
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Using GameAnalytics (Retention and Monetisation) (Ez mode)

[Open](https://devforum.roblox.com/t/using-gameanalytics-retention-and-monetisation-ez-mode/41083) | Roblox DevForum | 357 views | 2017-06-27

## Summary
Beginner tutorial (2017) on integrating the GameAnalytics Roblox module: setting up a GameAnalytics account and game, initialising ServerInit/ClientInit, reading Retention, Engagement and Monetisation dashboards, and sending transaction, resource flow and custom events with formatting rules.

## Tips
- [page](https://devforum.roblox.com/t/using-gameanalytics-retention-and-monetisation-ez-mode/41083) **[[analytics-metrics]]** Set up GameAnalytics with ServerInit once on the server and ClientInit once per client, as early as possible after join, to get retention and playtime data.
- [page](https://devforum.roblox.com/t/using-gameanalytics-retention-and-monetisation-ez-mode/41083) **[[analytics-metrics]]** Lower the module's send-interval setting (around line 5) to about 1 while debugging so events appear quickly instead of waiting a minute.
- [page](https://devforum.roblox.com/t/using-gameanalytics-retention-and-monetisation-ez-mode/41083) **[[analytics-metrics]]** Do not rely on GameAnalytics acquisition data for Roblox games; the author says it is inaccurate due to Roblox.
- [page](https://devforum.roblox.com/t/using-gameanalytics-retention-and-monetisation-ez-mode/41083) **[[analytics-metrics]]** Verify a test session in GameAnalytics Realtime; expect processing of about 15 minutes for small games, up to 45 during slowdowns.
- [page](https://devforum.roblox.com/t/using-gameanalytics-retention-and-monetisation-ez-mode/41083) **[[monetisation-other]]** Log every Robux purchase with RecordTransaction(Player, Price, "Category:Specific") using integer Robux prices and no spaces in string arguments.
- [page](https://devforum.roblox.com/t/using-gameanalytics-retention-and-monetisation-ez-mode/41083) **[[monetisation-other]]** Use RecordResource with Source/Sink flow types and consistent currency and item names to track where in-game currency is earned and spent.
- [page](https://devforum.roblox.com/t/using-gameanalytics-retention-and-monetisation-ez-mode/41083) **[[common-mistakes]]** Never expose the GameKey and SecretKey publicly; keep them out of shared or distributed code.
- [page](https://devforum.roblox.com/t/using-gameanalytics-retention-and-monetisation-ez-mode/41083) **[[common-mistakes]]** Call ServerInit only once in the entire game, and ClientInit once per client; repeat calls break event tracking.
- [page](https://devforum.roblox.com/t/using-gameanalytics-retention-and-monetisation-ez-mode/41083) **[[common-mistakes]]** Ensure HTTP service is enabled in the game settings, otherwise GameAnalytics events will not send.
- [page](https://devforum.roblox.com/t/using-gameanalytics-retention-and-monetisation-ez-mode/41083) **[[common-mistakes]]** Do not put spaces in plain-text string arguments to analytics functions; spaces break the event formatting.

## Numbers
- [page](https://devforum.roblox.com/t/using-gameanalytics-retention-and-monetisation-ez-mode/41083) Realtime processing time: **15 min small games; 45 min during slowdowns** (Time before a test visit appears in GameAnalytics Realtime)
- [page](https://devforum.roblox.com/t/using-gameanalytics-retention-and-monetisation-ez-mode/41083) Send interval (debug setting): **around 1** (Module line 5 setting lowered for faster event submission while testing)
- [page](https://devforum.roblox.com/t/using-gameanalytics-retention-and-monetisation-ez-mode/41083) Transaction price unit: **integer Robux** (Price argument to RecordTransaction must be an int in Robux)

## Tools
GameAnalytics, GameAnalytics Roblox AnalyticsModule, GameAnalytics Realtime dashboard, GameAnalytics Collector REST API

## He points to
- GameAnalytics Collector REST API Reference
- GameAnalytics website resource flow examples

## Quotes
- [page](https://devforum.roblox.com/t/using-gameanalytics-retention-and-monetisation-ez-mode/41083) "N.B Because of Roblox, acquisition is not accurate so uhhh, don't use that."
- [page](https://devforum.roblox.com/t/using-gameanalytics-retention-and-monetisation-ez-mode/41083) "Call THIS ONCE IN THE ENTIRE GAME!!!!!!!"

## Topics
[[analytics-metrics]] [[common-mistakes]] [[monetisation-other]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
