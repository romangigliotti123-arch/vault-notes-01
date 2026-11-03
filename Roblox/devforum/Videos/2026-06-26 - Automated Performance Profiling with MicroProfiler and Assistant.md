---
title: "Automated Performance Profiling with MicroProfiler and Assistant"
url: https://devforum.roblox.com/t/automated-performance-profiling-with-microprofiler-and-assistant/4704417
creator: Roblox DevForum
official: false
advice_density: medium
date: 2026-06-26
views: 225
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Automated Performance Profiling with MicroProfiler and Assistant

[Open](https://devforum.roblox.com/t/automated-performance-profiling-with-microprofiler-and-assistant/4704417) | Roblox DevForum | 225 views | 2026-06-26

## Summary
Roblox DevForum/docs announcement: Studio Assistant can analyze paused MicroProfiler captures, identify frame-time spike causes (physics- vs script-bound, highest exclusive time category), and propose fixes. Also works via Studio MCP in agentic loops. Underlying LibMP API exposes all MicroProfiler data programmatically.

## Tips
- [page](https://devforum.roblox.com/t/automated-performance-profiling-with-microprofiler-and-assistant/4704417) **[[optimization-and-streaming]]** Open MicroProfiler with Ctrl+F6 (Cmd+F6 on Mac), and pause the capture (Ctrl+P) when you spot a frame time spike before asking for analysis.
- [page](https://devforum.roblox.com/t/automated-performance-profiling-with-microprofiler-and-assistant/4704417) **[[optimization-and-streaming]]** Ask Assistant whether a spike is physics-bound or script-bound, and which category has the highest exclusive time, to narrow down bottlenecks quickly.
- [page](https://devforum.roblox.com/t/automated-performance-profiling-with-microprofiler-and-assistant/4704417) **[[testing-debugging-and-qa]]** Use a reproduce-profile-fix-retest loop with Assistant: reproduce the FPS drop, find the cause in MicroProfiler, apply the fix, then profile again to verify.
- [page](https://devforum.roblox.com/t/automated-performance-profiling-with-microprofiler-and-assistant/4704417) **[[version-control-and-tooling]]** Connect your own AI agent via Studio MCP to run MicroProfiler analysis inside agentic loops and measure how each change affects performance.
- [page](https://devforum.roblox.com/t/automated-performance-profiling-with-microprofiler-and-assistant/4704417) **[[scripting-and-performance]]** For advanced profiling, use the MicroProfiler API (LibMP) to programmatically access all MicroProfiler data.

## Tools
Roblox Studio MicroProfiler, Assistant (Studio AI), Studio MCP server, MicroProfiler API (LibMP)

## He points to
- Studio MCP server connection instructions (linked in post)

## Topics
[[optimization-and-streaming]] [[scripting-and-performance]] [[testing-debugging-and-qa]] [[version-control-and-tooling]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
