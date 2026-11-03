---
title: "Docs: studio / optimization / scriptprofiler"
url: https://create.roblox.com/docs/studio/optimization/scriptprofiler.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: studio / optimization / scriptprofiler

[Open](https://create.roblox.com/docs/studio/optimization/scriptprofiler.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox Creator Docs page on the Script Profiler tool in the Developer Console. Covers recording client or server CPU profiles (frequency, session length, live polling), reading Callgraph and Functions views with ms or % units and averaging, and exporting session data as JSON with its field definitions.

## Tips
- [page](https://create.roblox.com/docs/studio/optimization/scriptprofiler) **[[scripting-and-performance]]** Use Script Profiler (Developer Console > ScriptProfiler) to find the scripts consuming the most CPU time before optimizing.
- [page](https://create.roblox.com/docs/studio/optimization/scriptprofiler) **[[scripting-and-performance]]** Use the 1 KHz default for general profiling; 10 KHz gives higher precision but costs more performance and may still miss very frequent API calls.
- [page](https://create.roblox.com/docs/studio/optimization/scriptprofiler) **[[scripting-and-performance]]** Profile Client and Server separately; server data is cleared at the end of each session, so export it before starting a new one.
- [page](https://create.roblox.com/docs/studio/optimization/scriptprofiler) **[[optimization-and-streaming]]** Use Average (e.g. 5-minute) to extrapolate short test sessions into expected per-minute cost for longer play periods.
- [page](https://create.roblox.com/docs/studio/optimization/scriptprofiler) **[[analytics-metrics]]** Export profiling data as JSON to compare sessions or analyze node and function TotalDuration values outside Studio.

## Numbers
- [page](https://create.roblox.com/docs/studio/optimization/scriptprofiler) Profiler frequency options: **1,000/s (default) or 10,000/s** (Script Profiler sampling rate; 10 KHz more precise but costlier)
- [page](https://create.roblox.com/docs/studio/optimization/scriptprofiler) Session length options: **1, 5, 10 minutes or Manual (default)** (Recording duration; Manual requires stopping manually)
- [page](https://create.roblox.com/docs/studio/optimization/scriptprofiler) Live polling refresh: **Each second when enabled** (Live checkbox refreshes profiling data during session; off by default)
- [page](https://create.roblox.com/docs/studio/optimization/scriptprofiler) Export time units: **TotalDuration in microseconds** (JSON export; SessionStart/EndTime in milliseconds)

## Tools
Script Profiler, Developer Console

## He points to
- Roblox Creator Docs: Developer Console

## Topics
[[analytics-metrics]] [[optimization-and-streaming]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
