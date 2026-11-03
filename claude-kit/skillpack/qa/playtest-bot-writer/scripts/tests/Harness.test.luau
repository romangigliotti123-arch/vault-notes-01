--!nocheck
-- Run from the kit's systems folder: lune run ../skillpack/qa/playtest-bot-writer/scripts/tests/Harness.test.luau
local t = require("../../../../../systems/_check/harness")
local Harness = require("../Harness")

local function fake()
	local now = 0
	local h = Harness.new("demo", function(s)
		now += s
	end, function()
		return now
	end)
	return h
end

t.test("check and checkEq record pass and fail", function()
	local h = fake()
	t.truthy(h:check("a", true))
	t.falsy(h:checkEq("b", 1, 2))
	t.eq(h:failures(), 1)
	t.truthy(string.find(h:report(), "FAIL b (expected 2, got 1)", 1, true))
	t.truthy(string.find(h:report(), "1/2 checks passed", 1, true))
end)

t.test("waitFor succeeds when the predicate turns true in time", function()
	local h = fake()
	local n = 0
	t.truthy(h:waitFor("counter", function()
		n += 1
		return n >= 3
	end, 5, 0.5))
	t.eq(h:failures(), 0)
end)

t.test("waitFor fails on timeout and survives a throwing predicate", function()
	local h = fake()
	t.falsy(h:waitFor("never", function()
		error("nope")
	end, 1, 0.25))
	t.eq(h:failures(), 1)
end)

t.test("step records an error instead of throwing", function()
	local h = fake()
	t.falsy(h:step("explodes", function()
		error("boom")
	end))
	t.truthy(string.find(h:report(), "error:", 1, true))
end)

t.done()
