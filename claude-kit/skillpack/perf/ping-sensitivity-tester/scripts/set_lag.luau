--!strict
-- set_lag.luau: STUDIO ONLY test aid. Sets the Studio network setting NetworkSettings.IncomingReplicationLag (seconds the client waits before applying replicated data) to simulate
-- latency in a local play session, or clears it. Command bar / MCP `execute_luau` (Edit datamodel) BEFORE pressing Play; the value persists in Studio settings, so always reset it.
-- Usage: set LAG_MS below (0 = reset). It is a coarse one-direction simulation (incoming replication only): it does NOT model packet loss, jitter, or a real cellular link.
-- Vault: Creator Docs test-on-hardware: Studio simulation is only for quick iteration; confirm behaviour over real cellular or constrained Wi-Fi on a device (official).
local LAG_MS = 0 -- 0 resets. Typical test steps: 100, 200, 300 (heuristic matrix; widen from your players' ping in the Performance dashboard)

local network = settings().Network
local before = network.IncomingReplicationLag
network.IncomingReplicationLag = LAG_MS / 1000
return ("IncomingReplicationLag: %.0f ms -> %.0f ms (0 = off). Reset to 0 when finished."):format(before * 1000, LAG_MS)
