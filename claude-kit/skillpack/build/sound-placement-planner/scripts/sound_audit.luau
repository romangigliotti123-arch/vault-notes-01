--!strict
local ROOT: Instance? = nil
local MUSIC_MAX_VOLUME = 0.3
local MAX_LIST = 8

local function run(): string
	local root = ROOT or game
	local sounds, audioPlayers, positional, ambient2D = 0, 0, 0, 0
	local flags: { [string]: { string } } = {}
	local function flag(kind: string, inst: Instance)
		local list = flags[kind]
		if not list then
			list = {}
			flags[kind] = list
		end
		table.insert(list, inst:GetFullName())
	end
	for _, inst in root:GetDescendants() do
		if inst:IsA("Sound") then
			local s = inst :: Sound
			sounds += 1
			local parent = s.Parent
			local is3D = parent ~= nil and (parent:IsA("BasePart") or parent:IsA("Attachment"))
			if is3D then
				positional += 1
				if s.Looped and s.RollOffMaxDistance >= 10000 then
					flag("looped 3D sound with default RollOffMaxDistance 10000 (audible map-wide)", s)
				end
			else
				ambient2D += 1
			end
			if s.SoundId == "" then
				flag("empty SoundId", s)
			end
			if parent and parent:IsA("SoundService") then
				flag("sound stored in SoundService (loads at join; create at runtime instead)", s)
			end
			local lower = string.lower(s.Name)
			if
				(string.find(lower, "music", 1, true) or string.find(lower, "theme", 1, true))
				and s.Volume > MUSIC_MAX_VOLUME
			then
				flag(`music volume above {MUSIC_MAX_VOLUME} (official example 0.2)`, s)
			end
			if s.SoundGroup == nil then
				flag("no SoundGroup (no bus to balance or mute)", s)
			end
			if s.Volume > 1 then
				flag("Volume above 1 (clipping risk)", s)
			end
		elseif inst:IsA("AudioPlayer") then
			audioPlayers += 1
			if (inst :: AudioPlayer).Asset == "" then
				flag("AudioPlayer with empty Asset", inst)
			end
		end
	end
	local lines = {
		`SOUND AUDIT: {root:GetFullName()} legacy Sounds={sounds} (3D {positional}, 2D {ambient2D}) AudioPlayers={audioPlayers}`,
	}
	if sounds > 0 and audioPlayers == 0 then
		table.insert(
			lines,
			"all audio is legacy Sound: the docs say prefer Audio objects (AudioPlayer + AudioEmitter) for new work"
		)
	end
	for kind, list in flags do
		table.insert(lines, `[{#list}] {kind}`)
		for i = 1, math.min(MAX_LIST, #list) do
			table.insert(lines, `  e.g. {list[i]}`)
		end
	end
	table.insert(lines, "read-only run: nothing changed")
	return table.concat(lines, "\n")
end

local report = run()
print(report)
return report
