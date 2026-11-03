---
title: "Roblox Deferred Engine Events - How Are Signals Impacted?"
url: https://youtu.be/xz_G2n1Q8-U
creator: Crusherfire
official: false
advice_density: low
date: 2024-01-23
views: 9241
transcript: auto-captions
confidence: high
tags: [roblox, crusherfiredev, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.7
---

> [!note] Trust: TRUSTED (credibility audit score 8.7): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# Roblox Deferred Engine Events - How Are Signals Impacted?

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Watch](https://youtu.be/xz_G2n1Q8-U) | crusherfiredev | 9,241 views | 2024-01-23

## Summary
Explains Roblox's shift from immediate to deferred engine event signaling (Nov 2023 rollout, Workspace SignalBehavior property). Demonstrates via bindable event tests that deferred callbacks run later in the frame, breaking expectations for destroying/CharacterRemoving events where the instance is already gone. Calls for Roblox to fix this.

## Tips
- [2:46](https://youtu.be/xz_G2n1Q8-U?t=166) **[[code-architecture-and-frameworks]]** Check Workspace.SignalBehavior (Default/Immediate/Deferred) in every project; know which mode your game uses before debugging event order.
- [5:23](https://youtu.be/xz_G2n1Q8-U?t=323) **[[luau-language-and-types]]** Under deferred signals, don't assume a handler connected inside another handler has run yet; events fired in a callback queue behind already-queued callbacks.
- [12:20](https://youtu.be/xz_G2n1Q8-U?t=740) **[[common-mistakes]]** Don't rely on CharacterRemoving or DescendantRemoving to read the instance's parent; under deferred mode it may already be nil by the time the callback runs.
- [12:20](https://youtu.be/xz_G2n1Q8-U?t=740) **[[scripting-and-performance]]** For cleanup that needs the instance still in the world, do it before triggering the removal rather than in a removing/destroying callback.

## Numbers
- [0:00](https://youtu.be/xz_G2n1Q8-U?t=0) Deferred engine events rollout: **Announced Nov 2023; new games default to deferred; default workspace setting switches to deferred Feb 2024**
- [8:54](https://youtu.be/xz_G2n1Q8-U?t=534) Test frame: **Bindable tests fired at frame 100 of Heartbeat count**

## Tools
Roblox Studio, RBXScriptSignal / BindableEvent, Workspace.SignalBehavior property

## Topics
[[code-architecture-and-frameworks]] [[common-mistakes]] [[luau-language-and-types]] [[scripting-and-performance]]

Back to [[crusherfiredev - How to make successful Roblox games]]
