--!strict
-- list_assets.luau: read-only. Lists every distinct asset id referenced in the place, with a count, an example path and the property.
-- Use the list to check ownership, licence and moderation status of each asset before shipping. Studio command bar or MCP `execute_luau` (Edit).
-- ROOTS nil = the whole game except CoreGui-like services that are not accessible.
local ROOTS: { Instance }? = nil

local SERVICES = {
	"Workspace",
	"ReplicatedStorage",
	"ReplicatedFirst",
	"ServerStorage",
	"ServerScriptService",
	"StarterGui",
	"StarterPack",
	"StarterPlayer",
	"Lighting",
	"SoundService",
	"MaterialService",
}

-- class -> properties that can hold an asset id
local PROPS: { [string]: { string } } = {
	MeshPart = { "MeshId", "TextureID" },
	SpecialMesh = { "MeshId", "TextureId" },
	Sound = { "SoundId" },
	AudioPlayer = { "AssetId" },
	Animation = { "AnimationId" },
	Decal = { "Texture" },
	Texture = { "Texture" },
	ImageLabel = { "Image" },
	ImageButton = { "Image", "HoverImage", "PressedImage" },
	ParticleEmitter = { "Texture" },
	Beam = { "Texture" },
	Trail = { "Texture" },
	Sky = { "SkyboxBk", "SkyboxDn", "SkyboxFt", "SkyboxLf", "SkyboxRt", "SkyboxUp" },
	SurfaceAppearance = { "ColorMap", "NormalMap", "MetalnessMap", "RoughnessMap" },
	Shirt = { "ShirtTemplate" },
	Pants = { "PantsTemplate" },
	ShirtGraphic = { "Graphic" },
	MaterialVariant = { "ColorMap", "NormalMap", "MetalnessMap", "RoughnessMap" },
}

local function readProp(inst: Instance, prop: string): string?
	local ok, value = pcall(function()
		return (inst :: any)[prop]
	end)
	if ok and type(value) == "string" and value ~= "" then
		return value
	end
	return nil
end

local found: { [string]: { count: number, example: string, prop: string } } = {}
local function scan(root: Instance)
	for _, inst in root:GetDescendants() do
		for class, props in PROPS do
			if inst:IsA(class) then
				for _, prop in props do
					local value = readProp(inst, prop)
					if
						value
						and (
							string.find(value, "rbxassetid://", 1, true)
							or string.find(value, "rbxasset://", 1, true)
							or string.find(value, "http", 1, true)
							or string.match(value, "^%d+$")
						)
					then
						local entry = found[value]
						if entry then
							entry.count += 1
						else
							found[value] = { count = 1, example = inst:GetFullName(), prop = `{inst.ClassName}.{prop}` }
						end
					end
				end
				break
			end
		end
	end
end

local roots: { Instance } = ROOTS or {}
if not ROOTS then
	for _, name in SERVICES do
		local ok, service = pcall(function()
			return game:GetService(name)
		end)
		if ok and service then
			table.insert(roots, service)
		end
	end
end
for _, root in roots do
	scan(root)
end

local rows = {}
for id, e in found do
	table.insert(rows, { id = id, count = e.count, example = e.example, prop = e.prop })
end
table.sort(rows, function(a, b)
	return a.count > b.count
end)
local lines = { `ASSET LIST: {#rows} distinct ids (check each: owner, licence, moderation state, still available)` }
for _, r in rows do
	table.insert(lines, `{r.id} | x{r.count} | {r.prop} | e.g. {r.example}`)
end
local report = table.concat(lines, "\n")
print(report)
return report
