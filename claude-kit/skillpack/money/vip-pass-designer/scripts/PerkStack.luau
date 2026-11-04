--!strict
local PerkStack = {}

export type Perk = { source: string, target: string, multiplier: number }

function PerkStack.multiplier(perks: { Perk }, target: string, cap: number?): number
	local total = 1
	for _, p in perks do
		assert(p.multiplier >= 1, `perk {p.source} has a multiplier below 1`)
		if p.target == target then
			total += p.multiplier - 1
		end
	end
	return math.min(total, cap or 3)
end

function PerkStack.audit(allPerks: { Perk }, cap: number?): { { target: string, raw: number, cap: number } }
	local limit = cap or 3
	local raw: { [string]: number } = {}
	for _, p in allPerks do
		assert(p.multiplier >= 1, `perk {p.source} has a multiplier below 1`)
		raw[p.target] = (raw[p.target] or 1) + p.multiplier - 1
	end
	local out = {}
	for target, value in raw do
		if value > limit then
			table.insert(out, { target = target, raw = value, cap = limit })
		end
	end
	table.sort(out, function(a, b)
		return a.target < b.target
	end)
	return out
end

function PerkStack.perkShare(multiplier: number): number
	assert(multiplier >= 1, "multiplier must be >= 1")
	return 1 - 1 / multiplier
end

return PerkStack
