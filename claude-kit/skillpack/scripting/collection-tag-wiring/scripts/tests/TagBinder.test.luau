--!nocheck
local t = require("../../../../../systems/_check/harness")
local TagBinder = require("../TagBinder")

local function fakeService(initial)
	local tagged = initial or {}
	local added, removed = {}, {}
	local svc = {}
	local function signal(list)
		return {
			Connect = function(_, fn)
				table.insert(list, fn)
				return {
					Disconnect = function()
						table.remove(list, table.find(list, fn))
					end,
				}
			end,
		}
	end
	function svc.GetTagged(_, tag)
		return table.clone(tagged[tag] or {})
	end
	function svc.GetInstanceAddedSignal()
		return signal(added)
	end
	function svc.GetInstanceRemovedSignal()
		return signal(removed)
	end
	function svc.tag(tag, inst)
		tagged[tag] = tagged[tag] or {}
		table.insert(tagged[tag], inst)
		for _, fn in table.clone(added) do
			fn(inst)
		end
	end
	function svc.untag(tag, inst)
		table.remove(tagged[tag], table.find(tagged[tag], inst))
		for _, fn in table.clone(removed) do
			fn(inst)
		end
	end
	return svc
end

t.test("binds existing tagged instances and later ones", function()
	local svc = fakeService({ Coin = { "c1" } })
	local binder = TagBinder.new(svc)
	local seen = {}
	binder:Bind("Coin", function(inst)
		table.insert(seen, inst)
	end)
	svc.tag("Coin", "c2")
	t.eq(seen, { "c1", "c2" })
	t.eq(binder:Count("Coin"), 2)
end)

t.test("removing the tag runs the cleanup once", function()
	local svc = fakeService()
	local binder = TagBinder.new(svc)
	local cleaned = {}
	binder:Bind("Coin", function(inst)
		return function()
			table.insert(cleaned, inst)
		end
	end)
	svc.tag("Coin", "c1")
	svc.untag("Coin", "c1")
	svc.untag("Coin", "c1")
	t.eq(cleaned, { "c1" })
	t.eq(binder:Count("Coin"), 0)
end)

t.test("an object with Destroy works as a cleanup", function()
	local svc = fakeService()
	local binder = TagBinder.new(svc)
	local destroyed = 0
	binder:Bind("Door", function()
		return {
			Destroy = function()
				destroyed += 1
			end,
		}
	end)
	svc.tag("Door", "d1")
	binder:Destroy()
	t.eq(destroyed, 1)
end)

t.test("a throwing behaviour is reported and does not stop others", function()
	local svc = fakeService({ Coin = { "bad", "good" } })
	local errors = {}
	local binder = TagBinder.new(svc, function(tag, inst, err)
		table.insert(errors, tag .. ":" .. inst)
	end)
	local good = 0
	binder:Bind("Coin", function(inst)
		if inst == "bad" then
			error("boom")
		end
		good += 1
	end)
	t.eq(errors, { "Coin:bad" })
	t.eq(good, 1)
	t.eq(binder:Count("Coin"), 1)
end)

t.test("the same instance is never bound twice", function()
	local svc = fakeService({ Coin = { "c1" } })
	local binder = TagBinder.new(svc)
	local n = 0
	binder:Bind("Coin", function()
		n += 1
	end)
	svc.tag("Coin", "c1")
	t.eq(n, 1)
end)

t.test("Unbind stops listening and runs cleanups; double Bind is refused", function()
	local svc = fakeService({ Coin = { "c1" } })
	local binder = TagBinder.new(svc)
	local cleaned = 0
	binder:Bind("Coin", function()
		return function()
			cleaned += 1
		end
	end)
	t.falsy(pcall(binder.Bind, binder, "Coin", function() end))
	binder:Unbind("Coin")
	t.eq(cleaned, 1)
	svc.tag("Coin", "c2")
	t.eq(binder:Count("Coin"), 0)
end)

t.done()
