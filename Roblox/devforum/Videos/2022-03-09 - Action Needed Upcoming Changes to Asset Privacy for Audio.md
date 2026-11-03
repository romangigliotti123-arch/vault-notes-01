---
title: "[Action Needed] Upcoming Changes to Asset Privacy for Audio"
url: https://devforum.roblox.com/t/action-needed-upcoming-changes-to-asset-privacy-for-audio/1701697
creator: Roblox DevForum
official: false
advice_density: medium
date: 2022-03-09
views: 20981
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# [Action Needed] Upcoming Changes to Asset Privacy for Audio

[Open](https://devforum.roblox.com/t/action-needed-upcoming-changes-to-asset-privacy-for-audio/1701697) | Roblox DevForum | 20,981 views | 2022-03-09

## Summary
Roblox DevForum announcement (March 2022) on audio privacy changes: from March 22 new audio and existing audio over 6 seconds become Private, so experiences using others' audio break. Introduces the Audio Discovery plugin for auditing, free audio uploads with monthly limits, and the licensed music/SFX catalog as a replacement source.

## Tips
- [page](https://devforum.roblox.com/t/action-needed-upcoming-changes-to-asset-privacy-for-audio/1701697) **[[updates-live-ops]]** Update Studio and run the Audio Discovery plugin on every published experience; it only gives accurate results for published places.
- [page](https://devforum.roblox.com/t/action-needed-upcoming-changes-to-asset-privacy-for-audio/1701697) **[[common-mistakes]]** Do not rely on audio uploaded by other users or groups; it will stop working after privacy changes unless the audio is under 6 seconds or from Roblox/partners.
- [page](https://devforum.roblox.com/t/action-needed-upcoming-changes-to-asset-privacy-for-audio/1701697) **[[events-and-seasonal-content]]** Sound-triggered gameplay events will not fire if the sound fails to load due to privacy; replace those sounds or add fallback logic.
- [page](https://devforum.roblox.com/t/action-needed-upcoming-changes-to-asset-privacy-for-audio/1701697) **[[sound-and-music]]** Replace flagged audio with audio uploaded by your own user or group, or with Roblox licensed music and SFX catalog tracks.
- [page](https://devforum.roblox.com/t/action-needed-upcoming-changes-to-asset-privacy-for-audio/1701697) **[[sound-and-music]]** For radios or boomboxes, switch from ID-based playback to letting users pick from the Roblox licensed music catalog to avoid breakage.
- [page](https://devforum.roblox.com/t/action-needed-upcoming-changes-to-asset-privacy-for-audio/1701697) **[[updates-live-ops]]** Start the audio review now; upload queues are heavily loaded and approval times may be longer than expected.
- [page](https://devforum.roblox.com/t/action-needed-upcoming-changes-to-asset-privacy-for-audio/1701697) **[[common-mistakes]]** Private audio becoming Private cannot be reverted to public after March 22, so plan replacements rather than relying on toggling privacy back.

## Numbers
- [page](https://devforum.roblox.com/t/action-needed-upcoming-changes-to-asset-privacy-for-audio/1701697) Audio upload limit (default): **10 uploads per month**
- [page](https://devforum.roblox.com/t/action-needed-upcoming-changes-to-asset-privacy-for-audio/1701697) Audio upload limit (ID verified): **100 uploads per month**
- [page](https://devforum.roblox.com/t/action-needed-upcoming-changes-to-asset-privacy-for-audio/1701697) Privacy threshold: **Audio longer than 6 seconds becomes Private**
- [page](https://devforum.roblox.com/t/action-needed-upcoming-changes-to-asset-privacy-for-audio/1701697) Licensed music catalog: **More than 100,000 rights-cleared songs**
- [page](https://devforum.roblox.com/t/action-needed-upcoming-changes-to-asset-privacy-for-audio/1701697) Licensed SFX catalog: **More than 100,000 SFX**
- [page](https://devforum.roblox.com/t/action-needed-upcoming-changes-to-asset-privacy-for-audio/1701697) Privacy change date: **March 22, 2022**

## Tools
Audio Discovery plugin (Roblox Studio)

## He points to
- Roblox licensed music catalog and Monstercat collection

## Topics
[[common-mistakes]] [[events-and-seasonal-content]] [[sound-and-music]] [[updates-live-ops]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
