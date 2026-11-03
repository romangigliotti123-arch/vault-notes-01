---
title: "How to use Promises (and why you should) in Roblox Development"
url: https://youtu.be/TeMGAqzZrDc
creator: B Ricey
official: false
advice_density: medium
date: 2022-06-19
views: 46283
transcript: auto-captions
confidence: high
tags: [roblox, bricey, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.0
---

> [!note] Trust: TRUSTED (credibility audit score 8.0): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# How to use Promises (and why you should) in Roblox Development

[Watch](https://youtu.be/TeMGAqzZrDc) | BRicey | 46,283 views | 2022-06-19

## Summary
Tutorial on the Promise library for Roblox. Shows a cancellable delay tied to a part's Destroying event, chaining promises with andThen, finally and catch so an error doesn't break a round loop, and wrapping TweenService in a promise with cancel and resolve hooks.

## Tips
- [2:44](https://youtu.be/TeMGAqzZrDc?t=164) **[[code-architecture-and-frameworks]]** Use Promise.delay instead of task.delay when the delayed action depends on an object; cancel the promise on the part's Destroying event to avoid errors and stray state changes.
- [5:26](https://youtu.be/TeMGAqzZrDc?t=326) **[[data-persistence]]** Give promises to Trove or Janitor so cleanup automatically cancels pending delays when a vehicle or part is torn down.
- [7:19](https://youtu.be/TeMGAqzZrDc?t=439) **[[scripting-and-performance]]** Don't run a round loop as a bare while-true; a single runtime error breaks the whole loop. Chain stages with promises so errors are caught and cleanup still runs.
- [11:31](https://youtu.be/TeMGAqzZrDc?t=691) **[[testing-debugging-and-qa]]** Add a catch block at the end of a promise chain to warn or log errors with a clean stack, and optionally send them to AnalyticsService.
- [14:18](https://youtu.be/TeMGAqzZrDc?t=858) **[[code-architecture-and-frameworks]]** Wrap yielding Roblox APIs like TweenService in Promise.new, using resolve, reject and onCancel to hook completion and cancellation.
- [17:18](https://youtu.be/TeMGAqzZrDc?t=1038) **[[code-architecture-and-frameworks]]** Wrapping tweens in promises lets you cancel, retween and reset cleanly instead of juggling raw Tween:Cancel calls.

## Tools
Promise library (promise.lua from GitHub releases), Trove, Janitor, TweenService

## He points to
- Promise library GitHub repository and documentation (linked in video description)

## Quotes
- [18:15](https://youtu.be/TeMGAqzZrDc?t=1095) "Promises can be used by anyone as long as you know when they can use them."

## Topics
[[code-architecture-and-frameworks]] [[data-persistence]] [[scripting-and-performance]] [[testing-debugging-and-qa]]

Back to [[BRicey - How to make successful Roblox games]]
