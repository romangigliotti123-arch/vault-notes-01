--!nocheck
--# selene: allow(incorrect_standard_library_use)
local fs = require("@lune/fs")
local process = require("@lune/process")
local SecretScan = require("./SecretScan")

local root = process.args[1]
if root == nil then
	print("usage: lune run scan_folder.luau <folder>")
	process.exit(2)
end

local EXT = {
	luau = true,
	lua = true,
	json = true,
	toml = true,
	yml = true,
	yaml = true,
	md = true,
	txt = true,
	env = true,
	ini = true,
	rbxlx = true,
	rbxmx = true,
}
local SKIP = { [".git"] = true, node_modules = true, Packages = true, DevPackages = true }

local all = {}
local files = 0
local function walk(dir: string)
	for _, name in fs.readDir(dir) do
		local path = dir .. "/" .. name
		if fs.isDir(path) then
			if not SKIP[name] then
				walk(path)
			end
		else
			local ext = string.match(name, "%.([%w]+)$")
			if (ext and EXT[string.lower(ext)]) or name == ".env" then
				files += 1
				local text = fs.readFile(path)
				for _, f in SecretScan.scanText(path, text) do
					table.insert(all, f)
				end
				for _, f in SecretScan.scanClientVisible(path, text) do
					table.insert(all, f)
				end
			end
		end
	end
end
walk(root)
print(`scanned {files} files`)
print(SecretScan.report(all))
for _, f in all do
	if f.severity == "CRITICAL" or f.severity == "HIGH" then
		process.exit(1)
	end
end
