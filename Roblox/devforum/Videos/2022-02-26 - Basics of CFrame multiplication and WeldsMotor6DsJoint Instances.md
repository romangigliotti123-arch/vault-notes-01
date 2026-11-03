---
title: "Basics of CFrame multiplication and Welds/Motor6Ds/Joint Instances"
url: https://devforum.roblox.com/t/basics-of-cframe-multiplication-and-weldsmotor6dsjoint-instances/1682079
creator: Roblox DevForum
official: false
advice_density: low
date: 2022-02-26
views: 126
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Basics of CFrame multiplication and Welds/Motor6Ds/Joint Instances

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Open](https://devforum.roblox.com/t/basics-of-cframe-multiplication-and-weldsmotor6dsjoint-instances/1682079) | Roblox DevForum | 126 views | 2022-02-26

## Summary
Devforum tutorial by dthecoolest on CFrame multiplication order (local vs world axes), attachments' WorldCFrame, the weld equation Part1.CFrame*C1 == Part0.CFrame*C0, and editing Motor6D C0/C1 to aim joints without breaking them.

## Tips
- [page](https://devforum.roblox.com/t/basics-of-cframe-multiplication-and-weldsmotor6dsjoint-instances/1682079) **[[scripting-and-performance]]** When rotating a part in world space, rotate at origin first then add position back: part.CFrame = rotation.Rotation + part.Position, to avoid orbital motion.
- [page](https://devforum.roblox.com/t/basics-of-cframe-multiplication-and-weldsmotor6dsjoint-instances/1682079) **[[building-art-and-assets]]** To rotate a CFrame around world axes in one line: CFrame.Angles(Rx,Ry,Rz) * (cf - cf.Position) + cf.Position.
- [page](https://devforum.roblox.com/t/basics-of-cframe-multiplication-and-weldsmotor6dsjoint-instances/1682079) **[[scripting-and-performance]]** Modify Motor6D joints by changing C0 with Part0.CFrame:Inverse() * targetWorldCFrame * C1, keeping original C0 position, so limbs stay attached.
- [page](https://devforum.roblox.com/t/basics-of-cframe-multiplication-and-weldsmotor6dsjoint-instances/1682079) **[[scripting-and-performance]]** Use CFrame.lookAt-style world CFrames for head look-at and arm pointing by converting them into joint C0 space, which is useful for IK.

## Tools
Roblox Studio, Motor6D, Weld, Attachment

## Topics
[[building-and-level-design]] [[building-art-and-assets]] [[client-server-and-remotes]] [[common-mistakes]] [[scripting-and-performance]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
