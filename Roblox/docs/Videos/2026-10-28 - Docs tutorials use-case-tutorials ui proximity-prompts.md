---
title: "Docs: tutorials / use-case-tutorials / ui / proximity-prompts"
url: https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/proximity-prompts.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: tutorials / use-case-tutorials / ui / proximity-prompts

[Open](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/proximity-prompts.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Official Roblox docs tutorial on proximity prompts: creating a ProximityPrompt on an Attachment, configuring ObjectText/ActionText, key codes, MaxActivationDistance and HoldDuration, and handling prompt events centrally via ProximityPromptService using the Dungeon Delve project as an example.

## Tips
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/proximity-prompts) **[[building-and-level-design]]** Parent ProximityPrompts to an Attachment rather than directly to the part or model to control exactly where the interaction point sits.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/proximity-prompts) **[[scripting-and-performance]]** Handle prompt events centrally with ProximityPromptService (PromptTriggered, PromptButtonHoldBegan, PromptButtonHoldEnded) instead of attaching a script to each prompt object.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/proximity-prompts) **[[scripting-and-performance]]** Keep event handlers thin: have the service script call functions in a ModuleScript (e.g. ObjectActions) so action logic stays in one reusable place.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/proximity-prompts) **[[core-loops-and-game-design]]** Set HoldDuration above zero for actions that should feel deliberate (e.g. picking a lock); PromptTriggered fires only after the hold completes.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/proximity-prompts) **[[first-session-onboarding]]** Use clear ObjectText and ActionText labels (e.g. 'Door' / 'Pick Lock') so players know what the prompt does.
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/proximity-prompts) **[[ui-ux-design]]** Tune MaxActivationDistance per object (example: 4 studs for a lock) to push interaction closer to the target instead of relying on the default.

## Numbers
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/proximity-prompts) MaxActivationDistance: **4 (example for lock door; default works in most cases)** (Tutorial example value for prison door prompt)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/proximity-prompts) HoldDuration: **4 seconds** (Tutorial example for picking a lock)
- [page](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/proximity-prompts) Attachment Position offset: **-2.25, -0.5, -0.5** (Tutorial example placing prompt in front of keyhole)

## Games
- **Dungeon Delve**: Official showcase project for the tutorial; prompt events routed through PromptEvents script to an ObjectActions ModuleScript.

## Tools
Roblox Studio, ProximityPrompt, ProximityPromptService, Attachment, ModuleScript

## He points to
- Class.ProximityPrompt reference
- Class.ProximityPromptService reference

## Topics
[[building-and-level-design]] [[core-loops-and-game-design]] [[first-session-onboarding]] [[scripting-and-performance]] [[ui-ux-design]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
