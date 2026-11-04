--!nocheck
local t = require("../../../../../systems/_check/harness")
local RemoteGuard = require("../RemoteGuard")

t.test("number rejects NaN, inf, strings and out of range", function()
	local v = RemoteGuard.number(0, 10)
	t.truthy(v(5))
	t.falsy(v(11))
	t.falsy(v(0 / 0))
	t.falsy(v(math.huge))
	t.falsy(v("5"))
end)

t.test("integer rejects fractions", function()
	local v = RemoteGuard.integer(1, 5)
	t.truthy(v(3))
	t.falsy(v(2.5))
	t.falsy(v(0))
end)

t.test("string length and pattern", function()
	local v = RemoteGuard.string(5, "^%a+$")
	t.truthy(v("abc"))
	t.falsy(v("abcdef"))
	t.falsy(v("ab1"))
	t.falsy(v(12))
end)

t.test("oneOf allows only listed literals", function()
	local v = RemoteGuard.oneOf({ "buy", "sell" })
	t.truthy(v("buy"))
	t.falsy(v("steal"))
	t.falsy(v(nil))
end)

t.test("optional accepts nil", function()
	local v = RemoteGuard.optional(RemoteGuard.boolean())
	t.truthy(v(nil))
	t.truthy(v(true))
	t.falsy(v("x"))
end)

t.test("limiter blocks the call over the limit and resets after the window", function()
	local now = 0
	local l = RemoteGuard.newLimiter(2, 1, function()
		return now
	end)
	t.truthy(l:allow(7))
	t.truthy(l:allow(7))
	t.falsy(l:allow(7))
	t.truthy(l:allow(8))
	now = 1.5
	t.truthy(l:allow(7))
end)

t.test("check rejects too many and invalid arguments", function()
	local vs = { RemoteGuard.integer(1, 9) }
	local ok = RemoteGuard.check(vs, 3)
	t.truthy(ok)
	local ok2, why2 = RemoteGuard.check(vs, 3, 4)
	t.falsy(ok2)
	t.eq(why2, "too many arguments")
	local ok3, why3 = RemoteGuard.check(vs, 99)
	t.falsy(ok3)
	t.eq(why3, "argument 1 invalid")
end)

t.test("bind runs handler only for valid, allowed calls", function()
	local handler = nil
	local fake = {
		OnServerEvent = {
			Connect = function(_self, fn)
				handler = fn
				return { Connected = true }
			end,
		},
		IsA = function(_self, c)
			return c == "RemoteEvent"
		end,
	}
	local got, rejected = {}, {}
	RemoteGuard.bind(fake, {
		args = { RemoteGuard.integer(1, 9) },
		limit = { calls = 2, per = 100 },
		handler = function(_p, n)
			table.insert(got, n)
		end,
		onReject = function(_p, why)
			table.insert(rejected, why)
		end,
	})
	local player = { UserId = 1 }
	handler(player, 4)
	handler(player, 99)
	handler(player, 5)
	t.eq(got, { 4 })
	t.eq(rejected, { "argument 1 invalid", "rate limit" })
end)

t.done()
