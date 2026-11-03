---
title: "Creating a Crate/Spin System"
url: https://devforum.roblox.com/t/creating-a-cratespin-system/260895
creator: Roblox DevForum
official: false
advice_density: medium
date: 2019-04-01
views: 589
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Creating a Crate/Spin System

[Open](https://devforum.roblox.com/t/creating-a-cratespin-system/260895) | Roblox DevForum | 589 views | 2019-04-01

## Summary
ForeverHD's DevForum tutorial on building a Roblox crate/spin system. Covers client request validation, server-side random item generation via weighted rarity tables, duplicate handling, and a TweenService-driven spinner UI that moves a single holder frame instead of individual crates.

## Tips
- [page](https://devforum.roblox.com/t/creating-a-cratespin-system/260895) **[[monetisation-other]]** Never generate spin results on the client; generate and reward on the server, since clients can be exploited to request any item.
- [page](https://devforum.roblox.com/t/creating-a-cratespin-system/260895) **[[anti-exploit-and-security]]** Put the permission check in a shared ModuleScript so client and server run the same validation, but always re-verify on the server.
- [page](https://devforum.roblox.com/t/creating-a-cratespin-system/260895) **[[client-server-and-remotes]]** Use a RemoteFunction for the spin request; server verifies funds, deducts cost, generates results, and returns data for the client animation.
- [page](https://devforum.roblox.com/t/creating-a-cratespin-system/260895) **[[combat-and-gameplay-systems]]** Generate the full batch of spin items (e.g. 45) and pick the winner at a fixed index (e.g. 5 from the end) so the spinner looks like it has more to come.
- [page](https://devforum.roblox.com/t/creating-a-cratespin-system/260895) **[[combat-and-gameplay-systems]]** Make sure rarity chances sum to exactly 1, since weighted selection relies on cumulative chance.
- [page](https://devforum.roblox.com/t/creating-a-cratespin-system/260895) **[[combat-and-gameplay-systems]]** Convert duplicate items into a cash reward per rarity instead of granting them again, and remove owned items from the pool if you want new-item-only spins.
- [page](https://devforum.roblox.com/t/creating-a-cratespin-system/260895) **[[optimization-and-streaming]]** Pre-create crate UI clones once when the player joins and toggle their contents per spin rather than regenerating them each spin.
- [page](https://devforum.roblox.com/t/creating-a-cratespin-system/260895) **[[optimization-and-streaming]]** Do not update each crate's position every frame in a loop; animate only the holder frame with TweenService and an easing style like Quart.
- [page](https://devforum.roblox.com/t/creating-a-cratespin-system/260895) **[[ui-ux-design]]** Set ClipsDescendants to true on the spinner's border frame so crates stay clipped inside the spinner window.
- [page](https://devforum.roblox.com/t/creating-a-cratespin-system/260895) **[[ui-ux-design]]** Add a debounce and loading/error text on the spin button to prevent double-spinning and to show failed requests.
- [page](https://devforum.roblox.com/t/creating-a-cratespin-system/260895) **[[sound-and-music]]** Play a tick sound effect as each crate passes the centre line to add feedback during the spin.

## Numbers
- [page](https://devforum.roblox.com/t/creating-a-cratespin-system/260895) Crates generated per spin: **45 (winner at 40th, 5 from end)** (Server-generated strip; client spins through crates before landing on winner)
- [page](https://devforum.roblox.com/t/creating-a-cratespin-system/260895) Example rarity chances: **Common 0.589, Uncommon 0.300, Rare 0.100, Legendary 0.010, Mythical 0.001** (Sample tiers in tutorial; must sum to 1)
- [page](https://devforum.roblox.com/t/creating-a-cratespin-system/260895) Duplicate cash rewards by rarity: **Common 20, Uncommon 50, Rare 100, Legendary 200, Mythical 500** (Cash granted when a duplicate item is rolled)
- [page](https://devforum.roblox.com/t/creating-a-cratespin-system/260895) Spin duration: **7-8 seconds random via math.random(7,8)** (TweenInfo time with Quart easing)
- [page](https://devforum.roblox.com/t/creating-a-cratespin-system/260895) Crate gap: **10 pixels between crates** (Spacing computed from AbsoluteSize.X plus gap)
- [page](https://devforum.roblox.com/t/creating-a-cratespin-system/260895) Error message display: **1 second** (wait(1) before resetting button text after error)

## Tools
TweenService, RemoteFunction, ModuleScript, leaderstats

## He points to
- Crate/Spin System open-source place by ForeverHD

## Quotes
- [page](https://devforum.roblox.com/t/creating-a-cratespin-system/260895) "Often, inexperienced developers will generate the items on the client then request the server to give them that particular item. This is a huge no no... Never trust the client."
- [page](https://devforum.roblox.com/t/creating-a-cratespin-system/260895) "Please please please do not do this! Using a loop and updating the position of each individual crate over 30 times a second."

## Topics
[[anti-exploit-and-security]] [[client-server-and-remotes]] [[combat-and-gameplay-systems]] [[monetisation-other]] [[optimization-and-streaming]] [[sound-and-music]] [[ui-ux-design]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
