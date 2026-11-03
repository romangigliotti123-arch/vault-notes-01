---
title: "Client Anti Cheats: Aren't as bad as you think!"
url: https://devforum.roblox.com/t/client-anti-cheats-arent-as-bad-as-you-think/2471974
creator: Roblox DevForum
official: false
advice_density: medium
date: 2023-07-16
views: 599
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Client Anti Cheats: Aren't as bad as you think!

[Open](https://devforum.roblox.com/t/client-anti-cheats-arent-as-bad-as-you-think/2471974) | Roblox DevForum | 599 views | 2023-07-16

## Summary
DevForum tutorial arguing client-side anti-cheats are viable as a secondary defense. Shows hiding a script via getfenv().script (removing it from Dex and nil instances), and a RemoteEvent handshake loop where the server kicks clients that stop reporting within a timeout. Notes that keys/encryption are needed to stop replication.

## Tips
- [page](https://devforum.roblox.com/t/client-anti-cheats-arent-as-bad-as-you-think/2471974) **[[anti-exploit-and-security]]** Treat the client as a secondary defence; keep the server as the main security focus and validate everything there.
- [page](https://devforum.roblox.com/t/client-anti-cheats-arent-as-bad-as-you-think/2471974) **[[anti-exploit-and-security]]** Hide the client anti-cheat script by setting getfenv().script to nil after destroying it so it does not appear in Dex or getnilinstances().
- [page](https://devforum.roblox.com/t/client-anti-cheats-arent-as-bad-as-you-think/2471974) **[[anti-exploit-and-security]]** Implement a handshake: client fires a RemoteEvent every few seconds; server kicks players whose last handshake is older than the timeout (example uses 30s).
- [page](https://devforum.roblox.com/t/client-anti-cheats-arent-as-bad-as-you-think/2471974) **[[anti-exploit-and-security]]** Use keys and encryption in handshakes so exploiters cannot simply replicate the FireServer loop; a plain FireServer is only a demo.
- [page](https://devforum.roblox.com/t/client-anti-cheats-arent-as-bad-as-you-think/2471974) **[[anti-exploit-and-security]]** Combine client anti-cheat with server anti-cheat; the combination is stronger than either alone.
- [page](https://devforum.roblox.com/t/client-anti-cheats-arent-as-bad-as-you-think/2471974) **[[anti-exploit-and-security]]** Consider tamper checks such as property spoofing and namecall tampering detection for further client protection.

## Numbers
- [page](https://devforum.roblox.com/t/client-anti-cheats-arent-as-bad-as-you-think/2471974) Handshake interval: **every 5 seconds (task.wait(5))** (Client fires handshake RemoteEvent in this loop)
- [page](https://devforum.roblox.com/t/client-anti-cheats-arent-as-bad-as-you-think/2471974) Kick timeout: **30 seconds** (Server kicks if no handshake received within this window)

## Tools
Dex Explorer, getnilinstances

## He points to
- HexadecimalLiker (DevForum helper)

## Quotes
- [page](https://devforum.roblox.com/t/client-anti-cheats-arent-as-bad-as-you-think/2471974) "I bet that 90% of the DevForums users who make these claims have never actually attempted to create an anti-exploit system themselves."
- [page](https://devforum.roblox.com/t/client-anti-cheats-arent-as-bad-as-you-think/2471974) "Client anti-cheats are actually good, especially when combined with server anti-cheats."

## Topics
[[anti-exploit-and-security]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
