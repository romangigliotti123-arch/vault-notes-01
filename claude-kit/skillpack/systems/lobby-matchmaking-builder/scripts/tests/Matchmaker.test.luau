--!nocheck
-- Run from the kit's systems folder: lune run ../skillpack/systems/lobby-matchmaking-builder/scripts/tests/Matchmaker.test.luau
local t = require("../../../../../systems/_check/harness")
local Matchmaker = require("../Matchmaker")

local clock = 0
local function make()
	return Matchmaker.new({
		minSize = 3,
		maxSize = 4,
		waitSeconds = 30,
		now = function()
			return clock
		end,
	})
end

t.test("a full match starts immediately", function()
	clock = 0
	local m = make()
	m:enqueue({ 1 })
	m:enqueue({ 2 })
	m:enqueue({ 3 })
	t.eq(#m:step(), 0)
	m:enqueue({ 4 })
	t.eq(m:step(), { { 1, 2, 3, 4 } })
	t.eq(m:size(), 0)
end)

t.test("a short match starts after the wait if the minimum is met", function()
	clock = 0
	local m = make()
	m:enqueue({ 1 })
	m:enqueue({ 2 })
	m:enqueue({ 3 })
	clock = 29
	t.eq(#m:step(), 0)
	clock = 30
	t.eq(m:step(), { { 1, 2, 3 } })
end)

t.test("below the minimum nobody starts, however long they wait", function()
	clock = 0
	local m = make()
	m:enqueue({ 1 })
	m:enqueue({ 2 })
	clock = 999
	t.eq(#m:step(), 0)
end)

t.test("parties stay together and are never split", function()
	clock = 0
	local m = make()
	m:enqueue({ 1, 2, 3 })
	m:enqueue({ 4, 5 })
	t.eq(m:step(), {})
	clock = 30
	t.eq(m:step(), { { 1, 2, 3 } })
	t.eq(m:size(), 2)
end)

t.test("double queueing and oversized or empty parties are refused", function()
	local m = make()
	t.truthy((m:enqueue({ 1, 2 })))
	t.falsy((m:enqueue({ 2, 9 })))
	t.falsy((m:enqueue({ 7, 7 })))
	t.falsy((m:enqueue({ 1, 2, 3, 4, 5 })))
	t.falsy((m:enqueue({})))
end)

t.test("leaving removes the player and lets them queue again", function()
	clock = 0
	local m = make()
	m:enqueue({ 1, 2 })
	m:leave(1)
	t.eq(m:size(), 1)
	t.truthy((m:enqueue({ 1 })))
	m:leave(99)
	t.eq(m:size(), 2)
end)

t.done()
