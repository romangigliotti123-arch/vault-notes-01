---
title: "Docs: animation / inverse-kinematics"
url: https://create.roblox.com/docs/animation/inverse-kinematics.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: animation / inverse-kinematics

[Open](https://create.roblox.com/docs/animation/inverse-kinematics.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox documentation page on Inverse Kinematics (IK). Explains IKControl for procedurally posing character rigs (Type, EndEffector, Target, ChainRoot), a quick Transform test setup via Attachment target, and adding HingeConstraint (elbow) and BallSocketConstraint (wrist) with LimitsEnabled/UpperAngle to prevent unnatural bending.

## Tips
- [page](https://create.roblox.com/docs/animation/inverse-kinematics) **[[scripting-and-performance]]** Set IKControl Type, EndEffector, Target and ChainRoot explicitly; wrong values produce unnatural poses. Test each IKControl during Play test.
- [page](https://create.roblox.com/docs/animation/inverse-kinematics) **[[3d-modeling-rigging-and-animation]]** ChainRoot determines which joints move: set to LeftUpperArm to affect the whole arm, or LeftLowerArm to affect only below the elbow.
- [page](https://create.roblox.com/docs/animation/inverse-kinematics) **[[3d-modeling-rigging-and-animation]]** Constraint attachments must sit on the same parts as the Motor6D Part0/Part1 and match Motor6D C0/C1 relative positions; the constraint and IKControl must share the same parent Model.
- [page](https://create.roblox.com/docs/animation/inverse-kinematics) **[[3d-modeling-rigging-and-animation]]** Match Attachment1 CFrameOrientation to Attachment0 on hinge constraints; a red arrow in the visualization means orientations violate the constraint.
- [page](https://create.roblox.com/docs/animation/inverse-kinematics) **[[3d-modeling-rigging-and-animation]]** Add a BallSocketConstraint with LimitsEnabled on the wrist; UpperAngle of 80 degrees approximates natural wrist bend.
- [page](https://create.roblox.com/docs/animation/inverse-kinematics) **[[3d-modeling-rigging-and-animation]]** Use R15 built-in RigAttachments (LeftElbowRigAttachment, LeftWristRigAttachment) as constraint attachment anchors instead of creating new joints.

## Numbers
- [page](https://create.roblox.com/docs/animation/inverse-kinematics) BallSocketConstraint UpperAngle (wrist): **80 degrees** (Approximate natural wrist bend limit for IKControl)

## Tools
IKControl, HingeConstraint, BallSocketConstraint, Attachment, Roblox Studio Explorer/Properties

## He points to
- Roblox Creator Docs: Animation Editor

## Topics
[[3d-modeling-rigging-and-animation]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
