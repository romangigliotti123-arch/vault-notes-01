---
title: "UI Design Objects & Tips"
url: https://devforum.roblox.com/t/ui-design-objects-tips/613948
creator: Roblox DevForum
official: false
advice_density: high
date: 2020-06-06
views: 182
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# UI Design Objects & Tips

[Open](https://devforum.roblox.com/t/ui-design-objects-tips/613948) | Roblox DevForum | 182 views | 2020-06-06

## Summary
Reference guide covering UI objects not in the starter guide (UICorner, UIGradient, ViewportFrame, layouts, UIScale, constraints) plus scripting and design tips for Roblox GUIs: feedback, input events, TweenService, GUI inset handling.

## Tips
- [page](https://devforum.roblox.com/t/ui-design-objects-tips/613948) **[[ui-ux-design]]** Use UICorner for rounded corners; a scale of 0.5+ on a square makes a circle. Heavy use can hurt performance since it is a shader applied over the rendered object.
- [page](https://devforum.roblox.com/t/ui-design-objects-tips/613948) **[[ui-ux-design]]** Use UIListLayout and UIGridLayout instead of scripting positions; for grid cells, parent a UIAspectRatioConstraint inside the UIGridLayout to keep aspect ratio.
- [page](https://devforum.roblox.com/t/ui-design-objects-tips/613948) **[[ui-ux-design]]** For simple menus, manually toggle Visible/Enabled rather than UIPageLayout, which often needs cut/paste to refresh after visibility or LayoutOrder changes.
- [page](https://devforum.roblox.com/t/ui-design-objects-tips/613948) **[[ui-ux-design]]** Use UIScale on every element that must resize with screen size; then only update each UIScale's Scale value instead of recalculating sizes individually (e.g. 0.7 for smaller GUIs).
- [page](https://devforum.roblox.com/t/ui-design-objects-tips/613948) **[[ui-ux-design]]** Use UISizeConstraint MinSize to stop elements shrinking to unreadable sizes on small screens.
- [page](https://devforum.roblox.com/t/ui-design-objects-tips/613948) **[[ui-ux-design]]** Anchor GUIs to screen edges (e.g. X position {1,0} with AnchorPoint) so elements never float unintentionally in the middle of the screen.
- [page](https://devforum.roblox.com/t/ui-design-objects-tips/613948) **[[ui-ux-design]]** Use the top 36px inset: set ScreenGui.IgnoreGuiInset to true or compensate with offsets; account for it in code via GuiService:GetGuiInset().
- [page](https://devforum.roblox.com/t/ui-design-objects-tips/613948) **[[ui-ux-design]]** Use numeric rbxassetid:// IDs (Copy ID in Explorer), not rbxgameasset:// URLs, which break across games and when assets are renamed.
- [page](https://devforum.roblox.com/t/ui-design-objects-tips/613948) **[[client-server-and-remotes]]** Give instant feedback on button presses and events before the server responds; do purely client-side work on the client without server round trips.
- [page](https://devforum.roblox.com/t/ui-design-objects-tips/613948) **[[ui-ux-design]]** Add sound to UI interactions, including error sounds (e.g. insufficient funds) to communicate state to the player.
- [page](https://devforum.roblox.com/t/ui-design-objects-tips/613948) **[[ui-ux-design]]** Use GUI InputBegan/InputEnded/MouseButton1Up events for reliable hover and click handling; MouseEnter/MouseLeave often fail to fire.
- [page](https://devforum.roblox.com/t/ui-design-objects-tips/613948) **[[ui-ux-design]]** Process a button press only if the mouse is released while still over the button, the standard real-world convention for a good experience.
- [page](https://devforum.roblox.com/t/ui-design-objects-tips/613948) **[[ui-ux-design]]** Size a ScrollingFrame's CanvasSize by binding to layout:GetPropertyChangedSignal('AbsoluteContentSize') so scrolling always works correctly.
- [page](https://devforum.roblox.com/t/ui-design-objects-tips/613948) **[[ui-ux-design]]** Use camera ViewportSize for full screen size (no inset); use TextService:GetTextSize to measure text.
- [page](https://devforum.roblox.com/t/ui-design-objects-tips/613948) **[[ui-ux-design]]** Use TweenService to animate any GUI property, storing the Tween object for reused open/close animations and calling Play().
- [page](https://devforum.roblox.com/t/ui-design-objects-tips/613948) **[[ui-ux-design]]** For ViewportFrames, set the camera CFrame to look at the model from outside it, lower FieldOfView below 70 for better 2D viewing, and reassign CurrentCamera via script at runtime.
- [page](https://devforum.roblox.com/t/ui-design-objects-tips/613948) **[[ui-ux-design]]** Use WorldModel instead of Model in a ViewportFrame to enable physics and animation on characters.

## Numbers
- [page](https://devforum.roblox.com/t/ui-design-objects-tips/613948) GUI inset height: **36px topbar reserved at top of screen** (Topbar inset; will always be 36px in future per docs)
- [page](https://devforum.roblox.com/t/ui-design-objects-tips/613948) Default camera FieldOfView: **70 (lower recommended for ViewportFrames)** (ViewportFrame camera; lower FOV requires moving camera further away)
- [page](https://devforum.roblox.com/t/ui-design-objects-tips/613948) UICorner circle threshold: **Scale 0.5+ on square** (Produces a circle from a UICorner)

## Tools
UICorner, UIGradient, ViewportFrame, UIListLayout, UIGridLayout, UIScale, TweenService, GuiService

## He points to
- UI Design Starter Guide (EmeraldSlash, DevForum)

## Quotes
- [page](https://devforum.roblox.com/t/ui-design-objects-tips/613948) "Some of my games don't have any button objects at all, it's all just Frames, TextLabels and ImageLabels."
- [page](https://devforum.roblox.com/t/ui-design-objects-tips/613948) "It's just not worth trying to mess around with an object that doesn't quite get exactly what you want where you could just make it yourself."

## Topics
[[client-server-and-remotes]] [[ui-ux-design]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
