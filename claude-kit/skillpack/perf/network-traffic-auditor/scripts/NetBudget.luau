--!strict
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

function NetBudget.audit(remotes: { Remote }, players: number): ({ Row }, number)
	local rows: { Row } = {}
	local perClient = 0
	for _, r in remotes do
		local bytes = NetBudget.payloadBytes(r.fields, r.stringBytes)
		local recv = r.receivers or players
		local kbpsPerReceiver = bytes * r.hz / 1024
		perClient += kbpsPerReceiver
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

function NetBudget.batchedCalls(callsPerSecond: number, batchesPerSecond: number): number
	return math.max(0, callsPerSecond - batchesPerSecond)
end

function NetBudget.status(perClientKbps: number): string
	if perClientKbps > NetBudget.CLIENT_KBPS then
		return "over"
	elseif perClientKbps > NetBudget.CLIENT_KBPS * 0.6 then
		return "warn"
	end
	return "ok"
end

return NetBudget
