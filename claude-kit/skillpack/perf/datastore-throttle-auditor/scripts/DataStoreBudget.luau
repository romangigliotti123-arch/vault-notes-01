--!strict
local DataStoreBudget = {}

export type Usage = { reads: number, writes: number, lists: number?, orderedWrites: number? }

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

function DataStoreBudget.minSaveInterval(players: number, fraction: number?): number
	local f = fraction or 0.5
	local perMinute = DataStoreBudget.serverBudget(players).readWrite * f
	return 60 * players / perMinute
end

function DataStoreBudget.maxWritesPerMinutePerKey(valueBytes: number): number
	local kb = math.max(1, math.ceil(valueBytes / 1024))
	return math.floor(4 * 1024 / kb)
end

function DataStoreBudget.fitsValueLimit(serializedChars: number): boolean
	return serializedChars <= 4194304
end

return DataStoreBudget
