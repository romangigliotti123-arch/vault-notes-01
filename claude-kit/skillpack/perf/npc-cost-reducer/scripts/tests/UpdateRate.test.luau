--!nocheck
local t = require("../../../../../systems/_check/harness")
local UpdateRate = require("../UpdateRate")

t.test("rings pick the rate by distance and park far NPCs", function()
	t.eq(UpdateRate.hzFor(50), 30)
	t.eq(UpdateRate.hzFor(100), 30)
	t.eq(UpdateRate.hzFor(101), 10)
	t.eq(UpdateRate.hzFor(400), 3)
	t.eq(UpdateRate.hzFor(900), 0)
end)

t.test("a 10 Hz NPC updates exactly 10 times in 60 frames", function()
	local n = 0
	for frame = 1, 60 do
		if UpdateRate.shouldUpdate(frame, 7, 10) then
			n += 1
		end
	end
	t.eq(n, 10)
end)

t.test("staggering spreads 60 NPCs at 10 Hz evenly: 10 per frame", function()
	for frame = 1, 12 do
		local n = 0
		for id = 1, 60 do
			if UpdateRate.shouldUpdate(frame, id, 10) then
				n += 1
			end
		end
		t.eq(n, 10)
	end
end)

t.test("parked NPCs never update", function()
	for frame = 1, 120 do
		t.falsy(UpdateRate.shouldUpdate(frame, 3, 0))
	end
end)

t.test("a crowd mostly beyond 250 studs saves most of the work", function()
	local d = {}
	for i = 1, 100 do
		d[i] = if i <= 10 then 50 else 600
	end
	local saved = UpdateRate.savedPercent(d)
	t.truthy(saved > 94 and saved < 96, "saved " .. saved)
end)

t.done()
