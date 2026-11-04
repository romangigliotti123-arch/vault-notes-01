--!nocheck
local t = require("../../../../../systems/_check/harness")
local ParallelBatch = require("../ParallelBatch")

t.test("partition makes near-equal contiguous chunks and loses nothing", function()
	local chunks = ParallelBatch.partition({ 1, 2, 3, 4, 5, 6, 7 }, 3)
	t.eq(chunks, { { 1, 2, 3 }, { 4, 5 }, { 6, 7 } })
end)

t.test("partition never makes empty chunks", function()
	t.eq(ParallelBatch.partition({ 1, 2 }, 5), { { 1 }, { 2 } })
	t.eq(ParallelBatch.partition({}, 4), {})
	t.eq(ParallelBatch.partition({ 1, 2, 3 }, 0), { { 1, 2, 3 } })
end)

t.test("merge restores order even when chunks finish out of order", function()
	t.eq(ParallelBatch.merge({ [3] = { "e" }, [1] = { "a", "b" }, [2] = { "c", "d" } }), { "a", "b", "c", "d", "e" })
end)

t.test("partition then merge is the identity", function()
	local items = {}
	for i = 1, 50 do
		items[i] = i * 3
	end
	local chunks = ParallelBatch.partition(items, 7)
	t.eq(ParallelBatch.merge(chunks), items)
end)

t.test("plan keeps tiny work serial", function()
	local p = ParallelBatch.plan(10, 0.01, 16, 8)
	t.falsy(p.parallel)
end)

t.test("plan picks parallel for heavy work and caps workers by item count", function()
	local p = ParallelBatch.plan(400, 0.1, 16, 8)
	t.truthy(p.parallel)
	t.eq(p.workers, 8)
	t.eq(ParallelBatch.plan(3, 20, 16, 8).workers, 3)
end)

t.test("plan refuses when overhead eats the gain", function()
	local p = ParallelBatch.plan(40, 0.2, 16, 8, 5)
	t.falsy(p.parallel)
end)

t.done()
