---
title: "Simple Things Mobile Players LOVE! | Roblox Studio"
url: https://youtu.be/e48wgHQll2Y
creator: Stewiepfing
official: false
advice_density: medium
date: 2025-04-27
views: 12531
transcript: auto-captions
confidence: high
tags: [roblox, stewiepfing, youtube-learn]
creator_trust: TRUSTED
creator_score: 7.7
---

> [!note] Trust: TRUSTED (credibility audit score 7.7): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Simple Things Mobile Players LOVE! | Roblox Studio

[Watch](https://youtu.be/e48wgHQll2Y) | stewiepfing | 12,531 views | 2025-04-27

## Summary
Mobile-optimisation tutorial for Roblox Studio using Luau scripts: scales UI strokes to screen height via observe-pattern modules, adds haptic rumble via a haptics module (noting HapticService is deprecated in favour of HapticEffect), shows UIAspectRatioConstraint for consistent shapes across devices, and builds a click ripple effect.

## Tips
- [0:19](https://youtu.be/e48wgHQll2Y?t=19) **[[scripting-and-performance]]** Scale UI strokes with viewport height: store thickness at 1080p baseline and set thickness = viewportSize.Y × (originalThickness/1080) so borders look the same on phones.
- [4:30](https://youtu.be/e48wgHQll2Y?t=270) **[[scripting-and-performance]]** Use WaitForChild on required modules in replicated scripts; otherwise code runs before replication and errors on load.
- [5:54](https://youtu.be/e48wgHQll2Y?t=354) **[[playtesting-and-feedback]]** Add haptic rumble to mobile and console players to boost engagement; use timed rumble for fixed durations and start/stop rumble for open-ended systems.
- [5:13](https://youtu.be/e48wgHQll2Y?t=313) **[[roblox-platform-changes]]** HapticService is deprecated; check the docs and use HapticEffect for new rumble code.
- [8:50](https://youtu.be/e48wgHQll2Y?t=530) **[[building-art-and-assets]]** Apply UIAspectRatioConstraint to frames and images so shapes keep their proportions across phone, tablet and PC resolutions.
- [10:27](https://youtu.be/e48wgHQll2Y?t=627) **[[first-session-onboarding]]** Add a click ripple tween on input (mouse, touch, or controller R2) to make the game feel more responsive, a cheap polish tweak.

## Numbers
- [0:00](https://youtu.be/e48wgHQll2Y?t=0) Mobile share of Roblox players: **Large majority (no figure given)**
- [5:54](https://youtu.be/e48wgHQll2Y?t=354) Haptic rumble example: **Amount 2, duration 5 s (timed); 3 s start/stop example**

## Tools
Roblox Studio, Luau, Slight Nick observe pattern modules (ObserveProperty, ObserveTag), HapticEffect (recommended replacement for HapticService), UIAspectRatioConstraint, UIStroke, Custom haptics module

## He points to
- Slight Nick observe pattern modules (GitHub, linked in description)
- Creator's older haptics module video

## Quotes
- [0:00](https://youtu.be/e48wgHQll2Y?t=0) "The large majority of players on Roblox are playing on mobile devices. That's why it's essential to optimize and design our games with mobile users in mind."
- [5:13](https://youtu.be/e48wgHQll2Y?t=313) "I just looked at the haptic service documentation and it looks like the service is deprecated."

## On screen
Contact sheet shows a phone-emulator view with a scaled UI square (0:09, 5:03), Studio Explorer with a ScaleUIStroke tag setup and StarterGui/ReplicatedStorage hierarchy, code for the ripple module (10:33 shows a clicked-in-game ripple on a platform), and green vs red squares at 9:32 comparing UIAspectRatioConstraint on and off. No analytics or thumbnails shown.

## Topics
[[building-art-and-assets]] [[first-session-onboarding]] [[playtesting-and-feedback]] [[roblox-platform-changes]] [[scripting-and-performance]]

Back to [[stewiepfing - How to make successful Roblox games]]
