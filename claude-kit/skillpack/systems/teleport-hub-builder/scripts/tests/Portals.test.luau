--!nocheck
-- Run from the kit's systems folder: lune run ../skillpack/systems/teleport-hub-builder/scripts/tests/Portals.test.luau
local t = require("../../../../../systems/_check/harness")
local Portals = require("../Portals")

local clock = 0
local function make()
	return Portals.new({
		now = function()
			return clock
		end,
		cooldown = 3,
		maxGroup = 2,
		destinations = { Forest = { placeId = 555, reserved = true, maxParty = 5 }, Draft = { placeId = 0 } },
	})
end

t.test("only named destinations resolve; non-strings and unset ids are refused", function()
	local p = make()
	t.eq((p:plan("Atlantis", { 1 })), nil)
	t.eq((p:plan(555, { 1 })), nil)
	t.eq((p:plan({}, { 1 })), nil)
	local plan, why = p:plan("Draft", { 1 })
	t.eq(plan, nil)
	t.truthy(string.find(why, "SET IN CREATOR HUB"))
end)

t.test("a party is split into batches of maxGroup", function()
	local p = make()
	local plan = p:plan("Forest", { 1, 2, 3, 4, 5 })
	t.eq(plan.groups, { { 1, 2 }, { 3, 4 }, { 5 } })
	t.eq(plan.reserved, true)
	t.eq(plan.placeId, 555)
end)

t.test("party size limits and empty parties are refused", function()
	local p = make()
	t.eq((p:plan("Forest", {})), nil)
	t.eq((p:plan("Forest", { 1, 2, 3, 4, 5, 6 })), nil)
end)

t.test("cooldown blocks a second teleport; failed() releases it", function()
	local p = make()
	t.truthy(p:plan("Forest", { 1 }))
	local plan, why = p:plan("Forest", { 1 })
	t.eq(plan, nil)
	t.eq(why, "cooldown")
	clock = 3
	t.truthy(p:plan("Forest", { 1 }))
	p:failed({ 1 })
	t.truthy(p:plan("Forest", { 1 }))
end)

t.test("retry delays back off and stop", function()
	local p = make()
	t.eq({ p:retryDelay(1), p:retryDelay(2), p:retryDelay(3), p:retryDelay(4), p:retryDelay(5) }, { 1, 2, 4, 8, 8 })
	t.eq(p:retryDelay(6), nil)
end)

t.done()
