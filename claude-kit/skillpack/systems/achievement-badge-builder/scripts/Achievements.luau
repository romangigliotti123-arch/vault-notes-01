--!strict
-- Achievements: unlock once, award the Roblox badge idempotently with retries. The unlock flag is saved in player data in the same
-- step as the decision; the badge call (BadgeService:AwardBadge, may fail or yield) is a separate pending entry that is retried
-- until it succeeds, so a failed call never loses a badge and a retry never double-awards.
--   local ach = Achievements.new({ defs = { first_win = { badgeId = 0 } }, award = function(userId, badgeId) return pcallAward(userId, badgeId) end })
--   ach:unlock(userId, data, "first_win")   -- from the server code that saw the condition
--   ach:flush(userId, data)                 -- on join, after each unlock, and on a timer (yields; call from its own thread)
local Achievements = {}
Achievements.__index = Achievements

export type Data = { [any]: any }
export type Def = { badgeId: number } -- 0 = not created yet (SET IN CREATOR HUB): the achievement unlocks, no badge call is made
export type Config = {
	defs: { [string]: Def },
	award: (userId: number, badgeId: number) -> boolean, -- true when Roblox confirms (or says already owned)
	onUnlock: ((userId: number, id: string) -> ())?,
	maxAttempts: number?, -- per pending entry before it is parked for the next session (default 8)
}
export type Achievements = typeof(setmetatable({} :: { _c: Config }, Achievements))

function Achievements.new(config: Config): Achievements
	return setmetatable({ _c = config }, Achievements)
end

function Achievements.init(_self: Achievements, data: Data): Data
	local a = data.Achievements
	if type(a) ~= "table" then
		a = { done = {}, pending = {} }
		data.Achievements = a
	end
	a.done = a.done or {}
	a.pending = a.pending or {}
	return a
end

function Achievements.has(self: Achievements, data: Data, id: string): boolean
	return self:init(data).done[id] == true
end

-- true only the first time
function Achievements.unlock(self: Achievements, userId: number, data: Data, id: string): boolean
	local def = self._c.defs[id]
	if def == nil then
		return false
	end
	local a = self:init(data)
	if a.done[id] then
		return false
	end
	a.done[id] = true
	if def.badgeId ~= 0 then
		a.pending[id] = 0
	end
	if self._c.onUnlock then
		self._c.onUnlock(userId, id)
	end
	return true
end

-- try every pending badge once; returns how many were awarded. Entries that keep failing are kept (attempt counter) for next session.
function Achievements.flush(self: Achievements, userId: number, data: Data): number
	local a = self:init(data)
	local awarded = 0
	local ids = {}
	for id in a.pending do
		table.insert(ids, id)
	end
	table.sort(ids)
	for _, id in ids do
		local tries: number = a.pending[id]
		local def = self._c.defs[id]
		if def == nil then
			a.pending[id] = nil
		elseif tries < (self._c.maxAttempts or 8) then
			if self._c.award(userId, def.badgeId) then
				a.pending[id] = nil
				awarded += 1
			else
				a.pending[id] = tries + 1
			end
		end
	end
	return awarded
end

-- on join: give parked entries a fresh set of attempts
function Achievements.resetAttempts(self: Achievements, data: Data)
	local a = self:init(data)
	for id in a.pending do
		a.pending[id] = 0
	end
end

return Achievements
