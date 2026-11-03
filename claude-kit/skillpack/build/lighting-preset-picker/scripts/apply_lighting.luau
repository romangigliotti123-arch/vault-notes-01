--!strict
-- apply_lighting.luau: show (dry run) or apply a lighting + atmosphere + post-effect preset to Lighting. Dry run by default.
-- Paste into the Studio command bar or send through the Studio MCP `execute_luau` tool (datamodel_type Edit).
-- PRESET below is the output of LightingPresets.toLuau(LightingPresets.pick(mood, device)) (scripts/LightingPresets.luau, tested under
-- Lune): regenerate it for another mood or for mobile and paste it over this table. Existing effects are updated in place, missing
-- ones are created, effects the preset does not mention are left alone and listed. Lighting.Technology and the Sky asset are
-- never touched (set Technology to ShadowMap in the Lighting properties by hand; skybox ids are the owner's choice).
-- One undo step. Take a screenshot before and after (screen_capture) and compare at the camera the players will see.
local APPLY = false

local Lighting = game:GetService("Lighting")
local ChangeHistoryService = game:GetService("ChangeHistoryService")

local PRESET: any = {
	atmosphere = {
		Color = { 199, 215, 235 },
		Decay = { 106, 112, 125 },
		Density = 0.269,
		Glare = 0,
		Haze = 1,
		Offset = 0.25,
	},
	bloom = {
		Intensity = 0.4,
		Size = 24,
		Threshold = 1.2,
	},
	blur = {
		Size = 4,
	},
	colorCorrection = {
		Brightness = 0,
		Contrast = 0.1,
		Saturation = 0.2,
		TintColor = { 255, 255, 255 },
	},
	lighting = {
		Ambient = { 100, 100, 110 },
		Brightness = 3,
		ClockTime = 14,
		EnvironmentDiffuseScale = 1,
		EnvironmentSpecularScale = 0.5,
		ExposureCompensation = 0,
		OutdoorAmbient = { 140, 140, 150 },
	},
	mood = "bright_cartoon",
	source = "indie cartoon preset from the building KB (atmosphere density 0.269, blur 4), rest is the skill's own",
	sunRays = {
		Intensity = 0.05,
		Spread = 0.5,
	},
}

local SECTIONS: { { key: string, class: string } } = {
	{ key = "atmosphere", class = "Atmosphere" },
	{ key = "bloom", class = "BloomEffect" },
	{ key = "colorCorrection", class = "ColorCorrectionEffect" },
	{ key = "sunRays", class = "SunRaysEffect" },
	{ key = "blur", class = "BlurEffect" },
}

local function convert(v: any): any
	if type(v) == "table" and #v == 3 then
		return Color3.fromRGB(v[1], v[2], v[3])
	end
	return v
end

local function show(v: any): string
	if typeof(v) == "Color3" then
		return string.format("(%d,%d,%d)", v.R * 255 + 0.5, v.G * 255 + 0.5, v.B * 255 + 0.5)
	end
	return tostring(v)
end

local function sync(inst: Instance, props: { [string]: any }, lines: { string }, write: boolean)
	local keys: { string } = {}
	for k in props do
		table.insert(keys, k)
	end
	table.sort(keys)
	for _, k in keys do
		local new = convert(props[k])
		local old = (inst :: any)[k]
		if old ~= new then
			table.insert(lines, `  {inst.ClassName}.{k}: {show(old)} -> {show(new)}`)
			if write then
				(inst :: any)[k] = new
			end
		end
	end
end

local function run(): string
	local lines = { `LIGHTING PRESET: {PRESET.mood} ({PRESET.source})` }
	local recording = if APPLY then ChangeHistoryService:TryBeginRecording("lighting-preset-picker") else nil
	sync(Lighting, PRESET.lighting, lines, APPLY)
	for _, sec in SECTIONS do
		local props = PRESET[sec.key]
		local existing = Lighting:FindFirstChildOfClass(sec.class :: any)
		if props then
			if not existing then
				table.insert(lines, `  create {sec.class}`)
				if APPLY then
					local created = Instance.new(sec.class)
					created.Parent = Lighting
					existing = created
				end
			end
			if existing then
				sync(existing, props, lines, APPLY)
			end
		elseif existing then
			table.insert(
				lines,
				`  {sec.class} exists but the preset has none: left in place (consider disabling for mobile)`
			)
		end
	end
	if recording then
		ChangeHistoryService:FinishRecording(recording, Enum.FinishRecordingOperation.Commit)
	end
	table.insert(lines, if APPLY then "applied (one undo step)" else "dry run: nothing changed")
	return table.concat(lines, "\n")
end

local report = run()
print(report)
return report
