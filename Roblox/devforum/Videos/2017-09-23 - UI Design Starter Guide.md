---
title: "UI Design Starter Guide"
url: https://devforum.roblox.com/t/ui-design-starter-guide/53461
creator: Roblox DevForum
official: false
advice_density: high
date: 2017-09-23
views: 1111
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# UI Design Starter Guide

[Open](https://devforum.roblox.com/t/ui-design-starter-guide/53461) | Roblox DevForum | 1,111 views | 2017-09-23

## Summary
Starter guide on Roblox GUI design: UDim2 scale vs offset, AnchorPoint, ZIndex/DisplayOrder, aspect-ratio control via SizeConstraint (RelativeYY preferred) and UIAspectRatioConstraint, text readability (TextScaled, colour contrast, strokes, background), images (9-slicing, spritesheets, black edge fix), and padding techniques.

## Tips
- [page](https://devforum.roblox.com/t/ui-design-starter-guide/53461) **[[ui-ux-design]]** Build UIs mainly in Scale rather than Offset; use Offset only when pixel-exact sizing is specifically needed.
- [page](https://devforum.roblox.com/t/ui-design-starter-guide/53461) **[[ui-ux-design]]** Design for the device aspect ratio, not just Studio's screen size; Studio layouts often look different in-game on other devices.
- [page](https://devforum.roblox.com/t/ui-design-starter-guide/53461) **[[ui-ux-design]]** Use SizeConstraint RelativeYY to keep aspect ratio; size relative to the dominant axis (e.g. width 2x height = {2,0},{1,0} for 2:1).
- [page](https://devforum.roblox.com/t/ui-design-starter-guide/53461) **[[ui-ux-design]]** Use RelativeXX for objects inside a vertical ScrollingFrame so they don't grow as CanvasSize increases; RelativeYY for horizontal ones.
- [page](https://devforum.roblox.com/t/ui-design-starter-guide/53461) **[[ui-ux-design]]** Use AnchorPoint (e.g. 0,1 with Position Y scale 1) to pin elements to screen edges without extra position math.
- [page](https://devforum.roblox.com/t/ui-design-starter-guide/53461) **[[ui-ux-design]]** Avoid TextScaled blindly; check visual consistency so buttons in the same group don't end up with different text sizes.
- [page](https://devforum.roblox.com/t/ui-design-starter-guide/53461) **[[ui-ux-design]]** Use white or bright text by default; for dark colours like blue or red, lighten them or add a stroke or background.
- [page](https://devforum.roblox.com/t/ui-design-starter-guide/53461) **[[ui-ux-design]]** Give text a TextStrokeColor3 that contrasts with the text colour; white text can use stroke transparency ~0.8 for subtle separation.
- [page](https://devforum.roblox.com/t/ui-design-starter-guide/53461) **[[ui-ux-design]]** Keep the background behind text simple and uncluttered so letters remain readable.
- [page](https://devforum.roblox.com/t/ui-design-starter-guide/53461) **[[ui-ux-design]]** Avoid text wrapping in buttons; resize the button, shrink the text, or disable TextWrapped for consistent appearance.
- [page](https://devforum.roblox.com/t/ui-design-starter-guide/53461) **[[ui-ux-design]]** Do not display images larger than their original resolution; it causes pixelation and blur.
- [page](https://devforum.roblox.com/t/ui-design-starter-guide/53461) **[[ui-ux-design]]** Use 9-slicing (ScaleType Slice, SliceCenter in pixels) so rounded or bordered images stretch without distortion.
- [page](https://devforum.roblox.com/t/ui-design-starter-guide/53461) **[[ui-ux-design]]** Use spritesheets with ImageRectSize and ImageRectOffset to swap hover or animation states without uploading many images.
- [page](https://devforum.roblox.com/t/ui-design-starter-guide/53461) **[[ui-ux-design]]** Add padding between element edges and parent frames; use UIPadding or manual sizing, and separate text from frame edges with a child label.
- [page](https://devforum.roblox.com/t/ui-design-starter-guide/53461) **[[ui-ux-design]]** Maintain contrast between elements and keep UI styling consistent; restyle free models or bought GUIs to match your game.
- [page](https://devforum.roblox.com/t/ui-design-starter-guide/53461) **[[ui-ux-design]]** Keep UI from covering the game view; large sidebars covering a third of the screen waste space.
- [page](https://devforum.roblox.com/t/ui-design-starter-guide/53461) **[[ui-ux-design]]** Use ZIndex within a ScreenGui for layering; use ScreenGui DisplayOrder to layer separate ScreenGuis.

## Numbers
- [page](https://devforum.roblox.com/t/ui-design-starter-guide/53461) Aspect ratio example: **Width 2x height: Size {2,0},{1,0} with RelativeYY** (Half-screen-height version uses {1,0},{0.5,0})
- [page](https://devforum.roblox.com/t/ui-design-starter-guide/53461) Padding example: **10px padding: size {1,-20},{1,-20}, position {0,10},{0,10}** (Manual padding both sides; subtract only 10 for one side)
- [page](https://devforum.roblox.com/t/ui-design-starter-guide/53461) Stroke transparency: **0.8 for white text** (Barely visible shadow for white text separation)
- [page](https://devforum.roblox.com/t/ui-design-starter-guide/53461) Spritesheet example: **52x104 sheet, hover ImageRectOffset X = 52** (Two-state button using 52px wide sprites)

## Tools
UIAspectRatioConstraint, UIPadding, UIListLayout, PixelFix, SizeConstraint, ScrollingFrame, TextScaled, 9-slicing (SliceCenter)

## He points to
- PixelFix: Remove the black edges on scaled images
- Quenty Medium article on fixing images in Roblox UI
- How to use SliceCenter (Roblox's 9-Slice GUI Property)
- UI Design Objects & Tips (DevForum)

## Quotes
- [page](https://devforum.roblox.com/t/ui-design-starter-guide/53461) "I make my UIs 100% in Scale unless I have a specific need for offset. All three of my recent games have had only a single UI that scales perfectly across all devices."
- [page](https://devforum.roblox.com/t/ui-design-starter-guide/53461) "Offset is not very good either, and for support on multiple devices will require redesigning your UI multiple times."

## Topics
[[ui-ux-design]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
