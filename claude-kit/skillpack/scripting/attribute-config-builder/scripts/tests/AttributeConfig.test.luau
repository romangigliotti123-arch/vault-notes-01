--!nocheck
-- Run: lune run AttributeConfig.test.luau   (from the kit's systems folder, see check-scripts.sh)
local t = require("../../../../../systems/_check/harness")
local AttributeConfig = require("../AttributeConfig")

-- fake instance: SetAttribute fires the changed handlers, like the engine does
local function fakeInstance(initial)
	local attrs = initial or {}
	local handlers = {}
	local inst = {}
	function inst.GetAttribute(_, name)
		return attrs[name]
	end
	function inst.SetAttribute(_, name, value)
		attrs[name] = value
		for _, h in handlers[name] or {} do
			h()
		end
	end
	function inst.GetAttributeChangedSignal(_, name)
		return {
			Connect = function(_, fn)
				handlers[name] = handlers[name] or {}
				table.insert(handlers[name], fn)
				return {
					Disconnect = function()
						handlers[name] = {}
					end,
				}
			end,
		}
	end
	return inst, attrs
end

local schema = {
	Health = { kind = "number", default = 100, min = 1, max = 500 },
	Phase = { kind = "string", default = "one", allowed = { "one", "two" } },
	Enraged = { kind = "boolean", default = false },
}

t.test("bind writes defaults for missing attributes", function()
	local inst, attrs = fakeInstance()
	AttributeConfig.bind(inst, schema)
	t.eq(attrs.Health, 100)
	t.eq(attrs.Phase, "one")
	t.eq(attrs.Enraged, false)
end)

t.test("bind repairs an invalid starting value and keeps a valid one", function()
	local inst, attrs = fakeInstance({ Health = 9999, Phase = "three", Enraged = true })
	local cfg = AttributeConfig.bind(inst, schema)
	t.eq(attrs.Health, 500)
	t.eq(attrs.Phase, "one")
	t.eq(cfg:Get("Enraged"), true)
end)

t.test("a live edit inside the rules fires onChange with new and old", function()
	local inst = fakeInstance()
	local seen
	local cfg = AttributeConfig.bind(inst, schema, function(name, new, old)
		seen = { name, new, old }
	end)
	inst:SetAttribute("Health", 250)
	t.eq(seen, { "Health", 250, 100 })
	t.eq(cfg:Get("Health"), 250)
end)

t.test("an out-of-range edit is clamped and a wrong-type edit is reverted", function()
	local inst, attrs = fakeInstance()
	local cfg = AttributeConfig.bind(inst, schema)
	inst:SetAttribute("Health", 99999)
	t.eq(attrs.Health, 500)
	inst:SetAttribute("Health", "lots")
	t.eq(attrs.Health, 500)
	inst:SetAttribute("Phase", "nope")
	t.eq(attrs.Phase, "one")
	t.eq(cfg:Get("Phase"), "one")
end)

t.test("NaN and infinity are rejected", function()
	local inst, attrs = fakeInstance()
	AttributeConfig.bind(inst, schema)
	inst:SetAttribute("Health", 0 / 0)
	t.eq(attrs.Health, 100)
	inst:SetAttribute("Health", math.huge)
	t.eq(attrs.Health, 100)
end)

t.test("Set applies the same rules and reports acceptance", function()
	local inst, attrs = fakeInstance()
	local cfg = AttributeConfig.bind(inst, schema)
	t.truthy(cfg:Set("Health", 300))
	t.eq(attrs.Health, 300)
	t.falsy(cfg:Set("Health", "x"))
	t.falsy(cfg:Set("Unknown", 1))
	t.eq(cfg:Snapshot().Health, 300)
end)

t.test("Destroy stops listening", function()
	local inst = fakeInstance()
	local count = 0
	local cfg = AttributeConfig.bind(inst, schema, function()
		count += 1
	end)
	cfg:Destroy()
	inst:SetAttribute("Health", 200)
	t.eq(count, 0)
end)

t.test("a schema whose default breaks its own rules is refused", function()
	t.eq(#AttributeConfig.validateSchema({ A = { kind = "number", default = 50, min = 60 } }), 1)
	t.eq(#AttributeConfig.validateSchema({ A = { kind = "table", default = {} } }), 1)
	t.falsy(pcall(AttributeConfig.bind, fakeInstance(), { A = { kind = "number", default = 0, min = 5, max = 1 } }))
end)

t.done()
