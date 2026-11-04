--!strict
local Pool = {}
Pool.__index = Pool

export type Options<T> = {
	create: () -> T,
	reset: (item: T) -> (),
	max: number,
	prewarm: number?,
	whenFull: string?,
}
export type Stats = { free: number, inUse: number, created: number, recycled: number, refused: number }
export type Pool<T> = typeof(setmetatable(
	{} :: {
		_options: Options<T>,
		_free: { T },
		_inUse: { T },
		_created: number,
		_recycled: number,
		_refused: number,
	},
	Pool
))

function Pool.new<T>(options: Options<T>): Pool<T>
	assert(options.max >= 1, "Pool max must be at least 1")
	local self = setmetatable({
		_options = options,
		_free = {},
		_inUse = {},
		_created = 0,
		_recycled = 0,
		_refused = 0,
	}, Pool)
	for _ = 1, math.min(options.prewarm or 0, options.max) do
		local item = options.create()
		options.reset(item)
		self._created += 1
		table.insert(self._free, item)
	end
	return self
end

function Pool.Acquire<T>(self: Pool<T>): T?
	local free = self._free
	if #free > 0 then
		local item = table.remove(free) :: T
		table.insert(self._inUse, item)
		return item
	end
	if self._created < self._options.max then
		local item = self._options.create()
		self._created += 1
		table.insert(self._inUse, item)
		return item
	end
	if self._options.whenFull == "recycleOldest" and #self._inUse > 0 then
		local oldest = table.remove(self._inUse, 1) :: T
		self._options.reset(oldest)
		self._recycled += 1
		table.insert(self._inUse, oldest)
		return oldest
	end
	self._refused += 1
	return nil
end

function Pool.Release<T>(self: Pool<T>, item: T): boolean
	local at = table.find(self._inUse, item)
	if at == nil then
		return false
	end
	table.remove(self._inUse, at)
	self._options.reset(item)
	table.insert(self._free, item)
	return true
end

function Pool.Stats<T>(self: Pool<T>): Stats
	return {
		free = #self._free,
		inUse = #self._inUse,
		created = self._created,
		recycled = self._recycled,
		refused = self._refused,
	}
end

function Pool.Destroy<T>(self: Pool<T>, destroyItem: (item: T) -> ())
	for _, item in self._free do
		destroyItem(item)
	end
	for _, item in self._inUse do
		destroyItem(item)
	end
	table.clear(self._free)
	table.clear(self._inUse)
	self._created = 0
end

return Pool
