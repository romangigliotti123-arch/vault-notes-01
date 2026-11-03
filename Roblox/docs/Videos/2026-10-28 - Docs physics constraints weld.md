---
title: "Docs: physics / constraints / weld"
url: https://create.roblox.com/docs/physics/constraints/weld.md
creator: Roblox Creator Docs
official: true
advice_density: low
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: physics / constraints / weld

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://create.roblox.com/docs/physics/constraints/weld.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs on WeldConstraint: connects two BaseParts so they keep relative position/orientation, even if not touching. Covers Studio Constraint-tool creation rules and how moving a welded part via Position (only that part moves, offset recalculated) differs from moving via CFrame (all welded parts move).

## Tips
- [page](https://create.roblox.com/docs/physics/constraints/weld) **[[building-and-level-design]]** Use WeldConstraint to lock BaseParts together; parts need not touch. For attachments or bones use RigidConstraint instead.
- [page](https://create.roblox.com/docs/physics/constraints/weld) **[[building-and-level-design]]** To move a welded assembly, set the root part's CFrame, not Position; setting Position moves only that part and recalculates the weld offset.
- [page](https://create.roblox.com/docs/physics/constraints/weld) **[[building-and-level-design]]** When using Studio's Constraint tool with multiple parts selected, only touching or overlapping parts get welded automatically.

## Tools
Studio Constraint tool, WeldConstraint, RigidConstraint

## Topics
[[building-and-level-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
