--!strict
local Leaderboard = {}
Leaderboard.__index = Leaderboard

export type Entry = { key: string, value: number }
export type Config = {
	now: () -> number,
	ttl: number,
	fetch: (limit: number) -> { Entry }?,
	minWriteGap: number?,
	maxScore: number?,
}
export type Leaderboard = typeof(setmetatable(
	{} :: {
		_c: Config,
		_page: { Entry }?,
		_at: number,
		_limit: number,
		_lastWrite: { [number]: number },
		_lastValue: { [number]: number },
	},
	Leaderboard
))

function Leaderboard.new(config: Config): Leaderboard
	assert(config.ttl >= 1, "ttl must be at least 1 second")
	return setmetatable(
		{ _c = config, _page = nil, _at = -math.huge, _limit = 0, _lastWrite = {}, _lastValue = {} },
		Leaderboard
	)
end

function Leaderboard.clean(self: Leaderboard, score: any): number?
	if type(score) ~= "number" or score ~= score or score < 0 or score == math.huge then
		return nil
	end
	local s = math.floor(score)
	if s > (self._c.maxScore or 1e12) then
		return nil
	end
	return s
end

function Leaderboard.top(self: Leaderboard, limit: number): { Entry }
	local now = self._c.now()
	if self._page == nil or limit > self._limit or now - self._at >= self._c.ttl then
		local page = self._c.fetch(math.max(limit, self._limit))
		if page then
			self._page, self._at, self._limit = page, now, math.max(limit, self._limit)
		elseif self._page == nil then
			return {}
		end
	end
	local out = {}
	for i, e in self._page :: { Entry } do
		if i > limit then
			break
		end
		table.insert(out, e)
	end
	return out
end

function Leaderboard.shouldWrite(self: Leaderboard, userId: number, score: any): boolean
	local s = self:clean(score)
	if s == nil then
		return false
	end
	local now = self._c.now()
	if now - (self._lastWrite[userId] or -math.huge) < (self._c.minWriteGap or 30) then
		return false
	end
	if s <= (self._lastValue[userId] or -1) then
		return false
	end
	self._lastWrite[userId] = now
	self._lastValue[userId] = s
	return true
end

function Leaderboard.forget(self: Leaderboard, userId: number)
	self._lastWrite[userId] = nil
	self._lastValue[userId] = nil
end

function Leaderboard.rank(entries: { Entry }, key: string): number?
	for i, e in entries do
		if e.key == key then
			return i
		end
	end
	return nil
end

function Leaderboard.short(n: number): string
	local units: { { size: number, label: string } } = {
		{ size = 1e12, label = "T" },
		{ size = 1e9, label = "B" },
		{ size = 1e6, label = "M" },
		{ size = 1e3, label = "K" },
	}
	for _, u in units do
		if n >= u.size then
			local v = n / u.size
			if v >= 100 then
				return string.format("%d%s", math.floor(v), u.label)
			end
			return string.format("%.1f%s", math.floor(v * 10) / 10, u.label)
		end
	end
	return tostring(math.floor(n))
end

return Leaderboard
