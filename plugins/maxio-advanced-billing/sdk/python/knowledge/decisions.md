# Maxio Advanced Billing: decisions

**Contents.** Read the sections you need, not the whole file.

- D1 · Identify the customer at signup (exactly one source)
- D2 · Supply the payment method at signup (exactly one source, or none)
- D3 · Choose the collection method (always send it)
- D4 · Start a subscription later
- D5 · Show the price before signup
- D8 · Several subscriptions for one payer
- D6 · Change a subscriber's payment method
- D7 · Remove a payment profile
- D9 · Change a price
- D10 · Choose a component kind
- D17 · Choose a pricing scheme
- D18 · Overlapping catalog lookups
- D11 · Cancel now, at period end, or on a date
- D12 · Bring a subscription back
- D13 · Change a subscription's plan
- D14 · Record quantity, usage or events
- D15 · Which money operation (Relationship Invoicing)
- D16 · Which invoice operation a status allows
- D19 · Keep subscription state current in your app
- D20 · Words the user says that map to a different API object

Where Maxio offers more than one way to do something, the choice changes what is charged, who is
charged, or when. Pick the row that matches the user's intent; if the intent is unclear at one of these
forks, ask before writing code. Read the item your task touches, not the whole file.

Each item ends with its sources, tagged as in `rules.md`. A cell marked *(inferred)* or *(unconfirmed)*
is not settled by those sources. Per-operation detail is in `operations/<page>.md`.

---

## Signing up

### D1 · Identify the customer at signup (exactly one source)
| Need | Use | Why |
|---|---|---|
| Your app has a stable user id | `customer_reference` (the customer's `reference`) | Maxio's own advice: map your user to a customer by reference |
| You stored the Maxio customer id | `customer_id` | Exact, no lookup |
| The lookup below just answered "not there" | `customer_attributes`, with your `reference` in it | Creates the customer in the same call |
| A second plan for an existing customer | `customer_reference` or `customer_id`, plus `payment_profile_id` to reuse the card | `customer_attributes` again creates a second customer *(inferred)* |

Look the customer up first (`lifecycles.md` L2 step 4), even when the task says "new customer": a
resend of the same signup meets the customer the first attempt created. Email is not unique and must
never be the key *(inferred: `reference` is the only uniqueness rule the spec states)*.

Sources: [spec] createSubscription, Create-Subscription (`customer_id`, `customer_reference`), createCustomer · [docs] basic-concepts/subscription-signup "Multiple Subscriptions"

### D2 · Supply the payment method at signup (exactly one source, or none)
| Need | Use | Watch out |
|---|---|---|
| Card or bank details collected in your UI | `credit_card_attributes` / `bank_account_attributes` holding the `chargify_token` and no card or bank fields | Tokenize with Maxio.js (rules.md R15) |
| Customer already has a stored profile | `payment_profile_id` | Must belong to that customer |
| The merchant bills by invoice | No payment fields, with the invoice method from D3 | Nothing is collected; choose it by intent, never to clear a 422 (rules.md R14) |
| Nothing is due at signup (a trial, a free plan) | No payment fields, `automatic` *(inferred)* | What happens at trial end is `lifecycles.md` L4 |
| Migrating profiles already in your gateway | `vault_token` + `current_vault` | Import only. `current_vault` must name the site's real gateway (`stripe_connect`, not `stripe`) |
| Raw card number on your server | The card fields themselves | Only if the merchant is PCI compliant |

Sources: [spec] Create-Subscription (`payment_profile_id`, `credit_card_attributes`), Payment-Profile-Attributes (`chargify_token`, `vault_token`, `current_vault`) · [docs] basic-concepts/subscription-signup "API" · [announcement] 2021-12-16 current vault validation

### D3 · Choose the collection method (always send it)
| Site (`read_site`) | How the customer pays | `payment_collection_method` |
|---|---|---|
| Any | By card or bank account, charged automatically | `automatic`, plus a payment source (D2) |
| Any | Nothing is due at signup (a trial, a free plan) | `automatic`, with no payment source *(inferred)* |
| Relationship Invoicing | The merchant sends invoices; the customer pays them | `remittance`: the customer is not charged automatically, and the payment is recorded when it arrives. That it starts active with an open invoice is *(inferred)* |
| Relationship Invoicing | The customer pre-funds a balance that is drawn down | `prepaid` (the spec's example sends `prepaid_configuration` with it; whether it is required is *(unconfirmed)*). When the balance runs out the state is `suspended` |
| Legacy Statements | The merchant sends invoices | `invoice` |

Send it on every signup, and ask when the task does not say how the customer pays (rules.md R14).

Sources: [spec] Collection-Method, Site, Subscription-State (`suspended`), createSubscription example "Prepaid Subscription" · [docs] basic-concepts/subscription-signup "Payment Methods" · [announcement] 2021-11-05 payment collection validation

### D4 · Start a subscription later
| Need | Field | Effect |
|---|---|---|
| Start now, with trial and setup fee | (none) | Charged at create |
| Start on a known future date, keeping trial and setup fee | `initial_billing_at` | `awaiting_signup` until then; a failed payment at that date cancels it |
| Start date not yet known | `defer_signup: true` | Set `initial_billing_at` later with `update_subscription` |
| Import an existing customer mid-cycle | `next_billing_at` (+ `previous_billing_at`) | **No trial, no setup fee, no charge at signup** |
| Bill on a fixed day of the month | `calendar_billing` (`snap_day` 1–28 or `end`) | Not with `next_billing_at`; `calendar_billing_first_charge` decides the first charge |

Sources: [spec] Create-Subscription (`initial_billing_at`, `defer_signup`, `next_billing_at`, `previous_billing_at`, `calendar_billing_first_charge`), Calendar-Billing

### D5 · Show the price before signup
| Need | Operation | Note |
|---|---|---|
| Price, next billing date and tax for a cart | `preview_subscription` (same body as create) | Creates nothing |
| A quote shaped as an invoice | `preview_signup_proforma_invoice` | Relationship Invoicing only; not persisted |
| A persisted quote document | `create_signup_proforma_invoice` | Relationship Invoicing only; set `customer_id` |

Sources: [spec] previewSubscription, previewSignupProformaInvoice, createSignupProformaInvoice

### D8 · Several subscriptions for one payer
| Need | Operation |
|---|---|
| Several new subscriptions in one call, one payment profile | `signup_with_subscription_group` |
| One new subscription into an existing group or customer hierarchy | `create_subscription` with `group` (it can change who pays for the whole hierarchy) |
| Group subscriptions that already exist | `create_subscription_group` |

Sources: [spec] signupWithSubscriptionGroup, createSubscriptionGroup, Group-Settings · [docs] basic-concepts/subscription-signup "Subscription in a Subscription Group", "Billing Parameters for Group and Customer Hierarchy Subscriptions"

---

## Payment methods

### D6 · Change a subscriber's payment method
| Need | Operation | Why |
|---|---|---|
| New card for a past-due subscriber, collect now | `update_subscription` with card attributes | Updating the profile does not collect; this call does (rules.md R11) |
| New card, nothing owed | `create_payment_profile`, then `change_subscription_default_payment_profile` | A new profile is never the default automatically |
| Switch to another stored profile | `change_subscription_default_payment_profile` | Whether it collects a past-due balance is *(unconfirmed)* |
| Fix name or address on the same card | `update_payment_profile` | On major gateways the card number is ignored |
| Customer does it themselves | Billing Portal or the self-service page | No PCI scope for you |

Sources: [spec] updateSubscription, updatePaymentProfile, createPaymentProfile, changeSubscriptionDefaultPaymentProfile · [docs] basic-concepts/subscription-signup "Updating Payment Details"

### D7 · Remove a payment profile
| Need | Operation | Effect |
|---|---|---|
| Profile used by no subscription | `delete_unused_payment_profile` | 422 if it is in use |
| Profile used by a subscription | `delete_subscriptions_payment_profile` | Removed from **all** the customer's subscriptions; set a new default |

Sources: [spec] deleteUnusedPaymentProfile, deleteSubscriptionsPaymentProfile

---

## Catalog and pricing

### D9 · Change a price
| Who should pay the new price | Operation |
|---|---|
| New signups only | Create a new price point, then promote it to default (existing subscribers stay put) |
| Everyone on the price point now | `update_product_price_point` / `update_component_price_point` (that the edit reaches existing subscribers is *(inferred)*; mid-period proration uses the component's current price) |
| Existing subscribers' components → another price point | `bulk_update_subscription_components_price_points` (`"_default"` resets) |
| One existing subscriber's plan → another price point of the **same** plan | `update_subscription` with the price point (not prorated; the new price starts at the next period). A migration to the subscription's current product is a common failure, so whether `migrate_subscription_product` does this is *(unconfirmed)* |
| One existing subscriber's plan → another plan and price point | `migrate_subscription_product` with the price point (D13) |
| One subscriber only | `custom_price` on the subscription (max 30 custom price points) |

Never use `update_product` to change a price: it creates and promotes a new default price point.

Sources: [spec] updateProduct, promoteComponentPricePointToDefault, bulkUpdateSubscriptionComponentsPricePoints, updateSubscription "Product Change", migrateSubscriptionProduct "Failed Migrations", allocateComponent, Subscription-Custom-Price

### D10 · Choose a component kind
| Need | Kind | Quantity reaches it via |
|---|---|---|
| Usage that resets each period (API calls, minutes) | metered | `create_usage` |
| Seats or licences that persist | quantity-based, recurring | `allocate_component` |
| A one-time fee | quantity-based, `recurring: false` *(inferred: the field has no description)* | `allocate_component` |
| A flat recurring add-on | on/off | allocate 1 or 0 |
| Customer prepays a block of units | prepaid usage | allocate to buy, `create_usage` to consume |
| Usage computed from streamed events | event-based | events host + `activate_event_based_component` |

Choose on purpose: the update operations take no kind, so a component's kind cannot be changed later
*(inferred)*.

Sources: [spec] createMeteredComponent, createQuantityBasedComponent, allocateComponent, listUsages, Update-Component · [docs] basic-concepts/product-catalog "Usage/Allocation"

### D17 · Choose a pricing scheme
| Need | Scheme |
|---|---|
| Same price for every unit | `per_unit` |
| A flat fee per band ("$500 for up to 10 seats"): the bracket `unit_price` is the band's price | `stairstep` |
| Each unit priced by the bracket it falls in | `tiered` *(inferred)* |
| All units priced at the bracket the total reaches | `volume` *(unconfirmed: not defined in Maxio's sources here; confirm with the user)* |

Sources: [docs] basic-concepts/hybrid-pricing "Creating the Component" (stairstep) · [spec] Pricing-Scheme

### D18 · Overlapping catalog lookups
| Need | Operation |
|---|---|
| Product by handle | `read_product_by_handle` (`read_product` is id-only) |
| Component by handle | `find_component` |
| A code a customer typed | `validate_coupon` (pass the family if not the default) |
| Add coupon subcodes | `create_coupon_subcodes` (`update_coupon_subcodes` deletes all existing first) |
| Coupons on a subscription | `apply_coupons_to_subscription` with codes in the body (a `code` query parameter replaces all existing codes) |

Sources: [spec] readProductByHandle, findComponent, validateCoupon, updateCouponSubcodes, applyCouponsToSubscription

---

## After signup

### D11 · Cancel now, at period end, or on a date
| Need | Operation |
|---|---|
| Stop billing now | `cancel_subscription` with no schedule parameters |
| Cancel at the end of the current period | `initiate_delayed_cancellation` (not while `past_due`) |
| Cancel on a specific date | `cancel_subscription` with `scheduled_cancellation_at` (site feature; not for prepaid) |
| Undo a pending end-of-period cancel | `cancel_delayed_cancellation` |

- **Prepaid:** cancelling a prepaid subscription refunds the remaining prepaid balance by default
  (`refund_prepayment_account_balance`, default `true`). Send `false` to keep it, and make the choice on
  purpose. The option needs the site's Schedule Subscription Cancellation feature; what a site without
  it does with the balance is *(unconfirmed)*.
- **The `cancel_at_end_of_period` option on `cancel_subscription`:** its own description says it cancels
  at the end of the period. It is one of the schedule options, which work only on sites with the Schedule
  Subscription Cancellation feature [spec] (`read_site`: `schedule_subscription_cancellation_enabled`);
  what a site without the feature does with it is *(unconfirmed)*. `initiate_delayed_cancellation` needs
  no such feature, so use it for a cancel at period end.
- **Proof that a delayed cancellation landed:** `initiate_delayed_cancellation` answers with a message
  only. Read the subscription back: `cancel_at_end_of_period: true` is the proof, and the subscription keeps
  its current state until the period ends. `delayed_cancel_at` tells you when it will cancel; do not use it
  alone as the test *(inferred: the spec ties `cancel_at_end_of_period` to these two operations and
  describes `delayed_cancel_at` only as a timestamp)*.

Sources: [spec] cancelSubscription, Cancellation-Options, initiateDelayedCancellation, cancelDelayedCancellation, Subscription (`cancel_at_end_of_period`, `delayed_cancel_at`)

### D12 · Bring a subscription back
| Situation | Operation |
|---|---|
| `on_hold` | `resume_subscription` (after the original renewal date it charges now) |
| `canceled`, keep the old billing date or do nothing | `reactivate_subscription` with `resume: {"require_resume": true}` |
| `canceled`, fresh period is fine | `reactivate_subscription` without `resume` (charges a new period) |
| `trial_ended` | `reactivate_subscription` for a new period. Whether it can also be resumed is *(unconfirmed)*: the spec shows a resume scenario for it, and Maxio's help page says it is not eligible to resume |
| `unpaid` | `reactivate_subscription` *(unconfirmed: its 422 text lists "Unpaid" as allowed, its list of states that work does not)* |
| `suspended` | Apply a prepayment; `create_prepayment` is the operation for that *(inferred)* |
| `past_due`, new card, collect now | `update_subscription` with card attributes |
| `past_due`, card fixed, collect now | `retry_subscription` |
| `past_due`, collect one open invoice from a stored profile | `record_payment_for_invoice` with `type: payment` and `payment_profile_id`: it charges that profile *(inferred: the spec says only that the profile is "to be used for the payment")* |
| `past_due`, paid offline | `record_payment_for_invoice` with `type: external` (the default): it records money received elsewhere and charges nothing *(inferred)* |
| Stop dunning, keep the subscription | `cancel_dunning` (collects nothing *(inferred)*) |

Every row that can charge follows rules.md R11.

Sources: [spec] resumeSubscription, reactivateSubscription, retrySubscription, updatePaymentProfile, cancelDunning, Subscription-State (`suspended`), Invoice-Payment-Type, Create-Invoice-Payment · [docs] Maxio help "Reactivating and Resuming"

### D13 · Change a subscription's plan
| Need | Operation | Money |
|---|---|---|
| Upgrade or downgrade now, prorated, keep the billing date | `migrate_subscription_product` with `preserve_period: true` (preview first; `trialing`: see below) | Prorated charge or credit |
| Switch at the next renewal | `update_subscription` with `product_change_delayed: true` | New price from renewal |
| Switch now, new price from next period | `update_subscription` with the product | **Not prorated**: the new plan applies at once and its price is first charged at the next period, so an upgrade is free until renewal *(the consequence is inferred)* |
| Restart the period on the new plan | `migrate_subscription_product` (default) | **Full price now**, period resets |

A migration needs the subscription in `active` or `trialing`. Migrating to the product it is already on
is one of "the most common ways that a migration can fail", so target another product; whether a
migration can change only the price point is *(unconfirmed)* (D9).

Preview a migration first. Whether the preview accepts a `trialing` subscription is *(unconfirmed)*: its
only documented rejection is "Subscription must be active". So for a `trialing` subscription a refused
preview is not a refused plan change. Go on to the migration and say in the result that no amounts were
previewed. Stop before migrating only when the user asked to see the amounts first.

Sources: [spec] updateSubscription "Product Change", "Delayed Product Change", migrateSubscriptionProduct, Subscription-Product-Migration (`preserve_period`)

### D14 · Record quantity, usage or events
| Component kind | Call | Quantity means |
|---|---|---|
| quantity-based, on/off | `allocate_component` / `allocate_components` | The **new total**, not the change: the call "sets the current allocated quantity". A call that changes nothing is rejected with 422 *(cause inferred from the message)* |
| prepaid usage | allocate to buy, `create_usage` to consume, delete allocations to reduce | Each allocation **adds** units: prepaid allocations "are always additive" |
| metered | `create_usage` | An amount added to the period's balance |
| event-based | `activate_event_based_component`, then `record_event` / `bulk_record_events` | Computed by Maxio from the events |

Sources: [spec] allocateComponent, deletePrepaidUsageAllocation, createUsage, activateEventBasedComponent · [docs] basic-concepts/product-catalog "Usage/Allocation"

### D15 · Which money operation (Relationship Invoicing)
| Need | Operation |
|---|---|
| Bill a one-off amount | `create_invoice`. It creates an `open` invoice by default. The spec does not say the payment method is charged when the invoice is created *(unconfirmed)*: read the invoice back and never report "charged" from the 201. It replaces the legacy charges endpoint in Maxio's older docs *(inferred)* |
| Collect an open invoice from a stored payment profile | `record_payment_for_invoice` with `type: payment` and `payment_profile_id` (a charge to that profile *(inferred)*) |
| Record a payment made outside Maxio | `record_payment_for_invoice` with `type: external` (the default) / `record_payment_for_subscription`. Never send `type: payment` for money already taken elsewhere: it would charge the profile again *(inferred)* |
| Goodwill credit against future invoices | `issue_service_credit` |
| Customer funds an account balance | `create_prepayment` (only `credit_card_on_file` charges a card) |
| Money back for a paid invoice | `refund_invoice` (`external: true` returns nothing) |
| Unused prepayment back | `refund_prepayment` |
| What the customer owes or holds | `read_account_balances` |

Sources: [spec] createInvoice, Create-Invoice-Status, recordPaymentForInvoice, Invoice-Payment-Type, Create-Invoice-Payment, recordPaymentForSubscription, issueServiceCredit, createPrepayment, Refund-Invoice, refundPrepayment, readAccountBalances

### D16 · Which invoice operation a status allows
| Status | Need | Operation |
|---|---|---|
| `draft` (ad hoc) | Discard / edit | `delete_invoice` / `update_invoice` (a `coupons` key replaces all discounts) |
| `draft`, `pending` | Finalize | `issue_invoice`. Automatic subscription: payment is attempted, so choose `on_failed_payment` (the default leaves the invoice `open`). Remittance subscription: nothing is attempted, and `on_failed_payment` is rejected if sent |
| `open` | Collect it | A payment per D15 |
| `open`, `canceled`, `pending` (not consolidated) | Cancel the debt | `void_invoice` |
| `paid` | Money back | `refund_invoice` (with `void_invoice: true`, a full refund that applies no credit also voids it) |
| `canceled` | Make it due again | `reopen_invoice` |
| `processing` | A payment was started and is not yet confirmed | Wait and read it again; no operation is documented for this status *(unconfirmed)* |

Sources: [spec] deleteInvoice, updateInvoice, issueInvoice, voidInvoice, Refund-Invoice, reopenInvoice, Invoice-Status · [docs] Maxio help "Advanced Billing Invoices Overview" (`processing`)

---

## Integration architecture

### D19 · Keep subscription state current in your app
| Need | Approach |
|---|---|
| Gate a customer's access on each request | A local copy of state, updated from webhooks (re-read the resource on each event, rules.md R20) |
| List the subscriptions that have access now | `list_subscriptions`, paged, with no `state` filter, keeping the rows whose own `state` has access in `lifecycles.md` L3 (rules.md R8, R9) |
| Reconcile drift | `list_subscriptions` with `date_field=updated_at` and a window; a full pass "usually no more than once a month" |
| Bulk extract | Export jobs (`export_subscriptions`, ...) instead of paging |

Scope a list to one plan only when the user names that plan (D20).

Sources: [docs] about-the-api/tips "Getting Subscription States", "Synchronizing Your Database", "Downloading Bulk Data" · [spec] listSubscriptions, Subscription-State-Filter

### D20 · Words the user says that map to a different API object
| User says | API object | Operations |
|---|---|---|
| "Plan" (new Catalog UI) | product | products, product price points, `migrate_subscription_product` |
| "Product", "add-on" (new Catalog UI) | component | components, `allocate_component`, `create_usage` |
| "The product", "our product", with no plan named | No filter: every plan on the site *(inferred)* | Do not scope a list or report to one plan, and never invent a setting to pick one. Ask if one plan is meant |
| "Pause" | hold → state `on_hold` | `pause_subscription` |
| "Resume" an on-hold subscription | `resume_subscription` | not `reactivate_subscription`'s `resume` option |

Sources: [announcement] 2026 "NEW Catalog Experience and Terminology" · [spec] pauseSubscription, resumeSubscription, reactivateSubscription
