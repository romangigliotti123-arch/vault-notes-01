--!strict
-- StreamerAlias: a stable, anonymous display alias for streamer mode, pure Luau (testable under Lune).
-- The server wires it up: when a player turns streamer mode on, show every OTHER player's alias in your own UI (leaderboards, nameplates,
-- chat headers) instead of their name, and show them as "You" or your alias only if you choose to. The alias is computed from the userId plus a
-- per-session salt, so it is stable within a session (a viewer can follow "Player-K7Q2XM") and a viewer cannot read the id from it (a hash for display, not security: do not use it for anything that must resist a determined attacker).
-- Real names stay in text the platform already filters; this only changes what YOUR client labels. Never store the alias.
local StreamerAlias = {}

local ALPHABET = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789" -- 32 symbols, no look-alikes (0/O, 1/I)

local function hashSalt(salt: string): number
	local h = 2166136261 % 2 ^ 31
	for i = 1, #salt do
		h = (bit32.bxor(h, string.byte(salt, i)) * 16777619) % 2 ^ 31
	end
	return h
end

local function mix(x: number): number
	x = bit32.bxor(x, bit32.rshift(x, 15))
	x = (x * 69069 + 12345) % 2 ^ 31
	x = bit32.bxor(x, bit32.rshift(x, 13))
	x = (x * 69069 + 54321) % 2 ^ 31
	return bit32.bxor(x, bit32.rshift(x, 16))
end

-- six symbols of 32 = 30 bits; collisions are possible in a big server, so callers that must be unique use uniqueAliases
function StreamerAlias.alias(userId: number, salt: string): string
	local x = mix(bit32.bxor(userId % 2 ^ 32, hashSalt(salt)))
	x = mix(x + (userId // 2 ^ 32))
	local out = {}
	for _ = 1, 6 do
		local idx = x % 32
		table.insert(out, string.sub(ALPHABET, idx + 1, idx + 1))
		x = bit32.rshift(x, 5) + 7 * idx + 1
	end
	return "Player-" .. table.concat(out)
end

-- aliases for a whole server with collisions resolved deterministically (later userIds get a -2, -3 suffix); order of userIds does not matter
function StreamerAlias.uniqueAliases(userIds: { number }, salt: string): { [number]: string }
	local sorted = table.clone(userIds)
	table.sort(sorted)
	local seen: { [string]: number } = {}
	local out = {}
	for _, id in sorted do
		local a = StreamerAlias.alias(id, salt)
		seen[a] = (seen[a] or 0) + 1
		out[id] = if seen[a] == 1 then a else `{a}-{seen[a]}`
	end
	return out
end

return StreamerAlias
