--!strict
-- OfferLint: check a list of paid offers against the vault's pay-to-win and paid-randomness rules before they ship.
-- Each offer is described by yes/no facts you fill in honestly; the linter turns them into BLOCK / WARN findings with the rule's source.
-- It judges the description you give it, not the live game, and Roblox policy changes: live-check the cited rule before relying on a verdict.
--   local findings, blocked = OfferLint.check({ { name = "Sword Crate", randomized = true, oddsShown = false } })
local OfferLint = {}

export type Offer = {
	name: string,
	priceRobux: number?,
	pvp: boolean?, -- the offer is usable in competitive player-versus-player play
	grantsCombatPower: boolean?, -- changes damage, health, aim or other fight outcomes
	gatesCoreProgress: boolean?, -- free players cannot reach required content without it
	requiresHardCurrency: boolean?, -- core tasks demand the paid currency
	randomized: boolean?, -- paid random outcome (crate, spin, egg, re-roll, key)
	oddsShown: boolean?, -- every outcome and numeric odds shown BEFORE the spend (including keys, re-rolls, luck boosts)
	restrictionPathHandled: boolean?, -- code checks the platform's paid-random-items restriction for each player and offers a non-random path
	popupOnJoin: boolean?, -- a sale modal shows on join or stacks on others
	timerSkipOrAppointment: boolean?, -- sells removal of a wait, or forces return at set times
	limitedStock: boolean?, -- capped quantity that makes players race
}
export type Finding = { offer: string, severity: "block" | "warn", rule: string, source: string }

local KB = "monetisation-other.md"

function OfferLint.check(offers: { Offer }): ({ Finding }, boolean)
	local out: { Finding } = {}
	local blocked = false
	local function add(o: Offer, severity: "block" | "warn", rule: string, source: string)
		table.insert(out, { offer = o.name, severity = severity, rule = rule, source = source })
		if severity == "block" then
			blocked = true
		end
	end
	for _, o in offers do
		assert(type(o.name) == "string" and o.name ~= "", "every offer needs a name")
		if o.gatesCoreProgress then
			add(
				o,
				"block",
				"Free players must be able to reach all core content: sell convenience or cosmetics instead",
				"monetisation-gamepasses.md"
			)
		end
		if o.pvp and o.grantsCombatPower then
			add(
				o,
				"block",
				"Paid items must not change damage, health or aim in competitive play (boosts affect progression, not fights)",
				KB
			)
		end
		if o.randomized and not o.oddsShown then
			add(
				o,
				"block",
				"Paid random items must show every outcome and numeric odds before spend, including keys, re-rolls and luck boosts",
				KB
			)
		end
		if o.randomized and not o.restrictionPathHandled then
			add(
				o,
				"block",
				"Paid random items: check the platform restriction per player (PolicyService.ArePaidRandomItemsRestricted) and give restricted players a free, fixed or direct path. Live-check the current rule",
				KB
			)
		end
		if o.requiresHardCurrency then
			add(o, "warn", "Avoid tasks that only the paid currency can complete (forces spending)", KB)
		end
		if o.timerSkipOrAppointment then
			add(
				o,
				"warn",
				"Avoid appointment timers and timers that can be bought out: spend should come from enjoyment, not necessity",
				KB
			)
		end
		if o.popupOnJoin then
			add(o, "warn", "Do not show sales on join or stack modals: offer at the moment of need instead", KB)
		end
		if o.limitedStock then
			add(
				o,
				"warn",
				"Limited stock frustrates players who lose the race; prefer limited TIME with permanent ownership (one creator disagrees, self-reported)",
				KB
			)
		end
		if o.priceRobux ~= nil then
			assert(o.priceRobux >= 0, `offer {o.name} has a negative price`)
		end
	end
	return out, blocked
end

function OfferLint.summary(findings: { Finding }): string
	local b, w = 0, 0
	for _, f in findings do
		if f.severity == "block" then
			b += 1
		else
			w += 1
		end
	end
	return `{b} block, {w} warn`
end

return OfferLint
