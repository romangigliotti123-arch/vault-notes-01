---
title: "Tech Talks EP29: Creator"
url: https://youtu.be/6iB5__RCQDc
creator: Roblox
official: true
advice_density: medium
date: 2025-09-05
views: 79701
transcript: auto-captions
confidence: high
tags: [roblox, robloxofficial, youtube-learn]
---

# Tech Talks EP29: Creator

[Watch](https://youtu.be/6iB5__RCQDc) | RobloxOfficial | 79,701 views | 2025-09-05

## Summary
Roblox Tech Talks EP29 with SVP engineering Nick Touro and Grow a Garden creator Jandelle. Covers Grow a Garden's success drivers (offline growth, weekly updates, low-pressure catch-up), Roblox scale (45M+ CCU, cloud bursting), studio real-time collaboration, cross-device rendering/streaming, AI tooling in Studio, update cadence, A/B testing limits, and upcoming server authority features.

## Tips
- [4:46](https://youtu.be/6iB5__RCQDc?t=286) **[[core-loops-and-game-design]]** Let progress accrue while players are offline (e.g., plants grow while away) so returning after hours or days feels rewarding.
- [5:27](https://youtu.be/6iB5__RCQDc?t=327) **[[core-loops-and-game-design]]** Keep chase goals reachable for most players so missing a week doesn't leave someone behind; they can rejoin the next update.
- [32:12](https://youtu.be/6iB5__RCQDc?t=1932) **[[social-features-and-virality]]** Build altruistic social mechanics, such as letting players place sprinklers on others' plots or gift expensive items to newcomers, to drive delight and retention.
- [32:12](https://youtu.be/6iB5__RCQDc?t=1932) **[[retention-d1-d7]]** Avoid pressure to log in daily; a game that is fun to return to after two weeks retains players without manipulative hooks.
- [19:21](https://youtu.be/6iB5__RCQDc?t=1161) **[[social-features-and-virality]]** Use live events and global chat/messaging features; Jandelle expected live events to scale strongly when retention is good.
- [39:23](https://youtu.be/6iB5__RCQDc?t=2363) **[[updates-live-ops]]** Ship small, frequent content updates; Grow a Garden updates weekly for 3-4 years, arguing stale games shouldn't be rewarded.
- [42:52](https://youtu.be/6iB5__RCQDc?t=2572) **[[development-process-and-speed]]** Use Studio's one-click multi-platform deploy (iOS, Android, Mac, PC, console, VR) to ship a new version in under 30 minutes.
- [46:33](https://youtu.be/6iB5__RCQDc?t=2793) **[[analytics-metrics]]** A/B testing breaks at scale: at about 0.5-1M players, analytics queries became too expensive and data unreliable; Grow a Garden switched to player-feedback-driven decisions.
- [46:33](https://youtu.be/6iB5__RCQDc?t=2793) **[[playtesting-and-feedback]]** Gather structured player feedback and build tooling for it when A/B testing is no longer viable.
- [23:26](https://youtu.be/6iB5__RCQDc?t=1406) **[[development-process-and-speed]]** Use Roblox native tools (Studio with drafts) for maximum velocity; minimize external IDEs and tooling to cut friction.
- [23:26](https://youtu.be/6iB5__RCQDc?t=1406) **[[development-process-and-speed]]** Enable drafts (branching) once team grows beyond ~10 engineers so one buggy change doesn't block everyone.
- [36:50](https://youtu.be/6iB5__RCQDc?t=2210) **[[ai-and-tools]]** Use Studio's AI assistant for tedious work: scatter thousands of trees, generate meshes from prompts, convert Blender avatars, and code completion.
- [49:39](https://youtu.be/6iB5__RCQDc?t=2979) **[[roblox-platform-changes]]** Roblox is rolling out easier server-authoritative tooling to stop cheating; Jandelle says anti-cheat consumes most dev time.
- [43:33](https://youtu.be/6iB5__RCQDc?t=2613) **[[analytics-metrics]]** Use built-in experiments in Creator Hub and Studio to run A/B tests that control for confounding variables when changing things serially.

## Numbers
- [3:23](https://youtu.be/6iB5__RCQDc?t=203) Grow a Garden team size: **~30 engineers (up from 10)**
- [15:17](https://youtu.be/6iB5__RCQDc?t=917) Grow a Garden early concurrency: **2M players then 22M a month later**
- [7:12](https://youtu.be/6iB5__RCQDc?t=432) Roblox peak concurrent users: **over 45 million in a weekend**
- [46:33](https://youtu.be/6iB5__RCQDc?t=2793) A/B testing cutoff for Grow a Garden: **~500K-1M players**
- [3:23](https://youtu.be/6iB5__RCQDc?t=203) Grow a Garden update cadence: **weekly for 3-4 years**
- [42:52](https://youtu.be/6iB5__RCQDc?t=2572) Deploy to all platforms from Studio: **under 30 minutes**
- [47:38](https://youtu.be/6iB5__RCQDc?t=2858) Future concurrency target mentioned: **50 million concurrent for live event**
- [12:35](https://youtu.be/6iB5__RCQDc?t=755) Future scale spec discussed: **100,000+ concurrent players in one stadium**

## Games
- **Grow a Garden** [0:03](https://youtu.be/6iB5__RCQDc?t=3): Offline growth, weekly updates, low-pressure catch-up, and altruistic player interactions drove record concurrency; built from a 16-year-old creator's original.
- **Farmville** [6:08](https://youtu.be/6iB5__RCQDc?t=368): Early asynchronous social farming game; Grow a Garden was loosely inspired, though its original creator hadn't heard of it.
- **Wacky Wizards** [19:21](https://youtu.be/6iB5__RCQDc?t=1161): Jandelle's earlier game where he tested global chat and live events, learning their effectiveness before Grow a Garden.
- **Gunfight Arena** [51:01](https://youtu.be/6iB5__RCQDc?t=3061): Showcased at RDC as an example where server authority would help competitive, anti-cheat-sensitive play.

## Tools
Roblox Studio, Studio AI assistant, Creator Hub experiments, Roblox messaging/global chat, Git (via plugin, Grow a Garden team)

## He points to
- RDC (Roblox Developers Conference) announcements
- Apollo 13 (analogy for systems checks)

## Quotes
- [32:12](https://youtu.be/6iB5__RCQDc?t=1932) "It's actually fun to come back in two weeks and you're not under pressure to come back every day."
- [46:33](https://youtu.be/6iB5__RCQDc?t=2793) "The game got so big there was actually no solutions for us to AB test anymore."
- [39:23](https://youtu.be/6iB5__RCQDc?t=2363) "I don't think that not updating your game on 6 months on the platform should be rewarded."

## Topics
[[ai-and-tools]] [[analytics-metrics]] [[core-loops-and-game-design]] [[development-process-and-speed]] [[playtesting-and-feedback]] [[retention-d1-d7]] [[roblox-platform-changes]] [[social-features-and-virality]] [[updates-live-ops]]

Back to [[RobloxOfficial - How to make successful Roblox games]]
