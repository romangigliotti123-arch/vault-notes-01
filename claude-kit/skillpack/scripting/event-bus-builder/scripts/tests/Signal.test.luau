--!nocheck
local t = require("../../../../../systems/_check/harness")
local Signal = require("../Signal")

t.test("handlers run in connection order with the fired arguments", function()
	local s = Signal.new()
	local log = {}
	s:Connect(function(a, b)
		table.insert(log, "1:" .. a .. b)
	end)
	s:Connect(function(a)
		table.insert(log, "2:" .. a)
	end)
	s:Fire("x", "y")
	t.eq(log, { "1:xy", "2:x" })
end)

t.test("Disconnect stops delivery and is idempotent", function()
	local s = Signal.new()
	local n = 0
	local c = s:Connect(function()
		n += 1
	end)
	s:Fire()
	c:Disconnect()
	c:Disconnect()
	s:Fire()
	t.eq(n, 1)
	t.eq(c.Connected, false)
	t.eq(s:Count(), 0)
end)

t.test("disconnecting another handler during Fire is safe and takes effect immediately", function()
	local s = Signal.new()
	local log = {}
	local second
	s:Connect(function()
		table.insert(log, "first")
		second:Disconnect()
	end)
	second = s:Connect(function()
		table.insert(log, "second")
	end)
	s:Fire()
	t.eq(log, { "first" })
end)

t.test("Once fires a single time", function()
	local s = Signal.new()
	local n = 0
	s:Once(function()
		n += 1
	end)
	s:Fire()
	s:Fire()
	t.eq(n, 1)
	t.eq(s:Count(), 0)
end)

t.test("Wait returns the next fired values", function()
	local s = Signal.new()
	local got
	local thread = coroutine.create(function()
		got = { s:Wait() }
	end)
	coroutine.resume(thread)
	t.eq(got, nil)
	s:Fire(7, "ok")
	t.eq(got, { 7, "ok" })
end)

t.test("a throwing handler does not stop later handlers when the spawner isolates errors", function()
	local s = Signal.new(function(fn, ...)
		pcall(fn, ...)
	end)
	local n = 0
	s:Connect(function()
		error("boom")
	end)
	s:Connect(function()
		n += 1
	end)
	s:Fire()
	t.eq(n, 1)
end)

t.test("Destroy drops handlers and later Connect or Fire do nothing", function()
	local s = Signal.new()
	local n = 0
	local c = s:Connect(function()
		n += 1
	end)
	s:Destroy()
	t.eq(c.Connected, false)
	local late = s:Connect(function()
		n += 1
	end)
	s:Fire()
	t.eq(n, 0)
	t.eq(late.Connected, false)
	t.eq(s:Count(), 0)
end)

t.done()
