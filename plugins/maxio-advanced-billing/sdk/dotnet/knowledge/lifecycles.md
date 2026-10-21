# Maxio Advanced Billing: order of operations and states

**Contents.** Read the sections you need, not the whole file.

- L1 · Catalog setup order
- L2 · Signup, end to end
- L3 · Subscription states
- L4 · Trial end
- L5 · Renewal, failure and dunning
- L6 · Replace a subscriber's card
- L7 · Webhook endpoint health
- L8 · Invoice statuses (Relationship Invoicing)
- L9 · Cancel, then win the customer back

What must exist before what, the order a flow's calls go in, and the state models your code must
handle. Seed the contract sheet's cross-operation invariants from here. Read the item your task
touches, not the whole file.

Each item ends with its sources, tagged as in `rules.md`. A step or cell marked *(inferred)* or
*(unconfirmed)* is not settled by those sources.

---

### L1 · Catalog setup order
1. Product family (the container; no API archive or delete).
2. Products (plans), components (add-ons and usage) and coupons inside the family; give each a handle.
3. Price points on products and components; currency prices after the site currency exists.
4. Offers, then feature templates, then feature catalog items.
5. Subscriptions last.

A family-scoped path with no valid family answers `404 "A valid product_family_id is required"`
(documented on `ListProductsForProductFamily`; assumed for the creates). A currency the site does not
have is rejected with 422: `"Currency must be defined on the site level."` on
`CreateOrUpdateCouponCurrencyPrices`, and `"Currency: is not one of the allowed values."` on
`CreateCurrencyPrices`.

Sources: [docs] basic-concepts/product-catalog "Product Family", basic-concepts/entitlements · [spec] createProductFamily, listProductsForProductFamily, createOrUpdateCouponCurrencyPrices, createCurrencyPrices. Each dependency is stated; the end-to-end order is *(inferred)* from them.

### L2 · Signup, end to end
1. **Once per process** (at startup, or on first use and kept): `ReadSite` → invoicing architecture,
   default collection method, currency, `test` (rules.md R3).
2. **Resolve the plan by handle:** `ListProductsForProductFamily` (`handle:<family>`) or
   `ReadProductByHandle`; pick the price point by handle or `type == default`, never by list position.
3. **Claim the signup in your own store** (one in-flight signup per user) before any Maxio call. Keep
   on the claim the subscription `reference` and one `uniqueness_token` per write this signup makes
   (the customer create, the subscription create), each minted once (rules.md R12). Replace a stored
   token only when you mint a new one (rules.md R11, R12). Derive the `reference` from your own record
   of the signup, never at random. Lookup-then-create is not atomic [observed]; an in-process lock
   does not survive a second instance.
4. **Customer:** call `ReadCustomerByReference` with your user id. Found: use that customer
   (decisions.md D1). On 404 [observed], `CreateCustomer` with that `reference` and its own
   `uniqueness_token`, or send `customer_attributes` carrying the `reference` in step 6. On a
   duplicate-reference 422 [observed], read the customer back.
5. **Payment and collection method:** decide how this customer pays (rules.md R14, decisions.md D2,
   D3). By card or bank: a Maxio.js token or a stored `payment_profile_id`, with `automatic`. Billed
   by invoice: no payment source, with the site's invoice method. Nothing due at signup: no payment
   source, with `automatic` *(inferred)*.
6. **Subscribe:** first see what Maxio already holds.
   - Call `FindSubscription` with your subscription reference, because an earlier attempt whose
     outcome you never learned may have succeeded *(inferred from rules.md R11)*.
   - If step 4 found the customer, also list its subscriptions and keep those on this plan (by
     `product.handle`), except one under your own subscription reference: that one is this signup's
     earlier attempt, which the first bullet settles. List them with `ListSubscriptions` filtered by `customer_id`, paging to an
     empty page (rules.md R8): `ListCustomerSubscriptions` declares no paging.
   - Branch on each `state` found (L3). Access on, transient or coming back → stop: the customer
     already has this plan (rules.md R16). `canceled` or `trial_ended` → reactivate it (decisions.md
     D12) or sign up anew. `expired` or `failed_to_create` → sign up anew. A new signup needs a
     reference no subscription holds yet. When the user's intent is unclear, ask.
   - Nothing found: `CreateSubscription` with one customer source, `product_handle`, an explicit
     `payment_collection_method`, the subscription `reference`, and this create's `uniqueness_token`
     at the body root.
7. **Settle the outcome:**
   - 201 → record it.
   - 422 with an `action_link` → 3-D Secure, not a failure: send the customer through it, then settle
     from a read-back *(whether a subscription exists at this point is unconfirmed)*.
   - Any other 422 → rejected; read the message (rules.md R13). No live subscription was created
     *(inferred)*, though a `signup_failure` webhook can carry a `failed_to_create` record [spec].
     If the request was at fault, correct it and send it with a new token, stored on the claim. If
     that is refused for its reference, sign up anew *(whether a failed signup keeps its reference is
     unconfirmed)*. An account block is not fixed by changing the request.
   - 409, a timeout, a dropped connection, a 5xx, a 408 or a 2xx you cannot read → the outcome is
     unknown. Follow rules.md R11 with `FindSubscription` as the read-back. It is by a unique
     reference you set, so R11 step 4 lets you start again with a new token only after a 409 and
     120 s with nothing found; until then a 404 means "not there yet". Never report an unknown outcome
     as a failure.
8. **Confirm to the user** from the response: product, price, `state`, `current_period_ends_at` (next
   billing date).
9. **Keep it current** from webhooks (`signup_success`, `subscription_state_change`).

Sources: [spec] readSite, findSubscription, listCustomerSubscriptions, listSubscriptions, createSubscription "3D Secure (3DS) Authentication", Subscription (`current_period_ends_at`), Subscription-State (`failed_to_create`) · [docs] about-the-api/duplicate-prevention, about-the-api/error-handling "Timeout Limitation", webhooks-reference · [announcement] 2020-01-27 price point order · [observed] steps 3 and 4

### L3 · Subscription states

| State | Meaning | Access | A second subscription to the same plan beside it? | Exits |
|---|---|---|---|---|
| `active` | Paid and up to date (`cancel_at_end_of_period: true` = "pending cancellation") | yes | no | → `past_due`, `soft_failure`, `on_hold`, `canceled`, `expired`, `suspended` |
| `trialing` | In a valid trial | yes | no | → `active` (paid), `trial_ended` (no-obligation, no card), `past_due`/`canceled` |
| `past_due` | Latest payment failed; in dunning | **yes** (stays on through dunning) | no | → `active` (paid), `canceled` or `unpaid` (dunning end) |
| `soft_failure` | Failed for a merchant-side reason; retried automatically | yes | no | → `active` *(inferred)*; don't ask the customer to act |
| `assessing` | Mid-renewal; transient | keep the previous decision | no | → `active` / `past_due` |
| `pending` | Being created; transient | keep the previous decision | no | → a live state |
| `awaiting_signup` | Created with a future `initial_billing_at` or `defer_signup` | no | no: it starts later | → `trialing`/`active` at the date or on `ActivateSubscription`; → `canceled` if that payment fails |
| `on_hold` | Paused by `PauseSubscription` | no | no: it resumes | → `active` via `ResumeSubscription` or `automatically_resume_at` |
| `suspended` | Prepaid balance used up | no | no: a prepayment restores it | → `active` when a prepayment is applied |
| `unpaid` | Dunning ended with "mark unpaid" | no | no | `ReactivateSubscription` *(unconfirmed, see decisions.md D12)* |
| `canceled` | Canceled by request or by dunning; no collection | no | yes, or reactivate it | → `active`/`trialing` via `ReactivateSubscription` |
| `trial_ended` | No-obligation trial ended without a card | no | yes, or reactivate it | → `active`/`trialing` via `ReactivateSubscription` |
| `expired` | Ran its full fixed term | no | yes | `ReactivateSubscription` alone refuses it *(inferred from its 422 text)*; Maxio's help page says cancel it, then reactivate *(not probed)* |
| `failed_to_create` | Signup failed; seen in a `signup_failure` webhook | no | yes | none |
| `paused` | An internal state no API call produces *(inferred)*. The spec says the merchant's own Maxio account is in arrears; Maxio's help page says Maxio Support paused the subscription *(unconfirmed which)* | no | no: raise it with the merchant *(inferred)* | none via API |

- **Access** matches Maxio's entitlements: `enabled` is true in the states marked yes and in
  `assessing`, false in the rest, and stays true through dunning [docs].
- **`pending` and `assessing`:** never change an access decision because you saw one of them; keep the
  decision you had. Where there is none, as in a one-off list of subscriptions with access, count
  `assessing` in (its entitlements stay enabled, and it is entered from a subscription that already
  had access) and `pending` out (it is still being created) *(inferred)*.
- **"Already subscribed" checks** read the fourth column, for the same plan only, and End of Life in
  the schema means "not billing", not "ended" (rules.md R16). To list by access, see rules.md R9.
- Every state change emits `subscription_state_change` with `previous_state` (meaningful only in
  webhook payloads). Drive access from state changes, never from `renewal_success`: a customer who
  recovers from `past_due` gets `payment_success` and a state change, but no `renewal_success`.

Sources: [spec] Subscription-State, Subscription-State-Filter, Create-Subscription, activateSubscription, resumeSubscription, reactivateSubscription, Subscription (`previous_state`) · [docs] basic-concepts/entitlements, webhooks-reference `renewal_success`; Maxio help "Subscription States" (`paused`, `expired`)

### L4 · Trial end
The price point's `trial_type` decides what happens when a trial ends with no card on file:
`no_obligation` → `trial_ended`, quietly, no emails; `payment_expected` → `past_due`, dunning starts.
Set it on purpose when creating products and price points.

That is for an `automatic` subscription. A `remittance` subscription on a no-obligation trial goes
`active` at trial end instead, so a cardless trial that should lapse must be `automatic`
(rules.md R14).

Sources: [spec] Trial-Type, Subscription-State (`trial_ended`) · [docs] Maxio help "Trialing Subscriptions" (the remittance case; not probed)

### L5 · Renewal, failure and dunning
1. Renewal: `active` → `assessing` → `active` (`renewal_success`), or → `past_due` (`renewal_failure`).
2. In `past_due`, access stays on; `current_period_ends_at` has already advanced, so it is not a
   paid-through date. `next_assessment_at` is the next retry.
3. Dunning ends in `active` (paid), `canceled` (`cancellation_method: dunning`) or `unpaid`.
4. Recovery calls differ in whether they collect (decisions.md D12).
5. Renewal webhooks also fire while `past_due` (since 2023-01-24); deduplicate on webhook `id`.

Sources: [spec] Subscription-State, Subscription (`next_assessment_at`), Cancellation-Method · [docs] basic-concepts/entitlements, webhooks-reference `renewal_success`, `renewal_failure` · [announcement] 2023-01-24 renewal events

### L6 · Replace a subscriber's card
1. `CreatePaymentProfile` with a Maxio.js token.
2. `ChangeSubscriptionDefaultPaymentProfile` (a new profile never becomes the default by itself).
3. If the subscription is `past_due`: `RetrySubscription` to collect now. (Or do steps 1–3 in one call
   with `UpdateSubscription` + card attributes.)

Step 3 and the one-call form take a payment (rules.md R11).

Sources: [spec] createPaymentProfile, retrySubscription, updatePaymentProfile, updateSubscription "Update Subscription Payment Method"

### L7 · Webhook endpoint health
1. Failures 1–25: retried (about 0 s, 10 s, 15 s, 90 s, 180 s after each failure, up to 5 attempts).
2. Failures 26–50: new webhooks are created **paused** and must be replayed by hand; the endpoint is
   re-checked every 2 h.
3. 51 and over: the endpoint is disabled and "Webhooks are no longer generated".

Return 200 for every event, including unhandled ones and `event=test` *(inferred)*. Watch
`ListWebhooks` for `status` `failed` and `paused` (one value per call), and replay with
`ReplayWebhooks` once the receiver is fixed.

Sources: [docs] webhooks "Responding to a Webhook", "Inoperative Endpoints", "Testing Webhooks" · [spec] listWebhooks, Webhook-Status, replayWebhooks

### L8 · Invoice statuses (Relationship Invoicing)
| Status | Reached by | Next |
|---|---|---|
| `draft` | `CreateInvoice` with `status: draft` | `UpdateInvoice`, `DeleteInvoice` (ad hoc), `IssueInvoice` |
| `pending` | Accrued allocation charges; `rollback_to_pending` | `IssueInvoice`, `VoidInvoice` (not consolidated) |
| `open` | Issued and due | paid → `paid`; `VoidInvoice`; subscription canceled → `canceled` |
| `processing` | A payment was started and is not yet confirmed, for example Direct Debit | → `paid`, or back to `open` if the payment fails *(inferred)*. Do not treat it as paid |
| `paid` | Paid in full | `RefundInvoice`. `VoidInvoice` does not take a paid invoice, but a full refund with `void_invoice: true` voids it |
| `canceled` | Was `open` when the subscription was canceled; no longer due | `ReopenInvoice`, `VoidInvoice` |
| `voided` | `VoidInvoice` | none |

Sources: [spec] Invoice-Status, Create-Invoice-Status, issueInvoice, voidInvoice, reopenInvoice, Refund-Invoice · [docs] Maxio help "Advanced Billing Invoices Overview" (`processing`)

### L9 · Cancel, then win the customer back
1. Cancelling turns every `open` invoice `canceled` and stops collection.
2. To collect older periods' invoices, `ReopenInvoice` each **before** reactivating; reactivation
   reopens only the most recent period's.
3. Reactivate with the `resume` choice from decisions.md D12. Credits and prepayments are spent by
   default when the reactivation resumes the current period; for a new period that is
   *(unconfirmed)*. Reactivation can take a payment (rules.md R11).

Sources: [spec] Subscription-State (`canceled`), reopenInvoice, reactivateSubscription · [announcement] 2021-02-12 reactivation behavior change
