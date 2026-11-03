--!strict
-- texture_inventory.luau: read-only list of every texture-like asset id in the place with its kind and use count, as lines of
--   id<TAB>kind<TAB>uses<TAB>example path
-- Studio cannot read an image's width/height from its id, so add the sizes yourself (Asset Manager, the source file, or the
-- Developer Console texture memory view) and feed {id, width, height, uses} into scripts/TextureBudget.luau for the memory estimate.
-- Paste into the Studio command bar or send through the Studio MCP `execute_luau` tool (datamodel_type Edit).
local ROOT: Instance? = nil -- nil = Workspace, ReplicatedStorage, StarterGui, Lighting
local MAX_LINES = 80

local PROPS: { [string]: { { prop: string, kind: string } } } = {
	MeshPart = { { prop = "TextureID", kind = "meshTexture" } },
	SurfaceAppearance = {
		{ prop = "ColorMap", kind = "color" },
		{ prop = "NormalMap", kind = "normal" },
		{ prop = "MetalnessMap", kind = "metalness" },
		{ prop = "RoughnessMap", kind = "roughness" },
	},
	Decal = { { prop = "Texture", kind = "decal" } },
	Texture = { { prop = "Texture", kind = "texture" } },
	ImageLabel = { { prop = "Image", kind = "ui" } },
	ImageButton = { { prop = "Image", kind = "ui" } },
	ParticleEmitter = { { prop = "Texture", kind = "particle" } },
	Sky = {
		{ prop = "SkyboxBk", kind = "sky" },
		{ prop = "SkyboxDn", kind = "sky" },
		{ prop = "SkyboxFt", kind = "sky" },
		{ prop = "SkyboxLf", kind = "sky" },
		{ prop = "SkyboxRt", kind = "sky" },
		{ prop = "SkyboxUp", kind = "sky" },
	},
}

type Entry = { id: string, kind: string, uses: number, example: string }

local function run(): string
	local roots: { Instance } = if ROOT
		then { ROOT }
		else {
			workspace,
			game:GetService("ReplicatedStorage"),
			game:GetService("StarterGui"),
			game:GetService("Lighting"),
		}
	local byKey: { [string]: Entry } = {}
	local surfaceApps, withMetalness = 0, 0
	for _, root in roots do
		for _, inst in root:GetDescendants() do
			local specs = PROPS[inst.ClassName]
			if specs then
				if inst:IsA("SurfaceAppearance") then
					surfaceApps += 1
				end
				for _, spec in specs do
					local ok, value = pcall(function()
						return (inst :: any)[spec.prop]
					end)
					local id = if ok then tostring(value) else ""
					if id ~= "" and id ~= "nil" then
						if spec.kind == "metalness" then
							withMetalness += 1
						end
						local key = id .. "|" .. spec.kind
						local e = byKey[key]
						if e then
							e.uses += 1
						else
							byKey[key] = { id = id, kind = spec.kind, uses = 1, example = inst:GetFullName() }
						end
					end
				end
			end
		end
	end
	local list: { Entry } = {}
	for _, e in byKey do
		table.insert(list, e)
	end
	table.sort(list, function(a, b)
		if a.uses ~= b.uses then
			return a.uses > b.uses
		end
		return a.id < b.id
	end)
	local lines = {
		`TEXTURE INVENTORY: {#list} unique (id, kind) pairs, SurfaceAppearances={surfaceApps}, metalness maps set={withMetalness}`,
		"id\tkind\tuses\texample",
	}
	for i = 1, math.min(MAX_LINES, #list) do
		local e = list[i]
		table.insert(lines, `{e.id}\t{e.kind}\t{e.uses}\t{e.example}`)
	end
	if #list > MAX_LINES then
		table.insert(lines, `... {#list - MAX_LINES} more (raise MAX_LINES)`)
	end
	if withMetalness > 0 then
		table.insert(
			lines,
			"vault: leave MetalnessMap empty on non-metallic surfaces - check each metalness map is really metal"
		)
	end
	table.insert(lines, "read-only run: nothing changed")
	return table.concat(lines, "\n")
end

local report = run()
print(report)
return report
