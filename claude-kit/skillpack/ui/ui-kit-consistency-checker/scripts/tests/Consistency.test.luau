--!nocheck
local t = require("../../../../../systems/_check/harness")
local C = require("../Consistency")

local function recs(field, values)
	local out = {}
	for i, v in values do
		table.insert(out, { path = "G.n" .. i, [field] = v })
	end
	return out
end

t.test("dominant value and a rare outlier with its path", function()
	local values = {}
	for _ = 1, 9 do
		table.insert(values, 8)
	end
	table.insert(values, 6)
	local r = C.analyse(recs("cornerRadius", values), { "cornerRadius" }).cornerRadius
	t.eq(r.dominant, 8)
	t.eq(r.dominantShare, 0.9)
	t.eq(r.distinct, 2)
	t.eq(#r.outliers, 1)
	t.eq(r.outliers[1].value, 6)
	t.eq(r.outliers[1].paths, { "G.n10" })
end)
t.test("no clear dominant value means no outliers are named", function()
	local r = C.analyse(recs("textSize", { 12, 14, 16, 18, 20 }), { "textSize" }).textSize
	t.eq(r.outliers, {})
	t.eq(r.distinct, 5)
end)
t.test("records missing a field are ignored for that field", function()
	local r = C.analyse({ { path = "a", font = "Gotham" }, { path = "b" } }, { "font" }).font
	t.eq(r.dominant, "Gotham")
	t.eq(r.dominantShare, 1)
end)
t.test("empty input is safe", function()
	local r = C.analyse({}, { "font" }).font
	t.eq(r.dominant, nil)
	t.eq(r.distinct, 0)
end)
t.test("a mid-sized minority (over the share cap) is not an outlier", function()
	local values = {}
	for _ = 1, 6 do
		table.insert(values, 8)
	end
	for _ = 1, 4 do
		table.insert(values, 12)
	end
	t.eq(C.analyse(recs("cornerRadius", values), { "cornerRadius" }).cornerRadius.outliers, {})
end)
t.done()
