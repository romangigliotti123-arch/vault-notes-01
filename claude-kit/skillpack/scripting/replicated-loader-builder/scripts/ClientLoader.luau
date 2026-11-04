--!strict
local ClientLoader = {}

export type NodeLike = { WaitForChild: (self: any, name: string, timeout: number?) -> any }

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
