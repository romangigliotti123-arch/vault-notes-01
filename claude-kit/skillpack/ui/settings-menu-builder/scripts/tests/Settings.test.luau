--!nocheck
-- Run: lune run Settings.test.luau   (from the kit's systems folder, see check-scripts.sh)
local t = require("../../../../../systems/_check/harness")
local S = require("../Settings")

local schema = {
	{ key = "music", kind = "slider", default = 0.5, min = 0, max = 1, step = 0.1 },
	{ key = "shake", kind = "toggle", default = true },
	{ key = "quality", kind = "choice", default = "auto", options = { "auto", "low", "high" } },
}

t.test("defaults come from the schema", function()
	t.eq(S.defaults(schema), { music = 0.5, shake = true, quality = "auto" })
end)
t.test("sanitize clamps, snaps, coerces and drops unknown keys", function()
	local out = S.sanitize(schema, { music = 7, shake = "yes", quality = "ultra", cheat = 1 })
	t.eq(out, { music = 1, shake = true, quality = "auto" })
	t.eq(S.sanitize(schema, { music = 0.34 }).music, 0.3)
end)
t.test("NaN, infinity and non-table input fall back to defaults", function()
	t.eq(S.sanitize(schema, { music = 0 / 0 }).music, 0.5)
	t.eq(S.sanitize(schema, { music = math.huge }).music, 0.5)
	t.eq(S.sanitize(schema, "junk"), S.defaults(schema))
	t.eq(S.sanitize(schema, nil), S.defaults(schema))
end)
t.test("valid values pass through", function()
	local out = S.sanitize(schema, { music = 0.8, shake = false, quality = "high" })
	t.eq(out, { music = 0.8, shake = false, quality = "high" })
end)
t.test("diff returns only changes", function()
	t.eq(S.diff({ a = 1, b = 2 }, { a = 1, b = 3 }), { b = 3 })
end)
t.test("migrate runs each step in order", function()
	local saved, v = S.migrate({ old = true }, 1, {
		[1] = function(s)
			s.quality = "auto"
		end,
		[2] = function(s)
			s.shake = true
		end,
	})
	t.eq(v, 3)
	t.eq(saved, { old = true, quality = "auto", shake = true })
end)
t.done()
