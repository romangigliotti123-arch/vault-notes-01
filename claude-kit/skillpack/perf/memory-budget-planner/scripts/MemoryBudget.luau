--!strict
local MemoryBudget = {}

export type Tier = { ramGB: number, ceilingMB: number, targetMB: number }

local EJECT_FRACTION = 0.66
local TARGET_FRACTION_OF_CEILING = 0.33
MemoryBudget.WARN_AT = 0.75

function MemoryBudget.clientTier(ramGB: number): Tier
	local ceiling = ramGB * 1024 * EJECT_FRACTION
	local target = if ramGB <= 2 then 450 else math.floor(ceiling * TARGET_FRACTION_OF_CEILING)
	return { ramGB = ramGB, ceilingMB = math.floor(ceiling), targetMB = target }
end

function MemoryBudget.serverTotalMB(maxPlayers: number): number
	return 6.25 * 1024 + 100 * maxPlayers
end

function MemoryBudget.serverTargetMB(maxPlayers: number): number
	return MemoryBudget.serverTotalMB(maxPlayers) * 0.5
end

function MemoryBudget.assessClient(usedMB: number, tier: Tier): string
	if usedMB >= tier.ceilingMB then
		return "ejection-zone"
	elseif usedMB > tier.targetMB + (tier.ceilingMB - tier.targetMB) * 0.5 then
		return "risk"
	elseif usedMB > tier.targetMB then
		return "over-target"
	end
	return "ok"
end

function MemoryBudget.assessServer(usedMB: number, maxPlayers: number): string
	if usedMB > MemoryBudget.serverTotalMB(maxPlayers) * 0.5 then
		return "over"
	elseif usedMB > MemoryBudget.serverTotalMB(maxPlayers) * 0.4 then
		return "warn"
	end
	return "ok"
end

function MemoryBudget.breakdown(categories: { [string]: number }): { { name: string, mb: number, share: number } }
	local total = 0
	for _, v in categories do
		total += v
	end
	local rows = {}
	for k, v in categories do
		table.insert(rows, { name = k, mb = v, share = if total > 0 then v / total else 0 })
	end
	table.sort(rows, function(a, b)
		if a.mb ~= b.mb then
			return a.mb > b.mb
		end
		return a.name < b.name
	end)
	return rows
end

return MemoryBudget
