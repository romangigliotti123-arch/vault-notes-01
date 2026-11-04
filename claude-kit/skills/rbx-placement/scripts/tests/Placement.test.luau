--!nocheck
local fs = require("@lune/fs")
local process = require("@lune/process")
local serde = require("@lune/serde")
local t = require("../../../../systems/_check/harness")
local Core = require("../PlacementCore")

local fixturePath = "../skills/rbx-placement/scripts/tests/fixtures.json"
local dumpPath = nil
local args = process.args
local i = 1
while i <= #args do
	if args[i] == "--dump" then
		dumpPath = args[i + 1]
		i += 1
	else
		fixturePath = args[i]
	end
	i += 1
end

local fx = serde.decode("json", fs.readFile(fixturePath))
local dump = {}

local function getNum(rep, key)
	local parts = string.split(key, ".")
	local v = rep.checks[parts[1]].measured
	for k = 2, #parts do
		local p = parts[k]
		if type(v) == "table" and v[1] ~= nil then
			v = v[tonumber(p) + 1]
		else
			v = v[p]
		end
	end
	return v
end

for _, c in fx.cases do
	t.test(c.name, function()
		local rep = Core.verify(c.snap, c.intent, c.env, c.opts)
		dump[c.name] = rep
		for k, v in c.expect do
			t.eq(rep.checks[k].status, v, k .. " status (" .. table.concat(rep.checks[k].issues, "; ") .. ")")
		end
		if c.status ~= nil then
			t.eq(rep.status, c.status, "overall status")
		end
		for k, v in c.num do
			t.eq(getNum(rep, k), v, k)
		end
		for k, a in c.fix do
			local found = false
			for _, f in rep.checks[k].fixes do
				if f.action == a then
					found = true
				end
			end
			t.truthy(found, "fix " .. k .. " should include " .. a)
		end
	end)
end

t.test("every check id has a name and the report lists the failed ones", function()
	for _, id in Core.ORDER do
		t.truthy(Core.NAMES[id], id)
	end
	local rep = Core.verify(fx.cases[1].snap, { kind = "door", face = { target = { 10, 3.5, 20 } } }, fx.cases[1].env)
	t.eq(rep.status, "fail")
	t.eq(rep.failed[1], "P4")
end)

if dumpPath then
	fs.writeFile(dumpPath, serde.encode("json", dump))
end
t.done()
