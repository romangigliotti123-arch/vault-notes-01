--!strict
local Checkpoints = {}
Checkpoints.__index = Checkpoints

export type Data = { [any]: any }
export type Config = { stages: number, minStageSeconds: number, now: () -> number, maxFlags: number? }
export type Checkpoints = typeof(setmetatable(
	{} :: { _c: Config, _last: { [number]: number }, flags: { [number]: number } },
	Checkpoints
))

function Checkpoints.new(config: Config): Checkpoints
	assert(config.stages >= 1 and config.minStageSeconds >= 0, "bad checkpoint config")
	return setmetatable({ _c = config, _last = {}, flags = {} }, Checkpoints)
end

function Checkpoints.stage(_self: Checkpoints, data: Data): number
	local o = data.Obby
	if type(o) ~= "table" then
		o = { stage = 0 }
		data.Obby = o
	end
	return o.stage
end

function Checkpoints.touch(self: Checkpoints, data: Data, userId: number, index: any): (boolean, string)
	if type(index) ~= "number" or index ~= math.floor(index) or index < 1 or index > self._c.stages then
		return false, "bad stage"
	end
	local cur = self:stage(data)
	if index <= cur then
		return true, "already"
	end
	if index ~= cur + 1 then
		return false, "skipped"
	end
	local now = self._c.now()
	local last = self._last[userId]
	if last and now - last < self._c.minStageSeconds then
		self.flags[userId] = (self.flags[userId] or 0) + 1
		return false, "too fast"
	end
	data.Obby.stage = index
	self._last[userId] = now
	if index == self._c.stages then
		data.Obby.finishedAt = os.time()
	end
	return true, "advanced"
end

function Checkpoints.suspicious(self: Checkpoints, userId: number): boolean
	return (self.flags[userId] or 0) >= (self._c.maxFlags or 5)
end

function Checkpoints.respawnStage(self: Checkpoints, data: Data): number
	return self:stage(data)
end

function Checkpoints.reset(self: Checkpoints, data: Data, userId: number)
	data.Obby = { stage = 0 }
	self._last[userId] = nil
	self.flags[userId] = nil
end

function Checkpoints.forget(self: Checkpoints, userId: number)
	self._last[userId] = nil
	self.flags[userId] = nil
end

return Checkpoints
