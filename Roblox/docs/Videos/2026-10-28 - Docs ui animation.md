---
title: "Docs: ui / animation"
url: https://create.roblox.com/docs/ui/animation.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: ui / animation

[Open](https://create.roblox.com/docs/ui/animation.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox developer docs on UI animation with TweenService: tweening position, size, rotation, transparency, color and strokes; chaining tweens via Completed; easing styles and directions; and a typewriter text effect using a ModuleScript with utf8 graphemes.

## Tips
- [page](https://create.roblox.com/docs/ui/animation) **[[building-art-and-assets]]** Set AnchorPoint to (0.5, 0.5) before tweening position or size so the object grows or moves around its center.
- [page](https://create.roblox.com/docs/ui/animation) **[[ui-ux-design]]** Use Scale UDim2 values instead of pixel offsets for tween targets so UI lands in the same relative place across screen sizes.
- [page](https://create.roblox.com/docs/ui/animation) **[[ui-ux-design]]** Attach a UIAspectRatioConstraint when tweening Size so the element keeps its designed aspect ratio.
- [page](https://create.roblox.com/docs/ui/animation) **[[ui-ux-design]]** For whole-object fades, place the elements in a CanvasGroup and tween GroupTransparency or GroupColor3 instead of tweening each child.
- [page](https://create.roblox.com/docs/ui/animation) **[[ui-ux-design]]** Prefer a UIStroke child over TextStrokeTransparency/TextStrokeColor3 or BorderColor3 for stroke tweens; the docs call it the modern alternative.
- [page](https://create.roblox.com/docs/ui/animation) **[[ui-ux-design]]** Chain tween sequences by calling the next tween's Play inside the previous tween's Completed event.
- [page](https://create.roblox.com/docs/ui/animation) **[[ui-ux-design]]** Default easing is Quad with Out direction; choose Back, Bounce or Elastic for overshoot effects and Linear for constant speed.
- [page](https://create.roblox.com/docs/ui/animation) **[[ui-ux-design]]** Set TextLabel.AutoLocalize to false and strip RichText tags before a per-character typewriter reveal, since tags break the character loop.
- [page](https://create.roblox.com/docs/ui/animation) **[[ui-ux-design]]** Use MaxVisibleGraphemes with utf8.graphemes for typewriter text so multi-byte characters and emoji reveal correctly.

## Numbers
- [page](https://create.roblox.com/docs/ui/animation) Default tween easing style: **Enum.EasingStyle.Quad** (Default when TweenInfo easing style is not specified)
- [page](https://create.roblox.com/docs/ui/animation) Default tween easing direction: **Out** (Default EasingDirection for TweenInfo)
- [page](https://create.roblox.com/docs/ui/animation) Example size target: **UDim2.new(0.4, 0, 0.4, 0)** (Scales object to 40% of screen width or height, whichever is smaller)
- [page](https://create.roblox.com/docs/ui/animation) Example typewriter delay: **0.05 seconds per character** (delayBetweenChars used in the typewriter example)

## Tools
TweenService, TweenInfo, UIAspectRatioConstraint, UIStroke, CanvasGroup, LocalizationService, utf8.graphemes

## He points to
- Style Editor guide (style transitions)
- Stroke section of UI tween docs

## Topics
[[building-art-and-assets]] [[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
