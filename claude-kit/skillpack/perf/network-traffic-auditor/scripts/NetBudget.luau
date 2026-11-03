--!strict
-- NetBudget: estimate remote/replication bandwidth per client and rank the biggest senders. Pure logic, Lune-tested.
-- Sources (vault, optimization-and-streaming KB; labels as there):
--   Keep per-client replication/incoming under about 50 KB/s; above Roblox's roughly 50 KB/s throttle humanoids replicate slowly or teleport (creators; docs-adjacent).
--   Position as Vector3int16 about 6 bytes vs CFrame about 20 bytes; Color3 12 bytes vs about 5 as an Int8 string; numbers are Float64 (8 bytes); arrays beat string-keyed dictionaries.
--   Batch many small remotes into fewer sends. 60 tweened server doors used about 1,800 KB/s received vs about 0 KB/s with animation playback (one test, indie).
-- Per-remote byte sizes below are estimates from those figures plus 1 byte for a boolean; there is no per-call header in the estimate. Confirm real traffic
-- with the Network Stats / MicroProfiler network view (Ctrl+F7) or lag-hunter/scripts/remote_probe.luau.
local NetBudget = {}

NetBudget.CLIENT_KBPS = 50
NetBudget.SIZES = {
	number = 8,
	boolean = 1,
	vector3 = 12,
	vector3int16 = 6,
	cframe = 20,
	color3 = 12,
	color3string = 5,
	int16 = 2,
	int8 = 1,
} :: { [string]: number }

export type Remote = { name: string, fields: { string }, hz: number, receivers: number?, stringBytes: number? }
export type Row = { name: string, bytes: number, kbpsPerReceiver: number, kbpsTotalServerSend: number }

function NetBudget.payloadBytes(fields: { string }, stringBytes: number?): number
	local total = 0
	for _, f in fields do
		if f == "string" then
			total += stringBytes or 16
		else
			local size = NetBudget.SIZES[f]
			assert(size ~= nil, "unknown field type " .. f)
			total += size
		end
	end
	return total
end

-- hz = calls per second. receivers = how many clients each call reaches (FireAllClients = player count). Returns rows worst-first.
function NetBudget.audit(remotes: { Remote }, players: number): ({ Row }, number)
	local rows: { Row } = {}
	local perClient = 0
	for _, r in remotes do
		local bytes = NetBudget.payloadBytes(r.fields, r.stringBytes)
		local recv = r.receivers or players
		local kbpsPerReceiver = bytes * r.hz / 1024
		perClient += kbpsPerReceiver -- worst case: every remote reaches every client
		table.insert(rows, {
			name = r.name,
			bytes = bytes,
			kbpsPerReceiver = kbpsPerReceiver,
			kbpsTotalServerSend = kbpsPerReceiver * recv,
		})
	end
	table.sort(rows, function(a, b)
		if a.kbpsTotalServerSend ~= b.kbpsTotalServerSend then
			return a.kbpsTotalServerSend > b.kbpsTotalServerSend
		end
		return a.name < b.name
	end)
	return rows, perClient
end

-- batching: n small calls per second folded into `batchesPerSecond` sends. Saves nothing on payload bytes, only on call overhead, so report
-- the call-count cut and let the profiler decide whether it mattered.
function NetBudget.batchedCalls(callsPerSecond: number, batchesPerSecond: number): number
	return math.max(0, callsPerSecond - batchesPerSecond)
end

function NetBudget.status(perClientKbps: number): string
	if perClientKbps > NetBudget.CLIENT_KBPS then
		return "over"
	elseif perClientKbps > NetBudget.CLIENT_KBPS * 0.6 then
		return "warn" -- heuristic: 60 percent of the 50 KB/s figure
	end
	return "ok"
end

return NetBudget
