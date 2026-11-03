--!strict
-- Rounds: the intermission -> playing -> ending state machine as pure logic driven by tick(dt). It decides WHAT state we are in and
-- who may join; the glue (teleports, map load, scoreboards) is in the callbacks, and cleanup always runs when a round ends.
-- States: Waiting (not enough players) -> Intermission (countdown) -> Playing -> Ending (results) -> back to Waiting/Intermission.
--   local rounds = Rounds.new({ minPlayers = 2, intermission = 15, roundLength = 120, endScreen = 6, joinGrace = 10,
--       onStart = function(ids) ... end, onEnd = function(reason, winners) ... end, cleanup = function() ... end })
--   every second:  rounds:tick(1, playerCount)       ; on death/leave: rounds:out(userId) ; late join: rounds:join(userId) -> "play" | "spectate"
local Rounds = {}
Rounds.__index = Rounds

export type Config = {
	minPlayers: number,
	intermission: number,
	roundLength: number,
	endScreen: number,
	joinGrace: number?, -- seconds into a round during which a late joiner may still enter (default 0 = never)
	onStart: (ids: { number }) -> (),
	onEnd: (reason: string, survivors: { number }) -> (),
	cleanup: () -> (),
	soloEnds: boolean?, -- end when one player is left alive (default true)
}
export type State = "Waiting" | "Intermission" | "Playing" | "Ending"
export type Rounds = typeof(setmetatable(
	{} :: {
		_c: Config,
		state: State,
		left: number,
		elapsed: number,
		alive: { [number]: boolean },
		waiting: { [number]: boolean },
		rounds: number,
		startedWith: number,
	},
	Rounds
))

function Rounds.new(config: Config): Rounds
	assert(
		config.minPlayers >= 1 and config.intermission >= 0 and config.roundLength > 0 and config.endScreen >= 0,
		"bad round config"
	)
	return setmetatable({
		_c = config,
		state = "Waiting" :: State,
		left = 0,
		elapsed = 0,
		alive = {},
		waiting = {},
		rounds = 0,
		startedWith = 0,
	}, Rounds)
end

local function aliveList(self: Rounds): { number }
	local out = {}
	for id, v in self.alive do
		if v then
			table.insert(out, id)
		end
	end
	table.sort(out)
	return out
end

local function finish(self: Rounds, reason: string)
	local survivors = aliveList(self)
	self.state = "Ending"
	self.left = self._c.endScreen
	self._c.onEnd(reason, survivors)
end

-- who is waiting for the next round is tracked by the glue through join(); tick only needs the head count of ready players
function Rounds.tick(self: Rounds, dt: number, ready: number): State
	if self.state == "Waiting" then
		if ready >= self._c.minPlayers then
			self.state, self.left = "Intermission", self._c.intermission
		end
	elseif self.state == "Intermission" then
		if ready < self._c.minPlayers then
			self.state = "Waiting" -- someone left: the countdown restarts when enough are back
		else
			self.left -= dt
			if self.left <= 0 then
				self.state, self.left, self.elapsed = "Playing", self._c.roundLength, 0
				self.rounds += 1
				self.alive = {}
				for id in self.waiting do
					self.alive[id] = true
				end
				self.waiting = {}
				self.startedWith = #aliveList(self)
				self._c.onStart(aliveList(self))
			end
		end
	elseif self.state == "Playing" then
		self.left -= dt
		self.elapsed += dt
		local n = #aliveList(self)
		if n == 0 then
			finish(self, "empty")
		elseif n <= 1 and self._c.soloEnds ~= false and self.startedWith >= 2 then
			finish(self, "last standing")
		elseif self.left <= 0 then
			finish(self, "time")
		end
	elseif self.state == "Ending" then
		self.left -= dt
		if self.left <= 0 then
			self._c.cleanup()
			self.alive = {}
			self.state = "Waiting"
		end
	end
	return self.state
end

-- a player became ready to play (joined the lobby/spectator pool). Returns "play" when they will be in the next/this round, else "spectate".
function Rounds.join(self: Rounds, userId: number): string
	if self.state == "Playing" then
		if self.elapsed <= (self._c.joinGrace or 0) then
			self.alive[userId] = true
			return "play"
		end
		return "spectate"
	end
	if self.state == "Ending" then
		return "spectate"
	end
	self.waiting[userId] = true
	return "play"
end

-- died, left or was eliminated
function Rounds.out(self: Rounds, userId: number)
	self.alive[userId] = nil
	self.waiting[userId] = nil
end

function Rounds.aliveCount(self: Rounds): number
	return #aliveList(self)
end

return Rounds
