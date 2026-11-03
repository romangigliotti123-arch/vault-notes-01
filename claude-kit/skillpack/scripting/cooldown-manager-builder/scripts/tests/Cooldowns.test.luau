--!nocheck
-- Run: lune run Cooldowns.test.luau   (from the kit's systems folder, see check-scripts.sh)
local t = require("../../../../../systems/_check/harness")
local Cooldowns = require("../Cooldowns")

local function setup()
	local now = 0
	local c = Cooldowns.new(function()
		return now
	end)
	return c, function(n)
		now = n
	end
end

t.test("first call passes, repeats fail until the duration has passed", function()
	local c, at = setup()
	t.truthy(c:Try(1, "Swing", 2))
	at(1.9)
	t.falsy(c:Try(1, "Swing", 2))
	at(2)
	t.truthy(c:Try(1, "Swing", 2))
end)

t.test("a failed Try does not extend the cooldown", function()
	local c, at = setup()
	c:Try(1, "Swing", 2)
	at(1)
	c:Try(1, "Swing", 2)
	at(2)
	t.truthy(c:Try(1, "Swing", 2))
end)

t.test("players and actions are independent", function()
	local c = setup()
	t.truthy(c:Try(1, "Swing", 5))
	t.truthy(c:Try(2, "Swing", 5))
	t.truthy(c:Try(1, "Dash", 5))
	t.falsy(c:Try(1, "Swing", 5))
end)

t.test("Remaining and IsReady", function()
	local c, at = setup()
	c:Try(1, "Swing", 4)
	at(1)
	t.eq(c:Remaining(1, "Swing"), 3)
	t.falsy(c:IsReady(1, "Swing"))
	at(10)
	t.eq(c:Remaining(1, "Swing"), 0)
	t.eq(c:Remaining(9, "Never"), 0)
end)

t.test("Reset and Clear free the action", function()
	local c = setup()
	c:Try(1, "Swing", 99)
	c:Reset(1, "Swing")
	t.truthy(c:Try(1, "Swing", 99))
	c:Clear(1)
	t.truthy(c:Try(1, "Swing", 99))
end)

t.test("Sweep removes expired entries only", function()
	local c, at = setup()
	c:Try(1, "A", 1)
	c:Try(1, "B", 10)
	c:Try(2, "A", 1)
	at(5)
	t.eq(c:Sweep(), 2)
	t.eq(c:Remaining(1, "B"), 5)
	t.truthy(c._until[2] == nil)
end)

t.test("Gate runs the function only when ready", function()
	local c = setup()
	local n = 0
	t.truthy(c:Gate(1, "X", 1, function()
		n += 1
	end))
	t.falsy(c:Gate(1, "X", 1, function()
		n += 1
	end))
	t.eq(n, 1)
end)

t.done()
