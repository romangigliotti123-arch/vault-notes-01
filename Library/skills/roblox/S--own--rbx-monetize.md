---
id: "rbx-monetize"
type: skill
category: "roblox"
source: "own"
license: "first-party"
repo_path: "skills/roblox/rbx-monetize/SKILL.md"
description: "Set up and review Roblox monetisation: game passes, developer products with a correct ProcessReceipt, premium benefits, ethical pricing. Use when adding purchases to a Roblox game or auditing existing ones."
orig_name: "rbx-monetize"
tags: [lib/skill, cat/roblox, src/own]
---

# rbx-monetize

> Set up and review Roblox monetisation: game passes, developer products with a correct ProcessReceipt, premium benefits, ethical pricing. Use when adding purchases to a Roblox game or auditing existing ones.

Type: skill | Category: [[categories/cat-roblox|roblox]] | Source: [[sources/src-own|own]] | License: first-party
Repo file: `skills/roblox/rbx-monetize/SKILL.md` (extra files, if any, sit beside it in the repo)

Related: [[S--own--rbx-analytics]]

---
# Roblox monetisation setup

Code comments: none by default (see rbx-luau, Comments).

Output: product list (names, purpose, Robux price, grant logic), working Luau, then a checklist verdict.

## Choose the product type
- Game pass: one-time permanent unlock (VIP area, extra slot). Check ownership with `MarketplaceService:UserOwnsGamePassAsync(userId, passId)` (pcall it, cache per player, re-check on `PromptGamePassPurchaseFinished`).
- Developer product: repeatable (currency packs, revives, boosts). Granted only through `MarketplaceService.ProcessReceipt`.
- Premium: benefits via `Player.MembershipType == Enum.MembershipType.Premium`; never lock core content behind it.

## ProcessReceipt (the part most often wrong)
```lua
MarketplaceService.ProcessReceipt = function(info)
	local player = Players:GetPlayerByUserId(info.PlayerId)
	if not player then return Enum.ProductPurchaseDecision.NotProcessedYet end
	local profile = getProfile(player)
	if not profile then return Enum.ProductPurchaseDecision.NotProcessedYet end
	if profile.receipts[info.PurchaseId] then
		return Enum.ProductPurchaseDecision.PurchaseGranted
	end
	local grant = grants[info.ProductId]
	if not grant then return Enum.ProductPurchaseDecision.NotProcessedYet end
	grant(player, profile)
	profile.receipts[info.PurchaseId] = true
	if not saveNow(player) then
		return Enum.ProductPurchaseDecision.NotProcessedYet
	end
	return Enum.ProductPurchaseDecision.PurchaseGranted
end
```
Rules: set the callback once, on the server, in one script; return `PurchaseGranted` only after the grant is saved; dedupe by `PurchaseId`; if unsure return `NotProcessedYet` (Roblox retries).

## Pricing and design checks
1. Every product has a one-line benefit shown before the prompt; prompts come from a server-validated request, not spam.
2. No pay-to-win that breaks PvP fairness; no real-money-style gambling; no paid random rewards (eggs, spins, crates bought with Robux); no fear-of-missing-out countdowns aimed at kids.
3. Price ladder: 3-5 tiers, a clearly best-value tier, a cheap entry price. Check current Robux and DevEx rules in official docs, not from memory.
4. A free path exists to every core progression step; paid items speed up or decorate.
5. Test with the Studio purchase flow and a second test account: buy, receive, leave, rejoin, still owned; a failed purchase grants nothing; the same receipt twice grants once.
6. Log purchases (anonymised player id, product, time) for rbx-analytics.

Verdict: list each product with pass/fail on checks 1-5 and the exact fix for each fail.
