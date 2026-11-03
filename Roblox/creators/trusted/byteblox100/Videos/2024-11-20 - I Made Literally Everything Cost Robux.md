---
title: "I Made Literally Everything Cost Robux"
url: https://youtu.be/Jl0SdXksQsI
creator: ByteBlox
official: false
advice_density: low
date: 2024-11-20
views: 164263
transcript: auto-captions
confidence: high
tags: [roblox, byteblox100, youtube-learn]
creator_trust: TRUSTED
creator_score: 8.1
---

> [!note] Trust: TRUSTED (credibility audit score 8.1): usable as a primary source; official Roblox docs still win on numbers and limits. See [[creator-credibility]].

# I Made Literally Everything Cost Robux

> Tagged **low-advice**: mostly entertainment/experiment; notes kept short.
[Watch](https://youtu.be/Jl0SdXksQsI) | byteblox100 | 164,263 views | 2024-11-20

## Summary
Satirical experiment: a Roblox prototype that charges Robux for walking, jumping and camera movement, built with DevProducts, MarketplaceService prompts and LocalScripts. The creator says it violates Roblox ToS and deletes it. He also estimates revenue per average 40-minute session, which the video presents as a pitfall rather than a model to follow.

## Tips
- [2:03](https://youtu.be/Jl0SdXksQsI?t=123) **[[monetisation-devproducts]]** Use developer products for repeatable purchases and gamepasses for one-time unlocks. Products can be bought many times; gamepasses only once.
- [4:46](https://youtu.be/Jl0SdXksQsI?t=286) **[[scripting-and-performance]]** Check the isPurchased flag from PromptProductFinished and return early if false. Players can close the purchase prompt without buying.
- [14:20](https://youtu.be/Jl0SdXksQsI?t=860) **[[scripting-and-performance]]** Reset camera type to Custom at script start and after a failed purchase. Otherwise a rejected prompt can leave the camera stuck in Scriptable forever.
- [8:09](https://youtu.be/Jl0SdXksQsI?t=489) **[[luau-language-and-types]]** Add a type annotation like :Humanoid to variables so the editor autofills the properties (WalkSpeed, JumpHeight) instead of typing them by hand.

## Numbers
- [17:27](https://youtu.be/Jl0SdXksQsI?t=1047) Walk unlock price: **20 Robux for 10 seconds of walking**
- [17:27](https://youtu.be/Jl0SdXksQsI?t=1047) Jump unlock price: **30 Robux for 10 seconds of jumping**
- [17:27](https://youtu.be/Jl0SdXksQsI?t=1047) Camera unlock price: **50 Robux for 10 seconds of camera movement**
- [18:09](https://youtu.be/Jl0SdXksQsI?t=1089) Robux cost per 10-second window: **100 Robux combined**

## Games
- **Adopt Me** [0:48](https://youtu.be/Jl0SdXksQsI?t=48): Monetization is handled carefully; purchases are optional extras after the game is fun.
- **Pet Simulator** [1:29](https://youtu.be/Jl0SdXksQsI?t=89): Monetization is handled carefully; the game earns trust before asking for money.
- **DOORS** [1:29](https://youtu.be/Jl0SdXksQsI?t=89): Monetization is handled carefully; paid items don't block core play.

## Tools
Roblox Studio, Luau, MarketplaceService (PromptProductPurchase, PromptProductFinished), UserInputService

## Topics
[[analytics-metrics]] [[common-mistakes]] [[luau-language-and-types]] [[monetisation-devproducts]] [[monetisation-other]] [[scripting-and-performance]]

Back to [[byteblox100 - How to make successful Roblox games]]
