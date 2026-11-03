--!nocheck
-- Run: lune run Mocks.test.luau   (from the kit's systems folder, see check-scripts.sh)
local t = require("../../../../../systems/_check/harness")
local Mocks = require("../Mocks")
local Cooldowns = require("../../../cooldown-manager-builder/scripts/Cooldowns")

t.test("clock reads and advances", function()
	local c = Mocks.clock(10)
	t.eq(c.read(), 10)
	c.advance(2.5)
	t.eq(c.read(), 12.5)
end)

t.test("spy records calls and forwards to the inner function", function()
	local spy = Mocks.spy(function(x)
		return x * 2
	end)
	t.eq(spy.fn(3), 6)
	spy.fn(4)
	t.eq(spy.count, 2)
	t.eq(spy.calls, { { 3 }, { 4 } })
end)

t.test("signal connects, fires and disconnects", function()
	local s = Mocks.signal()
	local got = {}
	local c = s:Connect(function(a, b)
		table.insert(got, a + b)
	end)
	s:Fire(1, 2)
	c:Disconnect()
	s:Fire(5, 5)
	t.eq(got, { 3 })
	t.eq(s:ConnectionCount(), 0)
end)

t.test("remote delivers client calls to the server handler and records server sends", function()
	local r = Mocks.remote()
	local seen
	r.OnServerEvent:Connect(function(player, action, qty)
		seen = { player.UserId, action, qty }
	end)
	r:FireFromClient(Mocks.player(7), "buy", 3)
	t.eq(seen, { 7, "buy", 3 })
	r:FireClient(Mocks.player(7), "ok")
	t.eq(#r.sent, 1)
	t.eq(r.sent[1].args, { "ok" })
end)

t.test("player leaves", function()
	local p = Mocks.player(5, "Bob")
	t.eq(p.Name, "Bob")
	t.truthy(p.Parent)
	p:Leave()
	t.eq(p.Parent, nil)
end)

t.test("store fails the requested number of times, then works", function()
	local s = Mocks.store()
	s:failNext(2)
	t.falsy(pcall(s.SetAsync, s, "k", 1))
	t.falsy(pcall(s.GetAsync, s, "k"))
	t.truthy(pcall(s.SetAsync, s, "k", 1))
	t.eq(s:GetAsync("k"), 1)
	t.eq(
		s:UpdateAsync("k", function(old)
			return old + 1
		end),
		2
	)
	t.eq(s.calls, 5)
end)

t.test("example: a real module tested with the mocks (Cooldowns with a fake clock)", function()
	local clock = Mocks.clock()
	local c = Cooldowns.new(clock.read)
	t.truthy(c:Try(1, "Swing", 2))
	clock.advance(1)
	t.falsy(c:Try(1, "Swing", 2))
	clock.advance(1)
	t.truthy(c:Try(1, "Swing", 2))
end)

t.done()
