# Subscription Products: provider notes

Plan changes. Which call fits which change is `../decisions.md` D13: an immediate change through
`updateSubscription` is **not prorated**; only a migration prorates. An operation of this group that
has no section here has no provider notes (see `../index.json`).

### migrateSubscriptionProduct
`client.subscriptionProducts.migrateSubscriptionProduct` · `POST /subscriptions/{subscription_id}/migrations.json` · contract: `map/operations/subscription-products.md`
**Always:** Send `preserve_period` explicitly: `true` prorates and keeps the billing date; omitted resets the period and charges in full (D13). Preview first (`trialing`: D13). One random `uniqueness_token` per change, never computed (R12).

**Before you call**
- The subscription is `active` or `trialing` [spec], and the target is not its current product (D13):
  migrating to the current product is one of "the most common ways that a migration can fail" [spec].
- Run `previewSubscriptionProductMigration` with the same `migration` fields and show the amounts. The
  preview has its own request shape, so reuse the field values, not the request itself. For a `trialing`
  subscription the preview may refuse *(unconfirmed)*: then migrate without the amounts and say so (D13).
- Decide `preserve_period`.

**Rules**
- `preserve_period` omitted or `false` **resets the billing period to today and charges the full
  price of the new product**. `preserve_period: true` leaves the billing period as it is and issues a
  prorated charge [spec]. For a prorated mid-period upgrade or downgrade that keeps the billing date,
  send `true` (D13).
- A reset migration is not the new price on top of what was already paid. Maxio's migrations page says
  a credit for the unused part of the current plan is applied beside the full charge for the new one
  [docs]. Take the amounts from the preview; do not compute them.
- `preserve_period` has two homes: directly in `migration`, and as `proration.preserve_period`, the
  "alternative to sending preserve_period as a direct attribute" [spec]. Send it in one place. If both
  are present they must agree: the spec does not say which one wins *(unconfirmed)*.
- Crossing product families drops components, and coupons "cannot migrate" [spec]; re-create them
  yourself.
- Without a price point the target's default is used.
- For `trial_ended`, cancel, change the product, then reactivate; migrating it is allowed but not
  recommended [spec].
- A migration can charge the payment method on file at once [docs]. Send one `uniqueness_token` at the
  top level of the body, beside `migration`, kept on every resend (R12). Mint it at random: one computed
  from the change repeats when the change is repeated, and the repeat answers 409 (R12). After an unknown outcome the
  read-back is `readSubscription`: is `product` already the target? It is not by a unique reference,
  so a migration still not settled after a 409 is settled from webhooks or by hand, never sent again
  automatically (R11 step 4).

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 422 "No credit card was on file for the …" | An upgrade charge is due and there is no payment method | Add a payment method (D6), then migrate again |
| 422 "This subscription is not eligible for a prorated migration" | `preserve_period: true` cannot be honoured. Maxio's migrations page names one cause: the two plans have different billing intervals [docs]. Other causes are not documented | Check the preview. Migrate without `preserve_period` only when a reset period and a full charge are what the user wants |
| 422 Invalid Product | The target is not a product of the site, or it is the subscription's current product *(inferred)* | Choose a different product or price point |
| 422 with an `action_link` | 3-D Secure is required [spec]. This is not a decline | Send the customer to the link. Do not resend |

**Sources:** [spec] migrateSubscriptionProduct, Subscription-Product-Migration, Proration · [docs]
Maxio help "Product Changes and Migrations"

### previewSubscriptionProductMigration
`client.subscriptionProducts.previewSubscriptionProductMigration` · `POST /subscriptions/{subscription_id}/migrations/preview.json` · contract: `map/operations/subscription-products.md`

**Rules**
- Send the same `migration` fields you will send to `migrateSubscriptionProduct`. The answer is what
  that migration would charge and credit, in integer cents (R4).
- The preview follows the migration's own rules. Since 2022-12-07 it also preserves the period for
  subscriptions with allocated components, so that the preview "matches the actual migration"
  [announcement].
- A `proration_date` previews a later moment; it must fall within the current billing period [spec].
- State: the migration itself accepts `active` or `trialing` [spec]. The preview's only documented
  rejection is "Subscription must be active", and the spec does not say whether a `trialing`
  subscription can be previewed *(unconfirmed)*. Check `state` yourself before either call. A preview
  rejection for a `trialing` subscription does not prove that the migration would fail: go on as D13
  says.

**When it fails**
| Status · message | Cause | Do |
|---|---|---|
| 422 "Subscription must be active" | The subscription is not in a state the preview accepts. Whether it accepts `trialing` is not stated *(unconfirmed)* | Read `state`. `active`: check the request. `trialing`: the amounts cannot be previewed, and the plan change is not refused. Migrate and report that no amounts were previewed, unless the user asked to see them first (D13). Any other state: no plan change until the subscription is brought back (D12) |

**Sources:** [spec] previewSubscriptionProductMigration, migrateSubscriptionProduct · [announcement]
2022-12-07 migration preview
