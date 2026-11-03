--!strict
-- stream_audit.luau: READ-ONLY audit of a place's instance-streaming setup. Studio command bar or MCP `execute_luau` (Edit datamodel).
-- Reports: StreamingEnabled and radii (docs defaults: StreamingMinRadius 64, StreamingTargetRadius 1024), models whose size or mode needs a decision
-- (Persistent / Atomic / default), and scripts that look like they assume everything is loaded (direct workspace.Name.Child chains without WaitForChild).
-- It changes nothing: StreamingEnabled and the radii are place settings the owner sets in Studio's Properties window (Workspace).
local LARGE_MODEL_STUDS = 64 -- Creator Docs streaming/techniques: keep a model's extent to about 64 cubic studs so it streams in whole; larger models stream in pieces
local TOP = 10

local Workspace = game:GetService("Workspace")

local out: { string } = {}
local function add(line: string)
	table.insert(out, line)
end

add(
	("StreamingEnabled=%s  MinRadius=%d (docs default 64)  TargetRadius=%d (docs default 1024)"):format(
		tostring(Workspace.StreamingEnabled),
		(Workspace :: any).StreamingMinRadius,
		(Workspace :: any).StreamingTargetRadius
	)
)
add("StreamingIntegrityMode=" .. tostring((Workspace :: any).StreamingIntegrityMode))

local persistent, atomic, defaultMode = 0, 0, 0
local large: { { name: string, size: number } } = {}
for _, inst in Workspace:GetDescendants() do
	if inst:IsA("Model") then
		local model = inst :: Model
		if model.ModelStreamingMode == Enum.ModelStreamingMode.Persistent then
			persistent += 1
		elseif model.ModelStreamingMode == Enum.ModelStreamingMode.Atomic then
			atomic += 1
		else
			defaultMode += 1
		end
		local ok, size = pcall(function()
			return model:GetExtentsSize()
		end)
		if ok then
			local longest = math.max(size.X, size.Y, size.Z)
			if longest > LARGE_MODEL_STUDS and model.ModelStreamingMode == Enum.ModelStreamingMode.Default then
				table.insert(large, { name = model:GetFullName(), size = longest })
			end
		end
	end
end
table.sort(large, function(a, b)
	return a.size > b.size
end)
add(("Models: Persistent=%d Atomic=%d Default=%d"):format(persistent, atomic, defaultMode))
add(
	("Default-mode models longer than %d studs (candidates for Atomic if scripts need all children together): %d"):format(
		LARGE_MODEL_STUDS,
		#large
	)
)
for i = 1, math.min(TOP, #large) do
	add(("  %5.0f studs  %s"):format(large[i].size, large[i].name))
end

-- scripts that read the world as if it were all present
local risky = 0
local riskyList: { string } = {}
for _, inst in game:GetDescendants() do
	if inst:IsA("LuaSourceContainer") then
		local ok, src = pcall(function()
			return (inst :: any).Source :: string
		end)
		if ok and src then
			local hit = string.find(src, "workspace%.[%w_]+%.[%w_]+")
				or string.find(src, "workspace:FindFirstChild%b()%.")
			if hit then
				risky += 1
				if #riskyList < TOP then
					table.insert(riskyList, inst:GetFullName())
				end
			end
		end
	end
end
add(
	("Scripts with workspace.A.B chains (may break when parts stream out; use WaitForChild/Persistent): %d"):format(
		risky
	)
)
for _, name in riskyList do
	add("  " .. name)
end
add(
	"Next: test with StreamingTargetRadius 64 while traversing, teleporting and revisiting areas (docs testing advice); judge by client memory and join time."
)

return table.concat(out, "\n")
