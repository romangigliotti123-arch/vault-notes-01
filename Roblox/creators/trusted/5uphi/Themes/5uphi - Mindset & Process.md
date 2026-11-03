---
title: 5uphi - Mindset & Process
creator: 5uphi
tags: [roblox, 5uphi, theme]
creator_trust: TRUSTED
creator_score: 8.8
---

> [!note] Trust: TRUSTED (credibility audit score 8.8): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# 5uphi: Mindset & Process

All 5uphi tips on this theme, grouped by topic, oldest first. Cross-creator synthesis: see [[README]] in roblox-kb.

## [[analytics-metrics]]
- 2024-11-28 [2:23:21](https://youtu.be/SVLFkdeh6c8?t=8601) Benchmark plugin cost with os.clock: analysing a 500-line script took about 0.06s, and module updates about 0.005s. ([[2024-11-28 - Global Framework - Roblox (Library, Plugin, Scripting)|Global Framework - Roblox (Library, Plugin, Script]])

## [[development-process-and-speed]]
- 2024-11-28 [0:58](https://youtu.be/SVLFkdeh6c8?t=58) Use the Global Library model from the Toolbox as a starting point; the framework does not force a particular programming style. ([[2024-11-28 - Global Framework - Roblox (Library, Plugin, Scripting)|Global Framework - Roblox (Library, Plugin, Script]])

## [[common-mistakes]]
- 2023-06-22 [5:05](https://youtu.be/ARPfIt16sXI?t=305) Misconception: UpdateAsync is not inherently more secure than SetAsync; it only helps when you read and modify the previous value. ([[2023-06-22 - DataStore2 vs ProfileService vs Suphi's DataStore Module|DataStore2 vs ProfileService vs Suphi's DataStore ]])
- 2024-11-28 [39:31](https://youtu.be/SVLFkdeh6c8?t=2371) Never put infinite loops in the script or initialize stages; they block all later stages. Only loop inside the start stage. ([[2024-11-28 - Global Framework - Roblox (Library, Plugin, Scripting)|Global Framework - Roblox (Library, Plugin, Script]])

## [[testing-debugging-and-qa]]
- 2024-08-06 [1:19:54](https://youtu.be/DTEraIOfoS0?t=4794) Using task.defer hides iteration bugs; test with task.spawn first to expose problems in event systems. ([[2024-08-06 - Linked List Signals - Roblox Scripting Tutorial|Linked List / Signals - Roblox Scripting Tutorial]])
- 2024-10-13 [22:44](https://youtu.be/AkF-4x7qfzM?t=1364) Simulate lag with Studio Settings > Network > incoming replication lag and sudden ping changes to reproduce desync bugs. ([[2024-10-13 - Animation Controller Synchronization - Roblox Scripting Tutorial|Animation Controller Synchronization - Roblox Scri]])

Up: [[5uphi - How to make successful Roblox games]]
