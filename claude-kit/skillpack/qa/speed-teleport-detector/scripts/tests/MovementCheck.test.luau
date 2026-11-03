--!nocheck
-- Run from the kit's systems folder: lune run ../skillpack/qa/speed-teleport-detector/scripts/tests/MovementCheck.test.luau
local t = require("../../../../../systems/_check/harness")
local MovementCheck = require("../MovementCheck")

local function p(x, y, z)
	return { x = x, y = y or 0, z = z or 0 }
end

print("MovementCheck")

t.test("walking at normal speed stays ok", function()
	local m = MovementCheck.new()
	m:Sample("a", p(0), 0)
	for i = 1, 10 do
		t.eq(m:Sample("a", p(i * 4), i * 0.5).kind, "ok") -- 8 studs/s
	end
end)

t.test("double speed is flagged and the reset point is the last valid position", function()
	local m = MovementCheck.new()
	m:Sample("a", p(0), 0)
	m:Sample("a", p(8), 0.5)
	local v = m:Sample("a", p(8 + 40), 1.5) -- 40 studs in 1 s, allowed 16*1+2
	t.eq(v.kind, "speed")
	t.eq(v.resetTo.x, 8)
	t.truthy(v.excess > 20)
end)

t.test("a big jump is a teleport, not speed", function()
	local m = MovementCheck.new()
	m:Sample("a", p(0), 0)
	t.eq(m:Sample("a", p(500), 1).kind, "teleport")
end)

t.test("small lag spike inside the margin is tolerated", function()
	local m = MovementCheck.new()
	m:Sample("a", p(0), 0)
	t.eq(m:Sample("a", p(17.5), 1).kind, "ok")
end)

t.test("exempt window allows a legit teleport and moves the baseline", function()
	local m = MovementCheck.new()
	m:Sample("a", p(0), 0)
	m:Exempt("a", 2, 0.5)
	t.eq(m:Sample("a", p(900), 1).kind, "exempt")
	t.eq(m:Sample("a", p(904), 3).kind, "ok") -- exemption over, baseline is the new place
end)

t.test("a speed boost raises the allowance for that player only", function()
	local m = MovementCheck.new()
	m:Sample("a", p(0), 0)
	m:Sample("b", p(0), 0)
	m:SetSpeed("a", 32)
	t.eq(m:Sample("a", p(30), 1).kind, "ok")
	t.eq(m:Sample("b", p(30), 1).kind, "speed")
end)

t.test("falling is ignored but climbing faster than a jump is fly", function()
	local m = MovementCheck.new()
	m:Sample("a", p(0, 100), 0)
	t.eq(m:Sample("a", p(0, 10), 1).kind, "ok")
	t.eq(m:Sample("a", p(0, 200), 2).kind, "fly")
end)

t.test("airborne too long is fly even with no big position change", function()
	local m = MovementCheck.new({ maxAirtime = 3 })
	m:Sample("a", p(0, 50), 0, true)
	local kind = "ok"
	for i = 1, 8 do
		kind = m:Sample("a", p(0, 50), i, true).kind
	end
	t.eq(kind, "fly")
	t.eq(m:Sample("a", p(0, 50), 9, false).kind, "ok")
end)

t.test("NaN position never becomes the baseline", function()
	local m = MovementCheck.new()
	m:Sample("a", p(0), 0)
	local v = m:Sample("a", p(0 / 0), 1)
	t.eq(v.kind, "teleport")
	t.eq(v.resetTo.x, 0)
	t.eq(m:Sample("a", p(5), 1.5).kind, "ok")
end)

t.test("a long silent gap re-baselines instead of accusing", function()
	local m = MovementCheck.new()
	m:Sample("a", p(0), 0)
	t.eq(m:Sample("a", p(300), 60).kind, "exempt")
end)

t.done()
