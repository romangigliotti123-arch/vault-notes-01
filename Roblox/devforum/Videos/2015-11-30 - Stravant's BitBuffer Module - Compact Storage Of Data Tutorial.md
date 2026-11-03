---
title: "Stravant's BitBuffer Module - Compact Storage Of Data [Tutorial]"
url: https://devforum.roblox.com/t/stravants-bitbuffer-module-compact-storage-of-data-tutorial/20189
creator: Roblox DevForum
official: false
advice_density: high
date: 2015-11-30
views: 69
transcript: web-page
confidence: high
tags: [roblox, roblox devforum, youtube-learn]
---

# Stravant's BitBuffer Module - Compact Storage Of Data [Tutorial]

[Open](https://devforum.roblox.com/t/stravants-bitbuffer-module-compact-storage-of-data-tutorial/20189) | Roblox DevForum | 69 views | 2015-11-30

## Summary
Stravant's BitBuffer module (as summarized by TheNexusAvenger, 2015) for compact binary storage of numbers, strings, bools and CFrame rotations in DataStores. Covers each write/read function, bit-width math, Base64 saving, versioning and string-encoding optimisation.

## Tips
- [page](https://devforum.roblox.com/t/stravants-bitbuffer-module-compact-storage-of-data-tutorial/20189) **[[data-persistence]]** Write and read fields in the exact same order with the same bit widths; mismatched order is the hardest bug to find.
- [page](https://devforum.roblox.com/t/stravants-bitbuffer-module-compact-storage-of-data-tutorial/20189) **[[data-persistence]]** Store a version number (6-8 bits) at the start of every save format so future format changes can load old data.
- [page](https://devforum.roblox.com/t/stravants-bitbuffer-module-compact-storage-of-data-tutorial/20189) **[[data-persistence]]** Compute the minimum bit width from your max value using math.ceil(math.log10(n+1)/math.log10(2)) instead of defaulting to 32 bits.
- [page](https://devforum.roblox.com/t/stravants-bitbuffer-module-compact-storage-of-data-tutorial/20189) **[[data-persistence]]** Store the chosen bit width in a 6-bit header first, since 6 bits can represent widths up to 63.
- [page](https://devforum.roblox.com/t/stravants-bitbuffer-module-compact-storage-of-data-tutorial/20189) **[[data-persistence]]** Use Buffer:ToBase64() for DataStores; ToString() output cannot be stored reliably there.
- [page](https://devforum.roblox.com/t/stravants-bitbuffer-module-compact-storage-of-data-tutorial/20189) **[[data-persistence]]** Use BitBuffer for numeric-heavy data; for mostly-string data, expect little saving unless you map characters to small indexes.
- [page](https://devforum.roblox.com/t/stravants-bitbuffer-module-compact-storage-of-data-tutorial/20189) **[[anti-exploit-and-security]]** Compact encoding is obfuscation, not security; encrypt sensitive data and never store what players shouldn't decode.
- [page](https://devforum.roblox.com/t/stravants-bitbuffer-module-compact-storage-of-data-tutorial/20189) **[[data-persistence]]** Use 32-bit floats for compact storage and 64-bit floats when precision matters.
- [page](https://devforum.roblox.com/t/stravants-bitbuffer-module-compact-storage-of-data-tutorial/20189) **[[data-persistence]]** Avoid WriteBrickColor for long-lived saves, since the BrickColor palette changes over time.

## Numbers
- [page](https://devforum.roblox.com/t/stravants-bitbuffer-module-compact-storage-of-data-tutorial/20189) DataStore max size per key: **64 KB (~65,792 characters)**
- [page](https://devforum.roblox.com/t/stravants-bitbuffer-module-compact-storage-of-data-tutorial/20189) Bits per ASCII character in string: **8 bits; BitBuffer WriteString uses 7 bits plus 7-bit null terminator**
- [page](https://devforum.roblox.com/t/stravants-bitbuffer-module-compact-storage-of-data-tutorial/20189) Bits used for '100' as string: **24 bits (3 characters)**
- [page](https://devforum.roblox.com/t/stravants-bitbuffer-module-compact-storage-of-data-tutorial/20189) Version header size suggested: **6-8 bits**
- [page](https://devforum.roblox.com/t/stravants-bitbuffer-module-compact-storage-of-data-tutorial/20189) Max value storable in 6-bit width header: **63**

## Games
- **Roblox Battle Remastered**: Format changed 3 times with live versions; read version first and dispatch to matching decoder.

## Tools
BitBuffer module (Stravant)

## He points to
- Stravant's original BitBuffer post (DevForum)

## Topics
[[anti-exploit-and-security]] [[data-persistence]]

Back to [[Roblox DevForum - How to make successful Roblox games]]
