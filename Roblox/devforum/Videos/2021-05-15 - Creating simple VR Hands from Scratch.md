---
title: "Creating simple VR Hands from Scratch"
url: https://devforum.roblox.com/t/creating-simple-vr-hands-from-scratch/1227966
creator: Roblox DevForum
official: false
advice_density: medium
date: 2021-05-15
views: 159
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Creating simple VR Hands from Scratch

[Open](https://devforum.roblox.com/t/creating-simple-vr-hands-from-scratch/1227966) | Roblox DevForum | 159 views | 2021-05-15

## Summary
DevForum tutorial on building simple VR hands in Roblox from scratch. Covers a LocalScript in StarterCharacterScripts that disables VR controller models and laser pointer, anchors the HumanoidRootPart, resets the camera CFrame, creates two hand Parts, and moves them via UserInputService.UserCFrameChanged multiplied by the camera CFrame. Notes a follow-up teleport-movement tutorial.

## Tips
- [page](https://devforum.roblox.com/t/creating-simple-vr-hands-from-scratch/1227966) **[[client-server-and-remotes]]** Put the VR setup LocalScript in StarterPlayer > StarterCharacterScripts so it runs only after the character has loaded and Player.Character is available.
- [page](https://devforum.roblox.com/t/creating-simple-vr-hands-from-scratch/1227966) **[[cross-platform-and-console]]** Set Camera.CameraType to Scriptable and reset camera CFrame to its position to avoid a wrongly angled VR view.
- [page](https://devforum.roblox.com/t/creating-simple-vr-hands-from-scratch/1227966) **[[cross-platform-and-console]]** Disable VR controller models (SetCore VREnableControllerModels false) and laser pointer (VRLaserPointerMode 0) before replacing them with custom hand models.
- [page](https://devforum.roblox.com/t/creating-simple-vr-hands-from-scratch/1227966) **[[cross-platform-and-console]]** Update hand positions in UserInputService.UserCFrameChanged, which fires before render, to avoid visible lag between controller and hand models; multiply move by camera.CFrame.
- [page](https://devforum.roblox.com/t/creating-simple-vr-hands-from-scratch/1227966) **[[common-mistakes]]** Avoid capitalised Part names like RightHand for VR hands; the tutorial reports texturing issues fixed by renaming to rightHand/leftHand.
- [page](https://devforum.roblox.com/t/creating-simple-vr-hands-from-scratch/1227966) **[[cross-platform-and-console]]** Anchor the HumanoidRootPart to stop the default character from moving or being visible while in VR.

## Tools
Roblox Studio, Luau, UserInputService, StarterGui:SetCore

## He points to
- VR Teleportation Movement using Hands (DevForum community tutorial, follow-up)

## Topics
[[client-server-and-remotes]] [[common-mistakes]] [[cross-platform-and-console]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
