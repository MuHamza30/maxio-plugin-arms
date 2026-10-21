# Subscriptions: provider notes

Notes for the Subscriptions operations an integration most often calls. State changes (cancel, hold,
reactivate) are on `subscription-status.md`, plan changes on `subscription-products.md`. An operation
of this group that has no section here has no provider notes (see `../index.json`).

### createSubscription
`client.subscriptions.create_subscription` · `POST /subscriptions.json` · contract: `map/operations/subscriptions.md`
**Always:** Find the customer (`read_customer_by_reference`) and any plan it holds (L2); name it once (D1). Send `payment_collection_method` (R14), `reference`, a body-root `uniqueness_token` kept on resends (R12). Timeout, 409: unknown (R11).

**Before you call**
- Resolve the product by handle (`product_handle`: "The product ID is not currently published, so we
  recommend using the API Handle instead" [spec]) and, if it is not the default, its price point
  (`product_price_point_handle`).
- Customer: exactly one source (decisions.md D1), chosen by a lookup. Call `read_customer_by_reference`
  with your user id first, even when the task says "new customer": a resend meets the customer the
  first attempt created (lifecycles.md L2 step 4). Found: `customer_id` or `customer_reference`, but
  first list its subscriptions on this product. A "new" customer can be one who already holds the plan:
  stop when one of them is in a state that allows no second subscription beside it (lifecycles.md L3,
  fourth column; L2 step 6; R16). One under this signup's own reference is not a second plan: "Look
  first" below settles it. 404: `customer_attributes` carrying that `reference`.
- Collection method: send `payment_collection_method` on every signup, chosen by how the customer will
  pay (R14, D3). Ask when the task does not say.
  - The customer pays by card or bank account: `automatic`, with a payment source.
  - The merchant bills by invoice: `remittance` on a Relationship Invoicing site, `invoice` on a legacy
    Statements site (`read_site`, R3). The customer is not charged automatically [docs]; that the
    subscription starts active with an open invoice is *(inferred)*.
  - Nothing is due at signup (a trial, a free plan): `automatic` with no payment source *(inferred)*.
- Payment source: at most one (D2). A Maxio.js `chargify_token` for new card or bank details (R15), or a
  stored `payment_profile_id`.
- Duplicate safety (R12, lifecycles.md L2 step 3): before the first send, save in your own store a
  `reference` for this signup and a `uniqueness_token` for this create, its own and not the customer
  create's. Derive the reference from your own record of the signup (an order or signup id), so that
  every resend carries the same one and a later signup by the same customer gets a new one. Allow one
  signup in flight per customer.
- Look first: `find_subscription` by that reference. A hit means a subscription already holds the
  reference: do not create. Branch on its `state` as the `find_subscription` section says.

**Rules**
- **Collection method.** Omitted, the site's `default_payment_collection_method` applies (the spec
  declares no default; `automatic` on the test site [observed]). Never switch a card-paying plan to an
  invoice method to clear the first rejection below: the customer would hold an unpaid invoice.
- **What is charged.** Any trial or initial charge is taken at create. "If the card cannot be
  successfully charged, the subscription will not be created" [spec].
- **Reading the answer (R13, lifecycles.md L2 step 7).**
  - 201: created. Settle from the body.
  - 422 carrying an `action_link`: 3-D Secure, not a decline (table below). Whether a subscription
    exists at that point is *(unconfirmed)*.
  - Any other 422: rejected. For a declined card no subscription is created [spec], though a
    `signup_failure` webhook may carry a record in state `failed_to_create` [spec]. A validation error
    creates nothing either *(inferred)*. When the request was at fault, correct it and send it with a
    **new** token: a request that was received spends its token even when it is rejected [docs]. An
    account block is not fixed by changing the request (R13).
  - 409, a timeout, a dropped connection, a 5xx, a 408 or a 2xx you cannot read: the outcome is unknown.
- **Unknown outcome (R11).** Settle it in R11's order. The read-back is `find_subscription` by your
  `reference`, which is a unique reference you set, and the create carries a token, so every step of
  R11 applies, step 4 included. Never report an unknown outcome as a failure.
- **What the token does not cover:** a replay after its window or through another API key (R12). Your
  own record and the reference lookup are the lasting guard; keep signups serialized per customer.
- `uniqueness_token` goes at the top level of the body, beside `subscription`, never inside it [docs].
  It is not in the contract, and neither is `action_link`. How to send the one and read the other is in
  `docs/models.md`, section "Fields the spec does not declare".
- A future `next_billing_at` turns the signup into an import: "no trial or initial charges will be
  applied … no payment will be captured at all" [spec]. To start later and keep the trial and setup
  fee, use `initial_billing_at`; for a fixed billing day use `calendar_billing` (D4).
- `calendar_billing` cannot be combined with `next_billing_at` [spec].
- "You cannot set `cancel_at_end_of_period` at subscription creation" [spec]; with `next_billing_at` it
  answers 422 since 2022-12 [announcement]. Create, then call `initiate_delayed_cancellation`.
- Send coupons in `coupon_codes`, not the deprecated `coupon_code`.
- Components at signup: `allocated_quantity` for quantity-based, `unit_balance` for metered,
  `enabled: true` for on/off. Allocations made at signup fire no `component_allocation_change` webhook
  [docs].
- The currency is fixed at signup: "you cannot update the currency of an existing subscription" [spec].
- An invalid `ref` (referral code) fails the whole signup [spec]; check it first with
  `validate_referral_code` and drop it if it is not valid.
- Unknown `metafields` keys create new site-wide custom fields (limit 100 per resource) [spec].
- Taxes need a full address with ISO codes; without one no tax is assessed [docs].

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 422 "No payment method was on file for the …" | Collection is `automatic` (sent, or the site default), money is due at signup and there is no payment source (documented on `signup_with_subscription_group`; seen here [observed]) | Decide by intent (R14). A customer who pays by card or bank needs a payment source. A customer billed by invoice needs `remittance` or `invoice`. Never switch a card-paying plan to an invoice method to clear this |
| 422 with an `action_link` | 3-D Secure is required [spec]. This is not a decline | Send the customer to the link, then settle with `find_subscription`. Do not resend |
| 422 (the gateway's decline text; not documented) | The card was declined at the first charge. No subscription was created [spec] | Ask for another payment method and send again with a new `uniqueness_token`. `signup_failure` fires for gateway failures, not for validation errors [docs] |
| 422 "Bank routing number: cannot be blank." | Raw bank fields were sent and are incomplete. The spec shows "Bank account number: cannot be blank." beside it | Send only a Maxio.js `chargify_token` in `bank_account_attributes` (R15, D2). Raw bank fields are for a merchant that handles bank details itself |
| 409 `DuplicatePrevention::DuplicateSubmissionError` | A request with this `uniqueness_token` already reached Maxio [docs]. Its outcome is unknown: a 409 never proves success | Follow R11 with `find_subscription` by your reference. Found: settle from what Maxio holds. Still not found once 120 seconds have passed since the first send: start again with a new token (R11 step 4) |
| 429 | Too many requests in flight for the site, or throttling (documented for the whole API in error-handling, not on this operation) | Pause for minutes and lower concurrency (R10). Then send the request again with the same `uniqueness_token`, never a new one (R12) |

**Sources:** [spec] createSubscription, Create-Subscription, Collection-Method, Calendar-Billing,
Subscription-State, initiateDelayedCancellation, Subscription-Group-Signup-Error-Response · [docs]
about-the-api/duplicate-prevention, error-handling "Timeout Limitation" and "Rate Limits and Blocks",
basic-concepts/subscription-signup, webhooks-reference (signup_failure, component_allocation_change) ·
[announcement] 2022-12-07 cancel at end of period · [observed] missing collection method; duplicates
under concurrency (single run)

### previewSubscription
`client.subscriptions.preview_subscription` · `POST /subscriptions/preview.json` · contract: `map/operations/subscriptions.md`

**Rules**
- Same body as `create_subscription`; it "does not create a subscription". Use it to show price, next
  billing date and tax before signup.
- Tax appears only if taxes are configured, the item is taxable and the address is complete. A billing
  address needs payment-profile fields, because the address is stored on the card.
  `skip_billing_manifest_taxes: true` skips tax.

**Sources:** [spec] previewSubscription

### findSubscription
`client.subscriptions.find_subscription` · `GET /subscriptions/lookup.json` · contract: `map/operations/subscriptions.md`
**Always:** A 404 is "not there", not proof that a create failed: after a create with an unknown outcome follow R11. That create gets a new `uniqueness_token` only after a corrected 422, or after a 409 once 120 s pass with nothing found.

**Rules**
- Looks up one subscription by the `reference` you set at create. Use it before a create, and as the
  read-back after every `create_subscription` whose outcome is unknown (rules.md R11, R12).
- A 404 is the normal "not there" answer (R13). It does not prove that an earlier create failed: Maxio
  works on a request for up to 120 seconds [docs], so the first copy may still be running. This lookup
  is by a unique reference you set, so it can settle R11 step 4.
- A hit is not always a live subscription. Read `state` and branch (lifecycles.md L2 step 6, L3):
  - `active`, `trialing`, `past_due`, `soft_failure`, `pending` or `assessing`: the signup landed. Stop.
  - `on_hold`, `suspended`, `unpaid` or `awaiting_signup`: not billing, but coming back. Stop; never
    create a second subscription beside it.
  - `canceled` or `trial_ended`: reactivate it (D12) or sign up again under a new reference, as the
    user intends. `expired` or `failed_to_create`: sign up again under a new reference (L3). Whether
    the lookup returns `failed_to_create` records is not stated *(unconfirmed)*.
- The spec does not say subscription references are unique *(unconfirmed)*; make yours unique by
  construction.

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 404 | No subscription holds that reference. This is the normal "not there" answer. A create sent less than 120 seconds ago may still be running | Before a first create: go on and create. After a create with an unknown outcome it means only "not there yet": follow R11, whose step 4 this lookup can settle |

**Sources:** [spec] findSubscription, Subscription-State · [docs] about-the-api/duplicate-prevention,
error-handling "Timeout Limitation"

### readSubscription
`client.subscriptions.read_subscription` · `GET /subscriptions/{subscription_id}.json` · contract: `map/operations/subscriptions.md`

**Rules**
- For access decisions read `state` and map it with lifecycles.md L3; `enabled` on entitlements is the
  other access signal (entitlements.md).
- Planless subscriptions on the new Catalog experience return `product`, `product_price_point_id` and
  `product_price_point_type` as `null` [spec]. The spec says of them: "This functionality is supported
  in the API, but is not currently supported in SDKs."
- The self-service card-update token appears only with `include[]=self_service_page_token`.

**Sources:** [spec] readSubscription, createSubscription, Subscription-State

### listSubscriptions
`client.subscriptions.list_subscriptions` · `GET /subscriptions.json` · contract: `map/operations/subscriptions.md`
**Always:** Page until a page comes back empty (R8). The `state` filter cannot name `soft_failure`: to list everyone with access, leave it out and classify each row's `state` (R9, R16). Filter `product` by id or exact name, never a handle.

**Rules**
- Prefer webhooks plus a local cache for access checks; use this list to reconcile, with a full pass
  "usually no more than once a month" [docs].
- Page until a page comes back empty. A `per_page` above the maximum is lowered silently, so a loop
  that stops on a short page can stop early (R8).
- `state` here is a filter with its own values, not the subscription's `state`. The spec types it as
  one value per request [spec]. Maxio's tips page says it "accepts a comma-separated list of values"
  [docs]. The two disagree, so send one value per call *(a comma list is unconfirmed)*.
- The filter cannot name `soft_failure`, `assessing`, `pending`, `failed_to_create` or `paused`, and it
  has values that are not states, such as `pending_cancellation` and `awaiting_signup_date` [spec]. So
  a list of everyone who has access cannot be built from `state` filters: it would miss
  `soft_failure`. For that list, page without a `state` filter and classify each row yourself.
- Access by a row's `state` (R16, lifecycles.md L3): on in `active`, `trialing`, `past_due` and
  `soft_failure`. `pending` and `assessing` are transient: keep the access decision you already hold;
  L3 says how to count them where you hold none. The other states mean no access.
- Scope the list to one product only when the user names that product. "The product", with none named,
  means every product on the site; never invent a setting to pick one (D19, D20) *(inferred)*.
- Filter `product` by id or exact name: "Product handle is not supported" [spec]. For incremental sync
  send `date_field=updated_at` with a window; a `date_field` value the list does not know is ignored
  and the whole set comes back (R9) [announcement].

**Sources:** [spec] listSubscriptions, Subscription-State-Filter, Subscription-State · [docs]
about-the-api/tips "Getting Subscription States", "Synchronizing Your Database" · [announcement]
2020-12-18 date_field

### updateSubscription
`client.subscriptions.update_subscription` · `PUT /subscriptions/{subscription_id}.json` · contract: `map/operations/subscriptions.md`
**Always:** A product sent here switches the plan now, with no proration; add `product_change_delayed: true` to switch at renewal (D13). With card details this call can take a payment: turn off the client's automatic retry for it (R11).

**Before you call**
- Know which change you are making: payment card, product, price point, billing date, snap day,
  collection method, or deferred start.

**Rules**
- **Plan change (D13).** A `product_handle` or `product_id` sent here switches the subscription to that
  product **now**: "a product change is instantaneous" [spec]. Nothing is prorated: the customer is
  neither charged nor credited at the time of the change [docs], and "the new payment amount is
  calculated and charged at the normal start of the next period" [spec]. So an upgrade is not paid for
  until renewal *(inferred)*.
- To switch at the next renewal instead, send `product_change_delayed: true` with the product. Only
  that flag defers the change: it "schedules the product change to happen automatically" at the next
  renewal date [spec]. `next_product_id: ""` cancels a scheduled change.
- For a change that takes effect now **and** is prorated, use `migrate_subscription_product` with
  `preserve_period: true` (D13).
- Without a price point the new product's default price point is used [spec]. A price point sent
  alone (`product_price_point_handle` or `product_price_point_id`) follows the same timing: it changes
  now unless `product_change_delayed: true` is sent [spec].
- **Payment (R11).** `credit_card_attributes` here replaces the card and triggers an attempt to collect
  a past-due balance; `update_payment_profile` does not [spec]. So this `PUT` can take a payment: turn
  automatic retry off for it and allow at least 120 seconds (R11). It can carry a `uniqueness_token`
  (R12). After an unknown outcome the read-back is `read_subscription` (`state`, `balance_in_cents`).
  It is not by a unique reference, so a payment still not found after a 409 is settled from webhooks
  or by hand, never sent again automatically (R11 step 4).
- `next_billing_at` is not echoed back; verify through `current_period_ends_at`. Invalid dates roll
  forward silently (February 30 becomes March 2 in a non-leap year) [spec].
- To move the subscription to another stored payment profile, use
  `change_subscription_default_payment_profile` (D6), not this call.

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 422 "Payment collection method cannot be set to 'invoice' when the subscription is past due" | Changing the collection method to `invoice` while the subscription is `past_due` | Collect the balance first (D12) |
| 422 "'expires_at' cannot be set for subscriptions on calendar billing" | `expires_at` sent for a subscription on calendar billing | Do not set it |

**Sources:** [spec] updateSubscription, Update-Subscription, updatePaymentProfile · [docs]
about-the-api/duplicate-prevention, error-handling "Timeout Limitation", Maxio help "Change a
Subscription's Plan"

### activateSubscription
`client.subscriptions.activate_subscription` · `PUT /subscriptions/{subscription_id}/activate.json` · contract: `map/operations/subscriptions.md`
**Always:** It can take a payment: turn off the client's automatic retry for it (R11). Set `revert_on_failure` explicitly. Only on Relationship Invoicing sites (R3), for an `awaiting_signup` or `trialing` subscription not in a group.

**Before you call**
- Relationship Invoicing sites only (rules.md R3); not for subscriptions in a group. The subscription is
  `awaiting_signup` or `trialing` [spec].

**Rules**
- Set `revert_on_failure` deliberately. Omitted or null, the site setting applies (default `true`)
  [spec].
  - `true`: when the payment fails, the state and the billing period stay as they were. For a
    `trialing` subscription the activation invoice is voided and any prepayments and credits applied
    to it are returned.
  - `false`: the activation goes on although the payment failed. A trial ends as `trial_ended`
    (no-obligation trial), `past_due` (trial with an obligation) or `canceled` (no dunning, or dunning
    that cancels at once). For `awaiting_signup` the text says "always canceled", but the spec's own
    diagram shows `past_due` for a product with a trial on a site with dunning. Read `state` back
    instead of assuming.
- **Payment (R11).** This `PUT` attempts a payment: turn automatic retry off for it and allow at least
  120 seconds (R11). It can carry a `uniqueness_token` (R12). After an unknown outcome the read-back is
  `read_subscription` (`state`). It is not by a unique reference, so an activation still not settled
  after a 409 is settled from webhooks or by hand, never sent again automatically (R11 step 4).

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 400 "Purchase Declined. The subscription is now in the …" | The payment failed and the activation was reverted: the message ends with the state the subscription is back in (the spec shows `awaiting_signup`). It arrives under `errors.base` | Fix the payment method, then call again on purpose. Never from an automatic retry (R11) |

**Sources:** [spec] activateSubscription, Activate-Subscription-Request · [docs]
about-the-api/duplicate-prevention, error-handling "Timeout Limitation"

### overrideSubscription
`client.subscriptions.override_subscription` · `PUT /subscriptions/{subscription_id}/override.json` · contract: `map/operations/subscriptions.md`
**Always:** Use it only to align fields Maxio manages with your own history. Other fields do not follow (a new `expires_at` leaves the next assessment date), but `current_period_starts_at` sets how mid-period allocations prorate.

**Rules**
- This call sets fields that Maxio normally manages itself, to align them with history from before
  the merchant used Maxio. The spec's own warning: with it "you are stepping out on your own".
- "Changing these fields will not affect any other attributes": for example, a new `expires_at` does
  not move the next assessment date [spec]. So do not use it to change billing or `state`. One field
  does reach billing: `current_period_starts_at` "Allows you to set when the period started so mid
  period component allocations have the correct proration" [spec].
- `current_period_starts_at` is accepted only while the subscription is unbilled (no statements or
  invoices), and it must lie in the past [spec].

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 422 "Current period starts at: must be a valid date/time" | `current_period_starts_at` is not a date-time. The message arrives as a single `error` string | Send an ISO 8601 date-time that lies in the past |
| 400 | A field this call does not accept was sent [spec] | Send only the fields the contract lists for this call |

**Sources:** [spec] overrideSubscription, Override-Subscription

### applyCouponsToSubscription
`client.subscriptions.apply_coupons_to_subscription` · `POST /subscriptions/{subscription_id}/add_coupon.json` · contract: `map/operations/subscriptions.md`
**Always:** Send the codes in the request body. Never use the deprecated `code` query parameter: it replaces every coupon already on the subscription (D18).

**Rules**
- Codes sent in the request body are added to the coupons already on the subscription. A code sent in
  the deprecated `code` query parameter **replaces every coupon** on the subscription, silently
  removing existing discounts [spec].
- Only stackable coupons combine.

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 422 "That coupon is not stackable" | A code in the request cannot be combined with another coupon. The message starts with the code | Remove one of the codes, or use stackable coupons |
| 422 "Coupon code could not be found." | A code in the request does not exist. The message starts with the code | Check the code first with `validate_coupon` (D18) |
| 422 "Coupon Codes: Subscription already has at least one non-stackable coupon." | A coupon already on the subscription blocks any other | Leave the subscription as it is, or remove the existing coupon first with `remove_coupon_from_subscription` |

**Sources:** [spec] applyCouponsToSubscription

### purgeSubscription
`client.subscriptions.purge_subscription` · `POST /subscriptions/{subscription_id}/purge.json` · contract: `map/operations/subscriptions.md`
**Always:** Set `ack` to the subscription's customer id. Call on test sites only. Send `cascade[]=customer` or `cascade[]=payment_profile` only to delete those records too.

**Rules**
- Test sites only. `ack` must equal the subscription's customer id; `cascade[]=customer` and
  `cascade[]=payment_profile` also delete those records [spec]. No `customer_delete` webhook fires
  [docs].

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 400 | Wrong `ack`, or the site is not in test mode *(inferred; the spec gives the status with no message)* | Check the customer id and that `read_site` returns `test: true` |

**Sources:** [spec] purgeSubscription · [docs] webhooks-reference (customer_delete)
