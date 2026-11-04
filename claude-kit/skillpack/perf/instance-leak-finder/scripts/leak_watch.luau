--!strict
local INTERVAL = 30
local SAMPLES = 10
local TOP = 8

local function snapshot(): ({ [string]: number }, number)
	local classes: { [string]: number } = {}
	local total = 0
	for _, inst in game:GetDescendants() do
		total += 1
		classes[inst.ClassName] = (classes[inst.ClassName] or 0) + 1
	end
	return classes, total
end

local first, firstTotal = snapshot()
local series: { number } = { firstTotal }
local last = first
for _ = 2, SAMPLES do
	task.wait(INTERVAL)
	local c, total = snapshot()
	table.insert(series, total)
	last = c
end

local growth: { { class: string, delta: number } } = {}
for class, n in last do
	local d = n - (first[class] or 0)
	if d > 0 then
		table.insert(growth, { class = class, delta = d })
	end
end
table.sort(growth, function(a, b)
	if a.delta ~= b.delta then
		return a.delta > b.delta
	end
	return a.class < b.class
end)

local lines = {
	("instances every %ds: { %s }"):format(INTERVAL, table.concat(series, ", ")),
	("first %d -> last %d (%+d)"):format(series[1], series[#series], series[#series] - series[1]),
	"Classes that grew most:",
}
for i = 1, math.min(TOP, #growth) do
	table.insert(lines, ("  +%d  %s"):format(growth[i].delta, growth[i].class))
end
return table.concat(lines, "\n")
