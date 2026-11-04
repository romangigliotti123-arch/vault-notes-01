--!strict
local Achievements = {}
Achievements.__index = Achievements

export type Data = { [any]: any }
export type Def = { badgeId: number }
export type Config = {
	defs: { [string]: Def },
	award: (userId: number, badgeId: number) -> boolean,
	onUnlock: ((userId: number, id: string) -> ())?,
	maxAttempts: number?,
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

function Achievements.resetAttempts(self: Achievements, data: Data)
	local a = self:init(data)
	for id in a.pending do
		a.pending[id] = 0
	end
end

return Achievements
