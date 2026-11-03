--!strict
-- LoadingProgress: honest progress for a loading screen. Weighted real tasks (assets preloaded, data received, character spawned)
-- give a raw fraction; the displayed bar smooths toward it, never moves backwards, never reaches 100% until every task is done,
-- and reports a stall so the screen can say something useful instead of freezing. Time is passed in.
--   local p = LoadingProgress.new({ { name = "assets", weight = 5 }, { name = "data", weight = 2 }, { name = "spawn", weight = 1 } })
--   p:set("assets", 0.4); p:done("data"); local shown = p:update(dt, now); if p:stalled(now, 10) then ... end
local LoadingProgress = {}
LoadingProgress.__index = LoadingProgress

export type Task = { name: string, weight: number }
export type Progress = typeof(setmetatable(
	{} :: {
		_weights: { [string]: number },
		_fraction: { [string]: number },
		_total: number,
		_shown: number,
		_lastChange: number,
		_speed: number,
	},
	LoadingProgress
))

function LoadingProgress.new(tasks: { Task }, maxSpeedPerSecond: number?): Progress
	local weights, fraction, total = {}, {}, 0
	for _, t in tasks do
		assert(t.weight > 0, "task weight must be positive")
		weights[t.name] = t.weight
		fraction[t.name] = 0
		total += t.weight
	end
	return setmetatable({
		_weights = weights,
		_fraction = fraction,
		_total = total,
		_shown = 0,
		_lastChange = 0,
		_speed = maxSpeedPerSecond or 1.5,
	}, LoadingProgress)
end

function LoadingProgress.set(self: Progress, name: string, f: number, now: number?)
	assert(self._weights[name] ~= nil, "unknown task " .. name)
	local clamped = math.clamp(f, 0, 1)
	if clamped > self._fraction[name] then -- progress only moves forward
		self._fraction[name] = clamped
		self._lastChange = now or self._lastChange
	end
end

function LoadingProgress.done(self: Progress, name: string, now: number?)
	self:set(name, 1, now)
end

function LoadingProgress.raw(self: Progress): number
	local sum = 0
	for name, w in self._weights do
		sum += w * self._fraction[name]
	end
	return sum / self._total
end

function LoadingProgress.isComplete(self: Progress): boolean
	for name in self._weights do
		if self._fraction[name] < 1 then
			return false
		end
	end
	return true
end

-- Smoothed value for the bar. Capped just under 1 until complete so the bar never lies about being finished.
function LoadingProgress.update(self: Progress, dt: number): number
	local target = self:raw()
	if not self:isComplete() then
		target = math.min(target, 0.99)
	end
	if target > self._shown then
		self._shown = math.min(target, self._shown + self._speed * dt)
	end
	return self._shown
end

function LoadingProgress.stalled(self: Progress, now: number, timeoutSeconds: number): boolean
	return not self:isComplete() and now - self._lastChange >= timeoutSeconds
end

-- Tip rotation: next index, never repeating the previous one when there is a choice.
function LoadingProgress.nextTip(count: number, last: number?, roll: number): number
	if count <= 1 then
		return 1
	end
	local pick = (math.floor(roll * (count - 1)) % (count - 1)) + 1
	if last ~= nil and pick >= last then
		pick += 1
	end
	return pick
end

return LoadingProgress
