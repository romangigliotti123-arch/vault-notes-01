---
title: "Docs: cloud-services / video-service"
url: https://create.roblox.com/docs/cloud-services/video-service.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: cloud-services / video-service

[Open](https://create.roblox.com/docs/cloud-services/video-service.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox Video Service docs: how VideoFrame video assets download and play, the Video Service dashboard in Creator Dashboard Monitoring (Playback breakdown and Playback hours charts), usage categories (played-viewed, preloaded-never-played, played-never-viewed), and guidance to set Video only when players will likely see it.

## Tips
- [page](https://create.roblox.com/docs/cloud-services/video-service) **[[analytics-metrics]]** Check the Video Service dashboard (Creator Dashboard > Monitoring) to compare efficient vs inefficient video usage after adding or changing videos.
- [page](https://create.roblox.com/docs/cloud-services/video-service) **[[optimization-and-streaming]]** Only set VideoFrame.Video/VideoContent and call Play() when players are likely to see or hear the video; clear the property (e.g. to "") when it is no longer visible or nearby.
- [page](https://create.roblox.com/docs/cloud-services/video-service) **[[optimization-and-streaming]]** Preload video ahead of time only when you are confident it will be seen, such as a mandatory later cutscene or a video in a central hub, to avoid loading delay.
- [page](https://create.roblox.com/docs/cloud-services/video-service) **[[optimization-and-streaming]]** If you only need a video's audio, extract it and play it as a separate audio asset instead of a video asset; decoding video for audio wastes data and memory.
- [page](https://create.roblox.com/docs/cloud-services/video-service) **[[optimization-and-streaming]]** Monitor download-vs-view ratio to reduce unnecessary data transfer and improve performance on lower-end devices.

## Tools
Video Service dashboard (Creator Dashboard > Monitoring), Class.VideoFrame, Class.SurfaceGui, Class.ScreenGui

## Topics
[[analytics-metrics]] [[optimization-and-streaming]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
