--!strict
local Spawns = {}
Spawns.__index = Spawns

export type Pos = { x: number, y: number, z: number }
export type Spawn = { id: string, team: string?, pos: Pos }
export type Config = { protectSeconds: number, now: () -> number, minEnemyDistance: number? }
export type Spawns = typeof(setmetatable(
	{} :: { _c: Config, _until: { [number]: number }, _lastPick: { [string]: string } },
	Spawns
))

function Spawns.new(config: Config): Spawns
	assert(
		config.protectSeconds >= 0 and config.protectSeconds <= 10,
		"protection longer than 10 s invites spawn-camping abuse"
	)
	return setmetatable({ _c = config, _until = {}, _lastPick = {} }, Spawns)
end

local function dist(a: Pos, b: Pos): number
	local dx, dy, dz = a.x - b.x, a.y - b.y, a.z - b.z
	return math.sqrt(dx * dx + dy * dy + dz * dz)
end

function Spawns.pick(self: Spawns, list: { Spawn }, team: string?, enemies: { Pos }): Spawn?
	local best, bestScore = nil :: Spawn?, -math.huge
	for _, s in list do
		if s.team == nil or s.team == team then
			local nearest = math.huge
			for _, e in enemies do
				nearest = math.min(nearest, dist(s.pos, e))
			end
			local score = if nearest == math.huge then 1e9 else nearest
			if self._lastPick[team or ""] == s.id then
				score -= 1
			end
			if score > bestScore then
				best, bestScore = s, score
			end
		end
	end
	if best then
		self._lastPick[team or ""] = best.id
	end
	return best
end

function Spawns.protect(self: Spawns, userId: number)
	self._until[userId] = self._c.now() + self._c.protectSeconds
end

function Spawns.isProtected(self: Spawns, userId: number): boolean
	local u = self._until[userId]
	return u ~= nil and self._c.now() < u
end

function Spawns.attacked(self: Spawns, userId: number)
	self._until[userId] = nil
end

function Spawns.damageFor(self: Spawns, victimId: number, amount: number): number
	return if self:isProtected(victimId) then 0 else amount
end

function Spawns.forget(self: Spawns, userId: number)
	self._until[userId] = nil
end

return Spawns
