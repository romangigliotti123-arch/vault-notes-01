--!strict
-- LootTable: weighted loot, egg and crate rolls with a pity counter, a displayable odds table and a drop log. Server only.
-- The roll uses an injected random function (math.random on the server; a fixed sequence in tests). The client never sends a roll,
-- a luck value or a result. Odds shown to players are computed from the SAME weights the roll uses.
--   local loot = LootTable.new({ name = "ForestEgg", rng = function() return Random.new():NextNumber() end,
--       entries = { { id = "Dog", weight = 70, rarity = "common" }, { id = "Fox", weight = 25, rarity = "rare" }, { id = "Dragon", weight = 5, rarity = "legendary" } },
--       pity = { rarity = "legendary", every = 50 } })
--   local id = loot:roll(data, luck)       -- luck >= 1 multiplies the weight of non-common entries (server-side boost value)
--   loot:odds()                            -- { { id, rarity, percent } ... } for the hatch UI
local LootTable = {}
LootTable.__index = LootTable

export type Data = { [any]: any }
export type Entry = { id: string, weight: number, rarity: string }
export type Pity = { rarity: string, every: number }
export type Config = {
	name: string,
	entries: { Entry },
	rng: () -> number, -- returns [0, 1)
	pity: Pity?,
	baseRarity: string?, -- the rarity luck does NOT boost (default "common")
	log: ((entry: { [string]: any }) -> ())?,
}
export type LootTable = typeof(setmetatable({} :: { _c: Config }, LootTable))

function LootTable.new(config: Config): LootTable
	assert(#config.entries >= 1, "loot table needs entries")
	local total, ids = 0, {}
	for _, e in config.entries do
		assert(e.weight > 0 and e.weight == e.weight, `entry {e.id}: weight must be > 0`)
		assert(not ids[e.id], `duplicate entry {e.id}`)
		ids[e.id] = true
		total += e.weight
	end
	if config.pity then
		assert(config.pity.every >= 1, "pity.every must be >= 1")
		local found = false
		for _, e in config.entries do
			found = found or e.rarity == config.pity.rarity
		end
		assert(found, "pity rarity has no entry in this table")
	end
	return setmetatable({ _c = config }, LootTable)
end

-- the odds the player is shown (percent, 4 significant digits is plenty); same numbers the roll uses at luck 1
function LootTable.odds(self: LootTable): { { id: string, rarity: string, percent: number } }
	local total = 0
	for _, e in self._c.entries do
		total += e.weight
	end
	local out = {}
	for _, e in self._c.entries do
		table.insert(out, { id = e.id, rarity = e.rarity, percent = e.weight / total * 100 })
	end
	return out
end

local function pityState(_self: LootTable, data: Data): Data
	local l = data.Loot
	if type(l) ~= "table" then
		l = { pity = {} }
		data.Loot = l
	end
	l.pity = l.pity or {}
	return l
end

function LootTable.sinceRare(self: LootTable, data: Data): number
	return pityState(self, data).pity[self._c.name] or 0
end

function LootTable.roll(self: LootTable, data: Data, luck: number?): string
	local boost = luck or 1
	assert(boost >= 1 and boost <= 100, "luck must be 1..100")
	local l = pityState(self, data)
	local misses: number = l.pity[self._c.name] or 0
	local base = self._c.baseRarity or "common"
	local pool: { Entry } = self._c.entries
	local forced = false
	local pity = self._c.pity
	if pity and misses + 1 >= pity.every then
		forced = true
		pool = {}
		for _, e in self._c.entries do
			if e.rarity == pity.rarity then
				table.insert(pool, e)
			end
		end
	end
	local weights, total = {}, 0
	for i, e in pool do
		local w = if e.rarity == base then e.weight else e.weight * boost
		weights[i] = w
		total += w
	end
	local r = self._c.rng()
	assert(r >= 0 and r < 1, "rng must return [0, 1)")
	local pick, acc = pool[#pool], 0
	for i, e in pool do
		acc += weights[i]
		if r * total < acc then
			pick = e
			break
		end
	end
	if pity and pick.rarity == pity.rarity then
		l.pity[self._c.name] = 0
	else
		l.pity[self._c.name] = misses + 1
	end
	if self._c.log then
		self._c.log({ table = self._c.name, id = pick.id, rarity = pick.rarity, luck = boost, pity = forced })
	end
	return pick.id
end

return LootTable
