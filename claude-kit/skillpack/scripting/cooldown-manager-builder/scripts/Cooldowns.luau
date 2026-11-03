--!strict
-- Cooldowns: per-player, per-action cooldowns kept on the server. One object guards every remote and prompt.
--   local cooldowns = Cooldowns.new()                       -- clock defaults to os.clock
--   if not cooldowns:Try(player.UserId, "Swing", 0.6) then return end   -- starts the cooldown when it succeeds
--   cooldowns:Remaining(player.UserId, "Swing")  cooldowns:Reset(userId, "Swing")  cooldowns:Clear(userId) -- on PlayerRemoving
-- Keys are UserIds (numbers), never player names or Player objects, so entries cannot outlive a rejoin or pin a Player in memory.
local Cooldowns = {}
Cooldowns.__index = Cooldowns

export type Cooldowns = typeof(setmetatable(
	{} :: { _clock: () -> number, _until: { [number]: { [string]: number } } },
	Cooldowns
))

function Cooldowns.new(clock: (() -> number)?): Cooldowns
	return setmetatable({ _clock = clock or os.clock, _until = {} }, Cooldowns)
end

-- true and the cooldown starts if the action is ready; false (nothing changes) while it is cooling down
function Cooldowns.Try(self: Cooldowns, userId: number, action: string, duration: number): boolean
	local now = self._clock()
	local perPlayer = self._until[userId]
	if perPlayer == nil then
		perPlayer = {}
		self._until[userId] = perPlayer
	end
	local readyAt = perPlayer[action]
	if readyAt ~= nil and now < readyAt then
		return false
	end
	perPlayer[action] = now + duration
	return true
end

function Cooldowns.Remaining(self: Cooldowns, userId: number, action: string): number
	local perPlayer = self._until[userId]
	local readyAt = if perPlayer then perPlayer[action] else nil
	if readyAt == nil then
		return 0
	end
	return math.max(0, readyAt - self._clock())
end

function Cooldowns.IsReady(self: Cooldowns, userId: number, action: string): boolean
	return self:Remaining(userId, action) == 0
end

-- end a cooldown early (a reset power-up, a respawn)
function Cooldowns.Reset(self: Cooldowns, userId: number, action: string)
	local perPlayer = self._until[userId]
	if perPlayer then
		perPlayer[action] = nil
	end
end

-- forget one player: call from PlayerRemoving
function Cooldowns.Clear(self: Cooldowns, userId: number)
	self._until[userId] = nil
end

-- drop expired entries so a long-running server does not accumulate them; returns how many were removed
function Cooldowns.Sweep(self: Cooldowns): number
	local now = self._clock()
	local removed = 0
	for userId, perPlayer in self._until do
		local left = 0
		for action, readyAt in perPlayer do
			if now >= readyAt then
				perPlayer[action] = nil
				removed += 1
			else
				left += 1
			end
		end
		if left == 0 then
			self._until[userId] = nil
		end
	end
	return removed
end

-- run fn only if the cooldown allows it; returns whether it ran
function Cooldowns.Gate(self: Cooldowns, userId: number, action: string, duration: number, fn: () -> ()): boolean
	if not self:Try(userId, action, duration) then
		return false
	end
	fn()
	return true
end

return Cooldowns
