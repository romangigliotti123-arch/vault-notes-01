--!nocheck
-- Run: lune run ActorDispatcher.test.luau   (from the kit's systems folder, see check-scripts.sh)
local t = require("../../../../../systems/_check/harness")
local ActorDispatcher = require("../ActorDispatcher")
local ParallelBatch = require("../ParallelBatch")

-- fake event: Fire runs handlers; fake actors double each item and reply after `delay` wait ticks (nil = never reply)
local function rig(delays)
	local now = 0
	local queue = {}
	local io = {
		newEvent = function()
			local handlers = {}
			return {
				Event = {
					Connect = function(_, fn)
						table.insert(handlers, fn)
						return {
							Disconnect = function()
								handlers = {}
							end,
						}
					end,
				},
				Fire = function(_, ...)
					for _, h in handlers do
						h(...)
					end
				end,
				Destroy = function() end,
			}
		end,
		wait = function()
			now += 1
			for i = #queue, 1, -1 do
				local job = queue[i]
				job.left -= 1
				if job.left <= 0 then
					table.remove(queue, i)
					job.fire()
				end
			end
		end,
		clock = function()
			return now
		end,
	}
	local actors = {}
	for n = 1, #delays do
		actors[n] = {
			SendMessage = function(_, _topic, index, chunk, done)
				local out = {}
				for i, v in chunk do
					out[i] = v * 2
				end
				if delays[n] then
					table.insert(queue, {
						left = delays[n],
						fire = function()
							done:Fire(index, out)
						end,
					})
				end
			end,
		}
	end
	return actors, io
end

t.test("results come back merged in item order even when actors finish out of order", function()
	local actors, io = rig({ 3, 1, 2 })
	local d = ActorDispatcher.new(actors, "Work", ParallelBatch, io)
	local out, err = d:Run({ 1, 2, 3, 4, 5, 6 }, 10)
	t.eq(err, nil)
	t.eq(out, { 2, 4, 6, 8, 10, 12 })
end)

t.test("an actor that never replies gives a timeout error naming the missing chunks", function()
	local actors, io = rig({ 1, false })
	local d = ActorDispatcher.new(actors, "Work", ParallelBatch, io)
	local out, err = d:Run({ 1, 2, 3, 4 }, 5)
	t.eq(out, nil)
	t.truthy(string.find(err, "1 of 2 chunks", 1, true))
end)

t.test("fewer items than actors uses only as many actors as items", function()
	local actors, io = rig({ 1, 1, 1, 1 })
	local d = ActorDispatcher.new(actors, "Work", ParallelBatch, io)
	t.eq((d:Run({ 5, 6 }, 5)), { 10, 12 })
end)

t.test("no items returns an empty result without waiting", function()
	local actors, io = rig({ 1 })
	local d = ActorDispatcher.new(actors, "Work", ParallelBatch, io)
	t.eq((d:Run({}, 5)), {})
end)

t.test("no actors is refused", function()
	t.falsy(pcall(ActorDispatcher.new, {}, "Work", ParallelBatch))
end)

t.done()
