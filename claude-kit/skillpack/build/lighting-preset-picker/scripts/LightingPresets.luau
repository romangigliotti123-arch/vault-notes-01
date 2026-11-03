--!strict
-- LightingPresets: mood x device presets for Lighting + Atmosphere + post effects, with range validation and a Luau serializer for
-- apply_lighting.luau. Pure logic, unit-tested under Lune. Values are STARTING POINTS tuned by eye in Studio: only bright_cartoon
-- and the warm ambient tint cite a vault source (indie, labelled); every other number is this skill's own. The vault's rules:
-- lighting and atmosphere are foundation (set light direction, intensity and skybox together), use ShadowMap by default, turn off
-- Haze and dynamic clouds for performance, keep post-processing in Lighting. Lighting.Technology and the Sky asset are NOT set here
-- (Technology needs a plugin-level setting; skybox ids are never invented).
local LightingPresets = {}

export type RGB = { number }
export type Preset = {
	mood: string,
	source: string,
	lighting: {
		ClockTime: number,
		Brightness: number,
		Ambient: RGB,
		OutdoorAmbient: RGB,
		ExposureCompensation: number,
		EnvironmentDiffuseScale: number,
		EnvironmentSpecularScale: number,
	},
	atmosphere: { Density: number, Offset: number, Color: RGB, Decay: RGB, Glare: number, Haze: number }?,
	bloom: { Intensity: number, Size: number, Threshold: number }?,
	colorCorrection: { Brightness: number, Contrast: number, Saturation: number, TintColor: RGB }?,
	sunRays: { Intensity: number, Spread: number }?,
	blur: { Size: number }?,
}

local PRESETS: { [string]: Preset } = {
	bright_cartoon = {
		mood = "bright_cartoon",
		source = "indie cartoon preset from the building KB (atmosphere density 0.269, blur 4), rest is the skill's own",
		lighting = {
			ClockTime = 14,
			Brightness = 3,
			Ambient = { 100, 100, 110 },
			OutdoorAmbient = { 140, 140, 150 },
			ExposureCompensation = 0,
			EnvironmentDiffuseScale = 1,
			EnvironmentSpecularScale = 0.5,
		},
		atmosphere = {
			Density = 0.269,
			Offset = 0.25,
			Color = { 199, 215, 235 },
			Decay = { 106, 112, 125 },
			Glare = 0,
			Haze = 1,
		},
		bloom = { Intensity = 0.4, Size = 24, Threshold = 1.2 },
		colorCorrection = { Brightness = 0, Contrast = 0.1, Saturation = 0.2, TintColor = { 255, 255, 255 } },
		sunRays = { Intensity = 0.05, Spread = 0.5 },
		blur = { Size = 4 },
	},
	warm_sunset = {
		mood = "warm_sunset",
		source = "the skill's own; warm ambient tint idea from the building KB (83,70,57 vs default 70,70,70)",
		lighting = {
			ClockTime = 17.8,
			Brightness = 2.5,
			Ambient = { 83, 70, 57 },
			OutdoorAmbient = { 150, 110, 90 },
			ExposureCompensation = 0.2,
			EnvironmentDiffuseScale = 1,
			EnvironmentSpecularScale = 1,
		},
		atmosphere = {
			Density = 0.35,
			Offset = 0.1,
			Color = { 230, 170, 130 },
			Decay = { 180, 100, 80 },
			Glare = 0.4,
			Haze = 1.5,
		},
		bloom = { Intensity = 0.6, Size = 30, Threshold = 1 },
		colorCorrection = { Brightness = 0, Contrast = 0.08, Saturation = 0.15, TintColor = { 255, 235, 215 } },
		sunRays = { Intensity = 0.12, Spread = 0.8 },
	},
	night = {
		mood = "night",
		source = "the skill's own",
		lighting = {
			ClockTime = 0,
			Brightness = 0.5,
			Ambient = { 25, 30, 55 },
			OutdoorAmbient = { 40, 45, 80 },
			ExposureCompensation = 0.4,
			EnvironmentDiffuseScale = 0.6,
			EnvironmentSpecularScale = 0.4,
		},
		atmosphere = {
			Density = 0.25,
			Offset = 0,
			Color = { 40, 50, 90 },
			Decay = { 20, 25, 50 },
			Glare = 0,
			Haze = 0.5,
		},
		bloom = { Intensity = 0.8, Size = 28, Threshold = 0.9 },
		colorCorrection = { Brightness = 0.02, Contrast = 0.1, Saturation = -0.1, TintColor = { 205, 215, 255 } },
	},
	spooky_fog = {
		mood = "spooky_fog",
		source = "the skill's own",
		lighting = {
			ClockTime = 20,
			Brightness = 1,
			Ambient = { 40, 45, 50 },
			OutdoorAmbient = { 60, 65, 70 },
			ExposureCompensation = 0,
			EnvironmentDiffuseScale = 0.7,
			EnvironmentSpecularScale = 0.3,
		},
		atmosphere = {
			Density = 0.55,
			Offset = 0,
			Color = { 120, 130, 130 },
			Decay = { 60, 70, 70 },
			Glare = 0,
			Haze = 2.5,
		},
		bloom = { Intensity = 0.3, Size = 20, Threshold = 1.3 },
		colorCorrection = { Brightness = -0.03, Contrast = 0.15, Saturation = -0.3, TintColor = { 220, 235, 230 } },
	},
	overcast = {
		mood = "overcast",
		source = "the skill's own",
		lighting = {
			ClockTime = 12,
			Brightness = 2,
			Ambient = { 110, 112, 118 },
			OutdoorAmbient = { 125, 128, 135 },
			ExposureCompensation = 0,
			EnvironmentDiffuseScale = 1,
			EnvironmentSpecularScale = 0.3,
		},
		atmosphere = {
			Density = 0.4,
			Offset = 0,
			Color = { 190, 195, 200 },
			Decay = { 140, 145, 150 },
			Glare = 0,
			Haze = 2,
		},
		colorCorrection = { Brightness = 0, Contrast = 0.05, Saturation = -0.1, TintColor = { 255, 255, 255 } },
	},
}

local function copy<T>(v: T): T
	if type(v) ~= "table" then
		return v
	end
	local out: any = {}
	for k, x in v :: any do
		out[k] = copy(x)
	end
	return out
end

function LightingPresets.moods(): { string }
	local names: { string } = {}
	for name in PRESETS do
		table.insert(names, name)
	end
	table.sort(names)
	return names
end

-- device: "pc" keeps the preset; "mobile" removes the costly extras (vault: turn off Haze, keep post-processing small).
function LightingPresets.pick(mood: string, device: string): Preset
	local base = PRESETS[mood]
	if not base then
		error("unknown mood: " .. mood .. " (try: " .. table.concat(LightingPresets.moods(), ", ") .. ")")
	end
	local p = copy(base)
	if device == "mobile" then
		if p.atmosphere then
			p.atmosphere.Haze = 0
		end
		p.sunRays = nil
		p.blur = nil
		if p.bloom then
			p.bloom.Intensity = math.min(p.bloom.Intensity, 0.5)
		end
	elseif device ~= "pc" then
		error("device must be pc or mobile")
	end
	return p
end

local function inRange(v: number, lo: number, hi: number): boolean
	return v >= lo and v <= hi
end

local function rgbOk(c: RGB): boolean
	return #c == 3 and inRange(c[1], 0, 255) and inRange(c[2], 0, 255) and inRange(c[3], 0, 255)
end

function LightingPresets.validate(p: Preset): { string }
	local errors: { string } = {}
	local l = p.lighting
	if not inRange(l.ClockTime, 0, 24) then
		table.insert(errors, "ClockTime outside 0..24")
	end
	if not inRange(l.Brightness, 0, 10) then
		table.insert(errors, "Brightness outside 0..10")
	end
	if not inRange(l.ExposureCompensation, -5, 5) then
		table.insert(errors, "ExposureCompensation outside -5..5")
	end
	if not rgbOk(l.Ambient) or not rgbOk(l.OutdoorAmbient) then
		table.insert(errors, "Ambient colour outside 0..255")
	end
	local a = p.atmosphere
	if
		a
		and (
			not inRange(a.Density, 0, 1)
			or not inRange(a.Offset, 0, 1)
			or not inRange(a.Glare, 0, 10)
			or not inRange(a.Haze, 0, 10)
		)
	then
		table.insert(errors, "Atmosphere value outside range")
	end
	local c = p.colorCorrection
	if
		c
		and (
			not inRange(c.Brightness, -1, 1)
			or not inRange(c.Contrast, -1, 1)
			or not inRange(c.Saturation, -1, 1)
			or not rgbOk(c.TintColor)
		)
	then
		table.insert(errors, "ColorCorrection value outside range")
	end
	return errors
end

-- Luau literal for pasting into apply_lighting.luau as `local PRESET = ...`
function LightingPresets.toLuau(p: Preset): string
	local function ser(v: any, indent: string): string
		if type(v) == "number" then
			return tostring(v)
		elseif type(v) == "string" then
			return string.format("%q", v)
		end
		local keys: { string } = {}
		local isArray = #v > 0
		for k in v do
			table.insert(keys, tostring(k))
		end
		table.sort(keys)
		local parts: { string } = {}
		if isArray then
			for _, x in v do
				table.insert(parts, ser(x, indent))
			end
			return "{ " .. table.concat(parts, ", ") .. " }"
		end
		for _, k in keys do
			table.insert(parts, indent .. "\t" .. k .. " = " .. ser(v[k], indent .. "\t") .. ",")
		end
		return "{\n" .. table.concat(parts, "\n") .. "\n" .. indent .. "}"
	end
	return ser(p, "")
end

return LightingPresets
