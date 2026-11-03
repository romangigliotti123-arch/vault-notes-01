---
title: "Analytics: Spot Performance Issues Before Players Do | RDC 2026"
url: https://youtu.be/bVU69VImiEc
creator: Roblox
official: true
advice_density: medium
date: 2026-10-12
views: 1465
transcript: auto-captions
confidence: high
tags: [roblox, mustwatch, youtube-learn]
---

# Analytics: Spot Performance Issues Before Players Do | RDC 2026

[Watch](https://youtu.be/bVU69VImiEc) | MustWatch | 1,465 views | 2026-10-12

## Summary
Roblox RDC 2026 talk on creator analytics. Roblox PM AJ, Doobig Studios CTO Yousef Ibraham, and Roblox engineer Andrew Grim cover new alerts, rebuilt error reports, experiments with harm detection, custom dashboards with calculated metrics, and Doobig's in-house tools (live server lists, microprofiler capture, log requests). Roadmap includes a session browser and analytics agent.

## Tips
- [1:55](https://youtu.be/bVU69VImiEc?t=115) **[[analytics-metrics]]** Set real-time alerts on client frame rate, crash rate and play time with static thresholds or period-over-period change detection, posted to your team's chat channel.
- [3:17](https://youtu.be/bVU69VImiEc?t=197) **[[analytics-metrics]]** After each release, check error reports filtered to the newest version; every error shows first-seen timestamp and version to identify what the update introduced.
- [3:58](https://youtu.be/bVU69VImiEc?t=238) **[[development-process-and-speed]]** Wrap risky updates in a config and roll them out as an experiment; watch key metrics and roll back with one action if harm thresholds trip.
- [4:39](https://youtu.be/bVU69VImiEc?t=279) **[[analytics-metrics]]** Test risky changes on a small segment (e.g. new players only) and compare session length and D1 retention against other users before a full launch.
- [6:01](https://youtu.be/bVU69VImiEc?t=361) **[[analytics-metrics]]** Use calculated metrics across multiple custom events (e.g. wins divided by match starts for win rate) and save them to shared custom dashboards.
- [6:41](https://youtu.be/bVU69VImiEc?t=401) **[[analytics-metrics]]** Revisit custom dashboards periodically; metrics tracked six months ago may no longer answer current questions as audience and game change.
- [8:26](https://youtu.be/bVU69VImiEc?t=506) **[[scripting-and-performance]]** Attach version number, device group and custom game-state metadata to alerts so the team can start investigating immediately.
- [9:09](https://youtu.be/bVU69VImiEc?t=549) **[[scripting-and-performance]]** Event-heavy live events can act as a mobile stress test; monitor client FPS and crash alerts during visually intense events.
- [10:31](https://youtu.be/bVU69VImiEc?t=631) **[[scripting-and-performance]]** When investigating FPS drops, pick affected phone or tablet sessions rather than healthy desktop sessions, so you profile the case that actually reproduces the issue.
- [11:16](https://youtu.be/bVU69VImiEc?t=676) **[[scripting-and-performance]]** Capture microprofiler dumps from live affected clients during the issue and diff against a pre-event dump to find the specific regressing task (here, particle emitters).
- [13:21](https://youtu.be/bVU69VImiEc?t=801) **[[scripting-and-performance]]** Keep server and client debug logs with version and game-state context; pulling logs from live servers avoids joining them yourself or asking players for dumps.
- [17:53](https://youtu.be/bVU69VImiEc?t=1073) **[[analytics-metrics]]** When a metric drops, slice by device tier until you find the smallest affected segment; a drop only on low-memory Android points to a resource problem, not game design.
- [18:33](https://youtu.be/bVU69VImiEc?t=1113) **[[analytics-metrics]]** Check timing first: a drop that starts exactly when you publish is likely tied to that update, so inspect that update's diff.
- [19:15](https://youtu.be/bVU69VImiEc?t=1155) **[[analytics-metrics]]** Do not trust total aggregate numbers alone; slice and dice to narrow down the cause of a metric change.
- [15:27](https://youtu.be/bVU69VImiEc?t=927) **[[development-process-and-speed]]** Prefer building on Roblox's native analytics stack over rebuilding basics; build custom tools only where your game needs them.
- [25:08](https://youtu.be/bVU69VImiEc?t=1508) **[[playtesting-and-feedback]]** For QA with a small tester group, start with the error report filtered to the latest version, since any error in a small test session is likely a real bug.

## Numbers
- [3:58](https://youtu.be/bVU69VImiEc?t=238) Fast config rollback speed: **90% faster across all servers** (Roblox claim for config rollback landing across servers without kicking players)
- [6:01](https://youtu.be/bVU69VImiEc?t=361) Harm detection check interval: **every 5 minutes** (Early harm detection (coming soon) checks experiments for critical metric thresholds)

## Games
- **Steal a Brainrot**: Live-event visual effects stacked during admin abuse caused mobile FPS drops; alerts plus microprofiler dumps pinpointed particle emitters as the bottleneck.
- **Blue Lock Rivals**: Custom dashboards tracking match time and win rate by character style let the team check whether an update shifted balance.

## Tools
Roblox real-time performance alerts, Roblox error reports (version filter), Roblox experiments with harm detection, Roblox custom dashboards and calculated metrics, Roblox microprofiler API, Roblox Open Cloud APIs, Roblox game server logs, Doobig in-house analytics SDK, alerts, server list, log requests, A/B pipeline, AI query assistant

## He points to
- Roblox RDC 2026 keynote (multiplayer testing tools, NPCs)
- New player data APIs with schemas (announced at RDC 2026)

## Quotes
- [1:23](https://youtu.be/bVU69VImiEc?t=83) "The best teams on Roblox don't always wait for us. When they see a problem, they solve it. Then they tell us about it."
- [17:53](https://youtu.be/bVU69VImiEc?t=1073) "Players aren't leaving because they disliked the update from Thursday. They're leaving because something got worse on their devices with the least headroom."
- [15:27](https://youtu.be/bVU69VImiEc?t=927) "We always prefer to build on top of Roblox's analytic stack instead of rebuilding the basics ourselves."

## On screen
Insights panel showing funnel steps and D1 retention for Android players; performance dashboard with average playtime, client CPU time and client frame rate with alert annotations; Doobig-style alert and dashboard screens.

## Topics
[[analytics-metrics]] [[development-process-and-speed]] [[playtesting-and-feedback]] [[scripting-and-performance]]

Back to [[MustWatch - How to make successful Roblox games]]
