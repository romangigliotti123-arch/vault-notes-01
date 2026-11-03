---
title: "Docs: tutorials / use-case-tutorials / ui / create-hud-meters"
url: https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/create-hud-meters.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: tutorials / use-case-tutorials / ui / create-hud-meters

[Open](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/create-hud-meters.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox official tutorial on building a custom HUD health meter: Device Emulator testing, ScreenGui with DeviceSafeInsets, scale-based UDim2 layout with UIPadding/UICorner/UIStroke/UISizeConstraint, disabling the default health GUI via SetCoreGuiEnabled, and tweened, gradient-colored health bar driven by Humanoid.HealthChanged.

## Tips
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/create-hud-meters) **[[first-session-onboarding]]** Test HUD layouts in Studio's Device Emulator on phones and tablets (e.g. iPhone X, iPad 7th Gen) before shipping, since mobile has the least screen space.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/create-hud-meters) **[[ui-ux-design]]** Set ScreenGui.ScreenInsets to DeviceSafeInsets to tuck HUD against the screen edge; CoreUISafeInsets leaves a large gap at the top.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/create-hud-meters) **[[ui-ux-design]]** Position and size HUD elements with Scale values so they adapt across resolutions; use Offset only for fixed pixel details like padding.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/create-hud-meters) **[[ui-ux-design]]** Use UISizeConstraint (e.g. MaxSize inf,20) to stop bars becoming too tall on tablets while keeping width responsive.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/create-hud-meters) **[[ui-ux-design]]** Use UICorner CornerRadius 0.5,0 for pill-shaped bars and UIStroke plus a semi-transparent dark fill so the bar reads on light and dark backgrounds.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/create-hud-meters) **[[ui-ux-design]]** Set ImageLabel ZIndex higher than sibling frames so icons render in front of the meter.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/create-hud-meters) **[[client-server-and-remotes]]** Drive HUD meters from Humanoid.HealthChanged on the client; health replicates from the server, so no extra remote is needed for display.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/create-hud-meters) **[[core-loops-and-game-design]]** Disable the default Roblox health GUI with StarterGui:SetCoreGuiEnabled(Enum.CoreGuiType.Health, false) from a LocalScript to avoid duplicate overlapping meters.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/create-hud-meters) **[[player-psychology-and-game-feel]]** Tween HUD bar size and color (about 0.5s, Exponential Out) rather than snapping, and replace the default red screen-edge damage tint with a ColorCorrectionEffect if wanted.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/create-hud-meters) **[[scripting-and-performance]]** Reset HUD state on respawn by running the update script from StarterCharacterScripts, which runs on every character spawn.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/create-hud-meters) **[[core-loops-and-game-design]]** Disable the Health script in StarterCharacterScripts if you want to remove the default gradual regeneration.

## Numbers
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/create-hud-meters) Edge padding: **16 px on all edges via UIPadding** (Applied regardless of screen resolution in the HUD container)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/create-hud-meters) Meter size: **35% width, 5% height (scale), max height 20 px** (Health meter bar dimensions in the tutorial)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/create-hud-meters) Icon size: **200% of MeterBar, 1:1 aspect ratio** (Heart icon ImageLabel size relative to the bar)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/create-hud-meters) Tween duration: **0.5 seconds** (Health bar size and color tween duration)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/create-hud-meters) Stroke transparency / thickness: **0.25 transparency, 3 thickness** (UIStroke on the meter frame)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/create-hud-meters) Background transparency: **0.75 (25% opacity), black fill** (MeterBar frame styling)

## Tools
Roblox Studio Device Emulator, ScreenGui, UIPadding, UICorner, UIStroke, UISizeConstraint, TweenService, LocalScript

## He points to
- Hazardous Space Station (starter template)
- UI Fundamentals - HUD Meter (completed reference template)

## Topics
[[client-server-and-remotes]] [[core-loops-and-game-design]] [[first-session-onboarding]] [[player-psychology-and-game-feel]] [[scripting-and-performance]] [[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
