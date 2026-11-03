---
title: "Live Ops with the Notorious Creators of Jailbreak | RDC 2021"
url: https://youtu.be/bKvOPfp3oX0
creator: Roblox Creators
official: true
advice_density: high
date: 2021-12-01
views: 5157
transcript: auto-captions
confidence: high
tags: [roblox, mustwatch, youtube-learn]
---

# Live Ops with the Notorious Creators of Jailbreak | RDC 2021

[Watch](https://youtu.be/bKvOPfp3oX0) | MustWatch | 5,157 views | 2021-12-01

## Summary
Jailbreak devs (Badimo/Alex Balfans and Semo) explain running live events without shutting down: goal-setting via player feedback and Trello, sneaky alt accounts and code names, trigger methods (visit-count proxy via Google Cloud Function vs. scheduled UTC time using DateTime API), hiding code in ServerStorage, cutscene reuse, social hype via Twitter/YouTube teasers and in-game countdowns. Lessons from the 2018 Volcano event and the 2020 Oceans event (550k CCU).

## Tips
- [5:33](https://youtu.be/bKvOPfp3oX0?t=333) **[[updates-live-ops]]** Write down what players have asked for over years, edit into a plan, and organise it in a tool like Trello with deadlines to ship on time.
- [6:55](https://youtu.be/bKvOPfp3oX0?t=415) **[[common-mistakes]]** Keep event asset names and alt-account names different from your normal naming scheme so the event cannot be found by searching the catalog.
- [8:49](https://youtu.be/bKvOPfp3oX0?t=529) **[[updates-live-ops]]** Trigger live events at a fixed UTC date/time using DateTime API rather than tick(), since tick() desyncs across servers (some were minutes late).
- [10:52](https://youtu.be/bKvOPfp3oX0?t=652) **[[scripting-and-performance]]** Hide event code in ServerStorage until launch, then copy it to ReplicatedStorage on the countdown event so exploiters cannot read it beforehand.
- [13:21](https://youtu.be/bKvOPfp3oX0?t=801) **[[updates-live-ops]]** Build live events as cutscenes reusing existing modules (nuke, rain, typewriter); sloppy code is acceptable since the map can reset itself.
- [14:06](https://youtu.be/bKvOPfp3oX0?t=846) **[[community-and-discord]]** Tweet regularly, starting about 10 days before the event, using a unique hashtag and always including date and time.
- [14:48](https://youtu.be/bKvOPfp3oX0?t=888) **[[ads-and-sponsored-experiences]]** Release teaser trailers on YouTube and share them on Twitter; reveal the story but not the event itself, and end each trailer with date and time.
- [17:05](https://youtu.be/bKvOPfp3oX0?t=1025) **[[first-session-onboarding]]** Place a countdown above the event location and guide players there so they do not miss the event.
- [17:05](https://youtu.be/bKvOPfp3oX0?t=1025) **[[community-and-discord]]** Seed clues for YouTubers and streamers to find and discuss without giving away the update.
- [17:50](https://youtu.be/bKvOPfp3oX0?t=1070) **[[common-mistakes]]** Do not sink or change the map with a countdown at an unclear location; players got lost and did not know where to look.
- [18:32](https://youtu.be/bKvOPfp3oX0?t=1112) **[[updates-live-ops]]** Keep event length short (the 10-15 minute event felt dead); players thought it had broken when little happened.
- [18:32](https://youtu.be/bKvOPfp3oX0?t=1112) **[[playtesting-and-feedback]]** Gather feedback after every event to improve the next one.
- [19:14](https://youtu.be/bKvOPfp3oX0?t=1154) **[[updates-live-ops]]** Trigger on a fixed time that suits your main audience's timezone; a 6am PST trigger for the 2 billion visit event drew few players.
- [19:57](https://youtu.be/bKvOPfp3oX0?t=1197) **[[development-process-and-speed]]** Predict trigger timing by monitoring player counts; they ramp up with excitement, so watch closely near the expected moment.

## Numbers
- [1:23](https://youtu.be/bKvOPfp3oX0?t=83) concurrent players increase from live event: **over 500%** (Jailbreak live event boost per presenter)
- [8:07](https://youtu.be/bKvOPfp3oX0?t=487) Volcano event trigger: **2 billion plays** (Triggered around 2017 via Google Cloud Function visit proxy)
- [18:32](https://youtu.be/bKvOPfp3oX0?t=1112) Volcano event trigger time: **6am PST on Nov 8 2018** (Poor turnout due to impractical time for NA players)
- [19:57](https://youtu.be/bKvOPfp3oX0?t=1197) Oceans event peak concurrent players: **over 550,000** (Previous record about 20-some thousand; hit top of front page)
- [14:06](https://youtu.be/bKvOPfp3oX0?t=846) Pre-event tweeting schedule: **daily for about 10 days** (Before Oceans event)
- [15:29](https://youtu.be/bKvOPfp3oX0?t=929) Teaser trailers produced: **3 (2 teasers + 1 final update trailer)** (Oceans event hype campaign)

## Games
- **Jailbreak** [4:57](https://youtu.be/bKvOPfp3oX0?t=297): Used live events (2018 Volcano, 2020 Oceans) to turn the map into a world and hit 550k CCU; alt accounts and code names kept reveal secret.
- **Jailbreak** [17:50](https://youtu.be/bKvOPfp3oX0?t=1070): 2018 Volcano event failed due to unclear countdown location and too-long event; the 2020 Oceans event worked after learning this.

## Tools
Trello, Twitter, YouTube, Google Cloud Function, Roblox DateTime API, Roblox HttpService, Roblox Developer API (game stats)

## He points to
- Community-supported Jailbreak wiki

## Quotes
- [1:23](https://youtu.be/bKvOPfp3oX0?t=83) "Live ops engages the entire Roblox community: existing players, new players following them in, and reactivating older players."
- [8:07](https://youtu.be/bKvOPfp3oX0?t=487) "The magic of a live event is that the event runs and modifies the game without ever shutting down."

## Topics
[[ads-and-sponsored-experiences]] [[common-mistakes]] [[community-and-discord]] [[development-process-and-speed]] [[first-session-onboarding]] [[playtesting-and-feedback]] [[scripting-and-performance]] [[updates-live-ops]]

Back to [[MustWatch - How to make successful Roblox games]]
