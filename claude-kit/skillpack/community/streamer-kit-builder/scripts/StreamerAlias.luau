--!strict
local StreamerAlias = {}

local ALPHABET = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"

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
