--!nocheck
local t = require("../../../../../systems/_check/harness")
local C = require("../CrashSignals")

print("CrashSignals")

t.test("classify maps message text to categories", function()
	t.eq(C.classify("DataStore request was added to queue. Request: SetAsync"), "datastore-throttle")
	t.eq(C.classify("Script timeout: exhausted allowed execution time"), "script-timeout")
	t.eq(C.classify("Infinite yield possible on 'Workspace.Map:WaitForChild(\"Spawn\")'"), "infinite-yield")
	t.eq(C.classify("Shop:31: attempt to index nil with 'coins'"), "script-error")
	t.eq(C.classify("You were kicked from this experience"), "kicked")
	t.eq(C.classify("Disconnected: connection lost"), "disconnect")
	t.eq(C.classify("hello world"), nil)
	t.eq(C.classify("DataStore saved fine"), nil)
	t.eq(C.classify("DataStore error: 502"), "datastore-error")
end)

t.test("a memory warning before the disconnect is the suspect", function()
	local s = C.summarize({
		"Loading",
		"low memory warning on client",
		"Shop:3: attempt to index nil with 'x'",
		"Disconnected: connection lost",
	})
	t.eq(s.suspect, "memory")
	t.eq(s.counts["script-error"], 1)
	t.eq(s.first.disconnect, 4)
end)

t.test("signals after the disconnect do not count as the cause", function()
	local s = C.summarize({ "Disconnected: connection lost", "Shop:3: attempt to index nil with 'x'" })
	t.eq(s.suspect, "disconnect")
end)

t.test("an empty or clean log reports no suspect and says the log may be incomplete", function()
	local s = C.summarize({ "all fine", "still fine" })
	t.eq(s.suspect, "none")
	t.truthy(string.find(s.why, "incomplete", 1, true))
end)

t.test("memory trend finds a steady climb and ignores a flat or noisy series", function()
	local climb, flat, noisy = {}, {}, {}
	for i = 0, 10 do
		table.insert(climb, { t = i * 60, mb = 400 + i * 12 })
		table.insert(flat, { t = i * 60, mb = 500 })
		table.insert(noisy, { t = i * 60, mb = 500 + (if i % 2 == 0 then 30 else -30) })
	end
	local c = C.memoryTrend(climb)
	t.truthy(c.leak)
	t.truthy(math.abs(c.slope - 12) < 0.01)
	t.falsy(C.memoryTrend(flat).leak)
	t.falsy(C.memoryTrend(noisy).leak)
	t.falsy(C.memoryTrend({ { t = 0, mb = 1 } }).leak)
end)

t.test("report names the suspect and the timeline", function()
	local r = C.report(C.summarize({ "low memory warning", "Disconnected" }))
	t.truthy(string.find(r, "suspect memory", 1, true))
	t.truthy(string.find(r, "line 1 [memory]", 1, true))
end)

t.done()
