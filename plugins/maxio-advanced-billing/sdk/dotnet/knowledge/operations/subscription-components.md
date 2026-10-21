# Subscription Components: provider notes

Recording seats, add-ons, usage and events on a subscription. Which call records which component kind
is `../decisions.md` D14. An operation of this group that has no section here has no provider notes
(see `../index.json`).

### allocateComponent
`client.SubscriptionComponents.AllocateComponent` · `POST /subscriptions/{subscription_id}/components/{component_id}/allocations.json` · contract: `map/operations/SubscriptionComponents.md`
**Always:** `quantity` is the new total, not a change; on prepaid each allocation adds units (D14). Send `upgrade_charge`, `downgrade_credit` and `accrue_charge` in the `allocation` when the money outcome matters: omitted, defaults decide.

**Before you call**
- The component is quantity-based, on/off or prepaid [spec], and the quantity actually changes.
- Know the defaults that apply when you leave a field out: the component's own `upgrade_charge` and
  `downgrade_credit`, then the site's (`ReadSite`: `allocation_settings`).

**Rules**
- `quantity` sets "the current allocated quantity for the component" [spec]: send the new total, not
  the difference. An on/off component takes 1 or 0.
- This call has one `allocation` object and no top level. `upgrade_charge` and `downgrade_credit`
  resolve in this order: the value in the `allocation`, then the component default, then the site
  default [spec]. Send them when the outcome matters.
- `accrue_charge: false` attempts the charge now and, if that fails, "the charge will be accrued until
  the next renewal". Omitted, the site setting decides. `initiate_dunning` defaults to `false` [spec].
  So a 200 does not mean the customer paid. Set both explicitly on upgrades.
- Proration uses the component's **current** price and tax rate [spec].
- Prepaid: the proration and accrual fields are ignored. The charge is always immediate and never
  prorated [spec], and each allocation **adds** units. To reduce, delete allocations with
  `DeletePrepaidUsageAllocation`.
- Resends (R11, R12): for a quantity-based or on/off component, sending the same total again changes
  nothing and answers the first 422 below *(inferred)*. For a prepaid component a resend buys the units
  a second time *(inferred)*. Send one `uniqueness_token` beside `allocation` for this write, unchanged
  on every resend of it. After an unknown outcome the read-back is `ListAllocations`. It is not by a
  unique reference, so an allocation still not found after a 409 is settled from webhooks or by hand,
  never sent again automatically (R11 step 4).
- Several components in one request: `AllocateComponents`, which resolves these fields differently.

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 422 "One or more allocation changes are required." | The quantity sent equals the current one *(inferred from the message)* | Skip the call: the component already has that quantity |
| 422 "Allocations can only be updated for quantity and on/off components." | The component is metered or event-based (documented on `PreviewAllocations`; assumed here) | Metered: `CreateUsage`. Event-based: `RecordEvent` (D14) |
| 422 with an `action_link` | 3-D Secure on the immediate charge (documented on `CreateSubscription`; assumed here) | Send the customer to the link. Do not resend |

**Sources:** [spec] allocateComponent, Create-Allocation, previewAllocations,
deletePrepaidUsageAllocation · [docs] about-the-api/tips "Handling Retries Safely"

### allocateComponents
`client.SubscriptionComponents.AllocateComponents` · `POST /subscriptions/{subscription_id}/allocations.json` · contract: `map/operations/SubscriptionComponents.md`
**Always:** Put `upgrade_charge` and `downgrade_credit` inside each allocation: a component default beats the request's top-level values. Send `accrue_charge` at the top level only. Give every allocation a `component_id`.

**Rules**
- `upgrade_charge` and `downgrade_credit` resolve in this order: (1) the value inside each allocation,
  (2) the component default, (3) the request's top-level value, (4) the site default [spec]. So a
  top-level `upgrade_charge` of `none` is silently overridden by a component default of `prorated`
  *(example inferred from that order)*.
- `accrue_charge` resolves differently: the request's top-level value, then the site default [spec]. A
  value inside an allocation is not in that order, so do not rely on one *(inferred)*.
- The charges and credits of all the allocations are "rolled up into a single total which is used to
  determine whether this is an upgrade or a downgrade" [spec].
- "A `component_id` is required for each allocation" [spec]. Each `quantity` is that component's new
  total, not a change; on a prepaid component each allocation adds units (D14).
- Resends follow `AllocateComponent`: one `uniqueness_token` at the top level of the body, the same on
  every resend (R12).

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 422 "Quantity: cannot be blank." | An allocation has no `quantity` | Send `quantity` in every allocation |

**Sources:** [spec] allocateComponents, Allocate-Components, Create-Allocation

### listAllocations
`client.SubscriptionComponents.ListAllocations` · `GET /subscriptions/{subscription_id}/components/{component_id}/allocations.json` · contract: `map/operations/SubscriptionComponents.md`

**Rules**
- Returns "the 50 most recent Allocations, ordered by most recent first" [spec]. It takes `page` but
  no `per_page`: never treat one answer as the whole history. Ask for the next `page` until one comes
  back empty *(inferred: the spec does not describe the last page)*.
- This is the read-back after an allocation whose outcome is unknown: the newest allocation is first.

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 422 "invalid page: 0" | `page` starts at 1 | Send `page` 1 or higher |

**Sources:** [spec] listAllocations

### deletePrepaidUsageAllocation
`client.SubscriptionComponents.DeletePrepaidUsageAllocation` · `DELETE /subscriptions/{subscription_id}/components/{component_id}/allocations/{allocation_id}.json` · contract: `map/operations/SubscriptionComponents.md`
**Always:** Choose `credit_scheme` by what the customer should get back: `credit` (Maxio's default) leaves a service credit and returns no money, `refund` refunds with a credit note, `none` gives nothing.

**Rules**
- This is the only way to reduce a prepaid allocation: prepaid allocations "are always additive", so
  each one "must be destroyed individually" [spec].
- `credit_scheme` decides the money [spec]. `credit`, which is also what Maxio does when the field is
  missing, creates a service credit on the subscription. `refund` issues a refund with a credit note.
  `none` updates the balances and gives nothing back.

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 422 "Credit scheme must be one of credit, refund or none." | `credit_scheme` holds another value | Send `credit`, `refund` or `none` |

**Sources:** [spec] deletePrepaidUsageAllocation

### createUsage
`client.SubscriptionComponents.CreateUsage` · `POST /subscriptions/{subscription_id_or_reference}/components/{component_id}/usages.json` · contract: `map/operations/SubscriptionComponents.md`
**Always:** Send a top-level `uniqueness_token`, unchanged when you resend the same report (R12). After an unknown outcome read `ListUsages` before sending again. Keep a negative `quantity` within the current `unit_balance`.

**Before you call**
- The component is metered or prepaid usage [spec].
- Aggregate: Maxio's advice is one report per customer per day, not one per event [docs].
- Duplicate safety (R12): before the first send, save one long random `uniqueness_token` with your own
  record of the report. It goes at the top level of the body, beside `usage` [docs]. Put your own
  report id in `memo`, so that the report can be found again *(inferred)*.
- The path takes the subscription's id or its `reference`. When a string of digits matches both an id
  and a reference, "the system will prioritize the subscription ID lookup" [spec]. Pass the id, or use
  references that are not all digits; otherwise usage can land on another subscription.

**Rules**
- One component per call. `quantity` accumulates into `unit_balance`. A negative quantity deducts, but
  the balance "has a floor of `0`", so an over-large correction is silently lost [spec].
- Without `price_point_id` the component's default price point is used [spec].
- Metered balances reset at renewal, and no `metered_usage` webhook fires for the reset [docs].
- **Unknown outcome (R11).** Settle it in R11's order. The read-back is `ListUsages` for the component
  and the day, with `until_date` set to the next day (see `ListUsages`), matched by your report id in
  `memo`. The report carries a token. At R11 step 4, send it again with a new token only when
  `ListUsages` shows it did not land [docs] *(the new token is inferred: the 409 spent the old one)*.
  A resend with a new token while the first copy is still running bills the usage twice.

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 422 "Price point: could not be found." | `price_point_id` is not a price point of this component | Send one of the component's price point ids. Whether a handle is accepted here is not stated *(unconfirmed)* |
| 409 `DuplicatePrevention::DuplicateSubmissionError` | A report with this `uniqueness_token` already reached Maxio [docs]. Its outcome is unknown: a 409 never proves success | Follow R11 with `ListUsages` for the component and the day, `until_date` set to the next day. Found: done. Still not found once 120 seconds have passed since the first send: R11 step 4 |

**Sources:** [spec] createUsage · [docs] about-the-api/tips "Reporting Usage" and "Handling Retries
Safely", duplicate-prevention, error-handling "Timeout Limitation", webhooks-reference (metered_usage)

### listUsages
`client.SubscriptionComponents.ListUsages` · `GET /subscriptions/{subscription_id_or_reference}/components/{component_id}/usages.json` · contract: `map/operations/SubscriptionComponents.md`

**Rules**
- This is the read-back after a `CreateUsage` whose outcome is unknown [docs].
- `since_date` and `until_date` each mean midnight at the start of that date [spec]. To read one day,
  send that day as `since_date` and the **next** day as `until_date`. With `until_date` set to today,
  today's usage is missing and a report that landed looks lost.
- `since_id` and `max_id` are inclusive: deduplicate the boundary record.
- Not for quantity-based components [spec].

**Sources:** [spec] listUsages · [docs] about-the-api/duplicate-prevention

### activateEventBasedComponent
`client.SubscriptionComponents.ActivateEventBasedComponent` · `POST /event_based_billing/subscriptions/{subscription_id}/components/{component_id}/activate.json` · contract: `map/operations/SubscriptionComponents.md`

**Rules**
- Call it for every subscription that should be billed. Events are accepted "regardless of component
  activation status", but only activated components are billed at renewal: without it, revenue is
  lost silently.

**Sources:** [spec] activateEventBasedComponent

### recordEvent
`client.SubscriptionComponents.RecordEvent` · `POST /events/{api_handle}.json` · contract: `map/operations/SubscriptionComponents.md`
**Always:** Put a `uniqueness_token` inside the event's `chargify` object (64 characters at most), the same on every resend: a duplicate in the stream is ignored silently, never 409. Events bill only after `ActivateEventBasedComponent`.

**Rules**
- Posts to the events host (`https://events.chargify.com/{subdomain}/events/{api_handle}.json`), not the
  site host [spec].
- Duplicate prevention is different here (R12). The token is `chargify.uniqueness_token`, nested
  inside the event, not at the top level of the body. It is scoped to the stream, a duplicate is
  "silently ignored" and never answered with 409, tokens expire after 31 days, and the value holds 64
  characters at most [spec]. So give each event one token and keep it on every resend. After an
  unknown outcome, send the event again: the answer will not say whether it was a duplicate.
- Send `chargify.timestamp` yourself. It decides the billing period the event is billed in, and when
  it is missing Maxio sets it to the time of arrival [spec], so a late resend could be billed in a
  later period *(inferred)*.
- Events are accepted "regardless of component activation status", but a subscription is billed for
  them only where `ActivateEventBasedComponent` has been called for it [spec].

**Sources:** [spec] recordEvent, Chargify-Ebb, activateEventBasedComponent

### bulkRecordEvents
`client.SubscriptionComponents.BulkRecordEvents` · `POST /events/{api_handle}/bulk.json` · contract: `map/operations/SubscriptionComponents.md`
**Always:** Send at most 1000 events per call. Give each event its own `chargify.uniqueness_token`, unchanged on a resend: duplicates in a stream are ignored silently, never 409.

**Rules**
- At most 1000 events per call; more answers 422 [spec]. Same host, token and billing rules as
  `RecordEvent`.
- After an unknown outcome send the whole batch again with the same tokens: the events that already
  arrived are ignored *(inferred from the per-event token)*.

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 422 | More than 1000 events in the request (message not documented) | Split the batch and send the parts with the same tokens |

**Sources:** [spec] bulkRecordEvents, Chargify-Ebb

### bulkResetSubscriptionComponentsPricePoints
`client.SubscriptionComponents.BulkResetSubscriptionComponentsPricePoints` · `POST /subscriptions/{subscription_id}/price_points/reset.json` · contract: `map/operations/SubscriptionComponents.md`
**Always:** This resets every component on the subscription to its current default price point, "even ones that have not been allocated yet". To move only some components use `BulkUpdateSubscriptionComponentsPricePoints`.

**Rules**
- It takes no list of components: all of them move to the current default [spec]. A price point set
  for one subscriber on purpose is lost with the rest *(inferred)*.
- To reset or move chosen components, use `BulkUpdateSubscriptionComponentsPricePoints`; there
  `"_default"` as the price point resets one component (D9).

**Sources:** [spec] bulkResetSubscriptionComponentsPricePoints,
bulkUpdateSubscriptionComponentsPricePoints

### listSubscriptionComponents
`client.SubscriptionComponents.ListSubscriptionComponents` · `GET /subscriptions/{subscription_id}/components.json` · contract: `map/operations/SubscriptionComponents.md`

**Rules**
- Returns archived components still on the subscription; keep them in any local catalog cache.

**Sources:** [spec] listSubscriptionComponents
