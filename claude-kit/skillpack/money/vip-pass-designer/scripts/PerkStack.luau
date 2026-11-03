--!strict
-- PerkStack: combine VIP / pass perks into one capped multiplier per target so owning several passes cannot break the economy.
-- Multipliers ADD their bonus (2x and 1.5x together are 2.5x, not 3x) and the total is clipped to a cap. The cap is a design number you choose
-- (default 3, a starting point, not a platform rule). Call it on the server when a reward is computed, with ownership from Shop / OwnershipCache.
--   local mult = PerkStack.multiplier(activePerks, "coins", 3)
--   local reward = baseReward * mult
local PerkStack = {}

export type Perk = { source: string, target: string, multiplier: number }

-- perks that apply: only those whose pass the player owns (filter before calling)
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

-- design-time audit over EVERY perk you plan to sell: which targets would exceed the cap if one player owned them all?
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

-- share of a buyer's income that comes from perks: 1 - 1/multiplier. Above ~0.5 free players earn less than half of what buyers do.
function PerkStack.perkShare(multiplier: number): number
	assert(multiplier >= 1, "multiplier must be >= 1")
	return 1 - 1 / multiplier
end

return PerkStack
