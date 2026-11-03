---
title: "Docs: ui / proximity-prompts"
url: https://create.roblox.com/docs/ui/proximity-prompts.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: ui / proximity-prompts

[Open](https://create.roblox.com/docs/ui/proximity-prompts.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox official docs on ProximityPrompt: creating prompts under parts/models/attachments, customizing appearance (ObjectText, ActionText, key codes), visibility (MaxActivationDistance, RequiresLineOfSight, Exclusivity modes), interactivity (HoldDuration, ClickablePrompt), and scripting via ProximityPromptService events.

## Tips
- [page](https://create.roblox.com/docs/ui/proximity-prompts) **[[ui-ux-design]]** Set ObjectText and ActionText so players know what the object is and what pressing the key will do.
- [page](https://create.roblox.com/docs/ui/proximity-prompts) **[[ui-ux-design]]** Use Exclusivity OneGlobally when several prompts sit in one area to reduce prompt clutter.
- [page](https://create.roblox.com/docs/ui/proximity-prompts) **[[ui-ux-design]]** Avoid AlwaysShow unless needed: all visible prompts with the same keycode fire on one keypress.
- [page](https://create.roblox.com/docs/ui/proximity-prompts) **[[cross-platform-and-console]]** Set KeyboardKeyCode and GamepadKeyCode; Roblox shows the correct input glyph per device type.
- [page](https://create.roblox.com/docs/ui/proximity-prompts) **[[cross-platform-and-console]]** Phones and tablets can always tap a prompt, regardless of ClickablePrompt; plan touch input accordingly.
- [page](https://create.roblox.com/docs/ui/proximity-prompts) **[[client-server-and-remotes]]** Connect prompt events via ProximityPromptService globally rather than duplicating handlers on each prompt.
- [page](https://create.roblox.com/docs/ui/proximity-prompts) **[[scripting-and-performance]]** Use HoldDuration of 0 for instant actions; non-zero values require hold-event handling (PromptButtonHoldBegan/Ended).

## Games
- **Dungeon Delve**: Official sample place with fully working proximity prompt examples.

## Tools
ProximityPrompt, ProximityPromptService

## He points to
- Dungeon Delve sample place

## Topics
[[client-server-and-remotes]] [[cross-platform-and-console]] [[scripting-and-performance]] [[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
