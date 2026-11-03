---
tags: [manager-kb, source]
url: https://blog.openreplay.com/remote-box-agentic-coding-setup/
type: practitioner-blog
author: OpenReplay Team
published: 2026-07-06
accessed: 2026-10-29
reliability: med (vendor blog, general security advice sound, claims not benchmarked)
---
# Setting up a remote box for agentic coding
## Key claims
- Two patterns people conflate: tmux (interactive, attach/detach, you steer) vs systemd (unattended HTTP service). Choosing wrong is "the most common structural mistake".
- Canonical free stack: Linux box + Tailscale + OpenSSH (+ mosh) + tmux. Do NOT enable `tailscale up --ssh` if you want mosh: Tailscale SSH is not OpenSSH, mosh cannot bootstrap through it. mosh needs UDP 60000-61000 reachable (fine inside a tailnet).
- Name tmux sessions after the project not the tool (`tmux new-session -s myproject`), so `tmux ls` identifies them.
- Security baseline: SSH keys only (`PasswordAuthentication no`, `PermitRootLogin no`), test the key in a second session before closing the first, never bind the agent to 0.0.0.0, use Tailscale ACLs when other people/devices share the tailnet, keep API keys out of systemd `Environment=` (use `EnvironmentFile=` or `LoadCredential=`).
- States native Remote Control is single-session and tied to a live process; DIY box is for always-on/headless/multi-project.
## Quotable
> do not enable Tailscale's built-in SSH server with tailscale up --ssh if you plan to use mosh.

## Used by
[[topic-cross-device-agent-control]]
