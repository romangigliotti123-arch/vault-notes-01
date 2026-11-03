---
tags: [manager-kb, source]
url: https://www.freedesktop.org/software/systemd/man/latest/systemd.service.html
type: official-doc
author: systemd
published: undated
accessed: 2026-10-29
reliability: high (man page; start-limit semantics live in systemd.unit and were NOT read)
---
# systemd.service: Restart=, RestartSec=, WatchdogSec=
## Key claims
- `Restart=on-failure` restarts on non-zero exit/signal/timeout/watchdog expiry; `always` regardless; default `no`. `RestartSec=` default 100 ms.
- "service restart is subject to unit start rate limiting" via StartLimitIntervalSec/StartLimitBurst (page defers to systemd.unit; semantics not verified here).
- `WatchdogSec=`: service must send `WATCHDOG=1` keep-alives via sd_notify; if the interval is exceeded the service is marked failed and killed (SIGABRT). I.e. a heartbeat, not a process-exists check. Model for a Windows watchdog: check a heartbeat FILE's mtime, not just whether claude.exe exists.

## Used by
[[topic-long-running-always-on-agents]]
