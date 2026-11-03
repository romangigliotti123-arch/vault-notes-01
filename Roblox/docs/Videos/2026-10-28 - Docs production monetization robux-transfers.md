---
title: "Docs: production / monetization / robux-transfers"
url: https://create.roblox.com/docs/production/monetization/robux-transfers.md
creator: Roblox Creator Docs
official: true
advice_density: medium
date: 2026-10-28
views: 0
transcript: web-page
confidence: high
tags: [roblox, roblox creator docs, youtube-learn]
---

# Docs: production / monetization / robux-transfers

[Open](https://create.roblox.com/docs/production/monetization/robux-transfers.md) | Roblox Creator Docs | 0 views | 2026-10-28

## Summary
Official Roblox docs on Robux transfers for Roblox Plus subscribers. Covers PromptRobuxTransferAsync usage with sender/receiver/amount, the 10% developer cut (90% to recipient, DevEx-eligible, no Roblox fee), the 10–500 Robux per-transaction limit, and handling sender/receiver receipts with Processed vs NotProcessedYet decisions.

## Tips
- [page](https://create.roblox.com/docs/production/monetization/robux-transfers) **[[monetisation-other]]** Validate receiver user ID and amount server-side before calling PromptRobuxTransferAsync; amount must be between 10 and 500 Robux per transaction.
- [page](https://create.roblox.com/docs/production/monetization/robux-transfers) **[[monetisation-other]]** Grant any transfer-linked reward only after processing the receipt, so rewards go out only for completed transfers.
- [page](https://create.roblox.com/docs/production/monetization/robux-transfers) **[[monetisation-other]]** Return NotProcessedYet from receipt handlers when the player has left the server; the receipt is redelivered when they rejoin.
- [page](https://create.roblox.com/docs/production/monetization/robux-transfers) **[[common-mistakes]]** Do not return Processed before finishing the handler's work; Processed marks the receipt complete and confirms the transfer.
- [page](https://create.roblox.com/docs/production/monetization/robux-transfers) **[[scripting-and-performance]]** Call PromptRobuxTransferAsync from a server-side script and wrap it in pcall; store the returned transferRequestId to correlate with receipts.

## Numbers
- [page](https://create.roblox.com/docs/production/monetization/robux-transfers) Developer revenue share from Robux transfer: **10% of Robux sent** (Recipient receives remaining 90%; Roblox takes no fee on transfers)
- [page](https://create.roblox.com/docs/production/monetization/robux-transfers) Transfer amount limit per transaction: **10 to 500 Robux** (Required range for amount passed to PromptRobuxTransferAsync)
- [page](https://create.roblox.com/docs/production/monetization/robux-transfers) Example payout: **100 Robux sent = 90 to recipient, 10 to game** (Worked example from docs)

## Tools
MarketplaceService:PromptRobuxTransferAsync, MarketplaceService:BindReceiptHandler, Enum.ReceiptType.RobuxTransferSender, Enum.ReceiptType.RobuxTransferReceiver, Enum.ReceiptDecision

## He points to
- Roblox DevEx program

## Topics
[[common-mistakes]] [[monetisation-other]] [[scripting-and-performance]]

Back to [[Roblox Creator Docs - How to make successful Roblox games]]
