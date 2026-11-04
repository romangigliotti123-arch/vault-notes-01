--!nocheck
local t = require("../../../../../systems/_check/harness")
local ClientLoader = require("../ClientLoader")

local function node(name, children)
	local n = { Name = name, children = children or {} }
	function n.WaitForChild(self, childName)
		return self.children[childName]
	end
	return n
end

local function tree()
	return node("ReplicatedStorage", {
		Shared = node("Shared", { Config = node("Config"), Types = node("Types") }),
		Client = node("Client", { UI = node("UI") }),
	})
end

local function fakeRequire(n)
	if n.Name == "Types" then
		error("Types.luau:3 syntax error")
	end
	return { loaded = n.Name }
end

t.test("waitPath returns the node at the end of the path", function()
	local found, err = ClientLoader.waitPath(tree(), { "Shared", "Config" }, 5)
	t.eq(found.Name, "Config")
	t.eq(err, nil)
end)

t.test("waitPath names the missing child and the path walked so far", function()
	local found, err = ClientLoader.waitPath(tree(), { "Shared", "Nope" }, 5)
	t.eq(found, nil)
	t.eq(err, "ReplicatedStorage.Shared missing child 'Nope' after 5s")
end)

t.test("load requires every listed module and returns them by name", function()
	local modules, err = ClientLoader.load(tree(), { Shared = { "Config" }, Client = { "UI" } }, 5, function(n)
		return { loaded = n.Name }
	end)
	t.eq(err, nil)
	t.eq(modules.Config.loaded, "Config")
	t.eq(modules.UI.loaded, "UI")
end)

t.test("load reports every problem at once: missing folder, missing module, module that errors", function()
	local modules, err =
		ClientLoader.load(tree(), { Shared = { "Config", "Types", "Ghost" }, Missing = { "X" } }, 5, fakeRequire)
	t.eq(modules, nil)
	t.truthy(string.find(err, "missing child 'Missing'", 1, true))
	t.truthy(string.find(err, "missing child 'Ghost'", 1, true))
	t.truthy(string.find(err, "Shared.Types failed to load", 1, true))
end)

t.test("duplicate module names across folders are flagged", function()
	local root = node("RS", { A = node("A", { Same = node("Same") }), B = node("B", { Same = node("Same") }) })
	local modules, err = ClientLoader.load(root, { A = { "Same" }, B = { "Same" } }, 1, function()
		return {}
	end)
	t.eq(modules, nil)
	t.truthy(string.find(err, "exists in two folders", 1, true))
end)

t.done()
