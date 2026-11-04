--!strict
local ToastQueue = {}
ToastQueue.__index = ToastQueue

export type Toast = { key: string, text: string, priority: number, ttl: number? }
export type Shown = { key: string, text: string, priority: number, expires: number, count: number }
export type Options = { maxVisible: number?, maxQueued: number?, keyCooldown: number?, defaultTtl: number? }
export type Queue = typeof(setmetatable(
	{} :: {
		_maxVisible: number,
		_maxQueued: number,
		_cooldown: number,
		_ttl: number,
		_visible: { Shown },
		_queued: { Toast },
		_lastShown: { [string]: number },
	},
	ToastQueue
))

ToastQueue.CRITICAL = 100

function ToastQueue.new(options: Options?): Queue
	local o: Options = options or {}
	return setmetatable({
		_maxVisible = o.maxVisible or 3,
		_maxQueued = o.maxQueued or 12,
		_cooldown = o.keyCooldown or 2,
		_ttl = o.defaultTtl or 3,
		_visible = {},
		_queued = {},
		_lastShown = {},
	}, ToastQueue)
end

local function show(self: Queue, t: Toast, now: number)
	self._lastShown[t.key] = now
	table.insert(self._visible, {
		key = t.key,
		text = t.text,
		priority = t.priority,
		expires = now + (t.ttl or self._ttl),
		count = 1,
	})
end

function ToastQueue.push(self: Queue, t: Toast, now: number): string
	for _, v in self._visible do
		if v.key == t.key then
			v.count += 1
			v.expires = now + (t.ttl or self._ttl)
			v.text = t.text
			return "merged"
		end
	end
	local critical = t.priority >= ToastQueue.CRITICAL
	local last = self._lastShown[t.key]
	if not critical and last ~= nil and now - last < self._cooldown then
		return "dropped"
	end
	if #self._visible < self._maxVisible then
		show(self, t, now)
		return "shown"
	end
	if critical then
		local worst = 1
		for i, v in self._visible do
			if v.priority < self._visible[worst].priority then
				worst = i
			end
		end
		table.remove(self._visible, worst)
		show(self, t, now)
		return "shown"
	end
	if #self._queued >= self._maxQueued then
		local lowest = 1
		for i, q in self._queued do
			if q.priority < self._queued[lowest].priority then
				lowest = i
			end
		end
		if self._queued[lowest].priority >= t.priority then
			return "dropped"
		end
		table.remove(self._queued, lowest)
	end
	table.insert(self._queued, t)
	return "queued"
end

function ToastQueue.tick(self: Queue, now: number): { Shown }
	for i = #self._visible, 1, -1 do
		if self._visible[i].expires <= now then
			table.remove(self._visible, i)
		end
	end
	while #self._visible < self._maxVisible and #self._queued > 0 do
		local best = 1
		for i, q in self._queued do
			if q.priority > self._queued[best].priority then
				best = i
			end
		end
		show(self, table.remove(self._queued, best) :: Toast, now)
	end
	return self._visible
end

function ToastQueue.queuedCount(self: Queue): number
	return #self._queued
end

return ToastQueue
