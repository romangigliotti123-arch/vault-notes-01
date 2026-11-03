--!strict
-- CurrencyCounter: the number logic behind a currency label: abbreviation that never rounds up into the next unit, and a count-up
-- that reaches the target in a bounded time. Pure; the TextLabel update and the tween/Heartbeat hookup are the caller's.
--   CurrencyCounter.format(1234567) -> "1.23M"      CurrencyCounter.format(999999) -> "999.99K"
--   local c = CurrencyCounter.new(100); c:set(5000); c:update(dt) -> integer to display
-- The balance shown is cosmetic: the server's value is the truth (kit PlayerData). On a mismatch call `snap`.
local CurrencyCounter = {}
CurrencyCounter.__index = CurrencyCounter

export type Counter = typeof(setmetatable(
	{} :: { _shown: number, _target: number, _speed: number, _duration: number, _instantDown: boolean },
	CurrencyCounter
))
export type Options = { duration: number?, instantOnDecrease: boolean? }

local UNITS: { { size: number, suffix: string } } = {
	{ size = 1e12, suffix = "T" },
	{ size = 1e9, suffix = "B" },
	{ size = 1e6, suffix = "M" },
	{ size = 1e3, suffix = "K" },
}

local function trim(x: number, decimals: number): string
	local f = 10 ^ decimals
	local s = string.format(`%.{decimals}f`, math.floor(x * f) / f) -- floor, never round up
	s = string.gsub(s, "%.?0+$", "")
	return s
end

function CurrencyCounter.format(n: number): string
	local sign = if n < 0 then "-" else ""
	local a = math.abs(math.floor(n))
	if a < 1000 then
		return sign .. tostring(a)
	end
	for _, u in UNITS do
		if a >= u.size then
			return sign .. trim(a / u.size, 2) .. u.suffix
		end
	end
	return sign .. tostring(a)
end

function CurrencyCounter.new(initial: number, options: Options?): Counter
	local o: Options = options or {}
	return setmetatable({
		_shown = initial,
		_target = initial,
		_speed = 0,
		_duration = o.duration or 0.6,
		_instantDown = o.instantOnDecrease ~= false,
	}, CurrencyCounter)
end

function CurrencyCounter.set(self: Counter, target: number)
	if target < self._shown and self._instantDown then
		self._shown, self._target, self._speed = target, target, 0
		return
	end
	self._target = target
	self._speed = math.max(1, math.abs(target - self._shown) / self._duration)
end

function CurrencyCounter.snap(self: Counter, value: number)
	self._shown, self._target, self._speed = value, value, 0
end

-- Advance by dt seconds; returns the integer to display. Never overshoots the target.
function CurrencyCounter.update(self: Counter, dt: number): number
	if self._shown ~= self._target then
		local step = self._speed * dt
		if self._shown < self._target then
			self._shown = math.min(self._target, self._shown + step)
		else
			self._shown = math.max(self._target, self._shown - step)
		end
	end
	return math.floor(self._shown)
end

function CurrencyCounter.isSettled(self: Counter): boolean
	return self._shown == self._target
end

return CurrencyCounter
