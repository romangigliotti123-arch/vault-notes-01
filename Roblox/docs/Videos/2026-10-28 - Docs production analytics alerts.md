---
title: "Docs: production / analytics / alerts"
url: https://create.roblox.com/docs/production/analytics/alerts.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: production / analytics / alerts

[Open](https://create.roblox.com/docs/production/analytics/alerts.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs on Alerts: configuring metric-based and period-over-period alert rules on experience performance and data store metrics, delivering them via experience webhooks (PagerDuty, Slack, Discord), permissions, severity levels, duration settings, and best practices for avoiding false alarms.

## Tips
- [page](https://create.roblox.com/docs/production/analytics/alerts) **[[analytics-metrics]]** Establish a baseline first: review analytics charts over the last 7 to 14 days before setting thresholds, so normal fluctuation does not trigger false alarms.
- [page](https://create.roblox.com/docs/production/analytics/alerts) **[[analytics-metrics]]** Set alert thresholds above normal levels. Example: if normal crash rate is about 1.2%, set the alert at 2.5% or 3%.
- [page](https://create.roblox.com/docs/production/analytics/alerts) **[[analytics-metrics]]** Use a duration of 5 (not 1) for volatile metrics like session time; sudden player influxes or asset loads can cause temporary spikes.
- [page](https://create.roblox.com/docs/production/analytics/alerts) **[[analytics-metrics]]** Use the Breakdown feature in one alert (e.g. by platform: Android, iOS, PC) instead of separate alerts per platform; the payload shows where the issue occurs.
- [page](https://create.roblox.com/docs/production/analytics/alerts) **[[analytics-metrics]]** Name alerts with a structured formula like 'metric - context' (e.g. 'High client crash rate - mobile') so issues can be triaged at a glance.
- [page](https://create.roblox.com/docs/production/analytics/alerts) **[[updates-live-ops]]** Create a crash-rate alert (e.g. client crash rate above 5%, 5-minute duration, critical severity) before pushing an update to catch performance regressions quickly.
- [page](https://create.roblox.com/docs/production/analytics/alerts) **[[updates-live-ops]]** Add an experience-level webhook (PagerDuty, Discord, Slack) so the team is notified immediately with metric value and dashboard link when an alert fires.
- [page](https://create.roblox.com/docs/production/analytics/alerts) **[[common-mistakes]]** Avoid setting alert duration to 1 on volatile metrics; it fires on a single data point and creates noise.
- [page](https://create.roblox.com/docs/production/analytics/alerts) **[[development-process-and-speed]]** Use the Create alert shortcut from a Performance dashboard chart's overflow menu to pre-fill the metric and filters.
- [page](https://create.roblox.com/docs/production/analytics/alerts) **[[scripting-and-performance]]** Monitor client memory, unexpected out-of-memory exits, server CPU time, and frame rate with alerts to catch performance problems early.

## Numbers
- [page](https://create.roblox.com/docs/production/analytics/alerts) Alerts eligibility: **100+ daily active users** (Required for performance metrics alerts)
- [page](https://create.roblox.com/docs/production/analytics/alerts) Max alerts per experience: **20** (Creating alerts requires Create and configure alerts permission)
- [page](https://create.roblox.com/docs/production/analytics/alerts) Duration range: **1-10 consecutive evaluations; minimum 5 minutes for minute granularity** (How many consecutive times condition must be met before firing)
- [page](https://create.roblox.com/docs/production/analytics/alerts) Example critical crash alert: **Client crash rate above 5% for 5 minutes** (Typical regression-catching alert from docs example)
- [page](https://create.roblox.com/docs/production/analytics/alerts) Baseline example threshold: **Normal crash rate 1.2% -> alert at 2.5% or 3%** (Docs example for leaving room for natural fluctuation)
- [page](https://create.roblox.com/docs/production/analytics/alerts) Time granularity options: **minute, half hour, hourly, daily** (How often a metric is evaluated)

## Tools
Roblox Creator Dashboard Alerts, Experience webhooks, PagerDuty, Discord webhooks, Slack webhooks

## He points to
- Roblox Creator Dashboard Performance dashboard
- Roblox experience Permissions page

## Topics
[[analytics-metrics]] [[common-mistakes]] [[development-process-and-speed]] [[scripting-and-performance]] [[updates-live-ops]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
