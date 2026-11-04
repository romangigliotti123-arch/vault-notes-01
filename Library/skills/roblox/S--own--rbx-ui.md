---
id: "rbx-ui"
type: skill
category: "roblox"
source: "own"
license: "first-party"
repo_path: "skills/roblox/rbx-ui/SKILL.md"
description: "Build Roblox ScreenGui interfaces that scale across phone, tablet, console and PC: Scale sizing, UIAspectRatio, safe areas, touch targets, controller focus. Use when creating or fixing Roblox UI."
orig_name: "rbx-ui"
orig_description: "Build Roblox ScreenGui interfaces that scale across phone, tablet, console and PC: Scale sizing, UIAspectRatio, safe areas, touch targets, controller focus. Use when creating or fixing Roblox UI, menus, HUD or shop screens with broken layout on phones."
tags: [lib/skill, cat/roblox, src/own]
---

# rbx-ui

> Build Roblox ScreenGui interfaces that scale across phone, tablet, console and PC: Scale sizing, UIAspectRatio, safe areas, touch targets, controller focus. Use when creating or fixing Roblox UI.

Type: skill | Category: [[categories/cat-roblox|roblox]] | Source: [[sources/src-own|own]] | License: first-party
Repo file: `skills/roblox/rbx-ui/SKILL.md` (extra files, if any, sit beside it in the repo)

Related: [[S--own--rbx-visual]]

---
# Responsive Roblox UI

Code comments: none by default (see rbx-luau, Comments).

Most Roblox players are on phones. Design for a phone first, then enlarge.

1. Sizing: use `Scale` for size and position (`UDim2.fromScale`), `Offset` only for borders/padding. Add `UIAspectRatioConstraint` to icons and square buttons, `UISizeConstraint` to cap huge sizes on 4K, `UIScale` for global tweaks by `workspace.CurrentCamera.ViewportSize`.
2. Layout objects: `UIListLayout`, `UIGridLayout`, `UIPadding`, `UICorner`; use `AutomaticSize` for text-driven boxes instead of manual measuring.
3. Safe areas: set `ScreenGui.ScreenInsets = Enum.ScreenInsets.DeviceSafeInsets` (or CoreUISafeInsets) so phone notches and the Roblox top bar do not cover buttons. Keep a clear gap under the topbar.
4. Touch targets: at least about 44x44 px equivalent on the smallest supported screen; thumb-reachable actions near the bottom corners; no hover-only interactions.
5. Text: `TextScaled` with `UITextSizeConstraint` (min 12-14, a sane max); test long localized strings; high contrast against busy backgrounds.
6. Input: support touch, mouse and gamepad. Set `Selectable` and `SelectionImageObject`, use `GuiService.SelectedObject` to focus the first button for gamepad, handle `UserInputService.LastInputTypeChanged` to swap prompts (tap/click/A button).
7. State: build with one controller module per screen that owns show/hide and cleans up connections; do not leave invisible GUIs updating each frame. Set `ResetOnSpawn = false` for persistent HUD.
8. Test: Studio Device Emulator with at least a small phone, a tablet and 1080p; portrait and landscape; check overlap with Roblox chat, jump button and thumbstick.

9. Overlap: stack neighbouring panels in HUD slots with `UIListLayout` instead of hand-placing them; keep bottom-left and bottom-right free for touch controls; one popup, banner or hint at a time through a queue; DisplayOrder per layer (HUD < popups < toasts). Measure instead of guessing: `rbx-visual/scripts/ui_overlap.luau` reports overlaps, hidden elements, off-screen items and small or low-contrast text at phone 844x390, tablet 1180x820 and desktop 1920x1080. The ready component set is the StyleKit of `rbx-art`.

Output a screenshot checklist: device | screen | overlap/overflow | fix.
