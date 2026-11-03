--!strict
-- SoundPlan: turn a list of map zones into an audio layout (2D bed, 3D spot emitters, volumetric area sounds) and check the mix.
-- Pure logic, unit-tested under Lune. Vault (sound KB, Creator Docs): prefer Audio objects (AudioPlayer + AudioEmitter) over legacy
-- Sound; keep a constant ambient bed so the game never feels silent; 2D background music Volume about 0.2 so other sounds stay
-- audible; volumetric emitters for rain, rooms, waterfalls, cities; spot ambiences on top of a 2D bed. The spot density and the
-- emitter cap are this skill's defaults (assumptions), not platform numbers.
local SoundPlan = {}

export type Zone = { name: string, kind: string, area: number } -- kind: "outdoor" | "indoor" | "event" | "hub"
export type Layout = {
	zone: string,
	bed: string,
	spots: number,
	volumetric: boolean,
	notes: { string },
}

SoundPlan.SPOT_AREA = 1600 -- studs^2 per spot ambience
SoundPlan.VOLUMETRIC_AREA = 6400 -- areas at least this big get a volumetric emitter instead of many spots
SoundPlan.MUSIC_VOLUME = 0.2
SoundPlan.MAX_SPOTS = 12 -- per zone

function SoundPlan.zone(z: Zone): Layout
	local notes: { string } = {}
	local volumetric = z.area >= SoundPlan.VOLUMETRIC_AREA
	local spots = math.min(SoundPlan.MAX_SPOTS, math.max(1, math.floor(z.area / SoundPlan.SPOT_AREA)))
	if volumetric then
		spots = math.min(spots, 4)
		table.insert(notes, "large area: one volumetric AudioEmitter for the bed texture, few point spots")
	end
	local bed = "looping 2D ambience"
	if z.kind == "indoor" then
		bed = "quiet room tone + reverb on the zone"
		table.insert(notes, "add AudioReverb for the interior, keep outdoor ambience muffled with an equalizer")
	elseif z.kind == "event" then
		bed = "music stinger over the zone bed"
		table.insert(notes, "pair every event sound with a visual cue (accessibility)")
	elseif z.kind == "hub" then
		table.insert(notes, "social space: keep the bed low so voice and UI sounds stay clear")
	end
	return { zone = z.name, bed = bed, spots = spots, volumetric = volumetric, notes = notes }
end

export type Plan = { layouts: { Layout }, totalSpots: number, issues: { string } }

function SoundPlan.plan(zones: { Zone }, concurrentEmitterCap: number?): Plan
	local cap = concurrentEmitterCap or 24 -- assumption: 3D emitters a player can be near at once
	local layouts: { Layout } = {}
	local total = 0
	for _, z in zones do
		local l = SoundPlan.zone(z)
		table.insert(layouts, l)
		total += l.spots
	end
	local issues: { string } = {}
	if #zones == 0 then
		table.insert(issues, "no zones given")
	end
	if total > cap then
		table.insert(
			issues,
			`{total} spot emitters across the map; only those near the player play, stream or pool the rest (cap guide {cap} near a player)`
		)
	end
	return { layouts = layouts, totalSpots = total, issues = issues }
end

export type Bus = { name: string, volume: number, priority: number } -- higher priority ducks lower

-- Mix checks on the bus list: music at the documented level, UI/weapons/dialogue above music in priority.
function SoundPlan.checkMix(buses: { Bus }): { string }
	local issues: { string } = {}
	local byName: { [string]: Bus } = {}
	for _, b in buses do
		byName[b.name] = b
	end
	local music = byName.music
	if music and music.volume > 0.3 then
		table.insert(
			issues,
			`music volume {music.volume} is loud; the official example uses about {SoundPlan.MUSIC_VOLUME}`
		)
	end
	for _, n in { "ui", "weapons", "dialogue" } do
		local b = byName[n]
		if b and music and b.priority <= music.priority then
			table.insert(issues, `{n} should have higher priority than music so music ducks under it`)
		end
	end
	if not music then
		table.insert(issues, "no music bus: add one so players get a separate music slider")
	end
	return issues
end

return SoundPlan
