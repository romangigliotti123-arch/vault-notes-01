---
title: "Docs: production / game-design / onboarding-techniques"
url: https://create.roblox.com/docs/production/game-design/onboarding-techniques.md
creator: Roblox Creator Docs
official: true
advice_density: high
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: production / game-design / onboarding-techniques

[Open](https://create.roblox.com/docs/production/game-design/onboarding-techniques.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Roblox official docs on onboarding techniques: three methods (visual elements, contextual/just-in-time tutorials, timed hints), with reasoning and examples from Color or Die, Hello Kitty Cafe, Jailbreak, Squishmallows, Plant, and Winds of Fortune. Notes Configs and Experiments for tuning timings.

## Tips
- [page](https://create.roblox.com/docs/production/game-design/onboarding-techniques) **[[first-session-onboarding]]** Use visual elements (arrows, highlights, particles, trails) instead of long text prompts; players skip text and rarely read instructions.
- [page](https://create.roblox.com/docs/production/game-design/onboarding-techniques) **[[first-session-onboarding]]** Place core-mechanic signs in the world in the player's line of sight, where they are unmissable but don't block starting the game.
- [page](https://create.roblox.com/docs/production/game-design/onboarding-techniques) **[[first-session-onboarding]]** Keep persistent hints on screen until the player completes the step, so exploration doesn't make them forget the objective.
- [page](https://create.roblox.com/docs/production/game-design/onboarding-techniques) **[[first-session-onboarding]]** Use directional trails or hints that suggest an action without forcing it, so the tutorial feels less forced and players keep choice.
- [page](https://create.roblox.com/docs/production/game-design/onboarding-techniques) **[[first-session-onboarding]]** Give immediate visual feedback for every player action (hit flashes, damage numbers, reward coins, quest counter updates) so players don't think the game is buggy.
- [page](https://create.roblox.com/docs/production/game-design/onboarding-techniques) **[[core-loops-and-game-design]]** Trigger tutorials just in time (on first encounter of a feature) instead of front-loading them in onboarding, to reduce cognitive load and speed up reaching fun.
- [page](https://create.roblox.com/docs/production/game-design/onboarding-techniques) **[[first-session-onboarding]]** Use contextual tutorials for non-core features (e.g. a marketplace) that only matter to mid/late-game players, and show them when the player finds the feature.
- [page](https://create.roblox.com/docs/production/game-design/onboarding-techniques) **[[retention-d1-d7]]** Use timed hints for struggling players to increase retention; they can become dedicated players if given well-timed support.
- [page](https://create.roblox.com/docs/production/game-design/onboarding-techniques) **[[playtesting-and-feedback]]** Set timed-hint delays from playtest data: e.g. if most players finish a step within 10 seconds, show the hint at 11 seconds.
- [page](https://create.roblox.com/docs/production/game-design/onboarding-techniques) **[[playtesting-and-feedback]]** Show each timed hint only once per task, and only after most players have completed it, so experienced players aren't annoyed.
- [page](https://create.roblox.com/docs/production/game-design/onboarding-techniques) **[[analytics-metrics]]** Track whether players who haven't used a feature (e.g. trade) after two sessions need a timed hint to surface it.
- [page](https://create.roblox.com/docs/production/game-design/onboarding-techniques) **[[analytics-metrics]]** A/B test hint timing with Experiments (e.g. 5s vs 10s) measuring funnel completion, then push the winner globally via Configs without restarting servers.
- [page](https://create.roblox.com/docs/production/game-design/onboarding-techniques) **[[ai-and-tools]]** Use Roblox Configs and Experiments to tune onboarding values live rather than hardcoding them.
- [page](https://create.roblox.com/docs/production/game-design/onboarding-techniques) **[[first-session-onboarding]]** Make visual hints in the world imply interactivity (e.g. footprints to escape routes) so players solve the problem and feel clever.

## Numbers
- [page](https://create.roblox.com/docs/production/game-design/onboarding-techniques) Example timed hint delay: **10 s before hint; hint at 11 s in Plant example** (Hypothetical: most playtesters press button within 10 seconds)
- [page](https://create.roblox.com/docs/production/game-design/onboarding-techniques) A/B test hint delay: **5 s vs 10 s** (Example Experiment comparing funnel completion)
- [page](https://create.roblox.com/docs/production/game-design/onboarding-techniques) Contextual combination example: **2 identical items trigger tutorial; 3 needed to combine** (Squishmallows combination station tutorial)
- [page](https://create.roblox.com/docs/production/game-design/onboarding-techniques) Marketplace stands: **3** (Plant selling stands where arrow hint could appear)

## Games
- **Color or Die**: Place core mechanic sign in player's line of sight at first pickup; prominent and doesn't block play.
- **Hello Kitty Cafe**: Spotlight target button, dim rest of screen, outline and arrow; leaves no doubt what to click next.
- **Jailbreak**: Use in-world visual hints like footprints to imply escape routes without explicit instructions.
- **Creatures of Sonaria**: Directional arrows and icons guide players in-world.
- **Winds of Fortune**: Combat feedback (VFX, damage numbers, health bars, reward coins, quest counters) teaches combat without a tutorial.
- **Squishmallows**: Contextual tutorials trigger on relevant state (duplicate items, first marketplace discovery) instead of in onboarding.
- **Plant**: Timed hints (highlight button, arrow at marketplace stall) shown only after most players complete the task.

## Tools
Roblox Configs, Roblox Experiments

## He points to
- Docs: UI and UX
- Video on color contrast (linked from docs)

## Quotes
- [page](https://create.roblox.com/docs/production/game-design/onboarding-techniques) "Players generally don't like to read instructions and skip through text prompts to get to gameplay."
- [page](https://create.roblox.com/docs/production/game-design/onboarding-techniques) "Contextual tutorials personalize instruction, which maximizes their relevance and utility within the broader onboarding funnel."
- [page](https://create.roblox.com/docs/production/game-design/onboarding-techniques) "Otherwise, players may not know that the action they took did anything, and wonder if they did something wrong, or wonder if the game is buggy."

## Topics
[[ai-and-tools]] [[analytics-metrics]] [[core-loops-and-game-design]] [[first-session-onboarding]] [[playtesting-and-feedback]] [[retention-d1-d7]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
