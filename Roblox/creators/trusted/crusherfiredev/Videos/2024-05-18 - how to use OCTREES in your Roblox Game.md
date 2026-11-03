---
title: "how to use OCTREES in your Roblox Game"
url: https://youtu.be/OksI7HpEd6w
creator: Crusherfire
official: false
advice_density: medium
date: 2024-05-18
views: 20046
transcript: auto-captions
confidence: high
tags: [roblox, crusherfiredev, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.7
---

> [!note] Trust: TRUSTED (credibility audit score 8.7): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# how to use OCTREES in your Roblox Game

[Watch](https://youtu.be/OksI7HpEd6w) | crusherfiredev | 20,046 views | 2024-05-18

## Summary
Tutorial on using octrees (spatial partitioning via nested cubes) in Roblox to speed up radius/distance queries over thousands of parts. Uses Quenty's octree module; benchmarks linear search at 0.032s vs octree at 0.002s for a 160-stud radius search over thousands of tagged parts.

## Tips
- [2:45](https://youtu.be/OksI7HpEd6w?t=165) **[[scripting-and-performance]]** For distance queries over thousands of objects, use a spatial structure (octree) instead of looping all objects and checking distance each time.
- [2:45](https://youtu.be/OksI7HpEd6w?t=165) **[[scripting-and-performance]]** Use Quenty's octree module (Octree/radiusSearch API) rather than writing your own spatial partitioning from scratch.
- [3:27](https://youtu.be/OksI7HpEd6w?t=207) **[[scripting-and-performance]]** Tag objects with CollectionService and collect them with GetTagged to bulk-insert them into the octree at startup.
- [5:30](https://youtu.be/OksI7HpEd6w?t=330) **[[scripting-and-performance]]** Benchmark with os.clock/tick start and end timestamps to compare approaches; measure execution time excluding any intentional delays.

## Numbers
- [8:13](https://youtu.be/OksI7HpEd6w?t=493) Linear search execution time: **0.032 s for thousands of tagged parts (160-stud radius)**
- [8:13](https://youtu.be/OksI7HpEd6w?t=493) Octree radius search execution time: **0.002 s for same query**
- [8:13](https://youtu.be/OksI7HpEd6w?t=493) Relative slowdown of linear search: **~1,500% slower (reported as 1,2103%, likely transcription error)**
- [0:00](https://youtu.be/OksI7HpEd6w?t=0) Example object count: **5,000 trees; speaker's test used thousands of parts**

## Tools
Quenty's octree module (Roblox), CollectionService, Roblox Studio

## He points to
- Quenty's octree module (linked in video description)
- Video on quadtrees for 2D games (linked in description)

## Quotes
- [0:42](https://youtu.be/OksI7HpEd6w?t=42) "once you start getting into the thousands ... you're going to want to have a more efficient way of figuring out what trees or whatever objects are closest to the player"

## Topics
[[scripting-and-performance]]

Back to [[crusherfiredev - How to make successful Roblox games]]
