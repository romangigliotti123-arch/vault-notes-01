---
title: "Consume everything - how greedy meshing works"
url: https://devforum.roblox.com/t/consume-everything-how-greedy-meshing-works/452717
creator: Roblox DevForum
official: false
advice_density: medium
date: 2020-02-07
views: 398
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Consume everything - how greedy meshing works

[Open](https://devforum.roblox.com/t/consume-everything-how-greedy-meshing-works/452717) | Roblox DevForum | 398 views | 2020-02-07

## Summary
Elttob explains greedy meshing for voxel builds: merge adjacent blocks into larger cuboids to cut part count while keeping visuals identical. Walks through the 1D algorithm (record start and end positions, extend over non-empty unvisited blocks), extends it to 2D by expanding across rows, and says 3D works the same way.

## Tips
- [page](https://devforum.roblox.com/t/consume-everything-how-greedy-meshing-works/452717) **[[optimization-and-streaming]]** Greedy-mesh voxel builds by merging adjacent blocks into larger cuboids; this cuts part count heavily while the visuals stay the same, reducing lag from large part counts.
- [page](https://devforum.roblox.com/t/consume-everything-how-greedy-meshing-works/452717) **[[building-and-level-design]]** Greedy meshing 1D: start at an unvisited non-empty block, extend while next block is non-empty and unvisited, then record the start and end positions as opposite corners of a cuboid.
- [page](https://devforum.roblox.com/t/consume-everything-how-greedy-meshing-works/452717) **[[scripting-and-performance]]** Extend greedy meshing to 2D by expanding the 1D run across the other axis while every block in that direction can be included, then emit one cuboid per region.
- [page](https://devforum.roblox.com/t/consume-everything-how-greedy-meshing-works/452717) **[[scripting-and-performance]]** Mark blocks as visited so each block is included in exactly one cuboid; repeat for every remaining block. Extending the same idea to 3D follows the 2D pattern.

## Numbers
- [page](https://devforum.roblox.com/t/consume-everything-how-greedy-meshing-works/452717) Part count, unoptimised voxel scene: **15931 instances** (Red scene in the author's comparison image, before greedy meshing)
- [page](https://devforum.roblox.com/t/consume-everything-how-greedy-meshing-works/452717) Part count, greedy-meshed voxel scene: **508 instances** (Blue scene in the author's comparison image, after greedy meshing)

## Tools
Blox (author's voxel project, greedy mesher)

## Quotes
- [page](https://devforum.roblox.com/t/consume-everything-how-greedy-meshing-works/452717) "Greedy meshing is a really useful concept when working with voxels, especially in Roblox where large numbers of parts can cause a lot of lag."

## Topics
[[building-and-level-design]] [[optimization-and-streaming]] [[scripting-and-performance]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
