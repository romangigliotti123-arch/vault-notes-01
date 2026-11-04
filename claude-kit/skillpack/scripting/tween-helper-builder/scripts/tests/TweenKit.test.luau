--!nocheck
local t = require("../../../../../systems/_check/harness")
local TweenKit = require("../TweenKit")

local function fakeService()
	local created = {}
	local service = {}
	function service.Create(_, instance, _info, goal)
		local tween = { played = false, cancelled = false, handlers = {} }
		tween.Completed = {
			Connect = function(_, fn)
				table.insert(tween.handlers, fn)
				return {
					Disconnect = function()
						tween.handlers = {}
					end,
				}
			end,
		}
		function tween.Play()
			tween.played = true
		end
		function tween.Cancel()
			tween.cancelled = true
		end
		function tween.complete()
			for _, h in tween.handlers do
				h("Completed")
			end
		end
		tween.instance, tween.goal = instance, goal
		table.insert(created, tween)
		return tween
	end
	return service, created
end

t.test("Play starts the tween and reports completion", function()
	local service, created = fakeService()
	local kit = TweenKit.new(service)
	local result
	kit:Play("door", {}, { Position = 1 }, function(c)
		result = c
	end)
	t.truthy(created[1].played)
	t.eq(kit:ActiveCount(), 1)
	created[1].complete()
	t.eq(result, true)
	t.eq(kit:ActiveCount(), 0)
end)

t.test("a new tween on the same property cancels the old one", function()
	local service, created = fakeService()
	local kit = TweenKit.new(service)
	local first
	kit:Play("door", {}, { Position = 1 }, function(c)
		first = c
	end)
	kit:Play("door", {}, { Position = 2 })
	t.truthy(created[1].cancelled)
	t.eq(first, false)
	t.eq(kit:ActiveCount(), 1)
end)

t.test("tweens on different properties of one instance both run", function()
	local service, created = fakeService()
	local kit = TweenKit.new(service)
	kit:Play("door", {}, { Position = 1 })
	kit:Play("door", {}, { Transparency = 1 })
	t.falsy(created[1].cancelled)
	t.eq(kit:ActiveCount(), 2)
end)

t.test("Chain runs steps in order and reports completion once", function()
	local service, created = fakeService()
	local kit = TweenKit.new(service)
	local done = {}
	kit:Chain({ { "a", {}, { X = 1 } }, { "b", {}, { Y = 1 } } }, function(c)
		table.insert(done, c)
	end)
	t.eq(#created, 1)
	created[1].complete()
	t.eq(#created, 2)
	t.eq(done, {})
	created[2].complete()
	t.eq(done, { true })
end)

t.test("cancelling a chain stops the running step and skips the rest", function()
	local service, created = fakeService()
	local kit = TweenKit.new(service)
	local done = {}
	local handle = kit:Chain({ { "a", {}, { X = 1 } }, { "b", {}, { Y = 1 } } }, function(c)
		table.insert(done, c)
	end)
	handle:Cancel()
	t.truthy(created[1].cancelled)
	t.eq(#created, 1)
	t.eq(done, { false })
	t.eq(kit:ActiveCount(), 0)
end)

t.test("Cancel(instance) and Destroy clear everything", function()
	local service = fakeService()
	local kit = TweenKit.new(service)
	kit:Play("a", {}, { X = 1 })
	kit:Play("b", {}, { X = 1 })
	kit:Cancel("a")
	t.eq(kit:ActiveCount(), 1)
	kit:Destroy()
	t.eq(kit:ActiveCount(), 0)
end)

t.done()
