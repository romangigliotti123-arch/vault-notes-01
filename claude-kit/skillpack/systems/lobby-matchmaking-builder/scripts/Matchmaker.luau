--!strict
local Matchmaker = {}
Matchmaker.__index = Matchmaker

export type Config = { minSize: number, maxSize: number, waitSeconds: number, now: () -> number }
type Party = { ids: { number }, at: number }
export type Matchmaker = typeof(setmetatable(
	{} :: { _c: Config, _q: { Party }, _in: { [number]: boolean } },
	Matchmaker
))

function Matchmaker.new(config: Config): Matchmaker
	assert(config.minSize >= 1 and config.maxSize >= config.minSize, "need 1 <= minSize <= maxSize")
	return setmetatable({ _c = config, _q = {}, _in = {} }, Matchmaker)
end

function Matchmaker.enqueue(self: Matchmaker, ids: { number }): (boolean, string)
	if #ids == 0 or #ids > self._c.maxSize then
		return false, "party size"
	end
	local seen: { [number]: boolean } = {}
	for _, id in ids do
		if self._in[id] or seen[id] then
			return false, "already queued"
		end
		seen[id] = true
	end
	for _, id in ids do
		self._in[id] = true
	end
	table.insert(self._q, { ids = table.clone(ids), at = self._c.now() })
	return true, "ok"
end

function Matchmaker.leave(self: Matchmaker, userId: number)
	if not self._in[userId] then
		return
	end
	self._in[userId] = nil
	for i = #self._q, 1, -1 do
		local p = self._q[i]
		local at = table.find(p.ids, userId)
		if at then
			table.remove(p.ids, at)
			if #p.ids == 0 then
				table.remove(self._q, i)
			end
		end
	end
end

function Matchmaker.size(self: Matchmaker): number
	local n = 0
	for _, p in self._q do
		n += #p.ids
	end
	return n
end

function Matchmaker.step(self: Matchmaker): { { number } }
	local matches: { { number } } = {}
	while #self._q > 0 do
		local now = self._c.now()
		local group: { number } = {}
		local used: { number } = {}
		for i, p in self._q do
			if #group + #p.ids <= self._c.maxSize then
				for _, id in p.ids do
					table.insert(group, id)
				end
				table.insert(used, i)
			end
		end
		local oldestWaited = now - self._q[1].at
		local full = #group >= self._c.maxSize
		local ready = #group >= self._c.minSize and oldestWaited >= self._c.waitSeconds
		if not (full or ready) then
			break
		end
		for k = #used, 1, -1 do
			table.remove(self._q, used[k])
		end
		for _, id in group do
			self._in[id] = nil
		end
		table.insert(matches, group)
	end
	return matches
end

return Matchmaker
