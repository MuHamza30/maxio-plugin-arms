# Subscription Status: provider notes

Cancel, delay a cancel, reactivate, hold, resume, retry and dunning. Which one fits a need is in
`../decisions.md` D11 and D12; the state model is `../lifecycles.md` L3. An operation of this group that
has no section here has no provider notes (see `../index.json`).

### cancelSubscription
`client.subscription_status.cancel_subscription` · `DELETE /subscriptions/{subscription_id}.json` · contract: `map/operations/subscription_status.md`
**Always:** To cancel now, send neither `cancel_at_end_of_period` nor `scheduled_cancellation_at` (D11). On prepaid, `refund_prepayment_account_balance` defaults to a refund and needs the Schedule Subscription Cancellation feature.

**Before you call**
- Decide the timing (D11): now, at the end of the period, or on a date. The two schedule parameters,
  `cancel_at_end_of_period` and `scheduled_cancellation_at`, need the site's Schedule Subscription
  Cancellation feature (`read_site`: `schedule_subscription_cancellation_enabled`) [spec]. For a cancel
  at the end of the period use `initiate_delayed_cancellation`, which needs no feature (D11).
- On a prepaid subscription, decide `refund_prepayment_account_balance`. It defaults to `true`, which
  refunds the remaining prepaid balance as part of the cancellation [spec]. The spec says this option
  also needs the Schedule Subscription Cancellation feature; what a site without the feature does
  with a prepaid balance is not stated *(unconfirmed)*.

**Rules**
- With neither schedule parameter the state becomes `canceled` at once [spec]. `canceled` is End of
  Life (not billing): the subscription can be reactivated (D12), and there is room for a new signup.
- Cancelling freezes the account; it does not collect. Every `open` invoice becomes `canceled` ("no
  longer considered to be due") and no further collection is attempted [spec].
- `scheduled_cancellation_at` "is not applicable for prepaid subscriptions" [spec].
- `reason_code` takes a code from `list_reason_codes`, not free text. Free text goes in
  `cancellation_message` [spec].

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 422 "The subscription is already canceled" | Already canceled. This message arrives as a single `error` string, not in an `errors` list [spec] | Treat as done; read the subscription back |
| 422 "subscription must be an Object" | The body is not wrapped in `subscription` | Send the options inside a `subscription` object |
| 422 "reason_code size cannot be greater than 255" | Free text was sent as `reason_code` | Send a code from `list_reason_codes`; put free text in `cancellation_message` |

**Sources:** [spec] cancelSubscription, Cancellation-Options, Subscription-State, reopenInvoice

### initiateDelayedCancellation
`client.subscription_status.initiate_delayed_cancellation` · `POST /subscriptions/{subscription_id}/delayed_cancel.json` · contract: `map/operations/subscription_status.md`
**Always:** Never call while `past_due` (D11). Send a body-root `uniqueness_token` (R12); a timeout is unknown (R11). The answer is only a message: confirm with `read_subscription` that `cancel_at_end_of_period` is `true`.

**Before you call**
- The subscription must already exist (this cannot be set at creation) and must not be `past_due`
  [spec].
- Read it first. When `cancel_at_end_of_period` is already `true`, send nothing (R12).

**Rules**
- It takes an optional body: the `Cancellation-Request` that `cancel_subscription` takes, with
  `cancellation_message` and `reason_code` inside `subscription` [spec]. So it can carry a
  `uniqueness_token` at the body root (R12), unlike `retry_subscription` and `resume_subscription`,
  which have no body (R11 step 5). Send one random token per cancellation, with an empty
  `subscription` object when you set no reason: `{"subscription": {}, "uniqueness_token": "..."}`.
  After a timeout, read back `cancel_at_end_of_period` (R11 step 1). Still `false` once 120 seconds
  have passed: resend with the same token (R11 steps 2 and 3).
- Cancels at the end of the current billing period [spec]. Until then the subscription keeps its
  `state` *(inferred)*: there is no pending-cancellation state, and `pending_cancellation` exists only
  as a value of the `list_subscriptions` filter.
- The response is only `message`. The proof that it landed is `cancel_at_end_of_period: true` on
  `read_subscription` (D11): that is the flag this call sets and `cancel_delayed_cancellation` resets to
  `false` [spec]. `delayed_cancel_at` is the "Timestamp for when the subscription is currently set to
  cancel" [spec]: read it for the date, but do not test it alone *(inferred: the spec does not say
  this call always fills it)*.
- The `pending_cancellation_change` webhook fires when a delayed cancel is set **and** when it is
  cleared [docs]. The event alone is not proof: re-read the subscription (R20).
- Undo with `cancel_delayed_cancellation`, which is idempotent [spec].

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 422 (message not documented) | The subscription is `past_due`. The spec states the rule but not the answer it gives (status not documented) | Recover payment first (D12), or cancel now with `cancel_subscription` |
| 422 "The subscription is already canceled" | Already canceled | Nothing to schedule |

**Sources:** [spec] initiateDelayedCancellation, cancelDelayedCancellation, Subscription · [docs]
webhooks-reference (pending_cancellation_change)

### reactivateSubscription
`client.subscription_status.reactivate_subscription` · `PUT /subscriptions/{subscription_id}/reactivate.json` · contract: `map/operations/subscription_status.md`
**Always:** It can take a payment: turn off the client's automatic retry for it, and settle a timeout by R11. For resume-or-nothing send `resume: {"require_resume": true}`; plain `resume: true` can start a new, charged period (D12).

**Before you call**
- The state is `canceled` or `trial_ended` [spec]. For `unpaid` the spec disagrees with itself: the
  422 text lists it as allowed, the list of states that work does not *(unconfirmed, D12)*. For
  `on_hold` use `resume_subscription` instead. For `expired`, Maxio's Subscription States page says to
  cancel it first and then reactivate it [docs] *(not probed)*.
- To collect canceled invoices from **older** periods, `reopen_invoice` them first; reactivation
  reopens only those of the most recent active period [spec] (lifecycles.md L9).
- Decide `resume`, `include_trial`, `preserve_balance` and `use_credits_and_prepayments`.

**Rules**
- **Payment (R11).** Reactivation can collect: it captures the open invoices, and one that starts a
  new billing period charges for that period [spec]. So this `PUT` can take a payment: turn automatic
  retry off for it and allow at least 120 seconds (R11). It can carry a `uniqueness_token` (R12).
  After an unknown outcome the read-back is `read_subscription` (`state`). It is not by a unique
  reference, so a reactivation still not settled after a 409 is settled from webhooks or by hand,
  never sent again automatically (R11 step 4).
- `resume: true` silently falls back to a **new, charged billing period** when the subscription can no
  longer be resumed [spec]. When the intent is "resume or do nothing", send
  `resume: {"require_resume": true}`: then, if it cannot be resumed, the subscription "will be left in
  its current state" [spec].
- A subscription is resumable only within the billing period it was canceled in [spec]. A resume keeps
  the billing date; payment "may or may not be collected", depending on the balance the subscription
  had when it was canceled [spec].
- `trial_ended` and `resume`: the spec's scenarios show `resume: true` working on a `trial_ended`
  subscription. Maxio's Reactivating and Resuming page says a Trial Ended subscription cannot be
  resumed and must start a new billing period [docs]. The two disagree *(unconfirmed)*: when a new
  period is not acceptable, send `require_resume` and handle the 422.
- Without `include_trial`, a product with a trial reactivates straight to `active` [spec], and the new
  period is charged *(inferred)*.
- `preserve_balance: true` keeps the old balance and adds the reactivation charges to it [spec].
- Credits and prepayments: since 2021-02-22 a reactivation within the current billing period applies
  service credits and prepayments to the invoice by default; send
  `use_credits_and_prepayments: false` to keep them [announcement]. For a reactivation that starts a
  new period the announcement does not say *(unconfirmed)*. Send the field explicitly either way.

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 422 "Cannot reactivate a subscription that is not marked …" | Wrong state. The message goes on to list Canceled, Unpaid and Trial Ended | `on_hold`: use `resume_subscription`. `expired`: cancel it first, then reactivate [docs]. Any other state: there is nothing to reactivate |
| 422 "Request was 'resume only', but this subscription cannot be resumed." | `require_resume` was sent after the billing period it was canceled in had ended. Nothing changed | Decide with the user whether a new, charged period is acceptable. If so, reactivate without `resume` |
| 422 "No payment method was on file for the …" | No payment profile is on file for the amount due at reactivation [announcement] | Add a payment method (D6), then reactivate again on purpose |
| 422 "The credit card on file could not be charged." | The payment was declined. Since 2021-10 the gateway's own decline text is returned instead [announcement]; the spec still shows this text | Get a working payment method (D6), then reactivate again on purpose. Never from an automatic retry (R11) |
| 422 with an `action_link` | 3-D Secure is required [spec]. This is not a decline | Send the customer to the link. Do not resend |

**Sources:** [spec] reactivateSubscription, Reactivate-Subscription-Request, Resume-Options,
reopenInvoice · [docs] about-the-api/duplicate-prevention, error-handling "Timeout Limitation",
Maxio help "Subscription States" and "Reactivating and Resuming" · [announcement] 2021-02-12
reactivation behavior, 2021-09-13 reactivation decline errors

### pauseSubscription
`client.subscription_status.pause_subscription` · `POST /subscriptions/{subscription_id}/hold.json` · contract: `map/operations/subscription_status.md`
**Always:** Pause only when `current_period_ends_at` is more than 24 hours away. Set any `automatically_resume_at` at least 24 hours ahead; omit it for an open-ended hold. The state becomes `on_hold`, never `paused` (R16).

**Before you call**
- The next billing date must be more than 24 hours away. The spec states this limit on
  `next_billing_at`, a field no response carries; read `current_period_ends_at` instead, as the spec
  itself advises for `update_subscription` [spec].
- Any `automatically_resume_at` should be at least 24 hours ahead. That minimum is documented on
  `update_automatic_subscription_resumption` and assumed to hold here *(inferred)*.

**Rules**
- A paused subscription is `on_hold`, **not** `paused`. `paused` is an internal state no API call
  produces (R16). Renewal stops [spec] and entitlements turn off [docs].
- `on_hold` is not billing but is expected to come back [spec]: no access meanwhile, and never create
  a second subscription to the same plan beside it (R16).
- Omit `automatically_resume_at` for an open-ended hold; change or clear it later with
  `update_automatic_subscription_resumption`.

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 422 "This subscription is not eligible to be put on hold." | The next billing date is within 24 hours [spec], or the subscription cannot be held for another reason *(inferred)* | Wait until after the renewal, then pause |
| 422 "Automatic resume date: must be at least 24 hours in the future." | `automatically_resume_at` is too soon (documented on `update_automatic_subscription_resumption`; assumed here) | Send a later date, or none |

**Sources:** [spec] pauseSubscription, updateSubscription, updateAutomaticSubscriptionResumption,
Subscription-State · [docs] basic-concepts/entitlements · [observed] code waiting for `paused` broke the
resume flow

### updateAutomaticSubscriptionResumption
`client.subscription_status.update_automatic_subscription_resumption` · `PUT /subscriptions/{subscription_id}/hold.json` · contract: `map/operations/subscription_status.md`
**Always:** Call only while the subscription is `on_hold`. Send `automatically_resume_at` at least 24 hours ahead, or `null` to remove the date and leave the hold open-ended.

**Rules**
- Same route as `pause_subscription`, with `PUT`: it changes only the resume date of a subscription that
  is already on hold [spec].
- `automatically_resume_at: null` removes the date [spec]. The subscription then stays `on_hold` until
  `resume_subscription`.
- A resume date later than the original renewal date leads to a charge when the hold ends, as it does
  for `resume_subscription` *(inferred)*.

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 422 "Subscription is not currently on hold." | The state is not `on_hold` | Nothing to change. Use `pause_subscription` to start a hold |
| 422 "Automatic resume date: must be at least 24 hours in the future." | The date is less than 24 hours away | Send a later date, or `null` |

**Sources:** [spec] updateAutomaticSubscriptionResumption, resumeSubscription

### resumeSubscription
`client.subscription_status.resume_subscription` · `POST /subscriptions/{subscription_id}/resume.json` · contract: `map/operations/subscription_status.md`
**Always:** Call only when the state is `on_hold`. Check first whether the original renewal date has passed: after it, resuming charges the customer at once (D12).

**Before you call**
- The state must be `on_hold`. Check whether the original renewal date has passed.

**Rules**
- Before the original renewal date: back to `active`, renewing on the original date. After it: behaves
  like a reactivation, the billing date becomes now and the customer is **charged immediately** [spec].
- After that date this call takes a payment. It has no request body, so it cannot carry a
  `uniqueness_token`: never resend it automatically (R11 step 5). After an unknown outcome read the
  subscription back with `read_subscription` (`state`) and settle from that, from webhooks or by hand.

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 422 "Only subscriptions that are on hold can be resumed." | The state is not `on_hold` | For `canceled` or `trial_ended` use `reactivate_subscription`. Other states: D12 |

**Sources:** [spec] resumeSubscription

### retrySubscription
`client.subscription_status.retry_subscription` · `PUT /subscriptions/{subscription_id}/retry.json` · contract: `map/operations/subscription_status.md`
**Always:** Call only on a `past_due` subscription. It takes a payment and cannot carry a `uniqueness_token`: never resend it automatically, allow 120 seconds, and after a timeout read the subscription back (R11).

**Before you call**
- The subscription is `past_due` and has a chargeable payment method. This is how to collect after
  fixing the card with `update_payment_profile`, which does not collect by itself [spec].

**Rules**
- **Payment (R11).** This `PUT` retries "collecting the balance due" [spec]: turn automatic retry off
  for it and allow at least 120 seconds (R11). It has no request body, so it cannot carry a
  `uniqueness_token` and is never resent automatically (R11 step 5). After an unknown outcome read the
  subscription back with `read_subscription` (`state`, `balance_in_cents`) and settle from that, from
  webhooks or by hand.
- On success the subscription returns to `active` and Maxio emits `payment_success` and
  `subscription_state_change`, but **not** `renewal_success` [docs].

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 422 "base: subscription retry was unsuccessful" | The payment was declined again, or the subscription was not `past_due` *(second cause inferred)* | Get a new payment method and collect through the subscription (D6, D12). Do not loop |
| 422 with an `action_link` | 3-D Secure is required [spec]. This is not a decline | Send the customer to the link. Do not resend |

**Sources:** [spec] retrySubscription, updatePaymentProfile · [docs] about-the-api/duplicate-prevention,
error-handling "Timeout Limitation", webhooks-reference (renewal_failure, renewal_success)

### cancelDunning
`client.subscription_status.cancel_dunning` · `POST /subscriptions/{subscription_id}/cancel_dunning.json` · contract: `map/operations/subscription_status.md`

**Rules**
- "Cancels the active dunning process … and sets it to active." Nothing is collected; the balance
  presumably stays owed *(inferred)*. Pair it with a recorded payment (`record_payment_for_invoice`,
  `record_payment_for_subscription`) if the debt matters; `retry_subscription` no longer applies once the
  state is `active` *(inferred)*.

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 422 "This subscription is not eligible to have its dunning canceled." | The subscription is not in dunning | Nothing to cancel |

**Sources:** [spec] cancelDunning

### previewRenewal
`client.subscription_status.preview_renewal` · `POST /subscriptions/{subscription_id}/renewals/preview.json` · contract: `map/operations/subscription_status.md`

**Rules**
- Read-only. Uses **current** component quantities: "End-of-period values for components are not
  predicted", so metered and event-based amounts come out low [spec]. Pass `components` with
  quantities for what-ifs.
- Free components appear as line items when their recorded quantity is above 0 (since 2021-11-18)
  [announcement].

**Sources:** [spec] previewRenewal · [announcement] 2021-11-18 renewal preview
