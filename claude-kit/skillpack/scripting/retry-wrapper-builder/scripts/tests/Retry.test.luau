--!nocheck
-- Run: lune run Retry.test.luau   (from the kit's systems folder, see check-scripts.sh)
local t = require("../../../../../systems/_check/harness")
local Retry = require("../Retry")

local function opts(extra)
	local waits = {}
	local o = {
		wait = function(s)
			table.insert(waits, s)
		end,
		random = function()
			return 0.5
		end,
		jitter = 0,
	}
	for k, v in extra or {} do
		o[k] = v
	end
	return o, waits
end

t.test("succeeds first time without waiting", function()
	local o, waits = opts()
	local ok, value, tries = Retry.run(function()
		return "data"
	end, o)
	t.truthy(ok)
	t.eq(value, "data")
	t.eq(tries, 1)
	t.eq(#waits, 0)
end)

t.test("retries transient failures with exponential delays, then succeeds", function()
	local o, waits = opts({ base = 1, factor = 2, attempts = 5 })
	local calls = 0
	local ok, value, tries = Retry.run(function()
		calls += 1
		if calls < 4 then
			error("HTTP 503 unavailable", 0)
		end
		return "fine"
	end, o)
	t.truthy(ok)
	t.eq(value, "fine")
	t.eq(tries, 4)
	t.eq(waits, { 1, 2, 4 })
end)

t.test("gives up after the attempt limit and returns the last error", function()
	local o = opts({ attempts = 3 })
	local calls = 0
	local ok, err, tries = Retry.run(function()
		calls += 1
		error("timed out", 0)
	end, o)
	t.falsy(ok)
	t.eq(err, "timed out")
	t.eq(tries, 3)
	t.eq(calls, 3)
end)

t.test("a permanent error is not retried", function()
	local o, waits = opts()
	local calls = 0
	local ok, _, tries = Retry.run(function()
		calls += 1
		error("403 Forbidden", 0)
	end, o)
	t.falsy(ok)
	t.eq(tries, 1)
	t.eq(#waits, 0)
end)

t.test("delay is capped and jitter stays within its band", function()
	t.eq(
		Retry.delayFor(10, {
			base = 1,
			max = 8,
			jitter = 0,
			random = function()
				return 0.5
			end,
		}),
		8
	)
	local low = Retry.delayFor(1, {
		base = 1,
		jitter = 0.5,
		random = function()
			return 0
		end,
	})
	local high = Retry.delayFor(1, {
		base = 1,
		jitter = 0.5,
		random = function()
			return 1
		end,
	})
	t.eq(low, 0.5)
	t.eq(high, 1.5)
end)

t.test("the waiting budget stops retries early", function()
	local o, waits = opts({ base = 4, factor = 1, attempts = 10, budget = 9 })
	local ok, _, tries = Retry.run(function()
		error("throttled", 0)
	end, o)
	t.falsy(ok)
	t.eq(#waits, 2)
	t.eq(tries, 3)
end)

t.test("a custom retryable test overrides the classifier", function()
	local o = opts({
		retryable = function(err)
			return err == "again"
		end,
		attempts = 3,
	})
	local calls = 0
	Retry.run(function()
		calls += 1
		error(calls == 1 and "again" or "stop", 0)
	end, o)
	t.eq(calls, 2)
end)

t.test("classify", function()
	t.eq(Retry.classify("429 Too Many Requests"), "transient")
	t.eq(Retry.classify("InvalidArgument"), "permanent")
	t.eq(Retry.classify("something odd"), "unknown")
	t.eq(Retry.classify("DatastoreThrottled"), "transient")
	t.eq(Retry.DATASTORE.attempts, 5)
end)

t.done()
