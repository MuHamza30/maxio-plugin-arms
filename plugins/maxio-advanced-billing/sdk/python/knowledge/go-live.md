# Maxio Advanced Billing: before you report the work done

**Contents.** Read the sections you need, not the whole file.

- Prove it against a sandbox
- G1 · Every signup sends `payment_collection_method`, chosen by how the customer pays
- G2 · Customers are found by `reference` before create
- G3 · Each write that may be resent carries a `uniqueness_token` at the body root
- G4 · Every list that takes `page` and `per_page` pages until an empty page with `per_page` within the cap
- G5 · Money fields are scaled by field name
- G6 · Access decisions and "already subscribed" checks
- G7 · At most 4 requests in flight per subdomain
- G8 · A 4xx is never taken as proof a call works
- G9 · Plan changes use the intended proration
- G10 · Cancellation timing matches intent
- G11 · Webhook endpoint
- G12 · Card data never touches your server unless the merchant is PCI compliant
- G13 · Site subdomain, region and API key come from configuration
- G14 · New payment profiles are made the default explicitly
- G15 · Null is accepted wherever the contract allows it

Go through every row that applies to the scope. Each row names the check and how to prove it. "I
believe it works" is not evidence; a passing test that never reached Maxio, or reached it and got a 4xx,
is not evidence either.

Provenance: each checklist row checks a rule, a decision or a lifecycle and cites it by id; the sources
are on that item. A step or row that states something of its own carries its own tag.

## Prove it against a sandbox

Probing a test site before and after coding was the most valuable behaviour observed across agent runs,
and agents that skipped it shipped request bodies the sandbox always rejects [observed].

1. **Write only to a test site.** `read_site` returns `test: true` before any write (rules.md R2). If the
   only credential you have is for a live site, probe read-only, never write, and say that writes were
   not exercised.
2. **Probe read-only first.** One `read_site`, one catalog read by handle, one customer lookup by a
   reference that does not exist (expect 404 [observed]). Note what came back.
3. **Verify writes with fresh data.** Create with a new customer reference each run, then read the
   result back and check its timestamps. Leftover sandbox data can make an idempotent path return an
   old success and hide a live 422 [observed].
4. **Prove duplicate safety under concurrency.** Fire the same signup 6 times in parallel and check
   that exactly one subscription exists. Tests that pass once prove nothing here: concurrent requests
   produced 2–3 subscriptions in runs that claimed double-click safety [observed].
5. **Prove the unknown outcome.** Drop the first response to a create, run the signup again, and check
   that the second attempt read back, found the subscription, sent no second create, and left one
   subscription (rules.md R11, R12).
6. **Report only what you ran.** Name each check above as run or not run; never write "verified live"
   for a path that never executed [observed].

## Checklist

| # | Check | How to prove it |
|---|---|---|
| G1 | Every signup sends `payment_collection_method`, chosen by how the customer pays, with the invoice value that fits the site when the merchant bills by invoice (rules.md R3, R14; decisions.md D3) | Read each created subscription back: its `payment_collection_method` is the one intended, a card or bank signup has a payment profile on file, and an invoiced signup has the site's invoice method with no card charged. A 201 without a card proves nothing by itself |
| G2 | Customers are found by `reference` before create; a duplicate reference is read back; email is never the key (decisions.md D1, lifecycles.md L2) | Two signups for one user leave one customer |
| G3 | Each write that may be resent carries a `uniqueness_token` at the body root (inside the event for event ingestion): one per write, the same on every resend of it, a new one only after a corrected 422 or at R11 step 4. Signups are serialized per customer in your own store. An unknown outcome (a timeout, 5xx, 408 or 409) is settled in R11's order and never reported as a failure; a write that cannot carry a token is never resent automatically (R11, R12) | The 6-way concurrency test and the dropped-response test above |
| G4 | Every list that takes `page` and `per_page` pages until an empty page with `per_page` within the cap; `list_allocations` pages by `page` alone; lists that take neither are called once (R8) | A test with more than one page of data |
| G5 | Money fields are scaled by field name: `*_in_cents` integer cents, `unit_price`/invoice amounts decimal (R4) | A price shown to the user matches the catalog |
| G6 | Access decisions and "already subscribed" checks (same plan only) use the full state table (R16, lifecycles.md L3) | Unit test per state, for access and for "already subscribed" |
| G7 | At most 4 requests in flight per subdomain; a 429 backs off for minutes and is not resent automatically; no write is resent blindly, and the payment-taking `PUT`s have automatic retry off and at least 120 s (R10, R11) | Test with a stubbed 429; a stubbed timeout on a payment-taking write shows one request |
| G8 | A 4xx is never taken as proof a call works; a 409 is treated as unknown; 3-D Secure `action_link` and account blocks are handled; raw bodies and serializer text never reach your callers (R13) | Test with a stubbed 422 body, a stubbed 409 and a malformed 200 body |
| G9 | Plan changes use the intended proration (`preserve_period: true` for mid-period changes) and are previewed first, where the preview accepts the subscription (decisions.md D13) | Preview amounts match the charge |
| G10 | Cancellation timing matches intent; a delayed cancel is confirmed by `cancel_at_end_of_period`; a prepaid refund is an explicit choice (decisions.md D11) | Read the subscription back after cancelling |
| G11 | Webhook endpoint: public, on port 80 or 443, HTTPS before live mode [docs]. Receiver: signature over the raw body, 200 within ~15 s, dedupe by webhook `id`, re-reads state, accepts both spellings of renamed events (R19, R20) | A replayed real body from `list_webhooks` verifies and is processed once |
| G12 | Card data never touches your server unless the merchant is PCI compliant; the API key never reaches a browser; the Maxio.js security token is sent where the site requires it (R1, R15) | Code review of the signup path |
| G13 | Site subdomain, region and API key come from configuration, never from tracked files, and startup fails when one is missing (R2). A handle that differs between sites is configuration too [observed] | Search the diff for the subdomain and key |
| G14 | New payment profiles are made the default explicitly (decisions.md D6, lifecycles.md L6) | Read the subscription's default profile back |
| G15 | Null is accepted wherever the contract allows it; unknown fields are accepted (R7) | Deserialize a response with extra and null fields |

Source for the endpoint requirements in G11: [docs] webhooks "Using Webhooks".
