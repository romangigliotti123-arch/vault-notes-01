--!nocheck
local t = require("../../../../../systems/_check/harness")
local Checkpoints = require("../Checkpoints")

local clock = 0
local function make()
	return Checkpoints.new({
		stages = 5,
		minStageSeconds = 2,
		maxFlags = 2,
		now = function()
			return clock
		end,
	})
end

t.test("advances one stage at a time, in order", function()
	clock = 0
	local d, c = {}, make()
	t.eq({ c:touch(d, 1, 1) }, { true, "advanced" })
	clock = 5
	t.eq({ c:touch(d, 1, 2) }, { true, "advanced" })
	t.eq(c:stage(d), 2)
end)

t.test("skipping ahead is refused and changes nothing", function()
	local d, c = {}, make()
	t.eq({ c:touch(d, 1, 3) }, { false, "skipped" })
	t.eq(c:stage(d), 0)
end)

t.test("touching an old stage is harmless", function()
	clock = 0
	local d, c = {}, make()
	c:touch(d, 1, 1)
	t.eq({ c:touch(d, 1, 1) }, { true, "already" })
	t.eq(c:stage(d), 1)
end)

t.test("too-fast clears are refused, counted, and flagged after the limit", function()
	clock = 0
	local d, c = {}, make()
	c:touch(d, 1, 1)
	clock = 0.5
	t.eq({ c:touch(d, 1, 2) }, { false, "too fast" })
	t.eq({ c:touch(d, 1, 2) }, { false, "too fast" })
	t.truthy(c:suspicious(1))
	clock = 3
	t.eq({ c:touch(d, 1, 2) }, { true, "advanced" })
end)

t.test("bad stage values are refused", function()
	local d, c = {}, make()
	for _, bad in { 0, -1, 6, 1.5, "2", 0 / 0 } do
		t.eq((c:touch(d, 1, bad)), false)
	end
end)

t.test("finishing records the time; reset clears progress", function()
	clock = 0
	local d, c = {}, make()
	for i = 1, 5 do
		clock += 3
		c:touch(d, 1, i)
	end
	t.truthy(d.Obby.finishedAt)
	c:reset(d, 1)
	t.eq(c:respawnStage(d), 0)
end)

t.done()
