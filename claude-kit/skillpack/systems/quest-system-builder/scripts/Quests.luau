--!strict
-- Quests: data-driven objective tracker. Gameplay code reports EVENTS from the server ("kill", "collect", "visit"); the quest module
-- turns them into progress, and a reward can be claimed exactly once. State lives in data.Quests (small, save-friendly).
--   local quests = Quests.new({ defs = { first_steps = { goal = { event = "collect", target = "Wood", amount = 10 },
--       reward = function(data) return wallet:add(data, "Coins", 50, "quest:first_steps", "quest:first_steps") end } } })
--   quests:progress(data, "collect", "Wood", 3)   -- from the server code that actually gave the player wood
--   quests:claim(data, "first_steps")              -- true once; a second call is refused
local Quests = {}
Quests.__index = Quests

export type Data = { [any]: any }
export type Goal = { event: string, target: string?, amount: number }
export type Def = { goal: Goal, requires: string?, reward: (data: Data) -> boolean }
export type Config = { defs: { [string]: Def }, maxEventAmount: number? }
export type Quests = typeof(setmetatable({} :: { _c: Config }, Quests))

function Quests.new(config: Config): Quests
	for id, def in config.defs do
		assert(
			def.goal.amount >= 1 and def.goal.amount == math.floor(def.goal.amount),
			`quest {id}: amount must be a positive integer`
		)
		if def.requires then
			assert(config.defs[def.requires] ~= nil, `quest {id}: requires unknown quest {def.requires}`)
			assert(def.requires ~= id, `quest {id}: requires itself`)
		end
	end
	-- a requires chain must end (no cycles)
	for id in config.defs do
		local seen: { [string]: boolean } = {}
		local cur: string? = id
		while cur do
			assert(not seen[cur], `quest {id}: requires chain loops`)
			seen[cur] = true
			cur = config.defs[cur].requires
		end
	end
	return setmetatable({ _c = config }, Quests)
end

function Quests.init(_self: Quests, data: Data): Data
	local q = data.Quests
	if type(q) ~= "table" then
		q = { progress = {}, claimed = {} }
		data.Quests = q
	end
	q.progress = q.progress or {}
	q.claimed = q.claimed or {}
	return q
end

function Quests.isAvailable(self: Quests, data: Data, id: string): boolean
	local def = self._c.defs[id]
	if def == nil then
		return false
	end
	local q = self:init(data)
	if q.claimed[id] then
		return false
	end
	return def.requires == nil or q.claimed[def.requires] == true
end

function Quests.value(self: Quests, data: Data, id: string): number
	return self:init(data).progress[id] or 0
end

function Quests.isComplete(self: Quests, data: Data, id: string): boolean
	local def = self._c.defs[id]
	return def ~= nil and self:value(data, id) >= def.goal.amount
end

-- server code reports an event. Returns the ids of quests that became complete on this call.
function Quests.progress(self: Quests, data: Data, event: string, target: string?, amount: number?): { string }
	local n = amount or 1
	if type(n) ~= "number" or n ~= n or n < 1 or n ~= math.floor(n) or n > (self._c.maxEventAmount or 1e6) then
		return {}
	end
	local q = self:init(data)
	local done: { string } = {}
	for id, def in self._c.defs do
		local g = def.goal
		if self:isAvailable(data, id) and g.event == event and (g.target == nil or g.target == target) then
			local before = q.progress[id] or 0
			if before < g.amount then
				q.progress[id] = math.min(g.amount, before + n)
				if q.progress[id] >= g.amount then
					table.insert(done, id)
				end
			end
		end
	end
	return done
end

-- claim a finished quest once. The flag is set only after the reward function succeeded, in the same synchronous step.
function Quests.claim(self: Quests, data: Data, id: string): (boolean, string)
	local def = self._c.defs[id]
	if def == nil then
		return false, "unknown quest"
	end
	local q = self:init(data)
	if q.claimed[id] then
		return false, "already claimed"
	end
	if not self:isAvailable(data, id) then
		return false, "locked"
	end
	if not self:isComplete(data, id) then
		return false, "not complete"
	end
	if not def.reward(data) then
		return false, "reward refused"
	end
	q.claimed[id] = true
	q.progress[id] = nil
	return true, "ok"
end

return Quests
