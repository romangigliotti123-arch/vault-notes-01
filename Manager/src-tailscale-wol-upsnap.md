---
tags: [manager-kb, source]
url: https://tailscale.com/blog/wake-on-lan-tailscale-upsnap
type: eng-blog
author: Kevin Purdy (Tailscale)
published: 2025-08-19
accessed: 2026-10-29
reliability: high (vendor blog, accurate on layer-2 limits)
---
# Wake-on-LAN with Tailscale (UpSnap)
## Key claims
- Tailscale works at L3; WoL magic packets are L2 broadcasts, so Tailscale cannot send them itself even with subnet routing. An always-on device on the target's LAN must send the packet (Raspberry Pi with `etherwake`, or the UpSnap self-hosted web app reachable over the tailnet, optionally as a Tailscale-sidecar node via Tailscale Serve).
- "devices needing a wake-up have to be on the same local network, and connected by ethernet" (their Pi example) - i.e. Wi-Fi targets are outside the happy path, consistent with Roman's CachyOS WoWLAN difficulties.
- The device itself must already be correctly configured for WoL; UpSnap can also power off and scan the network.
## Quotable
> Tailscale can't send WoL packets (sometimes called "Magic Packets") over a Layer 2 connection, even if you have enabled subnet routing

## Used by
[[topic-cross-device-agent-control]]
