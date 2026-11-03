--!strict
-- DataStoreBudget: request budgets from the Creator Docs formulas, utilisation checks and the shortest safe autosave interval. Pure logic, Lune-tested.
-- Source: Roblox Creator Docs cloud-services/data-stores/error-codes-and-limits (official; vault note "Docs cloud-services data-stores error-codes-and-limits"):
--   standard read budget  300 + CCU x 40 per minute;  standard write 300 + CCU x 20;  list 300 + CCU x 2;  ordered write 300 + CCU x 20;
--   per-server default read/write 60 + players x 40 per minute; per-server ordered write 30 + players x 5; per-key throughput read 25 MB/min, write 4 MB/min, rounded up to the next KB per request;
--   value limit 4,194,304 characters serialized; 30 queued requests per queue type. LIVE-CHECK: Roblox changes these; compare with the docs page before relying on them.
local DataStoreBudget = {}

export type Usage = { reads: number, writes: number, lists: number?, orderedWrites: number? } -- per minute, whole experience

function DataStoreBudget.experienceBudget(
	ccu: number
): { read: number, write: number, list: number, orderedWrite: number }
	return { read = 300 + ccu * 40, write = 300 + ccu * 20, list = 300 + ccu * 2, orderedWrite = 300 + ccu * 20 }
end

function DataStoreBudget.serverBudget(players: number): { readWrite: number, orderedWrite: number }
	return { readWrite = 60 + players * 40, orderedWrite = 30 + players * 5 }
end

function DataStoreBudget.utilisation(usage: Usage, ccu: number): { [string]: number }
	local b = DataStoreBudget.experienceBudget(ccu)
	return {
		read = usage.reads / b.read,
		write = usage.writes / b.write,
		list = (usage.lists or 0) / b.list,
		orderedWrite = (usage.orderedWrites or 0) / b.orderedWrite,
	}
end

-- worst: the metric nearest its limit and a status (over above 1.0; warn above 0.6, a heuristic that leaves room for bursts at join/leave).
function DataStoreBudget.worst(util: { [string]: number }): (string, number, string)
	local key, val = "read", -1
	for k, v in util do
		if v > val or (v == val and k < key) then
			key, val = k, v
		end
	end
	local status = if val > 1 then "over" elseif val > 0.6 then "warn" else "ok"
	return key, val, status
end

-- minSaveInterval: seconds between autosaves per player so that steady-state saves use at most `fraction` (default 0.5) of the server write budget.
function DataStoreBudget.minSaveInterval(players: number, fraction: number?): number
	local f = fraction or 0.5
	local perMinute = DataStoreBudget.serverBudget(players).readWrite * f
	return 60 * players / perMinute
end

-- Writes per minute one key can take before the 4 MB/min per-key write throughput is exceeded (size rounded up to KB).
function DataStoreBudget.maxWritesPerMinutePerKey(valueBytes: number): number
	local kb = math.max(1, math.ceil(valueBytes / 1024))
	return math.floor(4 * 1024 / kb)
end

function DataStoreBudget.fitsValueLimit(serializedChars: number): boolean
	return serializedChars <= 4194304
end

return DataStoreBudget
