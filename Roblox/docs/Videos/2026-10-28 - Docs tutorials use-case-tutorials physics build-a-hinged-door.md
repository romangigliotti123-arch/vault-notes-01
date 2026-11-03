---
title: "Docs: tutorials / use-case-tutorials / physics / build-a-hinged-door"
url: https://create.roblox.com/docs/tutorials/use-case-tutorials/physics/build-a-hinged-door.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: tutorials / use-case-tutorials / physics / build-a-hinged-door

[Open](https://create.roblox.com/docs/tutorials/use-case-tutorials/physics/build-a-hinged-door.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox docs tutorial on building a swinging hinged door with HingeConstraint: create door and frame parts, add attachments, orient their axes, connect Attachment0/Attachment1, then set LowerAngle/UpperAngle limits to restrict swing.

## Tips
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/physics/build-a-hinged-door) **[[building-and-level-design]]** Align paired attachments precisely; misaligned attachments can make the door swing incorrectly. Use Snap to Grid or edit Position in Properties.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/physics/build-a-hinged-door) **[[physics-pathfinding-and-npc-ai]]** Anchor the static frame but leave the door unanchored; anchored or blocked doors will not move.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/physics/build-a-hinged-door) **[[physics-pathfinding-and-npc-ai]]** Hinge pivots around the attachment's yellow axis; point both yellow axes up for a standard vertical door swing.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/physics/build-a-hinged-door) **[[physics-pathfinding-and-npc-ai]]** Limits use the orange axis, not yellow; orient DoorAttachment's orange arrow toward the frame so the green arc plane faces it.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/physics/build-a-hinged-door) **[[physics-pathfinding-and-npc-ai]]** Enable LimitsEnabled on the HingeConstraint and set LowerAngle -90 and UpperAngle 90 to stop the door swinging past the frame.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/physics/build-a-hinged-door) **[[building-and-level-design]]** Enable View > Show Constraint Details and use rotation snapping set to 90 for accurate attachment orientation.

## Numbers
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/physics/build-a-hinged-door) LowerAngle / UpperAngle: **-90 / 90** (Hinge limits for a standard door swing range)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/physics/build-a-hinged-door) Rotate snapping increment: **90** (Rotation snap value used to orient attachments accurately)

## Tools
Roblox Studio, HingeConstraint, Attachment, Properties window, Explorer

## He points to
- Roblox docs: Constraints (Class.HingeConstraint)

## Topics
[[building-and-level-design]] [[physics-pathfinding-and-npc-ai]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
