--!strict
local LAG_MS = 0

local network = settings().Network
local before = network.IncomingReplicationLag
network.IncomingReplicationLag = LAG_MS / 1000
return ("IncomingReplicationLag: %.0f ms -> %.0f ms (0 = off). Reset to 0 when finished."):format(before * 1000, LAG_MS)
