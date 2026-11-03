--!strict
-- ClientLoader: wait for the instances and modules a client script depends on, with a timeout and a message that names the
-- missing path. A replicated script can start before its modules replicate (vault: scripting-and-performance), and a bare
-- WaitForChild with no timeout hangs forever with only an "Infinite yield possible" warning.
--   local Loader = require(ReplicatedFirst.ClientLoader)
--   local loaded = Loader.load(ReplicatedStorage, { Shared = { "Config", "Types" }, Client = { "UI" } }, 10, require)
--   loaded.Config.Value ...     loaded is { [moduleName] = requiredValue }
--   Loader.waitPath(ReplicatedStorage, { "Assets", "Sounds", "Click" }, 5)   -- Instance or nil, plus an error text
-- Never yield inside a module's top level (a yield stalls every module waiting on it): load first, then start. Do the waiting
-- here, in one bootstrap script, then call each module's Init/Start from the result.
local ClientLoader = {}

export type NodeLike = { WaitForChild: (self: any, name: string, timeout: number?) -> any }

-- follow a path of child names; (node, nil) or (nil, "ReplicatedStorage.Assets.Sounds missing child 'Click' after 5s")
function ClientLoader.waitPath(root: NodeLike, path: { string }, timeout: number): (any, string?)
	local node: any = root
	local walked = tostring((root :: any).Name or "root")
	for _, name in path do
		local child = node:WaitForChild(name, timeout)
		if child == nil then
			return nil, `{walked} missing child '{name}' after {timeout}s`
		end
		node = child
		walked ..= "." .. name
	end
	return node, nil
end

-- require every listed module (folders: { FolderName = { "ModuleA", "ModuleB" } }) in a stable order.
-- Returns (modules, nil) or (nil, "all the problems at once") so one run shows every missing piece, not just the first.
function ClientLoader.load(
	root: NodeLike,
	folders: { [string]: { string } },
	timeout: number,
	requireFn: (module: any) -> any
): ({ [string]: any }?, string?)
	local folderNames = {}
	for name in folders do
		table.insert(folderNames, name)
	end
	table.sort(folderNames)

	local modules: { [string]: any } = {}
	local problems: { string } = {}
	for _, folderName in folderNames do
		local folder, err = ClientLoader.waitPath(root, { folderName }, timeout)
		if folder == nil then
			table.insert(problems, err or `{folderName} missing`)
		else
			for _, moduleName in folders[folderName] do
				local module, moduleErr = ClientLoader.waitPath(folder, { moduleName }, timeout)
				if module == nil then
					table.insert(problems, moduleErr or `{folderName}.{moduleName} missing`)
				elseif modules[moduleName] ~= nil then
					table.insert(problems, `module name '{moduleName}' exists in two folders`)
				else
					local ok, value = pcall(requireFn, module)
					if ok then
						modules[moduleName] = value
					else
						table.insert(problems, `{folderName}.{moduleName} failed to load: {tostring(value)}`)
					end
				end
			end
		end
	end
	if #problems > 0 then
		return nil, table.concat(problems, "\n")
	end
	return modules, nil
end

return ClientLoader
