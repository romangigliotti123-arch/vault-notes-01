--!nocheck
-- Run: lune run TypeScan.test.luau   (from the kit's systems folder, see check-scripts.sh)
local t = require("../../../../../systems/_check/harness")
local TypeScan = require("../TypeScan")

t.test("reads the type mode from the leading directive", function()
	t.eq(TypeScan.mode("--!strict\nlocal x = 1"), "strict")
	t.eq(TypeScan.mode("-- note\n--!nonstrict\nx = 1"), "nonstrict")
	t.eq(TypeScan.mode("local x = 1\n--!strict"), "none")
	t.eq(TypeScan.mode("--!nocheck\n"), "nocheck")
end)

t.test("flags untyped parameters and missing returns", function()
	local src = [==[
function M.add(a, b)
	return a + b
end
local function ok(a: number, b: number): number
	return a + b
end
function M:method(x)
end
]==]
	local r = TypeScan.scan(src)
	t.eq(r.totalFunctions, 3)
	t.eq(#r.functions, 2)
	t.eq(r.functions[1].name, "M.add")
	t.eq(r.functions[1].untyped, { "a", "b" })
	t.truthy(r.functions[1].missingReturn)
	t.eq(r.functions[2].untyped, { "x" })
end)

t.test("commas inside table and function types do not split parameters", function()
	local r = TypeScan.scan("local function f(map: { [string]: number }, cb: (a: number, b: number) -> ()): ()\nend")
	t.eq(#r.functions, 0)
end)

t.test("self and varargs are not reported", function()
	local r = TypeScan.scan("function M.run(self: M, ...): ()\nend")
	t.eq(#r.functions, 0)
end)

t.test("counts explicit any outside comments", function()
	local r = TypeScan.scan("local a: any = 1\nlocal b = x :: any\n-- local c: any\n")
	t.eq(r.anyCount, 2)
end)

t.test("anonymous callbacks and assigned functions are found", function()
	local r = TypeScan.scan("M.cb = function(a)\nend\nsignal:Connect(function(player)\nend)")
	t.eq(r.totalFunctions, 2)
	t.eq(r.functions[2].name, "<anonymous>")
end)

t.test("score is zero for a fully typed module", function()
	t.eq(TypeScan.score(TypeScan.scan("local function f(a: number): number\n\treturn a\nend")), 0)
	t.truthy(TypeScan.score(TypeScan.scan("local function f(a)\nend")) > 0)
end)

t.done()
