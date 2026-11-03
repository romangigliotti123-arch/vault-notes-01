---
title: "How to make a LIVE EVENT - Roblox Tutorial"
url: https://youtu.be/spFZ44yqIII
creator: AlvinBlox
official: false
advice_density: medium
date: 2020-06-01
views: 182485
transcript: auto-captions
confidence: high
tags: [roblox, alvinblox, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.1
---

> [!note] Trust: TRUSTED (credibility audit score 8.1): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# How to make a LIVE EVENT - Roblox Tutorial

[Watch](https://youtu.be/spFZ44yqIII) | AlvinBlox | 182,485 views | 2020-06-01

## Summary
Tutorial on building timed live events in Roblox scripts using os.time() Unix timestamps. Converts a human date/time to epoch seconds via epochconverter.com, sets time-to-start and time-to-stop values, loops checking the clock, and triggers an event (rocket launch demo). Also explains that stop time limits the event in new servers.

## Tips
- [0:22](https://youtu.be/spFZ44yqIII?t=22) **[[core-loops-and-game-design]]** Schedule live events by comparing os.time() (Unix seconds) against a start timestamp in a while loop, firing the event once the start time is reached.
- [5:33](https://youtu.be/spFZ44yqIII?t=333) **[[updates-live-ops]]** Set a time-to-stop value so new servers opened after the event window stop playing it; start and stop are both epoch timestamps.
- [5:11](https://youtu.be/spFZ44yqIII?t=311) **[[updates-live-ops]]** Convert a human date to an epoch timestamp with a converter site, and set the timezone correctly (AM/PM, local time) to avoid wrong event times.
- [8:18](https://youtu.be/spFZ44yqIII?t=498) **[[scripting-and-performance]]** Countdown to an event: subtract os.time() from the start timestamp to get seconds remaining.

## Numbers
- [1:42](https://youtu.be/spFZ44yqIII?t=102) Unix epoch start: **00:00:00 UTC, 1 January 1970** (os.time() counts seconds since this epoch)
- [3:46](https://youtu.be/spFZ44yqIII?t=226) Seconds per 10 minutes: **600** (Add seconds to current os.time() to schedule a future time)

## Tools
os.time() (Luau), epochconverter.com (human date to Unix timestamp), Roblox Studio output window

## He points to
- Epoch Converter website

## On screen
Contact sheet shows Studio output printing os.time() values, EpochConverter.com converting dates to timestamps, a calculator computing seconds remaining, and a countdown in output ("Time till live event"). A rocket model appears in the baseplate demo.

## Topics
[[core-loops-and-game-design]] [[scripting-and-performance]] [[updates-live-ops]]

Back to [[AlvinBlox - How to make successful Roblox games]]
