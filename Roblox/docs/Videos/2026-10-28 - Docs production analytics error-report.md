---
title: "Docs: production / analytics / error-report"
url: https://create.roblox.com/docs/production/analytics/error-report.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: production / analytics / error-report

[Open](https://create.roblox.com/docs/production/analytics/error-report.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox Creator Dashboard docs on Error Report: viewing server/client errors and warnings, filters, troubleshooting table and stack traces, custom ignore/group rules with regex constraints, and tracking limits (500 unique errors/warnings, 6-hour reset).

## Tips
- [page](https://create.roblox.com/docs/production/analytics/error-report) **[[analytics-metrics]]** Check the Error Report before and after each update to catch regressions early.
- [page](https://create.roblox.com/docs/production/analytics/error-report) **[[analytics-metrics]]** When a spike appears on the chart, use the error table to troubleshoot, then expand rows for stack traces.
- [page](https://create.roblox.com/docs/production/analytics/error-report) **[[analytics-metrics]]** Use the 'New errors since' filter to isolate errors introduced by your most recent version.
- [page](https://create.roblox.com/docs/production/analytics/error-report) **[[analytics-metrics]]** Use platform and OS breakdowns to see whether an error is specific to Desktop, Mobile, Console, or a given OS.
- [page](https://create.roblox.com/docs/production/analytics/error-report) **[[scripting-and-performance]]** Remove unique identifiers (user IDs, coordinates, timestamps) from error messages so repeats consolidate into one entry with a higher count.
- [page](https://create.roblox.com/docs/production/analytics/error-report) **[[scripting-and-performance]]** Use Ignore rules only for permanent noise such as unavoidable engine sound errors or legacy print statements.
- [page](https://create.roblox.com/docs/production/analytics/error-report) **[[scripting-and-performance]]** Use Group rules to consolidate families of related errors into one named row, e.g. HttpError:.* as 'Network Issues'.
- [page](https://create.roblox.com/docs/production/analytics/error-report) **[[scripting-and-performance]]** Test regex patterns against real error strings before saving; patterns cannot start with .* or .+ and cannot nest repeaters like (\w+)+.
- [page](https://create.roblox.com/docs/production/analytics/error-report) **[[scripting-and-performance]]** Rules apply only to errors logged after they are saved; order rules by priority since the first match wins.
- [page](https://create.roblox.com/docs/production/analytics/error-report) **[[community-and-discord]]** Check your Discord or DevForum for player reports of errors, including affected devices and regions, to corroborate Error Report findings.
- [page](https://create.roblox.com/docs/production/analytics/error-report) **[[scripting-and-performance]]** Use Developer Console (F9), Script Profiler, and Studio Output window to find and verify errors before publishing.

## Numbers
- [page](https://create.roblox.com/docs/production/analytics/error-report) Unique errors tracked: **500 unique errors by count** (Error Report tracking limit)
- [page](https://create.roblox.com/docs/production/analytics/error-report) Unique warnings tracked: **500 unique warnings by count** (Error Report tracking limit)
- [page](https://create.roblox.com/docs/production/analytics/error-report) New errors tracked per version: **top 100** (Error Report tracking limit)
- [page](https://create.roblox.com/docs/production/analytics/error-report) Tracking counter reset interval: **6 hours** (Error counts reset periodically)
- [page](https://create.roblox.com/docs/production/analytics/error-report) Custom rules per experience: **100** (Maximum ignore/group rules)
- [page](https://create.roblox.com/docs/production/analytics/error-report) Date range filter options: **1 hour, 1 day, 7 days, 30 days** (Error Report time filters)

## Tools
Roblox Creator Dashboard Error Report, Developer Console (F9), Script Profiler, Studio Output Window

## He points to
- Creator Dashboard > Creations > Monitoring > Error Report

## Topics
[[analytics-metrics]] [[community-and-discord]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
