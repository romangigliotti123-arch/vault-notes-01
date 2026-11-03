--!strict
-- Honeypot: suspicion score + escalation ladder + watch list. Pure logic (clock passed in), unit-tested in Lune.
-- A honeypot remote is one legitimate code never fires (fake "AddMoney"); a trip is high confidence. Movement/rate flags are low confidence.
-- This module only DECIDES; the glue (HoneypotService.luau) logs and acts. It never recommends a permanent ban by itself:
-- the top rung is "review" (a human looks at the log, then uses the Ban API by UserId), per the vault: reversible actions for uncertain cases.
local Honeypot = {}
Honeypot.__index = Honeypot

export type Action = "none" | "log" | "mitigate" | "restrict" | "review"
export type Entry = { t: number, userId: number, reason: string, weight: number, score: number, action: Action }
export type Config = {
	now: () -> number,
	mitigateAt: number?, -- score for quiet mitigation: reset position, drop the request (default 3)
	restrictAt: number?, -- temporary restriction: disable trading/shop for this session (default 6)
	reviewAt: number?, -- flag for human review / Ban API (default 10)
	decayPerMinute: number?, -- score lost per minute without new flags (default 1)
	maxLog: number?, -- entries kept (default 500)
	exempt: ((userId: number) -> boolean)?, -- e.g. staff accounts you want to test with; see Pitfalls: test with NON-exempt accounts too
}

export type Honeypot = typeof(setmetatable(
	{} :: { _c: Config, _score: { [number]: { v: number, t: number } }, _log: { Entry }, _watch: { [number]: boolean } },
	Honeypot
))

function Honeypot.new(config: Config): Honeypot
	return setmetatable({ _c = config, _score = {}, _log = {}, _watch = {} }, Honeypot)
end

local function current(self: Honeypot, userId: number): number
	local s = self._score[userId]
	if s == nil then
		return 0
	end
	local lost = (self._c.now() - s.t) / 60 * (self._c.decayPerMinute or 1)
	return math.max(0, s.v - lost)
end

function Honeypot.Score(self: Honeypot, userId: number): number
	return current(self, userId)
end

local function ladder(self: Honeypot, score: number): Action
	local c = self._c
	if score >= (c.reviewAt or 10) then
		return "review"
	elseif score >= (c.restrictAt or 6) then
		return "restrict"
	elseif score >= (c.mitigateAt or 3) then
		return "mitigate"
	elseif score > 0 then
		return "log"
	end
	return "none"
end

-- weight guide: movement/rate flag 1, repeated validation failure 1, impossible request 2-3, honeypot remote fired 10
function Honeypot.Flag(self: Honeypot, userId: number, reason: string, weight: number): Action
	local c = self._c
	if c.exempt and c.exempt(userId) then
		return "none"
	end
	local now = c.now()
	local score = current(self, userId) + weight
	self._score[userId] = { v = score, t = now }
	local action: Action = ladder(self, score)
	if action ~= "none" then
		self._watch[userId] = true
	end
	table.insert(
		self._log,
		{ t = now, userId = userId, reason = reason, weight = weight, score = score, action = action }
	)
	if #self._log > (c.maxLog or 500) then
		table.remove(self._log, 1)
	end
	return action
end

-- convenience: a honeypot remote fired is a straight jump to review
function Honeypot.Trip(self: Honeypot, userId: number, remoteName: string): Action
	return self:Flag(userId, "honeypot:" .. remoteName, self._c.reviewAt or 10)
end

-- suspects are kept apart from bans: most flagged accounts were never seen exploiting
function Honeypot.WatchList(self: Honeypot): { number }
	local out = {}
	for id in self._watch do
		table.insert(out, id)
	end
	table.sort(out)
	return out
end

function Honeypot.Log(self: Honeypot): { Entry }
	return self._log
end

function Honeypot.Forget(self: Honeypot, userId: number)
	self._score[userId] = nil
end

return Honeypot
