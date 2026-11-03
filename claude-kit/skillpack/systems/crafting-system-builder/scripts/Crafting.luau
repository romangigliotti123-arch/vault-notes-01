--!strict
-- Crafting: data-driven recipes with a timed queue, built on Inventory. Ingredients are consumed when the craft STARTS (so they
-- cannot be traded away or crafted twice) and the result is delivered on collect, based on absolute os.time() stamps so it survives
-- leaving the game. State lives in data.Crafting.queue.
--   local crafting = Crafting.new({ inventory = inv, queueLimit = 3, now = os.time,
--       recipes = { Plank = { inputs = { Wood = 2 }, output = { id = "Plank", qty = 1 }, seconds = 30 } } })
--   crafting:start(data, "Plank") ; crafting:collect(data)   -- returns the list of finished crafts delivered
local Crafting = {}
Crafting.__index = Crafting

export type Data = { [any]: any }
export type Recipe = { inputs: { [string]: number }, output: { id: string, qty: number }, seconds: number }
export type Config = { inventory: any, recipes: { [string]: Recipe }, queueLimit: number, now: () -> number }
export type Crafting = typeof(setmetatable({} :: { _c: Config }, Crafting))

function Crafting.new(config: Config): Crafting
	for name, r in config.recipes do
		assert(r.seconds >= 0, `recipe {name}: seconds must be >= 0`)
		assert(next(r.inputs) ~= nil, `recipe {name}: needs at least one input`)
		assert(r.output.qty >= 1, `recipe {name}: output qty must be >= 1`)
		for id, q in r.inputs do
			assert(q >= 1 and q == math.floor(q), `recipe {name}: input {id} must be a positive integer`)
			assert(id ~= r.output.id, `recipe {name}: output is also an input (infinite loop recipe)`)
		end
	end
	return setmetatable({ _c = config }, Crafting)
end

function Crafting.init(_self: Crafting, data: Data): Data
	local c = data.Crafting
	if type(c) ~= "table" then
		c = { queue = {} }
		data.Crafting = c
	end
	c.queue = c.queue or {}
	return c
end

function Crafting.canStart(self: Crafting, data: Data, name: string): (boolean, string)
	local r = self._c.recipes[name]
	if r == nil then
		return false, "unknown recipe"
	end
	local c = self:init(data)
	if #c.queue >= self._c.queueLimit then
		return false, "queue full"
	end
	for id, q in r.inputs do
		if not self._c.inventory:has(data, id, q) then
			return false, "missing " .. id
		end
	end
	return true, "ok"
end

-- consumes the inputs now and queues the craft; all or nothing
function Crafting.start(self: Crafting, data: Data, name: string): (boolean, string)
	local ok, why = self:canStart(data, name)
	if not ok then
		return false, why
	end
	local r = self._c.recipes[name]
	local c = self:init(data)
	local taken: { { id: string, qty: number } } = {}
	for id, q in r.inputs do
		local removed = self._c.inventory:remove(data, id, q)
		if not removed then
			for _, t in taken do
				self._c.inventory:add(data, t.id, t.qty)
			end
			return false, "could not take " .. id
		end
		table.insert(taken, { id = id, qty = q })
	end
	local now = self._c.now()
	local last = c.queue[#c.queue]
	local startAt = if last then math.max(now, last.doneAt) else now
	table.insert(c.queue, { recipe = name, doneAt = startAt + r.seconds })
	return true, "ok"
end

function Crafting.ready(self: Crafting, data: Data): number
	local n, now = 0, self._c.now()
	for _, q in self:init(data).queue do
		if q.doneAt <= now then
			n += 1
		end
	end
	return n
end

-- deliver finished crafts in order. A craft stays queued when the output does not fit (nothing is lost).
function Crafting.collect(self: Crafting, data: Data): { string }
	local c = self:init(data)
	local now = self._c.now()
	local delivered: { string } = {}
	while c.queue[1] and c.queue[1].doneAt <= now do
		local r = self._c.recipes[c.queue[1].recipe]
		if r == nil then
			table.remove(c.queue, 1) -- recipe removed in an update: drop the entry (refund is a design decision, see SKILL pitfalls)
		elseif self._c.inventory:add(data, r.output.id, r.output.qty) then
			table.insert(delivered, c.queue[1].recipe)
			table.remove(c.queue, 1)
		else
			break
		end
	end
	return delivered
end

return Crafting
