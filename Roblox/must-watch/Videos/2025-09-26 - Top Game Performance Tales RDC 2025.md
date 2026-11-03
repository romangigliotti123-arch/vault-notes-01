---
title: "Top Game Performance Tales | RDC 2025"
url: https://youtu.be/rwLEnBtXr30
creator: Roblox
official: true
advice_density: high
date: 2025-09-26
views: 69870
transcript: auto-captions
confidence: high
tags: [roblox, mustwatch, youtube-learn]
---

# Top Game Performance Tales | RDC 2025

[Watch](https://youtu.be/rwLEnBtXr30) | MustWatch | 69,870 views | 2025-09-26

## Summary
RDC 2025 talk by Roblox's Peter McNeil and Lynn on performance problems in top games (Dead Rails, Grow a Garden), covering diagnosis tools, root causes, fixes, and upcoming Roblox tooling.

## Tips
- [5:12](https://youtu.be/rwLEnBtXr30?t=312) **[[scripting-and-performance]]** Test client memory on a real low-end device with the dev console; PC client readings differ from mobile.
- [9:54](https://youtu.be/rwLEnBtXr30?t=594) **[[scripting-and-performance]]** Anchor and disable animators for NPCs outside combat range; Dead Rails cut server CPU by about half.
- [13:29](https://youtu.be/rwLEnBtXr30?t=809) **[[scripting-and-performance]]** Don't resize welded or anchored server parts per frame; make cosmetic effects client-side.
- [17:16](https://youtu.be/rwLEnBtXr30?t=1036) **[[scripting-and-performance]]** Don't store server-only data as attributes and tags on many parts; they replicate and multiply memory.
- [19:47](https://youtu.be/rwLEnBtXr30?t=1187) **[[development-process-and-speed]]** Build debug tools to spawn load in Studio so you can reproduce performance problems before release.
- [20:53](https://youtu.be/rwLEnBtXr30?t=1253) **[[analytics-metrics]]** Check client crash rate in creator analytics after each publish; a jump from 3-4% to 45% signals a bad build.
- [29:26](https://youtu.be/rwLEnBtXr30?t=1766) **[[scripting-and-performance]]** Triage: confirm the game works, test on real hardware, check frame rate, then stats screen, then microprofiler.

## Numbers
- [3:27](https://youtu.be/rwLEnBtXr30?t=207) Max concurrent users: **12M at start of year, 45M at time of talk**
- [4:32](https://youtu.be/rwLEnBtXr30?t=272) Low-end memory crash threshold: **~1.4 GB client memory**
- [17:16](https://youtu.be/rwLEnBtXr30?t=1036) Grow a Garden crash rate spike: **3-4% normal rising to 45% after one build**

## Games
- **Dead Rails**: Anchor and disable animators for out-of-range NPCs; fix stray awake physics parts.
- **Grow a Garden**: Replicated attributes and tags on thousands of parts caused a 45% crash spike.

## Tools
Developer Console, Microprofiler, F2 stats screen, Creator analytics

## He points to
- RDC 2024 Using Roblox Tools to Improve Performance
- Roblox Creator Hub
- Roblox DevForum

## Quotes
- [17:16](https://youtu.be/rwLEnBtXr30?t=1036) "you multiply that by 10,000 or 100,000 parts that amount of memory was going to stack up"

## Topics
[[analytics-metrics]] [[development-process-and-speed]] [[scripting-and-performance]]

Back to [[MustWatch - How to make successful Roblox games]]
