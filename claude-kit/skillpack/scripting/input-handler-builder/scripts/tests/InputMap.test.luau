--!nocheck
-- Run: lune run InputMap.test.luau   (from the kit's systems folder, see check-scripts.sh)
local t = require("../../../../../systems/_check/harness")
local InputMap = require("../InputMap")

local function fakeCas()
	local cas = { bound = {}, titles = {} }
	function cas.BindAction(_, name, fn, touch, ...)
		cas.bound[name] = { fn = fn, touch = touch, inputs = { ... } }
	end
	function cas.BindActionAtPriority(_, name, fn, touch, priority, ...)
		cas.bound[name] = { fn = fn, touch = touch, priority = priority, inputs = { ... } }
	end
	function cas.UnbindAction(_, name)
		cas.bound[name] = nil
	end
	function cas.SetTitle(_, name, title)
		cas.titles[name] = title
	end
	return cas
end

local RESULTS = { sink = "sink", pass = "pass" }
local function press(cas, name, phase)
	return cas.bound[name].fn(name, { Name = phase }, {})
end

t.test("Bind registers the inputs and routes phases to the handler", function()
	local cas = fakeCas()
	local map = InputMap.new(cas, RESULTS)
	local phases = {}
	map:Bind("Dash", { inputs = { "LeftShift", "ButtonB" }, touchButton = true, title = "Dash" }, function(p)
		table.insert(phases, p)
	end)
	t.eq(cas.bound.Dash.inputs, { "LeftShift", "ButtonB" })
	t.truthy(cas.bound.Dash.touch)
	t.eq(cas.titles.Dash, "Dash")
	t.eq(press(cas, "Dash", "Begin"), "sink")
	press(cas, "Dash", "End")
	t.eq(phases, { "Begin", "End" })
end)

t.test("IsDown follows Begin and End and Cancel", function()
	local cas = fakeCas()
	local map = InputMap.new(cas, RESULTS)
	map:Bind("Aim", { inputs = { "MouseButton2" } }, function() end)
	press(cas, "Aim", "Begin")
	t.truthy(map:IsDown("Aim"))
	press(cas, "Aim", "Cancel")
	t.falsy(map:IsDown("Aim"))
end)

t.test("throttle drops a repeated Begin inside the window but still sinks it", function()
	local cas = fakeCas()
	local now = 0
	local map = InputMap.new(cas, RESULTS, function()
		return now
	end)
	local count = 0
	map:Bind("Fire", { inputs = { "E" }, throttle = 0.5 }, function(p)
		if p == "Begin" then
			count += 1
		end
	end)
	press(cas, "Fire", "Begin")
	now = 0.2
	t.eq(press(cas, "Fire", "Begin"), "sink")
	now = 0.6
	press(cas, "Fire", "Begin")
	t.eq(count, 2)
end)

t.test("priority bindings use BindActionAtPriority", function()
	local cas = fakeCas()
	local map = InputMap.new(cas, RESULTS)
	map:Bind("Menu", { inputs = { "Tab" }, priority = 3000 }, function() end)
	t.eq(cas.bound.Menu.priority, 3000)
end)

t.test("Rebind swaps the inputs; Unbind and UnbindAll release them", function()
	local cas = fakeCas()
	local map = InputMap.new(cas, RESULTS)
	map:Bind("A", { inputs = { "Z" } }, function() end)
	map:Bind("B", { inputs = { "X" } }, function() end)
	t.truthy(map:Rebind("A", { "Q" }))
	t.eq(cas.bound.A.inputs, { "Q" })
	t.falsy(map:Rebind("Nope", { "Q" }))
	map:Unbind("A")
	t.eq(cas.bound.A, nil)
	t.eq(map:Bound(), { "B" })
	map:UnbindAll()
	t.eq(cas.bound.B, nil)
	t.eq(map:Bound(), {})
end)

t.test("binding the same name twice replaces the old binding", function()
	local cas = fakeCas()
	local map = InputMap.new(cas, RESULTS)
	local first = 0
	map:Bind("A", { inputs = { "Z" } }, function()
		first += 1
	end)
	map:Bind("A", { inputs = { "Y" } }, function() end)
	press(cas, "A", "Begin")
	t.eq(first, 0)
	t.eq(cas.bound.A.inputs, { "Y" })
end)

t.done()
