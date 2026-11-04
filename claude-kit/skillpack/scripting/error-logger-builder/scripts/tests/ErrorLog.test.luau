--!nocheck
local t = require("../../../../../systems/_check/harness")
local ErrorLog = require("../ErrorLog")

local function make(extra)
	local now = 0
	local printed = {}
	local opts = {
		clock = function()
			return now
		end,
		print = function(text)
			table.insert(printed, text)
		end,
	}
	for k, v in extra or {} do
		opts[k] = v
	end
	return ErrorLog.new(opts), function(n)
		now = n
	end, printed
end

t.test("Try returns the result on success and logs nothing", function()
	local log, _, printed = make()
	local ok, value = log:Try("Add", function(a, b)
		return a + b
	end, 2, 3)
	t.truthy(ok)
	t.eq(value, 5)
	t.eq(#printed, 0)
end)

t.test("Try catches an error, logs name and message, and keeps the trace", function()
	local log, _, printed = make()
	local ok = log:Try("Boom", function()
		error("bad thing", 0)
	end)
	t.falsy(ok)
	t.eq(#printed, 1)
	t.truthy(string.find(printed[1], "[Boom] bad thing", 1, true))
	local entry = log:Recent()[1]
	t.eq(entry.message, "bad thing")
	t.truthy(#entry.trace > 0)
end)

t.test("repeats inside the window are counted, not re-reported", function()
	local log, at, printed = make()
	for _ = 1, 5 do
		log:Report("Loop", "same")
	end
	t.eq(#printed, 1)
	t.eq(log:Stats().suppressed, 4)
	at(11)
	log:Report("Loop", "same")
	t.eq(#printed, 2)
	t.truthy(string.find(printed[2], "(+4 repeats)", 1, true))
end)

t.test("different messages are reported separately", function()
	local log, _, printed = make()
	log:Report("A", "one")
	log:Report("A", "two")
	log:Report("B", "one")
	t.eq(#printed, 3)
	t.eq(log:Stats().distinct, 3)
end)

t.test("the ring buffer keeps only the newest entries", function()
	local log = make({ capacity = 3 })
	for i = 1, 5 do
		log:Report("N", "m" .. i)
	end
	local recent = log:Recent()
	t.eq(#recent, 3)
	t.eq(recent[1].message, "m3")
end)

t.test("a throwing sink does not break reporting; a good sink receives the entry", function()
	local seen = {}
	local log = make({
		sink = function(entry)
			table.insert(seen, entry.message)
			error("sink down")
		end,
	})
	t.truthy(log:Report("S", "x"))
	t.eq(seen, { "x" })
end)

t.test("Wrap makes an event handler that swallows and logs errors", function()
	local log, _, printed = make()
	local handler = log:Wrap("Handler", function(a)
		if a == "bad" then
			error("nope", 0)
		end
	end)
	handler("ok")
	handler("bad")
	t.eq(#printed, 1)
end)

t.done()
