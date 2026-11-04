--!nocheck
local t = require("../../../../../systems/_check/harness")
local Honeypot = require("../Honeypot")

local function make(over)
	local clock = { t = 0 }
	local cfg = {
		now = function()
			return clock.t
		end,
	}
	for k, v in over or {} do
		cfg[k] = v
	end
	return Honeypot.new(cfg), clock
end

print("Honeypot")

t.test("score climbs the ladder one rung at a time", function()
	local h = make()
	t.eq(h:Flag(1, "speed", 1), "log")
	t.eq(h:Flag(1, "speed", 1), "log")
	t.eq(h:Flag(1, "speed", 1), "mitigate")
	t.eq(h:Flag(1, "rate", 3), "restrict")
	t.eq(h:Flag(1, "rate", 4), "review")
end)

t.test("a honeypot trip goes straight to review", function()
	local h = make()
	t.eq(h:Trip(7, "AddMoney"), "review")
	t.eq(h:Log()[1].reason, "honeypot:AddMoney")
end)

t.test("score decays so one lag spike a day never reaches review", function()
	local h, clock = make()
	h:Flag(1, "speed", 2)
	clock.t = 600
	t.eq(h:Score(1), 0)
	t.eq(h:Flag(1, "speed", 1), "log")
end)

t.test("watch list holds suspects without banning anyone", function()
	local h = make()
	h:Flag(5, "speed", 1)
	h:Flag(2, "speed", 1)
	t.eq(h:WatchList(), { 2, 5 })
end)

t.test("exempt accounts are skipped (and this is why you test with a normal account)", function()
	local h = make({
		exempt = function(id)
			return id == 99
		end,
	})
	t.eq(h:Trip(99, "AddMoney"), "none")
	t.eq(#h:Log(), 0)
end)

t.test("log is bounded", function()
	local h = make({ maxLog = 3 })
	for i = 1, 10 do
		h:Flag(i, "x", 1)
	end
	t.eq(#h:Log(), 3)
	t.eq(h:Log()[3].userId, 10)
end)

t.done()
