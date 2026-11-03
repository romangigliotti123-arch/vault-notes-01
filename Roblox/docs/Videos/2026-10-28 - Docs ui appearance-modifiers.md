---
title: "Docs: ui / appearance-modifiers"
url: https://create.roblox.com/docs/ui/appearance-modifiers.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: ui / appearance-modifiers

[Open](https://create.roblox.com/docs/ui/appearance-modifiers.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox documentation for UI appearance modifiers: UIGradient (color/transparency sequences, types, offset, rotation, scale, tile mode), UIStroke (text outline or border, thickness, transparency, position, corner style, layering), UICorner (scale vs offset radius, per-corner radii), UIPadding, and UIShadow (shape/text modes, blur, spread, inset, layering). Several features are beta.

## Tips
- [page](https://create.roblox.com/docs/ui/appearance-modifiers) **[[ui-ux-design]]** Avoid tweening UIStroke.Thickness on text objects; it renders and stores many glyph sizes each frame, causing lag or text flicker.
- [page](https://create.roblox.com/docs/ui/appearance-modifiers) **[[ui-ux-design]]** Use UICorner Scale 0.5 or higher to get a pill shape regardless of width or height; use Offset for fixed pixel radii.
- [page](https://create.roblox.com/docs/ui/appearance-modifiers) **[[ui-ux-design]]** Do not give sibling UIStroke or UIShadow instances the same ZIndex when their render order matters; order is undefined.
- [page](https://create.roblox.com/docs/ui/appearance-modifiers) **[[ui-ux-design]]** Use UIStroke Transparency separate from text transparency to make hollow outlined text or borders.
- [page](https://create.roblox.com/docs/ui/appearance-modifiers) **[[ui-ux-design]]** Set UIShadow.ShowBehindParent to false on transparent parents so the shadow does not darken content behind them.
- [page](https://create.roblox.com/docs/ui/appearance-modifiers) **[[ui-ux-design]]** Use UIGradient TileMode Mirror for seamless repetition; Repeat can show a seam if first and last values differ.
- [page](https://create.roblox.com/docs/ui/appearance-modifiers) **[[ui-ux-design]]** Gradient and upgraded UIShadow features are beta; enable via File > Beta Features before relying on them.

## Numbers
- [page](https://create.roblox.com/docs/ui/appearance-modifiers) UICorner pill threshold: **Scale >= 0.5** (UICorner Scale is relative to shortest edge)
- [page](https://create.roblox.com/docs/ui/appearance-modifiers) Radial gradient radius: **(width+height)/4** (UIGradient radial radius formula)
- [page](https://create.roblox.com/docs/ui/appearance-modifiers) Gradient offset units: **percentage of parent size** (Offset.X 0.25 shifts by 25% of width)
- [page](https://create.roblox.com/docs/ui/appearance-modifiers) Conical sweep default: **0 to 360 degrees** (Scale below 1 reduces the sweep angle)
- [page](https://create.roblox.com/docs/ui/appearance-modifiers) UIShadow blur scale base: **shorter of parent width/height** (BlurRadius scale is relative to shorter side)

## Tools
Roblox Studio, UIGradient, UIStroke, UICorner, UIPadding, UIShadow

## He points to
- Roblox docs: UI appearance modifiers

## Topics
[[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
