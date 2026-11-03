---
tags: [manager-kb, source]
url: https://github.com/ReimuNotMoe/ydotool
type: repo
author: ReimuNotMoe
published: undated (README at master)
accessed: 2026-10-29
reliability: high (upstream README)
---
# ydotool README
## Key claims
- Works on anything that accepts input (Wayland, X11, text console, fbdev) because it injects through the Linux `uinput` kernel framework instead of speaking to a display server; since v1.0.0 the `ydotoold` daemon is mandatory and holds a persistent virtual device (a fresh virtual device takes time to be recognised by udev/compositor, hence the daemon).
- `ydotoold` needs access to `/dev/uinput`, "usually requires root permissions" (our CachyOS setup runs it as a user service after sudo setup).
- It has no notion of windows: window focus/position must come from other tools (kdotool for KDE was tried and failed to build on the CachyOS box; xdotool only reaches XWayland windows). Input goes to whatever is focused, which is why CLAUDE.md says to click the target first.
- Search-snippet context (not opened): KDE screenshots use `spectacle`; the XDG RemoteDesktop portal + libei is the "proper" permissioned route (consent prompt) with no verified headless story.
## Quotable
> ydotool works differently from xdotool. xdotool sends X events directly to X server, while ydotool uses the uinput framework of Linux kernel to emulate an input device.

## Used by
[[topic-cross-device-agent-control]]
