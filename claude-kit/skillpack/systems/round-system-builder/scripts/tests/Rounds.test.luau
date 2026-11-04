--!nocheck
local t = require("../../../../../systems/_check/harness")
local Rounds = require("../Rounds")

local function make(extra)
	local ev = { starts = {}, ends = {}, cleanups = 0 }
	local cfg = {
		minPlayers = 2,
		intermission = 3,
		roundLength = 10,
		endScreen = 2,
		joinGrace = 2,
		onStart = function(ids)
			table.insert(ev.starts, ids)
		end,
		onEnd = function(reason, survivors)
			table.insert(ev.ends, { reason, survivors })
		end,
		cleanup = function()
			ev.cleanups += 1
		end,
	}
	for k, v in extra or {} do
		cfg[k] = v
	end
	return Rounds.new(cfg), ev
end

local function run(r, seconds, ready)
	for _ = 1, seconds do
		r:tick(1, ready)
	end
end

t.test("waits for enough players, then counts down, then plays", function()
	local r, ev = make()
	r:join(1)
	r:join(2)
	r:tick(1, 1)
	t.eq(r.state, "Waiting")
	r:tick(1, 2)
	t.eq(r.state, "Intermission")
	run(r, 3, 2)
	t.eq(r.state, "Playing")
	t.eq(ev.starts[1], { 1, 2 })
end)

t.test("the countdown aborts if players drop below the minimum", function()
	local r = make()
	r:join(1)
	r:join(2)
	r:tick(1, 2)
	r:tick(1, 1)
	t.eq(r.state, "Waiting")
end)

t.test("round ends on time, runs end hook and cleanup, returns to Waiting", function()
	local r, ev = make()
	r:join(1)
	r:join(2)
	run(r, 4, 2)
	run(r, 10, 2)
	t.eq(r.state, "Ending")
	t.eq(ev.ends[1][1], "time")
	run(r, 2, 2)
	t.eq(r.state, "Waiting")
	t.eq(ev.cleanups, 1)
end)

t.test("last player standing ends the round early", function()
	local r, ev = make()
	r:join(1)
	r:join(2)
	run(r, 4, 2)
	r:out(2)
	r:tick(1, 2)
	t.eq(r.state, "Ending")
	t.eq(ev.ends[1], { "last standing", { 1 } })
end)

t.test("late joiners play only inside the grace window", function()
	local r = make()
	r:join(1)
	r:join(2)
	run(r, 4, 3)
	t.eq(r:join(3), "play")
	run(r, 5, 3)
	t.eq(r:join(4), "spectate")
	t.eq(r:aliveCount(), 3)
end)

t.test("everyone leaving ends the round as empty", function()
	local r, ev = make()
	r:join(1)
	r:join(2)
	run(r, 4, 2)
	r:out(1)
	r:out(2)
	r:tick(1, 0)
	t.eq(ev.ends[1][1], "empty")
end)

t.done()
