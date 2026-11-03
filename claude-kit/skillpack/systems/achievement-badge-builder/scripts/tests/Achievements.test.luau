--!nocheck
-- Run from the kit's systems folder: lune run ../skillpack/systems/achievement-badge-builder/scripts/tests/Achievements.test.luau
local t = require("../../../../../systems/_check/harness")
local Achievements = require("../Achievements")

local calls, failFor
local function make(maxAttempts)
	calls, failFor = {}, 0
	return Achievements.new({
		maxAttempts = maxAttempts,
		defs = { win = { badgeId = 11 }, draft = { badgeId = 0 } },
		award = function(userId, badgeId)
			table.insert(calls, userId .. ":" .. badgeId)
			if failFor > 0 then
				failFor -= 1
				return false
			end
			return true
		end,
	})
end

t.test("unlock is true once and queues exactly one badge call", function()
	local d, a = {}, make()
	t.truthy(a:unlock(5, d, "win"))
	t.falsy(a:unlock(5, d, "win"))
	t.eq(a:flush(5, d), 1)
	t.eq(a:flush(5, d), 0)
	t.eq(calls, { "5:11" })
end)

t.test("a failed award is retried and never lost or doubled", function()
	local d, a = {}, make()
	a:unlock(5, d, "win")
	failFor = 2
	t.eq(a:flush(5, d), 0)
	t.eq(a:flush(5, d), 0)
	t.eq(a:flush(5, d), 1)
	t.eq(a:flush(5, d), 0)
	t.eq(#calls, 3)
end)

t.test("badge id 0 unlocks without any badge call", function()
	local d, a = {}, make()
	t.truthy(a:unlock(5, d, "draft"))
	a:flush(5, d)
	t.eq(#calls, 0)
	t.truthy(a:has(d, "draft"))
end)

t.test("unknown ids unlock nothing", function()
	local d, a = {}, make()
	t.falsy(a:unlock(5, d, "nope"))
	t.falsy(a:has(d, "nope"))
end)

t.test("attempts park after the limit and resume next session", function()
	local d, a = {}, make(2)
	a:unlock(5, d, "win")
	failFor = 99
	a:flush(5, d)
	a:flush(5, d)
	a:flush(5, d)
	t.eq(#calls, 2)
	failFor = 0
	a:resetAttempts(d)
	t.eq(a:flush(5, d), 1)
end)

t.done()
